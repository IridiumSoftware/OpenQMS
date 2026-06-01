"""Tests for instance-level traceability (P15.1a).

Inline markdown fixtures written to tmp_path, parsed into the instance
graph, then checked for parsing, inverse-edge materialization, referential
integrity, per-kind minimum-edge requirements, acyclicity, and the static
lint surface.
"""

from __future__ import annotations

from pathlib import Path

from openqms.trace_instances import (
    DEFAULT_POLICY,
    build_report,
    check_invariants,
    discover_records,
    lint_records,
    parse_id,
    parse_record,
)


def _write(p: Path, kind: str, rid: str, links: dict[str, list[str]] | None = None) -> Path:
    fm = [
        "---",
        f"document_id: {rid}",
        'version: "1.0"',
        "owner: x",
        "status: open",
        "opened_date: YYYY-MM-DD",
        f"record_kind: {kind}",
        f"record_id: {rid}",
    ]
    if links:
        fm.append("trace_links:")
        for rel, targets in links.items():
            fm.append(f"  {rel}:")
            for t in targets:
                fm.append(f"    - {t}")
    fm += ["---", "", f"# {rid}", ""]
    p.write_text("\n".join(fm), encoding="utf-8")
    return p


# --- parsing + grammar ---

def test_parse_id_scoped_scopeless_and_malformed():
    assert parse_id("HAZ-CARDIO-0007") == ("HAZ", "CARDIO", "0007")
    assert parse_id("CAPA-0034") == ("CAPA", None, "0034")
    assert parse_id("nope") is None
    assert parse_id("HAZ-CARDIO-12") is None  # seq must be >= 3 digits


def test_parse_record_reads_trace_frontmatter(tmp_path):
    p = _write(tmp_path / "h.md", "HAZ", "HAZ-CARDIO-0007", {"mitigated_by": ["MIT-CARDIO-0011"]})
    node = parse_record(p)
    assert node is not None
    assert node.kind == "HAZ" and node.record_id == "HAZ-CARDIO-0007"
    assert node.scope == "CARDIO"
    assert node.links["mitigated_by"] == ("MIT-CARDIO-0011",)


def test_parse_record_none_without_record_kind(tmp_path):
    p = tmp_path / "plain.md"
    p.write_text("---\ndocument_id: DOC-1\nversion: \"1.0\"\nowner: x\nstatus: draft\neffective_date: YYYY-MM-DD\n---\n# x\n", encoding="utf-8")
    assert parse_record(p) is None


# --- graph + invariants ---

def test_inverse_edge_satisfies_requirement_from_either_endpoint(tmp_path):
    # HAZ declares nothing; MIT declares `mitigates: [HAZ]`. The HAZ's
    # mitigated_by requirement must still be satisfied via the inverse edge.
    _write(tmp_path / "haz.md", "HAZ", "HAZ-CARDIO-0007")
    _write(tmp_path / "mit.md", "MIT", "MIT-CARDIO-0011", {"mitigates": ["HAZ-CARDIO-0007"], "verified_by": ["TST-CARDIO-0021"]})
    _write(tmp_path / "tst.md", "TST", "TST-CARDIO-0021")
    nodes = discover_records(tmp_path)
    findings = check_invariants(nodes, {"require": [{"kind": "HAZ", "edge": "mitigated_by", "min": 1}]})
    assert [f for f in findings if f.severity == "error"] == []


def test_missing_mitigation_flagged(tmp_path):
    _write(tmp_path / "haz.md", "HAZ", "HAZ-CARDIO-0007")
    nodes = discover_records(tmp_path)
    findings = check_invariants(nodes, {"referential_integrity": "off", "require": [{"kind": "HAZ", "edge": "mitigated_by", "min": 1}]})
    assert any("mitigated_by" in f.message and f.severity == "error" for f in findings)


def test_referential_integrity_flags_dangling_target(tmp_path):
    _write(tmp_path / "h.md", "HAZ", "HAZ-CARDIO-0007", {"mitigated_by": ["MIT-CARDIO-9999"]})
    nodes = discover_records(tmp_path)
    findings = check_invariants(nodes, {"require": []})
    assert any("does not resolve" in f.message for f in findings)


def test_acyclicity_detects_derived_from_cycle(tmp_path):
    _write(tmp_path / "a.md", "REQ", "REQ-X-0001", {"derived_from": ["REQ-X-0002"]})
    _write(tmp_path / "b.md", "REQ", "REQ-X-0002", {"derived_from": ["REQ-X-0001"]})
    nodes = discover_records(tmp_path)
    findings = check_invariants(nodes, {"referential_integrity": "off", "no_cycles": ["derived_from"], "require": []})
    assert any("cycle" in f.message for f in findings)


# --- lint surface ---

def test_lint_flags_prefix_mismatch_missing_scope_and_unknown_rel(tmp_path):
    _write(tmp_path / "bad.md", "HAZ", "MIT-CARDIO-0007", {"bogus_rel": ["X-Y-0001"]})  # prefix != kind + bad rel
    _write(tmp_path / "noscope.md", "REQ", "REQ-0001")  # product-bound, no scope
    nodes = discover_records(tmp_path)
    findings = lint_records(nodes, require_scope=True)
    msgs = " | ".join(f.message for f in findings)
    assert "prefix" in msgs and "unknown relationship" in msgs and "SCOPE" in msgs


# --- report shape: a clean graph has zero errors under the default policy ---

def test_clean_graph_report_has_zero_errors(tmp_path):
    _write(tmp_path / "func.md", "FUNC", "FUNC-CARDIO-0012", {"assured_by": ["VREC-CARDIO-0044"], "validates": ["URS-CARDIO-0003"]})
    _write(tmp_path / "vrec.md", "VREC", "VREC-CARDIO-0044")
    _write(tmp_path / "urs.md", "URS", "URS-CARDIO-0003", {"validated_by": ["VREC-CARDIO-0044"]})
    nodes = discover_records(tmp_path)
    report = build_report(nodes, {"referential_integrity": "error", "require": [{"kind": "FUNC", "edge": "assured_by", "min": 1, "severity": "error"}]})
    assert report["summary"]["errors"] == 0
    assert report["summary"]["records"] == 3
    assert "FUNC-CARDIO-0012" in report["edges"]


def test_default_policy_is_well_formed():
    assert any(r["kind"] == "HAZ" for r in DEFAULT_POLICY["require"])


def test_shipped_example_records_validate_clean(repo_root):
    """The committed worked example (examples/trace-instances/) must lint
    clean and satisfy the default policy with zero errors — this is what CI
    gates on."""
    root = repo_root / "examples" / "trace-instances"
    nodes = discover_records(root)
    assert len(nodes) >= 8, f"expected >=8 example records, found {len(nodes)}"
    lint = lint_records(nodes, require_scope=True)
    assert [f for f in lint if f.severity == "error"] == [], [f.message for f in lint if f.severity == "error"]
    report = build_report(nodes, DEFAULT_POLICY)
    assert report["summary"]["errors"] == 0, report["findings"]
