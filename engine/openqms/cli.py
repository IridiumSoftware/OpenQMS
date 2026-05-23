"""Command-line interface — ``openqms resolve`` and ``openqms validate``."""

from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path

from .module import compose, load_module
from .registry import (
    DEFAULT_REGISTRY_ROOT,
    load_registry,
    validate_module_against_registry,
)
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
        action="append",
        default=[],
        required=True,
        help=(
            "Module name (looked up under ./modules/<name>/module.yaml) or "
            "path to a module.yaml file. Repeatable: multiple --module "
            "arguments are composed into a single module before resolution."
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
    p_validate.add_argument(
        "--module",
        action="append",
        default=[],
        required=True,
        help=(
            "Module name or path. Repeatable: multiple --module arguments "
            "are composed before validation, exercising the OQ-001 invariant "
            "on the composite."
        ),
    )

    p_registry = sub.add_parser(
        "registry",
        help="Inspect the standards-and-jurisdictions registry (OQ-014).",
    )
    p_registry.add_argument(
        "action",
        choices=("list", "show"),
        help=(
            "`list` prints all registered standards and jurisdictions. "
            "`show` requires --id to print details for a single entry."
        ),
    )
    p_registry.add_argument(
        "--id",
        help="Standard id (or alias) or jurisdiction id, required for `show`.",
    )

    for sub_parser in (p_resolve, p_validate):
        sub_parser.add_argument(
            "--allow-unregistered-standards",
            action="store_true",
            help=(
                "Skip registry validation for --standard arguments and module "
                "standards. Jurisdictions remain validated. Default: strict."
            ),
        )

    args = parser.parse_args(argv)

    if args.cmd == "resolve":
        return _cmd_resolve(args)
    if args.cmd == "validate":
        return _cmd_validate(args)
    if args.cmd == "registry":
        return _cmd_registry(args)
    parser.print_help()
    return 2


def _try_load_registry():
    """Load the registry from cwd. Returns None if registry/ doesn't exist."""
    try:
        return load_registry()
    except FileNotFoundError:
        return None


def _cmd_resolve(args) -> int:
    registry = _try_load_registry()
    if registry is None and not args.allow_unregistered_standards:
        print(
            f"error: registry not found at {DEFAULT_REGISTRY_ROOT}/. "
            "Pass --allow-unregistered-standards to skip registry validation.",
            file=sys.stderr,
        )
        return 2

    canonical_standards = _canonicalize_standards(
        args.standard,
        registry,
        strict=not args.allow_unregistered_standards,
    )
    canonical_jurisdictions = _validate_jurisdictions(
        args.jurisdiction, registry
    )

    modules = [load_module(m) for m in args.module]
    if registry is not None and not args.allow_unregistered_standards:
        for m in modules:
            r = validate_module_against_registry(m, registry)
            if not r.invariant_holds:
                print(
                    f"error: module {r.module!r} references unregistered "
                    f"standards. module.standards: "
                    f"{list(r.unregistered_module_standards)}; "
                    f"clause.standard: "
                    f"{list(r.unregistered_clause_standards)}",
                    file=sys.stderr,
                )
                return 2

    module = (
        modules[0]
        if len(modules) == 1
        else compose(
            modules,
            name="+".join(m.name for m in modules),
            version="composed",
        )
    )
    bundle = Bundle(
        product=args.product,
        jurisdictions=tuple(canonical_jurisdictions),
        standards=tuple(canonical_standards),
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
    registry = _try_load_registry()
    modules = [load_module(m) for m in args.module]

    if registry is not None and not args.allow_unregistered_standards:
        for m in modules:
            r = validate_module_against_registry(m, registry)
            if not r.invariant_holds:
                print(
                    f"error: module {r.module!r} references unregistered "
                    f"standards. module.standards: "
                    f"{list(r.unregistered_module_standards)}; "
                    f"clause.standard: "
                    f"{list(r.unregistered_clause_standards)}",
                    file=sys.stderr,
                )
                return 2

    module = (
        modules[0]
        if len(modules) == 1
        else compose(
            modules,
            name="+".join(m.name for m in modules),
            version="composed",
        )
    )
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


def _canonicalize_standards(
    raw: list[str], registry, *, strict: bool
) -> list[str]:
    """Normalize a list of --standard args to canonical registry ids.

    If `strict` is True and an arg doesn't resolve, raises SystemExit(2)
    with a helpful error. If `strict` is False, unresolved args are
    passed through unchanged.
    """
    if registry is None:
        return list(raw)
    canonical: list[str] = []
    for s in raw:
        if registry.has_standard(s):
            canonical.append(registry.canonical_standard(s))
        elif strict:
            print(
                f"error: standard {s!r} is not in the registry. "
                f"Registered ids: "
                f"{sorted(e.id for e in registry.standards)}",
                file=sys.stderr,
            )
            raise SystemExit(2)
        else:
            canonical.append(s)
    return canonical


def _validate_jurisdictions(raw: list[str], registry) -> list[str]:
    """Validate jurisdictions against the registry (strict).

    Jurisdictions are always strictly validated when a registry is
    loaded — there's no equivalent to --allow-unregistered-standards
    for jurisdictions.
    """
    if registry is None:
        return list(raw)
    out: list[str] = []
    for j in raw:
        if registry.has_jurisdiction(j):
            out.append(j)
        else:
            print(
                f"error: jurisdiction {j!r} is not in the registry. "
                f"Registered ids: "
                f"{sorted(e.id for e in registry.jurisdictions)}",
                file=sys.stderr,
            )
            raise SystemExit(2)
    return out


def _cmd_registry(args) -> int:
    registry = _try_load_registry()
    if registry is None:
        print(
            f"error: registry not found at {DEFAULT_REGISTRY_ROOT}/.",
            file=sys.stderr,
        )
        return 2

    if args.action == "list":
        print("Standards:")
        for s in registry.standards:
            aliases = (
                f"  (aliases: {', '.join(s.aliases)})" if s.aliases else ""
            )
            print(
                f"  {s.id:<30}  [{s.license_kind:<10}]  "
                f"{s.kind:<10}  {s.name}{aliases}"
            )
        print()
        print("Jurisdictions:")
        for j in registry.jurisdictions:
            print(
                f"  {j.id:<15}  {j.region:<20}  "
                f"applicable_standards={list(j.applicable_standards)}"
            )
            print(f"    {j.name}")
        return 0

    if args.action == "show":
        if not args.id:
            print("error: --id is required for `registry show`", file=sys.stderr)
            return 2
        try:
            s = registry.resolve_standard(args.id)
            print(f"Standard: {s.id}")
            print(f"  name:         {s.name}")
            print(f"  publisher:    {s.publisher}")
            print(f"  edition:      {s.edition}")
            print(f"  kind:         {s.kind}")
            print(f"  license_kind: {s.license_kind}")
            if s.aliases:
                print(f"  aliases:      {', '.join(s.aliases)}")
            return 0
        except KeyError:
            pass
        try:
            j = registry.resolve_jurisdiction(args.id)
            print(f"Jurisdiction: {j.id}")
            print(f"  name:                 {j.name}")
            print(f"  region:               {j.region}")
            print(f"  applicable_standards: {list(j.applicable_standards)}")
            return 0
        except KeyError:
            pass
        print(
            f"error: {args.id!r} not found in standards or jurisdictions "
            "registry.",
            file=sys.stderr,
        )
        return 2

    return 2
