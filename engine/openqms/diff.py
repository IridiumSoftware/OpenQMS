"""Matrix diffing — compare two resolved traceability matrices.

Implements OQ-015: re-resolution on mutation produces a Git-reviewable diff.
Matrices are the JSON dicts emitted by ``openqms resolve``; the diff lists
standards added/removed, in-scope clauses added/removed, artifacts
added/removed, per-artifact address-set changes, and any module-version
change.

The matrix file itself (``bundles/<name>.matrix.json``) is the load-bearing
audit artifact — its Git diff is the regulatory record of how scope and
artifacts co-evolved. This module's structured-diff output is the
human-readable explanation that lives in the regenerate command's stdout.
"""

from __future__ import annotations

from dataclasses import dataclass


@dataclass(frozen=True)
class MatrixDiff:
    bundle_def_name: str | None
    standards_added: tuple[str, ...]
    standards_removed: tuple[str, ...]
    clauses_added: tuple[str, ...]
    clauses_removed: tuple[str, ...]
    artifacts_added: tuple[str, ...]
    artifacts_removed: tuple[str, ...]
    # path -> (added_clause_ids, removed_clause_ids); only populated for
    # artifacts present in both matrices (whole-artifact add/remove is in
    # artifacts_added / artifacts_removed).
    addresses_changed: dict[str, tuple[tuple[str, ...], tuple[str, ...]]]
    module_version_change: tuple[str, str] | None

    @property
    def has_changes(self) -> bool:
        return bool(
            self.standards_added
            or self.standards_removed
            or self.clauses_added
            or self.clauses_removed
            or self.artifacts_added
            or self.artifacts_removed
            or self.addresses_changed
            or self.module_version_change
        )


def diff_matrices(
    old: dict, new: dict, bundle_def_name: str | None = None
) -> MatrixDiff:
    """Compute the structured diff between two resolved matrices."""
    old_stds = set(old.get("bundle", {}).get("standards", []))
    new_stds = set(new.get("bundle", {}).get("standards", []))

    old_clauses = {c["id"] for c in old.get("in_scope_clauses", [])}
    new_clauses = {c["id"] for c in new.get("in_scope_clauses", [])}

    old_artifacts = {a["path"] for a in old.get("artifacts", [])}
    new_artifacts = {a["path"] for a in new.get("artifacts", [])}

    old_fwd = old.get("traceability", {}).get("forward", {})
    new_fwd = new.get("traceability", {}).get("forward", {})

    addresses_changed: dict[str, tuple[tuple[str, ...], tuple[str, ...]]] = {}
    for path in sorted(set(old_fwd) | set(new_fwd)):
        if path not in old_artifacts or path not in new_artifacts:
            # whole-artifact add or remove — surfaced elsewhere
            continue
        old_set = set(old_fwd.get(path, []))
        new_set = set(new_fwd.get(path, []))
        if old_set != new_set:
            addresses_changed[path] = (
                tuple(sorted(new_set - old_set)),
                tuple(sorted(old_set - new_set)),
            )

    old_ver = old.get("module", {}).get("version")
    new_ver = new.get("module", {}).get("version")
    version_change = (old_ver, new_ver) if old_ver != new_ver else None

    return MatrixDiff(
        bundle_def_name=bundle_def_name,
        standards_added=tuple(sorted(new_stds - old_stds)),
        standards_removed=tuple(sorted(old_stds - new_stds)),
        clauses_added=tuple(sorted(new_clauses - old_clauses)),
        clauses_removed=tuple(sorted(old_clauses - new_clauses)),
        artifacts_added=tuple(sorted(new_artifacts - old_artifacts)),
        artifacts_removed=tuple(sorted(old_artifacts - new_artifacts)),
        addresses_changed=addresses_changed,
        module_version_change=version_change,
    )


def format_diff(diff: MatrixDiff) -> str:
    """Render a human-readable diff for the CLI."""
    name = diff.bundle_def_name or "<unnamed>"
    lines = [f"=== diff: {name} ==="]

    if not diff.has_changes:
        lines.append("(no changes)")
        return "\n".join(lines)

    if diff.module_version_change:
        old, new = diff.module_version_change
        lines.append(f"Module version: {old} → {new}")

    if diff.standards_added or diff.standards_removed:
        lines.append("Standards:")
        for s in diff.standards_added:
            lines.append(f"  + {s}")
        for s in diff.standards_removed:
            lines.append(f"  - {s}")

    if diff.clauses_added or diff.clauses_removed:
        lines.append("In-scope clauses:")
        for c in diff.clauses_added:
            lines.append(f"  + {c}")
        for c in diff.clauses_removed:
            lines.append(f"  - {c}")

    if diff.artifacts_added or diff.artifacts_removed:
        lines.append("Artifacts:")
        for a in diff.artifacts_added:
            lines.append(f"  + {a}")
        for a in diff.artifacts_removed:
            lines.append(f"  - {a}")

    if diff.addresses_changed:
        lines.append("Per-artifact addressed-clause changes:")
        for path, (added, removed) in diff.addresses_changed.items():
            lines.append(f"  {path}:")
            for c in added:
                lines.append(f"    + {c}")
            for c in removed:
                lines.append(f"    - {c}")

    return "\n".join(lines)
