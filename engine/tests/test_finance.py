"""Tests for the finance vertical (SOX / ICFR spine — 8th vertical).

Sarbanes-Oxley §302/§404 + COSO 2013 + PCAOB AS 2201. Mirrors the other
vertical tests: load from disk, assert the OQ-001 invariant standalone and
composed with the financial cross-cutting overlays, check the templates.
"""

from __future__ import annotations

from openqms.module import compose, load_module
from openqms.validation import validate


def test_finance_validates_standalone(repo_root):
    m = load_module("finance", modules_root=repo_root / "modules")
    report = validate(m)
    assert report.invariant_holds, (
        f"orphaned_clauses={report.orphaned_clauses}, "
        f"orphaned_artifacts={report.orphaned_artifacts}"
    )


def test_finance_clause_and_standard_shape(repo_root):
    m = load_module("finance", modules_root=repo_root / "modules")
    assert m.name == "finance"
    assert len(m.clauses) == 16
    standards = set(m.standards)
    assert {
        "Sarbanes-Oxley Act (SOX)",
        "SEC Exchange Act (ICFR rules)",
        "COSO IC-IF (2013)",
        "PCAOB AS 2201",
    } <= standards
    for c in m.clauses:
        assert c.standard in standards, f"clause {c.id} cites {c.standard!r} not in module standards"


def test_finance_composes_with_financial_overlays(repo_root):
    """ICFR vertical + ITGC (iso-27001) + compliance (iso-37301-financial-services)
    + SOC 2 — the realistic public-company composite."""
    mod_root = repo_root / "modules"
    composite = compose(
        [
            load_module("finance", modules_root=mod_root),
            load_module("iso-27001", modules_root=mod_root),
            load_module("iso-37301-financial-services", modules_root=mod_root),
            load_module("soc-2", modules_root=mod_root),
        ],
        name="composite",
        version="0.1.0",
    )
    report = validate(composite)
    assert report.invariant_holds, (
        f"orphaned_clauses={report.orphaned_clauses}, "
        f"orphaned_artifacts={report.orphaned_artifacts}"
    )


def test_finance_template_paths_exist(repo_root):
    m = load_module("finance", modules_root=repo_root / "modules")
    assert len(m.templates) == 6
    for t in m.templates:
        assert (repo_root / t.path).is_file(), f"missing template file: {t.path}"
