"""Tests for openqms.signatures — 21 CFR Part 11 §11.50 signature-meaning
prototype (OQ-060)."""

from __future__ import annotations

import json
import subprocess
import sys
from pathlib import Path

import pytest

from openqms.signatures import (
    SignatureTrailer,
    export_audit_trail,
    extract_signatures_from_repo,
    parse_signature_trailers,
    signature_from_commit_data,
)


# ─── unit tests on the parser ───────────────────────────────────────────


def test_parse_signature_trailers_basic():
    msg = """Approve quality policy v2

Body explanation.

Signature-Meaning: approved
Signature-Role: QA-Lead

Signed-off-by: Aaron Green <aaron@example.com>
"""
    trailers = parse_signature_trailers(msg)
    assert trailers["Signature-Meaning"] == "approved"
    assert trailers["Signature-Role"] == "QA-Lead"


def test_parse_signature_trailers_empty_returns_empty():
    assert parse_signature_trailers("Just a subject\n") == {}


def test_parse_signature_trailers_handles_justification():
    msg = (
        "Subject\n\n"
        "Signature-Meaning: reviewed\n"
        "Signature-Justification: ISO 13485 §4.2.4 check complete.\n"
    )
    t = parse_signature_trailers(msg)
    assert t["Signature-Justification"] == "ISO 13485 §4.2.4 check complete."


def test_parse_ignores_unrelated_lines():
    msg = (
        "Subject\n\n"
        "Co-Authored-By: someone\n"
        "Signature-Meaning: approved\n"
        "Some unrelated line: with a colon\n"
    )
    t = parse_signature_trailers(msg)
    assert "Signature-Meaning" in t
    assert "Co-Authored-By" not in t


# ─── unit tests on signature_from_commit_data ───────────────────────────


def test_returns_none_without_meaning_trailer():
    sig = signature_from_commit_data(
        sha="abc",
        message="No trailers here.",
        author_name="Aaron",
        author_email="a@example.com",
        authored_at="2026-05-23T12:00:00+00:00",
    )
    assert sig is None


def test_constructs_signature_with_full_trailer_set():
    msg = (
        "Approve doc\n\n"
        "Signature-Meaning: approved\n"
        "Signature-Role: QA-Lead\n"
        "Signature-Justification: Meets ISO 13485 §4.2.4.\n"
    )
    sig = signature_from_commit_data(
        sha="abc123",
        message=msg,
        author_name="Aaron Green",
        author_email="aaron@example.com",
        authored_at="2026-05-23T12:00:00+00:00",
        gpg_status="G",
        gpg_key_id="KEY123",
    )
    assert sig is not None
    assert sig.meaning == "approved"
    assert sig.role == "QA-Lead"
    assert sig.justification == "Meets ISO 13485 §4.2.4."
    assert sig.signer_name == "Aaron Green"
    assert sig.signer_email == "aaron@example.com"
    assert sig.commit_sha == "abc123"
    assert sig.gpg_verified is True
    assert sig.gpg_signer_key_id == "KEY123"


@pytest.mark.parametrize(
    "status,expected",
    [
        ("G", True),
        ("U", True),
        ("B", False),
        ("X", False),
        ("Y", False),
        ("R", False),
        ("E", False),
        ("N", False),
        ("", False),
    ],
)
def test_gpg_status_codes(status, expected):
    sig = signature_from_commit_data(
        sha="abc",
        message="x\n\nSignature-Meaning: approved\n",
        author_name="A",
        author_email="a@e.com",
        authored_at="2026-05-23T12:00:00+00:00",
        gpg_status=status,
    )
    assert sig is not None
    assert sig.gpg_verified is expected


# ─── unit tests on export_audit_trail ───────────────────────────────────


def _make_signature(**overrides):
    base = dict(
        meaning="approved",
        role="QA-Lead",
        justification="Meets ISO 13485 §4.2.4.",
        signer_name="Aaron Green",
        signer_email="aaron@example.com",
        signed_at="2026-05-23T12:00:00+00:00",
        commit_sha="abc123",
        gpg_verified=True,
        gpg_signer_key_id="KEY123",
    )
    base.update(overrides)
    return SignatureTrailer(**base)


def test_export_audit_trail_has_part11_fields():
    sig = _make_signature()
    record = export_audit_trail([sig])[0]
    # §11.50 minimums
    assert record["name"] == "Aaron Green"
    assert record["datetime"] == "2026-05-23T12:00:00+00:00"
    assert record["meaning"] == "approved"
    # extras
    assert record["role"] == "QA-Lead"
    assert record["justification"] == "Meets ISO 13485 §4.2.4."
    # §11.70 binding
    assert record["record"]["type"] == "git_commit"
    assert record["record"]["sha"] == "abc123"
    assert record["verification"]["gpg_signed"] is True
    assert record["verification"]["gpg_key_id"] == "KEY123"


def test_export_audit_trail_handles_missing_optional_fields():
    sig = _make_signature(role=None, justification=None, gpg_signer_key_id=None)
    record = export_audit_trail([sig])[0]
    assert record["role"] is None
    assert record["justification"] is None
    assert record["verification"]["gpg_key_id"] is None


# ─── integration test against a tmp git repo ────────────────────────────


def _git(args, cwd, env=None, check=True):
    base_env = {
        "GIT_AUTHOR_NAME": "Test Author",
        "GIT_AUTHOR_EMAIL": "test@example.com",
        "GIT_COMMITTER_NAME": "Test Author",
        "GIT_COMMITTER_EMAIL": "test@example.com",
        "GIT_CONFIG_NOSYSTEM": "1",
        "HOME": str(cwd),
    }
    if env:
        base_env.update(env)
    return subprocess.run(
        ["git", *args],
        cwd=str(cwd),
        capture_output=True,
        text=True,
        check=check,
        env=base_env,
    )


def _make_tmp_repo(tmp_path):
    repo = tmp_path / "repo"
    repo.mkdir()
    _git(["init", "-q", "-b", "main"], cwd=repo)
    _git(["config", "commit.gpgsign", "false"], cwd=repo)
    return repo


def test_extract_signatures_from_tmp_repo(tmp_path):
    repo = _make_tmp_repo(tmp_path)

    # 1: no signature trailers
    (repo / "f1.md").write_text("hello\n")
    _git(["add", "f1.md"], cwd=repo)
    _git(["commit", "-q", "-m", "Initial commit"], cwd=repo)

    # 2: with a Signature-Meaning trailer
    (repo / "f1.md").write_text("hello v2\n")
    _git(["add", "f1.md"], cwd=repo)
    msg2 = (
        "Approve update\n\n"
        "Signature-Meaning: approved\n"
        "Signature-Role: QA-Lead\n"
        "Signature-Justification: Reviewed against SOP-001.\n"
    )
    _git(["commit", "-q", "-m", msg2], cwd=repo)

    # 3: no trailer
    (repo / "f2.md").write_text("another\n")
    _git(["add", "f2.md"], cwd=repo)
    _git(["commit", "-q", "-m", "Unrelated change"], cwd=repo)

    sigs = extract_signatures_from_repo(repo)
    assert len(sigs) == 1
    s = sigs[0]
    assert s.meaning == "approved"
    assert s.role == "QA-Lead"
    assert s.justification == "Reviewed against SOP-001."
    assert s.signer_name == "Test Author"
    assert s.signer_email == "test@example.com"
    # commits are not GPG-signed in the test repo
    assert s.gpg_verified is False


def test_extract_signatures_respects_path_filter(tmp_path):
    repo = _make_tmp_repo(tmp_path)
    (repo / "controlled").mkdir()
    (repo / "uncontrolled").mkdir()

    # Signed commit touching controlled path
    (repo / "controlled" / "policy.md").write_text("v1\n")
    _git(["add", "."], cwd=repo)
    _git(
        ["commit", "-q", "-m",
         "Approve policy\n\nSignature-Meaning: approved\n"],
        cwd=repo,
    )

    # Signed commit touching uncontrolled path
    (repo / "uncontrolled" / "scratch.md").write_text("notes\n")
    _git(["add", "."], cwd=repo)
    _git(
        ["commit", "-q", "-m",
         "Approve scratch\n\nSignature-Meaning: approved\n"],
        cwd=repo,
    )

    sigs = extract_signatures_from_repo(repo, paths=["controlled"])
    assert len(sigs) == 1
    sigs_all = extract_signatures_from_repo(repo)
    assert len(sigs_all) == 2


# ─── CLI subprocess integration ─────────────────────────────────────────


def test_cli_signatures_export_against_tmp_repo(tmp_path):
    repo = _make_tmp_repo(tmp_path)
    (repo / "f.md").write_text("v1\n")
    _git(["add", "."], cwd=repo)
    _git(
        ["commit", "-q", "-m",
         "Approve\n\nSignature-Meaning: approved\nSignature-Role: QA-Lead\n"],
        cwd=repo,
    )

    out = tmp_path / "trail.json"
    result = subprocess.run(
        [
            sys.executable, "-m", "openqms", "signatures", "export",
            "--output", str(out),
        ],
        cwd=str(repo),
        capture_output=True,
        text=True,
    )
    assert result.returncode == 0, result.stderr
    records = json.loads(out.read_text())
    assert len(records) == 1
    assert records[0]["meaning"] == "approved"
    assert records[0]["role"] == "QA-Lead"
    assert records[0]["record"]["type"] == "git_commit"


def test_cli_signatures_verify_passes_on_signed_commit(tmp_path):
    repo = _make_tmp_repo(tmp_path)
    (repo / "f.md").write_text("v1\n")
    _git(["add", "."], cwd=repo)
    _git(
        ["commit", "-q", "-m",
         "Approve\n\nSignature-Meaning: approved\n"],
        cwd=repo,
    )

    result = subprocess.run(
        [sys.executable, "-m", "openqms", "signatures", "verify"],
        cwd=str(repo),
        capture_output=True,
        text=True,
    )
    assert result.returncode == 0, result.stderr
    assert "approved" in result.stdout


def test_cli_signatures_verify_fails_without_trailer(tmp_path):
    repo = _make_tmp_repo(tmp_path)
    (repo / "f.md").write_text("v1\n")
    _git(["add", "."], cwd=repo)
    _git(["commit", "-q", "-m", "Plain commit, no trailers"], cwd=repo)

    result = subprocess.run(
        [sys.executable, "-m", "openqms", "signatures", "verify"],
        cwd=str(repo),
        capture_output=True,
        text=True,
    )
    assert result.returncode == 1
    assert "Signature-Meaning" in result.stderr


def test_cli_signatures_verify_require_gpg_fails_on_unsigned(tmp_path):
    repo = _make_tmp_repo(tmp_path)
    (repo / "f.md").write_text("v1\n")
    _git(["add", "."], cwd=repo)
    _git(
        ["commit", "-q", "-m",
         "Approve\n\nSignature-Meaning: approved\n"],
        cwd=repo,
    )

    result = subprocess.run(
        [
            sys.executable, "-m", "openqms", "signatures", "verify",
            "--require-gpg",
        ],
        cwd=str(repo),
        capture_output=True,
        text=True,
    )
    assert result.returncode == 1
    assert "GPG" in result.stderr or "gpg" in result.stderr.lower()
