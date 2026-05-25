"""Tests for engine/openqms/doc_control.py — P5 deliverable v0.60.0."""

from __future__ import annotations

import json
from pathlib import Path

import pytest

from openqms.doc_control import (
    ALLOWED_TRANSITIONS,
    NON_VERSION_TRIGGERING_FIELDS,
    AuditArtifact,
    FileCheck,
    build_audit_artifact,
    changed_fields,
    check_file,
    check_state_transition,
    check_version_drift,
    format_audit_markdown,
    needs_version_bump,
)


# ---------------- check_state_transition ----------------


def test_state_transition_self_allowed():
    for state in ALLOWED_TRANSITIONS:
        assert check_state_transition(state, state) is None


def test_state_transition_new_file_any_status_allowed():
    for state in ALLOWED_TRANSITIONS:
        assert check_state_transition(None, state) is None


def test_state_transition_removal_disallowed():
    err = check_state_transition("approved", None)
    assert err is not None
    assert "status field removed" in err


def test_state_transition_draft_to_review():
    assert check_state_transition("draft", "review") is None


def test_state_transition_review_to_approved():
    assert check_state_transition("review", "approved") is None


def test_state_transition_approved_to_effective():
    assert check_state_transition("approved", "effective") is None


def test_state_transition_effective_to_superseded():
    assert check_state_transition("effective", "superseded") is None


def test_state_transition_superseded_is_terminal():
    err = check_state_transition("superseded", "draft")
    assert err is not None
    assert "invalid state transition" in err


def test_state_transition_draft_to_effective_disallowed():
    """Cannot skip review + approval."""
    err = check_state_transition("draft", "effective")
    assert err is not None
    assert "draft" in err and "effective" in err


def test_state_transition_open_to_closed():
    assert check_state_transition("open", "closed") is None


def test_state_transition_open_to_cancelled():
    assert check_state_transition("open", "cancelled") is None


def test_state_transition_closed_is_terminal():
    err = check_state_transition("closed", "open")
    assert err is not None


def test_state_transition_strips_parenthetical_qualifier():
    """status: 'draft (pending NHTSA acceptance)' head token is 'draft'."""
    assert check_state_transition("draft (pending acceptance)", "review") is None


def test_state_transition_unrecognized_old_status_passes():
    """Schema-lint catches unrecognized statuses; state machine is silent."""
    assert check_state_transition("weirdstate", "approved") is None


# ---------------- changed_fields + needs_version_bump ----------------


def test_changed_fields_detects_value_change():
    base = {"a": 1, "b": 2}
    head = {"a": 1, "b": 999}
    assert changed_fields(base, head) == ["b"]


def test_changed_fields_detects_added_field():
    base = {"a": 1}
    head = {"a": 1, "b": 2}
    assert changed_fields(base, head) == ["b"]


def test_changed_fields_detects_removed_field():
    base = {"a": 1, "b": 2}
    head = {"a": 1}
    assert changed_fields(base, head) == ["b"]


def test_needs_version_bump_housekeeping_only():
    """last_review_date + next_review changes do NOT require version bump."""
    assert needs_version_bump(["last_review_date"]) is False
    assert needs_version_bump(["next_review"]) is False
    assert needs_version_bump(["last_review_date", "next_review", "status"]) is False


def test_needs_version_bump_substantive_change():
    assert needs_version_bump(["owner"]) is True
    assert needs_version_bump(["effective_date"]) is True
    assert needs_version_bump(["title", "last_review_date"]) is True


# ---------------- check_version_drift ----------------


def test_version_drift_draft_exempt():
    """draft documents may iterate without version bump."""
    base = {"version": "1.0", "status": "draft", "owner": "A"}
    head = {"version": "1.0", "status": "draft", "owner": "B"}  # substantive change
    assert check_version_drift(base, head, "body", "body changed") is None


def test_version_drift_substantive_change_requires_bump():
    base = {"version": "1.0", "status": "approved", "owner": "A"}
    head = {"version": "1.0", "status": "approved", "owner": "B"}
    err = check_version_drift(base, head, "body", "body")
    assert err is not None
    assert "substantive change without version increment" in err


def test_version_drift_substantive_change_with_bump_ok():
    base = {"version": "1.0", "status": "approved", "owner": "A"}
    head = {"version": "1.1", "status": "approved", "owner": "B"}
    assert check_version_drift(base, head, "body", "body") is None


def test_version_drift_housekeeping_only_no_bump_required():
    base = {"version": "1.0", "status": "effective", "last_review_date": "2025-01-01"}
    head = {"version": "1.0", "status": "effective", "last_review_date": "2026-05-25"}
    assert check_version_drift(base, head, "body", "body") is None


def test_version_drift_body_change_requires_bump():
    """A change to body text outside frontmatter triggers the rule too."""
    base = {"version": "1.0", "status": "approved"}
    head = {"version": "1.0", "status": "approved"}
    err = check_version_drift(base, head, "old body", "new body")
    assert err is not None


def test_version_drift_version_downgrade_rejected():
    base = {"version": "2.0", "status": "approved"}
    head = {"version": "1.5", "status": "approved"}
    err = check_version_drift(base, head, "body", "body different")
    assert err is not None


def test_version_drift_three_part_version_handled():
    base = {"version": "1.2.3", "status": "approved", "owner": "A"}
    head = {"version": "1.2.4", "status": "approved", "owner": "B"}
    assert check_version_drift(base, head, "body", "body") is None


def test_version_drift_malformed_version_caught():
    base = {"version": "not-semver", "status": "approved"}
    head = {"version": "not-semver", "status": "approved", "owner": "different"}
    err = check_version_drift(base, head, "body", "body")
    assert err is not None
    assert "missing or malformed" in err


# ---------------- check_file end-to-end ----------------


def _doc(version: str, status: str, owner: str = "Test", extra_body: str = "body") -> str:
    return f"""\
---
document_id: TEST-001
version: "{version}"
effective_date: "2026-05-25"
owner: "{owner}"
status: {status}
---

{extra_body}
"""


def test_check_file_new_file_ok():
    check = check_file(Path("x.md"), None, _doc("1.0", "draft"))
    assert check.passed is True
    assert check.head_version == "1.0"
    assert check.head_status == "draft"
    assert check.base_version is None


def test_check_file_missing_frontmatter_fails():
    check = check_file(Path("x.md"), None, "# no frontmatter\n")
    assert check.passed is False
    assert any("missing YAML frontmatter" in e for e in check.errors)


def test_check_file_invalid_state_transition_fails():
    base = _doc("1.0", "approved")
    head = _doc("1.1", "draft")  # approved → draft IS allowed (rollback)
    check = check_file(Path("x.md"), base, head)
    assert check.passed is True  # approved → draft is allowed
    # but approved → review is NOT in transitions...
    # Actually let's check superseded → effective (not allowed)
    base2 = _doc("1.0", "superseded")
    head2 = _doc("1.1", "effective", extra_body="different")
    check2 = check_file(Path("x.md"), base2, head2)
    assert check2.passed is False
    assert any("invalid state transition" in e for e in check2.errors)


def test_check_file_substantive_change_no_bump_fails():
    base = _doc("1.0", "approved", owner="A")
    head = _doc("1.0", "approved", owner="B")
    check = check_file(Path("x.md"), base, head)
    assert check.passed is False
    assert any("version increment" in e for e in check.errors)


def test_check_file_substantive_change_with_bump_passes():
    base = _doc("1.0", "approved", owner="A")
    head = _doc("1.1", "approved", owner="B")
    check = check_file(Path("x.md"), base, head)
    assert check.passed is True


def test_check_file_draft_iteration_allowed():
    """Draft documents may iterate freely."""
    base = _doc("0.1", "draft", owner="A", extra_body="rough draft")
    head = _doc("0.1", "draft", owner="B", extra_body="rougher draft")
    check = check_file(Path("x.md"), base, head)
    assert check.passed is True


def test_check_file_records_changed_fields():
    base = _doc("1.0", "approved", owner="A")
    head = _doc("1.1", "approved", owner="B")
    check = check_file(Path("x.md"), base, head)
    assert "owner" in check.changed_fields
    assert "version" in check.changed_fields


# ---------------- audit artifact ----------------


def test_build_audit_artifact_empty():
    artifact = build_audit_artifact(
        pr_number=42,
        commit_sha="abc123",
        base_ref="main",
        head_ref="feature",
        file_checks=[],
        signature_trailers=[],
        ci_status="pass",
    )
    assert artifact.pr_number == 42
    assert artifact.commit_sha == "abc123"
    assert artifact.ci_status == "pass"
    assert artifact.files_checked == []


def test_audit_artifact_to_dict_serializable():
    artifact = build_audit_artifact(
        pr_number=42,
        commit_sha="abc123",
        base_ref="main",
        head_ref="feature",
        file_checks=[FileCheck(path=Path("x.md"))],
        signature_trailers=[{"sha": "abc", "meaning": "Approved", "role": "QM", "justification": ""}],
        ci_status="pass",
    )
    serialized = json.dumps(artifact.to_dict())
    decoded = json.loads(serialized)
    assert decoded["pr_number"] == 42
    assert decoded["files"][0]["path"] == "x.md"
    assert decoded["signature_trailers"][0]["meaning"] == "Approved"


def test_format_audit_markdown_empty_section():
    artifact = build_audit_artifact(
        pr_number=42,
        commit_sha="abc123",
        base_ref="main",
        head_ref="feature",
        file_checks=[],
        signature_trailers=[],
        ci_status="pass",
    )
    md = format_audit_markdown(artifact)
    assert "## Doc-control audit artifact" in md
    assert "No controlled-document files changed" in md
    assert "No `Signature-Meaning:` trailers found" in md


def test_format_audit_markdown_with_files_and_trailers():
    fc = FileCheck(
        path=Path("qms-policy/quality-manual.md"),
        base_version="1.0",
        head_version="1.1",
        base_status="approved",
        head_status="approved",
        changed_fields=["owner", "version"],
    )
    artifact = build_audit_artifact(
        pr_number=42,
        commit_sha="abc123",
        base_ref="main",
        head_ref="feature",
        file_checks=[fc],
        signature_trailers=[
            {"sha": "abc123", "meaning": "Approved", "role": "QM", "justification": "annual review"}
        ],
        ci_status="pass",
    )
    md = format_audit_markdown(artifact)
    assert "qms-policy/quality-manual.md" in md
    assert "1.0" in md and "1.1" in md
    assert "Approved" in md
    assert "QM" in md
