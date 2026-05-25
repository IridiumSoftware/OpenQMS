"""Document-control state machine + version-drift + audit-artifact.

Closes compliance-architecture forward-work P5 (v0.60.0):

- Replaces shell/grep frontmatter parsing in `.github/workflows/doc-control.yml`
  with PyYAML schema-validated parsing via `openqms.template_schema`.
- Hard-fails version drift on controlled documents (was warning-only).
- Enforces document state-transition rules per the two lifecycle
  families recognized by the schema:
    Document lifecycle: draft → review → approved → effective → superseded
    Record lifecycle:   open → closed (or cancelled)
- Builds an audit-artifact JSON per PR with: commit SHA + per-file
  frontmatter delta + state-transition outcomes + signature-meaning
  trailers parsed from commits + CI gate summary.

Conventions in force:
- Status head-token is what the state machine checks; parenthetical
  qualifiers (e.g., "draft (pending NHTSA acceptance)") are stripped.
- Version-drift rule: any frontmatter change that is NOT a status-only
  bump from `draft → review`/`review → draft` AND is NOT a
  `last_review_date` bump REQUIRES a version increment.
- Version comparison: lexicographic on dotted-integer tuples; equal-or-
  lower is a violation.
- `draft` documents are exempt from version-drift (drafting is iterative).
"""

from __future__ import annotations

from dataclasses import dataclass, field
from pathlib import Path
from typing import Iterable

from openqms.template_schema import RECOGNIZED_STATUSES, parse_frontmatter


# --------- State-transition rules ---------

# Allowed transitions. Self-transitions are always allowed (a PR may
# not change status). The lists name what the state may TRANSITION TO.
ALLOWED_TRANSITIONS: dict[str, frozenset[str]] = {
    # Document lifecycle
    "draft":      frozenset({"draft", "review", "superseded"}),
    "review":     frozenset({"review", "draft", "approved", "superseded"}),
    "approved":   frozenset({"approved", "effective", "draft", "superseded"}),
    "effective":  frozenset({"effective", "superseded", "draft"}),
    "superseded": frozenset({"superseded"}),
    # Record lifecycle
    "open":      frozenset({"open", "closed", "cancelled"}),
    "closed":    frozenset({"closed"}),
    "cancelled": frozenset({"cancelled"}),
}


# Fields whose changes do NOT require a version bump (housekeeping).
NON_VERSION_TRIGGERING_FIELDS: frozenset[str] = frozenset({
    "last_review_date",
    "next_review",
    "status",  # status change handled separately by state machine
})


# --------- Data structures ---------


@dataclass
class FileCheck:
    """Aggregate outcome of doc-control checks for one file."""

    path: Path
    errors: list[str] = field(default_factory=list)
    warnings: list[str] = field(default_factory=list)
    base_version: str | None = None
    head_version: str | None = None
    base_status: str | None = None
    head_status: str | None = None
    changed_fields: list[str] = field(default_factory=list)

    @property
    def passed(self) -> bool:
        return not self.errors


@dataclass
class AuditArtifact:
    """JSON-serializable PR audit summary."""

    pr_number: int | None
    commit_sha: str
    base_ref: str
    head_ref: str
    files_checked: list[FileCheck]
    signature_trailers: list[dict]  # parsed from openqms signatures export
    ci_status: str  # "pass" | "fail" | "pending"

    def to_dict(self) -> dict:
        return {
            "pr_number": self.pr_number,
            "commit_sha": self.commit_sha,
            "base_ref": self.base_ref,
            "head_ref": self.head_ref,
            "ci_status": self.ci_status,
            "files": [
                {
                    "path": str(fc.path),
                    "passed": fc.passed,
                    "base_version": fc.base_version,
                    "head_version": fc.head_version,
                    "base_status": fc.base_status,
                    "head_status": fc.head_status,
                    "changed_fields": fc.changed_fields,
                    "errors": fc.errors,
                    "warnings": fc.warnings,
                }
                for fc in self.files_checked
            ],
            "signature_trailers": self.signature_trailers,
        }


# --------- Helpers ---------


def _strip_status_qualifier(status: str | None) -> str | None:
    """Return the head token of a status string (strip parenthetical qualifier)."""
    if status is None:
        return None
    return str(status).split()[0].lower() if status.strip() else None


def _parse_version_tuple(version: str | None) -> tuple[int, ...] | None:
    """Parse 'X.Y' or 'X.Y.Z' to a tuple of ints; None on bad input."""
    if version is None:
        return None
    try:
        return tuple(int(p) for p in str(version).split("."))
    except (ValueError, AttributeError):
        return None


# --------- State-transition check ---------


def check_state_transition(old_status: str | None, new_status: str | None) -> str | None:
    """Return error message if transition is invalid, else None.

    A None → X transition (new file) is always allowed.
    A X → None transition (status removed) is always an error.
    Unrecognized status values pass the state-machine check but will
    have been caught by the template schema already.
    """
    old = _strip_status_qualifier(old_status)
    new = _strip_status_qualifier(new_status)

    if new is None:
        return "status field removed; controlled docs must declare status"

    if old is None:
        # New file — any starting status is valid as long as it's recognized
        return None

    if old not in RECOGNIZED_STATUSES:
        # Old status wasn't recognized — no transition rule applies;
        # template-schema lint will have caught the cause already.
        return None

    allowed = ALLOWED_TRANSITIONS.get(old, frozenset())
    if new not in allowed:
        return (
            f"invalid state transition: {old!r} → {new!r}; "
            f"allowed from {old!r}: {sorted(allowed)}"
        )
    return None


# --------- Version-drift check ---------


def changed_fields(base_fm: dict, head_fm: dict) -> list[str]:
    """Return list of field names whose values differ between base + head."""
    all_keys = set(base_fm) | set(head_fm)
    return sorted(k for k in all_keys if base_fm.get(k) != head_fm.get(k))


def needs_version_bump(changed: Iterable[str]) -> bool:
    """True iff at least one substantive (non-housekeeping) field changed."""
    return any(field not in NON_VERSION_TRIGGERING_FIELDS for field in changed)


def check_version_drift(
    base_fm: dict, head_fm: dict, base_text: str = "", head_text: str = ""
) -> str | None:
    """Return error if substantive change without version bump, else None.

    Exempt: documents in `draft` status (iterative drafting allowed).
    Trigger: a substantive frontmatter change OR a body change (text
    outside frontmatter) without version increment.
    """
    head_status = _strip_status_qualifier(head_fm.get("status"))
    if head_status == "draft":
        # Draft documents are exempt
        return None

    changed = changed_fields(base_fm, head_fm)
    body_changed = base_text != head_text
    substantive_fm_changed = needs_version_bump(changed)

    if not substantive_fm_changed and not body_changed:
        # No substantive change; version bump not required
        return None

    base_v = _parse_version_tuple(base_fm.get("version"))
    head_v = _parse_version_tuple(head_fm.get("version"))

    if base_v is None or head_v is None:
        return (
            f"version field missing or malformed; cannot verify increment "
            f"(base={base_fm.get('version')!r} head={head_fm.get('version')!r})"
        )

    if head_v <= base_v:
        return (
            f"substantive change without version increment: "
            f"version {base_fm.get('version')!r} → {head_fm.get('version')!r}; "
            f"controlled documents in status {head_status!r} require a version bump "
            f"(changed fields: {changed})"
        )

    return None


# --------- Per-file check ---------


def check_file(path: Path, base_text: str | None, head_text: str) -> FileCheck:
    """Run all doc-control checks against one file's base vs head content.

    base_text=None means the file is newly added in this PR.
    """
    check = FileCheck(path=path)

    head_fm = parse_frontmatter(head_text)
    if head_fm is None:
        check.errors.append("missing YAML frontmatter")
        return check
    if head_fm.get("__yaml_error__"):
        check.errors.append("YAML frontmatter failed to parse")
        return check
    if head_fm.get("__not_a_dict__"):
        check.errors.append("YAML frontmatter is not a mapping")
        return check

    check.head_version = head_fm.get("version")
    check.head_status = _strip_status_qualifier(head_fm.get("status"))

    if base_text is None:
        # New file — state-transition rule trivially passes (None → X);
        # version-drift rule does not apply.
        if check.head_status not in RECOGNIZED_STATUSES and check.head_status is not None:
            check.warnings.append(
                f"new file status {check.head_status!r} not in recognized set "
                f"{sorted(RECOGNIZED_STATUSES)}"
            )
        return check

    base_fm = parse_frontmatter(base_text)
    if base_fm is None or base_fm.get("__yaml_error__") or base_fm.get("__not_a_dict__"):
        # Base couldn't be parsed — treat as new
        check.warnings.append(
            "base ref frontmatter could not be parsed; treating as new file"
        )
        return check

    check.base_version = base_fm.get("version")
    check.base_status = _strip_status_qualifier(base_fm.get("status"))
    check.changed_fields = changed_fields(base_fm, head_fm)

    # State-transition check
    transition_error = check_state_transition(check.base_status, check.head_status)
    if transition_error:
        check.errors.append(transition_error)

    # Version-drift check (HARD FAIL — change from v0.55.0 era warn-only)
    drift_error = check_version_drift(base_fm, head_fm, base_text, head_text)
    if drift_error:
        check.errors.append(drift_error)

    return check


# --------- Audit-artifact builder ---------


def build_audit_artifact(
    pr_number: int | None,
    commit_sha: str,
    base_ref: str,
    head_ref: str,
    file_checks: list[FileCheck],
    signature_trailers: list[dict],
    ci_status: str,
) -> AuditArtifact:
    """Assemble an AuditArtifact from per-file results + sig trailers + CI."""
    return AuditArtifact(
        pr_number=pr_number,
        commit_sha=commit_sha,
        base_ref=base_ref,
        head_ref=head_ref,
        files_checked=file_checks,
        signature_trailers=signature_trailers,
        ci_status=ci_status,
    )


def format_audit_markdown(artifact: AuditArtifact) -> str:
    """Render the audit artifact as a Markdown PR comment."""
    lines = [
        "## Doc-control audit artifact",
        "",
        f"- PR: #{artifact.pr_number}" if artifact.pr_number else "- PR: (no number)",
        f"- Commit: `{artifact.commit_sha}`",
        f"- Base → head: `{artifact.base_ref}` → `{artifact.head_ref}`",
        f"- CI status: **{artifact.ci_status}**",
        "",
        "### File checks",
        "",
    ]
    if not artifact.files_checked:
        lines.append("_No controlled-document files changed._")
    else:
        lines.append("| File | Pass | Version Δ | Status Δ | Errors | Warnings |")
        lines.append("|---|---|---|---|---|---|")
        for fc in artifact.files_checked:
            mark = "✓" if fc.passed else "✗"
            vdelta = (
                f"`{fc.base_version}` → `{fc.head_version}`"
                if fc.base_version != fc.head_version
                else f"`{fc.head_version}`"
            )
            sdelta = (
                f"`{fc.base_status}` → `{fc.head_status}`"
                if fc.base_status != fc.head_status
                else f"`{fc.head_status}`"
            )
            err_count = len(fc.errors)
            warn_count = len(fc.warnings)
            lines.append(
                f"| `{fc.path}` | {mark} | {vdelta} | {sdelta} | {err_count} | {warn_count} |"
            )

        # Detail block for any errors/warnings
        for fc in artifact.files_checked:
            if fc.errors or fc.warnings:
                lines.append("")
                lines.append(f"#### `{fc.path}`")
                for e in fc.errors:
                    lines.append(f"- **error:** {e}")
                for w in fc.warnings:
                    lines.append(f"- warning: {w}")

    lines.extend([
        "",
        "### Signature trailers",
        "",
    ])
    if not artifact.signature_trailers:
        lines.append("_No `Signature-Meaning:` trailers found on PR commits._")
    else:
        lines.append("| Commit | Meaning | Role | Justification |")
        lines.append("|---|---|---|---|")
        for trailer in artifact.signature_trailers:
            lines.append(
                f"| `{trailer.get('sha', '?')[:7]}` "
                f"| {trailer.get('meaning', '—')} "
                f"| {trailer.get('role', '—')} "
                f"| {trailer.get('justification', '—')} |"
            )

    lines.extend([
        "",
        "---",
        "_Generated by `.github/workflows/doc-control.yml` (P5 hardening — v0.60.0). "
        "See `engine/openqms/doc_control.py` + `docs/guide/doc-control.md`._",
    ])
    return "\n".join(lines)
