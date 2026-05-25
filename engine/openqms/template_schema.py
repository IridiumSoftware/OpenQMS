"""Template frontmatter schema validation.

Closes compliance-architecture forward-work P9 (template files have no
schema validation today; only module.yaml is linted via
scripts/lint-module-yaml.py).

Schema parallels the module-YAML validation pattern: required-field
list + per-field type/format check + permissive on extras (templates
carry domain-specific fields like recall_campaign_number,
worker_consultation, mock_recall_cadence — schema must not reject
these).

Conventions in force:
- Frontmatter is YAML between two `---` lines at the very top of the
  file (line 1 is `---`; closing `---` may appear at any subsequent
  line; YAML body is everything in between).
- All fields are snake_case strings unless otherwise typed.
- `addresses:` is the binding to in-module clause IDs; values must
  exist as clause IDs in at least one module that references the
  template (cross-checked by scripts/lint-module-yaml.py — not this
  schema).

NOTE on the migration from soft-warn to hard-fail: at v0.58.0 (when
this lands), all 105 shipped templates carry frontmatter. The linter
runs hard-fail mode (missing frontmatter exits 1). Before extending
this gate, ensure new templates carry frontmatter — see
docs/guide/doc-control.md (forward work) and the new
docs/guide/template-frontmatter.md companion.
"""

from __future__ import annotations

import re
from dataclasses import dataclass, field
from pathlib import Path
from typing import Iterable

try:
    import yaml
except ImportError as exc:
    raise ImportError(
        "PyYAML required: pip install pyyaml (or uv sync --frozen in engine/)"
    ) from exc


# Required fields per template frontmatter.
# (Field name, human-readable description for error messages.)
REQUIRED_FIELDS: tuple[tuple[str, str], ...] = (
    ("document_id", "stable identifier for the document, e.g., SOP-IDM-001"),
    ("version", "semver or version string, e.g., 0.1.0 or 1.0"),
    ("owner", "role or named individual who owns this document"),
    ("status", "document state: draft | review | approved | effective | superseded"),
)


# At least one of these date fields is required.
# Document-control templates typically use effective_date (SOPs, policies)
# or issued_date (notification letters, one-shot records).
# Record-style templates (deviation, OOS, change-control) use
# opened_date or assessment_date etc.
# Schema accepts any one — the per-template author picks the most
# appropriate for that record kind.
DATE_FIELD_ANY_OF: tuple[str, ...] = (
    "effective_date",
    "issued_date",
    "issue_date",
    "opened_date",
    "assessment_date",
    "notification_date",
    "approval_date",
)


# Recognized status values. Two lifecycle families coexist:
#   Document lifecycle: draft → review → approved → effective → superseded
#   Record lifecycle:   open → closed (or open → cancelled)
# Forward-work P5 (doc-control hardening) will narrow these per
# document-kind via state-machine enforcement.
RECOGNIZED_STATUSES: frozenset[str] = frozenset({
    # document-control lifecycle
    "draft",
    "review",
    "approved",
    "effective",
    "superseded",
    # record lifecycle (deviation, OOS, change-control, traceability)
    "open",
    "closed",
    "cancelled",
})


# version pattern — accepts X.Y or X.Y.Z (semver-ish). Templates use
# both ("1.0" + "0.1.0" are both in the wild).
_VERSION_RE = re.compile(r"^\d+\.\d+(\.\d+)?$")


# document_id pattern — alphanumeric + hyphens + underscores + bracket
# placeholders for adopter fill-in (e.g., "DI-[PRODUCT]-001"). Allows
# leading digit (e.g., "510K-XXX") because some regulator-defined IDs
# start with digits.
_DOCUMENT_ID_RE = re.compile(r"^[A-Za-z0-9][A-Za-z0-9_\-\[\]]*$")


# date pattern — YYYY-MM-DD or placeholder "YYYY-MM-DD".
_DATE_RE = re.compile(r"^(\d{4}-\d{2}-\d{2}|YYYY-MM-DD)$")


@dataclass
class Finding:
    """One linter finding against one template file."""

    path: Path
    severity: str  # "error" or "warning"
    message: str


@dataclass
class LintResult:
    """Aggregate linter outcome for a set of templates."""

    files_scanned: int = 0
    files_with_frontmatter: int = 0
    files_without_frontmatter: int = 0
    findings: list[Finding] = field(default_factory=list)

    @property
    def errors(self) -> list[Finding]:
        return [f for f in self.findings if f.severity == "error"]

    @property
    def warnings(self) -> list[Finding]:
        return [f for f in self.findings if f.severity == "warning"]


def parse_frontmatter(text: str) -> dict | None:
    """Return parsed YAML frontmatter dict, or None if no frontmatter present.

    A template has frontmatter iff line 1 is exactly `---` and a
    subsequent line is `---`. Lines between are parsed as YAML.
    """
    if not text.startswith("---\n"):
        return None
    rest = text[4:]
    close_marker = rest.find("\n---")
    if close_marker == -1:
        return None
    yaml_body = rest[:close_marker]
    try:
        parsed = yaml.safe_load(yaml_body)
    except yaml.YAMLError:
        # Malformed YAML in frontmatter — caller treats this as an error.
        return {"__yaml_error__": True}
    if not isinstance(parsed, dict):
        return {"__not_a_dict__": True}
    return parsed


def validate_frontmatter(path: Path, frontmatter: dict) -> list[Finding]:
    """Validate a parsed frontmatter dict against the schema.

    Returns a list of Findings (empty list = clean).
    """
    findings: list[Finding] = []

    if frontmatter.get("__yaml_error__"):
        findings.append(Finding(path, "error", "YAML frontmatter failed to parse"))
        return findings

    if frontmatter.get("__not_a_dict__"):
        findings.append(
            Finding(path, "error", "YAML frontmatter did not parse to a dict (got a list or scalar)")
        )
        return findings

    # Required fields presence
    for field_name, description in REQUIRED_FIELDS:
        if field_name not in frontmatter:
            findings.append(
                Finding(path, "error", f"missing required field `{field_name}` ({description})")
            )

    # At least one of the date fields
    if not any(f in frontmatter for f in DATE_FIELD_ANY_OF):
        findings.append(
            Finding(
                path,
                "error",
                f"missing date field — one of {list(DATE_FIELD_ANY_OF)} is required",
            )
        )

    # Per-field format checks
    if "document_id" in frontmatter:
        value = frontmatter["document_id"]
        if not isinstance(value, str) or not _DOCUMENT_ID_RE.match(value):
            findings.append(
                Finding(
                    path,
                    "error",
                    f"document_id `{value!r}` must match {_DOCUMENT_ID_RE.pattern}",
                )
            )

    if "version" in frontmatter:
        value = frontmatter["version"]
        # Allow quoted strings — YAML may parse "1.0" as float; coerce.
        str_value = str(value)
        if not _VERSION_RE.match(str_value):
            findings.append(
                Finding(
                    path,
                    "error",
                    f"version `{value!r}` must match X.Y or X.Y.Z",
                )
            )

    for date_field in DATE_FIELD_ANY_OF:
        if date_field in frontmatter:
            value = frontmatter[date_field]
            str_value = str(value)
            if not _DATE_RE.match(str_value):
                findings.append(
                    Finding(
                        path,
                        "error",
                        f"{date_field} `{value!r}` must be YYYY-MM-DD (or the literal placeholder 'YYYY-MM-DD')",
                    )
                )

    if "status" in frontmatter:
        value = frontmatter["status"]
        # status may have a parenthetical qualifier in the wild
        # (e.g., "draft (pending NHTSA acceptance)"); accept the first
        # whitespace-separated token as the canonical state.
        if isinstance(value, str):
            canonical = value.split()[0].lower() if value.strip() else ""
            if canonical and canonical not in RECOGNIZED_STATUSES:
                findings.append(
                    Finding(
                        path,
                        "warning",
                        f"status `{value!r}` head token `{canonical}` not in {sorted(RECOGNIZED_STATUSES)}",
                    )
                )

    # Owner should be non-empty string
    if "owner" in frontmatter:
        value = frontmatter["owner"]
        if not isinstance(value, str) or not value.strip():
            findings.append(
                Finding(path, "error", f"owner must be non-empty string, got {value!r}")
            )

    return findings


def lint_template(path: Path, require_frontmatter: bool = True) -> tuple[bool, list[Finding]]:
    """Lint a single template file.

    Returns (has_frontmatter, findings).
    If require_frontmatter is True and the file has none, returns a
    findings entry of severity error. If False, severity warning.
    """
    text = path.read_text()
    frontmatter = parse_frontmatter(text)
    if frontmatter is None:
        severity = "error" if require_frontmatter else "warning"
        return False, [
            Finding(
                path,
                severity,
                "no YAML frontmatter (first line must be '---' followed by YAML body then '---')",
            )
        ]
    return True, validate_frontmatter(path, frontmatter)


def lint_templates(
    paths: Iterable[Path], require_frontmatter: bool = True
) -> LintResult:
    """Lint a set of template files; return aggregated LintResult."""
    result = LintResult()
    for path in sorted(paths):
        result.files_scanned += 1
        has_fm, findings = lint_template(path, require_frontmatter=require_frontmatter)
        if has_fm:
            result.files_with_frontmatter += 1
        else:
            result.files_without_frontmatter += 1
        result.findings.extend(findings)
    return result


def discover_templates(root: Path) -> list[Path]:
    """Find all *.md template files under root (typically `templates/`)."""
    return [p for p in root.rglob("*.md") if p.is_file()]
