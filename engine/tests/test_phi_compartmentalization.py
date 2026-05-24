"""Tests for PHI/PII compartmentalization architecture (OQ-062).

Asserts the complaint intake template structurally cannot capture PHI:
- No field id/label matches PHI/PII patterns
- The PHI-handling warning block is present in the template body
"""

from __future__ import annotations

import re
from pathlib import Path

import yaml


REPO_ROOT = Path(__file__).resolve().parents[2]
COMPLAINT_TEMPLATE = REPO_ROOT / ".github" / "ISSUE_TEMPLATE" / "complaint.yml"


# Regex patterns that would indicate a PHI/PII field. Match either id or
# label. Anchored with word boundaries where it matters to avoid false
# positives.
PHI_FIELD_PATTERNS = [
    re.compile(r"\bpatient[_\s-]?(name|id|dob|birth|email|phone|address|mrn)\b", re.I),
    re.compile(r"\bcomplainant[_\s-]?(name|email|phone|address)\b", re.I),
    re.compile(r"\bssn\b", re.I),
    re.compile(r"\bmrn\b", re.I),
    re.compile(r"\bdate[_\s-]?of[_\s-]?birth\b", re.I),
    re.compile(r"\b(home|street|mailing)[_\s-]?address\b", re.I),
    re.compile(r"\b(personal|contact)[_\s-]?(email|phone|telephone)\b", re.I),
]


def _load_complaint_template() -> dict:
    assert COMPLAINT_TEMPLATE.is_file(), (
        f"complaint template missing at {COMPLAINT_TEMPLATE}"
    )
    return yaml.safe_load(COMPLAINT_TEMPLATE.read_text(encoding="utf-8"))


def _walk_form_fields(template: dict) -> list[dict]:
    """Return the input/textarea/dropdown/checkboxes fields (excludes
    type=markdown blocks which are display-only)."""
    out = []
    for item in template.get("body", []):
        if item.get("type") in {"input", "textarea", "dropdown", "checkboxes"}:
            out.append(item)
    return out


def test_complaint_template_loads_as_valid_yaml():
    template = _load_complaint_template()
    assert "name" in template
    assert "body" in template
    assert isinstance(template["body"], list)


def test_complaint_template_has_no_phi_fields():
    """OQ-062 architectural claim: the complaint intake is structurally
    incapable of capturing PHI. No field id or label may match a PHI/PII
    pattern."""
    template = _load_complaint_template()
    violations: list[tuple[str, str, str]] = []
    for field in _walk_form_fields(template):
        fid = field.get("id", "") or ""
        flabel = (field.get("attributes") or {}).get("label", "") or ""
        for pattern in PHI_FIELD_PATTERNS:
            if pattern.search(fid):
                violations.append((fid, flabel, f"id matches {pattern.pattern}"))
            if pattern.search(flabel):
                violations.append((fid, flabel, f"label matches {pattern.pattern}"))
    assert not violations, (
        f"PHI-capture-shaped fields found in complaint template: {violations}"
    )


def test_complaint_template_carries_phi_handling_warning():
    """OQ-062 evidence-of-discipline: the intake form must include an
    explicit PHI-handling disclaimer in the body so adopters cannot
    accidentally treat the issue as a PHI-bearing record."""
    template = _load_complaint_template()
    warning_phrases = ("phi", "pii", "do not")
    markdown_blocks = [
        ((item.get("attributes") or {}).get("value") or "").lower()
        for item in template.get("body", [])
        if item.get("type") == "markdown"
    ]
    combined = "\n".join(markdown_blocks)
    assert all(phrase in combined for phrase in warning_phrases), (
        "complaint template missing PHI handling warning. Expected all of "
        f"{warning_phrases} in markdown body blocks. Got: {combined[:300]!r}"
    )


def test_complaint_template_references_external_phi_record():
    """OQ-062 architectural pattern (A) + (B): the template must point
    adopters to an external access-restricted record for PHI-bearing
    detail, by ID/path reference — not by content."""
    template = _load_complaint_template()
    body_text = "\n".join(
        ((item.get("attributes") or {}).get("value") or "")
        for item in template.get("body", [])
    ).lower()
    field_text = "\n".join(
        ((field.get("attributes") or {}).get("label") or "")
        + " "
        + ((field.get("attributes") or {}).get("description") or "")
        for field in _walk_form_fields(template)
    ).lower()
    combined = body_text + "\n" + field_text
    indicators = ["private", "external", "ephi", "encrypted", "restricted", "eqms"]
    assert any(ind in combined for ind in indicators), (
        "complaint template missing reference to external PHI compartment "
        f"(expected one of {indicators})"
    )
