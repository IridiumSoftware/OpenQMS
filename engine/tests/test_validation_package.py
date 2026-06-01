"""Tests for the validation-package baseline module (P2.1).

Risk-based computerized-system validation overlay (CSA-framed; classic CSV
is the robust-scripted tier). Mirrors the test_composition style: load the
shipped module from disk, assert the OQ-001 invariant standalone and in a
composite with a vertical, and check the template files exist.
"""

from __future__ import annotations

from openqms.module import compose, load_module
from openqms.validation import validate


def test_validation_package_validates_standalone(repo_root):
    m = load_module("validation-package", modules_root=repo_root / "modules")
    report = validate(m)
    assert report.invariant_holds, (
        f"orphaned_clauses={report.orphaned_clauses}, "
        f"orphaned_artifacts={report.orphaned_artifacts}"
    )


def test_validation_package_clause_and_standard_shape(repo_root):
    m = load_module("validation-package", modules_root=repo_root / "modules")
    assert m.name == "validation-package"
    # 11 baseline clauses across GAMP 5 + ISO 13485 + ISO 29119-1
    assert len(m.clauses) == 11
    standards = set(m.standards)
    assert {"GAMP 5 (2nd Edition)", "ISO 13485:2016", "IEC/IEEE/ISO 29119-1:2022"} <= standards
    # every clause cites one of the module's declared standards
    for c in m.clauses:
        assert c.standard in standards, f"clause {c.id} cites unregistered-in-module standard {c.standard!r}"


def test_validation_package_composes_with_medical_devices(repo_root):
    mod_root = repo_root / "modules"
    medical = load_module("medical-devices", modules_root=mod_root)
    valpkg = load_module("validation-package", modules_root=mod_root)
    composite = compose([medical, valpkg], name="composite", version="0.1.0")
    report = validate(composite)
    assert report.invariant_holds, (
        f"orphaned_clauses={report.orphaned_clauses}, "
        f"orphaned_artifacts={report.orphaned_artifacts}"
    )


def test_validation_package_template_paths_exist(repo_root):
    m = load_module("validation-package", modules_root=repo_root / "modules")
    assert m.templates, "module declares no templates"
    for t in m.templates:
        assert (repo_root / t.path).is_file(), f"missing template file: {t.path}"
