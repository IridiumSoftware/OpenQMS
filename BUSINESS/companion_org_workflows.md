# Companion — Organizational workflows (v0.8.0)

**Date:** 2026-05-23
**Public commits:** `aedde0b` (content) + `ec188b3` (engine version bump)
**Range:** `0b06381..ec188b3`
**Spec deltas:** OQ-063 `:open → :tested`; OQ-064 `:open → :tested`. **Zero `:open` entries milestone reached.**

## §1 Computational basis

The last two `:open` spec entries — supplier-evaluation workflow and management-review aggregation — closed in a single content commit. Both are organizational-process workflows that ISO 13485 / 21 CFR 820 require but that don't ship as default templates in most QMS scaffolds; OpenQMS now does.

**Files new:**

- `templates/qms-suppliers/APPROVED-SUPPLIER-LIST-TEMPLATE.md` — ASL with criticality classification (Critical / Major / Minor), re-evaluation triggers (scheduled + NCR + complaint + supplier-change + performance-threshold-breach), disqualified-supplier register, procurement gate.
- `templates/qms-suppliers/SUPPLIER-EVALUATION-TEMPLATE.md` — per-supplier evaluation record (initial qualification / periodic re-evaluation / triggered re-evaluation). Sections: supplier identification, QMS assessment (cert review / audit / questionnaire), capability assessment, sample/lot qualification, SQA status, approval decision with conditions, sign-off.
- `.github/ISSUE_TEMPLATE/supplier-evaluation.yml` — workflow tracker. Captures supplier, ASL ID, evaluation type, criticality, trigger record link, scope, assigned reviewer, due date.
- `docs/guide/supplier-controls.md` — process, cadence defaults table (Critical 12mo / Major 24mo / Minor 36mo), procurement-gate patterns (procedural vs automated), audit-trail integration with management review.
- `templates/qms-management-review/MANAGEMENT-REVIEW-TEMPLATE.md` — meeting record covering all ISO 13485 §5.6.2 inputs (complaint trends, audit results, CAPA status, process performance metrics, regulatory and standards changes, supplier performance, risk management updates, resource adequacy, recommendations) and §5.6.3 outputs (QMS improvements, product improvements, resource needs, action items, effectiveness statement).
- `.github/ISSUE_TEMPLATE/management-review.yml` — workflow tracker including the §5.6.2 input-aggregation checklist.
- `docs/guide/management-review.md` — workflow, `gh` CLI input-aggregation patterns (complaints, audits, CAPAs, NCRs, supplier performance, training, risk management updates), three aggregation models (light-touch CLI / scripted shell-or-Python / external eQMS), cadence defaults (quarterly / semi-annually / per-product-line), triggered-review criteria.

**Files modified:**

- `modules/medical-devices/module.yaml` — 4 new clauses: `ISO13485-5.6` (management review), `ISO13485-7.4` (purchasing), `CFR820-820.20(c)` (management review subsection isolated for sharper traceability), `CFR820-820.50` (purchasing controls). 5 new artifact bindings (3 supplier + 2 management-review).
- `engine/openqms/cli.py` — CLI semantic fix: `regenerate --write-matrix` now exits 0 on successful write regardless of whether the diff was non-empty. Pre-fix conflated "you accepted the change" with "CI dry-run detected drift." Post-fix: `--write-matrix` exits 0 if write succeeded; non-write exits 1 if changes detected.
- `bundles/example-samd.matrix.json` — regenerated to absorb the 4 new clauses + 5 new artifacts.
- `engine/openqms/{__init__,pyproject.toml}` — 0.7.0 → 0.8.0.

**Test environment:** unchanged from v0.7.0. Test count unchanged at 97 — existing regenerate suite exercises the new exit-code semantics.

**Deliberate non-shipping decision** documented in management-review guide: OpenQMS does not ship a single aggregator tool. A one-size-fits-all label taxonomy would force adopter assumptions; declining keeps the QMS pluggable. Adopters compose `gh issue list --label X --search 'created:Q1'` queries per their environment, or pipe into a small shell/Python script, or integrate with an external dashboard (Grafana, Metabase).

## §2 Results

- **Supplier-controls infrastructure complete.** ASL + evaluation record + workflow issue template + guide. Procurement-gate model (PRs to ASL = approval signatures) + cadence defaults + audit-trail integration documented.
- **Management-review infrastructure complete.** Meeting record + workflow issue template + input-aggregation guide. Three aggregation models documented (light-touch / scripted / external eQMS).
- **Zero `:open` entries milestone reached.** Every spec claim now carries at least manual evidence (`:argued`) or mechanical evidence (`:tested`). No "we haven't started yet" claims remain in the spec.
- **CLI exit-code semantics cleaned up.** `regenerate --write-matrix` now means "write happened" (exit 0), separated from the CI dry-run signal ("changes detected, did not write" → exit 1).
- **Module manifest: 20 → 24 clauses, 12 → 17 artifacts.** Validation harness green throughout.

## §3 Verification

| Spec entry | Claim | Evidence type | How |
|---|---|---|---|
| OQ-063 | Supplier-evaluation workflow shipped + bound to ISO 13485 §7.4 / 21 CFR 820.50 | example-tested | 3 templates + 1 issue template + 1 guide shipped; module manifest binds; validation harness passes. |
| OQ-064 | Management-review aggregation shipped + bound to ISO 13485 §5.6 / 21 CFR 820.20(c) | example-tested | 1 template + 1 issue template + 1 guide shipped; module manifest binds; validation harness passes. |
| OQ-067 | Regenerate exit-code semantics clarified | example-tested (via existing regenerate test suite) | `test_regenerate_baseline_when_no_prior_matrix` + `test_regenerate_reports_changes_and_exits_one` + `test_regenerate_dry_run_does_not_write_matrix` continue to pass after the fix. |

## §4 Spec impact

| S-ID | Before | After | Evidence type after |
|---|---|---|---|
| OQ-063 | `:open` | `:tested` | example-tested |
| OQ-064 | `:open` | `:tested` | example-tested |
| OQ-041 | `:argued` (notes only updated) | `:argued` | manual | ISO 13485 §5.6 + §7.4 added to machine-readable subset (now 5 clauses); broader OQ-041 claim still `:argued` until full ISO 13485 clause set is machine-readable. |
| OQ-042 | `:argued` (notes only updated) | `:argued` | manual | 21 CFR 820 §820.20(c) + §820.50 added to machine-readable subset (now 5 sections); broader claim still `:argued`. |
| OQ-038 | `:tested` | `:tested` | example-tested | Template count 11 → 14 (notes only). |

Status counts at end of v0.8.0: 31 `:tested` · 15 `:argued` · **0 `:open`** · 0 `:proved`/`:verified`/`:benchmarked`. Total 46.

**Phase 0 round-out complete + Phase 1 fully closed.** Remaining work surface from this point forward is module-coverage population (the `:argued` items where mechanical evidence requires shipping more machine-readable clause sets) plus the substrate / invariant `:argued` items that are honest-effort-bound rather than implementation-bound.
