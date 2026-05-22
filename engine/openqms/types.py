"""Data types for the Open QMS engine.

All types are frozen dataclasses; the engine treats inputs and outputs as
immutable. This matches OQ-010 (bundle resolver is a pure function) — no
observable mutation of an input is required to produce the output.
"""

from __future__ import annotations

from dataclasses import dataclass


@dataclass(frozen=True)
class Clause:
    """A regulatory clause within a standard.

    ``summary`` is a normative summary written by the module author, not a
    redistribution of standard text. See OQ-070 — modules reference clauses
    by number and summary, not by reproducing the licensed standard.
    """

    id: str
    standard: str
    section: str
    summary: str
    gap_note: str | None = None


@dataclass(frozen=True)
class ArtifactTemplate:
    """A QMS artifact template — a controlled document, issue template, or
    workflow scaffold the engine emits as part of a resolved bundle.

    ``addresses`` is the tuple of clause IDs this template addresses. The
    validation harness checks that each entry resolves to a real clause in
    the same module.
    """

    path: str
    name: str
    addresses: tuple[str, ...]


@dataclass(frozen=True)
class Module:
    """A regulatory module: standards list, clause table, artifact templates."""

    name: str
    version: str
    standards: tuple[str, ...]
    clauses: tuple[Clause, ...]
    templates: tuple[ArtifactTemplate, ...]


@dataclass(frozen=True)
class Bundle:
    """The input tuple to the resolver: ``(product, jurisdictions, standards)``."""

    product: str
    jurisdictions: tuple[str, ...]
    standards: tuple[str, ...]


@dataclass(frozen=True)
class ResolvedQMS:
    """The resolver's output.

    The OQ-001 invariant for a given resolution holds iff every entry in
    ``in_scope_clauses`` appears as a key in ``reverse`` with a non-empty
    value, and every entry in ``artifacts`` appears as a key in ``forward``
    with a non-empty value.
    """

    bundle: Bundle
    in_scope_clauses: tuple[Clause, ...]
    artifacts: tuple[ArtifactTemplate, ...]
    forward: dict[str, tuple[str, ...]]
    reverse: dict[str, tuple[str, ...]]


@dataclass(frozen=True)
class ValidationReport:
    """The per-module validation harness output. Implements OQ-013."""

    module: str
    invariant_holds: bool
    orphaned_clauses: tuple[str, ...]
    orphaned_artifacts: tuple[str, ...]
