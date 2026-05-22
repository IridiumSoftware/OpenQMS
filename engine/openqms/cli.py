"""Command-line interface — ``openqms resolve`` and ``openqms validate``."""

from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path

from .module import load_module
from .resolver import resolve
from .types import Bundle
from .validation import validate


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(
        prog="openqms",
        description=(
            "Open QMS engine — resolve a (product, jurisdictions, standards) "
            "bundle into a QMS scaffold with bidirectional clause-to-artifact "
            "traceability, or validate a regulatory module's invariant."
        ),
    )
    sub = parser.add_subparsers(dest="cmd", required=True)

    p_resolve = sub.add_parser(
        "resolve",
        help="Resolve a bundle into a traceability matrix.",
    )
    p_resolve.add_argument("--product", required=True)
    p_resolve.add_argument(
        "--jurisdiction",
        action="append",
        default=[],
        required=True,
        help="Jurisdiction (repeatable).",
    )
    p_resolve.add_argument(
        "--standard",
        action="append",
        default=[],
        required=True,
        help=(
            "Active standard (repeatable). Must match the 'standard:' field "
            "in module clauses."
        ),
    )
    p_resolve.add_argument(
        "--module",
        required=True,
        help=(
            "Module name (looked up under ./modules/<name>/module.yaml) or "
            "path to a module.yaml file."
        ),
    )
    p_resolve.add_argument(
        "--output",
        default="-",
        help="Output path for the traceability-matrix JSON (default: stdout).",
    )

    p_validate = sub.add_parser(
        "validate",
        help=(
            "Validate a module's OQ-001 invariant: every clause addressed; "
            "no orphaned templates."
        ),
    )
    p_validate.add_argument("--module", required=True)

    args = parser.parse_args(argv)

    if args.cmd == "resolve":
        return _cmd_resolve(args)
    if args.cmd == "validate":
        return _cmd_validate(args)
    parser.print_help()
    return 2


def _cmd_resolve(args) -> int:
    module = load_module(args.module)
    bundle = Bundle(
        product=args.product,
        jurisdictions=tuple(args.jurisdiction),
        standards=tuple(args.standard),
    )
    qms = resolve(bundle, module)

    matrix = {
        "bundle": {
            "product": qms.bundle.product,
            "jurisdictions": list(qms.bundle.jurisdictions),
            "standards": list(qms.bundle.standards),
        },
        "module": {"name": module.name, "version": module.version},
        "in_scope_clauses": [
            {
                "id": c.id,
                "standard": c.standard,
                "section": c.section,
                "summary": c.summary,
                "gap_note": c.gap_note,
            }
            for c in qms.in_scope_clauses
        ],
        "artifacts": [
            {"path": t.path, "name": t.name, "addresses": list(t.addresses)}
            for t in qms.artifacts
        ],
        "traceability": {
            "forward": {k: list(v) for k, v in qms.forward.items()},
            "reverse": {k: list(v) for k, v in qms.reverse.items()},
        },
    }
    body = json.dumps(matrix, indent=2)

    if args.output == "-":
        print(body)
    else:
        Path(args.output).write_text(body + "\n")
        print(f"wrote {args.output}", file=sys.stderr)
    return 0


def _cmd_validate(args) -> int:
    module = load_module(args.module)
    report = validate(module)

    print(f"module:           {report.module}")
    print(f"invariant_holds:  {report.invariant_holds}")
    if report.orphaned_clauses:
        print("orphaned_clauses (no template addresses them):")
        for cid in report.orphaned_clauses:
            print(f"  - {cid}")
    if report.orphaned_artifacts:
        print("orphaned_artifacts (template addresses non-existent clause):")
        for path in report.orphaned_artifacts:
            print(f"  - {path}")

    return 0 if report.invariant_holds else 1
