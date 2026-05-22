"""Tests for openqms.resolver.resolve.

Covers OQ-010 (pure function), OQ-001 (bidirectional traceability invariant
holds on resolved bundles), and the determinism property test.
"""

from openqms.module import load_module
from openqms.resolver import resolve
from openqms.types import Bundle


def test_resolve_filters_to_in_scope_standards(fixtures_dir):
    module = load_module(str(fixtures_dir / "smoke_module.yaml"))
    bundle = Bundle(product="P", jurisdictions=("J",), standards=("StdA",))
    qms = resolve(bundle, module)
    assert {c.id for c in qms.in_scope_clauses} == {"A-1", "A-2"}
    assert {t.path for t in qms.artifacts} == {"templates/t1.md"}


def test_resolve_is_deterministic(fixtures_dir):
    module = load_module(str(fixtures_dir / "smoke_module.yaml"))
    bundle = Bundle(
        product="P", jurisdictions=("J",), standards=("StdA", "StdB")
    )
    a = resolve(bundle, module)
    b = resolve(bundle, module)
    assert a == b


def test_resolve_bidirectional_traceability(fixtures_dir):
    """OQ-001: forward and reverse traceability maps form a bijection on the
    in-scope set."""
    module = load_module(str(fixtures_dir / "smoke_module.yaml"))
    bundle = Bundle(
        product="P", jurisdictions=("J",), standards=("StdA", "StdB")
    )
    qms = resolve(bundle, module)

    for path, cids in qms.forward.items():
        assert cids, f"artifact {path} addresses no clauses"

    for cid, paths in qms.reverse.items():
        assert paths, f"in-scope clause {cid} is not addressed"

    for path, cids in qms.forward.items():
        for cid in cids:
            assert path in qms.reverse[cid]
    for cid, paths in qms.reverse.items():
        for path in paths:
            assert cid in qms.forward[path]


def test_resolve_drops_templates_with_no_in_scope_clauses(fixtures_dir):
    module = load_module(str(fixtures_dir / "smoke_module.yaml"))
    bundle = Bundle(product="P", jurisdictions=("J",), standards=("StdA",))
    qms = resolve(bundle, module)
    assert "templates/t2.md" not in qms.forward


def test_resolve_with_empty_standards_yields_empty_qms(fixtures_dir):
    module = load_module(str(fixtures_dir / "smoke_module.yaml"))
    bundle = Bundle(product="P", jurisdictions=("J",), standards=())
    qms = resolve(bundle, module)
    assert qms.in_scope_clauses == ()
    assert qms.artifacts == ()
    assert qms.forward == {}
    assert qms.reverse == {}
