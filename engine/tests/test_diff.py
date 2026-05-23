"""Tests for openqms.diff — matrix diffing for the regenerate workflow."""

from __future__ import annotations

from openqms.diff import MatrixDiff, diff_matrices, format_diff


def _matrix(standards=(), clauses=(), artifacts=(), forward=None, module_version="1.0"):
    """Build a minimal matrix dict for diff tests."""
    return {
        "bundle": {"product": "P", "jurisdictions": [], "standards": list(standards)},
        "module": {"name": "m", "version": module_version},
        "in_scope_clauses": [
            {"id": c, "standard": "S", "section": "1", "summary": "x", "gap_note": None}
            for c in clauses
        ],
        "artifacts": [
            {"path": p, "name": p, "addresses": list((forward or {}).get(p, []))}
            for p in artifacts
        ],
        "traceability": {
            "forward": forward or {},
            "reverse": {},  # diff doesn't read reverse
        },
    }


def test_no_changes_diff_is_empty():
    m = _matrix(standards=("A",), clauses=("c1",), artifacts=("t",), forward={"t": ["c1"]})
    d = diff_matrices(m, m)
    assert not d.has_changes


def test_standard_added():
    old = _matrix(standards=("A",))
    new = _matrix(standards=("A", "B"))
    d = diff_matrices(old, new)
    assert d.standards_added == ("B",)
    assert d.standards_removed == ()
    assert d.has_changes


def test_standard_removed():
    old = _matrix(standards=("A", "B"))
    new = _matrix(standards=("A",))
    d = diff_matrices(old, new)
    assert d.standards_removed == ("B",)
    assert d.standards_added == ()


def test_clause_added():
    old = _matrix(clauses=("c1",))
    new = _matrix(clauses=("c1", "c2"))
    d = diff_matrices(old, new)
    assert d.clauses_added == ("c2",)


def test_artifact_added_and_removed():
    old = _matrix(artifacts=("t1",), forward={"t1": ["c1"]})
    new = _matrix(artifacts=("t2",), forward={"t2": ["c1"]})
    d = diff_matrices(old, new)
    assert d.artifacts_added == ("t2",)
    assert d.artifacts_removed == ("t1",)
    # whole-artifact add/remove not double-counted under addresses_changed
    assert d.addresses_changed == {}


def test_addresses_changed_for_shared_artifact():
    old = _matrix(artifacts=("t",), forward={"t": ["c1"]})
    new = _matrix(artifacts=("t",), forward={"t": ["c1", "c2"]})
    d = diff_matrices(old, new)
    assert d.addresses_changed == {"t": (("c2",), ())}


def test_module_version_change():
    old = _matrix(module_version="1.0")
    new = _matrix(module_version="1.1")
    d = diff_matrices(old, new)
    assert d.module_version_change == ("1.0", "1.1")


def test_combined_diff_has_changes_flag():
    old = _matrix(standards=("A",), clauses=("c1",), artifacts=("t1",))
    new = _matrix(standards=("A", "B"), clauses=("c1", "c2"), artifacts=("t1",))
    d = diff_matrices(old, new)
    assert d.has_changes
    assert d.standards_added == ("B",)
    assert d.clauses_added == ("c2",)


def test_format_diff_no_changes():
    d = MatrixDiff(
        bundle_def_name="b",
        standards_added=(),
        standards_removed=(),
        clauses_added=(),
        clauses_removed=(),
        artifacts_added=(),
        artifacts_removed=(),
        addresses_changed={},
        module_version_change=None,
    )
    out = format_diff(d)
    assert "(no changes)" in out
    assert "b" in out


def test_format_diff_renders_all_sections():
    d = MatrixDiff(
        bundle_def_name="b",
        standards_added=("B",),
        standards_removed=("A",),
        clauses_added=("c-new",),
        clauses_removed=("c-old",),
        artifacts_added=("a-new",),
        artifacts_removed=("a-old",),
        addresses_changed={"shared": (("c1",), ("c0",))},
        module_version_change=("1.0", "2.0"),
    )
    out = format_diff(d)
    assert "1.0 → 2.0" in out
    assert "+ B" in out
    assert "- A" in out
    assert "+ c-new" in out
    assert "- c-old" in out
    assert "+ a-new" in out
    assert "- a-old" in out
    assert "shared:" in out
    assert "+ c1" in out
    assert "- c0" in out
