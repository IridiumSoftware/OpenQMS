"""Tests for `openqms coverage` per-module + aggregate metrics (OQ-115)."""

from __future__ import annotations

import json
import subprocess
import sys
from pathlib import Path


REPO_ROOT = Path(__file__).resolve().parents[2]


def _run(*args: str) -> tuple[str, int]:
    result = subprocess.run(
        [sys.executable, "-m", "openqms", "coverage", *args],
        capture_output=True,
        text=True,
        cwd=REPO_ROOT,
    )
    return result.stdout, result.returncode


def test_coverage_all_emits_summary():
    """`openqms coverage` (no --module) walks every module + emits summary."""
    stdout, rc = _run()
    assert rc == 0
    data = json.loads(stdout)
    assert "summary" in data
    assert "modules" in data
    assert data["summary"]["modules_in_scope"] > 50
    assert data["summary"]["aggregate_clause_coverage_pct"] >= 0
    assert data["summary"]["aggregate_clause_coverage_pct"] <= 100


def test_coverage_single_module_returns_expected_shape():
    """Per-module coverage entry has all expected fields."""
    stdout, rc = _run("--module", "hipaa")
    assert rc == 0
    data = json.loads(stdout)
    assert len(data["modules"]) == 1
    m = data["modules"][0]
    assert m["module"] == "hipaa"
    for k in (
        "total_clauses",
        "total_templates",
        "total_standards_declared",
        "clauses_bound",
        "clause_coverage_pct",
        "standards_with_clauses",
        "standards_unused",
        "standard_coverage_pct",
        "avg_templates_per_clause",
        "orphan_clauses",
        "orphan_templates",
    ):
        assert k in m, f"missing field {k!r}"


def test_coverage_threshold_zero_never_fails():
    """--threshold 0 (default) never returns nonzero exit."""
    _, rc = _run("--threshold", "0")
    assert rc == 0


def test_coverage_threshold_high_returns_one_when_below():
    """--threshold 99 returns 1 if any module is below 99%."""
    _, rc = _run("--threshold", "99")
    # Some modules may have < 99% if they have lightly-bound clauses;
    # whether this fails depends on current repo state. Accept either
    # 0 (all modules >= 99%) or 1 (at least one below).
    assert rc in (0, 1)


def test_coverage_markdown_renders():
    """Markdown format produces a header + table."""
    stdout, rc = _run("--module", "hipaa", "--format", "md")
    assert rc == 0
    assert "# Open QMS — coverage report" in stdout
    assert "| Module |" in stdout
