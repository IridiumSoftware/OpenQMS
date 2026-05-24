# Companion — Engine MVP (v0.2.0)

**Date:** 2026-05-22
**Public commit:** `4a72a9f` on `github.com/IridiumSoftware/OpenQMS` main (`43acffe..4a72a9f`, 21 files / +1033 / −6)
**Spec deltas:** OQ-001, OQ-010, OQ-013, OQ-040, OQ-066 transition `:open`/`:argued` → `:tested`

## §1 Computational basis

Implemented the Open QMS generator engine as a Python 3.11+ package at `engine/`.

**Files (new):**
- `engine/pyproject.toml` — hatchling build, Apache-2.0, runtime dep on `pyyaml>=6.0`, dev extra on `pytest>=8.0`, `openqms = "openqms.cli:main"` script entry.
- `engine/openqms/__init__.py` — version string.
- `engine/openqms/__main__.py` — `python -m openqms` entry.
- `engine/openqms/types.py` — frozen dataclasses: `Clause`, `ArtifactTemplate`, `Module`, `Bundle`, `ResolvedQMS`, `ValidationReport`.
- `engine/openqms/module.py` — YAML manifest loader (`load_module`).
- `engine/openqms/resolver.py` — `resolve(Bundle, Module) -> ResolvedQMS`. Pure function.
- `engine/openqms/validation.py` — `validate(Module) -> ValidationReport`. Asserts no orphaned clauses, no orphaned artifacts.
- `engine/openqms/cli.py` — argparse CLI with `resolve` and `validate` subcommands.
- `engine/tests/conftest.py` — fixtures (`repo_root`, `fixtures_dir`).
- `engine/tests/fixtures/smoke_module.yaml` — 3-clause / 2-template fixture for unit tests.
- `engine/tests/test_module.py` (4 tests), `test_resolver.py` (5 tests), `test_validation.py` (4 tests), `test_medical_devices.py` (2 tests). Total 15.
- `engine/README.md` — install + CLI + architecture summary.
- `modules/medical-devices/module.yaml` — first shipped regulatory module manifest. Four clauses (ISO 13485 §4.2.4, §7.3; 21 CFR 820 §820.30, §820.40) bound to three artifact templates.
- `modules/medical-devices/README.md` — module status + coverage roadmap + licensing note.
- `.github/workflows/engine-tests.yml` — CI workflow running pytest + `openqms validate --module medical-devices` on every push touching `engine/`, `modules/`, or `templates/`.

**Files modified:**
- `README.md` — added engine to "What's included" list, new "Generator engine" section after Quick start, architecture diagram includes `engine/`, "How it works" gains module-clause-coverage row.
- `.gitignore` — expanded to cover `.venv*/`, `*.egg-info/`, `.pytest_cache/`, `.ruff_cache/`, `.mypy_cache/`.

**Files removed:**
- `modules/medical-devices/.gitkeep` — replaced by `module.yaml` + `README.md`.

**Build / install:**
```bash
python3 -m venv .venv-engine
source .venv-engine/bin/activate
pip install -e './engine[dev]'
```

**Test run (local, Python 3.14.4 on Darwin 25.5.0, pytest 9.0.3):**
```
============================= test session starts ==============================
collected 15 items
engine/tests/test_medical_devices.py::test_medical_devices_module_invariant_holds PASSED
engine/tests/test_medical_devices.py::test_medical_devices_resolve_smoke PASSED
engine/tests/test_module.py::test_load_smoke_fixture PASSED
engine/tests/test_module.py::test_missing_module_raises PASSED
engine/tests/test_module.py::test_module_missing_name_raises PASSED
engine/tests/test_module.py::test_clause_missing_required_field_raises PASSED
engine/tests/test_resolver.py::test_resolve_filters_to_in_scope_standards PASSED
engine/tests/test_resolver.py::test_resolve_is_deterministic PASSED
engine/tests/test_resolver.py::test_resolve_bidirectional_traceability PASSED
engine/tests/test_resolver.py::test_resolve_drops_templates_with_no_in_scope_clauses PASSED
engine/tests/test_resolver.py::test_resolve_with_empty_standards_yields_empty_qms PASSED
engine/tests/test_validation.py::test_smoke_module_validates PASSED
engine/tests/test_validation.py::test_detects_orphaned_clause PASSED
engine/tests/test_validation.py::test_detects_orphaned_artifact PASSED
engine/tests/test_validation.py::test_detects_both_orphan_types PASSED
============================== 15 passed in 0.20s ==============================
```

**CLI smoke run (local):**
```
$ openqms validate --module medical-devices
module:           medical-devices
invariant_holds:  True
(exit 0)

$ openqms resolve --product ExampleDevice --jurisdiction FDA \
    --standard "ISO 13485:2016" --standard "21 CFR 820" \
    --module medical-devices --output /tmp/openqms_smoke_matrix.json
wrote /tmp/openqms_smoke_matrix.json
```

The resulting JSON contains `bundle`, `module`, `in_scope_clauses` (4 entries — all four clauses in the manifest fall under the bundle's standards), `artifacts` (3 entries — all three templates address ≥1 in-scope clause), `traceability.forward` (3 keys mapping artifact paths to clause-id tuples), `traceability.reverse` (4 keys mapping clause IDs to artifact-path tuples).

## §2 Results

The engine MVP demonstrates the OQ-001 invariant mechanically on the medical-devices reference module. Specifically:

- **Resolver determinism (OQ-010).** Re-running `resolve(bundle, module)` on identical inputs produces identical output. Verified by `test_resolve_is_deterministic`.
- **Bidirectional traceability (OQ-001).** For the ExampleDevice / FDA / (ISO 13485 + 21 CFR 820) bundle, every in-scope clause maps to ≥1 artifact and every emitted artifact maps to ≥1 clause; the forward and reverse maps agree as a bijection on the in-scope set. Verified by `test_resolve_bidirectional_traceability` (on smoke fixture) and `test_medical_devices_resolve_smoke` (on shipped module).
- **Per-module validation harness (OQ-013).** The harness detects orphaned clauses (clauses not addressed by any template) and orphaned artifacts (templates addressing non-existent clauses); both detection cases are unit-tested. The medical-devices module-as-shipped passes the harness.
- **Filter behavior.** Templates that address only out-of-scope clauses are dropped from the resolved artifact set. Verified by `test_resolve_drops_templates_with_no_in_scope_clauses`.
- **Edge case.** Empty standards set yields empty resolved QMS (no clauses, no artifacts, empty maps). Verified by `test_resolve_with_empty_standards_yields_empty_qms`.
- **Module loader.** Missing manifest, missing required fields, and malformed clause records all raise the expected exceptions. Verified by three negative-path tests in `test_module.py`.

The shipped medical-devices module covers 4 of the 27 clauses enumerated in the full crosswalk at `BUSINESS/regulatory_modules/medical_devices_crosswalk.md`. The remaining 23 are tracked as forward population work under priority P6 of `dashboard.md`.

## §3 Verification

| Spec entry | Claim | Evidence type | How |
|---|---|---|---|
| OQ-001 | Bidirectional traceability invariant | example-tested | `test_medical_devices_resolve_smoke` + `test_resolve_bidirectional_traceability` assert both forward and reverse maps are non-empty for every in-scope clause / emitted artifact, and that they agree as a bijection. |
| OQ-010 | Bundle resolver is a pure function | example-tested | `test_resolve_is_deterministic` asserts `resolve(b, m) == resolve(b, m)`. Type annotations on `resolve()` declare the signature. No I/O or mutation in the function body. |
| OQ-013 | Per-module validation harness | example-tested | `test_smoke_module_validates`, `test_detects_orphaned_clause`, `test_detects_orphaned_artifact`, `test_detects_both_orphan_types` cover the positive and both negative cases. |
| OQ-040 | Medical-devices module is the first reference module | example-tested | `modules/medical-devices/module.yaml` shipped at commit `4a72a9f`; `openqms validate --module medical-devices` passes; integration tests load and resolve it. |
| OQ-066 | Generator validation harness | example-tested | The harness is `openqms.validation.validate`; tests above demonstrate it functions. Implements OQ-013. |

No `:verified` (property-tested) or `:proved` (lean-proved / type-checked at mypy strictness / algebraic) evidence on this pass. Upgrading OQ-010 to `:verified` would require hypothesis-style property tests over arbitrary input tuples; upgrading to `:proved` would require either runtime type enforcement (e.g. `mypy --strict` in CI) or porting the resolver to a language with checked types. Both are forward enhancements.

## §4 Spec impact

| S-ID | Status before | Status after | Evidence type after |
|---|---|---|---|
| OQ-001 | `:argued` | `:tested` | example-tested |
| OQ-010 | `:open` | `:tested` | example-tested |
| OQ-013 | `:open` | `:tested` | example-tested |
| OQ-040 | `:argued` | `:tested` | example-tested |
| OQ-066 | `:open` | `:tested` | example-tested |

Other entries unchanged:

- **OQ-011** (modules compose under union) — stays `:open`. The resolver takes a single `Module`; composition is not implemented. Forward work.
- **OQ-012** (cross-cutting overlays compose) — stays `:open`. Depends on OQ-011.
- **OQ-014** (standards-and-jurisdictions registry versioned + immutable) — stays `:open`. No registry yet; standards are referenced as free-form strings on the CLI.
- **OQ-015** (re-resolution on mutation produces Git-reviewable diff) — stays `:open`. No mutation handling yet.
- **OQ-041..OQ-048** (per-standard module coverage) — stay `:argued`. The full crosswalks remain manual; the shipped module covers only 4 clauses across ISO 13485 and 21 CFR 820. Notes updated to record the partial mechanization.

Status counts after v0.2.0: 19 `:tested` / 13 `:argued` / 7 `:open` / 0 `:proved` / `:verified` / `:benchmarked`. Total 39.

Cross-audit (A0-A6) re-run after the v0.2.0 updates is in `dashboard.md`. No drift detected.
