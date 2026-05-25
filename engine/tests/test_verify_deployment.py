"""Tests for engine/openqms/verify_deployment.py — P11 deliverable v0.62.0."""

from __future__ import annotations

from pathlib import Path
from textwrap import dedent

import pytest
import yaml

from openqms.verify_deployment import (
    Finding,
    VerifyResult,
    format_result_text,
    load_policy,
    verify_branch_protection,
    verify_codeowners,
    verify_deployment,
)


# ---------------- load_policy ----------------


def test_load_policy_clean(tmp_path: Path):
    path = tmp_path / "policy.yaml"
    path.write_text(dedent("""\
        repo:
          owner: my-org
          name: my-qms
          branch: main
        branch_protection:
          require_signed_commits: true
    """))
    policy = load_policy(path)
    assert policy["repo"]["owner"] == "my-org"
    assert policy["branch_protection"]["require_signed_commits"] is True


def test_load_policy_missing_file(tmp_path: Path):
    with pytest.raises(FileNotFoundError):
        load_policy(tmp_path / "no-such.yaml")


def test_load_policy_missing_top_level_repo(tmp_path: Path):
    path = tmp_path / "policy.yaml"
    path.write_text("branch_protection:\n  require_signed_commits: true\n")
    with pytest.raises(ValueError, match="repo"):
        load_policy(path)


def test_load_policy_missing_repo_subkey(tmp_path: Path):
    path = tmp_path / "policy.yaml"
    path.write_text(dedent("""\
        repo:
          owner: my-org
        branch_protection: {}
    """))
    # missing both `name` and `branch`; raises on the first one detected
    with pytest.raises(ValueError, match="name|branch"):
        load_policy(path)


# ---------------- verify_branch_protection ----------------


def _bp_policy(**overrides) -> dict:
    base = {
        "repo": {"owner": "x", "name": "y", "branch": "main"},
        "branch_protection": {
            "required_pull_request_reviews": {
                "required_approving_review_count": 1,
                "require_code_owner_reviews": True,
                "dismiss_stale_reviews": True,
            },
            "required_status_checks": {
                "strict": True,
                "contexts": ["ci/required", "ci/lint"],
            },
            "require_signed_commits": True,
            "enforce_admins": True,
            "required_linear_history": True,
            "allow_force_pushes": False,
            "allow_deletions": False,
        },
    }
    base["branch_protection"].update(overrides)
    return base


def _all_good_response() -> dict:
    return {
        "required_pull_request_reviews": {
            "required_approving_review_count": 2,
            "require_code_owner_reviews": True,
            "dismiss_stale_reviews": True,
        },
        "required_status_checks": {
            "strict": True,
            "contexts": ["ci/required", "ci/lint", "extra/check"],
        },
        "require_signed_commits": {"enabled": True},
        "enforce_admins": {"enabled": True},
        "required_linear_history": {"enabled": True},
        "allow_force_pushes": {"enabled": False},
        "allow_deletions": {"enabled": False},
    }


def test_branch_protection_all_pass():
    findings = verify_branch_protection(_bp_policy(), _all_good_response())
    assert findings == []


def test_branch_protection_review_count_too_low():
    response = _all_good_response()
    response["required_pull_request_reviews"]["required_approving_review_count"] = 0
    findings = verify_branch_protection(_bp_policy(), response)
    assert any("required_approving_review_count" in f.message for f in findings)


def test_branch_protection_codeowners_disabled():
    response = _all_good_response()
    response["required_pull_request_reviews"]["require_code_owner_reviews"] = False
    findings = verify_branch_protection(_bp_policy(), response)
    assert any("require_code_owner_reviews" in f.message for f in findings)


def test_branch_protection_signed_commits_disabled():
    response = _all_good_response()
    response["require_signed_commits"] = {"enabled": False}
    findings = verify_branch_protection(_bp_policy(), response)
    assert any("require_signed_commits" in f.message for f in findings)


def test_branch_protection_force_push_enabled_flagged():
    response = _all_good_response()
    response["allow_force_pushes"] = {"enabled": True}
    findings = verify_branch_protection(_bp_policy(), response)
    assert any("allow_force_pushes" in f.message for f in findings)


def test_branch_protection_required_status_check_missing():
    response = _all_good_response()
    response["required_status_checks"]["contexts"] = ["ci/required"]  # ci/lint missing
    findings = verify_branch_protection(_bp_policy(), response)
    assert any("ci/lint" in f.message for f in findings)


def test_branch_protection_strict_disabled():
    response = _all_good_response()
    response["required_status_checks"]["strict"] = False
    findings = verify_branch_protection(_bp_policy(), response)
    assert any("strict" in f.message for f in findings)


def test_branch_protection_dismiss_stale_disabled():
    response = _all_good_response()
    response["required_pull_request_reviews"]["dismiss_stale_reviews"] = False
    findings = verify_branch_protection(_bp_policy(), response)
    assert any("dismiss_stale_reviews" in f.message for f in findings)


def test_branch_protection_enforce_admins_disabled():
    response = _all_good_response()
    response["enforce_admins"] = {"enabled": False}
    findings = verify_branch_protection(_bp_policy(), response)
    assert any("enforce_admins" in f.message for f in findings)


# ---------------- verify_codeowners ----------------


def _codeowners_policy(paths: list[str]) -> dict:
    return {
        "repo": {"owner": "x", "name": "y", "branch": "main"},
        "branch_protection": {},
        "codeowners": {"required_paths": paths},
    }


def test_codeowners_empty_file_fails():
    findings = verify_codeowners(_codeowners_policy(["modules/"]), "")
    assert any("empty" in f.message for f in findings)


def test_codeowners_missing_required_path():
    text = dedent("""\
        # comment
        *  @org/quality

        /docs/  @org/docs
    """)
    findings = verify_codeowners(_codeowners_policy(["modules/", "templates/"]), text)
    # Wildcard catch-all covers modules/ + templates/ via the * pattern
    # so neither should fail
    assert findings == []


def test_codeowners_no_wildcard_no_match_fails():
    text = dedent("""\
        /docs/  @org/docs
        /scripts/  @org/eng
    """)
    findings = verify_codeowners(_codeowners_policy(["modules/"]), text)
    assert any("modules/" in f.message for f in findings)


def test_codeowners_required_path_with_explicit_entry():
    text = dedent("""\
        /modules/  @org/quality
        /templates/  @org/quality
    """)
    findings = verify_codeowners(_codeowners_policy(["modules/", "templates/"]), text)
    assert findings == []


# ---------------- verify_deployment orchestrator (with fake gh) ----------------


def test_verify_deployment_all_pass(tmp_path: Path):
    codeowners = tmp_path / "CODEOWNERS"
    codeowners.write_text("*  @org/quality\n/modules/ @org/quality\n")
    policy = {
        "repo": {"owner": "x", "name": "y", "branch": "main"},
        "branch_protection": {
            "require_signed_commits": True,
            "allow_force_pushes": False,
        },
        "codeowners": {"required_paths": ["modules/"]},
    }
    fake_gh = lambda endpoint: _all_good_response()
    result = verify_deployment(policy, gh_invoker=fake_gh, codeowners_path=codeowners)
    assert result.passed is True
    assert result.errors == []


def test_verify_deployment_bp_fails(tmp_path: Path):
    codeowners = tmp_path / "CODEOWNERS"
    codeowners.write_text("*  @org/quality\n")
    policy = {
        "repo": {"owner": "x", "name": "y", "branch": "main"},
        "branch_protection": {"require_signed_commits": True},
    }
    fake_gh = lambda endpoint: {"require_signed_commits": {"enabled": False}}
    result = verify_deployment(policy, gh_invoker=fake_gh, codeowners_path=codeowners)
    assert result.passed is False
    assert any("require_signed_commits" in f.message for f in result.errors)


def test_verify_deployment_codeowners_missing(tmp_path: Path):
    policy = {
        "repo": {"owner": "x", "name": "y", "branch": "main"},
        "branch_protection": {},
        "codeowners": {"required_paths": ["modules/"]},
    }
    fake_gh = lambda endpoint: {}
    # Pass an explicit non-existent path so the default-search doesn't find
    # the project's own CODEOWNERS file.
    nonexistent = tmp_path / "no-such-CODEOWNERS"
    result = verify_deployment(policy, gh_invoker=fake_gh, codeowners_path=nonexistent)
    assert result.passed is False
    assert any("CODEOWNERS" in f.message for f in result.errors)


def test_verify_deployment_gh_api_failure(tmp_path: Path):
    """API failure surfaces as a finding, not an exception."""
    codeowners = tmp_path / "CODEOWNERS"
    codeowners.write_text("*  @org/quality\n")
    policy = {
        "repo": {"owner": "x", "name": "y", "branch": "main"},
        "branch_protection": {"require_signed_commits": True},
    }
    def failing_gh(endpoint):
        raise RuntimeError("simulated gh api failure")
    result = verify_deployment(policy, gh_invoker=failing_gh, codeowners_path=codeowners)
    assert result.passed is False
    assert any("failed to query" in f.message for f in result.errors)


# ---------------- format_result_text ----------------


def test_format_result_text_pass():
    out = format_result_text(VerifyResult())
    assert "PASS" in out


def test_format_result_text_with_errors():
    result = VerifyResult(findings=[
        Finding("error", "branch_protection", "missing thing"),
        Finding("warning", "codeowners", "soft warning"),
    ])
    out = format_result_text(result)
    assert "1 error(s)" in out
    assert "1 warning(s)" in out
    assert "missing thing" in out
    assert "soft warning" in out
