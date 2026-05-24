# Companion — Phase 1 engine completion (v0.4.0 + v0.5.0 + v0.6.0)

**Dates:** 2026-05-22 → 2026-05-23
**Public commits:** `2a146ad` (v0.4.0 P1.1) + `12b6b33` (v0.5.0 P1.2) + `3cfec2c` (v0.6.0 P1.3)
**Range:** `2625b98..3cfec2c`
**Spec deltas:** OQ-011, OQ-012, OQ-014, OQ-015, OQ-048, OQ-065 all `:open → :tested`.

## §1 Computational basis

Phase 1 closed in three commits: multi-module composition, standards-and-jurisdictions registry, and re-resolution-on-mutation with edition supersession. Each addresses a distinct engine primitive; together they make the OpenQMS engine production-shaped (not just MVP).

### v0.4.0 — P1.1: Multi-module composition + iso-27001 overlay

New `compose(modules: list[Module]) -> Module` primitive in `engine/openqms/module.py`. Unions clauses by ID (conflicts raise), template addresses by path (merged), standards (deduped). Empty input raises; single-element returns unchanged.

- `engine/openqms/cli.py` — `--module` repeatable on both `resolve` and `validate`; engine internally calls `compose` before resolving.
- `modules/iso-27001/module.yaml` — first cross-cutting overlay module. 3 Annex A clauses bound to existing OpenQMS templates that the medical-devices vertical also binds.
- `engine/tests/test_composition.py` — 13 new tests covering compose semantics + integration with iso-27001 overlay.

### v0.5.0 — P1.2: Standards-and-jurisdictions registry

`registry/standards.yaml` (15 entries: medical-devices crosswalk + cross-cutting + AI-regulation roadmap) + `registry/jurisdictions.yaml` (6 entries: FDA, Health Canada, EU MDR, PMDA, TGA, ANVISA).

- `engine/openqms/registry.py` — `Registry` / `StandardEntry` / `JurisdictionEntry` frozen dataclasses; `load_registry()` with dangling-reference cross-check; `validate_module_against_registry()`.
- `engine/openqms/cli.py` — `--standard` arguments normalized to canonical IDs via aliases (e.g. `"ISO 13485"` → `"ISO 13485:2016"`); unknown standards / jurisdictions raise. New `openqms registry list/show --id` subcommand. Escape hatch `--allow-unregistered-standards`.
- `engine/tests/test_registry.py` — 21 new tests (8 unit, 4 shipped-registry, 2 negative loader, 2 negative module-vs-registry, 5 CLI subprocess integration).

### v0.6.0 — P1.3: Regenerate workflow + edition supersession

New `openqms regenerate --bundle <name>` CLI subcommand. Re-resolves a stored bundle definition at `bundles/<name>.yaml` and diffs against the prior matrix at `bundles/<name>.matrix.json`.

- `engine/openqms/bundle.py` — `BundleDef` frozen dataclass + `load_bundle_def(path)`.
- `engine/openqms/diff.py` — `MatrixDiff` + `diff_matrices(old, new)` + `format_diff(diff)`. Standards/clauses/artifacts added/removed; per-artifact address-set changes; module-version change.
- `engine/openqms/registry.py` — `StandardEntry.superseded_by: str | None = None`; `RegistryValidationReport.superseded_standards` list of `(old, new)` pairs.
- `engine/openqms/cli.py` — `regenerate` subcommand with `--write-matrix` and `--strict-editions` flags.
- `bundles/example-samd.yaml` + `bundles/example-samd.matrix.json` — first stored bundle + committed baseline matrix. CI runs `regenerate --bundle example-samd` (dry-run) on every push touching `engine/` / `modules/` / `registry/` / `templates/` / `bundles/`.
- `engine/tests/test_bundle.py` + `test_diff.py` + `test_regenerate.py` — 25 new tests.

**Build / test:** `pip install -e './engine[dev]'` + `pytest engine/tests -v`. Test count grew **15 → 28 → 49 → 74** across the three commits, all green.

## §2 Results

- **Composition primitive shipped.** Modules can now be composed at runtime — vertical regulatory modules (medical-devices) compose with cross-cutting overlays (iso-27001) and the OQ-001 traceability invariant holds on the composite.
- **Registry catches typo / drift.** Pre-v0.5.0, `--standard "ISO 13485:2017"` silently filtered to zero clauses. Post-v0.5.0, it raises with the registered-IDs listed.
- **Idempotent regenerate.** First run after bundle creation writes the baseline matrix; subsequent dry-runs against unchanged inputs report `(no changes)` and exit 0. This is the regression-detection mechanism CI uses.
- **Supersession mechanism in place.** No supersessions in the shipped registry today, but the field exists. When ISO 13485:2026 supersedes 2016, registry-PR adds `superseded_by` to the 2016 entry; existing modules then surface warnings (or `--strict-editions` errors) on validate / regenerate.
- **Counting discrepancy reconciled.** At v0.6.0 the running spec total was off-by-6 (tracked 40, actually 46). Fixed at v0.6.0 — per-version transition records were always accurate; only the totals had drifted.

## §3 Verification

| Spec entry | Claim | Evidence type | How |
|---|---|---|---|
| OQ-011 | Modules compose under union; deduplication preserves invariant | example-tested | 11 unit tests in `test_composition.py` + integration test against iso-27001 overlay. |
| OQ-012 | Cross-cutting overlays compose with vertical modules | example-tested | `test_medical_devices_plus_iso27001_*` tests pass; resolve produces merged template addresses. |
| OQ-048 | ISO/IEC 27001 overlay shipped | example-tested | `modules/iso-27001/module.yaml` ships with 3 clauses bound to existing templates; validate green. |
| OQ-014 | Standards-and-jurisdictions registry is versioned and consulted | example-tested | 21 tests in `test_registry.py`; CLI rejects unknown standards/jurisdictions; module manifests cross-checked. |
| OQ-015 | Re-resolution on mutation produces Git-reviewable diff | example-tested | 8 CLI subprocess tests in `test_regenerate.py`; shipped-example regression test asserts no drift. |
| OQ-065 | Module-version drift detection | example-tested | 2 tests (`test_validate_warns_on_superseded_standard` + `test_validate_strict_editions_fails_on_superseded_standard`) inject supersessions into a tmp registry and assert behavior. |

## §4 Spec impact

| S-ID | Before | After | Evidence type after |
|---|---|---|---|
| OQ-011 | `:open` | `:tested` | example-tested |
| OQ-012 | `:open` | `:tested` | example-tested |
| OQ-014 | `:open` | `:tested` | example-tested |
| OQ-015 | `:open` | `:tested` | example-tested |
| OQ-048 | `:argued` | `:tested` | example-tested |
| OQ-065 | `:open` | `:tested` | example-tested |

Status counts at end of v0.6.0: 28 `:tested` / 15 `:argued` / 3 `:open` (total 46 — totals reconciled at this version).

**Phase 1 fully closed.** All four Phase 1 priorities (P1.1 composition, P1.2 registry, P1.3 re-resolution + supersession) shipped. Engine is now production-shaped.
