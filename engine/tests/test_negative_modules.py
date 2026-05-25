"""Negative-path test suite for bad modules — P10 (v0.59.0).

Closes compliance-architecture forward-work P10. The validation
harness + loader + linter all reject invalid inputs at runtime, but
prior to this suite there was no curated set of intentionally-broken
modules paired with assertions about the specific error messages
produced. Without those assertions, a refactor that subtly weakens an
error path could land silently.

Coverage by category:

  Loader (engine/openqms/module.py::load_module):
    - missing required top-level fields
    - top-level fields with wrong type (list vs dict)
    - missing required per-clause fields
    - missing required per-template fields
    - per-template addresses with wrong type
    - module file not found

  Compose (engine/openqms/module.py::compose):
    - empty input
    - conflicting clauses across modules

  Validation harness (engine/openqms/validation.py::validate):
    - orphan clause (no template binds it)
    - orphan template (addresses unknown clause)

  Linter (scripts/lint-module-yaml.py::_lint_one):
    - YAML parse failure
    - top-level not a mapping
    - duplicate clause id
    - addresses references unknown clause
    - clause missing required field
    - template missing required field

Total: 22 tests across the 4 categories.

Pattern: each test writes a minimal-fixture YAML to tmp_path and
invokes the production code path. Inline-string fixtures (not
on-disk-checked-in) so the broken construction sits next to the
assertion.
"""

from __future__ import annotations

import importlib.util
import sys
from pathlib import Path

import pytest
import yaml

from openqms.module import compose, load_module
from openqms.validation import validate


# ---------------- Helper: import the lint-module-yaml.py script ----------------
# Hyphenated filename can't be imported directly; use importlib.

_LINT_SCRIPT_PATH = (
    Path(__file__).resolve().parent.parent.parent / "scripts" / "lint-module-yaml.py"
)


def _import_linter():
    spec = importlib.util.spec_from_file_location("lint_module_yaml", _LINT_SCRIPT_PATH)
    assert spec and spec.loader, f"could not load {_LINT_SCRIPT_PATH}"
    module = importlib.util.module_from_spec(spec)
    sys.modules["lint_module_yaml"] = module
    spec.loader.exec_module(module)
    return module


def _write_module(tmp_path: Path, yaml_text: str, name: str = "module.yaml") -> Path:
    """Write a fixture YAML to tmp_path/name and return the path."""
    path = tmp_path / name
    path.write_text(yaml_text)
    return path


# ====================================================================
# CATEGORY 1 — Loader: module-level errors
# ====================================================================


def test_loader_missing_name_field(tmp_path: Path):
    path = _write_module(tmp_path, "version: 0.1.0\nclauses: []\n")
    with pytest.raises(ValueError, match="missing required field 'name'"):
        load_module(str(path))


def test_loader_clauses_not_a_list(tmp_path: Path):
    path = _write_module(
        tmp_path,
        "name: bad-mod\nversion: 0.1.0\nclauses:\n  not: a-list\n",
    )
    with pytest.raises(ValueError, match="'clauses' must be a list"):
        load_module(str(path))


def test_loader_templates_not_a_list(tmp_path: Path):
    path = _write_module(
        tmp_path,
        "name: bad-mod\nversion: 0.1.0\nclauses: []\ntemplates:\n  not: a-list\n",
    )
    with pytest.raises(ValueError, match="'templates' must be a list"):
        load_module(str(path))


def test_loader_standards_not_a_list(tmp_path: Path):
    path = _write_module(
        tmp_path,
        "name: bad-mod\nversion: 0.1.0\nstandards:\n  not: a-list\nclauses: []\n",
    )
    with pytest.raises(ValueError, match="'standards' must be a list"):
        load_module(str(path))


def test_loader_module_file_not_found(tmp_path: Path):
    with pytest.raises(FileNotFoundError, match="Module not found"):
        load_module(str(tmp_path / "does-not-exist.yaml"))


# ====================================================================
# CATEGORY 2 — Loader: per-clause errors
# ====================================================================


def test_loader_clause_missing_id(tmp_path: Path):
    path = _write_module(
        tmp_path,
        """\
name: bad-mod
version: 0.1.0
clauses:
  - standard: ISO 13485
    section: "4.2"
    summary: oops no id
""",
    )
    with pytest.raises(ValueError, match=r"Clause missing required fields.*id"):
        load_module(str(path))


def test_loader_clause_missing_standard(tmp_path: Path):
    path = _write_module(
        tmp_path,
        """\
name: bad-mod
version: 0.1.0
clauses:
  - id: C1
    section: "4.2"
    summary: oops no standard
""",
    )
    with pytest.raises(ValueError, match=r"Clause missing required fields.*standard"):
        load_module(str(path))


def test_loader_clause_missing_section(tmp_path: Path):
    path = _write_module(
        tmp_path,
        """\
name: bad-mod
version: 0.1.0
clauses:
  - id: C1
    standard: ISO 13485
    summary: oops no section
""",
    )
    with pytest.raises(ValueError, match=r"Clause missing required fields.*section"):
        load_module(str(path))


def test_loader_clause_missing_summary(tmp_path: Path):
    path = _write_module(
        tmp_path,
        """\
name: bad-mod
version: 0.1.0
clauses:
  - id: C1
    standard: ISO 13485
    section: "4.2"
""",
    )
    with pytest.raises(ValueError, match=r"Clause missing required fields.*summary"):
        load_module(str(path))


# ====================================================================
# CATEGORY 3 — Loader: per-template errors
# ====================================================================


def test_loader_template_missing_path(tmp_path: Path):
    path = _write_module(
        tmp_path,
        """\
name: bad-mod
version: 0.1.0
clauses: []
templates:
  - name: Missing path
    addresses: []
""",
    )
    with pytest.raises(ValueError, match=r"Template missing required fields.*path"):
        load_module(str(path))


def test_loader_template_missing_name(tmp_path: Path):
    path = _write_module(
        tmp_path,
        """\
name: bad-mod
version: 0.1.0
clauses: []
templates:
  - path: templates/x.md
    addresses: []
""",
    )
    with pytest.raises(ValueError, match=r"Template missing required fields.*name"):
        load_module(str(path))


def test_loader_template_addresses_not_a_list(tmp_path: Path):
    path = _write_module(
        tmp_path,
        """\
name: bad-mod
version: 0.1.0
clauses: []
templates:
  - path: templates/x.md
    name: bad
    addresses:
      not: a-list
""",
    )
    with pytest.raises(ValueError, match=r"'addresses' must be a list"):
        load_module(str(path))


# ====================================================================
# CATEGORY 4 — Compose: errors
# ====================================================================


def test_compose_empty_input():
    with pytest.raises(ValueError, match="requires at least one module"):
        compose([])


def test_compose_conflicting_clause(tmp_path: Path):
    """Same clause id, different content across modules — must reject."""
    mod_a = _write_module(
        tmp_path,
        """\
name: mod-a
version: 0.1.0
clauses:
  - id: C1
    standard: ISO 13485
    section: "4.2"
    summary: original wording
""",
        name="a.yaml",
    )
    mod_b = _write_module(
        tmp_path,
        """\
name: mod-b
version: 0.1.0
clauses:
  - id: C1
    standard: ISO 13485
    section: "4.2"
    summary: drift-introducing different wording
""",
        name="b.yaml",
    )
    a = load_module(str(mod_a))
    b = load_module(str(mod_b))
    with pytest.raises(ValueError, match=r"conflicts across modules"):
        compose([a, b])


# ====================================================================
# CATEGORY 5 — Validation harness: orphan detection
# ====================================================================


def test_validate_orphan_clause(tmp_path: Path):
    """Clause exists but no template addresses it → invariant fails."""
    path = _write_module(
        tmp_path,
        """\
name: orphan-clause-mod
version: 0.1.0
clauses:
  - id: C1
    standard: ISO 13485
    section: "4.2"
    summary: orphan — no template binds this
templates: []
""",
    )
    module = load_module(str(path))
    report = validate(module)
    assert report.invariant_holds is False
    assert "C1" in report.orphaned_clauses


def test_validate_orphan_template(tmp_path: Path):
    """Template addresses a clause id that does not exist in the module."""
    path = _write_module(
        tmp_path,
        """\
name: orphan-template-mod
version: 0.1.0
clauses:
  - id: C1
    standard: ISO 13485
    section: "4.2"
    summary: only clause
templates:
  - path: templates/x.md
    name: addresses-bad-clause
    addresses: [C-DOES-NOT-EXIST]
""",
    )
    module = load_module(str(path))
    report = validate(module)
    assert report.invariant_holds is False
    assert "templates/x.md" in report.orphaned_artifacts


# ====================================================================
# CATEGORY 6 — Linter: per-finding categories
# ====================================================================


def test_linter_yaml_parse_error(tmp_path: Path):
    """The chemicals-arc lesson: unquoted colon in template name breaks YAML parse."""
    linter = _import_linter()
    path = _write_module(
        tmp_path,
        # broken — unquoted colon-space in inline scalar at root
        "name: bad\n: : : : invalid yaml\n",
    )
    findings = linter._lint_one(path)
    assert any("YAML parse error" in f for f in findings)


def test_linter_top_level_not_a_mapping(tmp_path: Path):
    linter = _import_linter()
    path = _write_module(tmp_path, "- this is a list\n- not a mapping\n")
    findings = linter._lint_one(path)
    assert any("top-level must be a mapping" in f for f in findings)


def test_linter_duplicate_clause_id(tmp_path: Path):
    linter = _import_linter()
    path = _write_module(
        tmp_path,
        """\
name: dup-mod
version: 0.1.0
clauses:
  - id: C1
    standard: ISO 13485
    section: "4.2"
    summary: first
  - id: C1
    standard: ISO 13485
    section: "4.3"
    summary: second — id collides with first
""",
    )
    findings = linter._lint_one(path)
    assert any("duplicate clause id 'C1'" in f for f in findings)


def test_linter_addresses_unknown_clause(tmp_path: Path):
    linter = _import_linter()
    path = _write_module(
        tmp_path,
        """\
name: ghost-mod
version: 0.1.0
clauses:
  - id: C1
    standard: ISO 13485
    section: "4.2"
    summary: only real clause
templates:
  - path: templates/x.md
    name: addresses-ghost
    addresses: [C-GHOST]
""",
    )
    findings = linter._lint_one(path)
    assert any("addresses unknown clause" in f and "C-GHOST" in f for f in findings)


def test_linter_clause_missing_required_field(tmp_path: Path):
    linter = _import_linter()
    path = _write_module(
        tmp_path,
        """\
name: missing-fields-mod
version: 0.1.0
clauses:
  - id: C1
    standard: ISO 13485
    # missing section + summary
""",
    )
    findings = linter._lint_one(path)
    assert any("missing or empty 'section'" in f for f in findings)
    assert any("missing or empty 'summary'" in f for f in findings)


def test_linter_template_missing_required_field(tmp_path: Path):
    linter = _import_linter()
    path = _write_module(
        tmp_path,
        """\
name: missing-tpl-fields-mod
version: 0.1.0
clauses:
  - id: C1
    standard: ISO 13485
    section: "4.2"
    summary: real clause
templates:
  - path: templates/x.md
    # missing name + addresses
""",
    )
    findings = linter._lint_one(path)
    assert any("missing or empty 'name'" in f for f in findings)
    assert any("missing or empty 'addresses'" in f for f in findings)


# ====================================================================
# CATEGORY 7 — Composite negative paths: clause + template orphans together
# ====================================================================


def test_validate_both_orphan_kinds_simultaneously(tmp_path: Path):
    """Module with both an orphan clause AND an orphan template; both report."""
    path = _write_module(
        tmp_path,
        """\
name: double-trouble-mod
version: 0.1.0
clauses:
  - id: C1
    standard: ISO 13485
    section: "4.2"
    summary: orphan-clause (nothing addresses it)
templates:
  - path: templates/y.md
    name: addresses-nothing-real
    addresses: [C-PHANTOM]
""",
    )
    module = load_module(str(path))
    report = validate(module)
    assert report.invariant_holds is False
    assert "C1" in report.orphaned_clauses
    assert "templates/y.md" in report.orphaned_artifacts
