"""Command-line interface — ``openqms resolve`` and ``openqms validate``."""

from __future__ import annotations

import argparse
import json
import subprocess
import sys
from pathlib import Path

from .bundle import load_bundle_def
from .diff import diff_matrices, format_diff
from .module import compose, load_module
from .registry import (
    DEFAULT_REGISTRY_ROOT,
    load_registry,
    validate_module_against_registry,
)
from .resolver import resolve
from .signatures import (
    export_audit_trail,
    extract_signatures_from_repo,
    signature_from_commit_data,
)
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

    p_regen = sub.add_parser(
        "regenerate",
        help=(
            "Re-resolve a stored bundle definition (bundles/<name>.yaml) "
            "and print a structured diff against the prior matrix at "
            "bundles/<name>.matrix.json (OQ-015)."
        ),
    )
    p_regen.add_argument(
        "--bundle",
        required=True,
        help=(
            "Bundle definition name (looked up at bundles/<name>.yaml) "
            "or path to a bundle YAML file."
        ),
    )
    p_regen.add_argument(
        "--write-matrix",
        action="store_true",
        help=(
            "Write the new matrix to bundles/<name>.matrix.json. "
            "Default: dry-run, only print the diff."
        ),
    )

    p_sigs = sub.add_parser(
        "signatures",
        help=(
            "21 CFR Part 11 §11.50 signature-meaning prototype (OQ-060). "
            "Extracts commit-message trailers (`Signature-Meaning:` etc.) "
            "into a Part-11-format audit trail, optionally requiring GPG "
            "verification."
        ),
    )
    p_sigs.add_argument(
        "action",
        choices=("verify", "export"),
        help=(
            "`verify` checks a single commit (via --commit) has the required "
            "trailers and optionally a verified GPG signature. "
            "`export` walks `git log` and emits JSON audit records for every "
            "commit that declares a Signature-Meaning trailer."
        ),
    )
    p_sigs.add_argument(
        "--commit",
        help="Commit SHA (for `verify`). Default HEAD if omitted.",
    )
    p_sigs.add_argument(
        "--since",
        help="Walk commits in <since>..HEAD (for `export`). Default: full history.",
    )
    p_sigs.add_argument(
        "--path",
        action="append",
        default=[],
        help="Restrict to commits touching this path (repeatable, for `export`).",
    )
    p_sigs.add_argument(
        "--require-gpg",
        action="store_true",
        help="Treat un-GPG-verified signatures as an error (default: warn).",
    )
    p_sigs.add_argument(
        "--output",
        default="-",
        help="Output path for the JSON audit trail (for `export`). Default: stdout.",
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

    for sub_parser in (p_resolve, p_validate, p_regen):
        sub_parser.add_argument(
            "--allow-unregistered-standards",
            action="store_true",
            help=(
                "Skip registry validation for --standard arguments and module "
                "standards. Jurisdictions remain validated. Default: strict."
            ),
        )

    for sub_parser in (p_validate, p_regen):
        sub_parser.add_argument(
            "--strict-editions",
            action="store_true",
            help=(
                "Treat any module standard that the registry marks as "
                "superseded_by a newer edition as an error (OQ-065). "
                "Default: warn but pass."
            ),
        )

    args = parser.parse_args(argv)

    if args.cmd == "resolve":
        return _cmd_resolve(args)
    if args.cmd == "validate":
        return _cmd_validate(args)
    if args.cmd == "regenerate":
        return _cmd_regenerate(args)
    if args.cmd == "registry":
        return _cmd_registry(args)
    if args.cmd == "signatures":
        return _cmd_signatures(args)
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

    module = _compose_modules(modules)
    bundle = Bundle(
        product=args.product,
        jurisdictions=tuple(canonical_jurisdictions),
        standards=tuple(canonical_standards),
    )
    qms = resolve(bundle, module)
    body = json.dumps(_matrix_dict(bundle, qms, module), indent=2)

    if args.output == "-":
        print(body)
    else:
        Path(args.output).write_text(body + "\n")
        print(f"wrote {args.output}", file=sys.stderr)
    return 0


def _matrix_dict(bundle: Bundle, qms, module) -> dict:
    """Build the JSON-friendly matrix dict shared between resolve and regenerate."""
    return {
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


def _compose_modules(modules):
    return (
        modules[0]
        if len(modules) == 1
        else compose(
            modules,
            name="+".join(m.name for m in modules),
            version="composed",
        )
    )


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
            if r.superseded_standards:
                for old, new in r.superseded_standards:
                    print(
                        f"warning: module {r.module!r} references "
                        f"{old!r}, superseded by {new!r}",
                        file=sys.stderr,
                    )
                if args.strict_editions:
                    return 2

    module = _compose_modules(modules)
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


def _cmd_regenerate(args) -> int:
    registry = _try_load_registry()

    bundle_path = Path(args.bundle)
    if not bundle_path.is_file():
        candidate = Path("bundles") / f"{args.bundle}.yaml"
        if candidate.exists():
            bundle_path = candidate
        else:
            print(
                f"error: bundle definition not found: tried "
                f"{Path(args.bundle)}, {candidate}",
                file=sys.stderr,
            )
            return 2

    bundle_def = load_bundle_def(bundle_path)

    canonical_stds = _canonicalize_standards(
        list(bundle_def.bundle.standards),
        registry,
        strict=not args.allow_unregistered_standards,
    )
    canonical_jurisdictions = _validate_jurisdictions(
        list(bundle_def.bundle.jurisdictions), registry
    )
    bundle = Bundle(
        product=bundle_def.bundle.product,
        jurisdictions=tuple(canonical_jurisdictions),
        standards=tuple(canonical_stds),
    )

    modules = [load_module(m) for m in bundle_def.modules]
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
            if r.superseded_standards:
                for old, new in r.superseded_standards:
                    print(
                        f"warning: module {r.module!r} references "
                        f"{old!r}, superseded by {new!r}",
                        file=sys.stderr,
                    )
                if args.strict_editions:
                    return 2

    module = _compose_modules(modules)
    qms = resolve(bundle, module)
    new_matrix = _matrix_dict(bundle, qms, module)

    matrix_out_path = bundle_path.parent / f"{bundle_def.name}.matrix.json"

    diff = None
    if matrix_out_path.exists():
        old_matrix = json.loads(matrix_out_path.read_text())
        diff = diff_matrices(
            old_matrix, new_matrix, bundle_def_name=bundle_def.name
        )
        print(format_diff(diff))
    else:
        print(
            f"(no prior matrix at {matrix_out_path}; this is the baseline)"
        )

    if args.write_matrix:
        matrix_out_path.write_text(
            json.dumps(new_matrix, indent=2) + "\n"
        )
        print(f"wrote {matrix_out_path}", file=sys.stderr)
        return 0

    if diff is not None and diff.has_changes:
        print(
            "(dry-run: pass --write-matrix to update the file)",
            file=sys.stderr,
        )
        return 1
    return 0


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


def _cmd_signatures(args) -> int:
    if args.action == "verify":
        return _signatures_verify(args)
    if args.action == "export":
        return _signatures_export(args)
    return 2


def _signatures_verify(args) -> int:
    sha = args.commit or "HEAD"
    try:
        out = subprocess.run(
            [
                "git",
                "log",
                "-n",
                "1",
                "--format=format:%H%x00%an%x00%ae%x00%aI%x00%G?%x00%GK%x00%B",
                sha,
            ],
            capture_output=True,
            text=True,
            check=True,
        ).stdout
    except subprocess.CalledProcessError as e:
        print(f"error: git log failed: {e.stderr}", file=sys.stderr)
        return 2

    fields = out.split("\x00", 6)
    if len(fields) < 7:
        print(
            f"error: could not parse git log output for {sha}",
            file=sys.stderr,
        )
        return 2

    sha_full, name, email, date, gpg_status, gpg_key, message = fields
    sig = signature_from_commit_data(
        sha=sha_full,
        message=message,
        author_name=name,
        author_email=email,
        authored_at=date,
        gpg_status=gpg_status or "N",
        gpg_key_id=gpg_key or None,
    )
    if sig is None:
        print(
            f"error: commit {sha_full} does not declare a "
            "Signature-Meaning trailer.",
            file=sys.stderr,
        )
        return 1
    if args.require_gpg and not sig.gpg_verified:
        print(
            f"error: commit {sha_full} signature meaning "
            f"{sig.meaning!r} is not GPG-verified (--require-gpg).",
            file=sys.stderr,
        )
        return 1

    print(f"commit:           {sig.commit_sha}")
    print(f"signer:           {sig.signer_name} <{sig.signer_email}>")
    print(f"signed_at:        {sig.signed_at}")
    print(f"meaning:          {sig.meaning}")
    print(f"role:             {sig.role or '-'}")
    print(f"justification:    {sig.justification or '-'}")
    print(f"gpg_verified:     {sig.gpg_verified}")
    print(f"gpg_key_id:       {sig.gpg_signer_key_id or '-'}")
    return 0


def _signatures_export(args) -> int:
    try:
        sigs = extract_signatures_from_repo(
            repo_root=Path.cwd(),
            since_ref=args.since,
            paths=args.path or None,
        )
    except subprocess.CalledProcessError as e:
        print(f"error: git log failed: {e.stderr}", file=sys.stderr)
        return 2

    records = export_audit_trail(sigs)

    if args.require_gpg:
        unverified = [r for r in records if not r["verification"]["gpg_signed"]]
        if unverified:
            for r in unverified:
                print(
                    f"error: commit {r['record']['sha']} not GPG-verified "
                    f"(meaning={r['meaning']!r})",
                    file=sys.stderr,
                )
            return 1

    body = json.dumps(records, indent=2)
    if args.output == "-":
        print(body)
    else:
        Path(args.output).write_text(body + "\n")
        print(
            f"wrote {len(records)} signature records to {args.output}",
            file=sys.stderr,
        )
    return 0


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
