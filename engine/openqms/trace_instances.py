"""Instance-level cross-record traceability (P15.1a).

The clause-level trace (OQ-067, ``openqms trace``) proves *"every in-scope
clause has >=1 bound template"* at the module-YAML layer. This module
operates one layer down — on the **living records** an adopter produces —
implementing the P15 design in ``BUSINESS/companion_p15_trace_schema.md``.

P15.1a scope: **Tier-1 (frontmatter) over whole-record markdown files.**
Each record declares ``record_kind`` + ``record_id`` + ``trace_links`` in
its YAML frontmatter; this module parses those, builds the instance graph,
materializes inverse edges, and checks instance-level invariants
(referential integrity + per-kind minimum-edge requirements + optional
acyclicity) against a ``trace-policy.yaml``.

Tier-2 in-body item tables and the GitHub-issue substrate are P15.1b /
P15.2 respectively and are out of scope here.
"""

from __future__ import annotations

import re
from dataclasses import dataclass, field
from pathlib import Path

from .template_schema import parse_frontmatter

# --- Controlled vocabularies (companion_p15_trace_schema.md §4 + §5) ---

# Record kinds. Product-bound kinds require a SCOPE segment in the ID when
# the policy sets require_scope; process-level kinds may be scope-less.
PRODUCT_BOUND_KINDS: frozenset[str] = frozenset(
    {"REQ", "URS", "HAZ", "MIT", "TST", "IQ", "OQ", "PQ", "FUNC"}
)
PROCESS_LEVEL_KINDS: frozenset[str] = frozenset(
    {"CAPA", "CMPL", "NCR", "CHG", "AUD", "SUP", "SYS", "VREC", "PMS"}
)
RECORD_KINDS: frozenset[str] = PRODUCT_BOUND_KINDS | PROCESS_LEVEL_KINDS

# Directed relationships -> inverse. relates_to is symmetric.
INVERSE: dict[str, str] = {
    "derived_from": "derives",
    "derives": "derived_from",
    "mitigated_by": "mitigates",
    "mitigates": "mitigated_by",
    "verified_by": "verifies",
    "verifies": "verified_by",
    "validated_by": "validates",
    "validates": "validated_by",
    "triggered_by": "triggers",
    "triggers": "triggered_by",
    "implements": "implemented_by",
    "implemented_by": "implements",
    "part_of": "comprises",
    "comprises": "part_of",
    "assured_by": "assures",
    "assures": "assured_by",
    "relates_to": "relates_to",
}
RELATIONSHIPS: frozenset[str] = frozenset(INVERSE)

# ID grammar: KIND-SCOPE-NNNN or (scope-less) KIND-NNNN. KIND is validated
# against RECORD_KINDS separately so the linter can give a precise error.
_ID_RE = re.compile(r"^([A-Z]{2,5})-(?:([A-Z0-9]+)-)?(\d{3,})$")


@dataclass(frozen=True)
class TraceNode:
    """One record instance in the trace graph."""

    record_id: str
    kind: str
    source_path: str
    # relationship -> tuple of target record IDs (as declared on this node)
    links: dict[str, tuple[str, ...]] = field(default_factory=dict)
    scope: str | None = None


@dataclass
class Finding:
    severity: str  # "error" | "warning"
    message: str


def parse_id(rid: str) -> tuple[str, str | None, str] | None:
    """Return (kind, scope, seq) for a well-formed ID, else None."""
    m = _ID_RE.match(rid)
    if not m:
        return None
    return m.group(1), m.group(2), m.group(3)


def parse_record(path: Path) -> TraceNode | None:
    """Parse a markdown file's trace frontmatter into a TraceNode.

    Returns None if the file has no frontmatter or no ``record_kind``
    (i.e. it does not participate in the instance trace at Tier-1).
    """
    fm = parse_frontmatter(path.read_text(encoding="utf-8"))
    if not fm or fm.get("__yaml_error__") or fm.get("__not_a_dict__"):
        return None
    kind = fm.get("record_kind")
    if not kind:
        return None
    rid = fm.get("record_id") or fm.get("document_id")
    parsed = parse_id(str(rid)) if rid else None
    scope = parsed[1] if parsed else None

    links: dict[str, tuple[str, ...]] = {}
    raw_links = fm.get("trace_links") or {}
    if isinstance(raw_links, dict):
        for rel, targets in raw_links.items():
            if isinstance(targets, list):
                links[str(rel)] = tuple(str(t) for t in targets)
            elif targets:
                links[str(rel)] = (str(targets),)

    return TraceNode(
        record_id=str(rid),
        kind=str(kind),
        source_path=str(path),
        links=links,
        scope=scope,
    )


def discover_records(root: Path) -> list[TraceNode]:
    """Find all trace-participating records under ``root`` (recursively)."""
    nodes: list[TraceNode] = []
    for p in sorted(root.rglob("*.md")):
        if not p.is_file():
            continue
        node = parse_record(p)
        if node is not None:
            nodes.append(node)
    return nodes


def _effective_edges(nodes: list[TraceNode]) -> set[tuple[str, str, str]]:
    """All (source_id, relationship, target_id) edges, with inverses
    materialized so a query works regardless of which endpoint declared it."""
    edges: set[tuple[str, str, str]] = set()
    for n in nodes:
        for rel, targets in n.links.items():
            inv = INVERSE.get(rel)
            for t in targets:
                edges.add((n.record_id, rel, t))
                if inv:
                    edges.add((t, inv, n.record_id))
    return edges


def lint_records(nodes: list[TraceNode], require_scope: bool = True) -> list[Finding]:
    """Static grammar/vocabulary checks (the `lint-trace-links` surface).

    Checks, per record: well-formed ID; known KIND prefix matching
    declared record_kind; known relationships; and (when require_scope)
    a SCOPE segment on product-bound kinds.
    """
    findings: list[Finding] = []
    seen: dict[str, str] = {}
    for n in nodes:
        parsed = parse_id(n.record_id)
        if parsed is None:
            findings.append(Finding("error", f"{n.source_path}: malformed record_id {n.record_id!r} (expect KIND-SCOPE-NNNN)"))
        else:
            id_kind, scope, _ = parsed
            if n.kind not in RECORD_KINDS:
                findings.append(Finding("error", f"{n.source_path}: unknown record_kind {n.kind!r}"))
            if id_kind != n.kind:
                findings.append(Finding("error", f"{n.source_path}: record_id prefix {id_kind!r} != record_kind {n.kind!r}"))
            if require_scope and n.kind in PRODUCT_BOUND_KINDS and not scope:
                findings.append(Finding("error", f"{n.source_path}: {n.kind} {n.record_id!r} needs a SCOPE segment (require_scope)"))
        if n.record_id in seen:
            findings.append(Finding("error", f"{n.source_path}: duplicate record_id {n.record_id!r} (also in {seen[n.record_id]})"))
        seen[n.record_id] = n.source_path
        for rel in n.links:
            if rel not in RELATIONSHIPS:
                findings.append(Finding("error", f"{n.source_path}: unknown relationship {rel!r} on {n.record_id}"))
    return findings


def check_invariants(nodes: list[TraceNode], policy: dict) -> list[Finding]:
    """Runtime invariant checks against a trace-policy dict."""
    findings: list[Finding] = []
    ids = {n.record_id for n in nodes}
    edges = _effective_edges(nodes)

    # Referential integrity: every referenced target must resolve to a node.
    if policy.get("referential_integrity", "error") != "off":
        sev = policy.get("referential_integrity", "error")
        for n in nodes:
            for rel, targets in n.links.items():
                for t in targets:
                    if t not in ids:
                        findings.append(Finding(sev, f"{n.record_id} {rel} -> {t}: target does not resolve to any record"))

    # Per-kind minimum-edge requirements.
    by_kind: dict[str, list[TraceNode]] = {}
    for n in nodes:
        by_kind.setdefault(n.kind, []).append(n)
    for rule in policy.get("require", []):
        kind, edge, minimum = rule.get("kind"), rule.get("edge"), int(rule.get("min", 1))
        sev = rule.get("severity", "error")
        for n in by_kind.get(kind, []):
            count = sum(1 for (s, r, _t) in edges if s == n.record_id and r == edge)
            if count < minimum:
                findings.append(Finding(sev, f"{n.kind} {n.record_id} has {count} {edge} edge(s); policy requires >= {minimum}"))

    # Optional acyclicity on named relationships.
    for rel in policy.get("no_cycles", []):
        adj: dict[str, list[str]] = {}
        for (s, r, t) in edges:
            if r == rel:
                adj.setdefault(s, []).append(t)
        if _has_cycle(adj):
            findings.append(Finding("error", f"cycle detected in `{rel}` relationship graph"))
    return findings


def _has_cycle(adj: dict[str, list[str]]) -> bool:
    WHITE, GREY, BLACK = 0, 1, 2
    color: dict[str, int] = {}

    def visit(u: str) -> bool:
        color[u] = GREY
        for v in adj.get(u, []):
            c = color.get(v, WHITE)
            if c == GREY or (c == WHITE and visit(v)):
                return True
        color[u] = BLACK
        return False

    return any(color.get(u, WHITE) == WHITE and visit(u) for u in list(adj))


def build_report(nodes: list[TraceNode], policy: dict) -> dict:
    """Forward/reverse maps + invariant findings + summary."""
    edges = _effective_edges(nodes)
    forward: dict[str, list[str]] = {}
    for (s, r, t) in sorted(edges):
        forward.setdefault(s, []).append(f"{r}:{t}")
    findings = check_invariants(nodes, policy)
    return {
        "nodes": {n.record_id: {"kind": n.kind, "source": n.source_path} for n in nodes},
        "edges": forward,
        "findings": [{"severity": f.severity, "message": f.message} for f in findings],
        "summary": {
            "records": len(nodes),
            "kinds": sorted({n.kind for n in nodes}),
            "edges": len(edges),
            "errors": sum(1 for f in findings if f.severity == "error"),
            "warnings": sum(1 for f in findings if f.severity == "warning"),
        },
    }


# Default policy used when no trace-policy.yaml is supplied.
DEFAULT_POLICY: dict = {
    "referential_integrity": "error",
    "no_cycles": ["derived_from"],
    "require": [
        {"kind": "HAZ", "edge": "mitigated_by", "min": 1, "severity": "error"},
        {"kind": "MIT", "edge": "verified_by", "min": 1, "severity": "error"},
        {"kind": "REQ", "edge": "verified_by", "min": 1, "severity": "warning"},
        {"kind": "CAPA", "edge": "triggered_by", "min": 1, "severity": "error"},
        {"kind": "FUNC", "edge": "assured_by", "min": 1, "severity": "error"},
    ],
}
