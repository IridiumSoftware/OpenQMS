"""Standards-and-jurisdictions registry.

Implements OQ-014: a versioned, immutable catalog of supported standards
(with metadata) and jurisdictions (with their applicable-standards sets).
CLI arguments and module manifests are validated against the registry;
unregistered standards or jurisdictions raise rather than silently
filtering to empty resolution.

Files live at `<repo>/registry/standards.yaml` and
`<repo>/registry/jurisdictions.yaml`. Git history is the version;
immutability comes from the engine treating the loaded registry as
read-only.
"""

from __future__ import annotations

from dataclasses import dataclass
from pathlib import Path

import yaml


DEFAULT_REGISTRY_ROOT = Path("registry")


@dataclass(frozen=True)
class StandardEntry:
    id: str
    name: str
    publisher: str
    edition: str
    kind: str
    license_kind: str
    aliases: tuple[str, ...]


@dataclass(frozen=True)
class JurisdictionEntry:
    id: str
    name: str
    region: str
    applicable_standards: tuple[str, ...]


@dataclass(frozen=True)
class Registry:
    standards: tuple[StandardEntry, ...]
    jurisdictions: tuple[JurisdictionEntry, ...]

    def resolve_standard(self, name_or_alias: str) -> StandardEntry:
        for s in self.standards:
            if s.id == name_or_alias or name_or_alias in s.aliases:
                return s
        raise KeyError(
            f"Standard not in registry: {name_or_alias!r}. "
            f"Registered ids: {sorted(s.id for s in self.standards)}"
        )

    def has_standard(self, name_or_alias: str) -> bool:
        try:
            self.resolve_standard(name_or_alias)
        except KeyError:
            return False
        return True

    def canonical_standard(self, name_or_alias: str) -> str:
        return self.resolve_standard(name_or_alias).id

    def resolve_jurisdiction(self, id_: str) -> JurisdictionEntry:
        for j in self.jurisdictions:
            if j.id == id_:
                return j
        raise KeyError(
            f"Jurisdiction not in registry: {id_!r}. "
            f"Registered ids: {sorted(j.id for j in self.jurisdictions)}"
        )

    def has_jurisdiction(self, id_: str) -> bool:
        try:
            self.resolve_jurisdiction(id_)
        except KeyError:
            return False
        return True


def load_registry(root: Path | None = None) -> Registry:
    """Load the registry from ``<root>/standards.yaml`` + ``<root>/jurisdictions.yaml``.

    Performs a cross-check at load time: every jurisdiction's
    ``applicable_standards`` entries must resolve in the standards
    registry. Inconsistent registries raise ``ValueError``.
    """
    root = root or DEFAULT_REGISTRY_ROOT
    standards_path = root / "standards.yaml"
    jurisdictions_path = root / "jurisdictions.yaml"

    if not standards_path.exists():
        raise FileNotFoundError(
            f"Standards registry not found: {standards_path}"
        )
    if not jurisdictions_path.exists():
        raise FileNotFoundError(
            f"Jurisdictions registry not found: {jurisdictions_path}"
        )

    standards_data = yaml.safe_load(standards_path.read_text()) or {}
    jurisdictions_data = yaml.safe_load(jurisdictions_path.read_text()) or {}

    standards = tuple(
        _parse_standard(s) for s in (standards_data.get("standards") or [])
    )
    jurisdictions = tuple(
        _parse_jurisdiction(j)
        for j in (jurisdictions_data.get("jurisdictions") or [])
    )

    registry = Registry(standards=standards, jurisdictions=jurisdictions)
    dangling = _cross_check_jurisdictions(registry)
    if dangling:
        raise ValueError(
            "Jurisdictions reference standards not present in the "
            f"standards registry: {list(dangling)}"
        )
    return registry


def _parse_standard(data: dict) -> StandardEntry:
    required = ("id", "name", "publisher", "edition", "kind", "license_kind")
    missing = [k for k in required if k not in data]
    if missing:
        raise ValueError(
            f"Standard registry entry missing fields {missing}: "
            f"{data.get('id', '<unknown>')}"
        )
    aliases = data.get("aliases") or []
    if not isinstance(aliases, list):
        raise ValueError(
            f"Standard 'aliases' must be a list: {data['id']}"
        )
    return StandardEntry(
        id=str(data["id"]),
        name=str(data["name"]),
        publisher=str(data["publisher"]),
        edition=str(data["edition"]),
        kind=str(data["kind"]),
        license_kind=str(data["license_kind"]),
        aliases=tuple(str(a) for a in aliases),
    )


def _parse_jurisdiction(data: dict) -> JurisdictionEntry:
    required = ("id", "name", "region")
    missing = [k for k in required if k not in data]
    if missing:
        raise ValueError(
            f"Jurisdiction registry entry missing fields {missing}: "
            f"{data.get('id', '<unknown>')}"
        )
    applicable = data.get("applicable_standards") or []
    if not isinstance(applicable, list):
        raise ValueError(
            f"Jurisdiction 'applicable_standards' must be a list: "
            f"{data['id']}"
        )
    return JurisdictionEntry(
        id=str(data["id"]),
        name=str(data["name"]),
        region=str(data["region"]),
        applicable_standards=tuple(str(s) for s in applicable),
    )


def _cross_check_jurisdictions(registry: Registry) -> tuple[str, ...]:
    dangling: list[str] = []
    for j in registry.jurisdictions:
        for s in j.applicable_standards:
            if not registry.has_standard(s):
                dangling.append(f"{j.id} -> {s}")
    return tuple(sorted(dangling))


@dataclass(frozen=True)
class RegistryValidationReport:
    """Output of cross-checking a Module against the registry."""

    module: str
    invariant_holds: bool
    unregistered_module_standards: tuple[str, ...]
    unregistered_clause_standards: tuple[str, ...]


def validate_module_against_registry(module, registry: Registry) -> RegistryValidationReport:
    """Check that every standard the module references is in the registry.

    Two surfaces are checked:

    - the module's ``standards:`` list — each entry must resolve;
    - every clause's ``standard:`` field — each must resolve.

    A module passes iff both surfaces are clean.
    """
    unregistered_module = sorted(
        s for s in module.standards if not registry.has_standard(s)
    )
    unregistered_clauses = sorted(
        {
            c.standard
            for c in module.clauses
            if not registry.has_standard(c.standard)
        }
    )
    return RegistryValidationReport(
        module=module.name,
        invariant_holds=(
            not unregistered_module and not unregistered_clauses
        ),
        unregistered_module_standards=tuple(unregistered_module),
        unregistered_clause_standards=tuple(unregistered_clauses),
    )
