"""Tests for the validation-package-fda market overlay (P2.2).

FDA market dial: CSA framework + 21 CFR Part 11 + Part 820/QMSR predicate,
composing onto the neutral validation-package baseline.
"""

from __future__ import annotations

from openqms.module import compose, load_module
from openqms.validation import validate


def test_fda_overlay_validates_standalone(repo_root):
    m = load_module("validation-package-fda", modules_root=repo_root / "modules")
    report = validate(m)
    assert report.invariant_holds, (
        f"orphaned_clauses={report.orphaned_clauses}, "
        f"orphaned_artifacts={report.orphaned_artifacts}"
    )


def test_fda_overlay_clause_and_standard_shape(repo_root):
    m = load_module("validation-package-fda", modules_root=repo_root / "modules")
    assert m.name == "validation-package-fda"
    assert len(m.clauses) == 9
    standards = set(m.standards)
    assert {"FDA CSA Guidance (2026)", "21 CFR Part 11", "21 CFR 820"} <= standards
    for c in m.clauses:
        assert c.standard in standards, f"clause {c.id} cites {c.standard!r} not in module standards"


def test_fda_overlay_composes_with_baseline(repo_root):
    mod_root = repo_root / "modules"
    baseline = load_module("validation-package", modules_root=mod_root)
    fda = load_module("validation-package-fda", modules_root=mod_root)
    composite = compose([baseline, fda], name="composite", version="0.1.0")
    report = validate(composite)
    assert report.invariant_holds, (
        f"orphaned_clauses={report.orphaned_clauses}, "
        f"orphaned_artifacts={report.orphaned_artifacts}"
    )


def test_fda_overlay_composes_onto_medical_devices(repo_root):
    mod_root = repo_root / "modules"
    composite = compose(
        [
            load_module("medical-devices", modules_root=mod_root),
            load_module("validation-package", modules_root=mod_root),
            load_module("validation-package-fda", modules_root=mod_root),
        ],
        name="composite",
        version="0.1.0",
    )
    report = validate(composite)
    assert report.invariant_holds, (
        f"orphaned_clauses={report.orphaned_clauses}, "
        f"orphaned_artifacts={report.orphaned_artifacts}"
    )


def test_fda_overlay_part11_template_exists(repo_root):
    m = load_module("validation-package-fda", modules_root=repo_root / "modules")
    paths = {t.path for t in m.templates}
    assert "templates/qms-validation/ELECTRONIC-RECORDS-CONTROLS-TEMPLATE.md" in paths
    for t in m.templates:
        assert (repo_root / t.path).is_file(), f"missing template file: {t.path}"
