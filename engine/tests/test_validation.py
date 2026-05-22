"""Tests for openqms.validation.validate.

Covers OQ-013: every clause has ≥1 binding; no template binds a non-existent
clause.
"""

from openqms.module import load_module
from openqms.types import ArtifactTemplate, Clause, Module
from openqms.validation import validate


def test_smoke_module_validates(fixtures_dir):
    module = load_module(str(fixtures_dir / "smoke_module.yaml"))
    report = validate(module)
    assert report.invariant_holds
    assert report.orphaned_clauses == ()
    assert report.orphaned_artifacts == ()


def test_detects_orphaned_clause():
    module = Module(
        name="m",
        version="0",
        standards=("S",),
        clauses=(
            Clause(id="c1", standard="S", section="1", summary="x"),
            Clause(id="c2", standard="S", section="2", summary="y"),
        ),
        templates=(
            ArtifactTemplate(path="t", name="T", addresses=("c1",)),
        ),
    )
    r = validate(module)
    assert not r.invariant_holds
    assert r.orphaned_clauses == ("c2",)
    assert r.orphaned_artifacts == ()


def test_detects_orphaned_artifact():
    module = Module(
        name="m",
        version="0",
        standards=("S",),
        clauses=(Clause(id="c1", standard="S", section="1", summary="x"),),
        templates=(
            ArtifactTemplate(
                path="t",
                name="T",
                addresses=("c1", "c-ghost"),
            ),
        ),
    )
    r = validate(module)
    assert not r.invariant_holds
    assert r.orphaned_clauses == ()
    assert r.orphaned_artifacts == ("t",)


def test_detects_both_orphan_types():
    module = Module(
        name="m",
        version="0",
        standards=("S",),
        clauses=(
            Clause(id="c1", standard="S", section="1", summary="x"),
            Clause(id="c2", standard="S", section="2", summary="y"),
        ),
        templates=(
            ArtifactTemplate(
                path="t",
                name="T",
                addresses=("c1", "c-ghost"),
            ),
        ),
    )
    r = validate(module)
    assert not r.invariant_holds
    assert r.orphaned_clauses == ("c2",)
    assert r.orphaned_artifacts == ("t",)
