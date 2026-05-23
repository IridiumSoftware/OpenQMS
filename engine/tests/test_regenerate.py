"""CLI integration tests for `openqms regenerate` and edition supersession."""

from __future__ import annotations

import json
import shutil
import subprocess
import sys

import pytest


def _run(args, cwd, **kwargs):
    return subprocess.run(
        [sys.executable, "-m", "openqms", *args],
        cwd=cwd,
        capture_output=True,
        text=True,
        **kwargs,
    )


def test_shipped_example_matrix_is_up_to_date(repo_root):
    """`openqms regenerate --bundle example-samd` must report no changes
    against the committed bundles/example-samd.matrix.json. If this fails,
    a module/registry/template change unexpectedly affected the example
    bundle and either the change should be reverted or
    `openqms regenerate --bundle example-samd --write-matrix` should be
    run and the result committed."""
    result = _run(
        ["regenerate", "--bundle", "example-samd"], cwd=str(repo_root)
    )
    assert result.returncode == 0, (
        f"regenerate reported drift; stdout:\n{result.stdout}\n"
        f"stderr:\n{result.stderr}"
    )
    assert "(no changes)" in result.stdout


def test_regenerate_baseline_when_no_prior_matrix(tmp_path, repo_root):
    """First run against a fresh bundle definition with no prior matrix
    prints a baseline message and writes the file when --write-matrix."""
    workdir = tmp_path / "work"
    shutil.copytree(repo_root, workdir, symlinks=True, ignore=shutil.ignore_patterns(
        ".git", ".venv*", "BUSINESS", "__pycache__", "*.egg-info",
        ".pytest_cache", "site"
    ))
    # Use a fresh bundle name with no prior matrix
    (workdir / "bundles" / "fresh.yaml").write_text(
        "name: fresh\n"
        "product: FreshDevice\n"
        "jurisdictions: [FDA]\n"
        "standards: ['ISO 13485:2016', '21 CFR 820']\n"
        "modules: [medical-devices]\n"
    )
    result = _run(
        ["regenerate", "--bundle", "fresh", "--write-matrix"],
        cwd=str(workdir),
    )
    assert result.returncode == 0, result.stderr
    assert "baseline" in result.stdout
    assert (workdir / "bundles" / "fresh.matrix.json").exists()


def test_regenerate_reports_changes_and_exits_one(tmp_path, repo_root):
    """When the matrix differs from the prior, regenerate prints the diff
    and exits 1."""
    workdir = tmp_path / "work"
    shutil.copytree(repo_root, workdir, symlinks=True, ignore=shutil.ignore_patterns(
        ".git", ".venv*", "BUSINESS", "__pycache__", "*.egg-info",
        ".pytest_cache", "site"
    ))
    # First write the baseline with all 5 standards
    (workdir / "bundles" / "drift.yaml").write_text(
        "name: drift\n"
        "product: DriftDevice\n"
        "jurisdictions: [FDA]\n"
        "standards: ['ISO 13485:2016', '21 CFR 820', 'ISO 14971:2019', 'IEC 62304:2006+A1:2015', 'ISO/IEC 27001:2022']\n"
        "modules: [medical-devices, iso-27001]\n"
    )
    r1 = _run(
        ["regenerate", "--bundle", "drift", "--write-matrix"],
        cwd=str(workdir),
    )
    assert r1.returncode == 0, r1.stderr

    # Now narrow the bundle (drop ISO 14971 + IEC 62304 + ISO 27001)
    (workdir / "bundles" / "drift.yaml").write_text(
        "name: drift\n"
        "product: DriftDevice\n"
        "jurisdictions: [FDA]\n"
        "standards: ['ISO 13485:2016', '21 CFR 820']\n"
        "modules: [medical-devices]\n"
    )
    r2 = _run(["regenerate", "--bundle", "drift"], cwd=str(workdir))
    assert r2.returncode == 1, (
        f"expected exit 1 (changes); got {r2.returncode}. "
        f"stdout:\n{r2.stdout}\nstderr:\n{r2.stderr}"
    )
    # Should mention removed standards and clauses
    assert "Standards:" in r2.stdout
    assert "- ISO 14971:2019" in r2.stdout
    assert "In-scope clauses:" in r2.stdout


def test_regenerate_dry_run_does_not_write_matrix(tmp_path, repo_root):
    """Without --write-matrix, the file is not touched even when there
    are changes."""
    workdir = tmp_path / "work"
    shutil.copytree(repo_root, workdir, symlinks=True, ignore=shutil.ignore_patterns(
        ".git", ".venv*", "BUSINESS", "__pycache__", "*.egg-info",
        ".pytest_cache", "site"
    ))
    (workdir / "bundles" / "dr.yaml").write_text(
        "name: dr\n"
        "product: DryDevice\n"
        "jurisdictions: [FDA]\n"
        "standards: ['ISO 13485:2016']\n"
        "modules: [medical-devices]\n"
    )
    r1 = _run(
        ["regenerate", "--bundle", "dr", "--write-matrix"],
        cwd=str(workdir),
    )
    assert r1.returncode == 0
    matrix_path = workdir / "bundles" / "dr.matrix.json"
    original_text = matrix_path.read_text()

    # Change the bundle, run without --write-matrix
    (workdir / "bundles" / "dr.yaml").write_text(
        "name: dr\n"
        "product: DryDevice\n"
        "jurisdictions: [FDA]\n"
        "standards: ['ISO 13485:2016', '21 CFR 820']\n"
        "modules: [medical-devices]\n"
    )
    r2 = _run(["regenerate", "--bundle", "dr"], cwd=str(workdir))
    assert r2.returncode == 1
    # Matrix file unchanged
    assert matrix_path.read_text() == original_text


def test_regenerate_unknown_bundle_raises(repo_root):
    result = _run(
        ["regenerate", "--bundle", "definitely-not-a-bundle"],
        cwd=str(repo_root),
    )
    assert result.returncode != 0
    assert "not found" in result.stderr.lower()


# ─── edition supersession (OQ-065) ──────────────────────────────────────


def test_validate_warns_on_superseded_standard(tmp_path, repo_root):
    """When a registry entry carries superseded_by, validate prints a
    warning by default and still exits 0."""
    workdir = tmp_path / "work"
    shutil.copytree(repo_root, workdir, symlinks=True, ignore=shutil.ignore_patterns(
        ".git", ".venv*", "BUSINESS", "__pycache__", "*.egg-info",
        ".pytest_cache", "site"
    ))
    # Patch the registry so ISO 13485:2016 is superseded by a hypothetical 2026 edition
    standards = (workdir / "registry" / "standards.yaml").read_text()
    standards = standards.replace(
        'aliases:\n      - "ISO 13485"\n      - "ISO13485"',
        'aliases:\n      - "ISO13485"\n    superseded_by: "ISO 13485:2026"',
        1,
    )
    # Add the successor entry
    standards += (
        '\n  - id: "ISO 13485:2026"\n'
        '    name: "Medical devices QMS (2026 edition)"\n'
        '    publisher: ISO\n'
        '    edition: "2026"\n'
        '    kind: standard\n'
        '    license_kind: commercial\n'
        '    aliases:\n'
        '      - "ISO 13485"\n'
    )
    (workdir / "registry" / "standards.yaml").write_text(standards)

    r = _run(
        ["validate", "--module", "medical-devices"],
        cwd=str(workdir),
    )
    # Default (no --strict-editions) → exit 0 with a warning on stderr
    assert r.returncode == 0, (
        f"expected default-mode pass; got {r.returncode}. "
        f"stderr:\n{r.stderr}"
    )
    assert "superseded" in r.stderr.lower()


def test_validate_strict_editions_fails_on_superseded_standard(tmp_path, repo_root):
    """Under --strict-editions, supersession becomes an error."""
    workdir = tmp_path / "work"
    shutil.copytree(repo_root, workdir, symlinks=True, ignore=shutil.ignore_patterns(
        ".git", ".venv*", "BUSINESS", "__pycache__", "*.egg-info",
        ".pytest_cache", "site"
    ))
    standards = (workdir / "registry" / "standards.yaml").read_text()
    standards = standards.replace(
        'aliases:\n      - "ISO 13485"\n      - "ISO13485"',
        'aliases:\n      - "ISO13485"\n    superseded_by: "ISO 13485:2026"',
        1,
    )
    standards += (
        '\n  - id: "ISO 13485:2026"\n'
        '    name: "Medical devices QMS (2026 edition)"\n'
        '    publisher: ISO\n'
        '    edition: "2026"\n'
        '    kind: standard\n'
        '    license_kind: commercial\n'
        '    aliases:\n'
        '      - "ISO 13485"\n'
    )
    (workdir / "registry" / "standards.yaml").write_text(standards)

    r = _run(
        ["validate", "--module", "medical-devices", "--strict-editions"],
        cwd=str(workdir),
    )
    assert r.returncode == 2, (
        f"expected --strict-editions to fail; got {r.returncode}. "
        f"stderr:\n{r.stderr}"
    )
    assert "superseded" in r.stderr.lower()
