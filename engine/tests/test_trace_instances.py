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
    extract_issue_trace_links,
    fetch_issues_via_gh,
    lint_records,
    load_issues_json,
    node_from_issue,
    nodes_from_issues,
    parse_id,
    parse_item_tables,
    parse_links_cell,
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


# --- Tier-2: in-body item tables ---

def test_parse_links_cell_compact_grammar():
    got = parse_links_cell("mitigated_by:MIT-X-0001,MIT-X-0002; verified_by:TST-X-0009")
    assert got == {"mitigated_by": ("MIT-X-0001", "MIT-X-0002"), "verified_by": ("TST-X-0009",)}
    assert parse_links_cell("—") == {}
    assert parse_links_cell("`mitigated_by:MIT-X-0001`") == {"mitigated_by": ("MIT-X-0001",)}


def test_parse_item_tables_extracts_rows_and_skips_placeholders(tmp_path):
    doc = tmp_path / "rmf.md"
    doc.write_text(
        "---\ndocument_id: RMF-X-0001\nversion: \"1.0\"\nowner: x\nstatus: effective\neffective_date: 2026-06-01\n---\n"
        "# RMF\n\n"
        "## Hazards\n\n"
        "| ID | Hazard | Severity | Trace links |\n"
        "|---|---|---|---|\n"
        "| `HAZ-CARDIO-0050` | Air-in-line | Critical | mitigated_by:MIT-CARDIO-0051 |\n"
        "| `HAZ-[PRODUCT]-001` | (blank template placeholder) | — | mitigated_by:MIT-[PRODUCT]-001 |\n",
        encoding="utf-8",
    )
    nodes = parse_item_tables(doc)
    assert len(nodes) == 1  # placeholder row skipped (bracket ID fails grammar)
    n = nodes[0]
    assert n.record_id == "HAZ-CARDIO-0050" and n.kind == "HAZ"
    assert n.links == {"mitigated_by": ("MIT-CARDIO-0051",)}


def test_tier2_collection_doc_composes_into_clean_graph(tmp_path):
    # A container RMF (no record_kind) with hazard + mitigation rows; the
    # mitigation row verifies a Tier-1 whole-record test file.
    (tmp_path / "rmf.md").write_text(
        "---\ndocument_id: RMF-X-0001\nversion: \"1.0\"\nowner: x\nstatus: effective\neffective_date: 2026-06-01\n---\n"
        "# RMF\n\n"
        "| ID | Item | Trace links |\n|---|---|---|\n"
        "| `HAZ-CARDIO-0050` | Air-in-line | mitigated_by:MIT-CARDIO-0051 |\n"
        "| `MIT-CARDIO-0051` | Air detector | verified_by:TST-CARDIO-0021 |\n",
        encoding="utf-8",
    )
    _write(tmp_path / "tst.md", "TST", "TST-CARDIO-0021")
    nodes = discover_records(tmp_path)
    ids = {n.record_id for n in nodes}
    assert {"HAZ-CARDIO-0050", "MIT-CARDIO-0051", "TST-CARDIO-0021"} <= ids
    report = build_report(nodes, DEFAULT_POLICY)
    assert report["summary"]["errors"] == 0, report["findings"]


def test_shipped_example_includes_tier2_rows(repo_root):
    nodes = discover_records(repo_root / "examples" / "trace-instances")
    ids = {n.record_id for n in nodes}
    # Tier-2 rows from RMF-CARDIO-0100.md are discovered alongside Tier-1 records
    assert "HAZ-CARDIO-0050" in ids and "MIT-CARDIO-0051" in ids
    report = build_report(nodes, DEFAULT_POLICY)
    assert report["summary"]["errors"] == 0, report["findings"]


# --- P15.2: GitHub-issue substrate ---

def test_extract_issue_trace_links_parses_section():
    body = "### Description\n\nx\n\n### Trace links\n\ntriggered_by:NCR-3; relates_to:CMPL-2026-0003\n\n### Next\n\ny"
    assert extract_issue_trace_links(body) == {"triggered_by": ("NCR-3",), "relates_to": ("CMPL-2026-0003",)}
    assert extract_issue_trace_links("### Trace links\n\n_No response_") == {}
    assert extract_issue_trace_links("no heading at all") == {}


def test_node_from_issue_label_to_kind_and_id():
    issue = {"number": 7, "labels": [{"name": "capa"}, {"name": "capa-open"}], "body": "### Trace links\n\ntriggered_by:NCR-3"}
    n = node_from_issue(issue)
    assert n is not None
    assert n.kind == "CAPA" and n.record_id == "CAPA-7" and n.origin == "issue"
    assert n.links == {"triggered_by": ("NCR-3",)}


def test_node_from_issue_unlabeled_or_numberless_returns_none():
    assert node_from_issue({"number": 12, "labels": [{"name": "question"}], "body": "x"}) is None
    assert node_from_issue({"labels": [{"name": "capa"}]}) is None


def test_issue_node_lints_clean_despite_short_numeric_id():
    nodes = nodes_from_issues([{"number": 7, "labels": [{"name": "capa"}], "body": "### Trace links\n\ntriggered_by:NCR-3"}])
    assert [f for f in lint_records(nodes, require_scope=True) if f.severity == "error"] == []


def test_fetch_issues_via_gh_with_injected_invoker():
    captured = {}

    def fake_invoker(args):
        captured["args"] = args
        return '[{"number": 7, "labels": [{"name": "capa"}], "body": "### Trace links\\n\\ntriggered_by:NCR-3"}]'

    issues = fetch_issues_via_gh("acme/repo", gh_invoker=fake_invoker)
    assert issues[0]["number"] == 7
    assert "--repo" in captured["args"] and "acme/repo" in captured["args"]


def test_issues_fold_into_markdown_graph_clean(repo_root):
    md = discover_records(repo_root / "examples" / "trace-instances")
    issues = load_issues_json(repo_root / "examples" / "trace-instances" / "issues-export.example.json")
    nodes = md + nodes_from_issues(issues)
    ids = {n.record_id for n in nodes}
    assert "CAPA-7" in ids and "NCR-3" in ids       # issue nodes folded in
    assert not any(i == "QUESTION-12" for i in ids)  # unlabeled issue ignored
    report = build_report(nodes, DEFAULT_POLICY)
    assert report["summary"]["errors"] == 0, report["findings"]
