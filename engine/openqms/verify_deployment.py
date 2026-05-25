"""Verify-deployment — adopter-side configuration check.

Closes compliance-architecture forward-work P11 at v0.62.0.

The reviewer's deepest substantive point (`docs/compliance-architecture.md`):

> The 'immutability' and approval model are not intrinsic properties of
> the repo. They are deployment controls.

This module shores that up. Open QMS itself can't enforce branch
protection / GPG-signing / required-reviewers / required-status-checks
in an adopter's fork — those are GitHub org-level configurations under
the adopter's admin. But Open QMS CAN ship a verifier that an adopter
runs against their own fork to confirm the declared policy is actually
in force.

Pattern: adopter writes a `deployment-policy.yaml` declaring what the
deployment MUST satisfy; `openqms verify-deployment --policy <file>`
queries the GitHub API (via the `gh` CLI subprocess; no new Python
dependency) + compares actual vs declared + exits 1 on any error.

Conventions in force:
- Policy is a YAML file with three sections: `repo`, `branch_protection`,
  `codeowners` (+ optional `signature_meaning_required`).
- API calls go through `gh api` so adopters reuse existing gh CLI auth;
  the `gh_invoker` callable is injected for testability (production
  injects real subprocess invocation; tests inject canned responses).
- Findings have severity (`error` | `warning` | `info`) — exit code is
  driven by error-count, warnings are surfaced but non-blocking.
- CODEOWNERS check is local-file-only (no API needed); other checks
  call the API.
"""

from __future__ import annotations

import json
import subprocess
from dataclasses import dataclass, field
from pathlib import Path
from typing import Callable

try:
    import yaml
except ImportError as exc:
    raise ImportError(
        "PyYAML required: pip install pyyaml (or uv sync --frozen in engine/)"
    ) from exc


# --------- Data structures ---------


@dataclass
class Finding:
    """One verifier finding."""

    severity: str  # "error" | "warning" | "info"
    category: str  # "branch_protection" | "codeowners" | "signed_commits" | "status_checks"
    message: str


@dataclass
class VerifyResult:
    """Aggregate verification outcome."""

    findings: list[Finding] = field(default_factory=list)

    @property
    def errors(self) -> list[Finding]:
        return [f for f in self.findings if f.severity == "error"]

    @property
    def warnings(self) -> list[Finding]:
        return [f for f in self.findings if f.severity == "warning"]

    @property
    def passed(self) -> bool:
        return not self.errors


# --------- gh CLI invoker ---------


GhInvoker = Callable[[str], dict | list]


def real_gh_invoker(endpoint: str) -> dict | list:
    """Production gh CLI invoker — calls `gh api <endpoint>` subprocess."""
    try:
        result = subprocess.run(
            ["gh", "api", endpoint],
            capture_output=True,
            check=True,
            text=True,
        )
        return json.loads(result.stdout)
    except FileNotFoundError as exc:
        raise RuntimeError(
            "gh CLI not found. Install: https://cli.github.com/ + run `gh auth login`"
        ) from exc
    except subprocess.CalledProcessError as exc:
        raise RuntimeError(
            f"gh api {endpoint} failed: {exc.stderr.strip()}"
        ) from exc


# --------- Policy loading ---------


def load_policy(path: Path) -> dict:
    """Load + minimally validate a deployment-policy.yaml file."""
    if not path.exists():
        raise FileNotFoundError(f"deployment policy not found: {path}")
    data = yaml.safe_load(path.read_text())
    if not isinstance(data, dict):
        raise ValueError(f"deployment policy must be a YAML mapping, got {type(data).__name__}")
    for required in ("repo", "branch_protection"):
        if required not in data:
            raise ValueError(f"deployment policy missing required top-level key: {required!r}")
    repo = data["repo"]
    for key in ("owner", "name", "branch"):
        if key not in repo:
            raise ValueError(f"deployment policy `repo` missing required key: {key!r}")
    return data


# --------- Per-check functions ---------


def verify_branch_protection(
    policy: dict, api_response: dict
) -> list[Finding]:
    """Compare actual branch-protection settings vs declared policy.

    `api_response` is the JSON returned by
    `GET /repos/{owner}/{repo}/branches/{branch}/protection`.
    """
    findings: list[Finding] = []
    declared = policy.get("branch_protection", {})

    # required_pull_request_reviews — nested dict
    declared_prr = declared.get("required_pull_request_reviews", {})
    actual_prr = (api_response or {}).get("required_pull_request_reviews") or {}

    if declared_prr:
        # required_approving_review_count
        d_count = declared_prr.get("required_approving_review_count")
        a_count = actual_prr.get("required_approving_review_count")
        if d_count is not None and (a_count is None or a_count < d_count):
            findings.append(Finding(
                "error",
                "branch_protection",
                f"required_approving_review_count: declared {d_count}, actual {a_count}",
            ))

        # require_code_owner_reviews
        d_codeowners = declared_prr.get("require_code_owner_reviews")
        a_codeowners = actual_prr.get("require_code_owner_reviews")
        if d_codeowners is True and not a_codeowners:
            findings.append(Finding(
                "error",
                "branch_protection",
                "require_code_owner_reviews: declared true, actual false (CODEOWNERS not load-bearing without this)",
            ))

        # dismiss_stale_reviews
        d_dismiss = declared_prr.get("dismiss_stale_reviews")
        a_dismiss = actual_prr.get("dismiss_stale_reviews")
        if d_dismiss is True and not a_dismiss:
            findings.append(Finding(
                "error",
                "branch_protection",
                "dismiss_stale_reviews: declared true, actual false",
            ))

    # required_status_checks — nested dict + list
    declared_checks = declared.get("required_status_checks", {})
    actual_checks = (api_response or {}).get("required_status_checks") or {}

    if declared_checks:
        d_strict = declared_checks.get("strict")
        a_strict = actual_checks.get("strict")
        if d_strict is True and not a_strict:
            findings.append(Finding(
                "error",
                "status_checks",
                "required_status_checks.strict: declared true, actual false",
            ))

        d_contexts = declared_checks.get("contexts") or []
        a_contexts = set(actual_checks.get("contexts") or [])
        missing = [c for c in d_contexts if c not in a_contexts]
        for c in missing:
            findings.append(Finding(
                "error",
                "status_checks",
                f"required status check missing: {c!r}",
            ))

    # Top-level boolean flags
    flag_checks = [
        ("require_signed_commits", "signed_commits",
         "require_signed_commits is the §11.100 unique-attribution anchor"),
        ("enforce_admins", "branch_protection", None),
        ("required_linear_history", "branch_protection", None),
    ]
    for key, category, reason in flag_checks:
        if declared.get(key) is True:
            actual = (api_response or {}).get(key)
            actual_value = actual.get("enabled") if isinstance(actual, dict) else actual
            if not actual_value:
                msg = f"{key}: declared true, actual false"
                if reason:
                    msg = f"{msg} ({reason})"
                findings.append(Finding("error", category, msg))

    # Negated flags — declared false means must NOT be enabled
    negated_flags = [
        ("allow_force_pushes", "branch_protection",
         "force-pushes erode OQ-022 immutability"),
        ("allow_deletions", "branch_protection",
         "branch deletion erodes audit-trail recoverability"),
    ]
    for key, category, reason in negated_flags:
        if declared.get(key) is False:
            actual = (api_response or {}).get(key)
            actual_value = actual.get("enabled") if isinstance(actual, dict) else actual
            if actual_value:
                msg = f"{key}: declared false, actual true"
                if reason:
                    msg = f"{msg} ({reason})"
                findings.append(Finding("error", category, msg))

    return findings


def verify_codeowners(policy: dict, codeowners_text: str) -> list[Finding]:
    """Check that CODEOWNERS covers every declared required path.

    codeowners_text is the contents of the CODEOWNERS file (caller
    reads from disk; missing-file case handled by caller).
    """
    findings: list[Finding] = []
    declared = policy.get("codeowners", {})
    required_paths = declared.get("required_paths") or []

    if not codeowners_text.strip():
        findings.append(Finding(
            "error", "codeowners",
            "CODEOWNERS file empty; required-path coverage cannot be verified",
        ))
        return findings

    # Parse CODEOWNERS: each non-comment non-blank line is `<pattern> <owner>...`
    declared_patterns = []
    for line in codeowners_text.splitlines():
        line = line.strip()
        if not line or line.startswith("#"):
            continue
        parts = line.split(None, 1)
        if not parts:
            continue
        declared_patterns.append(parts[0])

    for required in required_paths:
        # A required path is "covered" if any CODEOWNERS pattern is
        # a prefix of it OR matches it as a glob — keep simple: prefix match.
        covered = any(required.startswith(p.rstrip("*").lstrip("/")) or p == required
                      or required.rstrip("/").startswith(p.rstrip("/").lstrip("/"))
                      for p in declared_patterns)
        # also check exact + with leading slash
        if not covered:
            covered = any(
                p == required or
                p.lstrip("/") == required.lstrip("/") or
                required.startswith(p.rstrip("/*").lstrip("/")) or
                p.startswith("*")  # wildcard catch-all
                for p in declared_patterns
            )
        if not covered:
            findings.append(Finding(
                "error", "codeowners",
                f"required path {required!r} has no CODEOWNERS entry",
            ))

    return findings


# --------- Orchestrator ---------


def verify_deployment(
    policy: dict,
    gh_invoker: GhInvoker = real_gh_invoker,
    codeowners_path: Path | None = None,
) -> VerifyResult:
    """Run all configured checks; aggregate findings into VerifyResult.

    gh_invoker is injected for testability.
    codeowners_path defaults to ./.github/CODEOWNERS or ./CODEOWNERS.
    """
    result = VerifyResult()

    repo = policy["repo"]
    owner = repo["owner"]
    name = repo["name"]
    branch = repo["branch"]

    # Branch-protection check
    if policy.get("branch_protection"):
        endpoint = f"/repos/{owner}/{name}/branches/{branch}/protection"
        try:
            response = gh_invoker(endpoint)
        except RuntimeError as exc:
            result.findings.append(Finding(
                "error", "branch_protection",
                f"failed to query GitHub API: {exc}",
            ))
            response = None
        if isinstance(response, dict):
            result.findings.extend(verify_branch_protection(policy, response))

    # CODEOWNERS check
    if policy.get("codeowners"):
        if codeowners_path is None:
            # Try the two conventional locations
            for candidate in [Path(".github/CODEOWNERS"), Path("CODEOWNERS"), Path("docs/CODEOWNERS")]:
                if candidate.exists():
                    codeowners_path = candidate
                    break
        if codeowners_path is None or not codeowners_path.exists():
            result.findings.append(Finding(
                "error", "codeowners",
                "CODEOWNERS file not found at .github/CODEOWNERS, CODEOWNERS, or docs/CODEOWNERS",
            ))
        else:
            text = codeowners_path.read_text()
            result.findings.extend(verify_codeowners(policy, text))

    return result


def format_result_text(result: VerifyResult) -> str:
    """Human-readable rendering of a VerifyResult."""
    lines = []
    if not result.findings:
        lines.append("verify-deployment: PASS — all declared policy items match actual configuration")
    else:
        lines.append(
            f"verify-deployment: {len(result.errors)} error(s), {len(result.warnings)} warning(s)"
        )
        for f in result.findings:
            lines.append(f"  [{f.severity}] {f.category}: {f.message}")
    return "\n".join(lines)
