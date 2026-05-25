#!/usr/bin/env python3
"""Lint template frontmatter — parallel CI gate to lint-module-yaml.py.

Closes compliance-architecture forward-work P9 at v0.58.0.

Validates every `templates/**/*.md` file against the schema defined in
`engine/openqms/template_schema.py`:

- Required fields: document_id, version, owner, status, + one of
  (effective_date | issued_date)
- Format checks: version is X.Y or X.Y.Z; dates are YYYY-MM-DD or the
  literal placeholder; document_id is alphanumeric + hyphens +
  underscores; status head token in the recognized set
- Extras permitted: templates carry domain-specific fields
  (recall_campaign_number, worker_consultation, mock_recall_cadence,
  etc.) — schema must not reject these

Exit codes:
  0 — all templates pass schema
  1 — at least one error (hard-fail mode)

Warnings are reported but do not affect exit code.

Usage:
  python3 scripts/lint-template-frontmatter.py [<templates-root>]

Default <templates-root> is `templates/`.
"""

from __future__ import annotations

import sys
from pathlib import Path

# Allow running directly without installing the engine
sys.path.insert(0, str(Path(__file__).resolve().parent.parent / "engine"))

from openqms.template_schema import (
    discover_templates,
    lint_templates,
)


def main() -> int:
    root = Path(sys.argv[1] if len(sys.argv) > 1 else "templates")
    if not root.exists():
        print(f"error: templates root {root} not found", file=sys.stderr)
        return 1

    templates = discover_templates(root)
    if not templates:
        print(f"error: no *.md files found under {root}", file=sys.stderr)
        return 1

    result = lint_templates(templates, require_frontmatter=True)

    if result.errors:
        print(f"FAIL: {len(result.errors)} error(s) across {result.files_scanned} template(s)")
        for finding in result.errors:
            print(f"  error: {finding.path}: {finding.message}")
    if result.warnings:
        print(f"WARN: {len(result.warnings)} warning(s)")
        for finding in result.warnings:
            print(f"  warn:  {finding.path}: {finding.message}")
    if not result.errors and not result.warnings:
        print(
            f"lint ok: {result.files_scanned} template(s) scanned; "
            f"{result.files_with_frontmatter} with frontmatter; 0 findings"
        )
    elif not result.errors:
        print(
            f"lint ok (with warnings): {result.files_scanned} template(s) scanned; "
            f"{result.files_with_frontmatter} with frontmatter"
        )

    return 1 if result.errors else 0


if __name__ == "__main__":
    sys.exit(main())
