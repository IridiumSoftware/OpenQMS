"""Tests for engine/openqms/template_schema.py — P9 deliverable v0.58.0."""

from __future__ import annotations

from pathlib import Path
from textwrap import dedent

import pytest

from openqms.template_schema import (
    DATE_FIELD_ANY_OF,
    RECOGNIZED_STATUSES,
    REQUIRED_FIELDS,
    Finding,
    LintResult,
    discover_templates,
    lint_template,
    lint_templates,
    parse_frontmatter,
    validate_frontmatter,
)


# ---------------- parse_frontmatter ----------------


def test_parse_frontmatter_present():
    text = dedent("""\
        ---
        document_id: TEST-001
        version: "1.0"
        ---

        # Body
        """)
    parsed = parse_frontmatter(text)
    assert parsed == {"document_id": "TEST-001", "version": "1.0"}


def test_parse_frontmatter_absent():
    text = "# No frontmatter here\n\nJust markdown.\n"
    assert parse_frontmatter(text) is None


def test_parse_frontmatter_unclosed():
    text = "---\ndocument_id: X\n\n# missing close marker\n"
    assert parse_frontmatter(text) is None


def test_parse_frontmatter_yaml_error():
    text = "---\n  : : : invalid yaml\n---\n"
    parsed = parse_frontmatter(text)
    assert parsed == {"__yaml_error__": True}


# ---------------- validate_frontmatter ----------------


def _good_frontmatter() -> dict:
    return {
        "document_id": "TEST-001",
        "version": "1.0",
        "effective_date": "2026-05-25",
        "owner": "Test Owner",
        "status": "draft",
    }


def test_validate_clean_passes():
    findings = validate_frontmatter(Path("x.md"), _good_frontmatter())
    assert findings == []


def test_validate_missing_required_fields():
    for field_name, _ in REQUIRED_FIELDS:
        fm = _good_frontmatter()
        del fm[field_name]
        findings = validate_frontmatter(Path("x.md"), fm)
        error_messages = [f.message for f in findings if f.severity == "error"]
        assert any(field_name in msg for msg in error_messages), (
            f"expected error for missing {field_name}"
        )


def test_validate_missing_date_field():
    fm = _good_frontmatter()
    del fm["effective_date"]
    findings = validate_frontmatter(Path("x.md"), fm)
    error_messages = [f.message for f in findings if f.severity == "error"]
    assert any("missing date field" in msg for msg in error_messages)


def test_validate_alternate_date_field_accepted():
    for date_field in DATE_FIELD_ANY_OF:
        fm = _good_frontmatter()
        del fm["effective_date"]
        fm[date_field] = "2026-05-25"
        findings = validate_frontmatter(Path("x.md"), fm)
        date_errors = [
            f for f in findings if "missing date field" in f.message and f.severity == "error"
        ]
        assert date_errors == [], f"date field {date_field} should be accepted"


def test_validate_placeholder_date_accepted():
    """The literal placeholder 'YYYY-MM-DD' is acceptable in template files."""
    fm = _good_frontmatter()
    fm["effective_date"] = "YYYY-MM-DD"
    findings = validate_frontmatter(Path("x.md"), fm)
    date_errors = [f for f in findings if "effective_date" in f.message and f.severity == "error"]
    assert date_errors == []


def test_validate_bad_version_pattern():
    fm = _good_frontmatter()
    fm["version"] = "not-semver"
    findings = validate_frontmatter(Path("x.md"), fm)
    assert any("version" in f.message and f.severity == "error" for f in findings)


def test_validate_version_two_and_three_part_both_ok():
    for v in ("1.0", "1.0.0", "0.1.0", "2.3.4"):
        fm = _good_frontmatter()
        fm["version"] = v
        findings = validate_frontmatter(Path("x.md"), fm)
        version_errors = [f for f in findings if "version" in f.message and f.severity == "error"]
        assert version_errors == [], f"version {v} should be accepted"


def test_validate_bad_document_id():
    fm = _good_frontmatter()
    fm["document_id"] = "has spaces"
    findings = validate_frontmatter(Path("x.md"), fm)
    assert any("document_id" in f.message and f.severity == "error" for f in findings)


def test_validate_document_id_leading_digit_ok():
    """510K-XXX-style IDs (regulator-defined leading-digit prefixes) accepted."""
    fm = _good_frontmatter()
    fm["document_id"] = "510K-XXX"
    findings = validate_frontmatter(Path("x.md"), fm)
    doc_id_errors = [f for f in findings if "document_id" in f.message and f.severity == "error"]
    assert doc_id_errors == []


def test_validate_document_id_bracket_placeholder_ok():
    """Adopter-fillin placeholders like DI-[PRODUCT]-001 are accepted."""
    fm = _good_frontmatter()
    fm["document_id"] = "DI-[PRODUCT]-001"
    findings = validate_frontmatter(Path("x.md"), fm)
    doc_id_errors = [f for f in findings if "document_id" in f.message and f.severity == "error"]
    assert doc_id_errors == []


def test_validate_recognized_status_no_warning():
    for status in RECOGNIZED_STATUSES:
        fm = _good_frontmatter()
        fm["status"] = status
        findings = validate_frontmatter(Path("x.md"), fm)
        status_warnings = [
            f for f in findings if "status" in f.message and f.severity == "warning"
        ]
        assert status_warnings == [], f"recognized status {status} should not warn"


def test_validate_unrecognized_status_warns():
    fm = _good_frontmatter()
    fm["status"] = "weirdstate"
    findings = validate_frontmatter(Path("x.md"), fm)
    assert any("status" in f.message and f.severity == "warning" for f in findings)


def test_validate_status_with_parenthetical_qualifier_uses_head_token():
    """Real-world pattern: status: 'draft (pending NHTSA acceptance)' — accept."""
    fm = _good_frontmatter()
    fm["status"] = "draft (pending acceptance)"
    findings = validate_frontmatter(Path("x.md"), fm)
    status_warnings = [f for f in findings if "status" in f.message and f.severity == "warning"]
    assert status_warnings == []


def test_validate_extras_permitted():
    """Templates carry domain-specific fields — schema must not reject extras."""
    fm = _good_frontmatter()
    fm["recall_campaign_number"] = "26-V-001"
    fm["worker_consultation"] = "Yes — workers consulted 2026-05-01"
    fm["mock_recall_cadence"] = "Annual"
    findings = validate_frontmatter(Path("x.md"), fm)
    assert findings == []


# ---------------- lint_template + lint_templates ----------------


def test_lint_template_clean(tmp_path: Path):
    f = tmp_path / "OK.md"
    f.write_text(dedent("""\
        ---
        document_id: TEST-001
        version: "1.0"
        effective_date: "2026-05-25"
        owner: Test
        status: draft
        ---

        # body
        """))
    has_fm, findings = lint_template(f)
    assert has_fm is True
    assert findings == []


def test_lint_template_missing_frontmatter_hard_fail(tmp_path: Path):
    f = tmp_path / "BARE.md"
    f.write_text("# no frontmatter\n")
    has_fm, findings = lint_template(f, require_frontmatter=True)
    assert has_fm is False
    assert any(f.severity == "error" for f in findings)


def test_lint_template_missing_frontmatter_soft_warn(tmp_path: Path):
    f = tmp_path / "BARE.md"
    f.write_text("# no frontmatter\n")
    has_fm, findings = lint_template(f, require_frontmatter=False)
    assert has_fm is False
    assert all(f.severity == "warning" for f in findings)


def test_lint_templates_aggregates(tmp_path: Path):
    good = tmp_path / "OK.md"
    good.write_text(dedent("""\
        ---
        document_id: TEST-001
        version: "1.0"
        effective_date: "2026-05-25"
        owner: Test
        status: draft
        ---
        """))
    bad = tmp_path / "BARE.md"
    bad.write_text("# no frontmatter\n")
    result = lint_templates([good, bad])
    assert result.files_scanned == 2
    assert result.files_with_frontmatter == 1
    assert result.files_without_frontmatter == 1
    assert len(result.errors) >= 1


# ---------------- repo-wide invariant ----------------


def test_repo_templates_all_pass():
    """All shipped templates pass schema validation at HEAD.

    If this test fails, a recently committed template has bad
    frontmatter — fix the template OR explicitly opt-out via a path
    exclusion (currently no exclusion mechanism — fix the template).
    """
    repo_root = Path(__file__).resolve().parent.parent.parent
    templates_root = repo_root / "templates"
    assert templates_root.exists(), f"templates root not found at {templates_root}"
    templates = discover_templates(templates_root)
    assert len(templates) > 0, "no templates discovered"
    result = lint_templates(templates, require_frontmatter=True)
    if result.errors:
        msg = "\n".join(f"  {f.path}: {f.message}" for f in result.errors)
        pytest.fail(f"{len(result.errors)} template schema error(s):\n{msg}")
