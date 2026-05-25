#!/usr/bin/env python3
"""CI-invokable doc-control check — P5 deliverable v0.60.0.

Reads a newline-delimited list of changed file paths from stdin (or
positional arg), runs the doc-control checks for each, prints a
GitHub Actions–compatible diagnostic summary, writes an audit-artifact
JSON to the path given by --output (default: ./doc-control-audit.json),
and exits 1 if any file has an error.

Usage (invoked from .github/workflows/doc-control.yml):

  echo "qms-policy/quality-manual.md" | \\
    python3 scripts/doc-control-check.py \\
      --base-ref origin/main \\
      --commit-sha $GITHUB_SHA \\
      --pr-number ${{ github.event.pull_request.number }} \\
      --output doc-control-audit.json

The script:
  1. Reads list of changed files
  2. Skips files outside controlled-doc paths (templates/, modules/,
     engine/, .github/, docs/, scripts/, BUSINESS/, README.md,
     bundles/, registry/, *.json, etc.)
  3. For each remaining file, computes base+head text via git show
     (gracefully handling new files where base doesn't exist)
  4. Runs check_file() from doc_control module
  5. Parses signature-meaning trailers from PR commits via
     openqms.signatures
  6. Emits ::error and ::warning annotations
  7. Writes audit JSON
  8. Exits non-zero if any errors
"""

from __future__ import annotations

import argparse
import json
import subprocess
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent / "engine"))

from openqms.doc_control import (
    build_audit_artifact,
    check_file,
    format_audit_markdown,
)


# Paths outside these prefixes are NOT controlled-document scope and are
# skipped by this check (handled by other CI workflows or pure-engine
# code). This mirrors the legacy doc-control.yml skip set.
SKIP_PREFIXES: tuple[str, ...] = (
    ".github/",
    "docs/",
    "scripts/",
    "modules/",
    "templates/",
    "engine/",
    "BUSINESS/",
    "bundles/",
    "registry/",
)


def _should_check(path_str: str) -> bool:
    """Should this changed-file path go through doc-control?"""
    if not path_str.endswith(".md"):
        return False
    for prefix in SKIP_PREFIXES:
        if path_str.startswith(prefix):
            return False
    return True


def _git_show(ref: str, path: str) -> str | None:
    """Return file content at ref:path, or None if not present."""
    try:
        result = subprocess.run(
            ["git", "show", f"{ref}:{path}"],
            capture_output=True,
            check=True,
            text=True,
        )
        return result.stdout
    except subprocess.CalledProcessError:
        return None


def _parse_signature_trailers(base_ref: str, head_ref: str) -> list[dict]:
    """Walk PR commits + extract Signature-Meaning trailers."""
    try:
        result = subprocess.run(
            ["git", "log", f"{base_ref}..{head_ref}", "--pretty=format:%H%n%B%n--END--"],
            capture_output=True,
            check=True,
            text=True,
        )
    except subprocess.CalledProcessError:
        return []

    trailers: list[dict] = []
    for block in result.stdout.split("--END--"):
        block = block.strip()
        if not block:
            continue
        lines = block.splitlines()
        if not lines:
            continue
        sha = lines[0].strip()
        meaning = role = justification = None
        for line in lines[1:]:
            stripped = line.strip()
            if stripped.lower().startswith("signature-meaning:"):
                meaning = stripped.split(":", 1)[1].strip()
            elif stripped.lower().startswith("signature-role:"):
                role = stripped.split(":", 1)[1].strip()
            elif stripped.lower().startswith("signature-justification:"):
                justification = stripped.split(":", 1)[1].strip()
        if meaning:
            trailers.append({
                "sha": sha,
                "meaning": meaning,
                "role": role,
                "justification": justification,
            })
    return trailers


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--base-ref", default="origin/main")
    parser.add_argument("--head-ref", default="HEAD")
    parser.add_argument("--commit-sha", default="HEAD")
    parser.add_argument("--pr-number", type=int, default=None)
    parser.add_argument(
        "--changed-files",
        help="Path to file containing newline-delimited list of changed files "
        "(if omitted, stdin is read).",
    )
    parser.add_argument("--output", default="doc-control-audit.json")
    parser.add_argument("--markdown-output", default="doc-control-audit.md")
    parser.add_argument("--ci-status", default="pending")
    args = parser.parse_args()

    if args.changed_files:
        changed_files = Path(args.changed_files).read_text().splitlines()
    else:
        changed_files = sys.stdin.read().splitlines()
    changed_files = [f.strip() for f in changed_files if f.strip()]

    file_checks = []
    has_errors = False
    for path_str in changed_files:
        if not _should_check(path_str):
            continue
        path = Path(path_str)
        base_text = _git_show(args.base_ref, path_str)
        head_text = _git_show(args.head_ref, path_str)
        if head_text is None:
            # File deleted in this PR — skip (deletion-control is a separate concern)
            continue
        check = check_file(path, base_text, head_text)
        file_checks.append(check)
        if not check.passed:
            has_errors = True
        for err in check.errors:
            print(f"::error file={path_str}::{err}")
        for warn in check.warnings:
            print(f"::warning file={path_str}::{warn}")

    signature_trailers = _parse_signature_trailers(args.base_ref, args.head_ref)

    artifact = build_audit_artifact(
        pr_number=args.pr_number,
        commit_sha=args.commit_sha,
        base_ref=args.base_ref,
        head_ref=args.head_ref,
        file_checks=file_checks,
        signature_trailers=signature_trailers,
        ci_status="fail" if has_errors else args.ci_status,
    )

    Path(args.output).write_text(json.dumps(artifact.to_dict(), indent=2))
    Path(args.markdown_output).write_text(format_audit_markdown(artifact))

    if file_checks:
        print(
            f"\ndoc-control: {len(file_checks)} file(s) checked; "
            f"{sum(1 for fc in file_checks if fc.passed)} passed, "
            f"{sum(1 for fc in file_checks if not fc.passed)} failed"
        )
    else:
        print("doc-control: no controlled-document files in changeset; pass-through")

    return 1 if has_errors else 0


if __name__ == "__main__":
    sys.exit(main())
