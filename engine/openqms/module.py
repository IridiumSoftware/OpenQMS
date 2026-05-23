"""Module loading and composition.

``load_module`` parses a ``module.yaml`` manifest into the Module type.
``compose`` unions multiple modules into one — implementing OQ-011 (modules
compose under union; deduplication preserves the invariant) and OQ-012
(cross-cutting overlays compose with vertical modules).
"""

from __future__ import annotations

from pathlib import Path

import yaml

from .types import ArtifactTemplate, Clause, Module


DEFAULT_MODULES_ROOT = Path("modules")


def load_module(name_or_path: str, modules_root: Path | None = None) -> Module:
    """Load a regulatory module.

    If ``name_or_path`` is a path to an existing file, load it directly.
    Otherwise, treat it as a module name and look for
    ``<modules_root>/<name>/module.yaml``. ``modules_root`` defaults to
    ``Path("modules")`` relative to cwd.
    """
    root = modules_root or DEFAULT_MODULES_ROOT
    path = Path(name_or_path)

    if path.is_file():
        module_file = path
    else:
        candidate = root / name_or_path / "module.yaml"
        if candidate.exists():
            module_file = candidate
        elif path.exists():
            module_file = path
        else:
            raise FileNotFoundError(
                f"Module not found. Tried: {candidate}, {path}"
            )

    data = yaml.safe_load(module_file.read_text()) or {}
    return _parse_module(data)


def _parse_module(data: dict) -> Module:
    name = data.get("name")
    if not name:
        raise ValueError("Module manifest missing required field 'name'.")

    clauses_raw = data.get("clauses") or []
    if not isinstance(clauses_raw, list):
        raise ValueError("Module manifest 'clauses' must be a list.")

    templates_raw = data.get("templates") or []
    if not isinstance(templates_raw, list):
        raise ValueError("Module manifest 'templates' must be a list.")

    standards_raw = data.get("standards") or []
    if not isinstance(standards_raw, list):
        raise ValueError("Module manifest 'standards' must be a list.")

    return Module(
        name=str(name),
        version=str(data.get("version", "0.0.0")),
        standards=tuple(str(s) for s in standards_raw),
        clauses=tuple(_parse_clause(c) for c in clauses_raw),
        templates=tuple(_parse_template(t) for t in templates_raw),
    )


def _parse_clause(c: dict) -> Clause:
    missing = [k for k in ("id", "standard", "section", "summary") if k not in c]
    if missing:
        raise ValueError(
            f"Clause missing required fields {missing}: "
            f"{c.get('id', '<unknown>')}"
        )
    gap = c.get("gap_note")
    return Clause(
        id=str(c["id"]),
        standard=str(c["standard"]),
        section=str(c["section"]),
        summary=str(c["summary"]).strip(),
        gap_note=str(gap).strip() if gap else None,
    )


def _parse_template(t: dict) -> ArtifactTemplate:
    missing = [k for k in ("path", "name") if k not in t]
    if missing:
        raise ValueError(
            f"Template missing required fields {missing}: "
            f"{t.get('path', '<unknown>')}"
        )
    addresses = t.get("addresses") or []
    if not isinstance(addresses, list):
        raise ValueError(
            f"Template 'addresses' must be a list: {t['path']}"
        )
    return ArtifactTemplate(
        path=str(t["path"]),
        name=str(t["name"]),
        addresses=tuple(str(a) for a in addresses),
    )


def compose(
    modules: list[Module],
    name: str = "composed",
    version: str = "0.0.0",
) -> Module:
    """Compose multiple modules into one.

    Implements OQ-011 (modules compose under union; deduplication preserves
    the invariant) and OQ-012 (cross-cutting overlays compose with vertical
    modules — mechanically the same union operation).

    Composition rules:

    - **Clauses** union by ``id``. If two modules declare the same clause ID
      with the same content, the duplicate is silently absorbed (harmless
      dedup). If two modules declare the same clause ID with *different*
      content, ``ValueError`` is raised — clauses are facts about a
      standard and modules cannot disagree about them.
    - **Templates** union by ``path``. If two modules declare the same
      template path, their ``addresses`` are unioned (deduped, first-seen
      order preserved). The template ``name`` from the first module that
      declared the path wins.
    - **Standards** are concatenated and deduped (first-seen order).
    - **Empty input** raises ``ValueError``. **Single-element input** is
      returned unchanged so callers can compose unconditionally.

    The composite's own clauses-to-templates invariant (OQ-001 / OQ-013)
    is NOT enforced by ``compose`` itself — call ``validate(composite)`` to
    check it. An overlay module that has clauses but no own-templates can
    legitimately rely on a vertical module's templates to address its
    clauses once composed.
    """
    if not modules:
        raise ValueError("compose() requires at least one module")

    if len(modules) == 1:
        return modules[0]

    clause_by_id: dict[str, Clause] = {}
    for module in modules:
        for clause in module.clauses:
            existing = clause_by_id.get(clause.id)
            if existing is None:
                clause_by_id[clause.id] = clause
            elif existing != clause:
                raise ValueError(
                    f"Clause '{clause.id}' conflicts across modules: "
                    f"differs in content between modules '{module.name}' "
                    f"and an earlier module. Cannot compose."
                )

    template_addresses: dict[str, list[str]] = {}
    template_names: dict[str, str] = {}
    template_order: list[str] = []
    for module in modules:
        for template in module.templates:
            if template.path not in template_addresses:
                template_addresses[template.path] = []
                template_names[template.path] = template.name
                template_order.append(template.path)
            for addr in template.addresses:
                if addr not in template_addresses[template.path]:
                    template_addresses[template.path].append(addr)

    composed_templates = tuple(
        ArtifactTemplate(
            path=path,
            name=template_names[path],
            addresses=tuple(template_addresses[path]),
        )
        for path in template_order
    )

    seen_std: set[str] = set()
    composed_standards: list[str] = []
    for module in modules:
        for std in module.standards:
            if std not in seen_std:
                seen_std.add(std)
                composed_standards.append(std)

    return Module(
        name=name,
        version=version,
        standards=tuple(composed_standards),
        clauses=tuple(clause_by_id.values()),
        templates=composed_templates,
    )
