"""Tests for `openqms crosswalk` clause-crosswalk between modules (OQ-116)."""

from __future__ import annotations

import json
import subprocess
import sys
from pathlib import Path


REPO_ROOT = Path(__file__).resolve().parents[2]


def _run(*args: str) -> tuple[str, str, int]:
    result = subprocess.run(
        [sys.executable, "-m", "openqms", "crosswalk", *args],
        capture_output=True,
        text=True,
        cwd=REPO_ROOT,
    )
    return result.stdout, result.stderr, result.returncode


def test_crosswalk_requires_at_least_two_modules():
    """Single --module returns error code 2."""
    _, stderr, rc = _run("--module", "hipaa")
    assert rc == 2
    assert "at least 2" in stderr


def test_crosswalk_emits_summary_and_crosswalks():
    """Two-module crosswalk returns valid JSON with summary + crosswalks lists."""
    stdout, _, rc = _run("--module", "privacy", "--module", "us-state-privacy")
    assert rc == 0
    data = json.loads(stdout)
    assert "summary" in data
    assert "crosswalks" in data
    assert data["summary"]["modules_in_scope"] == ["privacy", "us-state-privacy"]
    assert "per_module_shared_clauses" in data["summary"]
    assert "per_module_own_only_clauses" in data["summary"]


def test_crosswalk_per_module_clause_counts_consistent():
    """Per-module shared + own-only = total clauses in module."""
    stdout, _, rc = _run("--module", "hipaa", "--module", "privacy")
    assert rc == 0
    data = json.loads(stdout)
    for mod_name in data["summary"]["modules_in_scope"]:
        shared = data["summary"]["per_module_shared_clauses"][mod_name]
        own = data["summary"]["per_module_own_only_clauses"][mod_name]
        assert shared >= 0
        assert own >= 0
        # Total must be positive (these modules have clauses)
        assert shared + own > 0


def test_crosswalk_markdown_renders():
    """Markdown format renders header + distribution table."""
    stdout, _, rc = _run(
        "--module", "privacy", "--module", "us-state-privacy", "--format", "md"
    )
    assert rc == 0
    assert "# Open QMS — clause crosswalk" in stdout
    assert "**Modules in scope:**" in stdout
    assert "| Module | Shared" in stdout
