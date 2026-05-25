"""Tests for `openqms jurisdictions-query` (OQ-117)."""

from __future__ import annotations

import json
import subprocess
import sys
from pathlib import Path


REPO_ROOT = Path(__file__).resolve().parents[2]


def _run(*args: str) -> tuple[str, int]:
    result = subprocess.run(
        [sys.executable, "-m", "openqms", "jurisdictions-query", *args],
        capture_output=True,
        text=True,
        cwd=REPO_ROOT,
    )
    return result.stdout, result.returncode


def test_fda_returns_fda_standards():
    """FDA query returns standards published by FDA."""
    stdout, rc = _run("--jurisdiction", "FDA", "--format", "json")
    assert rc == 0
    data = json.loads(stdout)
    assert data["query"] == "FDA"
    assert data["match_count"] > 0
    # Should include at least 21 CFR Part 4 (chemicals + medical-devices land)
    ids = [s["id"] for s in data["standards"]]
    assert any("21 CFR" in i or "FDA" in i.upper() for i in ids), (
        f"expected FDA-published standards in match; got: {ids}"
    )


def test_eu_mdr_returns_eu_standards():
    """EU MDR query returns EU-published standards."""
    stdout, rc = _run("--jurisdiction", "EU MDR", "--format", "json")
    assert rc == 0
    data = json.loads(stdout)
    assert data["match_count"] > 0


def test_unknown_jurisdiction_returns_zero_matches():
    """Unknown jurisdiction returns valid output with zero matches."""
    stdout, rc = _run("--jurisdiction", "ZZZ-Unknown", "--format", "json")
    assert rc == 0
    data = json.loads(stdout)
    assert data["match_count"] == 0
    assert data["standards"] == []


def test_text_format_renders():
    """Default text format produces readable output."""
    stdout, rc = _run("--jurisdiction", "FDA")
    assert rc == 0
    assert "jurisdiction: FDA" in stdout
    assert "matched:" in stdout
