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
from .trace_instances import (
    DEFAULT_POLICY,
    build_report as build_instance_report,
    discover_records,
    fetch_issues_via_gh,
    lint_records,
    load_issues_json,
    nodes_from_issues,
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

    p_trace = sub.add_parser(
        "trace",
        help=(
            "Emit a repository-wide bidirectional clause-to-artifact "
            "traceability matrix across all (or selected) modules (OQ-067)."
        ),
    )
    p_trace.add_argument(
        "--module",
        action="append",
        default=[],
        help=(
            "Module name (looked up under ./modules/<name>/module.yaml) or "
            "path to a module.yaml. Repeatable. If omitted (or --all), every "
            "module under ./modules/ is included."
        ),
    )
    p_trace.add_argument(
        "--all",
        action="store_true",
        help=(
            "Include every module under ./modules/ (default when --module "
            "is not specified)."
        ),
    )
    p_trace.add_argument(
        "--format",
        choices=("json", "md"),
        default="json",
        help="Output format: json (default) or md (markdown table).",
    )
    p_trace.add_argument(
        "--output",
        default="-",
        help="Output path. Default: stdout.",
    )

    p_trace_instances = sub.add_parser(
        "trace-instances",
        help=(
            "Walk record-producing markdown files, build the instance-level "
            "cross-record trace graph, and check instance invariants against a "
            "trace-policy (P15.1a — the instance-level analog of `trace`)."
        ),
    )
    p_trace_instances.add_argument(
        "--path",
        default="examples/trace-instances",
        help="Directory of record markdown files to walk. Default: examples/trace-instances.",
    )
    p_trace_instances.add_argument(
        "--policy",
        default=None,
        help="Path to a trace-policy.yaml. Default: the built-in policy.",
    )
    p_trace_instances.add_argument(
        "--issues-json",
        default=None,
        help=(
            "Path to a `gh issue list --json number,labels,body` export. "
            "Issue-sourced records (CAPA/complaint/NCR by label) fold into "
            "the same graph as the markdown records (P15.2)."
        ),
    )
    p_trace_instances.add_argument(
        "--github",
        default=None,
        metavar="OWNER/REPO",
        help="Fetch issues live via the `gh` CLI for OWNER/REPO and fold them in.",
    )
    p_trace_instances.add_argument(
        "--format",
        choices=("json", "md"),
        default="json",
        help="Output format: json (default) or md.",
    )
    p_trace_instances.add_argument(
        "--output",
        default="-",
        help="Output path. Default: stdout.",
    )

    p_coverage = sub.add_parser(
        "coverage",
        help=(
            "Report per-module + aggregate coverage metrics: percent of "
            "clauses bound to >=1 template, percent of declared standards "
            "with >=1 clause, average template-per-clause depth, orphan "
            "counts (OQ-115)."
        ),
    )
    p_coverage.add_argument(
        "--module",
        action="append",
        default=[],
        help=(
            "Module name or path to module.yaml. Repeatable. If omitted, "
            "every module under ./modules/ is included."
        ),
    )
    p_coverage.add_argument(
        "--all",
        action="store_true",
        help="Include every module under ./modules/.",
    )
    p_coverage.add_argument(
        "--format",
        choices=("json", "md"),
        default="json",
        help="Output format: json (default) or md.",
    )
    p_coverage.add_argument(
        "--output",
        default="-",
        help="Output path. Default: stdout.",
    )
    p_coverage.add_argument(
        "--threshold",
        type=int,
        default=0,
        help=(
            "Exit code 1 if any in-scope module's clause-coverage percentage "
            "falls below this integer. Default 0 (never fail). Use in CI to "
            "gate against coverage regression."
        ),
    )

    p_crosswalk = sub.add_parser(
        "crosswalk",
        help=(
            "Emit a clause-crosswalk between modules — identifies clauses "
            "that reference the same standard + section across modules "
            "(common across compose-partner modules and per-jurisdiction "
            "implementations) (OQ-116)."
        ),
    )
    p_crosswalk.add_argument(
        "--module",
        action="append",
        default=[],
        required=True,
        help=(
            "Module name or path. Repeatable. At least 2 modules required "
            "for a meaningful crosswalk."
        ),
    )
    p_crosswalk.add_argument(
        "--format",
        choices=("json", "md"),
        default="json",
        help="Output format: json (default) or md.",
    )
    p_crosswalk.add_argument(
        "--output",
        default="-",
        help="Output path. Default: stdout.",
    )

    p_jurisdictions = sub.add_parser(
        "jurisdictions-query",
        help=(
            "Query the registry for standards applicable to a given "
            "jurisdiction (publisher-based inference) — supports adopter "
            "planning of per-jurisdiction module scope (OQ-117)."
        ),
    )
    p_jurisdictions.add_argument(
        "--jurisdiction",
        required=True,
        help=(
            "Jurisdiction id or alias (e.g., FDA, EU MDR, NHTSA, EMA). "
            "Returns standards whose registry publisher matches the "
            "jurisdiction's known publishers."
        ),
    )
    p_jurisdictions.add_argument(
        "--format",
        choices=("json", "md", "text"),
        default="text",
        help="Output format: text (default), json, or md.",
    )

    p_verify_dep = sub.add_parser(
        "verify-deployment",
        help=(
            "Verify adopter-fork deployment configuration against a "
            "declared deployment-policy.yaml (OQ-126; closes "
            "compliance-architecture forward-work P11). Queries GitHub "
            "API via `gh` CLI subprocess; compares actual branch-"
            "protection + CODEOWNERS + signed-commits + required-status-"
            "checks vs declared policy."
        ),
    )
    p_verify_dep.add_argument(
        "--policy",
        required=True,
        help="Path to deployment-policy.yaml.",
    )
    p_verify_dep.add_argument(
        "--codeowners",
        help=(
            "Path to CODEOWNERS file. Default: auto-detect at "
            ".github/CODEOWNERS, CODEOWNERS, or docs/CODEOWNERS."
        ),
    )
    p_verify_dep.add_argument(
        "--format",
        choices=("text", "json"),
        default="text",
        help="Output format. Default: text.",
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
    if args.cmd == "trace":
        return _cmd_trace(args)
    if args.cmd == "trace-instances":
        return _cmd_trace_instances(args)
    if args.cmd == "coverage":
        return _cmd_coverage(args)
    if args.cmd == "crosswalk":
        return _cmd_crosswalk(args)
    if args.cmd == "jurisdictions-query":
        return _cmd_jurisdictions_query(args)
    if args.cmd == "verify-deployment":
        return _cmd_verify_deployment(args)
    parser.print_help()
    return 2


def _cmd_verify_deployment(args) -> int:
    """`openqms verify-deployment` — OQ-126 (P11)."""
    import json as _json
    from pathlib import Path as _Path

    from .verify_deployment import (
        format_result_text,
        load_policy,
        verify_deployment,
    )

    try:
        policy = load_policy(_Path(args.policy))
    except (FileNotFoundError, ValueError) as exc:
        print(f"error: {exc}", file=sys.stderr)
        return 2

    codeowners_path = _Path(args.codeowners) if args.codeowners else None

    try:
        result = verify_deployment(policy, codeowners_path=codeowners_path)
    except RuntimeError as exc:
        print(f"error: {exc}", file=sys.stderr)
        return 2

    if args.format == "json":
        body = _json.dumps({
            "passed": result.passed,
            "findings": [
                {"severity": f.severity, "category": f.category, "message": f.message}
                for f in result.findings
            ],
        }, indent=2)
        print(body)
    else:
        print(format_result_text(result))

    return 0 if result.passed else 1


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


def _cmd_trace(args) -> int:
    """Emit a repository-wide bidirectional traceability matrix (OQ-067).

    For each module in scope, walk its clauses + templates and produce
    forward map (clause -> templates that address it) + reverse map
    (template -> clauses it addresses). Reports orphaned clauses
    (no template addresses them) + orphaned templates (address no
    in-module clause).
    """
    modules_root = Path("./modules")
    if args.module:
        module_names = list(args.module)
    else:
        if not modules_root.is_dir():
            print(
                "error: no --module specified and ./modules/ not found",
                file=sys.stderr,
            )
            return 2
        module_names = sorted(
            p.name
            for p in modules_root.iterdir()
            if (p / "module.yaml").is_file() and p.name != "general"
        )

    matrices: dict[str, dict] = {}
    summary = {
        "modules_in_scope": 0,
        "total_clauses": 0,
        "total_templates": 0,
        "total_clause_addresses": 0,
        "orphaned_clauses_total": 0,
        "orphaned_templates_total": 0,
    }

    for name in module_names:
        try:
            mod = load_module(name)
        except (FileNotFoundError, ValueError) as exc:
            print(f"error: failed to load module {name!r}: {exc}", file=sys.stderr)
            return 2

        clause_ids = [c.id for c in mod.clauses]
        forward: dict[str, list[str]] = {cid: [] for cid in clause_ids}
        reverse: dict[str, list[str]] = {}

        for tpl in mod.templates:
            reverse[tpl.path] = list(tpl.addresses)
            for caddr in tpl.addresses:
                if caddr in forward:
                    forward[caddr].append(tpl.path)

        orphaned_clauses = [cid for cid, tlist in forward.items() if not tlist]
        orphaned_templates = [
            tpath
            for tpath, claddrs in reverse.items()
            if not any(addr in forward for addr in claddrs)
        ]

        matrices[name] = {
            "module": name,
            "version": mod.version,
            "standards": list(mod.standards),
            "clause_count": len(clause_ids),
            "template_count": len(mod.templates),
            "forward": forward,
            "reverse": reverse,
            "orphaned_clauses": orphaned_clauses,
            "orphaned_templates": orphaned_templates,
        }

        summary["modules_in_scope"] += 1
        summary["total_clauses"] += len(clause_ids)
        summary["total_templates"] += len(mod.templates)
        summary["total_clause_addresses"] += sum(len(v) for v in forward.values())
        summary["orphaned_clauses_total"] += len(orphaned_clauses)
        summary["orphaned_templates_total"] += len(orphaned_templates)

    output = {"summary": summary, "modules": matrices}

    if args.format == "json":
        rendered = json.dumps(output, indent=2, sort_keys=True)
    else:
        rendered = _format_trace_markdown(output)

    if args.output == "-":
        print(rendered)
    else:
        Path(args.output).write_text(rendered + "\n", encoding="utf-8")
        print(
            f"wrote trace matrix for {summary['modules_in_scope']} module(s) "
            f"to {args.output}"
        )
    return 0


def _format_trace_markdown(output: dict) -> str:
    s = output["summary"]
    lines: list[str] = []
    lines.append("# Open QMS — repository-wide traceability matrix")
    lines.append("")
    lines.append(
        f"**Modules:** {s['modules_in_scope']} · "
        f"**Clauses:** {s['total_clauses']} · "
        f"**Templates:** {s['total_templates']} · "
        f"**Clause→template addresses:** {s['total_clause_addresses']} · "
        f"**Orphaned clauses:** {s['orphaned_clauses_total']} · "
        f"**Orphaned templates:** {s['orphaned_templates_total']}"
    )
    lines.append("")
    for name in sorted(output["modules"].keys()):
        m = output["modules"][name]
        lines.append(f"## {name} (v{m['version']})")
        lines.append("")
        lines.append(
            f"Standards: {', '.join(m['standards'])}. "
            f"Clauses: {m['clause_count']}. Templates: {m['template_count']}."
        )
        lines.append("")
        if m["orphaned_clauses"]:
            lines.append("**Orphaned clauses (addressed by no template):**")
            lines.append("")
            for cid in m["orphaned_clauses"]:
                lines.append(f"- `{cid}`")
            lines.append("")
        if m["orphaned_templates"]:
            lines.append("**Orphaned templates (address no in-module clause):**")
            lines.append("")
            for tpath in m["orphaned_templates"]:
                lines.append(f"- `{tpath}`")
            lines.append("")
        lines.append("| Clause | Templates addressing |")
        lines.append("|---|---|")
        for cid in sorted(m["forward"].keys()):
            tlist = m["forward"][cid]
            tcell = ", ".join(f"`{t}`" for t in tlist) if tlist else "_(orphan)_"
            lines.append(f"| `{cid}` | {tcell} |")
        lines.append("")
    return "\n".join(lines)


def _cmd_trace_instances(args) -> int:
    """`openqms trace-instances` — instance-level cross-record trace (P15.1a).

    Walks record markdown under --path, runs the static lint surface +
    runtime invariants against the policy, emits json/md, and exits 1 if
    any error-severity finding is present (the CI gate).
    """
    import yaml as _yaml

    root = Path(args.path)
    policy = DEFAULT_POLICY
    if args.policy:
        try:
            policy = _yaml.safe_load(Path(args.policy).read_text(encoding="utf-8")) or {}
        except (OSError, _yaml.YAMLError) as exc:
            print(f"error: failed to read policy {args.policy!r}: {exc}", file=sys.stderr)
            return 2

    nodes = []
    if root.is_dir():
        nodes.extend(discover_records(root))
    elif not (args.issues_json or args.github):
        print(
            f"error: records path not found: {root} (and no --issues-json/--github)",
            file=sys.stderr,
        )
        return 2
    if args.issues_json:
        nodes.extend(nodes_from_issues(load_issues_json(Path(args.issues_json))))
    if args.github:
        try:
            nodes.extend(nodes_from_issues(fetch_issues_via_gh(args.github)))
        except (subprocess.CalledProcessError, FileNotFoundError, json.JSONDecodeError) as exc:
            print(f"error: gh issue fetch failed for {args.github!r}: {exc}", file=sys.stderr)
            return 2

    lint = lint_records(nodes, require_scope=bool(policy.get("require_scope", True)))
    report = build_instance_report(nodes, policy)
    # Fold the static lint findings in front of the runtime findings.
    report["findings"] = (
        [{"severity": f.severity, "message": f.message} for f in lint]
        + report["findings"]
    )
    report["summary"]["errors"] = sum(1 for f in report["findings"] if f["severity"] == "error")
    report["summary"]["warnings"] = sum(1 for f in report["findings"] if f["severity"] == "warning")

    rendered = (
        _format_trace_instances_markdown(report)
        if args.format == "md"
        else json.dumps(report, indent=2)
    )
    if args.output == "-":
        print(rendered)
    else:
        Path(args.output).write_text(rendered + "\n", encoding="utf-8")
        print(
            f"wrote instance-trace report ({report['summary']['records']} records) "
            f"to {args.output}"
        )
    return 1 if report["summary"]["errors"] else 0


def _format_trace_instances_markdown(report: dict) -> str:
    s = report["summary"]
    lines = [
        "# Open QMS — instance-level trace report",
        "",
        f"**Records:** {s['records']} · **Edges:** {s['edges']} · "
        f"**Kinds:** {', '.join(s['kinds'])} · **Errors:** {s['errors']} · "
        f"**Warnings:** {s['warnings']}",
        "",
    ]
    if report["findings"]:
        lines += ["## Findings", ""]
        for f in report["findings"]:
            lines.append(f"- **{f['severity']}** — {f['message']}")
        lines.append("")
    lines += ["## Records", "", "| Record | Kind | Outbound edges |", "|---|---|---|"]
    for rid in sorted(report["nodes"].keys()):
        edges = ", ".join(f"`{e}`" for e in report["edges"].get(rid, [])) or "—"
        lines.append(f"| `{rid}` | {report['nodes'][rid]['kind']} | {edges} |")
    lines.append("")
    return "\n".join(lines)


# ============================================================================
# OQ-115: openqms coverage — per-module + aggregate coverage metrics
# ============================================================================


def _cmd_coverage(args) -> int:
    """Emit per-module + aggregate coverage metrics.

    Per module: % clauses bound to ≥1 template (clause coverage), % declared
    standards with ≥1 clause (standard coverage), average templates per clause,
    orphaned clause + template counts. Aggregate: same metrics over the set.

    --threshold N: exit 1 if any in-scope module's clause-coverage % < N.
    """
    modules_root = Path("./modules")
    if args.module:
        module_names = list(args.module)
    else:
        if not modules_root.is_dir():
            print("error: ./modules/ not found", file=sys.stderr)
            return 2
        module_names = sorted(
            p.name
            for p in modules_root.iterdir()
            if (p / "module.yaml").is_file() and p.name != "general"
        )

    per_module: list[dict] = []
    threshold_failures: list[str] = []
    for name in module_names:
        try:
            mod = load_module(name)
        except (FileNotFoundError, ValueError) as exc:
            print(f"error: failed to load {name!r}: {exc}", file=sys.stderr)
            return 2

        clause_ids = [c.id for c in mod.clauses]
        clause_standards = {c.standard for c in mod.clauses}
        declared_standards = set(mod.standards)

        # Clause -> #templates addressing it
        clause_template_count: dict[str, int] = {cid: 0 for cid in clause_ids}
        # Template -> #clauses addressed (within this module)
        template_clause_count: dict[str, int] = {}
        orphan_templates: list[str] = []

        for tpl in mod.templates:
            in_scope_addresses = [a for a in tpl.addresses if a in clause_template_count]
            template_clause_count[tpl.path] = len(in_scope_addresses)
            if not in_scope_addresses:
                orphan_templates.append(tpl.path)
            for cid in in_scope_addresses:
                clause_template_count[cid] += 1

        clauses_bound = sum(1 for cnt in clause_template_count.values() if cnt > 0)
        orphan_clauses = [cid for cid, cnt in clause_template_count.items() if cnt == 0]
        standards_with_clauses = declared_standards & clause_standards
        standards_unused = declared_standards - clause_standards

        total_clauses = len(clause_ids)
        clause_coverage_pct = (
            (clauses_bound / total_clauses * 100) if total_clauses else 100.0
        )
        standard_coverage_pct = (
            (len(standards_with_clauses) / len(declared_standards) * 100)
            if declared_standards
            else 100.0
        )
        avg_templates_per_clause = (
            sum(clause_template_count.values()) / total_clauses
            if total_clauses
            else 0.0
        )

        per_module.append({
            "module": name,
            "version": mod.version,
            "total_clauses": total_clauses,
            "total_templates": len(mod.templates),
            "total_standards_declared": len(declared_standards),
            "clauses_bound": clauses_bound,
            "clause_coverage_pct": round(clause_coverage_pct, 2),
            "standards_with_clauses": sorted(standards_with_clauses),
            "standards_unused": sorted(standards_unused),
            "standard_coverage_pct": round(standard_coverage_pct, 2),
            "avg_templates_per_clause": round(avg_templates_per_clause, 2),
            "orphan_clauses": sorted(orphan_clauses),
            "orphan_templates": sorted(orphan_templates),
        })

        if args.threshold > 0 and clause_coverage_pct < args.threshold:
            threshold_failures.append(
                f"{name}: clause coverage {clause_coverage_pct:.1f}% < threshold {args.threshold}%"
            )

    # Aggregate
    total_clauses_all = sum(m["total_clauses"] for m in per_module)
    total_templates_all = sum(m["total_templates"] for m in per_module)
    total_bound_all = sum(m["clauses_bound"] for m in per_module)
    total_orphans_all = sum(len(m["orphan_clauses"]) for m in per_module)
    total_orphan_templates = sum(len(m["orphan_templates"]) for m in per_module)
    avg_coverage_pct = (
        sum(m["clause_coverage_pct"] for m in per_module) / len(per_module)
        if per_module
        else 0.0
    )

    output = {
        "summary": {
            "modules_in_scope": len(per_module),
            "total_clauses": total_clauses_all,
            "total_templates": total_templates_all,
            "total_clauses_bound": total_bound_all,
            "aggregate_clause_coverage_pct": round(
                (total_bound_all / total_clauses_all * 100) if total_clauses_all else 100.0,
                2,
            ),
            "average_per_module_coverage_pct": round(avg_coverage_pct, 2),
            "orphan_clauses_total": total_orphans_all,
            "orphan_templates_total": total_orphan_templates,
            "threshold_pct": args.threshold,
            "threshold_failures": len(threshold_failures),
        },
        "modules": per_module,
    }

    if args.format == "json":
        rendered = json.dumps(output, indent=2, sort_keys=True)
    else:
        rendered = _format_coverage_markdown(output)

    if args.output == "-":
        print(rendered)
    else:
        Path(args.output).write_text(rendered + "\n", encoding="utf-8")
        print(
            f"wrote coverage report for {len(per_module)} module(s) to {args.output}"
        )

    if threshold_failures:
        for f in threshold_failures:
            print(f"threshold-fail: {f}", file=sys.stderr)
        return 1
    return 0


def _format_coverage_markdown(output: dict) -> str:
    s = output["summary"]
    lines: list[str] = []
    lines.append("# Open QMS — coverage report")
    lines.append("")
    lines.append(
        f"**Modules:** {s['modules_in_scope']} · "
        f"**Clauses:** {s['total_clauses']} · "
        f"**Templates:** {s['total_templates']} · "
        f"**Clauses bound:** {s['total_clauses_bound']} · "
        f"**Aggregate coverage:** {s['aggregate_clause_coverage_pct']}% · "
        f"**Average per-module coverage:** {s['average_per_module_coverage_pct']}% · "
        f"**Orphan clauses:** {s['orphan_clauses_total']} · "
        f"**Orphan templates:** {s['orphan_templates_total']}"
    )
    if s["threshold_pct"]:
        lines.append(
            f"\n**Threshold:** {s['threshold_pct']}% — "
            f"{s['threshold_failures']} failure(s)"
        )
    lines.append("")
    lines.append("| Module | Clauses | Bound | Coverage | Templates | Standards | Avg tpls/clause | Orphan clauses | Orphan tpls |")
    lines.append("|---|---|---|---|---|---|---|---|---|")
    for m in output["modules"]:
        lines.append(
            f"| `{m['module']}` v{m['version']} | {m['total_clauses']} | "
            f"{m['clauses_bound']} | **{m['clause_coverage_pct']}%** | "
            f"{m['total_templates']} | "
            f"{len(m['standards_with_clauses'])}/{m['total_standards_declared']} "
            f"({m['standard_coverage_pct']}%) | "
            f"{m['avg_templates_per_clause']} | "
            f"{len(m['orphan_clauses'])} | {len(m['orphan_templates'])} |"
        )
    return "\n".join(lines)


# ============================================================================
# OQ-116: openqms crosswalk — clause-crosswalk between modules
# ============================================================================


def _cmd_crosswalk(args) -> int:
    """Emit a clause crosswalk between modules.

    Identifies clauses referencing the same standard + section across the
    modules in scope. Output groups matching clauses by (standard, section)
    key with cross-module clause-ID + summary preview.
    """
    if len(args.module) < 2:
        print("error: crosswalk requires at least 2 --module arguments", file=sys.stderr)
        return 2

    modules: list = []
    for name in args.module:
        try:
            modules.append(load_module(name))
        except (FileNotFoundError, ValueError) as exc:
            print(f"error: failed to load {name!r}: {exc}", file=sys.stderr)
            return 2

    # Build (standard, section) -> [(module_name, clause_id, summary_preview)] index
    index: dict[tuple[str, str], list[dict]] = {}
    for mod in modules:
        for c in mod.clauses:
            key = (c.standard, c.section)
            index.setdefault(key, []).append({
                "module": mod.name,
                "clause_id": c.id,
                "summary_preview": (c.summary or "").strip().splitlines()[0][:160]
                if c.summary else "",
            })

    # Only emit crosswalks where ≥2 modules reference the same (standard, section)
    crosswalks = [
        {
            "standard": std,
            "section": sec,
            "entries": entries,
            "module_count": len(set(e["module"] for e in entries)),
        }
        for (std, sec), entries in index.items()
        if len(set(e["module"] for e in entries)) >= 2
    ]
    crosswalks.sort(key=lambda x: (x["standard"], x["section"]))

    # Per-module own-only clauses (not in any crosswalk)
    crosswalked_keys = {(c["standard"], c["section"]) for c in crosswalks}
    own_only: dict[str, int] = {}
    shared: dict[str, int] = {}
    for mod in modules:
        own_only[mod.name] = 0
        shared[mod.name] = 0
        for c in mod.clauses:
            if (c.standard, c.section) in crosswalked_keys:
                shared[mod.name] += 1
            else:
                own_only[mod.name] += 1

    output = {
        "summary": {
            "modules_in_scope": [m.name for m in modules],
            "total_crosswalks": len(crosswalks),
            "per_module_shared_clauses": shared,
            "per_module_own_only_clauses": own_only,
        },
        "crosswalks": crosswalks,
    }

    if args.format == "json":
        rendered = json.dumps(output, indent=2, sort_keys=True)
    else:
        rendered = _format_crosswalk_markdown(output)

    if args.output == "-":
        print(rendered)
    else:
        Path(args.output).write_text(rendered + "\n", encoding="utf-8")
        print(
            f"wrote crosswalk report ({len(crosswalks)} overlaps) to {args.output}"
        )
    return 0


def _format_crosswalk_markdown(output: dict) -> str:
    s = output["summary"]
    lines: list[str] = []
    lines.append("# Open QMS — clause crosswalk")
    lines.append("")
    lines.append(
        f"**Modules in scope:** {', '.join('`' + n + '`' for n in s['modules_in_scope'])}"
    )
    lines.append(f"**Total cross-module (standard, section) overlaps:** {s['total_crosswalks']}")
    lines.append("")
    lines.append("**Per-module clause distribution:**")
    lines.append("")
    lines.append("| Module | Shared (crosswalked) | Own-only |")
    lines.append("|---|---|---|")
    for mod_name in s["modules_in_scope"]:
        lines.append(
            f"| `{mod_name}` | {s['per_module_shared_clauses'][mod_name]} | "
            f"{s['per_module_own_only_clauses'][mod_name]} |"
        )
    lines.append("")
    if output["crosswalks"]:
        lines.append("## Crosswalk details")
        lines.append("")
        for cw in output["crosswalks"]:
            lines.append(f"### {cw['standard']} — `{cw['section']}`")
            lines.append("")
            lines.append("| Module | Clause ID | Summary preview |")
            lines.append("|---|---|---|")
            for e in cw["entries"]:
                lines.append(
                    f"| `{e['module']}` | `{e['clause_id']}` | {e['summary_preview']} |"
                )
            lines.append("")
    return "\n".join(lines)


# ============================================================================
# OQ-117: openqms jurisdictions-query — standards by jurisdiction
# ============================================================================


# Publisher → jurisdiction-id mapping (inference fallback when registry lacks
# explicit per-standard jurisdiction tag). Covers the major regulatory
# publishers known to Open QMS.
_PUBLISHER_TO_JURISDICTIONS: dict[str, tuple[str, ...]] = {
    "U.S. Food and Drug Administration": ("FDA", "FDA-Food"),
    "U.S. Environmental Protection Agency": ("EPA",),
    "U.S. Department of Transportation, Pipeline and Hazardous Materials Safety Administration (PHMSA)": ("DOT", "PHMSA"),
    "U.S. National Highway Traffic Safety Administration": ("NHTSA",),
    "U.S. Federal Aviation Administration": ("FAA",),
    "U.S. Department of Defense": ("DoD",),
    "U.S. Department of Health and Human Services": ("HHS", "OCR", "CMS"),
    "U.S. Department of Labor (Occupational Safety and Health Administration)": ("OSHA",),
    "U.S. Occupational Safety and Health Administration": ("OSHA",),
    "U.S. Department of Agriculture (Food Safety and Inspection Service)": ("USDA-FSIS",),
    "U.S. Pharmacopeial Convention": ("USP",),
    "U.S. Congress / HHS / FDA": ("FDA", "HHS"),
    "U.S. State Legislatures": ("US-States",),
    "State of California": ("California", "CPPA"),
    "European Union": ("EU MDR", "EMA", "ECHA"),
    "European Medicines Agency": ("EMA",),
    "European Aviation Safety Agency": ("EASA",),
    "International Organization for Standardization": ("INTL",),
    "International Civil Aviation Organization": ("ICAO",),
    "International Air Transport Association": ("INTL",),
    "International Maritime Organization (IMO)": ("INTL",),
    "United Nations Economic Commission for Europe (UNECE)": ("UNECE",),
    "Intergovernmental Organisation for International Carriage by Rail (OTIF)": ("OTIF",),
    "Organisation for Economic Co-operation and Development (OECD)": ("OECD",),
    "AICPA": ("AICPA", "US"),
    "PCI Security Standards Council": ("INTL",),
    "HITRUST Alliance": ("US",),
    "National Institute of Standards and Technology": ("NIST", "US"),
    "RTCA Inc.": ("FAA", "EASA"),
    "SAE International": ("INTL",),
    "AIAG": ("US",),
    "IATF (International Automotive Task Force)": ("INTL",),
    "Codex Alimentarius Commission": ("INTL", "WHO"),
    "International Council for Harmonisation of Technical Requirements for Pharmaceuticals for Human Use (ICH)": ("INTL", "FDA", "EMA"),
    "Pharmaceutical Inspection Co-operation Scheme (PIC/S)": ("INTL",),
    "WHO": ("WHO",),
}


def _cmd_jurisdictions_query(args) -> int:
    """Query the registry for standards applicable to a given jurisdiction.

    Inference based on publisher → jurisdiction mapping (cli._PUBLISHER_TO_JURISDICTIONS)
    + any explicit jurisdictions: field on registry standards entries
    (forward-compatibility — none today have it but the field is honored).
    """
    target = args.jurisdiction.strip()
    target_norm = target.lower()

    registry = _try_load_registry()
    if registry is None:
        print("error: registry not found at ./registry/", file=sys.stderr)
        return 2

    # Build standards list with inferred jurisdictions
    matching: list[dict] = []
    for std in registry.standards:
        # Forward-compatible explicit field (None today)
        explicit = getattr(std, "jurisdictions", None) or ()
        inferred = _PUBLISHER_TO_JURISDICTIONS.get(std.publisher, ())
        all_jurs = tuple(explicit) + inferred

        # Match by id, by alias, or by case-insensitive prefix
        if any(
            j.lower() == target_norm
            or target_norm in j.lower()
            or j.lower() in target_norm
            for j in all_jurs
        ):
            matching.append({
                "id": std.id,
                "name": std.name,
                "publisher": std.publisher,
                "kind": std.kind,
                "license_kind": std.license_kind,
                "inferred_jurisdictions": list(all_jurs),
            })

    matching.sort(key=lambda x: x["id"])

    output = {
        "query": target,
        "match_count": len(matching),
        "standards": matching,
    }

    if args.format == "json":
        print(json.dumps(output, indent=2, sort_keys=True))
    elif args.format == "md":
        print(f"# Standards in jurisdiction `{target}`")
        print()
        print(f"**Match count:** {len(matching)}")
        print()
        print("| Standard ID | Publisher | Kind | License | Inferred jurisdictions |")
        print("|---|---|---|---|---|")
        for m in matching:
            print(
                f"| `{m['id']}` | {m['publisher']} | {m['kind']} | "
                f"{m['license_kind']} | {', '.join(m['inferred_jurisdictions'])} |"
            )
    else:
        # text
        print(f"jurisdiction: {target}")
        print(f"matched: {len(matching)} standards")
        print()
        for m in matching:
            print(
                f"  {m['id']:50s} ({m['license_kind']:10s}) {m['publisher']}"
            )

    return 0
