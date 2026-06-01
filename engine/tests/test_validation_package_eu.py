"""Tests for the validation-package-eu market overlay (P2.3).

EU market dial: ISO 13485 §7.5.6/§7.6 backbone + EU GMP Annex 11 + Annex 15
+ ICH Q9, composing onto the neutral validation-package baseline. Also
covers the US+EU case where both market overlays compose.
"""

from __future__ import annotations

from openqms.module import compose, load_module
from openqms.validation import validate


def test_eu_overlay_validates_standalone(repo_root):
    m = load_module("validation-package-eu", modules_root=repo_root / "modules")
    report = validate(m)
    assert report.invariant_holds, (
        f"orphaned_clauses={report.orphaned_clauses}, "
        f"orphaned_artifacts={report.orphaned_artifacts}"
    )


def test_eu_overlay_clause_and_standard_shape(repo_root):
    m = load_module("validation-package-eu", modules_root=repo_root / "modules")
    assert m.name == "validation-package-eu"
    assert len(m.clauses) == 8
    standards = set(m.standards)
    assert {"ISO 13485:2016", "EU GMP Annex 11", "EU GMP Annex 15", "ICH Q9"} <= standards
    for c in m.clauses:
        assert c.standard in standards, f"clause {c.id} cites {c.standard!r} not in module standards"


def test_eu_overlay_composes_with_baseline(repo_root):
    mod_root = repo_root / "modules"
    composite = compose(
        [
            load_module("validation-package", modules_root=mod_root),
            load_module("validation-package-eu", modules_root=mod_root),
        ],
        name="composite",
        version="0.1.0",
    )
    report = validate(composite)
    assert report.invariant_holds, (
        f"orphaned_clauses={report.orphaned_clauses}, "
        f"orphaned_artifacts={report.orphaned_artifacts}"
    )


def test_us_and_eu_overlays_compose_together(repo_root):
    """A US+EU product composes baseline + both market overlays; the shared
    qms-validation templates union the FDA and EU clause bindings without
    collision."""
    mod_root = repo_root / "modules"
    composite = compose(
        [
            load_module("validation-package", modules_root=mod_root),
            load_module("validation-package-fda", modules_root=mod_root),
            load_module("validation-package-eu", modules_root=mod_root),
        ],
        name="composite",
        version="0.1.0",
    )
    report = validate(composite)
    assert report.invariant_holds, (
        f"orphaned_clauses={report.orphaned_clauses}, "
        f"orphaned_artifacts={report.orphaned_artifacts}"
    )


def test_eu_overlay_qualification_template_exists(repo_root):
    m = load_module("validation-package-eu", modules_root=repo_root / "modules")
    paths = {t.path for t in m.templates}
    assert "templates/qms-validation/QUALIFICATION-PROTOCOL-TEMPLATE.md" in paths
    for t in m.templates:
        assert (repo_root / t.path).is_file(), f"missing template file: {t.path}"
