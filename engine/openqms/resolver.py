"""Bundle resolver — pure function from ``(Bundle, Module)`` to ``ResolvedQMS``.

Implements OQ-010. The resolver filters the module's clause table to the
standards in the bundle, selects every template that addresses at least one
in-scope clause, and emits the bidirectional traceability map (OQ-001).
"""

from __future__ import annotations

from .types import Bundle, Module, ResolvedQMS


def resolve(bundle: Bundle, module: Module) -> ResolvedQMS:
    """Resolve ``bundle`` against ``module``.

    Pure function: re-running with the same inputs produces the same output.
    No I/O; no mutation of inputs.
    """
    bundle_standards = set(bundle.standards)
    in_scope = tuple(c for c in module.clauses if c.standard in bundle_standards)
    in_scope_ids = {c.id for c in in_scope}

    artifacts: list = []
    forward: dict[str, tuple[str, ...]] = {}
    reverse: dict[str, list[str]] = {c.id: [] for c in in_scope}

    for template in module.templates:
        addressed = tuple(
            cid for cid in template.addresses if cid in in_scope_ids
        )
        if not addressed:
            continue
        artifacts.append(template)
        forward[template.path] = addressed
        for cid in addressed:
            reverse[cid].append(template.path)

    return ResolvedQMS(
        bundle=bundle,
        in_scope_clauses=in_scope,
        artifacts=tuple(artifacts),
        forward=forward,
        reverse={cid: tuple(paths) for cid, paths in reverse.items()},
    )
