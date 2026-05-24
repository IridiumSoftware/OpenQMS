#!/usr/bin/env python3
"""Lint module.yaml files for the YAML failure modes observed in the
chemicals arc (v0.36-v0.38).

Most recurrent failure: unquoted colon in a template `name:` value
parsed as a nested mapping (e.g. `name: Multi-modal: DOT + IMDG`).

Other checks:
- Every module.yaml is parseable
- Every clause has id + standard + section + summary
- Every template has path + name + addresses (non-empty)
- Every template `addresses` entry refers to an in-module clause id
- (Soft) template `name:` strings containing unescaped colons get flagged

Exit code 0 = clean; 1 = lint findings; 2 = parse error.
"""

from __future__ import annotations

import re
import sys
from pathlib import Path

import yaml


REPO_ROOT = Path(__file__).resolve().parents[1]
MODULES_ROOT = REPO_ROOT / "modules"


def _lint_one(path: Path) -> list[str]:
    findings: list[str] = []
    raw = path.read_text(encoding="utf-8")

    # Soft-fail check #1 — yaml parser
    try:
        data = yaml.safe_load(raw)
    except yaml.YAMLError as exc:
        return [f"{path}: YAML parse error — {exc}"]

    if not isinstance(data, dict):
        return [f"{path}: module.yaml top-level must be a mapping"]

    for required in ("name", "version", "clauses"):
        if required not in data:
            findings.append(f"{path}: missing required key {required!r}")

    clauses = data.get("clauses") or []
    clause_ids: set[str] = set()
    for i, c in enumerate(clauses):
        if not isinstance(c, dict):
            findings.append(f"{path}: clauses[{i}] not a mapping")
            continue
        for ck in ("id", "standard", "section", "summary"):
            if ck not in c or c[ck] in (None, ""):
                findings.append(
                    f"{path}: clauses[{i}] missing or empty {ck!r}"
                )
        if "id" in c:
            cid = c["id"]
            if cid in clause_ids:
                findings.append(f"{path}: duplicate clause id {cid!r}")
            clause_ids.add(cid)

    templates = data.get("templates") or []
    for i, t in enumerate(templates):
        if not isinstance(t, dict):
            findings.append(f"{path}: templates[{i}] not a mapping")
            continue
        for tk in ("path", "name", "addresses"):
            if tk not in t or t[tk] in (None, "", []):
                findings.append(
                    f"{path}: templates[{i}] missing or empty {tk!r}"
                )
        # Every addresses entry must refer to a known clause
        for addr in (t.get("addresses") or []):
            if addr not in clause_ids:
                findings.append(
                    f"{path}: templates[{i}] addresses unknown clause "
                    f"{addr!r} (not in this module's clause set)"
                )

    # Soft check — template name strings with unescaped colons.
    # These are catastrophic when authored unquoted under YAML
    # block-mapping form. The parser caught them above if they
    # broke; this catches the SAFE-but-foot-gun cases where the
    # author got lucky (string was the value of a quoted field).
    # Look at the raw source line by line for `name: <something>:`
    # patterns inside the templates section that AREN'T quoted.
    for lineno, line in enumerate(raw.splitlines(), start=1):
        stripped = line.lstrip()
        if not stripped.startswith("name:"):
            continue
        # Only flag if appears inside a templates context
        # (cheap heuristic: name: lines under templates: block use
        # 4+ space indent; module top-level uses 0 indent)
        leading = len(line) - len(stripped)
        if leading < 4:
            continue
        value = stripped[len("name:"):].strip()
        if not value:
            continue
        # Skip if the value is already quoted
        if value.startswith(('"', "'")) and value[-1] in ('"', "'"):
            continue
        # Check for ": " pattern (colon followed by space) in unquoted value
        # — this is the foot-gun that broke transport-hazmat
        if re.search(r":\s", value):
            findings.append(
                f"{path}:{lineno}: template name contains unquoted "
                f"colon-space pattern (risk of YAML parse failure if "
                f"this file is re-saved with reformatting). Quote the "
                f"value: name: \"...\""
            )

    return findings


def main() -> int:
    if not MODULES_ROOT.is_dir():
        print(f"error: {MODULES_ROOT} not found", file=sys.stderr)
        return 2

    all_findings: list[str] = []
    parse_errors = 0
    modules_scanned = 0
    for module_yaml in sorted(MODULES_ROOT.glob("*/module.yaml")):
        modules_scanned += 1
        findings = _lint_one(module_yaml)
        if findings and "YAML parse error" in findings[0]:
            parse_errors += 1
        all_findings.extend(findings)

    if all_findings:
        for f in all_findings:
            print(f)
        print(
            f"\nlint failed: {len(all_findings)} finding(s) across "
            f"{modules_scanned} module(s); {parse_errors} parse error(s)"
        )
        return 2 if parse_errors else 1

    print(f"lint ok: {modules_scanned} module(s) scanned; 0 findings")
    return 0


if __name__ == "__main__":
    sys.exit(main())
