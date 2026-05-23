"""Tests for openqms.registry — standards-and-jurisdictions registry (OQ-014)."""

from __future__ import annotations

import pytest

from openqms.module import load_module
from openqms.registry import (
    JurisdictionEntry,
    Registry,
    StandardEntry,
    load_registry,
    validate_module_against_registry,
)


# ─── unit tests on Registry ─────────────────────────────────────────────


def _smoke_registry():
    return Registry(
        standards=(
            StandardEntry(
                id="ISO 13485:2016",
                name="QMS for medical devices",
                publisher="ISO",
                edition="2016",
                kind="standard",
                license_kind="commercial",
                aliases=("ISO 13485", "ISO13485"),
            ),
            StandardEntry(
                id="21 CFR 820",
                name="FDA QSR",
                publisher="US FDA",
                edition="current",
                kind="regulation",
                license_kind="public",
                aliases=("QSR",),
            ),
        ),
        jurisdictions=(
            JurisdictionEntry(
                id="FDA",
                name="U.S. FDA",
                region="United States",
                applicable_standards=("21 CFR 820",),
            ),
        ),
    )


def test_resolve_standard_by_canonical_id():
    r = _smoke_registry()
    assert r.resolve_standard("ISO 13485:2016").id == "ISO 13485:2016"


def test_resolve_standard_by_alias():
    r = _smoke_registry()
    assert r.resolve_standard("ISO 13485").id == "ISO 13485:2016"
    assert r.resolve_standard("ISO13485").id == "ISO 13485:2016"
    assert r.resolve_standard("QSR").id == "21 CFR 820"


def test_resolve_standard_unknown_raises():
    r = _smoke_registry()
    with pytest.raises(KeyError, match="not in registry"):
        r.resolve_standard("ISO 13485:2017")


def test_canonical_standard_normalizes_alias():
    r = _smoke_registry()
    assert r.canonical_standard("ISO 13485") == "ISO 13485:2016"


def test_has_standard():
    r = _smoke_registry()
    assert r.has_standard("ISO 13485:2016")
    assert r.has_standard("QSR")
    assert not r.has_standard("ISO 13485:2017")


def test_resolve_jurisdiction():
    r = _smoke_registry()
    assert r.resolve_jurisdiction("FDA").id == "FDA"


def test_resolve_jurisdiction_unknown_raises():
    r = _smoke_registry()
    with pytest.raises(KeyError, match="not in registry"):
        r.resolve_jurisdiction("EMA")


# ─── loader tests on shipped registry ────────────────────────────────────


def test_load_shipped_registry(repo_root):
    registry = load_registry(root=repo_root / "registry")
    assert len(registry.standards) >= 10
    assert len(registry.jurisdictions) >= 5
    # Shipped standards we expect by construction
    for canonical in (
        "ISO 13485:2016",
        "21 CFR 820",
        "ISO 14971:2019",
        "IEC 62304:2006+A1:2015",
        "ISO/IEC 27001:2022",
    ):
        assert registry.has_standard(canonical), (
            f"shipped registry missing canonical standard {canonical!r}"
        )
    # Jurisdictions
    for jid in ("FDA", "Health Canada", "EU MDR"):
        assert registry.has_jurisdiction(jid), (
            f"shipped registry missing jurisdiction {jid!r}"
        )


def test_shipped_registry_cross_check_is_clean(repo_root):
    """load_registry raises if any jurisdiction references a standard not in
    standards.yaml. This test enforces that the shipped registry is
    internally consistent — repeated here as a self-check so a future PR
    that breaks it surfaces a clear failure."""
    # If the shipped registry had a dangling reference, load_registry would
    # have raised on the previous test. Re-load here for clarity.
    registry = load_registry(root=repo_root / "registry")
    for j in registry.jurisdictions:
        for s in j.applicable_standards:
            assert registry.has_standard(s), (
                f"jurisdiction {j.id!r} references unregistered standard "
                f"{s!r} — registry cross-check should have caught this at "
                "load time"
            )


def test_load_registry_missing_files_raise(tmp_path):
    with pytest.raises(FileNotFoundError, match="Standards registry"):
        load_registry(root=tmp_path)


def test_load_registry_dangling_jurisdiction_raises(tmp_path):
    (tmp_path / "standards.yaml").write_text(
        "standards:\n"
        "  - id: A\n    name: A\n    publisher: X\n    edition: '1'\n"
        "    kind: standard\n    license_kind: public\n"
    )
    (tmp_path / "jurisdictions.yaml").write_text(
        "jurisdictions:\n"
        "  - id: J\n    name: J\n    region: X\n"
        "    applicable_standards: [Z]\n"  # Z not in standards
    )
    with pytest.raises(ValueError, match="not present in the standards"):
        load_registry(root=tmp_path)


# ─── module-vs-registry cross-check ─────────────────────────────────────


def test_shipped_medical_devices_module_passes_registry_check(repo_root):
    registry = load_registry(root=repo_root / "registry")
    module = load_module(
        "medical-devices", modules_root=repo_root / "modules"
    )
    report = validate_module_against_registry(module, registry)
    assert report.invariant_holds, (
        f"medical-devices module references unregistered standards: "
        f"module={list(report.unregistered_module_standards)}, "
        f"clauses={list(report.unregistered_clause_standards)}"
    )


def test_shipped_iso27001_module_passes_registry_check(repo_root):
    registry = load_registry(root=repo_root / "registry")
    module = load_module("iso-27001", modules_root=repo_root / "modules")
    report = validate_module_against_registry(module, registry)
    assert report.invariant_holds, (
        f"iso-27001 module references unregistered standards: "
        f"module={list(report.unregistered_module_standards)}, "
        f"clauses={list(report.unregistered_clause_standards)}"
    )


def test_validate_module_detects_unregistered_module_standard():
    from openqms.types import Module

    registry = _smoke_registry()
    bad = Module(
        name="bad",
        version="0",
        standards=("ISO 13485:2016", "Made Up Standard"),
        clauses=(),
        templates=(),
    )
    r = validate_module_against_registry(bad, registry)
    assert not r.invariant_holds
    assert "Made Up Standard" in r.unregistered_module_standards


def test_validate_module_detects_unregistered_clause_standard():
    from openqms.types import Clause, Module

    registry = _smoke_registry()
    bad = Module(
        name="bad",
        version="0",
        standards=("ISO 13485:2016",),
        clauses=(
            Clause(
                id="X-1",
                standard="Phantom Standard",
                section="1",
                summary="x",
            ),
        ),
        templates=(),
    )
    r = validate_module_against_registry(bad, registry)
    assert not r.invariant_holds
    assert "Phantom Standard" in r.unregistered_clause_standards


# ─── CLI integration ────────────────────────────────────────────────────


def test_cli_resolve_canonicalizes_alias(repo_root, tmp_path, monkeypatch):
    """`openqms resolve --standard "ISO 13485"` should resolve to the
    canonical 'ISO 13485:2016' and find clauses that reference the
    canonical id — without the registry, the alias would silently filter
    to zero clauses."""
    import json
    import subprocess
    import sys

    monkeypatch.chdir(repo_root)
    out = tmp_path / "matrix.json"
    result = subprocess.run(
        [
            sys.executable, "-m", "openqms", "resolve",
            "--product", "ExampleDevice",
            "--jurisdiction", "FDA",
            "--standard", "ISO 13485",          # alias
            "--standard", "21 CFR 820",         # canonical
            "--module", "medical-devices",
            "--output", str(out),
        ],
        capture_output=True,
        text=True,
    )
    assert result.returncode == 0, f"stderr: {result.stderr}"
    matrix = json.loads(out.read_text())
    assert "ISO 13485:2016" in matrix["bundle"]["standards"]
    in_scope = {c["standard"] for c in matrix["in_scope_clauses"]}
    assert "ISO 13485:2016" in in_scope


def test_cli_resolve_rejects_unknown_standard(repo_root, monkeypatch):
    import subprocess
    import sys

    monkeypatch.chdir(repo_root)
    result = subprocess.run(
        [
            sys.executable, "-m", "openqms", "resolve",
            "--product", "ExampleDevice",
            "--jurisdiction", "FDA",
            "--standard", "ISO 13485:2017",  # typo; not in registry
            "--module", "medical-devices",
            "--output", "-",
        ],
        capture_output=True,
        text=True,
    )
    assert result.returncode != 0
    assert "not in the registry" in result.stderr


def test_cli_resolve_rejects_unknown_jurisdiction(repo_root, monkeypatch):
    import subprocess
    import sys

    monkeypatch.chdir(repo_root)
    result = subprocess.run(
        [
            sys.executable, "-m", "openqms", "resolve",
            "--product", "ExampleDevice",
            "--jurisdiction", "BogusGov",  # not in registry
            "--standard", "ISO 13485:2016",
            "--module", "medical-devices",
            "--output", "-",
        ],
        capture_output=True,
        text=True,
    )
    assert result.returncode != 0
    assert "not in the registry" in result.stderr


def test_cli_allow_unregistered_standards_escape_hatch(repo_root, monkeypatch, tmp_path):
    """With --allow-unregistered-standards, an unknown standard is
    accepted but filters to zero clauses (the pre-v0.5.0 behavior)."""
    import json
    import subprocess
    import sys

    monkeypatch.chdir(repo_root)
    out = tmp_path / "matrix.json"
    result = subprocess.run(
        [
            sys.executable, "-m", "openqms", "resolve",
            "--product", "ExampleDevice",
            "--jurisdiction", "FDA",
            "--standard", "ISO 13485:2017",
            "--module", "medical-devices",
            "--allow-unregistered-standards",
            "--output", str(out),
        ],
        capture_output=True,
        text=True,
    )
    assert result.returncode == 0
    matrix = json.loads(out.read_text())
    # Empty resolution because no clauses reference "ISO 13485:2017"
    assert matrix["in_scope_clauses"] == []


def test_cli_registry_list(repo_root, monkeypatch):
    import subprocess
    import sys

    monkeypatch.chdir(repo_root)
    result = subprocess.run(
        [sys.executable, "-m", "openqms", "registry", "list"],
        capture_output=True,
        text=True,
    )
    assert result.returncode == 0
    assert "ISO 13485:2016" in result.stdout
    assert "FDA" in result.stdout


def test_cli_registry_show_by_alias(repo_root, monkeypatch):
    import subprocess
    import sys

    monkeypatch.chdir(repo_root)
    result = subprocess.run(
        [sys.executable, "-m", "openqms", "registry", "show", "--id", "ISO 13485"],
        capture_output=True,
        text=True,
    )
    assert result.returncode == 0
    assert "ISO 13485:2016" in result.stdout
    assert "publisher" in result.stdout
