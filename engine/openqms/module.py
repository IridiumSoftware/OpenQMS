"""Module loading — parse a ``module.yaml`` manifest into the Module type."""

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
