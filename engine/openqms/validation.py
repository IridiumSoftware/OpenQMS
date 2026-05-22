"""Per-module validation harness — implements OQ-013.

Asserts the OQ-001 invariant on a module's own clause table:

- every clause in the module is addressed by at least one template
- every template's ``addresses`` entries resolve to clauses in the module
"""

from __future__ import annotations

from .types import Module, ValidationReport


def validate(module: Module) -> ValidationReport:
    """Validate a regulatory module against the OQ-001 invariant."""
    clause_ids = {c.id for c in module.clauses}

    addressed_in_module: set[str] = set()
    orphaned_artifacts: list[str] = []

    for template in module.templates:
        unknown = [cid for cid in template.addresses if cid not in clause_ids]
        if unknown:
            orphaned_artifacts.append(template.path)
        for cid in template.addresses:
            if cid in clause_ids:
                addressed_in_module.add(cid)

    orphaned_clauses = sorted(clause_ids - addressed_in_module)
    invariant_holds = not orphaned_clauses and not orphaned_artifacts

    return ValidationReport(
        module=module.name,
        invariant_holds=invariant_holds,
        orphaned_clauses=tuple(orphaned_clauses),
        orphaned_artifacts=tuple(sorted(orphaned_artifacts)),
    )
