"""Tests for `openqms trace` repo-wide traceability matrix (OQ-067)."""

from __future__ import annotations

import json
import subprocess
import sys
from pathlib import Path


REPO_ROOT = Path(__file__).resolve().parents[2]


def _run_trace(*args: str) -> tuple[str, int]:
    result = subprocess.run(
        [sys.executable, "-m", "openqms", "trace", *args],
        capture_output=True,
        text=True,
        cwd=REPO_ROOT,
    )
    return result.stdout, result.returncode


def test_trace_all_emits_summary_for_every_module():
    """`openqms trace --all` walks every module under ./modules/ + emits
    a summary with module/clause/template counts. OQ-067 evidence."""
    stdout, rc = _run_trace("--all")
    assert rc == 0
    data = json.loads(stdout)
    assert "summary" in data
    assert "modules" in data
    summary = data["summary"]
    assert summary["modules_in_scope"] > 50, (
        "expected the repo to have substantially many modules; got "
        f"{summary['modules_in_scope']}"
    )
    assert summary["total_clauses"] > 500
    assert summary["total_templates"] > 100


def test_trace_module_forward_reverse_are_bidirectional():
    """For each module, the forward map (clause → templates) and the
    reverse map (template → clauses) must be consistent: every (clause,
    template) edge in forward appears in reverse and vice versa."""
    stdout, rc = _run_trace("--module", "medical-devices")
    assert rc == 0
    data = json.loads(stdout)
    mod = data["modules"]["medical-devices"]
    forward = mod["forward"]
    reverse = mod["reverse"]
    # Every edge in forward must appear in reverse
    for cid, tlist in forward.items():
        for tpath in tlist:
            assert tpath in reverse, (
                f"clause {cid} → template {tpath} in forward but template "
                "not in reverse"
            )
            assert cid in reverse[tpath], (
                f"clause {cid} → template {tpath} in forward but template "
                f"{tpath} does not declare addressing {cid}"
            )


def test_trace_orphan_detection_present_in_output():
    """Output includes orphaned_clauses + orphaned_templates lists per
    module — these are the OQ-001 invariant-violation surface that the
    trace command exposes for repo-wide audit."""
    stdout, rc = _run_trace("--all")
    assert rc == 0
    data = json.loads(stdout)
    for name, m in data["modules"].items():
        assert "orphaned_clauses" in m, f"module {name} missing orphaned_clauses"
        assert "orphaned_templates" in m, (
            f"module {name} missing orphaned_templates"
        )


def test_trace_markdown_format_renders():
    """Markdown format produces human-readable output usable in audit
    reports / per-PR review summaries."""
    stdout, rc = _run_trace("--module", "chemicals", "--format", "md")
    assert rc == 0
    assert "# Open QMS — repository-wide traceability matrix" in stdout
    assert "## chemicals" in stdout
    assert "| Clause | Templates addressing |" in stdout
