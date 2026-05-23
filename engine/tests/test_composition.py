"""Tests for openqms.module.compose.

Covers OQ-011 (modules compose under union; deduplication preserves
invariant) and OQ-012 (cross-cutting overlays compose with vertical
modules — mechanically the same union operation).
"""

from __future__ import annotations

import pytest

from openqms.module import compose, load_module
from openqms.resolver import resolve
from openqms.types import ArtifactTemplate, Bundle, Clause, Module
from openqms.validation import validate


def _module(name, clauses=(), templates=(), standards=("S",), version="0"):
    return Module(
        name=name,
        version=version,
        standards=standards,
        clauses=clauses,
        templates=templates,
    )


def _clause(cid, standard="S", section="1", summary="x", gap_note=None):
    return Clause(
        id=cid,
        standard=standard,
        section=section,
        summary=summary,
        gap_note=gap_note,
    )


def _template(path, addresses, name=None):
    return ArtifactTemplate(
        path=path,
        name=name or path,
        addresses=tuple(addresses),
    )


# ─── unit tests ──────────────────────────────────────────────────────────


def test_compose_empty_raises():
    with pytest.raises(ValueError, match="at least one module"):
        compose([])


def test_compose_single_returns_unchanged():
    m = _module("m1", clauses=(_clause("c1"),))
    assert compose([m]) is m


def test_compose_two_unions_clauses():
    a = _module("a", clauses=(_clause("c1"), _clause("c2")))
    b = _module("b", clauses=(_clause("c3"),))
    composite = compose([a, b])
    assert {c.id for c in composite.clauses} == {"c1", "c2", "c3"}


def test_compose_dedups_identical_clauses():
    shared = _clause("c1", summary="same")
    a = _module("a", clauses=(shared,))
    b = _module("b", clauses=(shared,))
    composite = compose([a, b])
    assert len(composite.clauses) == 1
    assert composite.clauses[0].id == "c1"


def test_compose_raises_on_clause_id_collision_with_different_content():
    a = _module("a", clauses=(_clause("c1", summary="alpha"),))
    b = _module("b", clauses=(_clause("c1", summary="beta"),))
    with pytest.raises(ValueError, match="conflicts across modules"):
        compose([a, b])


def test_compose_unions_template_addresses_for_shared_path():
    a = _module(
        "a",
        clauses=(_clause("c1"), _clause("c2")),
        templates=(_template("t.md", addresses=("c1", "c2")),),
    )
    b = _module(
        "b",
        clauses=(_clause("c3"),),
        templates=(_template("t.md", addresses=("c3",)),),
    )
    composite = compose([a, b])
    assert len(composite.templates) == 1
    t = composite.templates[0]
    assert t.path == "t.md"
    assert set(t.addresses) == {"c1", "c2", "c3"}


def test_compose_preserves_first_seen_template_name():
    a = _module(
        "a",
        clauses=(_clause("c1"),),
        templates=(_template("t.md", addresses=("c1",), name="A's name"),),
    )
    b = _module(
        "b",
        clauses=(_clause("c2"),),
        templates=(_template("t.md", addresses=("c2",), name="B's name"),),
    )
    composite = compose([a, b])
    assert composite.templates[0].name == "A's name"


def test_compose_dedups_and_orders_standards():
    a = _module("a", standards=("StdA", "StdB"))
    b = _module("b", standards=("StdB", "StdC"))
    composite = compose([a, b])
    assert composite.standards == ("StdA", "StdB", "StdC")


def test_compose_is_deterministic():
    a = _module(
        "a",
        clauses=(_clause("c1"), _clause("c2")),
        templates=(_template("t.md", addresses=("c1", "c2")),),
    )
    b = _module(
        "b",
        clauses=(_clause("c3"),),
        templates=(_template("t.md", addresses=("c3",)),),
    )
    assert compose([a, b]) == compose([a, b])


def test_composite_validates_when_each_input_module_is_self_consistent():
    a = _module(
        "a",
        clauses=(_clause("c1"),),
        templates=(_template("t1.md", addresses=("c1",)),),
    )
    b = _module(
        "b",
        clauses=(_clause("c2"),),
        templates=(_template("t2.md", addresses=("c2",)),),
    )
    report = validate(compose([a, b]))
    assert report.invariant_holds


def test_composite_can_close_gaps_in_overlay_only_module():
    """An overlay module may have clauses but no own-templates; composition
    with a vertical module whose templates address those clauses produces a
    valid composite. This is the OQ-012 overlay-composition story."""
    vertical = _module(
        "vertical",
        clauses=(_clause("c1"),),
        templates=(_template("t.md", addresses=("c1", "overlay-c1")),),
    )
    overlay = _module(
        "overlay",
        clauses=(_clause("overlay-c1", standard="OverlayStd"),),
        templates=(),  # overlay declares the clause but no own template
    )
    report = validate(compose([vertical, overlay]))
    assert report.invariant_holds, (
        f"composite should be valid; got {report}"
    )


# ─── integration: medical-devices + iso-27001 overlay ────────────────────


def test_medical_devices_plus_iso27001_composes_and_validates(repo_root):
    mod_root = repo_root / "modules"
    medical = load_module("medical-devices", modules_root=mod_root)
    overlay = load_module("iso-27001", modules_root=mod_root)
    composite = compose([medical, overlay], name="composite", version="0.1.0")
    report = validate(composite)
    assert report.invariant_holds, (
        f"composite invariant violation: "
        f"orphaned_clauses={report.orphaned_clauses}, "
        f"orphaned_artifacts={report.orphaned_artifacts}"
    )


def test_medical_devices_plus_iso27001_resolve_unions_template_addresses(repo_root):
    """The quality-policy template appears in both modules. After
    composition + resolution under all four vertical standards plus
    ISO/IEC 27001:2022, it should address clauses from both modules."""
    mod_root = repo_root / "modules"
    medical = load_module("medical-devices", modules_root=mod_root)
    overlay = load_module("iso-27001", modules_root=mod_root)
    composite = compose([medical, overlay])
    bundle = Bundle(
        product="ExampleSaMD",
        jurisdictions=("FDA",),
        standards=(
            "ISO 13485:2016",
            "21 CFR 820",
            "ISO 14971:2019",
            "IEC 62304:2006+A1:2015",
            "ISO/IEC 27001:2022",
        ),
    )
    qms = resolve(bundle, composite)

    qp_addresses = qms.forward.get("templates/qms-policy/quality-policy.md")
    assert qp_addresses is not None, "quality-policy template missing from forward map"
    assert "ISO13485-4.2.4" in qp_addresses
    assert "CFR820-820.40" in qp_addresses
    assert "ISO27001-A.5.1" in qp_addresses
    assert "ISO27001-A.5.31" in qp_addresses

    # And the reverse map carries the ISO 27001 clauses
    assert "templates/qms-policy/quality-policy.md" in qms.reverse["ISO27001-A.5.1"]
    assert "templates/qms-policy/quality-policy.md" in qms.reverse["ISO27001-A.5.31"]
