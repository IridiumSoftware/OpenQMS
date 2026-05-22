"""Integration test for the shipped medical-devices regulatory module.

Asserts that the module-as-shipped passes the OQ-013 validation harness
(no orphaned clauses, no orphaned artifacts) and that resolving an
ExampleDevice / FDA / (ISO 13485 + 21 CFR 820) bundle produces a non-empty
bidirectional traceability matrix.

Status transition this test enables: OQ-001 :argued → :tested (on the
medical-devices smoke bundle); OQ-040..OQ-048 :argued → :tested on the
clauses actually present in modules/medical-devices/module.yaml.
"""

from openqms.module import load_module
from openqms.resolver import resolve
from openqms.types import Bundle
from openqms.validation import validate


def test_medical_devices_module_invariant_holds(repo_root):
    module = load_module(
        "medical-devices", modules_root=repo_root / "modules"
    )
    report = validate(module)
    assert report.invariant_holds, (
        f"medical-devices invariant violation: "
        f"orphaned_clauses={report.orphaned_clauses}, "
        f"orphaned_artifacts={report.orphaned_artifacts}"
    )


def test_medical_devices_resolve_smoke(repo_root):
    """End-to-end smoke: resolve the medical-devices module against an
    ExampleDevice / FDA / (ISO 13485 + 21 CFR 820) bundle and assert the
    traceability matrix is bidirectionally complete."""
    module = load_module(
        "medical-devices", modules_root=repo_root / "modules"
    )
    bundle = Bundle(
        product="ExampleDevice",
        jurisdictions=("FDA",),
        standards=("ISO 13485:2016", "21 CFR 820"),
    )
    qms = resolve(bundle, module)

    assert len(qms.in_scope_clauses) >= 1
    assert len(qms.artifacts) >= 1

    for path, cids in qms.forward.items():
        assert cids, f"artifact {path} addresses no clauses"
    for cid, paths in qms.reverse.items():
        assert paths, f"in-scope clause {cid} is not addressed"
