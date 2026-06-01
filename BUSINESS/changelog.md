# Changelog — Open QMS

Versioned, top-down. Each entry summarizes spec deltas, evidence changes, and material project events.

---

## v0.68.0 DRAFT — 2026-06-01 — Finance vertical (SOX / ICFR — 8th vertical)

**OQ-130 NEW `:tested` (Module-tier).** The eighth vertical — the *QMS-of-financial-reporting*: Internal Control over Financial Reporting (ICFR) for US public companies.

- **`modules/finance/`** — 16 clauses across the SOX/ICFR spine: Sarbanes-Oxley §302 / §404(a) / §404(b) + SEC Exchange Act 13a-15/15d-15 + COSO 2013 (5 components / 17 principles, incl. fraud risk + management override) + PCAOB AS 2201 (top-down scoping, risk-control matrix, design + operating-effectiveness testing, deficiency evaluation, ITGC).
- **6 templates** (`templates/qms-finance/`): ICFR Risk-Control Matrix · Entity-Level Controls · ITGC Register · Control Test Plan & Results · SOX Certification (§302+§404) · Control Deficiency Log (a P15 Tier-2 trace table — deficiency = `NCR` → `triggers` `CAPA`).
- **Registry +4:** Sarbanes-Oxley Act + SEC Exchange Act ICFR rules + COSO IC-IF 2013 + PCAOB AS 2201.
- Composes with the existing financial overlays (iso-27001 ITGC · iso-37301-financial-services + soc-2 · dora/nist-csf/iso-22301 resilience) — all validated. **4 tests** (286 → 290); CI +4 validate steps; guide `docs/guide/finance-sox-icfr.md`.
- **Public surface synced** (README / index / catalog → v0.68.0): verticals 7→8, modules 119→120, templates 113→119, standards 140→144, spec 113→114, CLI 10→11 (index).

**Engine unchanged at 0.66.0** (finance is content). A0–A6 cross-audit `audit_2026-06-01_v0_68.md`. Status counts: 6 `:verified` / 103 `:tested` / 5 `:argued` / 0 `:open` (total 114). Forward-work arc remains 15/15 closed — finance is net-new scope beyond it.

---

## v0.67.0 DRAFT — 2026-06-01 — Public-surface cross-audit + sync (hygiene)

**0 NEW spec entries.** Remediation only — engine unchanged at 0.66.0. A dedicated cross-audit of the **public surface** found it lagging the BUSINESS/ tracking by ~6 releases (user-flagged: the GitHub README still showed v0.64.0).

- **Synced** `README.md` (v0.64.0→v0.66.0), `docs/index.md` (v0.63.0→v0.66.0), `docs/modules-catalog.md` (v0.64.0→v0.66.0) to current ground truth: **113** spec entries (6 `:verified` / 102 `:tested` / 5 `:argued` / 0 `:open`) · **119** modules · **113** templates / **1,012** clause→template bindings · **140** registry standards · **11** CLI subcommands · validation family + `trace-instances` now listed. Also fixed README architecture-tree comments frozen at "80 spec entries / 57 templates / 108 tests".
- **Critical A1/A2 fix:** `docs/compliance-architecture.md` forward-work still listed **P2 + P15 as open** ("2 hard remaining") — directly contradicting the dashboard (15/15 closed) and the spec (OQ-128 / OQ-129 shipped). Both marked **✓ closed** (v0.65.0 / v0.66.0); the section now reads "all 15 priorities closed; 0 open."
- New cross-audit `BUSINESS/audit_2026-06-01_v0_67.md`. Status counts unchanged: 6 `:verified` / 102 `:tested` / 5 `:argued` / 0 `:open` (total 113). Forward-work: **15 of 15 closed — queue empty.**

---

## v0.66.0 DRAFT — 2026-06-01 — Instance-level traceability (P15) — forward-work arc complete

**OQ-129 NEW `:tested` (Architecture-tier).** Closes compliance-architecture forward-work **P15** — the last hard priority. `openqms trace-instances` + `engine/openqms/trace_instances.py`: the instance-level cross-record trace graph (the analog of clause-level `openqms trace` / OQ-067).

- **Three substrates, one graph:** Tier-1 whole-record markdown frontmatter + Tier-2 in-body item tables (RMF hazards, SRS requirements) + the GitHub-issue substrate (CAPA/complaint/NCR by label, `KIND-<issue#>`, via `--github` live / `--issues-json` export).
- **Typed directed edges** with auto-materialized inverse; static lint (ID grammar + vocabulary + scope) + runtime invariants (referential integrity + per-kind minimum edges + acyclicity) via a configurable `trace-policy.yaml`; exit 1 on error (CI gate).
- Committed worked example `examples/trace-instances/` CI-gated at 0 errors (12 records / 16 edges). RMF template migrated to the Tier-2 shape; `capa`/`complaint`/`nonconformance` issue forms gained a `Trace links` field.
- **21 pytest tests** (`test_trace_instances.py`); suite 265 → 286. Phased **P15.1a** (Tier-1) → **P15.1b** (Tier-2) → **P15.2** (issues); PRs #10–#12. Guide `docs/guide/instance-traceability.md`.

**Engine 0.64.0 → 0.66.0** (P15 added engine code — first bump since the validation work; also reconciled the stale `uv.lock` openqms version 0.54.0 → 0.66.0). A0–A6 cross-audit: `audit_2026-06-01_v0_66.md`. Status counts: 6 `:verified` / 102 `:tested` / 5 `:argued` / 0 `:open` (total 113). **Forward-work: 15 of 15 closed — queue empty.** OQ-080 holds.

---

## v0.65.0 DRAFT — 2026-06-01 — Validation-package family (P2) + CI fix

**OQ-128 NEW `:tested` (Module-tier).** Closes compliance-architecture forward-work **P2** — risk-based computerized-system validation for production / QMS software, grounded in the final FDA CSA guidance (issued 2026-02-03).

- **3 composable modules:** `validation-package` (market-neutral baseline — GAMP 5 2nd ed. + ISO 13485 §4.1.6/7.5.6/7.6 + IEC/IEEE/ISO 29119-1) + `validation-package-fda` (CSA framework + 21 CFR Part 11 + Part 820/QMSR) + `validation-package-eu` (EU GMP Annex 11 + Annex 15 + ISO 13485 + ICH Q9).
- **One baseline + two orthogonal dials:** rigor = per-function assurance-tier determination (CSA Table 1; classic CSV = the robust-scripted tier); market = which overlay(s) composed (FDA + EU compose together for US+EU products, no clause-id collision).
- **8 new templates** (`templates/qms-validation/`) + **5 registry standards** + dogfood worked example (`docs/examples/openqms-self-validation.md` — Open QMS validates its own GitHub-hosted QMS as not-high-process-risk).
- **19 new pytest tests** (251 → 265). CI +12 validate steps. Adopter guide `docs/guide/validation-package.md`. Designs: `companion_p2_validation_package.md` + `companion_p15_trace_schema.md`.
- Phased **P2.1** (baseline) → **P2.2** (FDA) → **P2.3** (EU) → **P2.4** (dogfood); PRs #4–#7.

**CI fix (PR #8).** The engine-tests "Install engine + dev deps" step ran `cd engine` twice and never put the uv venv on PATH — the workflow had been failing at install since ~2026-05-25, leaving every post-install step (lint / pytest / validate / coverage / trace) silently un-run for ~a week (undetected; `main` has no branch protection). Fixed; full pipeline green again (run 26746084880).

**Engine package version unchanged at 0.64.0** — P2 is content + the CI fix is workflow-only; no `engine/openqms/*.py` changed. A0–A6 cross-audit: `audit_2026-06-01_v0_65.md`. Status counts: 6 `:verified` / 101 `:tested` / 5 `:argued` / 0 `:open` (total 112). Forward-work: 14 of 15 closed; **1 hard remaining (P15)**.

---

## v0.64.0 DRAFT — 2026-05-25 — Omnibus + cross-audit (closes v0.52-v0.63 arc)

**0 NEW entries.** Spec total unchanged at 111. Engine 0.63.0 → 0.64.0. Pure bookkeeping release closing the v0.52-v0.63 build arc cleanly.

### What ships

- **A0-A6 cross-audit** (`BUSINESS/audit_2026-05-25_v0_63.md`) — covers the 12-release window from v0.52.0 through v0.63.0:
  - A0 Self-audit: ✓
  - A1 Coverage: ✓ (111 spec / 111 registry; zero drift)
  - A2 Logic & Status parity: ✓
  - A3 Evidence exists: ✓ (spot-checked all new files in 9 new spec entries)
  - A4 Status honesty: ✓
  - A5 Stale counts: 3 findings (F-A + F-B + F-C — README + catalog scope cells were stale on `Spec entries: 103` and `Document templates: 103`); remediated inline as part of audit
  - A6 Test sync: ✓ (251/251 pytest pass; lint clean on 116 modules + 105 templates; bundle baselines clean on 8 + 4 presets; mkdocs builds clean under --strict)
- **Omnibus companion** (`BUSINESS/companion_v0_52_to_63.md`) — 12-release record covering:
  - 9 new spec entries (OQ-119..OQ-127)
  - 13 of 15 forward-work priorities closed
  - 3 new engine modules (template_schema + doc_control + verify_deployment)
  - 3 new CI scripts + 1 new CLI subcommand
  - 5 new issue templates + 5 new role/process guides
  - 2 new SOP templates + 4 new preset bundles + 1 new trust-gate document + 1 new cadence governance document + 1 new maturity-model guide
  - 1 new workflow + 1 rewritten workflow
  - Pytest count 129 → 251 (+122)
  - 6 lessons + observations captured
- **`companion_index.md`** — new omnibus row added at top of table
- **README.md + docs/modules-catalog.md** scope cells corrected (A5 remediation): `Spec entries: 111` and `Document templates: 105 on disk / 379 in-module bindings`

### Forward-work status after v0.64.0

| Status | Count | Priorities |
|---|---|---|
| ✓ Closed | 13 | P1 + P3 + P4 + P5 + P6 + P7 + P8 + P9 + P10 + P11 + P12 + P13 + P14 |
| Open hard | 2 | P2 (validation package) + P15 (integration-architecture trace network) |
| Open medium + light | 0 | (queues empty) |

Both remaining priorities are multi-session deliverables. Each warrants dedicated scope decision before kickoff.

### Pattern observation from the arc

13 substantive releases closed 13 of 15 priorities across 5 weeks of session work. The light-batch pattern (v0.55.0 closed 6 lights in 1 release) was the highest-leverage move; without it the arc would have been ~19 releases instead of 13. Light items batch well when they share infrastructure (SOP templates, governance docs, light CI additions). Medium items don't batch — each got its own release. Hard items haven't been touched and likely shouldn't be without explicit scope decisions.

No functional code change in this release. 251/251 pytest pass. Bundle baselines clean. Module lint clean. Template lint clean. Repo invariants hold (116 modules / 867 clauses / 379 template bindings / 0 orphans / 100.0% aggregate coverage).

Status counts unchanged: 6 `:verified` / 100 `:tested` / 5 `:argued` / 0 `:open` (total 111).

---

## v0.63.0 DRAFT — 2026-05-25 — Pages site refresh

**1 NEW entry** OQ-127 (Gap-tier). Spec total 110 → 111. Engine 0.62.0 → 0.63.0. Pure documentation refinement; no engine code change.

User-flagged in v0.62 retrospective: *"A Pages demo would be nice. Existing one looks stale."* The mkdocs Pages site under `mkdocs.yml` + `docs/index.md` was last meaningfully updated at v0.7.0 — showed a 4-item nav and generic marketing index while the project had grown to v0.62 + 110 spec entries + 19 docs/guide pages + 4 compliance/maturity/catalog docs.

### What ships

- **`mkdocs.yml`** — nav rewrite from 4-item to 7-section (~25 entries):
  - Home
  - For evaluators (compliance-architecture · modules-catalog)
  - Getting started (quick-start · onboarding · configuration)
  - Role guides (Quality Manager · Engineer · Auditor)
  - Workflows (12 entries: doc-control · document-routing · capa-lifecycle · traceability · training · supplier-controls · management-review · complaints · signature-meaning · gpg-signing · release · verify-deployment)
  - Schemas + maturity (template-frontmatter · maturity-model)
  - Regulatory reference (overview · medical-devices)
- **`docs/index.md`** — rewritten landing page with:
  - 14-row scope table (verticals · shapes · class overlays · cross-cutting · sub-overlays · cross-overlays · modules · standards · jurisdictions · templates · bundles · spec entries · CLI subcommands · pytest count · deepest composite)
  - 14-row QMS-activity → GitHub-equivalent mapping
  - 4-audience quick-paths (new-to-project · new-hire · startup-stage-pick · fork-setup · audit)
  - 5-bullet honest disclaimers
- **Deployment** — auto via existing `.github/workflows/deploy-docs.yml`; push to main with `docs/**` or `mkdocs.yml` triggers redeploy.
- **Build verification** — `mkdocs build --strict` runs clean (zero broken links).

### Pattern observation

OQ-097 (public adopter-surface release, v0.23.0) rewrote `README.md` + introduced `docs/modules-catalog.md` but the Pages-site `mkdocs.yml` + `docs/index.md` weren't in scope. This release closes that loop. Going forward, the per-release version-counts in `index.md` should be updated alongside the per-release version bumps in `README.md` + `docs/modules-catalog.md` (add to release checklist).

### Forward-work status after v0.63.0

| Status | Count | Priorities |
|---|---|---|
| ✓ Closed | 13 | P1 + P3 + P4 + P5 + P6 + P7 + P8 + P9 + P10 + P11 + P12 + P13 + P14 |
| Open hard | 2 | P2 (validation package) + P15 (integration-architecture trace network) |
| Open medium | 0 | (empty) |
| Open light | 0 | (empty) |

Forward-work unchanged from v0.62.0 (OQ-127 is not in the P-series; it's a parallel doc-debt cleanup). The remaining queue is exactly the 2 hard items.

No engine code change. 251/251 pytest pass. Bundle baselines clean. Module lint clean. Template lint clean. Repo invariants hold (116 modules / 867 clauses / 379 template bindings / 0 orphans / 100.0% aggregate coverage).

Status counts: 6 `:verified` / 100 `:tested` / 5 `:argued` / 0 `:open` (total 111).

---

## v0.62.0 DRAFT — 2026-05-25 — Verify-deployment subcommand (P11)

**1 NEW entry** OQ-126 (Architecture-tier — third since v0.49.0; first since v0.60.0 OQ-124). Spec total 109 → 110. Engine 0.61.0 → 0.62.0.

Closes compliance-architecture forward-work P11 (medium effort per v0.54.0 distribution). **Last open medium priority — closes the medium queue entirely.**

### What ships

- **`engine/openqms/verify_deployment.py`** — pure-Python module (PyYAML only):
  - `Policy` loading + validation (`load_policy`)
  - `verify_branch_protection` (compares declared vs API response)
  - `verify_codeowners` (local-file check + path-coverage)
  - `verify_deployment` (orchestrator with injectable `gh_invoker`)
  - `format_result_text` (human-readable rendering)
  - `Finding` + `VerifyResult` dataclasses
- **`engine/openqms/cli.py`** — new `_cmd_verify_deployment()` + `p_verify_dep` argparser block; subcommand `openqms verify-deployment --policy <path> [--codeowners <path>] [--format text|json]`
- **`scripts/verify-deployment.sh`** — shell wrapper for adopters who prefer a script entry point
- **`deployment-policy.example.yaml`** — annotated reference policy at repo root
- **`docs/guide/verify-deployment.md`** — adopter usage + CI cron example + adopter checklist
- **`engine/tests/test_verify_deployment.py`** — 23 new pytest tests (count 228 → 251)

### What the verifier checks

| Category | Field | What it does |
|---|---|---|
| **Branch protection** | `required_approving_review_count` | declared count ≤ actual count |
| | `require_code_owner_reviews` | actual must be true if declared true |
| | `dismiss_stale_reviews` | actual must be true if declared true |
| | `enforce_admins` | actual must be enabled if declared true |
| | `required_linear_history` | actual must be enabled if declared true |
| **Signed commits** | `require_signed_commits` | actual must be enabled if declared true — the §11.100 unique-attribution anchor (OQ-023) |
| **Status checks** | `required_status_checks.strict` | actual must be true if declared true |
| | `required_status_checks.contexts` | every declared context appears in actual |
| **Negated flags** | `allow_force_pushes` | actual must NOT be enabled if declared false — preserves OQ-022 immutability |
| | `allow_deletions` | actual must NOT be enabled if declared false — preserves audit-trail recoverability |
| **CODEOWNERS** | file presence | exists at `.github/CODEOWNERS` / `CODEOWNERS` / `docs/CODEOWNERS` |
| | required_paths coverage | every declared path has a CODEOWNERS pattern |

### What it does NOT check (intentional gaps documented in guide)

- Org-level 2FA enforcement (needs org-admin API)
- Per-individual GPG key registration (covered by `IDENTITY-MAPPING-SOP-TEMPLATE.md` OQ-120 P12)
- Audit-log retention (varies by GitHub plan)
- External service integrations (out of QMS scope)
- Secret rotation cadence (out of substrate scope)

### Design choices

- **Zero new Python deps.** Uses `gh api` via subprocess. Reuses existing `gh` CLI authentication.
- **Injectable `gh_invoker` for testability.** Production injects `real_gh_invoker` (subprocess call); tests inject canned-response callables. No real API hits in CI.
- **Soft failure on API error.** A failed `gh api` call becomes a finding, not an unhandled exception. The adopter sees the failure as part of the verification output.
- **Policy is optional-per-field.** Missing fields mean "no check run." Declare only what your adopter policy actually requires.
- **Architecture-tier.** Changes the engine's surface (new module + new CLI subcommand + new shell wrapper). Third Architecture-tier entry since v0.49.0 OQ-115/116/117.

### Pattern observation

This release operationalizes the reviewer's deepest substantive concern (`docs/compliance-architecture.md` §"Adopter-deployment governance"): *"branch protection, GPG enforcement, role/identity mapping, backup posture — all live in the adopter's GitHub org configuration, not the Open QMS source tree. Open QMS can ship the tools that help adopters verify their own deployment is configured correctly."* The IDENTITY-MAPPING-SOP (OQ-120 P12) documents the HR-to-GitHub identity discipline; the BACKUP-RESTORE-SOP (OQ-120 P13) documents the backup-restore discipline; this verifier checks that the GitHub controls those SOPs depend on are actually in force.

### Forward-work status after v0.62.0

| Status | Count | Priorities |
|---|---|---|
| ✓ Closed | 13 | P1 + P3 + P4 + P5 + P6 + P7 + P8 + P9 + P10 + P11 + P12 + P13 + P14 |
| Open hard | 2 | P2 (validation package) + P15 (integration-architecture trace network) |
| Open medium | 0 | **medium queue empty** |

The medium queue is now closed entirely. The remaining open priorities are the two hard items — P2 (validation package; the highest-value remaining customer-facing deliverable per adopter feedback) and P15 (integration-architecture cross-record trace network; the strategic differentiator per reviewer #2).

No engine logic change (resolver / loader / validation unchanged). 251/251 pytest pass. Bundle baselines clean (8 example + 4 preset). Module lint clean. Template lint clean. Repo invariants hold (116 modules / 867 clauses / 379 template bindings / 0 orphans / 100.0% aggregate coverage). CLI subcommand count 9 → 10 (added `verify-deployment`).

Status counts: 6 `:verified` / 99 `:tested` / 5 `:argued` / 0 `:open` (total 110).

---

## v0.61.0 DRAFT — 2026-05-25 — Startup-stage presets (P4)

**1 NEW entry** OQ-125 (Gap-tier). Spec total 108 → 109. Engine 0.60.0 → 0.61.0.

Closes compliance-architecture forward-work P4 (medium effort per v0.54.0 distribution). Adopter-facing — 4 opinionated preset bundles + maturity-model guide; no engine code change required.

### What ships

**4 preset bundles at `presets/`** (industry-agnostic; strictly monotonic):

| Preset | Modules | Headline | Graduation trigger |
|---|---|---|---|
| `pre-seed.yaml` | 3 | `iso-31000` + `iso-27001` + `integrated-management-system` | first paying customer · vertical commitment · first non-founder hire |
| `seed.yaml` | 7 | + `privacy` + `iso-37001` + `iso-22301` + `manufacturing` placeholder | SOC 2 Type II asked · 15+ employees · first formal cert pursuit |
| `series-a.yaml` | 14 | + `soc-2` + `soc-2-type-ii` + `iso-27001-cloud` + `iso-27001-privacy` + `iso-14001` + `iso-45001` + `recall-workflow` | HITRUST asked · 50+ employees · non-home-jurisdiction market · NIST CSF tier-3+ goal |
| `series-b-plus.yaml` | 21 | + `hitrust-csf` + `hitrust-i1` + `nist-csf` + `nist-csf-tier-3` + `iso-37301` + `iso-37301-general-business` + `iso-50001` | beyond this stage, composition is too organization-specific — layer vertical + cross-overlays explicitly |

Each preset includes:
- YAML bundle definition
- `.matrix.json` resolved-matrix baseline (committed for regression detection)
- Per-stage README documenting what's IN + what's NOT + compliance-event graduation triggers + per-vertical layering examples

Plus:
- `presets/README.md` — family index with at-a-glance comparison table + composition examples
- `docs/guide/maturity-model.md` — 264-line cross-stage progression guide with 4 anti-patterns + opinionated-choices-flagged section + per-vertical layering reference

### Design choices (opinionated; documented in maturity-model guide)

- **Funding-round labels** (`pre-seed` / `seed` / `series-a` / `series-b-plus`) over compliance-event labels — funding rounds are recognizable to founders + operators + boards. But the actual trigger to graduate is a compliance event, named per-stage in the README.
- **Industry-agnostic** — no preset bakes in a vertical. `manufacturing` is the placeholder in seed+; adopters swap for `medical-devices` / `pharma` / `aerospace` / `automotive` / `food-safety` / `chemicals` based on their actual vertical.
- **Strictly monotonic** — each stage contains the prior stage's modules exactly. No reverse progressions.
- **Privacy at seed, not pre-seed** — privacy substrate is meaningful only when there's data flow to protect.
- **SOC 2 at series-a, not seed** — Type II is what customers want; observation period is meaningful only with stable operations.
- **HITRUST at series-b-plus, not series-a** — HITRUST is ongoing-attestation; needs a named compliance function.
- **No HIPAA in any preset** — adopter-layered; keeps presets industry-agnostic.

### Pattern parallel to `bundles/`

`bundles/` (8 example bundles) are vertical-specific (`example-samd` for medical devices, `example-aircraft` for aerospace, etc.) — *scope by product*. `presets/` are stage-specific — *scope by maturity*. The two are orthogonal lenses on the same module catalog; adopters use whichever framing fits their current decision.

### CI integration

`.github/workflows/engine-tests.yml` extended with a new step running `openqms regenerate --bundle presets/<name>.yaml` in dry-run mode for all 4 presets on every push touching engine/, modules/, registry/, templates/, bundles/, or presets/. Same regression-detection pattern as the existing `bundles/example-*` baselines.

### 15 new pytest tests

`engine/tests/test_presets.py`:

- `test_preset_loads_cleanly` × 4 — each bundle YAML parses
- `test_preset_module_count` × 4 — counts match expected (3/7/14/21)
- `test_preset_modules_exist_on_disk` × 4 — every referenced module exists
- `test_preset_monotonic_progression` — each stage strictly contains the prior
- `test_preset_matrix_files_present` — all 4 `.matrix.json` baselines committed
- `test_preset_readmes_present` — family README + 4 per-stage READMEs + maturity-model guide all present

### Forward-work status after v0.61.0

| Status | Count | Priorities |
|---|---|---|
| ✓ Closed | 12 | P1 + P3 + P4 + P5 + P6 + P7 + P8 + P9 + P10 + P12 + P13 + P14 |
| Open hard | 2 | P2 (validation package) + P15 (integration-architecture trace network) |
| Open medium | 1 | P11 (verify-deployment script) |

Down to 3 open. P11 is the last remaining medium; P2 + P15 are the multi-session hard items.

No engine code change. 228/228 pytest pass. Bundle baselines clean (8 example + 4 preset). Module lint clean. Template lint clean. Repo invariants hold (116 modules / 867 clauses / 379 template bindings / 0 orphans / 100.0% aggregate coverage).

Status counts: 6 `:verified` / 98 `:tested` / 5 `:argued` / 0 `:open` (total 109).

---

## v0.60.0 DRAFT — 2026-05-25 — Doc-control workflow hardening (P5)

**1 NEW entry** OQ-124 (Architecture-tier — second since v0.49.0 OQ-115/116/117; first since v0.58.0 OQ-122). Spec total 107 → 108. Engine 0.59.0 → 0.60.0.

Closes compliance-architecture forward-work P5 (medium effort per v0.54.0 distribution). Substantive behavioral change: version-drift becomes **hard-fail** (was warning-only). Adopters with currently-stale versions on controlled docs will see CI errors on next PR until they bump.

### What ships

- **`engine/openqms/doc_control.py`** — pure-Python module (depends on `openqms.template_schema` from OQ-122):
  - `ALLOWED_TRANSITIONS` dict encoding the 8-status state machine
  - `NON_VERSION_TRIGGERING_FIELDS` for housekeeping-exempt fields
  - `check_state_transition()`, `check_version_drift()`, `check_file()` core checks
  - `build_audit_artifact()`, `format_audit_markdown()` artifact emission
  - `FileCheck` + `AuditArtifact` dataclasses
- **`scripts/doc-control-check.py`** — CI-invokable script:
  - Reads changed-file list from `--changed-files` or stdin
  - Computes base vs head text via `git show`
  - Runs `check_file()` per file
  - Parses `Signature-Meaning:` trailers from PR commits via git log
  - Emits `::error` and `::warning` GitHub Actions annotations
  - Writes audit JSON + Markdown
  - Exits 1 on any error
- **`.github/workflows/doc-control.yml`** — rewritten:
  - Sets up Python 3.12 + uv 0.11.7 (parallel to engine-tests.yml)
  - Installs engine via `uv sync --frozen`
  - Invokes `scripts/doc-control-check.py`
  - Uploads `doc-control-audit.json` + `.md` as 90-day workflow artifact
  - Posts Markdown summary as PR comment via `gh pr comment`
  - `pull-requests: write` permission scoped to comment posting only

### Three hardenings

**(1) PyYAML schema-validated parsing — chemicals-arc lesson applied retroactively.** The legacy `.github/workflows/doc-control.yml` used `head -20 | grep ^field:` to scan for required frontmatter fields. This is the same shell-over-YAML antipattern that broke the chemicals-arc release at v0.36-v0.38 (unquoted colon in template `name:` value). The rewrite uses `openqms.template_schema.parse_frontmatter()` — true YAML parsing, no whitespace/colon assumptions.

**(2) Document state-transition machine.**

Document lifecycle:
```
draft ──→ review ──→ approved ──→ effective ──→ superseded (terminal)
  ↑         ↓             ↑            ↑
  └─────────┴─────────────┴────────────┘
   (rollback paths: review→draft, approved→draft, effective→draft)
   (superseded reachable from any non-terminal state)
```

Record lifecycle:
```
open ──→ closed (terminal)
  └──→ cancelled (terminal)
```

`ALLOWED_TRANSITIONS` enforces these. Status head-token is what's checked (parenthetical qualifiers like `'draft (pending NHTSA acceptance)'` are stripped).

**(3) Hard-fail version drift.**

Rule: substantive change without version increment → fail.

| Field changed | Triggers version-bump requirement? |
|---|---|
| `version` itself | n/a |
| `status` (alone) | no (handled by state machine) |
| `last_review_date`, `next_review` | no (housekeeping) |
| `owner`, `effective_date`, `title`, `addresses`, etc. | **yes** |
| Body text (non-frontmatter) | **yes** |

**Exemption:** draft documents may iterate freely without version bumps (drafting is intentionally iterative). Once status leaves `draft`, the hard-fail kicks in.

### Audit artifact

Per-PR JSON written to workflow artifact + Markdown rendered into a PR comment. Shape:

```json
{
  "pr_number": 42,
  "commit_sha": "abc...",
  "base_ref": "origin/main",
  "head_ref": "HEAD",
  "ci_status": "pass" | "fail" | "pending",
  "files": [
    {
      "path": "qms-policy/quality-manual.md",
      "passed": true,
      "base_version": "1.0",
      "head_version": "1.1",
      "base_status": "approved",
      "head_status": "approved",
      "changed_fields": ["owner", "version"],
      "errors": [],
      "warnings": []
    }
  ],
  "signature_trailers": [
    { "sha": "abc...", "meaning": "Approved", "role": "Quality Manager", "justification": "annual review" }
  ]
}
```

Posted as a PR comment via `gh pr comment` for auditor walkthrough; uploaded as 90-day workflow artifact for adopter long-term mirroring per `BACKUP-RESTORE-SOP-TEMPLATE.md` §2.

**Not yet:** GPG-signing of the audit artifact JSON itself. Today the artifact is unsigned (the `Signature-Meaning:` trailers it cites ARE signed via per-commit GPG, so the chain holds at the commit layer). Adopters with a CI signing key can extend the workflow to GPG-sign the JSON before upload.

### 38 new pytest tests

`engine/tests/test_doc_control.py`:

- `check_state_transition` — 14 tests covering self / new-file / removal / all 8 state transitions in/out / parenthetical-stripping / unrecognized-old-status
- `changed_fields` + `needs_version_bump` — 5 tests
- `check_version_drift` — 8 tests covering draft-exempt / substantive-fail / substantive-with-bump / housekeeping-only / body-change / version-downgrade / three-part-version / malformed-version
- `check_file` — 7 tests covering new-file / missing-frontmatter / invalid-transition / drift-fail / drift-pass / draft-iteration / changed-fields-record
- `build_audit_artifact` + `format_audit_markdown` — 4 tests covering empty / JSON serializable / Markdown empty section / Markdown with files+trailers

### Pattern observation

This release builds directly on OQ-122 (template schema, v0.58.0) — `doc_control.py` imports `parse_frontmatter` + `RECOGNIZED_STATUSES` from the schema module. The two together implement two layers of the same discipline:
- OQ-122: static-shape — does the file have the right fields with the right types?
- OQ-124: temporal-shape — given the field values, is the change a valid step in the lifecycle?

### Forward-work status after v0.60.0

| Status | Count | Priorities |
|---|---|---|
| ✓ Closed | 11 | P1 + P3 + P5 + P6 + P7 + P8 + P9 + P10 + P12 + P13 + P14 |
| Open hard | 2 | P2 (validation package) + P15 (integration-architecture trace network) |
| Open medium | 2 | P4 (startup-stage presets) + P11 (verify-deployment script) |

Medium queue down to 2. Of the remaining medium items, P11 has natural overlap with this release (the audit-artifact emission pattern + workflow-permission scoping) and P4 is the most-customer-facing item left.

No functional change to engine code (loader / compose / validation / resolver / CLI unchanged). 213/213 pytest pass. Bundle baselines clean. Module lint clean. Template lint clean. Repo invariants hold (116 modules / 867 clauses / 379 template bindings / 0 orphans / 100.0% aggregate coverage).

Status counts: 6 `:verified` / 97 `:tested` / 5 `:argued` / 0 `:open` (total 108).

---

## v0.59.0 DRAFT — 2026-05-25 — Negative-path test suite for bad modules (P10)

**1 NEW entry** OQ-123 (Gap-tier). Spec total 106 → 107. Engine 0.58.0 → 0.59.0.

Closes compliance-architecture forward-work P10 (medium effort per v0.54.0 distribution). Pure test addition — no engine code changes; no template changes; no documentation requiring updates beyond this changelog + spec.

### What ships

`engine/tests/test_negative_modules.py` — 23 broken-by-construction fixtures + assertions on the specific error type + message produced by each. Pytest count 152 → 175.

### Coverage by category

| Category | Tests | Targets |
|---|---|---|
| Loader: module-level errors | 5 | missing `name` · `clauses` not a list · `templates` not a list · `standards` not a list · module file not found |
| Loader: per-clause errors | 4 | missing `id` · missing `standard` · missing `section` · missing `summary` |
| Loader: per-template errors | 3 | missing `path` · missing `name` · `addresses` not a list |
| Compose errors | 2 | empty input · conflicting clause across modules |
| Validation harness orphan detection | 2 | orphan clause (no template binds it) · orphan template (addresses unknown clause) |
| Linter findings | 6 | YAML parse error · top-level not a mapping · duplicate clause id · addresses references unknown clause · clause missing required field · template missing required field |
| Composite | 1 | both orphan kinds simultaneously in same module |

### Design choices

- **Inline-string fixtures over on-disk:** the broken construction sits next to its assertion. Easier to read; no fixture-discovery overhead.
- **`tmp_path` per test:** each fixture is written to a fresh temp directory; no test-pollution risk.
- **Linter imported via `importlib.util.spec_from_file_location`:** the hyphenated filename (`scripts/lint-module-yaml.py`) can't be imported directly because `lint-module-yaml` is not a valid Python identifier.
- **Assertion on message substrings, not full strings:** the tests check the substring uniquely identifying each error path, allowing the engine to refine error messages without breaking tests for cosmetic word changes.

### Pattern observation

This release parallels OQ-122 (template schema tests, v0.58.0) — both shore up the engine's error-rejection surface with explicit assertions. Coincidentally both ship 23 tests (152 → 175 here; 129 → 152 there). The pattern: when an engine surface is established as production-bearing (clause-template trace, template schema), the next release after is the negative-path coverage that catches regressions in the rejection paths.

### What this enables

Any future refactor that subtly weakens an error path now fails one or more of these tests:
- Loosening a required-field check
- Catching an exception that should propagate
- Dropping a finding from the linter
- Allowing duplicate clause IDs to slip through

Message-quality drift is also visible — tests assert on specific substrings, so if an error message becomes less informative, the test fails and prompts a deliberate decision.

### Forward-work status after v0.59.0

| Status | Count | Priorities |
|---|---|---|
| ✓ Closed | 10 | P1 + P3 + P6 + P7 + P8 + P9 + P10 + P12 + P13 + P14 |
| Open hard | 2 | P2 (validation package) + P15 (integration-architecture trace network) |
| Open medium | 3 | P4 (startup-stage presets) + P5 (doc-control hardening) + P11 (verify-deployment script) |

Medium queue is down to 3. The remaining priorities are either bounded-medium (P4/P5/P11 — each a clean single-release deliverable) or genuinely hard (P2/P15 — each multi-session).

No functional code changes. 175/175 pytest pass. Bundle baselines clean. Module lint clean. Template lint clean. Repo invariants hold (116 modules / 867 clauses / 379 template bindings / 0 orphans / 100.0% aggregate coverage).

Status counts: 6 `:verified` / 96 `:tested` / 5 `:argued` / 0 `:open` (total 107).

---

## v0.58.0 DRAFT — 2026-05-25 — Template frontmatter schema validation (P9)

**1 NEW entry** OQ-122 (Architecture-tier — first since OQ-115/OQ-116/OQ-117 at v0.49.0). Spec total 105 → 106. Engine 0.57.0 → 0.58.0.

Closes compliance-architecture forward-work P9 (medium effort per v0.54.0 distribution). Engine surface change — new schema module + new linter script + new CI gate.

### What ships

- **`engine/openqms/template_schema.py`** — pure-Python (PyYAML only) schema module with `parse_frontmatter()`, `validate_frontmatter()`, `lint_template()`, `lint_templates()`, `discover_templates()` + `Finding` and `LintResult` dataclasses
- **`scripts/lint-template-frontmatter.py`** — CI-gate executable parallel to `scripts/lint-module-yaml.py` (from OQ-040 at v0.40.0)
- **`engine/tests/test_template_schema.py`** — 23 new pytest tests (parse / validate per-field / lint per-file / lint aggregate / **repo-wide invariant** asserting all shipped templates pass schema)
- **`.github/workflows/engine-tests.yml`** — extended with "Lint template frontmatter (P9 gate)" step before pytest
- **`docs/guide/template-frontmatter.md`** — companion guide documenting schema + prefix conventions per template group + minimal-new-template recipe

### The schema

**Required fields:**

| Field | Pattern | Notes |
|---|---|---|
| `document_id` | `^[A-Za-z0-9][A-Za-z0-9_\-\[\]]*$` | Allows leading digit (`510K-XXX`) + bracket placeholders (`DI-[PRODUCT]-001`) |
| `version` | `^\d+\.\d+(\.\d+)?$` | Two-part or three-part semver-ish |
| `owner` | non-empty string | Role or named individual |
| `status` | one of 8 recognized | See state lists below |
| **one of:** `effective_date` / `issued_date` / `issue_date` / `opened_date` / `assessment_date` / `notification_date` / `approval_date` | `YYYY-MM-DD` or literal placeholder | 7 acceptable aliases per document-vs-record kind |

**8 recognized status values** across two lifecycle families:

- **Document lifecycle:** `draft → review → approved → effective → superseded`
- **Record lifecycle:** `open → closed` (or `open → cancelled`)

**Permissive on extras** — domain-specific fields (`recall_campaign_number`, `worker_consultation`, `mock_recall_cadence`, `qa_approval`, `archive_location`, `phi_classification`, etc.) pass without modification.

### Migration: 24 templates batched in this release

The schema run on initial commit revealed 37 errors across 27 files. After schema relaxation (broader date-field aliases + open/closed/cancelled status + bracket-permissive document_id + leading-digit-permissive document_id), 27 errors remained. 24 templates without frontmatter were migrated in this same release using a one-shot script (per-template document_id prefix + owner-role hint):

| Group | Count | Templates |
|---|---|---|
| qms-hipaa | 8 | BAA, HIPAA-AUTHORIZATION, REPRODUCTIVE-HEALTH-ATTESTATION, ACCOUNTING-OF-DISCLOSURES-LOG, OCR-INVESTIGATION-RESPONSE, HIPAA-RISK-ANALYSIS, NPP, RESTRICTION-REQUEST-LOG, HIPAA-BREACH-RISK-ASSESSMENT |
| qms-privacy | 7 | DPA, ROPA, DPIA, PRIVACY-POLICY, US-STATE-PRIVACY-MATRIX, DATA-PROTECTION-ASSESSMENT, PERSONAL-DATA-BREACH-NOTIFICATION |
| qms-logistics | 2 | SHIPPING-PAPER, HMT-TRAINING-RECORD |
| qms-ohs | 1 | HAZCOM-WRITTEN-PROGRAM |
| product-chemicals | 5 | BPR-AUTHORISATION-APPLICATION, PFAS-REPORTING-FORM, SVHC-COMMUNICATION-LETTER, REACH-AUTHORISATION-APPLICATION, SUBSTITUTION-PLAN |
| product-chemicals/glp | 1 | GLP-STUDY-PLAN-REPORT (had frontmatter but missing required fields owner/status/date) |

Each migrated template gets minimal stub:

```yaml
---
document_id: <PREFIX>-XXX
version: "1.0"
effective_date: YYYY-MM-DD
owner: "[Role / Team]"
status: draft
---
```

End state: **105/105 templates pass schema** at v0.58.0.

### Pytest count: 129 → 152

23 new tests in `test_template_schema.py`:

- `parse_frontmatter`: present / absent / unclosed / YAML-error cases
- `validate_frontmatter`: clean / missing-required / missing-date / alternate-date-field / placeholder-date / bad-version / two-and-three-part-version / bad-document_id / leading-digit-OK / bracket-placeholder-OK / recognized-status / unrecognized-status warns / parenthetical-qualifier-OK / extras-permitted
- `lint_template` + `lint_templates`: per-file and aggregate behavior + hard-fail vs soft-warn
- **Repo-wide invariant:** all shipped templates pass schema (this is the fail-fast for any future template that lands without frontmatter or with bad frontmatter)

### Forward-work status after v0.58.0

| Status | Count | Priorities |
|---|---|---|
| ✓ Closed | 9 | P1 + P3 + P6 + P7 + P8 + P9 + P12 + P13 + P14 |
| Open hard | 2 | P2 (validation package) + P15 (integration-architecture trace network) |
| Open medium | 4 | P4 + P5 + P10 + P11 |

The medium queue is shrinking — only 4 medium items remain. P10 (negative-path test suite) is the natural complement to this release (now that there's a schema, negative-path tests are easier to construct).

### Lessons + design choices

- **Schema relaxation iterations.** Initial schema rejected 14 legitimate templates beyond the 23 missing-frontmatter ones. Each rejection drove a real schema design decision: 7 date-field aliases reflect document-vs-record distinction; bracket-permissive document_id supports adopter fill-in templates; leading-digit-OK supports regulator-defined IDs (510K-XXX); open/closed/cancelled status family supports operational-record templates.
- **Permissive-on-extras is non-negotiable.** Templates ship with very heterogeneous frontmatter. The schema validates the spine (5 required fields + 1 date) and ignores everything else. This is the only way the schema doesn't become a maintenance burden as new domain-specific fields appear.
- **Hard-fail from day 1.** The migration was small enough (24 templates) to do same-release. No need for soft-warn-then-upgrade phase. End state is cleaner.
- **Architecture tier.** OQ-122 changes the engine's surface (new module + new gate), so it's Architecture-tier rather than Gap-tier (which is where the previous P-batch releases like OQ-120 and OQ-121 landed).

No engine logic changes (no `cli.py` touched; no resolver/validator changes). 152/152 pytest pass. Bundle baselines clean. Module lint clean. Template lint clean (P9 gate active). Repo invariants hold (116 modules / 867 clauses / 379 template bindings / 0 orphans / 100.0% aggregate coverage).

Status counts: 6 `:verified` / 95 `:tested` / 5 `:argued` / 0 `:open` (total 106).

---

## v0.57.0 DRAFT — 2026-05-25 — Non-technical UX batch (P3)

**1 NEW entry** OQ-121 (Gap-tier; batched). Spec total 104 → 105. Engine 0.56.0 → 0.57.0.

Closes compliance-architecture forward-work P3 (medium effort per v0.54.0 distribution). Adopter-facing surface — issue templates + guides — no engine code changes.

### 5 new GitHub Issue Forms

| Template | Purpose | Aligns with |
|---|---|---|
| `training-completion.yml` | Record completion of training event | ISO 13485 §6.2.2 + 21 CFR §820.25(b) + `docs/guide/training.md` |
| `document-review.yml` | Periodic doc review with 3-outcome flow (no-change / minor / major revision) | ISO 13485 §4.2.4 + 21 CFR §820.40(b) + Annex 11 §4.5 |
| `access-review.yml` | Quarterly access review | `templates/qms-policy/IDENTITY-MAPPING-SOP-TEMPLATE.md` §4 (shipped v0.55.0) |
| `restoration-test.yml` | Annual restoration test with 13-step runbook outcomes | `templates/qms-bcms/BACKUP-RESTORE-SOP-TEMPLATE.md` §4 (shipped v0.55.0) |
| `regulatory-review.yml` | Per-module independent regulatory review | `BUSINESS/regulatory_review_cadence.md` §2-3 (shipped v0.55.0) |

These align 1:1 with the SOPs shipped at OQ-120 — completing the SOP-template → operating-record-form lifecycle. Total GitHub issue templates: 7 → 12.

### 5 new role + process guides

| Guide | Audience | Notable content |
|---|---|---|
| `docs/guide/onboarding.md` | New hires + new contractors | First-30-days checklist (day-1 / day-2-7 / week-2 / week-3-4 / month-1) with completion criteria |
| `docs/guide/role-quality-manager.md` | Quality Manager / Quality Lead | Daily / weekly / monthly / quarterly / annual cadence with linked workflows + anti-patterns |
| `docs/guide/role-engineer.md` | Software / hardware / design engineers | Commit signing + when-to-use-which-trailer table + per-change-type workflow + anti-pattern list |
| `docs/guide/document-routing.md` | Anyone raising or reviewing PRs | Traditional-eQMS → GitHub-native mapping + example CODEOWNERS structure + branch-protection rules + edge cases |
| `docs/guide/capa-lifecycle.md` | Anyone touching CAPAs | 7-state state machine: OPEN → INVESTIGATION → ROOT-CAUSE → ACTION PLANNED → ACTION EXECUTED → EFFECTIVENESS CHECK → CLOSED + anti-patterns + aggregation at Management Review |

Total `docs/guide/` files: 12 → 17.

### Pattern observations

- **SOP ↔ operating-record-form pairing.** OQ-120 shipped 3 new SOP templates (identity-mapping + backup-restore + regulatory-review). OQ-121 ships the 3 corresponding issue forms that operate them (access-review + restoration-test + regulatory-review) plus 2 more (training-completion + document-review) covering cadences that pre-existed but lacked structured forms.
- **Role-specific guides reduce the "I don't know which form to use" friction.** Each role guide now points to the exact issue form for each common scenario.
- **Document-routing guide makes CODEOWNERS load-bearing.** Before this release the CODEOWNERS file existed but the WHY was scattered; the new guide consolidates the regulatory framing.
- **CAPA-lifecycle guide formalises a state machine that existed only implicitly.** The 7 states were always there in the workflow; documenting them explicitly enables non-technical users to navigate the lifecycle without coaching.

### Forward-work status after v0.57.0

| Status | Count | Priorities |
|---|---|---|
| ✓ Closed | 8 | P1 + P3 + P6 + P7 + P8 + P12 + P13 + P14 |
| Open hard | 2 | P2 (validation package) + P15 (integration-architecture trace network) |
| Open medium | 5 | P4 + P5 + P9 + P10 + P11 |

Remaining queue: 2 hard + 5 medium (was 2 + 6).

No functional code changes (issue templates + guides only; no engine code touched). 129/129 pytest pass. Bundle baselines clean. Lint clean. Repo invariants hold (116 modules / 867 clauses / 379 template bindings / 0 orphans / 100.0% aggregate coverage).

Status counts: 6 `:verified` / 94 `:tested` / 5 `:argued` / 0 `:open` (total 105).

---

## v0.56.0 DRAFT — 2026-05-25 — P15 added (integration-architecture trace network)

**0 NEW entries.** Spec total unchanged at 104. Engine 0.55.0 → 0.56.0. Doc-only refinement of OQ-119.

Independent reviewer comment received 2026-05-25:

> Risk management should not be a separate artifact. The future is integrated: requirements ↔ hazards ↔ mitigations ↔ testing ↔ CAPA ↔ complaints ↔ post-market surveillance. That connectedness is where modern systems win.

**Assessment of redundancy + effort:**

- **Redundancy: low.** The existing clause-level trace (OQ-001 invariant + OQ-067 `openqms trace`) operates on module-YAML `clause ↔ template` bindings, NOT on living-record cross-references. Partial precedent in the RMF template (`templates/product-dhf/risk-management/`) which gives an ISO 14971 unified-view artifact, and informal free-text `capa_link` fields in `complaint.yml` + `nonconformance.yml`, but nothing enforces or validates a cross-record graph today.
- **Effort: hard.** Comparable in scope to P2 (validation package). Multi-session. Requires frontmatter schema for trace-link IDs + structured-ID conversion of free-text link fields + new engine subcommand walking the cross-record graph + instance-level zero-orphan invariant + per-template frontmatter migration + CI gate + docs.

**P15 added** to `docs/compliance-architecture.md` forward-work as a new third reviewer-flagged cluster: **Integration-architecture priorities**. Sits next to the existing P2 (hard) in queue.

**Forward-work distribution updated:**

| Status | Count | Priorities |
|---|---|---|
| ✓ Closed | 7 | P1 + P6 + P7 + P8 + P12 + P13 + P14 |
| Open hard | 2 | P2 (validation package) + P15 (integration-architecture trace network) |
| Open medium | 6 | P3 + P4 + P5 + P9 + P10 + P11 |

No functional code changes. 129/129 pytest pass. Bundle baselines clean. Lint clean. Repo invariants hold (116 modules / 867 clauses / 379 template bindings / 0 orphans / 100.0% aggregate coverage).

Status counts unchanged: 6 `:verified` / 93 `:tested` / 5 `:argued` / 0 `:open` (total 104).

Maybe we'll get to it someday.

---

## v0.55.0 DRAFT — 2026-05-25 — Light-batch hardening release (P6 + P7 + P8 + P12 + P13 + P14)

**1 NEW entry** OQ-120 (Gap-tier; batched per OQ-104 / OQ-109 / OQ-118 precedent). Spec total 103 → 104. Engine 0.54.0 → 0.55.0.

Single hardening release closing the 6 light-effort forward-work priorities identified at v0.54.0. Per the effort-distribution observation that all 6 could batch as one release.

### P6 — Pinned + hashed deps via `uv.lock`

- `engine/uv.lock` generated by `uv lock` (10 packages, hashed: colorama + hypothesis + iniconfig + packaging + pluggy + pygments + pytest + pyyaml + sortedcontainers + tomli)
- `.github/workflows/engine-tests.yml` migrated from `pip install -e './engine[dev]'` to `uv sync --frozen --all-extras` + `uv pip install -e '.[dev]'`
- Lockfile-presence is a hard CI gate: missing `engine/uv.lock` exits 1 with reference to forward-work P6
- Reproducible installs; no floor-version drift

### P7 — Signed release tags

- `docs/guide/release.md` rewritten to mandate `git tag -s` for project upstream releases
- Adopter-side verification instructions (gpg keyserver + `git tag -v <tag>`)
- Verification embedded as P8 workflow step

### P8 — CI log archival per release

- New `.github/workflows/release-artifact.yml` triggered on `v*` / `release-*` tag push
- Captures: `openqms trace --all` + `openqms coverage --all` + `openqms signatures export` + pytest log + lint output + module-count snapshot + `git tag -v` output
- Bundled to ZIP + uploaded as release artifact (90-day GitHub retention default)
- Attached to GitHub Release on `v*` tags via `softprops/action-gh-release`
- Multi-year retention pattern (org-controlled S3 mirror) documented for adopters

### P12 — HR-to-GitHub identity-mapping SOP template

- New `templates/qms-policy/IDENTITY-MAPPING-SOP-TEMPLATE.md` (9 sections)
- Covers: register schema (12 fields) + new-hire provisioning + quarterly access review + planned + emergency key rotation + offboarding + audit-log retention + linkage table
- Bound to 21 CFR §11.100 + HIPAA §164.308(a)(3) + ISO 27001 A.9 + GDPR Article 32 via frontmatter `addresses`

### P13 — Backup/restore SOP + restoration-test discipline

- New `templates/qms-bcms/BACKUP-RESTORE-SOP-TEMPLATE.md` (8 sections)
- 3-2-1 backup posture concretization (Primary GitHub + Mirror 1 daily + Mirror 2 weekly cold + Mirror 3 monthly off-site)
- Cron automation snippets for `git clone --mirror` + `git bundle create` + GPG-encrypt + S3 upload
- RTO/RPO/MAO/MBCO declaration framework with suggested targets + adopter-fill fields
- 13-step annual restoration-test runbook (declared as regulatory minimum)
- Format-stability planning (parallel to ATMP 30-year clauses; recommended annual + 5-year + 10-year migration cadence for long-retention records)
- Backup-failure escalation matrix
- Bound to ISO 22301 §8.2 + HIPAA §164.308(a)(7) + 21 CFR §11.10 + EU GMP Annex 11 §7.1 via frontmatter `addresses`

### P14 — Regulatory-review cadence (module crosswalk semantics)

- New `BUSINESS/regulatory_review_cadence.md` (8 sections)
- Cadence schedule per standard kind (annual for active major; on-revision for revisions; quarterly for pre-effective drafts; biannual for sunsetting)
- 6-criterion reviewer-qualification standard
- Finding-log format with 3-tier severity (minor / major / critical) + per-tier response requirements
- Per-module attestation badge format for README headers
- **Honest review-debt baseline: 0 / 116 modules reviewed** by an independent qualified reviewer per §2 — this is the true starting state, declared transparently
- 8-module first-tier review-target list (highest-adoption-likelihood: medical-devices · pharma · iso-27001 · hipaa · privacy · regulated-ai · aerospace · automotive)
- Operationalizes the OQ-080 "coverage is not compliance" firewall as a tracked process

### Forward-work status after v0.55.0

| Status | Count | Priorities |
|---|---|---|
| ✓ Closed | 7 | P1 + P6 + P7 + P8 + P12 + P13 + P14 |
| Open | 7 | P2 (hard) · P3 + P4 + P5 + P9 + P10 + P11 (medium) |

The remaining queue is 1 hard + 6 medium — each medium item realistically warrants its own release; the hard one is the multi-session P2 validation package.

129/129 pytest pass. Bundle baselines clean. Lint clean. Repo invariants hold (116 modules / 867 clauses / 379 template bindings / 0 orphans / 100.0% aggregate coverage). The 2 new SOP templates ship as standalone (per OQ-099 standalone-template precedent); template-binding pass to bind them to relevant modules (hipaa + iso-22301 + iso-27001) is forward work.

Status counts: 6 `:verified` / 93 `:tested` / 5 `:argued` / 0 `:open` (total 104).

---

## v0.54.0 DRAFT — 2026-05-25 — Forward-work effort qualifiers

**0 NEW entries.** Spec total unchanged at 103. Engine 0.53.0 → 0.54.0. Pure documentation refinement of the OQ-119 deliverable.

Added per-priority `light/medium/hard` effort calibration to all three forward-work tables in `docs/compliance-architecture.md`. Helps adopters + maintainers understand sequencing options at a glance.

**Calibration scale:**

- **light** — single file or small set; mostly documentation or contained script; ≤ ½ day focused work
- **medium** — multiple deliverables: new templates + workflow changes + tests + composites; ½ to 2 days; bounded scope
- **hard** — substantial new feature surface: new module + multiple templates + standards crosswalks + tests + composites + docs + per-jurisdiction handling; 2+ days; multi-session

**Current distribution across the 13 open priorities:**

| Effort | Count | Priorities |
|---|---|---|
| **hard** | 1 | P2 (validation package — largest single deliverable in queue) |
| **medium** | 6 | P3 (non-technical UX) · P4 (startup-stage presets) · P5 (doc-control hardening) · P9 (template schema validation) · P10 (negative-path test suite) · P11 (verify-deployment script) |
| **light** | 6 | P6 (lockfile) · P7 (signed release tags) · P8 (CI log archival) · P12 (identity-mapping SOP) · P13 (backup-restore SOP) · P14 (regulatory-review cadence doc) |

The 6 light items could realistically be batched as a single hardening release; the 6 medium items each warrant their own release; P2 is the single multi-session deliverable.

No functional code changes. 129/129 pytest pass. Bundle baselines clean. Lint clean. Repo invariants hold (116 modules / 867 clauses / 379 templates / 0 orphans / 100.0% aggregate coverage).

Status counts unchanged: 6 `:verified` / 92 `:tested` / 5 `:argued` / 0 `:open` (total 103).

---

## v0.53.0 DRAFT — 2026-05-25 — Reviewer-feedback integration (forward-work expansion)

**0 NEW entries.** Spec total unchanged at 103. Engine 0.52.0 → 0.53.0. Pure documentation refinement of the OQ-119 deliverable.

Independent reviewer assessment received 2026-05-25 (reviewer evaluated a slightly older state — v0.38–v0.39 era — so several of their concerns are already addressed; remaining concerns expand the forward-work catalog).

**Reviewer's headline framing**: *"worth pursuing, but treat it as a generator for QMS infrastructure, not as 'the QMS'"* — matches the project's own honesty bound (OQ-080).

**Updated `docs/compliance-architecture.md` forward-work section** with three additions:

### 10 new priorities

**Engine-hardening cluster** (treating the engine itself as production-grade compliance tooling):

| Priority | Gap |
|---|---|
| P5 | `.github/workflows/doc-control.yml` parses YAML frontmatter via `head -20 \| grep`; version non-increment is warning not failure. Replace with PyYAML parser; hard-fail version drift; enforce document state-transition rules; signed audit artifact per PR |
| P6 | Dependency pins are floor-versions only (no lockfile). Adopt `uv` with `uv.lock` (hashed) |
| P7 | Release tags not signed. Add `git tag -s` discipline + CI verification step |
| P8 | CI logs are GitHub-default-retention. Add release-artifact ZIP snapshot of full CI run + invariant-check outputs |
| P9 | Template files have no schema validation today (only module.yaml does, via lint-module-yaml.py). Add JSON Schema / Pydantic for template frontmatter |
| P10 | No explicit negative-path test suite for bad modules. Add `engine/tests/test_negative_modules.py` with ~20 broken-by-construction fixtures + specific-error assertions |

**Adopter-deployment governance cluster** (the reviewer's deepest substantive point: "immutability and approval model are deployment controls, not intrinsic properties of the repo"):

| Priority | Gap |
|---|---|
| P11 | No automated verification that an adopter fork has required branch-protection + GPG-signing + required-reviewers + required-status-checks. Add `scripts/verify-deployment.sh` or `openqms verify-deployment` subcommand querying GitHub API + comparing against `deployment-policy.yaml` |
| P12 | No SOP template for HR-to-GitHub identity mapping (§11.100 unique-attribution depends on it). Add `templates/qms-policy/IDENTITY-MAPPING-SOP-TEMPLATE.md` |
| P13 | No backup/restore SOP template + restoration-test discipline. Add `templates/qms-bcms/BACKUP-RESTORE-SOP-TEMPLATE.md` with `git clone --mirror` cron pattern + RTO/RPO declaration + annual restoration-test runbook + format-stability planning |
| P14 | Process gap — no documented cadence for third-party regulatory review of module crosswalk semantics. Add `BUSINESS/regulatory_review_cadence.md` |

### Transparency table — what the reviewer flagged that is already addressed

| Reviewer concern | Status today |
|---|---|
| README version drift (v0.38.0 stale) | Fixed at v0.51.0 polishing pass; A5 stale-counts is a per-release gate |
| Immutable audit export | Shipped v0.7.0 (OQ-060) — `openqms signatures export` |
| Schema validation for module YAML | Shipped v0.40.0 — `scripts/lint-module-yaml.py` is a pre-pytest CI gate |
| Bidirectional traceability invariant | `:verified` at OQ-001 via hypothesis property tests |
| Standards-licensing posture | OQ-070 + OQ-071 `:argued` with documented disclosure in README |

### Permanent-not-gap callout

The reviewer's foundational point — *"coverage is not compliance"* — is permanent and architectural, not a gap to close. This is the OQ-080 firewall. Open QMS produces traceable scaffolds; semantic adequacy requires QA judgment and (where regulator requires) third-party assessment. P11 + P14 in particular make the substrate harder to lose / fake / drift — they do NOT claim Open QMS will replace regulatory expertise.

No functional code changes. 129/129 pytest pass. Bundle baselines clean. Lint clean. Repo invariants hold (116 modules / 867 clauses / 379 templates / 0 orphans / 100.0% aggregate coverage).

Status counts unchanged: 6 `:verified` / 92 `:tested` / 5 `:argued` / 0 `:open` (total 103).

---

## v0.52.0 DRAFT — 2026-05-25 — Compliance architecture trust-gate document (adopter-feedback P1)

**1 NEW entry** OQ-119 (Gap-tier). Spec total 102 → 103. Engine 0.51.0 → 0.52.0.

First response to adopter feedback received same day. Feedback highlighted four priorities; this release closes P1 (the trust-gate prerequisite). P2, P3, P4 acknowledged + scoped for future releases.

**OQ-119 — Compliance architecture trust-gate document**

Shipped `docs/compliance-architecture.md` — 11-section comprehensive trust-gate document for quality leaders + regulatory affairs + IT/SecOps evaluating Open QMS for adoption.

The 10 highest-frequency adopter-evaluator topics covered:

1. **21 CFR Part 11** — Electronic records & signatures (US FDA)
2. **EU GMP Annex 11** — Computerised systems
3. **ISO 13485:2016** — Medical devices QMS
4. **Audit trails** — git as the immutable audit trail
5. **E-signatures** — GPG + signature-meaning trailers (§11.50 binding)
6. **Permissions / access controls** — GitHub org permissions + branch protection + CODEOWNERS
7. **Validation** — engine validation + module validation + forward-work acknowledgment
8. **Backup / recovery** — git distributed model + GitHub durability + adopter export
9. **Record retention** — per-module clause-level retention requirements
10. **Cybersecurity** — full cross-cutting + sub-overlay + cross-overlay catalog
11. **System administration controls** — GitHub org admin + audit log + change management

For each topic the document maps:
- Regulatory requirement → architecture component → spec entry → evidence file → adopter responsibility

Plus:
- **"How to use this document at audit"** 6-step workflow for at-audit demonstration
- **"What Open QMS is NOT"** honest disclaimers reinforcing OQ-080
- **Forward-work** section acknowledging adopter-feedback priorities P2 + P3 + P4

The document is intentionally pointer-heavy — it indexes existing spec entries + modules + templates + 12 docs/guide pages rather than re-claiming evidence. The trust-gate framing is that quality leaders need a single document that maps "what auditor asks → what evidence we point to" rather than scattered repository spelunking.

**Adopter feedback received 2026-05-25 (full four-priority list):**

| Priority | Status | Future plan |
|---|---|---|
| **P1 — Compliance architecture documentation** | ✓ closed at v0.52.0 | n/a |
| P2 — Validation package templates (URS + IQ/OQ/PQ + Change Assessment + CSV) | acknowledged | future release — `validation-package` cross-cutting overlay |
| P3 — Better non-technical UX (CAPA + training + approvals + document routing + onboarding) | acknowledged with architecture-boundary note | future release — additional issue templates + role-specific quickstart guides; Open QMS is GitHub-native, not a web app |
| P4 — Opinionated best-practice workflows (startup-stage presets + phased maturity models + compliant defaults) | acknowledged | future release — `presets/` family extending `bundles/` |

No functional code changes. README pointer added to compliance-architecture.md. 129/129 pytest pass. Bundle baselines clean. Lint clean. Repo invariants hold (116 modules / 867 clauses / 379 templates / 0 orphans / 100.0% aggregate coverage).

Status counts: 6 `:verified` / 92 `:tested` / 5 `:argued` / 0 `:open` (total 103).

---

## v0.51.0 DRAFT — 2026-05-25 — Polishing pass

**0 NEW entries.** Spec total unchanged at 102. Engine 0.50.0 → 0.51.0.

Pure bookkeeping release closing the v0.46-v0.50 build arc:

- **A0-A6 cross-audit clean** (zero findings; see `BUSINESS/audit_2026-05-25_v0_50.md`)
- **Omnibus companion** for the 4-release arc (`BUSINESS/companion_v0_48_to_51.md`) covering us-state-privacy + 3 engine adopter-features + final cross-overlay batch + this polishing pass
- **companion_index.md** updated with the new omnibus row
- **dashboard.md "Latest" note** refreshed to v0.51.0 polishing-pass
- **README.md + docs/modules-catalog.md** version-refs bumped 0.50.0 → 0.51.0

No functional code changes. All 129/129 pytest pass. Bundle baselines clean. Lint clean. Repo invariants hold (116 modules / 867 clauses / 379 templates / 0 orphans / 100.0% aggregate coverage).

Status counts unchanged: 6 `:verified` / 91 `:tested` / 5 `:argued` / 0 `:open` (total 102).

---

## v0.50.0 DRAFT — 2026-05-25 — Final cross-overlay batch (4)

**1 NEW entry** OQ-118. Spec total 101 → 102. Engine 0.49.0 → 0.50.0.

Completes the cross-overlay shape coverage across the remaining major vertical intersections (introduced v0.44.0 OQ-111; extended v0.47.0 OQ-113). The cross-overlay tour now spans medical-device intersections (combination-product + connected-medical-device + digital-health-multi-region) + pharma intersections (combination-product + cell-therapy-supply-chain + clinical-trial-multi-region) + food intersections (food-pharma-grade + food-allergen-recall) + automotive intersections (automotive-supply-chain) + financial intersections (banking-resilience) + utility intersections (utility-cybersecurity) + defense intersections (defense-aerospace-cyber) + IMS (integrated-management-system).

**The 4 cross-overlays**

- **automotive-supply-chain** — automotive + automotive-asil-d + automotive-cal-4 + recall-workflow. 7 clauses across Development Interface Agreement (DIA, ISO 26262-8 §5) + Cybersecurity Interface Agreement (CIA, ISO/SAE 21434-7) + AIAG PPAP 4th-Edition 18-element + 5-level submission framework + ISO/SAE 21434 §15 supplier management + UN R155 Type-Approval CSMS + R156 SUMS + production-suspension + NHTSA Part 573 5-working-day recall coordination + IATF 16949 §8.4 tier-N flow-down + software-supplier special considerations (OTA + AD + ADAS + RTOS).

- **clinical-trial-multi-region** — pharma + privacy + hipaa + digital-health-multi-region. 7 clauses across ICH E6(R3) GCP (Step 4 2024-01-19) + EU CTR 536/2014 + CTIS portal + 21 CFR 312 IND + §312.32 Safety Reports (15-day + 7-day fatal/life-threatening) + DCT considerations (E6(R3) Annex 2 + FDA Sept 2024 final + EMA Recommendation 2022) + multi-region PHI coordination (HIPAA Authorization §164.508 + GDPR Article 9 + state-law sensitive-data consent + Common Rule 45 CFR 46) + parallel IRB/IEC tracking + Risk-Based Monitoring (E6(R3) Principle 4) + pharmacovigilance multi-region triage.

- **banking-resilience** — iso-37301-financial-services + dora + dora-non-ctpp + nist-csf + nist-csf-tier-3 + iso-22301. 7 clauses across DORA + FFIEC IT Handbook cross-regime alignment + NIST CSF 2.0 6-Function backbone + multi-stream incident reporting (DORA 4h+72h+1mo + FRB/FDIC/OCC 36-hour CSI rule effective 2022-05-01 + NYDFS Part 500 72-hour + CIRCIA-eligible) + TLPT framework alignment (TIBER-EU + CBEST + MAS AASE + iCAST) + CTPP designation + Lead Overseer + OCC Third-Party Risk Bulletins + SR Letters + ISO 22301 BIA + RTO/MAO/MBCO/RPO + DORA Article 11 ICT BCP + Article 12 restoration testing.

- **utility-cybersecurity** — manufacturing + iso-27001 + nist-csf + nist-csf-tier-3. 7 clauses across NERC CIP-002 through CIP-014 BES Cyber System framework (FERC-approved under Section 215 Federal Power Act) + TSA Pipeline SD 02 series (post-Colonial Pipeline May 2021; 24-hour CISA reporting) + CISA 16 Critical Infrastructure Sectors per PPD-21 + EU NIS2 Directive 2022/2555 Essential + Important Entities (transposition 2024-10-17; Article 23 early-warning 24h + 72h + 1mo) + IEC 62443 series IACS framework + NIST SP 800-82 Rev 3 (2023) OT Security + Purdue Reference Model + CIRCIA 72h cyber + 24h ransomware reporting + Energy Subsector + ONG-C2M2 + ES-C2M2 maturity models.

All 4 reuse parent-overlay templates (no new template files).

**Registry +5 PUBLIC standards:** ICH E6(R3) + EU CTR 536/2014 + NERC CIP + EU NIS2 + FFIEC IT Handbook.

**Counts:**
- Cross-overlay count: 8 → 12
- Total module count: 112 → 116
- Cross-cutting overlay count unchanged at 26

CI extended (+8 validate steps: 4 standalone + 4 vertical-composite).

All 129/129 pytest pass. All 8 bundle baselines clean. YAML linter clean on all 116 modules. Repo-wide invariants: 116 modules / 867 clauses / 379 templates / 0 orphans / **100.0% aggregate coverage**.

Status counts: 6 `:verified` / 91 `:tested` / 5 `:argued` / 0 `:open` (total 102).

Per user direction "do the final overlays" — shipped. **Polishing pass follows as v0.51.0.**

---

## v0.49.0 DRAFT — 2026-05-25 — Engine adopter-features (coverage + crosswalk + jurisdictions-query)

**3 NEW entries** OQ-115 + OQ-116 + OQ-117. Spec total 98 → 101. Engine 0.48.0 → 0.49.0.

3 new CLI subcommands extending the engine adopter-surface. First Architecture-tier additions since OQ-067 (`openqms trace`, v0.39.0). No new modules; no new registry standards.

**OQ-115 — `openqms coverage`**

Per-module + aggregate coverage metrics + `--threshold N` CI regression gate. At v0.49.0 audit time **aggregate coverage = 100.0%** across 112 modules / 838 clauses / 0 orphans. Paired complement to OQ-067 zero-orphan trace invariant.

**OQ-116 — `openqms crosswalk`**

Identifies clauses referencing the same (standard, section) across multiple modules + per-module shared-vs-own-only counts. Useful for spotting overlap across compose-partner modules + per-jurisdiction implementations + cross-overlay parent/child relationships.

**OQ-117 — `openqms jurisdictions-query`**

Queries the registry for standards applicable to a given jurisdiction via publisher-inference (`_PUBLISHER_TO_JURISDICTIONS` table covering 30+ major regulatory publishers: FDA / EPA / DOT / NHTSA / FAA / DoD / HHS / OSHA / USP / EU / EMA / EASA / ISO / ICAO / IATA / IMO / UNECE / OECD / AICPA / PCI SSC / HITRUST / NIST / RTCA / SAE / ICH / WHO etc.). Forward-compatible with explicit `jurisdictions:` field on registry standards entries. FDA query returns 18 standards at audit; EU MDR returns 11.

**13 new pytest tests** (116 → 129):
- `engine/tests/test_coverage.py` — 5 tests
- `engine/tests/test_crosswalk.py` — 4 tests
- `engine/tests/test_jurisdictions_query.py` — 4 tests

CI extended (+3 new smoke-check steps).

All commands work on the current codebase without modification (no per-module migration required).

129/129 pytest pass. All 8 bundle baselines clean. YAML linter clean on all 112 modules. Repo-wide invariants: 112 modules / 838 clauses / 371 templates / 0 orphans / **100.0% aggregate coverage**.

Status counts: 6 `:verified` / 90 `:tested` / 5 `:argued` / 0 `:open` (total 101).

Per user direction "do the engine first then" — shipped. Final cross-overlays (automotive-supply-chain + clinical-trial-multi-region + banking-resilience + utility-cybersecurity) + polishing follow as v0.50.0+.

---

## v0.48.0 DRAFT — 2026-05-25 — US State Privacy Umbrella cross-cutting overlay

**1 NEW entry** OQ-114. Spec total 97 → 98. Engine 0.47.0 → 0.48.0.

26th cross-cutting overlay — **US state comprehensive privacy laws** using the VCDPA template family + state-divergence handling. Single overlay covering ~14 US states. Distinct from the `privacy` overlay (GDPR + CCPA) because CCPA scope is California-only + the other ~14 state laws use a 2-way GDPR-like controller/processor framework distinct from CCPA's 4-way classification + the VCDPA-template states include unique provisions (right-to-appeal denial; UOOM mandatory in 8 states; Maryland MODPA data-minimization strict-necessity).

**Covered state laws** (as of 2026-05-25):
- **Virginia VCDPA** (effective 2023-01-01) — template state
- **Colorado CPA** (2023-07-01)
- **Connecticut CTDPA** (2023-07-01)
- **Utah UCPA** (2023-12-31)
- **Texas TDPSA** (2024-07-01)
- **Oregon OCPA** (2024-07-01)
- **Montana MCDPA** (2024-10-01)
- **Iowa ICDPA** (2025-01-01)
- **Delaware DPDPA** (2025-01-01)
- **New Hampshire NHPA** (2025-01-01)
- **New Jersey NJDPA** (2025-01-15)
- **Tennessee TIPA** (2025-07-01)
- **Minnesota MCDPA** (2025-07-31)
- **Maryland MODPA** (2025-10-01) — **STRICTER** (data minimization strict-necessity + absolute ban on sale of sensitive data + absolute ban on targeted advertising to under-18)
- **Indiana INCDPA** (2026-01-01)
- **Florida FDBR** (2024-07-01) — **NARROW scope** (only entities ≥$1B from online consumer ad services OR consumer app store + ≥250k apps OR smart-speaker virtual assistant)

**10 clauses:** applicability thresholds (per-state) + controller/processor framework + 6 common consumer rights (with right-to-appeal — unique to VCDPA template) + sensitive data divergence (per-state lists vary) + Universal Opt-Out Mechanism (GPC honoring; mandatory in 8 states, optional in 6) + Data Protection Assessment (state-level DPA parallel to GDPR DPIA) + cure period + AG enforcement framework + controller obligations + Maryland MODPA stricter posture + Florida FDBR narrow scope.

**2 new templates:**

1. **`US-STATE-PRIVACY-MATRIX-TEMPLATE.md`** — state-by-state divergence tracker. Per-state matrix with applicability thresholds + cure periods (30-day-sunset vs persistent) + UOOM recognition + sensitive data scope + penalty caps + response deadlines + Maryland MODPA stricter scrutiny + Florida FDBR narrow-scope analysis. Operational programme summary + cure-period management + AG enforcement response sections.

2. **`DATA-PROTECTION-ASSESSMENT-TEMPLATE.md`** — state-level DPA (parallel to GDPR DPIA). Heightened-risk trigger determination (targeted advertising / sale of personal data / sensitive data / profiling / children's data) + 4-section processing description + benefits/risks assessment + Maryland MODPA strict-necessity assessment + Florida FDBR scope check + safeguards + risk-benefit balance decision. Coordinated with GDPR DPIA + CCPA Risk Assessment for single-assessment-multi-regime efficiency.

Plus 2 extensions to existing privacy templates:
- **PRIVACY-POLICY** — state-by-state addendum (per-state controller-contact + consumer-rights summary + UOOM honoring statement + appeal procedure)
- **DPA** — controller-processor contractual requirements per VCDPA-template states

**Registry +1 PUBLIC standard** ("US State Privacy Laws" — covers all 16 named state laws with per-state effective dates + code citations + aliases).

**Cross-cutting overlay count: 25 → 26. Total module count: 111 → 112.**

**7-module privacy/healthcare mega composite validates:**
```
openqms validate \
  --module privacy --module us-state-privacy --module hipaa \
  --module iso-27001 --module iso-27001-privacy \
  --module hitrust-csf --module hitrust-r2
# → invariant_holds: True
```

Repo-wide zero-orphan invariant holds: **112 modules / 838 clauses / 371 templates / 0 orphans** per `openqms trace --all`.

**Particularly natural compositions:**
- `privacy + us-state-privacy` (CCPA California + 14 other states; most common US digital operator stack)
- `privacy + us-state-privacy + hipaa` (full US privacy + healthcare)
- `privacy + us-state-privacy + hipaa + iso-27001 + iso-27001-privacy` (ISMS + PIMS + multi-state privacy + HIPAA — strongest US-operating SaaS posture)
- `privacy + us-state-privacy + connected-medical-device + hipaa + iso-27001 + iso-27001-cloud` (US-operating connected medical device with multi-state consumer base)

**Critical divergences from VCDPA template handled:**
- **Maryland MODPA (effective 2025-10-01)** — data minimization "strictly necessary" standard for sensitive data; absolute prohibition on sale of sensitive data; absolute prohibition on targeted advertising to under-18; narrower GLBA exception; up to $10k + $25k subsequent penalties. Treat as separate compliance posture.
- **Florida FDBR** — narrowest US state law; effectively only Google + Meta + Amazon + Apple. Most adopters OUT. Where applicable: provisions broadly similar to VCDPA + specific opt-out for sale of sensitive data.
- **Texas TDPSA** — cure period does NOT sunset (most states' cure periods sunset after 2-4 years).
- **UOOM divergence** — mandatory in 8 states (Colorado + Connecticut + Texas + Oregon + Montana + Delaware + New Jersey + Minnesota); optional in 6 (Virginia + Utah + Iowa + Tennessee + Indiana + New Hampshire).
- **Right-to-appeal** — denial → appeal mechanism unique to VCDPA-template states; NOT in GDPR or CCPA.

CI extended (+5 validate steps). 116/116 pytest pass. All 8 bundle baselines clean. YAML linter clean on all 112 modules.

Status counts: 6 `:verified` / 87 `:tested` / 5 `:argued` / 0 `:open` (total 98).

**Forward work** per us-state-privacy README:
- Per-state appeal procedure templates
- Universal Opt-Out Signal handling SOP (GPC + IAB GPP + DAA AppChoices)
- Maryland MODPA-specific data minimization assessment
- Florida FDBR threshold determination workflow
- State-AG complaint response template
- Washington My Health My Data Act (MHMDA) standalone overlay — distinct from comprehensive privacy; consumer health data only

Per user direction: "do the us-state privacy umbrella, then we'll turn to the engine next and do final cross-overlays and polishing" — us-state-privacy shipped here. Engine adopter-features (jurisdiction filtering + crosswalk export + module-coverage % reports) follow as v0.49.0+. Final cross-overlays + polishing as v0.50.0+.

---

## v0.47.0 DRAFT — 2026-05-25 — Cross-overlay batch (5): connected-medical-device + cell-therapy-supply-chain + food-allergen-recall + defense-aerospace-cyber + digital-health-multi-region

**1 NEW entry** OQ-113. Spec total 96 → 97. Engine 0.46.0 → 0.47.0.

5 new cross-overlays extending the cross-overlay shape (introduced at v0.44.0 OQ-111) to additional vertical intersections. Cross-overlay count: 3 → 8.

**connected-medical-device** (medical-devices + regulated-ai + privacy + iso-27001 + hipaa):
- FDA §524B cyber-device cybersecurity per Sept 2023 Final Guidance — premarket submission requires SBOM + vulnerability monitoring plan + cybersecurity processes
- EU MDR Annex I §17.2 + MDCG 2019-16 + IEC 81001-5-1
- FDA AI/ML SaMD Predetermined Change Control Plan (PCCP) per Cures Act §3060(d) — pre-authorized algorithm changes without new 510(k)
- NTIA Minimum Elements SBOM (SPDX / CycloneDX / SWID)
- Postmarket cybersecurity per FDA Guidance + 21 CFR 806 corrections + 21 CFR 803 MDR
- ONC Cures Act EHR interoperability (USCDI + FHIR + information-blocking prohibition + 8 exceptions)
- Cross-overlay PHI data-flow coordination (DPIA + HIPAA Risk Analysis + FDA Cybersecurity Risk Assessment shared threat catalog)

**cell-therapy-supply-chain** (pharma + atmp + transport-hazmat):
- Chain of Identity (vein-to-vein for autologous; donor+lot+recipient for allogeneic; 30-yr EU + indefinite US retention)
- Chain of Custody per EU GMP Annex 2A §11
- Cryogenic UN1977 LN2 dry-shipper per IATA PI 202 + 7-14 day vapor-shipper hold time
- Time-Out-of-Storage (TOS) cumulative budget across manufacturing + transport + clinical site
- 21 CFR 1271 HCT/P Subpart A registration + C donor eligibility + D cGTP + F additional requirements
- Autologous failure-mode escalation per FDA CAR-T 2024 Guidance (no batch-pool backup)
- IATA TTSC certification + CEIV Pharma carrier qualification

**food-allergen-recall** (food-safety + recall-workflow + privacy):
- 9 major allergens per FALCPA + FASTER Act (sesame addition effective 2023-01-01)
- 21 CFR 7 Class I default for undeclared allergens — reasonable probability of serious adverse health consequences
- FSMA §117.135(c)(2) food allergen preventive control + §117.140 verification
- Reportable Food Registry 24-hour reporting per FDA
- Consumer-notification ≥98% Level A effectiveness target
- Privacy-compliant consumer data handling per GDPR Article 6(1)(c) legal-obligation basis + CCPA §1798.145(a)(1) compliance-with-legal-obligation exception

**defense-aerospace-cyber** (aerospace + aerospace-defense + defense-cui + cmmc + cmmc-level-2):
- DFARS 252.204-7012 / 7019 / 7020 / 7021 stack
- MIL-STD-882E joint safety+cyber hazard tracking per Tasks 102 + 200 + 300
- ITAR USML Category VIII controlled technical data per 22 CFR §126.18
- Airworthiness cybersecurity per DO-326A / DO-356A / DO-355 / ED-202A
- Supply Chain Risk Management per NIST SP 800-161 + FY19 NDAA §889 prohibition (Huawei / ZTE / Hytera / Hikvision / Dahua) + counterfeit-parts AS9120 / AS6081 / GIDEP
- DoDI 5000.90 platform cyber resilience for acquisition programs
- CMMC Level 2 binding (NS-critical may require Level 3)

**digital-health-multi-region** (medical-devices + privacy + regulated-ai):
- Per-jurisdiction regulatory scope determination (FDA SaMD + EU MDR + UK MDR/Future Regulations + Swiss MepV + Canada MDR)
- Data residency + localisation (GDPR + EU-US DPF + China PIPL + Russia 152-FZ + India DPDP)
- Multi-region consent frameworks (GDPR Article 6+7+9 + HIPAA Authorization + Quebec Law 25 + Ontario PHIPA + state-specific)
- Multi-region AI/ML coordination (EU AI Act + FDA AI/ML SaMD + Canada AIDA + UK AI principles)
- Multi-stream breach notification (HIPAA + GDPR + state AG + MDR §92 + FDA §524B)
- ISO 13485 + MDSAP harmonisation (single audit covering US + Canada + Brazil + Australia + Japan)
- Per-jurisdiction vigilance reporting (FDA MDR + EUDAMED + UK Yellow Card + Health Canada Section 59-60 + Swissmedic)

All 5 reuse parent-overlay templates with binding deltas — no new templates required.

**Registry +3 PUBLIC standards:**
- FD&C §524B — 21 USC §360n-2 cyber-device cybersecurity
- FALCPA + FASTER Act — 21 USC §343(w) + §343(qq) food allergen labeling with sesame addition
- 21st Century Cures Act — Pub. L. 114-255 digital health + interoperability

**Cross-overlay count: 3 → 8.** Total module count: 106 → 111.

**24-module ultra composite validates (new depth record beats prior 22-module healthcare ultimate):**
```
openqms validate \
  --module medical-devices --module pharma --module combination-product \
  --module connected-medical-device --module digital-health-multi-region \
  --module pharma-sterile --module hipaa --module privacy \
  --module iso-27001 --module iso-27001-cloud --module iso-27001-privacy \
  --module regulated-ai --module iso-14001 --module iso-45001 \
  --module iso-50001 --module iso-37001 --module iso-22301 \
  --module iso-31000 --module integrated-management-system \
  --module soc-2 --module soc-2-type-ii \
  --module hitrust-csf --module hitrust-r2 --module iso-37301
# → invariant_holds: True
```

Repo-wide zero-orphan invariant holds: **111 modules / 828 clauses / 367 templates / 0 orphans**.

**Particularly natural compositions:**
- `medical-devices + samd + connected-medical-device + privacy + hipaa + regulated-ai + iso-27001 + iso-27001-cloud` (SaMD-with-cloud-backend)
- `pharma + atmp + transport-hazmat + cell-therapy-supply-chain + recall-workflow` (commercial CAR-T with vein-to-vein logistics)
- `food-safety + recall-workflow + privacy + food-allergen-recall + iso-22000` (multi-channel food brand)
- `aerospace + aerospace-defense + defense-cui + cmmc + cmmc-level-2 + defense-aerospace-cyber + iso-27001 + iso-27001-cloud` (DoD aerospace prime)
- `medical-devices + samd + privacy + hipaa + regulated-ai + digital-health-multi-region` (multi-region digital health SaaS)

CI extended (+11 validate steps including the 24-module ultra composite). 116/116 pytest pass. All 8 bundle baselines clean. YAML linter clean on all 111 modules.

Status counts: 6 `:verified` / 86 `:tested` / 5 `:argued` / 0 `:open` (total 97).

Per user direction: "do more cross-overlays" — all 5 candidates from earlier forward-work list shipped together. Discharges 4 of 5 cross-overlay candidates named in last what's-left analysis (cell-therapy-supply-chain + connected-medical-device + defense-aerospace-cyber + digital-health-multi-region) + adds food-allergen-recall.

---

## v0.46.0 DRAFT — 2026-05-25 — HIPAA satellite templates (discharges OQ-112 forward-work bucket)

**0 NEW entries; 1 new clause + 5 new templates** added to existing OQ-112 hipaa module. Spec total unchanged at 96. Engine 0.45.0 → 0.46.0.

5 HIPAA satellite templates shipped — finishes the HIPAA story end-to-end. Plus 1 new clause added to the hipaa module for the 2024 Reproductive Health Care Privacy Rule attestation requirement per §164.509.

**New clause added to hipaa module:**

- `HIPAA-164-509-reproductive-health-attestation` — §164.509 attestation requirement per HHS Final Rule 89 FR 32976 (April 2024; effective 2026-12-23). CE/BA may not disclose PHI potentially related to reproductive health care for health-oversight / judicial-administrative / law-enforcement / coroner purposes without signed attestation per §164.509(c). Companion to §164.502(a)(5)(iii) prohibition on using PHI to investigate or impose liability for lawful reproductive health care.

**5 new HIPAA satellite templates:**

1. **`HIPAA-AUTHORIZATION-TEMPLATE.md`** — §164.508 written Authorization. Required content per §164.508(c)(1) + required statements per §164.508(c)(2) including right to revoke + treatment-conditioning prohibition + re-disclosure potential + marketing/sale-of-PHI notices. Validity check per §164.508(b)(2). Compound-Authorization prohibition handling. Psychotherapy-notes SEPARATE Authorization requirement. Cross-reference to §164.509 Reproductive Health Care Privacy Rule.

2. **`ACCOUNTING-OF-DISCLOSURES-LOG-TEMPLATE.md`** — §164.528 ongoing log of accountable disclosures. Exempted-disclosures catalog (TPO + to individual + via Authorization + facility directory + §510(b) involvement + national security + correctional + pre-April 2003 + Limited Data Set). Temporary-suspension handling per §164.528(a)(2) for health-oversight + law-enforcement. Individual-request handling: 60-day deadline + 30-day extension + first-accounting-free per 12-month + reasonable cost-based fee for subsequent. 6-year retention.

3. **`RESTRICTION-REQUEST-LOG-TEMPLATE.md`** — §164.522(a) permissive restrictions + HITECH §13405(a) MANDATORY out-of-pocket restrictions + §164.522(a)(2) termination handling + §164.522(b) confidential communications co-administered. Critical: mandatory out-of-pocket restrictions MUST be agreed by CE; operational implications for billing system (segregate patient + service from claim; no insurance bill; subsequent collection efforts must not disclose to health plan).

4. **`OCR-INVESTIGATION-RESPONSE-TEMPLATE.md`** — HHS OCR Compliance Investigation full lifecycle. Document Request response tracking with privileged-log discipline. Interview coordination. Site-visit logistics. Letter of Findings response strategy. Resolution Agreement + Corrective Action Plan execution. CMP tier mapping per §160.404 HITECH 4-tier (Tier 1 unknowing → Tier 4 willful neglect uncorrected; 2024 inflation-adjusted ranges). 42 USC §1320d-6 criminal-penalty cross-reference. Wall of Shame public-listing risk + communications planning. SEC Item 1.05 8-K coordination for material incidents at US-public-company controllers.

5. **`REPRODUCTIVE-HEALTH-ATTESTATION-TEMPLATE.md`** — §164.509 Attestation per HHS Final Rule. Threshold determination ("could the PHI potentially relate to reproductive health care"). Required content per §164.509(c). Validity check (incomplete / compound / known-false / substantial-evidence-of-false defects). Refusal handling. Cross-state-line scenario coordination (reproductive health care lawful in provider state but criminalised in requestor state — engage legal counsel). Accounting of Disclosures cross-logging.

Plus the existing SOP template binding updated to reference §164.509 attestation handling alongside existing operational items.

**hipaa module: 14→15 clauses, 5→10 templates.**

**No new registry standards** — all reuse existing HIPAA + HITECH registrations.

**Total templates: 96 → 101.** Total modules unchanged at 106.

**OQ-112 forward-work bucket discharged:**
- ✓ Authorization form template per §164.508
- ✓ Accounting of Disclosures log template per §164.528
- ✓ Restriction Request log per §164.522(a)
- ✓ OCR Compliance Investigation response template
- ✓ Reproductive Health Care Privacy Rule 2024 attestation template per §164.509

Remaining OQ-112 forward work (deferred per scope):
- 42 CFR Part 2 (substance use disorder) overlay — narrower scope than HIPAA + additional consent requirements; separate dedicated overlay rather than HIPAA satellite template
- ONC certified EHR technology adoption tracker
- connected-medical-devices cross-overlay

CI: 116/116 pytest pass. All 8 bundle baselines clean. YAML linter clean on all 106 modules.

Status counts unchanged: 6 `:verified` / 85 `:tested` / 5 `:argued` / 0 `:open` (total 96).

Per user direction: "do 1" + scope clarification "HIPAA satellite templates only" — shipped here. Finishes the HIPAA story end-to-end.

---

## v0.45.0 DRAFT — 2026-05-24 — HIPAA dedicated cross-cutting overlay

**1 NEW entry** OQ-112. Spec total 95 → 96. Engine 0.44.0 → 0.45.0.

25th cross-cutting overlay — US healthcare-specific privacy + security per 45 CFR Parts 160 + 164 + HITECH. Distinct from the `privacy` overlay (GDPR + CCPA) — HIPAA's CE/BA framework + 4-rule architecture + OCR enforcement + BAA contractual framework + healthcare-specific provisions (TPO + de-identification Safe Harbor + NPP + accounting of disclosures + Authorization) warrant dedicated overlay.

**Standards: both PUBLIC**
- HIPAA — 45 CFR Parts 160 + 164 (Privacy + Security + Breach Notification + Enforcement Rules)
- HITECH — Pub. L. 111-5 Title XIII + Final Rule 78 FR 5566 + Promoting Interoperability

**14 clauses** across CE/BA scope + uses + disclosures + de-identification + individual rights + administrative requirements + Security Rule (administrative + physical + technical safeguards) + BAA + 6-year documentation + Breach Notification 4-factor + Enforcement Rule 4-tier CMP + HITECH extensions.

**4 new HIPAA-specific templates:**
- NPP — Notice of Privacy Practices per §164.520 with 2024 Reproductive Health Care Privacy Rule additions per §164.509
- BAA — Business Associate Agreement per §164.504(e) + §164.314 with subcontractor flow-down + 60-day breach notification + return/destroy at termination
- HIPAA Security Rule Risk Analysis — §164.308(a)(1)(ii)(A) foundational artifact with threat catalog + vulnerability assessment + implementation-specification status per §§308/310/312 (Required vs Addressable)
- HIPAA Breach 4-Factor Risk Assessment — §164.402(2) presumption-rebuttal worksheet with encryption/destruction safe harbor + 4-factor analysis + notification matrix

**Cross-cutting overlay count: 24 → 25.** Total module count: 105 → 106. Registry +2 PUBLIC standards.

**22-module healthcare ultimate composite validates (new depth record beats prior 20-module):** medical-devices + pharma + combination-product + pharma-sterile + hipaa + privacy + iso-27001 + iso-27001-cloud + iso-27001-privacy + regulated-ai + iso-14001 + iso-45001 + iso-50001 + iso-37001 + iso-22301 + iso-31000 + integrated-management-system + soc-2 + soc-2-type-ii + hitrust-csf + hitrust-r2 + iso-37301.

Repo-wide zero-orphan invariant holds: **106 modules / 792 clauses / 350 templates / 0 orphans**.

**Particularly natural compositions:**
- `hipaa + privacy` (PHI under HIPAA + non-PHI under GDPR/CCPA/state)
- `medical-devices + hipaa + privacy + iso-27001` (connected medical devices)
- `pharma + hipaa + privacy` (clinical-trial PHI)
- `hipaa + hitrust-csf + hitrust-r2` (validated multi-framework attestation including HIPAA)
- `hipaa + soc-2 + soc-2-type-ii` (healthcare-tech SaaS standard pairing)
- `hipaa + iso-27001 + iso-27001-privacy` (ISMS + PIMS + HIPAA triad)
- `hipaa + iso-37301 + iso-37301-healthcare` (compliance-management + sectoral + HIPAA)

CI extended (+8 validate steps). 116/116 pytest pass. All 8 bundle baselines clean. YAML linter clean on all 106 modules.

Status counts: 6 `:verified` / 85 `:tested` / 5 `:argued` / 0 `:open` (total 96).

Per user direction: "do 2 then 1" — 2 (HIPAA dedicated) shipped here; 1 (cross-audit + v0.40-v0.45 omnibus companion) follows.

---

## v0.44.0 DRAFT — 2026-05-24 — Cross-overlay batch (combination-product + integrated-management-system + food-pharma-grade)

**1 NEW entry** OQ-111. Spec total 94 → 95. Engine 0.43.0 → 0.44.0.

3 new cross-overlays introducing a new module shape — **cross-overlay**: overlays that bind ACROSS specific vertical combinations to encode intersection-specific regulatory requirements. Distinct from cross-cutting overlays (apply to any single vertical), class overlays (within-vertical rigor delta), and sub-overlays (within-cross-cutting tier delta).

**combination-product (medical-devices + pharma):**
- 6 clauses across FDA 21 CFR Part 4 + EU MDR Article 117
- PMOA determination + RFD per 21 CFR §3.7
- Streamlined single-system CGMP approach per §4.4 (drug-led or device-led)
- EU MDR Article 117 device-component NB opinion (with USP <660>/<661>, ISO 11608, ISO 11040, ISO 8536 typical citations)
- Cross-application registration coordination (NDA/BLA + 510(k)/PMA)
- Postmarket surveillance coordination (lead-reporter MDR + ADE per §4 Subpart B; 5-day + 30-day deadlines)
- Design controls cross-application (specific QSR §820.20/30/50/100/170/200 + specific Part 211 §211.84/103/132/137/165/166/167/170)

**integrated-management-system (multi-MS coordination):**
- 8 clauses across Annex SL HLS leverage
- Shared policy + objectives across all in-scope MS
- Shared context + interested-parties analysis
- Integrated risk + opportunity register (composes with iso-31000 meta-framework)
- Combined management review per §9.3 of each MS standard
- Combined audit programme per ISO 19011:2018
- Integrated documented-information control
- Annex SL HLS version tracking + coordinated revision transitions

**food-pharma-grade (chemicals + food-safety + pharma):**
- 6 clauses at the intersection of three regulatory regimes
- US FCS/FCN pathway (21 CFR 174-178 + FCN per 21 USC §348(h) + TOR per §170.39 + GRAS per §170.30 + prior-sanctioned)
- EU FCM framework (Regulation 1935/2004 Article 3 safety + Article 16 supply-chain DoC)
- EU plastic FCM positive list + SMLs (Regulation 10/2011 Annex I + II OML 10mg/dm² or 60mg/kg + III food simulants A-E + Amendment 2023/1442)
- USP packaging chapters (<660> glass Type I-IV + <661> plastics including <661.1>/<661.2> + <87>/<88> biological reactivity Class I-VI)
- E&L workflow per USP <1663>/<1664> + per-dosage-form risk-based scoping (OINDP + parenteral highest)
- Supply-chain DoC cascade per EU Article 16

All 3 reuse parent-overlay templates with binding deltas — no new templates required.

**Registry +5 standards:**
- 21 CFR Part 4 (PUBLIC) — FDA combination products CGMP
- 21 CFR 174-178 (PUBLIC) — food-contact substances
- EU 1935/2004 (PUBLIC) — FCM framework
- EU 10/2011 (PUBLIC) — plastic FCM
- USP Packaging Chapters (commercial) — pharma packaging

**Module count: 102 → 105. Cross-cutting overlay count UNCHANGED at 24.** Cross-overlays are a distinct module shape from cross-cutting overlays.

**20-module ultimate composite validates (new depth record beats prior 19-module):**
```
openqms validate \
  --module medical-devices --module pharma --module combination-product \
  --module pharma-sterile --module privacy \
  --module iso-27001 --module regulated-ai --module iso-14001 \
  --module iso-45001 --module iso-50001 --module iso-37001 \
  --module iso-22301 --module iso-31000 \
  --module integrated-management-system \
  --module soc-2 --module soc-2-type-ii \
  --module hitrust-csf --module hitrust-r2 \
  --module iso-27001-cloud --module iso-27001-privacy
# → invariant_holds: True
```

Repo-wide zero-orphan invariant holds: **105 modules / 778 clauses / 345 templates / 0 orphans** per `openqms trace --all`. CI extended (+10 validate steps). 116/116 pytest pass. All 8 bundle baselines clean. YAML linter clean on all 105 modules.

Status counts: 6 `:verified` / 84 `:tested` / 5 `:argued` / 0 `:open` (total 95).

Per user direction: "now let's do the cross-overlays" — all three shipped together.

---

## v0.43.0 DRAFT — 2026-05-24 — Sub-overlay batch (DORA tiers + HITRUST scoping levels + ISO 37301 sectoral profiles)

**1 NEW entry** OQ-110. Spec total 93 → 94. Engine 0.42.0 → 0.43.0.

10 new sub-overlays extending the v0.42.0 sub-overlay shape to three additional cross-cutting overlays.

**DORA tiers (3):**
- `dora-ctpp` — Critical Third-Party Provider per Chapter V Articles 31-44 (Lead Overseer EBA/ESMA/EIOPA direct oversight; JET inspections; corrective recommendations; oversight fees; enhanced Article 28+30 contracts)
- `dora-non-ctpp` — Baseline Article 30 contractual framework; indirect via financial-entity due diligence
- `dora-tlpt` — Threat-Led Penetration Testing per Articles 26-27 + TIBER-EU framework (3-year minimum; TI Provider + Red Team Provider accreditation; third-party inclusion + cross-border recognition + Article 19 integration)

**HITRUST scoping levels (3):**
- `hitrust-e1` — Essentials 1-year (44 controls cyber-hygiene baseline)
- `hitrust-i1` — Intermediate 1-year (182 leading-practices controls)
- `hitrust-r2` — Risk-based 2-year (200-2000+ factor-tailored controls + PRISMA + multi-framework crosswalk HIPAA + HITECH + ISO 27001 + NIST + PCI DSS + GDPR)

**ISO 37301 sectoral profiles (4):**
- `iso-37301-public-sector` — public-trust + procurement integrity + FOI + UN anti-corruption
- `iso-37301-financial-services` — prudential/conduct + AML/CFT/sanctions + consumer protection + DORA/NYDFS coordination
- `iso-37301-healthcare` — HIPAA/HITECH + FWA + research compliance + 340B/pharmacy
- `iso-37301-general-business` — Annex SL IMS baseline + employment + product safety + tax/trade + antitrust

All 10 reuse parent-overlay templates with binding deltas. No new registry standards.

Cross-cutting overlay count unchanged at 24. Sub-overlays not counted in 24.

Total module count: 92 → 102. Total sub-overlay count: 16 → 26.

Repo-wide zero-orphan invariant holds: **102 modules / 758 clauses / 338 templates / 0 orphans** per `openqms trace --all`. CI extended (+15 validate steps). 116/116 pytest pass. All 8 bundle baselines clean. YAML linter clean on all 102 modules.

Status counts: 6 `:verified` / 83 `:tested` / 5 `:argued` / 0 `:open` (total 94).

Per user direction: "do the sub-overlay" → all three (DORA + HITRUST + ISO 37301) — shipped together.

---

## v0.42.0 DRAFT — 2026-05-24 — Sub-overlay Tier 1 batch (CMMC levels + SOC 2 types + ISO 27001 extensions)

**1 NEW entry** OQ-109. Spec total 92 → 93. Engine 0.41.0 → 0.42.0.

7 new sub-overlays introducing a new module shape — **class-overlay-like rigor/scope deltas on cross-cutting overlays** (analog to how class overlays like aerospace-dal-a or pharma-sterile delta against vertical overlays). Splits previously-monolithic cross-cutting overlays into their natural tier structure per the underlying standards.

**CMMC sub-overlays (3) — splits monolithic `cmmc` into CMMC 2.0's three levels:**
- `cmmc-level-1` — FAR 52.204-21 17 basic safeguarding requirements; FCI-only scope; annual self-assessment + SPRS + senior official affirmation; no POAM allowance
- `cmmc-level-2` — NIST SP 800-171 110 requirements across 14 control families; CUI scope; self-assessment OR C3PAO bifurcation per prioritized-acquisition designation; 5% POAM allowance with 180-day Conditional CMMC Status; DFARS 7012 72h DIBNet incident reporting
- `cmmc-level-3` — additional 24 NIST SP 800-172 enhanced APT-protection requirements; national-security-critical CUI scope; DIBCAC-only assessment (NOT C3PAO-delegable); no POAM allowance

**SOC 2 sub-overlays (2) — splits monolithic `soc-2` into reporting types:**
- `soc-2-type-i` — point-in-time design suitability per AT-C 205; no observation period; readiness/first-year pathway; lower customer acceptance (many enterprise procurement teams reject Type I)
- `soc-2-type-ii` — design + operating effectiveness over observation period (minimum 3 months / typical 6mo first / 12mo annual renewal); enterprise-customer default; bridge-letter handling for inter-report gaps; modified-opinion handling

**ISO 27001 extension sub-overlays (2) — splits monolithic `iso-27001` extensions:**
- `iso-27001-cloud` — ISO/IEC 27017:2015 Code of practice for cloud services. CSP + CSC shared responsibility model; 7 new cloud-specific controls (CLD.6.3.1 shared roles; CLD.8.1.5 termination data removal; CLD.9.5.1/2 virtual segregation + VM hardening; CLD.12.1.5 admin operations; CLD.12.4.5; CLD.13.1.4 virtual+physical network alignment)
- `iso-27001-privacy` — ISO/IEC 27701:2019 PIMS (Privacy Information Management System). Extension to 27001 ISMS; Annex A 31 controller controls + Annex B 18 processor controls; Annex D GDPR mapping + Annex E ISO 29100 mapping. Strong complement to the `privacy` cross-cutting overlay (privacy encodes legal framework; 27701 encodes certifiable management system)

All 7 reuse parent-overlay templates with binding deltas — no new templates required.

**Registry +2 commercial standards:**
- ISO/IEC 27017:2015 (cloud services)
- ISO/IEC 27701:2019 (PIMS)

Other 4 sub-overlays reuse existing registered standards (CMMC 2.0 + NIST SP 800-171 + AICPA TSC 2017).

**Cross-cutting overlay count unchanged at 24** — sub-overlays are NOT counted in the 24; they are class-overlay-shaped deltas on cross-cutting overlays, analogous to how aerospace-dal-a is not counted in the verticals count.

**Total module count: 76 → 83.**

**19-module deepest composite validates (new depth record beats prior 17-module):**
```
openqms validate \
  --module chemicals --module chemicals-svhc \
  --module chemicals-authorisation --module chemicals-tonnage-1000 \
  --module osha-hcs --module transport-hazmat --module eu-biocides \
  --module tsca-pfas --module iso-27001 --module iso-27001-cloud \
  --module iso-27001-privacy --module regulated-ai --module iso-14001 \
  --module iso-45001 --module iso-50001 --module iso-37001 \
  --module iso-22301 --module iso-31000 --module privacy
# → invariant_holds: True
```

Repo-wide zero-orphan invariant holds: **83 modules / 675 clauses / 319 templates / 0 orphaned clauses / 0 orphaned templates** per `openqms trace --all`.

**Particularly natural compositions:**
- `defense-cui + cmmc + cmmc-level-2` (typical DoD CUI handler self-assessment scope)
- `defense-cui + cmmc + cmmc-level-2 + cmmc-level-3` (NS-critical handlers; Level 3 is additive to Level 2)
- `soc-2 + soc-2-type-ii` (enterprise-customer steady-state)
- `soc-2 + soc-2-type-i` (first-year readiness; Type-I-to-Type-II progression)
- `iso-27001 + iso-27001-cloud` (cloud-native SaaS)
- `iso-27001 + iso-27001-privacy + privacy` (ISMS + PIMS + legal-framework triad — strongest privacy certification posture)
- `iso-27001 + iso-27001-cloud + iso-27001-privacy + privacy` (cloud SaaS processing PII)

CI extended (+14 validate steps including the 19-module deepest composite). 116/116 pytest pass. All 8 bundle baselines clean. YAML linter clean on all 83 modules.

Status counts: 6 `:verified` / 82 `:tested` / 5 `:argued` / 0 `:open` (total 93).

**Tier 2 sub-overlays ALSO shipped in same release** (9 additional): 4 NIST CSF Implementation Tiers (nist-csf-tier-1 Partial / tier-2 Risk Informed / tier-3 Repeatable / tier-4 Adaptive) + 5 PCI DSS SAQ types (pci-dss-saq-a / saq-a-ep / saq-d-merchant / saq-d-sp / saq-p2pe). Originally planned for v0.43.0, consolidated into v0.42.0 since both tiers share the same sub-overlay shape + spec entry.

**Total sub-overlay batch: 16 sub-overlays** (7 Tier 1 + 9 Tier 2). All reuse parent-overlay templates. Registry +2 commercial standards (ISO 27017 + ISO 27701); other 14 reuse existing registered standards (CMMC 2.0 + NIST SP 800-171 + AICPA TSC 2017 + NIST CSF 2.0 + PCI DSS v4.0).

Total module count: **76 → 92**. Cross-cutting overlay count UNCHANGED at 24 (sub-overlays are not counted in the 24 — they are class-overlay-shaped deltas on cross-cutting overlays).

Per user direction: "do cluster A" (sub-overlays) — all 16 shipped together.

---

## v0.41.0 DRAFT — 2026-05-24 — Privacy cross-cutting overlay (GDPR + CCPA/CPRA) — last major management-system gap

**1 NEW entry** OQ-108. Spec total 91 → 92. Engine 0.40.0 → 0.41.0.

24th cross-cutting overlay shipped — closes the last major management-system gap in the Open QMS overlay set. Universally applicable since virtually every adopter processes personal data (customers, employees, suppliers, clinical-trial subjects, complaint reporters, safety reporters).

**Standards:**
- **EU GDPR** (Regulation (EU) 2016/679) — PUBLIC; effective 2018-05-25
- **CCPA/CPRA** (Cal. Civ. Code §1798.100-199) — PUBLIC; CCPA effective 2020-01-01; CPRA amendments 2023-01-01; CPPA final ADMT + Risk Assessment + Cybersecurity Audit regulations 2025-2026
- UK GDPR addressed under same clauses (DPA 2018 retains EU GDPR with UK ICO as supervisory authority)

**21 clauses across the two frameworks:**

*GDPR (15 clauses):* Article 5 principles + Article 6 lawful bases + Article 7 consent + Article 9 special categories + Article 12 modalities + Articles 13-14 information + Articles 15-22 substantive rights + Article 25 by-design/default + Article 28 processor + DPA + Article 30 ROPA + Article 32 security + Articles 33-34 breach + Article 35 DPIA + Articles 37-39 DPO + Articles 44-49 international transfers (with Schrems II Transfer Impact Assessment).

*CCPA/CPRA (6 consumer + 4 business = 10 clauses):* §1798.100/110/115 right to know + §1798.105 right to delete + §1798.106 right to correct + §1798.120/135 opt-out of sale/share (+ GPC honoring per CPPA §7025) + §1798.121 limit use of SPI + §1798.130 methods + 45-day response + §1798.135/§7012 notice at collection + §1798.140/§7050-7053 service provider/contractor/third party + §1798.150 private right of action + §1798.185 CPPA regulatory regime (ADMT + Risk Assessment + Cybersecurity Audit 2025-2026).

**5 new privacy-specific templates:**

1. **`PRIVACY-POLICY-TEMPLATE.md`** — Public-facing policy covering GDPR Articles 13-14 information requirements + CCPA notice-at-collection in one document. Includes the 11 CCPA personal-information categories (A-K + SPI L) table; GDPR Article 6 lawful-basis-per-purpose grid; special-category / SPI handling per GDPR Article 9 + CPRA SPI; CCPA + GDPR rights summary; Global Privacy Control honoring; international transfer disclosure; cookies + tracking; children's privacy; dispute channels with EU SA + UK ICO + Swiss FDPIC + CPPA + FTC + state AG contacts.

2. **`DPA-TEMPLATE.md`** — Multi-regime Data Processing Agreement covering GDPR Article 28 required content + CCPA §1798.140 service-provider/contractor/third-party classification per CPPA §7050-7053 + Implementing Decision 2021/915 SCCs + Transfer Impact Assessment per Schrems II + sub-processor authorisation modes + audit rights with SOC 2 / ISO 27001 / ISO 27701 acceptable-attestation alternatives + 24-hour breach notification SLA + deletion/return at termination + CPPA Cybersecurity Audit + Risk Assessment + ADMT assistance.

3. **`DPIA-TEMPLATE.md`** — GDPR Article 35 DPIA + CCPA Risk Assessment per CPPA §7150-7157. Threshold assessment (Article 35(3) automatic triggers + lead SA positive/negative lists + EDPB WP248 rev.01 9-criteria scoring + CCPA Risk Assessment triggers) + systematic description (nature / scope / context / purposes) + necessity + proportionality + risk assessment (per WP250 + EDPB Guidelines 4/2019 consequence categories with likelihood × severity) + measures (Article 25 by-design + Article 32 security) + DPO + data subject consultation + decision matrix (proceed / with conditions / Article 36 prior consultation / not proceed).

4. **`ROPA-TEMPLATE.md`** — GDPR Article 30 Records of Processing Activities. Part A controller variant (all 7 required fields per 30(1)(a)-(g) + supplementary metadata) + Part B processor variant (all 4 required fields per 30(2)(a)-(d)). Maintenance discipline table mapping triggering events (new purpose / modified purpose / retirement / new recipient / retention change / Article 32 measure change / annual review / SA Article 30(4) request) to ROPA actions.

5. **`PERSONAL-DATA-BREACH-NOTIFICATION-TEMPLATE.md`** — Multi-regime breach record covering GDPR Article 33 (72-hour SA notification) + Article 34 (data subject notification when high risk) + Article 33(5) documentation obligation (records retained regardless of notification threshold) + CCPA §1798.150 documented incident record + US state AG breach notification cross-reference (Cal. Civ. Code §1798.82, TX/NY/FL/IL state laws) + HIPAA Breach Notification Rule + FTC Health Breach Notification Rule + SEC Item 1.05 8-K for material cybersecurity incidents at US-public-company controllers. CIA-triad classification + cause categorisation + encryption/pseudonymisation state (which determines Article 34(3)(a) exemption + CCPA §1798.150 private-action exposure) + WP250 consequence-category risk assessment + notification decision matrix per regime + Article 33(3) info elements.

Plus 1 cross-cutting binding (SOP-TEMPLATE) for privacy operational SOPs (consent management + DSR intake + DPO escalation + identity verification per CPPA §7060-7064 3-2-1 tier model + transfer impact assessment per Schrems II).

**Registry +2 PUBLIC standards** (GDPR + CCPA). EDPB Guidelines (WP248 rev.01 + WP250 + 07/2019 + 07/2020 + 03/2022 + 4/2019 + 9/2022) + CPPA regulations + 2021/915 SCCs + UK IDTA all PUBLIC supplementary.

**Cross-cutting overlay count: 23 → 24.** Last major management-system gap closed.

**17-module ultimate composite validates (new depth record beats prior 16-module):**
```
openqms validate --module chemicals --module chemicals-svhc \
  --module chemicals-authorisation --module chemicals-tonnage-1000 \
  --module osha-hcs --module transport-hazmat --module eu-biocides \
  --module tsca-pfas --module iso-27001 --module regulated-ai \
  --module iso-14001 --module iso-45001 --module iso-50001 \
  --module iso-37001 --module iso-22301 --module iso-31000 \
  --module privacy
# → invariant_holds: True
```

Repo-wide zero-orphan invariant holds: **76 modules / 639 clauses / 305 templates / 0 orphaned clauses / 0 orphaned templates** per `openqms trace --all`.

**Particularly natural compositions** documented in `modules/privacy/README.md`:
- privacy + iso-27001 (privacy is WHY; iso-27001 is HOW for Article 32 security)
- privacy + soc-2 (SOC 2 Privacy criterion overlap)
- privacy + hitrust-csf (HITRUST internally maps HIPAA + GDPR + CCPA)
- privacy + regulated-ai (GDPR Article 22 + CCPA ADMT for automated decision-making)
- privacy + recall-workflow (recall customer notifications process personal data)
- privacy + medical-devices/pharma/food-safety/automotive/chemicals — universal

**Out of scope (deferred):** UK GDPR specialist overlay (UK ICO + UK IDTA specialisation); PIPEDA (Canada); LGPD (Brazil); APPI (Japan); PIPL (China); US state-privacy overlays (Virginia VCDPA + Colorado CPA + Connecticut CTDPA + Utah UCPA + Texas TDPSA + Oregon OCPA + Montana MCDPA + Iowa ICDPA + Florida FDBR + Delaware DPDPA + New Jersey NJDPA + Tennessee TIPA + Indiana INCDPA + New Hampshire NHPA — most follow VCDPA template; could ship as single `us-state-privacy` overlay); HIPAA dedicated overlay; GLBA Safeguards Rule; COPPA; FERPA; EU ePrivacy standalone; CPPA ADMT/Risk/Cybersecurity sub-overlays once final; DSR Workflow issue templates; TIA standalone; cookie banner standards; DPO appointment letter; Article 27 EU representative appointment.

CI extended (+11 validate steps including the 17-module ultimate composite). 116/116 pytest pass. All 8 bundle baselines clean. YAML linter clean on all 76 modules.

Status counts: 6 `:verified` / 81 `:tested` / 5 `:argued` / 0 `:open` (total 92).

Per user direction: "let's start with the privacy overlay" — shipped.

---

## v0.40.0 DRAFT — 2026-05-24 — Hygiene pass — audit F1-F6 + YAML linter + v0.39 companion

**0 spec entries; 0 status changes.** Pure hygiene release discharging audit `audit_2026-05-24.md` findings + adding tooling discipline + closing v0.39.0 documentation. Engine 0.39.0 → 0.40.0.

**F1 closeout — OQ-054..OQ-058 registry rows expanded.** Previously condensed per a v0.12.0 snapshot footnote. A1 coverage gap now zero — 91 spec entries / 91 registry rows.

**F5 — exact template count.** README + catalog claim "81+ templates" → exact "87" (with breakdown: v0.38.0 +3 chemicals class-overlay; v0.37.0 +5 chemicals-adjacent).

**F6 — `ivd` re-categorised as sub-vertical.** Catalog medical-devices class-overlay table reorganised: `ivd` (IVD sub-vertical scope — EU IVDR + 21 CFR 809 + ISO 15189) is a sub-vertical cross-cutting that takes its own class overlays `ivdr-class-c` + `ivdr-class-d`. Listed for discoverability but NOT counted in the 9 medical class overlays (which are all rigor/risk-class deltas). Resolves the "medical 9 vs 10" ambiguity flagged by the audit.

**New tooling — `scripts/lint-module-yaml.py`.** Pre-pytest CI gate that catches the YAML failure modes observed during chemicals arc:
- Unquoted colon-space pattern in template `name:` values (the foot-gun that broke `transport-hazmat/module.yaml` parse at v0.37.0)
- Missing or empty required keys (`name`, `version`, `clauses`)
- Missing or empty clause fields (`id`, `standard`, `section`, `summary`)
- Duplicate clause ids within a module
- Missing or empty template fields (`path`, `name`, `addresses`)
- Template `addresses` entries referring to clauses not in the module's own clause set (cross-module address bug)
- Top-level `module.yaml` malformed (not a mapping)

Linter clean on all 75 modules at v0.40.0. Wired into CI as a pre-pytest gate so the YAML-parse failure mode is caught before the validate sweep runs.

**OQ-067 deferred cleanup — workflow job ID renamed.** `.github/workflows/traceability.yml` job ID `generate-trace-matrix` → `generate-traceability-snippet`. Original job's display name was already accurate ("Generate traceability snippet"); the YAML id was misleading and the deferred-cleanup note in OQ-067 spec entry has been pending since v0.1.1. Renamed now that the actual `openqms trace` command shipped (no name collision risk). Branch-protection required-checks may need a one-time update if any were configured against the old name.

**v0.39.0 companion shipped.** `BUSINESS/companion_v0_39_argued_push.md` documents the `:argued → :tested` upgrade arc (OQ-062 + OQ-067) per TCE companion-doc discipline. `companion_index.md` row added.

**Audit findings status post-v0.40.0:**

| Finding | Status |
|---|---|
| F1 — Registry missing 5 rows OQ-100..OQ-104 | Closed (v0.39 audit commit added 5 rows; v0.40 added 5 more for OQ-054..OQ-058) |
| F2 — Example bundles count claimed 12; actual 8 | Closed (audit commit) |
| F3 — Catalog section headings stale | Closed (audit commit) |
| F4 — OQ-068 stale notes | Closed (audit commit) |
| F5 — Templates count "81+" vs actual 87 | Closed (v0.40 — exact count) |
| F6 — Medical-devices class overlay count ambiguity | Closed (v0.40 — ivd recategorised as sub-vertical) |
| F7 — Omnibus companion span inconsistency | Closed (audit commit) |

All 7 audit findings discharged. Project hygiene now at the floor.

**Test count**: 116 unchanged. All passing. All 8 bundle baselines clean. New linter gate passes clean.

Per user direction: "do 1 through 6" — items 1 (v0.39 companion) + 2 (F5 template count) + 3 (F6 ivd categorisation) + 4 (YAML linter) + 5 (workflow job-ID rename) + 6 (OQ-054..058 registry expansion) all shipped together as v0.40.0.

---

## v0.39.0 DRAFT — 2026-05-24 — `:argued → :tested` push (OQ-062 PHI compartmentalization + OQ-067 repo-wide trace)

**0 NEW entries; 2 status upgrades.** Spec total unchanged at 91. Engine 0.38.0 → 0.39.0.

Two of the seven `:argued` entries upgraded to `:tested` per the audit recommendation. The remaining 5 `:argued` entries are honest-effort-by-nature (OQ-003 invariant disclaimer; OQ-022 + OQ-023 substrate items requiring adopter-org config; OQ-070 + OQ-071 licensing items requiring manual interpretation) and stay `:argued` indefinitely.

**OQ-062 PHI/PII compartmentalization — `:argued → :tested`**

New test file `engine/tests/test_phi_compartmentalization.py` with 4 structural property tests asserting the complaint intake template (`.github/ISSUE_TEMPLATE/complaint.yml`) is structurally incapable of capturing PHI:
- `test_complaint_template_loads_as_valid_yaml` — YAML well-formedness
- `test_complaint_template_has_no_phi_fields` — no form field id or label matches PHI/PII patterns (patient_name / mrn / ssn / dob / personal email / contact phone / mailing address etc.)
- `test_complaint_template_carries_phi_handling_warning` — body markdown contains "PHI" + "PII" + "do not" warning trio
- `test_complaint_template_references_external_phi_record` — body or field text references external compartment (private / external / ephi / encrypted / restricted / eqms)

These are structural tests on the template DESIGN — they enforce the compartmentalization property at the artifact level, not runtime PHI scanning of submitted issues (correctly out of scope; adopters' own infrastructure handles runtime hygiene per their SOP).

**OQ-067 repo-wide trace matrix — `:argued → :tested`**

New CLI subcommand `openqms trace [--module M | --all] [--format json|md] [--output FILE]`:

- Walks every module under `./modules/` (or selected modules)
- Per-module: forward map (clause → templates that address it) + reverse map (template → clauses it addresses) + orphan detection (orphaned clauses + orphaned templates)
- Aggregate summary: module count + total clauses + total templates + total clause→template addresses + orphan totals
- JSON output (machine-readable for downstream tooling) or Markdown (audit-ready)

Implementation: `engine/openqms/cli.py::_cmd_trace` + `_format_trace_markdown`. Tests: `engine/tests/test_trace.py` with 4 tests covering `--all` summary, bidirectional forward/reverse consistency, orphan detection presence, markdown format rendering.

CI extended with a new `Repo-wide trace matrix (smoke check + zero-orphan invariant)` step that runs `openqms trace --all` and asserts zero orphaned clauses + zero orphaned templates across every shipped module. This is the OQ-001 invariant at scale — every push verifies that no module ever leaves a clause without a template or a template without a clause-binding.

At audit time `openqms trace --all` reports:
- 75 modules in scope
- 614 clauses total
- 299 templates total
- 0 orphaned clauses
- 0 orphaned templates

Repo-wide OQ-001 invariant holds.

**Test count**: 108 → 116 (+8). All passing.

Status counts: 6 `:verified` / 80 `:tested` / **5 `:argued`** / 0 `:open` (total 91).

`:argued` 7 → 5 — only honest-effort-by-nature entries remain.

Per user direction: "do OQ-062 and OQ-067" — both shipped.

---

## v0.38.0 DRAFT — 2026-05-24 — Chemicals class overlays (SVHC + Authorisation + 4 tonnage bands)

**1 NEW entry** OQ-107. Spec total 90 → 91. Engine 0.37.0 → 0.38.0.

6 chemicals class overlays shipped — the first chemicals class-overlay set, completing the chemicals-domain build-out alongside v0.36.0 vertical + v0.37.0 adjacent standalones.

**chemicals-svhc** — REACH SVHC supply-chain + ECHA notification obligations
- 5 clauses: Article 7(2) SVHC-in-articles ECHA notification (>1 t/y AND >0.1% w/w); Article 33(1) recipient communication; Article 33(2) consumer response 45 days; Waste Framework Directive (EU) 2018/851 Article 9(1)(i) SCIP database notification; Annex XV identification dossier
- New template: `templates/product-chemicals/svhc/SVHC-COMMUNICATION-LETTER-TEMPLATE.md` (covers Article 33(1) + 33(2) + SCIP cross-reference + consumer-response 45-day handling)
- SVHC Candidate List currently ~240 substances; refreshed ~2x/year — re-screen supply chain each refresh
- *FCD* CJEU C-106/14 judgment — >0.1% threshold applies per-component, not per total mass of complex article

**chemicals-authorisation** — REACH Title VII Articles 55-66 + Annex XIV
- 6 clauses: Article 56 prohibition without authorisation; Article 60 grant (Adequate Control route vs. Socio-Economic route — Adequate Control NOT available for non-threshold-CMR/PBT/vPvB); Article 62 application content (CSR + AoA + Substitution Plan + SEA); Articles 65-66 holder labelling + downstream-user notification within 3 months; Article 61 review (report 18 months before period end); Annex XIV ~60 listed substances incl. phthalates DEHP/DBP/BBP/DIBP + chromates + lead chromate
- New templates: `templates/product-chemicals/authorisation/REACH-AUTHORISATION-APPLICATION-TEMPLATE.md` (Article 62 full application with route selection per substance properties + fee structure + joint-application provisions) + `templates/product-chemicals/authorisation/SUBSTITUTION-PLAN-TEMPLATE.md` (Article 60(4)(c) with 10-action timetable + risk-management transition + contingencies)

**chemicals-tonnage-1** — Annex VII baseline ≥1 t/y entry tier
- 3 clauses: Annex VII baseline (Physico-Chemical + Toxicological screening + Ecotoxicological screening); Article 12(1)(b) registration content 1-10 t/y range (CSR NOT required); Annex XI data waiving
- Reuses chemicals REACH dossier template with band-specific binding

**chemicals-tonnage-10** — Annex VIII + CSR mandatory (major cost cliff)
- 3 clauses: Annex VIII incremental (sub-acute 28-day RDT + reproductive screening + toxicokinetics basic + short-term fish + activated sludge resp + hydrolysis-vs-pH + adsorption + biodegradation extension); Article 14 CSR mandatory; Article 31(7) Extended SDS (eSDS) with CSR-derived exposure scenarios
- Typical incremental cost: €30-100k CSR + €40-80k 28-day RDT + eSDS distribution coordination

**chemicals-tonnage-100** — Annex IX + sub-chronic + reproductive + long-term ecotox
- 2 clauses: Annex IX incremental (sub-chronic 90-day RDT + reproductive screening OECD TG 421/422 or EOGRTS + long-term Daphnia + fish + soil + sediment + bird ecotox + simulation degradation); Article 40 vertebrate test-proposal mechanism with 45-day public consultation
- Typical incremental cost: €200-500k 90-day RDT + multi-year regulatory timeline

**chemicals-tonnage-1000** — Annex X + chronic + carcinogenicity + EOGRTS (top tier)
- 3 clauses: Annex X incremental (chronic 12-month RDT + 2-year carcinogenicity bioassay TG 451 + EOGRTS TG 443 full Cohort 1A/1B/2A/2B/3 + developmental second species + chronic multi-species ecotox + degradation-product fate); Article 40 vertebrate test proposals; Article 66 reminder that high tonnage increases Annex XIV migration vulnerability per Article 58 prioritisation
- Typical incremental cost: €1.5-3M carcinogenicity + €1-2M EOGRTS + €300-700k chronic RDT + €200-500k chronic ecotox + 3-5 year vertebrate test-proposal timeline. SIEF joint submission essentially mandatory.

No registry additions — all 6 overlays operate against EU REACH already registered at v0.36.0.

Class-overlay count: 38 → 44 (chemicals first class-overlay set).

CI extended (+12 validate steps including 16-module deepest-composite — chemicals + SVHC + Authorisation + tonnage-1000 + 4 adjacent + 8 cross-cutting overlays — beats prior 13-module record).

108/108 pytest pass.

Status counts: 6 `:verified` / 78 `:tested` / 7 `:argued` / 0 `:open` (total 91).

**Tonnage-band semantics.** In practice tonnage bands are mutually exclusive per substance — a registrant uses ONE band at a time, with each higher band supersedes-and-includes lower bands. Open QMS module-union semantics correctly allow either compose-and-validate (16-module composite for documentation purposes) OR adopt-only-current-band (3-module composite chemicals + chemicals-svhc + chemicals-tonnage-10 typical for SMEs at the CSR-mandatory threshold).

**Cumulative chemicals build-out v0.36-v0.38.** 11 chemicals-domain modules shipped across 3 releases: chemicals vertical (v0.36) + 4 adjacent standalones (v0.37) + 6 class overlays (v0.38) — discharges all chemicals-companion forward-work commitments through SVHC + Authorisation + tonnage-banded dossier structure. Per user direction: "do 1 and 2" — both groups now shipped.

---

## v0.37.0 DRAFT — 2026-05-24 — Chemicals-adjacent standalones (OSHA HCS + transport HazMat + EU Biocides + TSCA PFAS)

**1 NEW entry** OQ-106. Spec total 89 → 90. Engine 0.36.0 → 0.37.0.

4 chemicals-adjacent regulatory regimes shipped as cross-cutting overlays, discharging all 4 chemicals-companion (OQ-105) forward-work items:

**osha-hcs — US workplace HazCom (29 CFR 1910.1200; HCS 2024 final rule alignment with UN GHS Rev. 7)**
- 9 clauses: §(e) Written Program; §(f) Labels including workplace + portable + pipe-marking; §(g) SDS access during each shift; §(h) Employee training before assignment + when new hazard introduced; §(i) Trade secrets; Appendix A 10 health hazard classes; Appendix B 17 physical hazard classes; Appendix C label elements + 8 pictograms; Appendix D 16-section SDS content
- New template: `templates/qms-ohs/HAZCOM-WRITTEN-PROGRAM-TEMPLATE.md` (the required §(e)(1) artifact)
- Reuses chemicals SDS template — receiver-side complement to chemicals' sender-side SDS authoring
- Compliance dates: substance mfr/importer 2026-01-19; mixture mfr/importer 2027-07-19

**transport-hazmat — Dangerous-goods transport (DOT HMR 49 CFR 100-185 + IMDG + IATA DGR + ADR 2025 + RID 2025)**
- 17 clauses across 5 modes: DOT HMT classification + shipping papers + marking + labels + placards + emergency-response telephone + four-component HMT training + non-bulk packagings + tank cars; IMDG classification + segregation + DG declaration; IATA state+operator variations + passenger-vs-cargo limits + Shipper's Declaration + CBTA training; ADR/RID classification + tanks + driver vocational training + DGSA appointment
- New templates: `templates/qms-logistics/SHIPPING-PAPER-TEMPLATE.md` (multi-modal Multimodal DG Form per IMO/ILO/UNECE Guidelines) + `templates/qms-logistics/HMT-TRAINING-RECORD-TEMPLATE.md` (multi-regime training record DOT + IATA CBTA + ADR driver + DGSA)
- Standards licensing: DOT + ADR + RID PUBLIC; IMDG + IATA DGR commercial (~USD 200-400 per edition; biennial updates)
- Composes broadly: chemicals primary; automotive (UN3480 Li-ion + UN0503 airbag); aerospace (cryogenics + pyrotechnics); medical-devices (UN3373 Cat B specimens); pharma; manufacturing

**eu-biocides — EU Biocidal Products Regulation (BPR 528/2012; product-on-market authorisation route distinct from REACH)**
- 10 clauses: Articles 4-9 active substance approval; Articles 17-23 product authorisation pathways (national/MR-parallel/MR-sequence/Union/simplified); Article 19(1) conditions; Articles 49-50 + Article 95 supplier list; Article 56 R&D exemption; Article 58 treated articles; Articles 69-72 biocide-specific C+L+P additions over CLP; Annex V 22 product types in 4 groups (disinfectants PT 1-5, preservatives PT 6-13, pest control PT 14-20, other PT 21-22); Annex VI Common Principles
- New template: `templates/product-chemicals/biocides/BPR-AUTHORISATION-APPLICATION-TEMPLATE.md` (Article 17 full application with pathway selection + Article 95 verification + Article 19(1) conditions check + efficacy + HHRA + ERA dossier framework + Article 69 label additions + Annex dossier index)
- Critical adopter-cost gotcha: Article 95 supplier list — biocidal products containing active substances whose supplier is not Article-95-listed cannot be placed on EU market post-2015-09-01

**tsca-pfas — US EPA TSCA Section 8(a)(7) PFAS Reporting (40 CFR Part 705; final rule October 2023)**
- 7 clauses: §705.3 applicability (no de minimis, no exemption for substances in commerce, no exemption for impurities + byproducts, articles in scope per "knowability" standard); §705.15 submission window 2025-07-11 to 2026-01-11 standard / 2026-07-11 small-mfr-article-only (EPA may extend further); §705.20-30 per-substance per-year per-site for 11-year 2011-2022 lookback; §705.25 5-year retention; §705.35 CBI claims per §703.5; §705.40 CDX/CISS submission; preamble "knowability" standard for article importers
- New template: `templates/product-chemicals/pfas/PFAS-REPORTING-FORM-TEMPLATE.md` (full per-substance per-year per-site data structure + CBI/non-CBI dual-version + article-importer due-diligence record with common-categories checklist catching non-obvious PFAS imports across textile / semiconductor / cookware / cosmetics / automotive / medical-device / outdoor-gear / aerospace verticals)
- Critical scope-creep: importer-of-record is reporter; affiliated-entity consolidation typically required at parent level; ~1,400+ substances meet broad PFAS structural definition per §705.5(b)

Registry +9 standards:
- 29 CFR 1910.1200 (OSHA HCS; PUBLIC)
- 49 CFR 100-185 (US DOT HMR; PUBLIC)
- IMDG Code (Amendment 42-24 mandatory 2026-01-01; commercial)
- IATA DGR 66th Edition (effective 2026-01-01; commercial)
- ADR 2025 (PUBLIC)
- RID 2025 (PUBLIC)
- EU BPR (Regulation 528/2012; PUBLIC)
- 40 CFR 705 (TSCA PFAS Reporting; PUBLIC)

Cross-cutting overlay count: 19 → 23.

CI extended (+12 validate steps):
- 4 standalone validates (osha-hcs, transport-hazmat, eu-biocides, tsca-pfas)
- 4 chemicals + adjacent pairs
- chemicals + all 4 adjacent composite
- automotive + transport-hazmat + tsca-pfas (cross-vertical applicability)
- pharma + osha-hcs + transport-hazmat
- **13-module deepest-composite** (new depth record): chemicals + 4 adjacent + 8 cross-cutting overlays — realistic shape for a US-and-EU specialty-chemicals manufacturer with full IMS + DG transport + workplace HazCom + biocide product line + TSCA PFAS reporting obligation

108/108 pytest pass.

Status counts: 6 `:verified` / 77 `:tested` / 7 `:argued` / 0 `:open` (total 90).

Per user direction: "do 1 and 2" (group 1 chemicals-adjacent standalones + group 2 chemicals class overlays). This release ships group 1; group 2 ships at v0.38.0.

---

## v0.36.0 DRAFT — 2026-05-24 — Chemicals vertical (7th vertical)

**1 NEW entry** OQ-105. Spec total 88 → 89. Engine 0.35.0 → 0.36.0.

7th Open QMS vertical (after medical-devices / aerospace / automotive / manufacturing / pharma / food-safety) covering chemical substance + mixture manufacturing + import across EU and US regulatory regimes. 21 clauses across 5 standards spanning the four major chemical-industry regulatory regimes: EU REACH (no-data-no-market + tonnage-banded technical dossier + CSR for ≥10 t/y + SDS + supply-chain SVHC communication + downstream-user obligations + Authorisation + Restriction); EU CLP (self-classification + C&L Inventory notification + label content + Annex VI CLH + UFI + Poison Centre Notification); UN GHS Rev. 10 (hazard classification + 16-section SDS format + label elements); OECD GLP Principles (facility organisation + QA Programme + SOPs + study conduct + reporting + archive); US TSCA (PMN for new chemicals + risk evaluation + CDR every 4 years + import/export).

4 new chemicals-specific templates:
- **Safety Data Sheet** — 16-section per GHS Rev. 10 + REACH Annex II + CLP + OSHA HCS Appendix D. Foundational risk-communication artifact across all chemical-product distribution.
- **REACH Registration Dossier Outline** — Articles 5-6 + 10 + 14 + Annexes VI-X tonnage-banded technical dossier + Annex I CSR for ≥10 t/y. Covers SIEF joint submission + IUCLID 6 dossier preparation + REACH-IT submission + post-submission update obligations + Authorisation / Restriction considerations.
- **CLP Classification Notification + Label** — full classification tables across all GHS hazard classes (physical / health / environmental) + EUH supplementary statements + Annex VI CLH harmonised classification + UFI + Poison Centre Notification per Annex VIII.
- **GLP Study Plan + Final Report** — combined per Principles 8.1 + 9.1. QA Programme Statement per Principle 9.1(j). Archive per Principle 9.2 (minimum 10-year retention typical for chemical industry).

Plus 2 cross-cutting bindings (quality-policy + SOP-TEMPLATE) addressing REACH no-data-no-market and TSCA operational SOPs (PMN procedures + CDR reporting + downstream-user communication + import/export per Section 12-13).

Registry +5 standards (all PUBLIC license — meaningful adopter cost reduction for chemical-industry startups + SMEs + academic spinouts):
- EU REACH (Regulation (EC) 1907/2006)
- EU CLP (Regulation (EC) 1272/2008)
- UN GHS Rev. 10 (2023)
- OECD GLP Principles (ENV/MC/CHEM(98)17)
- US TSCA (15 USC §2601; 40 CFR Parts 700-799)

New example bundle `example-specialty-chemical` (mid-size 50-100 t/y SVHC-adjacent intermediate manufacturer with REACH + TSCA scope composing chemicals + iso-27001 + iso-14001 + iso-45001 + iso-31000). Baseline matrix committed; idempotent regenerate verified.

CI extended (+5 validate steps + 1 regenerate dry-run):
- `openqms validate --module chemicals`
- `openqms validate --module chemicals --module iso-27001`
- `openqms validate --module chemicals --module iso-14001 --module iso-45001`
- `openqms validate --module chemicals --module iso-14001 --module iso-45001 --module iso-50001 --module iso-27001 --module regulated-ai`
- Chemicals full-IMS deepest-composite: `--module chemicals --module iso-27001 --module regulated-ai --module iso-14001 --module iso-45001 --module iso-50001 --module iso-37001 --module iso-22301 --module iso-31000`

108/108 pytest pass.

**Out of scope (deferred):** OSHA HCS 29 CFR 1910.1200 (US workplace HazCom — workplace H&S overlap partially covered by iso-45001 overlay); DOT HazMat 49 CFR Parts 100-185 + IMDG + IATA + ADR/RID (transport classifications — forward standalone overlay); pesticides (FIFRA + EU Plant Protection Products Regulation 1107/2009 — separate regulatory framework); cosmetics (EU 1223/2009 + US MoCRA — separate vertical); biocides (EU 528/2012); detergents (EU 648/2004).

Annex SL composability: REACH/CLP/GHS aren't Annex-SL but compose seamlessly with all 9 Annex-SL cross-cutting overlays via the module-union primitive (OQ-011). OECD GLP cleanly layers on as a quality-system-for-non-clinical-safety-studies discipline.

Status counts: 6 `:verified` / 76 `:tested` / 7 `:argued` / 0 `:open` (total 89). Vertical count: 6 → 7.

Per user direction: "do chemicals, save rest of verticals for future work." Other candidate verticals (cosmetics / pesticides / nuclear / oil-and-gas / construction / textiles / mining / electrical-equipment) deferred to future work.

---

## v0.25.0 – v0.35.0 DRAFT — 2026-05-24 — Catch-up note (11 releases consolidated)

Per-version changelog entries for v0.25.0 through v0.35.0 were not back-filled here in real time as the releases shipped; the omnibus companion `BUSINESS/companion_v0_24_to_34_omnibus.md` covers v0.24.0–v0.34.0 in narrative form, and `docs/modules-catalog.md` reflects the current module + template inventory. v0.35.0 added the omnibus companion + catalog refresh + README scope-summary update.

Cumulative across these 11 releases:
- 5 new spec entries (OQ-100 per-module READMEs Gap; OQ-101 pharma class overlay batch; OQ-102 food-safety class overlay batch; OQ-103 aerospace+automotive extension + IVDR class overlay batch; OQ-104 cross-cutting overlay batch IS+governance+compliance+resilience+DoD-CUI).
- Vertical count unchanged: 6 (medical-devices / aerospace / automotive / manufacturing / pharma / food-safety).
- Class-overlay count: 21 → 37 (added 5 pharma + 5 food-safety + 4 aerospace/automotive extension + 2 IVDR class overlays).
- Cross-cutting overlay count: 7 → 19 (added soc-2 + pci-dss + hitrust-csf + nist-csf + iso-31000 + iso-37301 + dora + eu-gpsr + tisax + defense-cui + cmmc).
- Spec total: 83 → 88. Status counts: 6 `:verified` / 75 `:tested` / 7 `:argued` / 0 `:open`.

Per-version detail is reconstructable from `git log` of the v0.25.0..v0.35.0 commit range; see `companion_v0_24_to_34_omnibus.md` for narrative.

---

## v0.24.0 DRAFT — 2026-05-24 — Cross-vertical recall-workflow overlay

**1 NEW entry** OQ-098. Spec total 81 → 82. Engine 0.23.0 → 0.24.0.

Cross-vertical recall-workflow overlay covering four regulatory frameworks: NHTSA Part 573/577/579 (automotive) + FDA 21 CFR 7/806 (medical-device corrections + removals + general FDA recall) + CPSIA §15 (consumer products). 11 clauses + 2 new templates.

**Architectural decision:** shipped as a cross-cutting overlay rather than four separate per-vertical class overlays because the recall procedure SHAPE is essentially the same across all four frameworks (decision flow with single Recall Coordinator; multi-functional team activation; distribution-list extraction; classification; regulator notification within framework-specific window; customer/owner notification; effectiveness checks; recovery + disposition; root cause + CAPA; closure). Only the classification scheme + notification windows + notification content differ across frameworks — and these are parametrized in the Generalized Recall Procedure template.

Registry +6 standards (all PUBLIC license — US federal regulations + statutes):
- 49 CFR 573 (Defect and Noncompliance Reports — NHTSA)
- 49 CFR 577 (Owner Notification)
- 49 CFR 579 (TREAD Act Early Warning Reporting)
- 21 CFR 7 (FDA general recall policy + classification + effectiveness checks)
- 21 CFR 806 (Medical Device Reports of Corrections and Removals)
- CPSIA §15 (15 USC §2064 — Substantial Product Hazard reports + recalls)

2 new templates:

- **GENERALIZED-RECALL-PROCEDURE-TEMPLATE** — cross-vertical recall procedure with framework-specific table covering classification scheme (NHTSA: safety-related defect or FMVSS noncompliance — no I/II/III subcategorization; FDA medical/pharma/food: Class I/II/III; CPSC: substantial product hazard — one tier) + regulator notification window (NHTSA 5 working days; FDA medical device 10 working days; FDA pharma 3 working days for Field Alert; FDA food 24 hours for Reportable Food Registry per 21 USC §350f; CPSC 24 hours per §15(b)) + notification content (NHTSA §577.5 10 elements; FDA medical §806.10 specifics; etc.). Includes 24/7 cross-vertical Recall Team with 11 roles; hour-0 + hour-1-24 + hour-24-168 + hour-168+ action sequences; mock-recall annual cadence.

- **NHTSA-OWNER-NOTIFICATION-TEMPLATE** — automotive-specific 49 CFR Part 577 owner notification letter with all 10 §577.5 mandatory elements (manufacturer + product identification; defect/noncompliance description; risk to motor vehicle safety in vehicle-owner-comprehensible language; warning against continued use + interim safe-operation instructions; remedy description + availability; no-charge remedy statement; instructions + NHTSA complaint procedure; recall campaign number; provisions if not original purchaser; lessor notice to lessees per §577.5(h)). Also includes §577.7 timing (60 days from DIR submission); §577.8 second notification trigger at < 70% completion at 6 months; §577.9 reimbursement for pre-notification remedy charges.

Validates as:
- recall-workflow standalone
- automotive + recall-workflow
- medical-devices + recall-workflow
- manufacturing + recall-workflow (consumer-products under CPSIA)
- food-safety + recall-workflow (extends food-safety's existing internal recall template)

**10-module composite validates** (new depth record): `automotive + automotive-asil-d + automotive-cal-4 + recall-workflow + regulated-ai + iso-27001 + iso-14001 + iso-45001 + iso-50001 + iso-22301`. Realistic shape for a top-rigor connected automotive ECU manufacturer with full recall discipline + integrated management system.

CI workflow extended (+6 validate steps).

Test count unchanged at 108. Overlay + templates are content.

Forward work:
- EU Article 19 General Product Safety Regulation 2023/988 standalone overlay
- FDA pharma Field Alert Report 21 CFR 314.81 dedicated workflow
- Product-liability insurance claim coordination workflow
- Class-action litigation hold integration

---

## v0.23.0 DRAFT — 2026-05-23 — Public adopter-surface release

**Closes P10 from original priority stack.** 1 NEW entry OQ-097. Spec total 80 → 81. Engine 0.22.0 → 0.23.0.

Pure consolidation release — no new module-tier entries, no new templates, no engine code changes. The build had run substantially ahead of public discoverability for many releases; v0.23.0 closes that gap.

### What changed

**README.md** — rewritten from v0.7.0-era state to current v0.22.0+ state:
- Top-level scope-summary table (6 verticals + 22 class overlays + 7 cross-cutting overlays + 63 standards + 20 jurisdictions + 57 templates + 11 example bundles + 81 spec entries)
- Verticals catalog table with module IDs + primary standards + class overlays per vertical
- Cross-cutting overlays catalog with when-to-use guidance
- Quick-start with vertical-pick + composition workflow
- Per-audience adoption guidance ("If your organization makes X...")
- Architecture diagram updated to reflect current layout (modules/ subdivided by vertical; cross-cutting overlays; product-pharma/ + product-atmp/ template trees)
- 9-module composite reference (deepest tested in CI)
- Standards-licensing inventory split by public vs. commercial (notable: pharma + atmp verticals are all-public-license)
- Status (v0.22.0): 6 `:verified` / 67 `:tested` / 7 `:argued` / 0 `:open` (total 80) — pre-this-release counts; this release adds OQ-097 → 81

**docs/modules-catalog.md** — NEW. Comprehensive per-module catalog:
- Three module-type taxonomy (verticals / class overlays / cross-cutting overlays)
- Per-vertical entry with module ID + standards + license mix + compatible class overlays + example bundle + module README link
- Class overlay tables per vertical (medical 7; aerospace 5 DALs; automotive 9 ASIL+CAL; pharma 1 ATMP)
- Cross-cutting overlay entries with when-to-use guidance
- Example bundles table (11 entries) with vertical + cross-cutting composition shown
- Composition examples — smallest viable scaffold through 9-module deepest composite
- Decision flow ("1. Pick vertical / 2. Add class overlay / 3. Compose cross-cutting overlays / 4. Define bundle / 5. Validate / 6. Adopt templates")

**modules/food-safety/README.md** — NEW. Documents the 6th vertical (was missing).

**modules/atmp/README.md** — NEW. Documents the ATMP class overlay (was missing).

**.gitignore** — `BUSINESS/` removed. All spec discipline now publicly readable:
- ENGINE_SPEC.md (81 spec entries with logic tiers + evidence types + status)
- DESIGN.md (architectural narrative)
- artifact_registry.md (S-ID → evidence file mapping)
- dashboard.md (status summary + priority stack)
- changelog.md (this file)
- 13 companion docs (per-session computational basis + verification records back to v0.2.0)

The publication makes existing claims publicly auditable — the publication itself is not a new claim about Open QMS capabilities.

### Spec transitions

- **OQ-097** NEW `:tested`. Tier: Gap. Evidence type: example-tested. Depends_on: none.

### Why closing P10 now

P10 (Public release of BUSINESS/ contents) was on the dashboard priority stack from v0.1.0 (the BUSINESS/ baseline). The user-stated condition was "things being further along" — the platform now has 6 verticals + 22 class overlays + 7 cross-cutting overlays + 9-module composite validation, which clearly meets that bar.

### Engine version

0.22.0 → 0.23.0. No engine code change; documentation + gitignore consolidation.

### Public commit

`<sha>` (this commit) — includes README rewrite + modules-catalog.md + food-safety/atmp READMEs + .gitignore edit + BUSINESS/ contents (newly public) + engine version bump in one commit.

---

## v0.22.0 DRAFT — 2026-05-23 — ATMP class overlay (cell + gene therapy)

**1 NEW entry** OQ-096. Spec total 79 → 80. Engine 0.21.0 → 0.22.0. Public commit `2efc102`.

**First pharma class overlay; most-stringent biologics scope.** Covers autologous + allogeneic cell therapies (CAR-T, iPSC-derived), gene therapies (AAV + lentiviral + retroviral), ex vivo gene-modified HSCT, oncolytic viruses. All cited standards PUBLIC license (same character as parent pharma vertical).

10 clauses across 4 standards (EU GMP Annex 2A + 2B + 21 CFR 1271 + ICH Q5A(R2) 2023). Most distinguishing requirements beyond baseline pharma:

- **Donor eligibility** unique to cell-based ATMPs (21 CFR 1271 Subpart C / EU Directive 2004/23/EC) — RCDA screening + testing
- **Bidirectional donor → product → recipient traceability with EXTREME retention**: 30 years EU per Directive 2004/23/EC Art. 8; 10 years US per 21 CFR 1271.270 — outlasts most operational systems → format-stability planning required
- **Aseptic processing throughout** — ATMPs typically cannot be terminally sterilized; closed-system processing preferred per Annex 2A
- **OOS handling for autologous** — cannot easily reject because patient typically already conditioned (lymphodepleted); risk-based release with clinical decision in collaboration with treating physician
- **Viral safety per ICH Q5A(R2) 2023** — explicitly extended to viral vector products with vector-specific RCV testing (RCL/RCA/RCAAV)

3 new ATMP-specific templates:

- **Donor Eligibility Assessment** — full RCDA panel (HIV-1/2, HBV, HCV, HTLV-1/2, T. pallidum, T. cruzi, WNV, Zika, reproductive Chlamydia + Gonorrhea, EU-additional Malaria) + specimen-window compliance per §1271.80(b) + exception handling per §1271.65 with required labeling + recipient informed consent. **PHI compartmentalization required** — template captures determination + non-PHI traceability; full identifiable record in separate access-restricted system per HIPAA + GDPR Special Category data.

- **Tissue/Cell Traceability Record** — bidirectional chain with forward (donor → recipient — for recipient AE investigation) + reverse (recipient → donor — for donor-source-related AE affecting multiple recipients) + recall scope queries. EU Single European Code per Directive 2015/565. Format + media stability planning for 30-year EU retention (PDF/A + CSV + XML; periodic format migration with checksums; vendor independence; multi-person knowledge; organizational-change contractual transfer; encryption-key escrow).

- **Viral Safety Evaluation Report** — Q5A(R2) three-pillar framework. MCB/WCB/EPC characterization per species-specific virus panel + raw material viral risk per CHMP/410/01 (bovine TSE/BSE) + porcine circo+parvovirus + murine MAP + human full RCDA. Viral clearance studies with model-virus panel (pseudorabies + X-MuLV + Reo3 + MVM as enveloped large/medium + non-enveloped medium/small) with cumulative LRF ≥ worst-case potential viral load. Vector products: RCV testing strategy alongside vector characterization (titer, purity, capsid-protein ratios for AAV, RCL/RCA/RCAAV per category).

Registry +4 standards: EU GMP Annex 2A, EU GMP Annex 2B, 21 CFR 1271, ICH Q5A(R2). All PUBLIC license.

New `bundles/example-cart.yaml` — autologous CD19-targeted CAR-T at US+EU dual-licensed site composing pharma + atmp + iso-27001 + iso-14001 + iso-45001 + iso-50001 across 16 standards.

CI +2 validate steps (pharma + atmp standalone; 9-module deepest composite) + 1 regenerate dry-run.

**9-module deepest composite validates**: pharma + atmp + iso-27001 + regulated-ai + iso-14001 + iso-45001 + iso-50001 + iso-37001 + iso-22301. This is the deepest composition tested in project history. Represents the realistic shape for a commercial-stage cell therapy organization pursuing fully-integrated management system certification (PQS + ATMP-specific GMP + IS + AI governance + EMS + OHSMS + EnMS + ABMS + BCMS).

Forward work:
- Reproductive tissue / gametes specific overlay (21 CFR 1271 reproductive-tissue-specific subprovisions)
- HCT/P that is NOT an ATMP overlay (different regulatory pathway — no IND/BLA)
- Veterinary ATMP overlay
- In situ gene editing overlay (CRISPR direct administration without ex vivo cell processing)
- Site Master File template for ATMPs
- Comparability protocol template (ICH Q5E — particularly critical for autologous ATMPs without reference standard)
- CAR-T-specific release-testing template
- AAV-specific empty/full capsid ratio + dose-determination template

---

## v0.21.0 DRAFT — 2026-05-23 — Governance + resilience cross-cutting overlays

**Cross-cutting overlay set complete.** 2 NEW entries: OQ-094 ISO 37001:2016 anti-bribery + OQ-095 ISO 22301:2019 BCMS. Spec total grows 77 → 79. Engine 0.20.0 → 0.21.0. Public commit `ee215d7`.

Both overlays share Annex SL structure → compose cleanly with every vertical and every other cross-cutting overlay.

ISO 37001 ABMS — 14 clauses: governing-body responsibility (§5.1.2); anti-bribery policy (§5.2); INDEPENDENT compliance function (§5.3.2); ABMS risks + opportunities (§6.1); personnel DD for elevated-risk roles (§7.2.2.2); awareness + training (§7.3); risk-proportionate transaction/project/business-associate DD (§8.2); financial controls (§8.3); non-financial controls (§8.4); controls cascaded to controlled orgs + business associates (§8.5); gifts/hospitality/donations (§8.7); whistleblowing with non-retaliation (§8.9); investigations (§8.10); compliance-function review (§9.4). New template: Anti-Bribery Due Diligence Assessment with Low/Medium/High/Prohibited risk-tier framework + sanctions/PEP/adverse-media/UBO screening + contractual-safeguards checklist.

ISO 22301 BCMS — 13 clauses: BC policy (§5.2); BCMS risks (§6.1); BC objectives (§6.2); Business Impact Analysis with RTO/MAO/MBCO/RPO (§8.2.2); BC risk assessment (§8.2.3); BC strategies + solutions covering people+ICT+infrastructure+supplies+partners+financial (§8.4); BC plans (§8.5); exercise programme — tabletop annual + technical annual + live activation biennial (§8.6); evaluation (§8.7); monitoring + measurement (§9.1); internal audit (§9.2); mgmt review (§9.3); NC + CA (§10.2). New template: Business Continuity Plan with 8 disruption scenarios + crisis management team with 24/7 contacts + communications matrix with regulatory reporting windows + exercise cadence.

**8-module ultimate composite validates** (deepest tested): pharma + iso-27001 + regulated-ai + iso-14001 + iso-45001 + iso-50001 + iso-37001 + iso-22301 — realistic IMS-pursuing pharma shape (PQS + IS + AI governance + EMS + OHSMS + EnMS + ABMS + BCMS).

Registry +2 standards. CI +6 validate steps. Test count unchanged at 108.

---

## v0.20.0 DRAFT — 2026-05-23 — Food safety vertical (6th vertical)

**1 NEW entry** OQ-093 food-safety. Spec total 76 → 77. Engine 0.19.0 → 0.20.0. Public commit `ca6e69b`.

Covers human-food manufacturing under ISO 22000 FSMS + Codex HACCP + US FSMA Preventive Controls + FSSC 22000 v6 (GFSI-benchmarked scheme). 16 clauses across 5 standards (Codex + 21 CFR 117 + 21 CFR 123 are PUBLIC; ISO 22000 + FSSC commercial). 3 new food-safety-specific templates:

- **HACCP Plan** — Codex + ISO 22000 §8.5 + 21 CFR 117 Subpart C + 21 CFR 123. B/C/P/A hazards (biological + chemical + physical + allergens per FALCPA + FASTER Act + EU FIC). CCP determination via Codex decision tree. PCQI designation per FSMA §117.180.
- **Prerequisite Programs** — ISO/TS 22002 15-element index (construction + layout + utilities + waste + equipment + materials + cross-contamination + cleaning per zone 1-4 + pest control + personnel hygiene + rework + recall + warehousing + product information + food defense). Allergen management with changeover validation. FSVP cross-reference (21 CFR 1 Subpart L). Food defense vulnerability assessment per 21 CFR 121.
- **Recall + Withdrawal Procedure** — 21 CFR 117 Subpart D + 21 CFR 7 + Codex §5.7 + ISO 22000 §8.9. FDA Class I/II/III classification, 24/7 CMT, hour-0 decision flow, <4-hour distribution-list extraction, 24h regulatory notification incl. Reportable Food Registry per 21 USC §350f, effectiveness checks per FDA levels A/B/C, mock-recall annual cadence.

Registry +5 standards + 4 jurisdictions (FDA-Food, USDA-FSIS, EFSA, CFIA). New `bundles/example-food-processor.yaml` (mid-size RTE chilled-foods processor composing food-safety + iso-14001 + iso-45001 + iso-50001).

Forward work: USDA meat+poultry HACCP overlay (9 CFR 416+417); FSMA Animal Food overlay (21 CFR 507); Produce Safety overlay (21 CFR 112); BRCGS/SQF/IFS GFSI schemes; Intentional Adulteration standalone (21 CFR 121); FSVP standalone (21 CFR 1 Subpart L); class overlays for LACF / acidified / infant formula; dietary supplements vertical (21 CFR 111 DSHEA).

---

## v0.19.0 DRAFT — 2026-05-23 — Pharma vertical (5th vertical; largest remaining regulated-industry gap)

**1 NEW entry** OQ-092 pharma. Spec total 75 → 76. Engine 0.18.0 → 0.19.0. Public commit `a98854e`.

Covers both Active Pharmaceutical Ingredient (drug substance) + Drug Product (finished pharmaceutical form). Small-molecule + large-molecule + sterile + non-sterile manufacturing under FDA + EMA + MHRA + WHO PQ regulatory frameworks. 23 clauses across 8 standards spanning 4 discipline tracks:

- **PQS substrate** — ICH Q10 (§3.2.1 management responsibility, §3.2.2 integrated PQS elements, §3.2.4 Stage 3 CPV); ICH Q9(R1) Quality Risk Management.
- **API GMP** — ICH Q7 §2 quality management + §8 production + §12 validation.
- **US cGMP** — 21 CFR 211 Subparts B (organization + QCU independence per §211.22) + D (equipment) + E (components + containers) + F (production + process controls) + G (packaging + labeling) + I (laboratory controls) + J (records + reports including APQR per §211.180(e)).
- **EU GMP** — EudraLex Vol. 4 Ch. 1 (PQS + §1.10 PQR mandatory annually with QP), Ch. 2 (QP per Article 51 of Directive 2001/83/EC), Ch. 6 (QC + OOS §6.34), Annex 15 (qualification + validation), Annex 16 (QP certification + batch release).
- **Sterile manufacturing** — PIC/S Annex 1 (2022 revision) Contamination Control Strategy (§2 + §8), Aseptic Process Simulation (§9.40-§9.50), EM + cleanroom classification A/B/C/D (§9 + §9.27).
- **Electronic records + signatures** — 21 CFR Part 11 for pharma computerized systems.

6 new pharma-specific templates:

- **Master Batch Record** (21 CFR 211.186 + EU GMP Part I Ch. 4) — MBR is the spec; executed BR is the evidence.
- **Validation Master Plan** (ICH Q9+Q10 + EU GMP Annex 15 + FDA PV 2011) — site-level navigation across IQ/OQ/PQ + cleaning + process (Stage 1/2/3) + AMV per ICH Q2(R1) + CSV per GAMP 5.
- **Deviation Report** (21 CFR 211.100+192 + EU GMP Ch. 1 §1.4(xiv) + ICH Q10 §3.2.2.2) — Critical/Major/Minor categorization with QA-assignment criteria. Distinct from NCR — covers procedural departures regardless of conformance outcome. FDA Field Alert trigger per 21 CFR 314.81.
- **Change Control** (ICH Q10 §3.2.3 + EU GMP Ch. 1 §1.4(xiv) + 21 CFR 211.100) — QA-gated planned change with regulatory-impact assessment for FDA/EMA/MHRA/HC/PMDA submissions.
- **OOS Investigation** (FDA OOS Guidance 2006 + 21 CFR 211.192 + EU GMP Ch. 6 §6.34) — Phase 1 lab investigation (24-48 hours, no retesting) + Phase 2 full-scale investigation (30 days, multi-functional, retesting only with documented protocol).
- **Annual Product Quality Review** (21 CFR 211.180(e) + EU GMP Ch. 1 §1.10) — annual per-product trend aggregation with Cpk/Ppk + QP review in EU.

Registry +7 standards (all PUBLIC — **first vertical where most cited standards are public license**) + 3 jurisdictions (EMA, MHRA, WHO-PQ); FDA jurisdiction extended with pharma standards.

New `bundles/example-drug-product.yaml` — sterile small-volume parenteral (SVP injection) at US+EU dual-licensed site, composing pharma + all 5 HSE+IS overlays.

Validates as combination-product composite with medical-devices (per 21 CFR Part 4).

Forward work: ATMP (Annex 2A+2B + 21 CFR 1271 + ICH Q5A(R2)); radiopharma (Annex 3 + USP <823>); veterinary; IMP (Annex 13); generic/biosimilar; Site Master File template; Batch CoA template; Stability Protocol (ICH Q1A(R2)); sterile vs. non-sterile + biologics vs. small-molecule + commercial vs. clinical-stage class overlays.

---

## v0.18.0 DRAFT — 2026-05-23

**HSE + energy cross-cutting overlays — ISO 14001 + ISO 45001 + ISO 50001.**

**3 NEW spec entries** (OQ-089, OQ-090, OQ-091); spec total grows 72 → 75. Engine package version 0.17.0 → 0.18.0.

### Why ship the three together

ISO 14001 (environmental) + ISO 45001 (OH&S) + ISO 50001 (energy) form the EHS-and-energy block that most mid-size manufacturers want to integrate into a single sustainability + safety management system. All three follow the Annex SL high-level structure (the same structure ISO 9001 / ISO 27001 / ISO 42001 use), so composition is structurally clean. Shipping them in one release lets adopters compose any subset against any vertical immediately.

### Module — ISO 14001 environmental management overlay (commit `ef13f46`)

**`modules/iso-14001/`** — 11 clauses encoding the substantive ISO 14001:2015 additions over the Annex SL baseline:

- §4.2 interested parties (env-relevant: regulators, communities, customers, NGOs).
- §5.2 environmental policy with commitments to protection of environment (incl. prevention of pollution + sustainable resource use + climate change mitigation/adaptation + biodiversity), fulfillment of compliance obligations, continual improvement.
- **§6.1.2 environmental aspects** — the defining EMS artifact. Lifecycle-perspective identification of aspects of activities/products/services; impact determination; significance criteria flagging Significant Environmental Aspects (SEAs).
- §6.1.3 compliance obligations.
- §6.1.4 planning action.
- §6.2 environmental objectives.
- §7.4 communication (incl. external comms required by compliance obligations).
- §8.1 operational control of SEAs with lifecycle perspective in design + procurement + outsourced processes.
- §8.2 emergency preparedness + response with periodic test.
- §9.1.2 evaluation of compliance.
- §10.2 nonconformity + corrective action (incl. mitigating adverse environmental impacts).

**`templates/qms-environmental/ENVIRONMENTAL-ASPECTS-REGISTER-TEMPLATE.md`** — new template covering §6.1.2 + §6.1.3 + §8.1 + §8.2 cross-references. Per-aspect impact identification with Severity × Frequency × Regulatory × Stakeholder × Reversibility scoring → SEA determination → operational controls per §8.1 + emergency procedures per §8.2 + compliance-obligations cross-reference per §6.1.3. Lifecycle perspective explicit. Typical aspect categories enumerated (air emissions, water + land discharges, raw materials + energy use, energy emitted, waste generation, physical attributes).

### Module — ISO 45001 OH&S management overlay (commit `ef13f46`)

**`modules/iso-45001/`** — 11 clauses encoding the substantive ISO 45001:2018 additions:

- §4.2 interested parties (workers + their representatives, contractors, communities, families of workers).
- §5.2 OH&S policy with commitments to safe + healthy working conditions for prevention of work-related injury + ill-health, elimination of hazards + reduction of OH&S risks, worker consultation + participation.
- **§5.4 consultation + participation of workers** — THE foundational OHSMS requirement that has no analog in ISO 9001 / 14001 / 27001 / 42001 / 50001. Non-managerial workers + their reps consulted + participating in development + planning + implementation + evaluation + improvement. Mechanisms + time + training + barrier removal required.
- **§6.1.2 hazard identification + risk assessment + opportunities** — ongoing + proactive; routine + non-routine; psychosocial factors explicitly required.
- §6.1.3 legal + other requirements.
- §6.1.4 planning action.
- §7.3 awareness (incl. right to remove self from imminent danger + protection from undue consequences for doing so).
- **§8.1.2 eliminating hazards + reducing OH&S risks via hierarchy of controls** — elimination > substitution > engineering > administrative > PPE. PPE is the last resort, not the default.
- §8.1.3 management of change.
- §8.1.4 procurement (incl. contractor coordination).
- §8.2 emergency preparedness + response.
- §10.2 incident + nonconformity + corrective action with worker participation in evaluation + root-cause analysis.

**`templates/qms-ohs/HAZARD-IDENTIFICATION-RISK-ASSESSMENT-TEMPLATE.md`** — new template covering §6.1.2 with worker consultation per §5.4 as a precondition (not afterthought). Hazard register with S × L matrix + acceptability criterion + hierarchy-of-controls action per §8.1.2 + residual risk + cross-references to §6.1.3 legal + §8.1.3 MoC + §8.1.4 procurement + §8.2 emergency. Typical hazard categories enumerated (physical, chemical, biological, ergonomic, **psychosocial**, environmental, organizational). Frontmatter includes a required `worker_consultation:` field per §5.4 — surfacing the standard's unique requirement at the document boundary.

### Module — ISO 50001 energy management overlay (commit `ef13f46`)

**`modules/iso-50001/`** — 10 clauses encoding the substantive ISO 50001:2018 additions:

- §5.2 energy policy with commitments to procurement of energy-efficient products/services + design for energy performance + continual improvement of energy performance + the EnMS.
- **§6.3 energy review** — analyze use + consumption; identify Significant Energy Uses (SEUs); determine current performance of facilities + equipment + systems + processes + personnel affecting SEUs; identify + prioritize + record improvement opportunities. The analytical foundation of the EnMS.
- **§6.4 energy performance indicators (EnPIs)** — methodology + values + reviews + comparison to baselines documented.
- **§6.5 energy baseline (EnB)** — calculated from energy review; revised on EnPI-no-longer-reflects, static-factor change, operations change. **ISO 50001 is unique among the management-system standards in mandating a quantitative, calculated, periodically-recalibrated performance baseline.**
- §6.6 planning for collection of energy data (key characteristics, relevant variables, operational criteria, static factors).
- §8.1 operational control of SEUs (criteria for effective operation + maintenance; absence of which could lead to significant deviation from effective energy performance).
- §8.2 design (energy performance improvement opportunities + operational control in design of facilities/equipment/systems/processes with significant impact).
- §8.3 procurement of energy services + products + equipment + energy itself (with energy-performance criteria; suppliers informed; specifications for purchased energy).
- §9.1.1 monitoring + measurement + analysis + evaluation (incl. investigation + response to significant deviations from expected energy consumption).
- §10.2 nonconformity + corrective action.

**`templates/qms-energy/ENERGY-REVIEW-AND-ENPI-BASELINE-TEMPLATE.md`** — new template combining §6.3 + §6.4 + §6.5 + §6.6. Most quantitative artifact in Open QMS to date, matching ISO 50001's unique character. Per-SEU performance basis + improvement opportunity with payback; per-EnPI formula + numerator + denominator + normalization model; per-EnB calculation method + recalibration triggers; data collection plan; operational + procurement implications. Adopters must produce real numbers (energy intensity in MWh-equiv / tonne, chiller efficiency in kW/ton, etc.) — not just process discipline.

### Composition validation

All 3 overlays validate standalone:
- iso-14001 standalone → invariant_holds: True
- iso-45001 standalone → True
- iso-50001 standalone → True

Each overlay × each of 4 verticals — 12 composites validated:
- medical-devices + each — 3/3 pass
- aerospace + each — 3/3 pass
- automotive + each — 3/3 pass
- manufacturing + each — 3/3 pass

**6-module everything-shop composite** validates:
`manufacturing + iso-14001 + iso-45001 + iso-50001 + iso-27001 + regulated-ai`

This represents the realistic shape of a small-to-mid manufacturer pursuing full management-system integration: ISO 9001 QMS substrate + environmental + OH&S + energy + information security + AI governance. Composes cleanly under the OQ-011 compose primitive (built in medical-devices context at v0.4.0, unchanged).

### CI — engine-tests.yml extension

8 new validate steps:
- 3 standalone (iso-14001, iso-45001, iso-50001)
- 4 cross-vertical composites (medical-devices + 14001 + 45001; aerospace + 14001 + 45001; automotive + 14001 + 45001 + 50001; manufacturing + 14001 + 45001 + 50001)
- 1 full-stack mega-composite (manufacturing + all 5 cross-cutting management-system overlays)

### Spec, registry, dashboard transitions

- **OQ-089** NEW `:tested` (ISO 14001 environmental management cross-cutting overlay). Module / example-tested. Depends_on: OQ-011, OQ-012, OQ-014.
- **OQ-090** NEW `:tested` (ISO 45001 OH&S management cross-cutting overlay). Same.
- **OQ-091** NEW `:tested` (ISO 50001 energy management cross-cutting overlay). Same.
- **OQ-038** template count: 41 → 44 (Environmental Aspects Register + HIRA + Energy Review).
- Engine version 0.17.0 → 0.18.0 (no engine code change; keyword expansion: `iso-14001`, `iso-45001`, `iso-50001`, `environmental-management`, `occupational-health-safety`, `energy-management`).
- **Status counts (post-v0.18.0):** 6 `:verified` / 62 `:tested` / 7 `:argued` / 0 `:open` / 0 `:proved` / 0 `:benchmarked`. **Total 75.**
- Module-tier count: 36 → 39.
- Cross-cutting overlay set: 2 → 5 (iso-27001 + regulated-ai + iso-14001 + iso-45001 + iso-50001).

### Forward work

- **Compliance Obligations Register template** (ISO 14001 §6.1.3 dedicated — currently the register concept lives only inside the Environmental Aspects Register cross-reference).
- **OH&S legal-and-other-requirements register template** (ISO 45001 §6.1.3 — same situation as ISO 14001 compliance obligations).
- **Energy Objectives + Targets register template** (ISO 50001 §6.6).
- **ISO 37001 anti-bribery overlay** — the 4th common compliance-management-system standard alongside 14001/45001/50001. Would complete the EHS + governance cross-cutting overlay set.
- **ISO 22301 business continuity management overlay** — the operational-resilience compliance-management-system standard. Composes with any vertical.
- **Quality manual / process map / risk-and-opportunity register templates for manufacturing** — surfaced in `modules/manufacturing/README.md` forward-work list; not yet built.

### Public commits

- `ef13f46` — 3 overlay modules + 3 new templates + 3 new registry standards + CI extension + engine 0.17.0 → 0.18.0 version bump in a single commit.

A0-A6 cross-audit re-run: clean.

---

## v0.17.0 DRAFT — 2026-05-23

**Completes class-overlay coverage + adds general-manufacturing vertical.**

**9 NEW spec entries** (OQ-079, OQ-081 through OQ-088); spec total grows 63 → 72. Engine package version 0.16.0 → 0.17.0.

### Why this matters

Two parallel goals:

1. **Complete class-overlay coverage.** v0.16.0 shipped 3 aerospace DALs (A/B/C) + 3 automotive class overlays (ASIL-D, ASIL-B, CAL-4) — bracketing the rigor spectrum but leaving gaps (DAL-D/E, ASIL-C/A/QM, CAL-3/2/1). v0.17.0 fills the gaps. The aerospace, automotive ASIL, and automotive CAL class-overlay sets are now complete.

2. **Open Open QMS to non-regulated manufacturing.** Until v0.17.0 every vertical was for a regulated industry (medical-devices / aerospace / automotive). Organizations doing general manufacturing — machine shops, tooling, contract manufacturing, custom fab, job shops, fabrication houses, prototyping shops, light industrial — had no entry point. The new `manufacturing` vertical fills that gap with a pure ISO 9001:2015 module.

### Class overlay completions

**Aerospace DAL-D + DAL-E (full DAL set now A through E):**

- **`modules/aerospace-dal-d/`** — DO-178C / DO-254 Level D, Minor failure condition. 5 clauses:
  - DAL-D applicability gate (ARP4754A §5 from FHA Minor).
  - **No structural coverage required at DAL-D** — Table A-7 doesn't apply; software testing is requirements-based only (Normal-Range + Robustness per DO-178C §6.4.3).
  - **2-of-26 objectives with independence** (typically Quality Assurance + Software Configuration Management — substantially lighter independence regime than DAL-A/B/C).
  - Tool qualification typically at TQL-4 or TQL-5 (or none if the loosened verification objectives can be satisfied without tool substitution).
  - ARP4754A §5 allocation rationale.

- **`modules/aerospace-dal-e/`** — DO-178C / DO-254 Level E, No Safety Effect. 4 clauses:
  - DAL-E applicability gate — the FHA's No-Safety-Effect substantiation is the load-bearing claim; subsequent process is minimal.
  - **NO DO-178C objectives apply at DAL-E** — the software is not subject to DO-178C process discipline at all (§2.2.4).
  - **Configuration management still required** — so the cert authority can verify the deployed software matches the software whose DAL-E classification was substantiated.
  - ARP4754A §5 allocation rationale (isolation + failure-impact substantiation showing no contribution to any safety goal).

**Automotive ASIL-C + ASIL-A + QM (full ASIL set now D, C, B, A, QM):**

- **`modules/automotive-asil-c/`** — mid-high between D and B. 5 clauses: SPFM ≥ 97% / LFM ≥ 80% / PMHF < 10⁻⁷/h; 100% statement + 100% branch (MC/DC recommended — major delta from D); **I3 independence (same as ASIL-D** — major delta from ASIL-B's I2); language subset **REQUIRED** (vs. recommended at ASIL-B).

- **`modules/automotive-asil-a/`** — lowest non-QM tier. 5 clauses: PMHF < 10⁻⁶/h, NO quantitative SPFM/LFM targets; 100% statement only (branch + MC/DC recommended); I1 independence (different person in same team); MISRA C subset recommended.

- **`modules/automotive-qm/`** — Quality Management classification. 4 clauses encoding the *positive QM claim* (the QM allocation is a positive safety claim that the function does not require ISO 26262 process discipline beyond baseline IATF 16949 quality management — NOT an absence of analysis): QM applicability from HARA per Part 3 §6 Table 4; NO ISO 26262-specific HW metrics / SW coverage / method recommendations / confirmation measures (Part 2 §5.4.1); **HARA rationale is load-bearing** (mis-classification as QM when true classification is ASIL-A+ omits required FuSa rigor); Safety Plan listing of QM items as out-of-FuSa-scope with HARA cross-reference enabling confirmation reviewer / FuSa auditor to verify appropriate scoping (not silent omission).

  **Why ship a QM overlay rather than treat QM as "no overlay"?** Auditability. The QM allocation is a positive claim, not an absence; adopters need a place to document the QM rationale that traces from HARA through to the absence-of-FuSa-rigor decision.

**Automotive CAL-3 + CAL-2 + CAL-1 (full CAL set now 4, 3, 2, 1):**

- **`modules/automotive-cal-3/`** — mid-high. 5 clauses: TARA-derived CAL-3 applicability (Annex E); independent cybersecurity assessment **RECOMMENDED** (vs. required at CAL-4, optional at CAL-2); V&V baseline + vulnerability scanning + fuzz testing **required** (pentest recommended; side-channel not required vs. required-where-applicable at CAL-4); formal vulnerability monitoring with response-time commitments documented in CSMS + defined incident-response playbooks (rehearsal recommended — CAL-4 requires rehearsal); safety-security interaction analysis when item is also ASIL-rated.

- **`modules/automotive-cal-2/`** — mid-low. 4 clauses: TARA-derived applicability; independent assessment optional; V&V baseline + vulnerability scanning of dependencies + exposed interfaces (fuzz + pentest recommended); vulnerability monitoring with documented triage cadence (no formal response-time commitments).

- **`modules/automotive-cal-1/`** — lowest CAL. 4 clauses: TARA-derived applicability (low impact AND low feasibility); NO independent assessment required; baseline V&V (security functional only — no fuzz / pentest / side-channel); CSMS-baseline vulnerability monitoring (no response-time commitments specific to CAL-1).

### General manufacturing vertical (commit `f617b2e`)

**`modules/manufacturing/`** — ISO 9001:2015 only. 17 clauses across all seven §-groups:

- **§4 Context** — §4.1 context, §4.4 process approach.
- **§5 Leadership** — §5.1 leadership commitment, §5.2 quality policy.
- **§6 Planning** — §6.1 risk-and-opportunity (the "risk-based thinking" core of ISO 9001:2015).
- **§7 Support** — §7.1 resources, §7.1.5.2 measurement traceability, §7.4 communication, §7.5 documented information.
- **§8 Operation** — §8.1 operational planning, §8.4 supplier controls, §8.5 production + service provision, §8.5.5 post-delivery, §8.7 nonconforming outputs.
- **§9 Performance evaluation** — §9.1 monitoring + measurement + analysis, §9.2 internal audit, §9.3 management review.
- **§10 Improvement** — §10.2 nonconformity + corrective action.

All clauses bind to cross-cutting templates already in Open QMS (quality-policy, SOP, AUDIT-PROCEDURE, MANAGEMENT-REVIEW, ASL, SUPPLIER-EVALUATION, CAPA, nonconformance). **NO new templates required** — manufacturing is the smallest vertical in the project, intentionally minimal.

**Manufacturing does NOT define class overlays of its own** — ISO 9001 has no equivalent of DAL / ASIL / CAL rigor tiers. Organizations needing higher rigor typically migrate up to a regulated vertical (aerospace → AS9100D; automotive → IATF 16949; medical-devices → ISO 13485) rather than overlaying a class on top of base ISO 9001.

### Example bundle — example-machine-shop

`bundles/example-machine-shop.yaml` — small/mid precision machine shop pursuing baseline ISO 9001 certification + iso-27001 (for customer proprietary CAD/CAM file handling). The `jurisdictions:` list is intentionally empty — general manufacturing has no specific regulator. Composes `manufacturing + iso-27001`. Idempotent regenerate confirmed.

### Class-overlay coverage now complete

| Vertical | Class overlays | Count |
|---|---|---|
| medical-devices | samd, implantable, mdr-class-iii, mdr-class-iib, mdr-class-iia, fda-class-iii, fda-class-ii | 7 |
| aerospace | DAL-A, DAL-B, DAL-C, **DAL-D, DAL-E** | 5 |
| automotive ASIL | ASIL-D, **ASIL-C**, ASIL-B, **ASIL-A, QM** | 5 |
| automotive CAL | CAL-4, **CAL-3, CAL-2, CAL-1** | 4 |
| **Total class overlays** | | **21** |

(Bold = new at v0.17.0; rest were shipped at v0.11.0+v0.12.0+v0.16.0.)

### CI — engine-tests.yml extension

15 new validate steps + 1 new regenerate dry-run:
- 2 new aerospace DAL validates (DAL-D, DAL-E composed with `aerospace`)
- 3 new automotive ASIL validates (ASIL-C, ASIL-A, QM composed with `automotive`)
- 3 new automotive CAL validates (CAL-3, CAL-2, CAL-1 composed with `automotive`)
- 1 manufacturing standalone validate
- 1 manufacturing + iso-27001 composite validate
- 5 minor reorderings to group the now-complete class-overlay sets
- 1 new `regenerate --bundle example-machine-shop` dry-run

### Spec, registry, dashboard transitions

- **OQ-079** NEW `:tested` (aerospace DAL-D). Module / example-tested. Depends_on: OQ-011, OQ-059.
- **OQ-081** NEW `:tested` (aerospace DAL-E). Same tier / type / deps. (OQ-080 was assigned to a Gap entry; numbering skips to keep Module entries grouped.)
- **OQ-082** NEW `:tested` (automotive ASIL-C). Module / example-tested. Depends_on: OQ-011, OQ-072.
- **OQ-083** NEW `:tested` (automotive ASIL-A). Same.
- **OQ-084** NEW `:tested` (automotive QM). Same.
- **OQ-085** NEW `:tested` (automotive CAL-3). Same.
- **OQ-086** NEW `:tested` (automotive CAL-2). Same.
- **OQ-087** NEW `:tested` (automotive CAL-1). Same.
- **OQ-088** NEW `:tested` (general manufacturing vertical). Module / example-tested. Depends_on: OQ-011, OQ-014.
- Engine version 0.16.0 → 0.17.0 (no engine code change; keyword expansion: `manufacturing`, `iso-9001`, `machine-shop`).
- **Status counts (post-v0.17.0):** 6 `:verified` / 59 `:tested` / 7 `:argued` / 0 `:open` / 0 `:proved` / 0 `:benchmarked`. **Total 72.**
- Module-tier count: 27 → 36.
- Vertical count: 3 → 4 (medical-devices / aerospace / automotive / manufacturing).

### Forward work

- **Food safety vertical** — ISO 22000 + FSSC 22000 + HACCP. Natural next non-regulated → regulated bridge.
- **Pharma GMP vertical** — ICH Q7 (API) + 21 CFR 210/211 (US) + EudraLex Vol. 4 (EU) + PIC/S Annex 1 (sterile). Largest forward vertical by clause count.
- **Industrial machinery functional safety** — IEC 61508 (functional safety baseline) + ISO 13849 (safety-related parts of control systems for machinery). Bridges manufacturing + machinery scopes.
- **Cross-cutting overlays** — ISO 14001 (environmental), ISO 45001 (occupational H&S), ISO 50001 (energy management), ISO 37001 (anti-bribery). Each composes with any vertical.
- **Rigor-level overlay generator** — meta-pattern question. With 21 class overlays now shipped, evaluate whether a parameterized "rigor-level overlay" generator (encoding the rigor matrix per assurance dimension) is worth building, or whether per-class hand-written overlays remain the right granularity for adopter clarity. Decision can wait until food + pharma verticals land their first class overlays.

### Public commits

- `f617b2e` — 8 class overlays (DAL-D + DAL-E + ASIL-C + ASIL-A + QM + CAL-3 + CAL-2 + CAL-1) + manufacturing vertical + example-machine-shop bundle + CI extension + engine 0.16.0 → 0.17.0 version bump in a single commit.

A0-A6 cross-audit re-run: clean.

---

## v0.16.0 DRAFT — 2026-05-23

**Class overlays — 3 aerospace DAL + 3 automotive ASIL/CAL.**

**6 NEW spec entries** (OQ-073 through OQ-078, all `:tested`); spec total grows 57 → 63. Engine package version 0.15.0 → 0.16.0.

### Why this matters

v0.14.0 (aerospace) + v0.15.0 (automotive) shipped the verticals at a single rigor level — implicitly DAL-A/B/C-agnostic on aerospace; ASIL-agnostic and CAL-agnostic on automotive. That left the verticals usable but not yet tuned: a real avionics project knows whether its software target is DAL-A or DAL-D before signing the PSAC; a real automotive ECU project knows whether its torque-control function is ASIL-D before sizing the HW metrics + structural coverage targets.

Class overlays encode the rigor delta. The pattern is well-established from medical-devices (SaMD overlay for software-as-medical-device deployment scope; mdr-class-iii / mdr-class-iib / mdr-class-iia + fda-class-iii / fda-class-ii for risk-class-specific requirements). v0.16.0 brings the same pattern to aerospace + automotive.

### Aerospace class overlays (DO-178C + DO-254 + ARP4754A)

Three overlays bracket the avionics rigor spectrum from highest (DAL-A) through common-production (DAL-C). DAL-D (Minor failure-condition; very light process) and DAL-E (No Safety Effect; no DO-178C objectives) left as forward work.

- **`modules/aerospace-dal-a/`** — Catastrophic failure-condition. 7 clauses encoding the highest-rigor deltas:
  - DAL-A applicability gate (ARP4754A §5 traced from FHA).
  - **MC/DC structural coverage** (DO-178C Table A-7 obj 5 — the strongest practical coverage criterion; same standard as ISO 26262 ASIL-D MC/DC).
  - **25-of-71 objectives requiring independence** (Annex A independence column — vs. 14 at DAL-B, 2 at DAL-C, 2 at DAL-D, 0 at DAL-E).
  - **DO-330 tool qualification at TQL-1** typically (highest assurance for verification tools whose output substitutes for an objective).
  - **DO-254 §6.2 elemental analysis** required at DAL-A and DAL-B for hardware.
  - **DO-254 §6.3 safety-specific analyses** at DAL-A: Single Event Upset (SEU) analysis, common-mode analysis, supplementary analyses identified by ARP4761 SSA + CCA.
  - **ARP4754A §5 DAL-allocation rationale** traced from FHA's Catastrophic classification.
  Bindings extend PSAC + Software Test Protocol + Verification Protocol + System Safety Plan templates with DAL-A specifics.

- **`modules/aerospace-dal-b/`** — Hazardous failure-condition. 6 clauses: Decision Coverage instead of MC/DC (DO-178C Table A-7 obj 6 — the major delta from DAL-A), 14-of-69 objectives with independence, TQL-1/TQL-2 tool qualification, DO-254 elemental analysis still required, ARP4754A allocation rationale for Hazardous-classified items.

- **`modules/aerospace-dal-c/`** — Major failure-condition. **Most common DAL for production avionics functions** that are supervised by a higher-DAL function or are non-critical automation. 5 clauses: Statement Coverage instead of Decision Coverage (DO-178C Table A-7 obj 7 — the major delta from DAL-B), only 2-of-62 objectives with independence (a substantial cost-of-process reduction vs. DAL-A/B; this is why so much production avionics targets DAL-C explicitly), TQL-3/TQL-4 tool qualification, ARP4754A §3.5 decomposition often invoked to allocate higher DALs into multiple DAL-C elements with independence argumentation.

### Automotive class overlays (ISO 26262 + ISO/SAE 21434)

Three overlays — two ISO 26262 ASIL levels (D + B brackets the spectrum; A + C + QM left as forward work) and the highest ISO/SAE 21434 CAL (CAL-4; CAL-1/2/3 forward work).

- **`modules/automotive-asil-d/`** — Highest ISO 26262 FuSa rigor (HARA at S3 × E4 × C3 per Part 3 §6 Table 4). 6 clauses:
  - ASIL-D applicability gate from HARA.
  - **Hardware architectural metrics**: SPFM ≥ 99% (Single-Point Fault Metric), LFM ≥ 90% (Latent Fault Metric), PMHF < 10⁻⁸ failures/hour (Probabilistic Metric for Hardware Failures). Per ISO 26262 Part 5 §8-9 + Annex F.
  - **Software structural coverage**: 100% statement + 100% branch + 100% MC/DC at unit-test level (Part 6 Table 12); 100% function + 100% function-call at integration level (Table 13). MC/DC is the same criterion as DO-178C DAL-A — note the cross-domain consistency.
  - **I3-independence confirmation measures** for confirmation review + FuSa audit + FuSa assessment (Part 2 §6 Table 1 — different organizational unit minimum, or external).
  - **Software design + coding method requirements**: formal notations + strongly-typed languages strongly recommended; MISRA C 2012 mandatory rules required; defensive programming + restricted pointers + restricted recursion + restricted dynamic memory.
  - **Optional ASIL decomposition** per Part 9 §5: D = C(D)+A(D), or B(D)+B(D), or D+QM(D), with dependent-failure-analysis (DFA) per Part 9 §7 supporting the independence claim.
  Bindings extend Safety Concept + Verification Protocol + Software Test Protocol + SOP templates with ASIL-D specifics.

- **`modules/automotive-asil-b/`** — Mid-tier rigor; common production ECUs. 5 clauses: ASIL-B applicability (e.g., S2 × E4 × C2; S3 × E3 × C1; S2 × E3 × C3 per Part 3 §6 Table 4); SPFM ≥ 90% / LFM ≥ 60% / PMHF < 10⁻⁷ failures/hour; 100% statement + 100% branch (MC/DC recommended but NOT required — the major delta from ASIL-D); I2-independence confirmation measures (different team within the same organizational unit — less stringent than ASIL-D's I3 minimum); MISRA C 2012 recommended but not mandatory.

- **`modules/automotive-cal-4/`** — Highest ISO/SAE 21434 Cybersecurity Assurance Level. Assigned when TARA's impact-and-feasibility matrix yields CAL-4 (typically high-impact safety-affecting damage scenarios with non-low attack feasibility — examples: brake / steering / acceleration ECU compromise; back-end server controlling fleet OTA updates). 5 clauses:
  - CAL-4 applicability gate from TARA per Annex E (informative) or the adopter's CSMS-defined CAL determination method.
  - **Independent cybersecurity assessment** for cybersecurity case + final assessment (§6.4.7 + Annex C — different organizational unit or external).
  - **Rigorous V&V**: security functional testing + vulnerability scanning + fuzz testing + penetration testing + side-channel analysis where attack-feasibility analysis identifies side-channel threats (§10 + §13).
  - **Continuous activities** (§11): formal vulnerability monitoring with response-time commitments documented in CSMS; rehearsed incident-response playbooks; sustained cybersecurity through product end-of-support with explicit transition plan.
  - **Safety-security interaction analysis** when item is also ASIL-rated — cross-reference ISO 26262 Part 2 §6 with joint review by FuSa + cyber engineering. The Safety Concept template's optional Part C is the artifact where this is documented.

### Composition validation

All 6 overlays validate standalone composed with their respective verticals:
- aerospace + aerospace-dal-a (and dal-b, dal-c)
- automotive + automotive-asil-d (and asil-b, cal-4)

**5-module mega-composite validates**: `automotive + automotive-asil-d + automotive-cal-4 + regulated-ai + iso-27001`. This is the QMS scaffold for a top-rigor safety-critical AND cyber-critical AND ML-enabled ECU under enterprise information-security posture — a realistic shape for next-generation ADAS / automated-driving controllers. The fact that this composes cleanly under the existing OQ-011 compose primitive (built in medical-devices context at v0.4.0, no changes since) is a load-bearing structural validation of the platform.

### CI — engine-tests.yml extension

7 new validate steps in the test job:
- 3 aerospace DAL overlays (each composed with `aerospace`)
- 3 automotive class overlays (each composed with `automotive`)
- 1 mega-composite (`automotive + asil-d + cal-4 + regulated-ai + iso-27001`)

Any drift in a class overlay's manifest, a vertical it composes against, or the registry standards it cites will fail CI.

### Spec, registry, dashboard transitions

- **OQ-073** NEW `:tested` (aerospace DAL-A). Module / example-tested. Depends_on: OQ-011, OQ-059.
- **OQ-074** NEW `:tested` (aerospace DAL-B). Same tier / type / deps.
- **OQ-075** NEW `:tested` (aerospace DAL-C). Same.
- **OQ-076** NEW `:tested` (automotive ASIL-D). Module / example-tested. Depends_on: OQ-011, OQ-072.
- **OQ-077** NEW `:tested` (automotive ASIL-B). Same.
- **OQ-078** NEW `:tested` (automotive CAL-4). Same.
- Engine version 0.15.0 → 0.16.0 (no engine code change).
- **Status counts (post-v0.16.0):** 6 `:verified` / 50 `:tested` / 7 `:argued` / 0 `:open` / 0 `:proved` / 0 `:benchmarked`. **Total 63.**
- Module-tier count: 21 → 27 (OQ-040..OQ-059 + OQ-072..OQ-078).

### Forward work

- **Remaining aerospace DAL overlays:** DAL-D (Minor failure condition — very light process; usually no structural coverage), DAL-E (No Safety Effect — no DO-178C objectives at all).
- **Remaining automotive ASIL overlays:** ASIL-A (lowest non-QM tier), ASIL-C (mid-high; between B and D), QM (Quality Management baseline only — no FuSa-specific rigor).
- **Remaining CAL overlays:** CAL-1 (lowest), CAL-2, CAL-3 (mid-tier).
- **Cross-vertical pattern evaluation:** as more class overlays accumulate, evaluate whether a parameterized "rigor-level overlay" generator is worth building (e.g., one Python data-class generating all 5 DAL overlays from a rigor matrix), or whether per-class hand-written overlays remain the right granularity for adopter clarity.

### Public commits

- `ffad042` — 6 class overlays + CI extension + engine 0.15.0 → 0.16.0 version bump in a single commit.

A0-A6 cross-audit re-run: clean.

---

## v0.15.0 DRAFT — 2026-05-23

**Automotive vertical — second non-medical vertical.**

**1 NEW spec entry** (OQ-072 automotive vertical, `:tested`); spec total grows 56 → 57. Engine package version 0.14.0 → 0.15.0.

### Why this matters

v0.14.0's aerospace vertical proved the platform composition (OQ-011 + OQ-014 + OQ-013 + OQ-015) generalizes off the medical-devices substrate. v0.15.0's automotive vertical strengthens that from one data point to two — and on a substantively different shape of regulated industry.

**Key differences from aerospace:**

1. **Bifurcated risk-management discipline.** Aerospace has a single safety-assessment track (ARP4761 — FHA / PASA / PSSA / SSA / CCA). Automotive has *two parallel* risk tracks that interact at the architectural level:
   - **Functional safety** per ISO 26262: HARA → ASIL → Safety Goals → FSC → TSC → HW/SW with ASIL-driven process rigor (structural coverage, independence requirements, hardware metrics SPFM/LFM/PMHF).
   - **Cybersecurity engineering** per ISO/SAE 21434: TARA → CAL → Cybersecurity Goals → cybersecurity controls → continuous activities (vulnerability + incident response).

   The Safety Concept template explicitly models this with optional Part C for the Cybersecurity Concept, and a safety-security interaction analysis table (e.g., crypto-verification latency on a brake message vs. FTTI). This is a more nuanced composition pattern than aerospace required.

2. **Layered type-approval.** Aerospace certification is a per-aircraft Type Certificate from FAA / EASA / TCCA, with the QMS underneath (AS9100D registration). Automotive certification is layered: IATF 16949 QMS certification + UN R155 manufacturer CSMS certification + UN R156 manufacturer SUMS certification + per-vehicle-type cybersecurity assessment under R155 Annex 5 + per-vehicle-type approval from KBA / UNECE-recognised authority. Each layer is a separate gate.

3. **Production approval is broader.** Aerospace's AS9102 FAI focuses on dimensional inspection of new/changed parts (3 forms). Automotive's AIAG PPAP covers 18 elements including DFMEA, PFMEA, Control Plan, MSA, capability studies (Cpk/Ppk for Special Characteristics), and the Part Submission Warrant — a substantially broader production-readiness gate.

### Module — automotive vertical (commit `d35fedc`)

**`modules/automotive/`** — civil road-vehicle (passenger cars, light commercial, heavy duty trucks). 28 clauses across 8 standards:

- **QMS substrate (IATF 16949:2016):** §4.4 process approach with automotive-specific effectiveness + efficiency criteria; §7.1.5.2.1 calibration / verification records retention; §7.5 documented information including customer-specific requirements; §8.3.3.3 Special Characteristics identification (KC / CC / SC drives PFMEA + Control Plan + PPAP); §8.4 supplier control with Tier-N visibility + flow-down of customer-specific requirements; §8.5.1.1 Control Plan; §8.7 nonconforming output with customer-notification protocol; §9.2 internal audit with three IATF-mandated audit types (QMS + manufacturing-process + product); §10.2.3 problem solving with 8D-style structured approach.

- **Functional safety (ISO 26262:2018):** Part 2 management of functional safety + §6 confirmation measures (confirmation review + FuSa audit + FuSa assessment, with independence requirements scaling with ASIL); Part 3 §5 Item Definition + §6 HARA (S × E × C → ASIL determination → Safety Goals) + §7 Functional Safety Concept; Part 4 product development at the system level (Technical Safety Concept + system V&V); Part 5 product development at the hardware level (SPFM / LFM / PMHF metrics per ASIL target); Part 6 product development at the software level (structural coverage per ASIL — statement / branch / MC/DC); Part 8 supporting processes (config + change + tool qualification per §11 with TCL classification); Part 9 ASIL-oriented analyses (ASIL decomposition per §5 + dependent-failure analysis per §7).

- **Cybersecurity engineering (ISO/SAE 21434:2021):** §5 CSMS (Cybersecurity Management System — organizational capability); §9 + §10-13 concept + product development phases; §10 project-dependent cybersecurity management; §11 continuous cybersecurity activities (vulnerability mgmt + incident response); §15 TARA (Threat Analysis and Risk Assessment driving CAL — Cybersecurity Assurance Level 1-4).

- **Type-approval cybersecurity regulations:** UN R155 CSMS certification (manufacturer-level, Annex 7 + Schedule 1); UN R155 vehicle-type cybersecurity approval (per-vehicle-type assessment vs. Annex 5 threat categories); UN R156 SUMS certification (Software Update Management System — over-the-air + offline update process discipline). Mandatory for type approval in UNECE jurisdictions since July 2022; not mandatory in the US but increasingly flowed down by OEMs to suppliers.

- **Process maturity (Automotive SPICE 4.0):** SWE process group (SWE.1-6 — requirements analysis through qualification test, with bidirectional traceability); MAN + SUP process groups (project management, risk management, measurement, QA, configuration management, problem resolution, change request management).

- **Production approval (AIAG PPAP 4th Ed.):** 18-element submission package (Levels 1-5) with Part Submission Warrant.

**5 new automotive-specific templates:**

- **`templates/product-dhf/item-definition/ITEM-DEFINITION-TEMPLATE.md`** — ISO 26262 Part 3 §5. Functional + non-functional requirements, boundary, external interfaces, environmental conditions, legal requirements, preliminary architecture, dependencies on other items (with DIA — Development Interface Agreement references for cross-organization development per Part 8 §5), assumptions of use, preliminary safe states, preliminary ASIL + CAL allocations. The first concept-phase deliverable; iterates with HARA.
- **`templates/product-dhf/hara/HARA-TEMPLATE.md`** — ISO 26262 Part 3 §6. Operational situations × functions × malfunctions → hazardous events. Per-event Severity (S0-S3 per Annex B) × Exposure (E0-E4) × Controllability (C0-C3) classification. Reproduces the full ASIL determination table. Safety Goals derived per event. FTTI (Fault Tolerant Time Interval) and EOTI documented per goal. Confirmation review per Part 2 §6 with reviewer-independence requirements scaled to ASIL.
- **`templates/product-dhf/safety-concept/SAFETY-CONCEPT-TEMPLATE.md`** — combined FSC (Part 3 §7) + TSC (Part 4 §6) + optional Cybersecurity Concept (ISO 21434 §9) document. Part A: FSC with FSR derivation, ASIL allocation per architectural element, safe states + warning + degradation strategies, ASIL decomposition table per Part 9 §5. Part B: TSC with TSR derivation, system architecture safety analyses (FMEA / FTA / DFA), TSR allocation to HW + SW. Part C (optional): Cybersecurity Goals + Cybersecurity Requirements + safety-security interaction analysis.
- **`templates/product-dhf/tara/TARA-TEMPLATE.md`** — ISO/SAE 21434 §15. Asset identification → damage scenarios → impact rating (Safety / Financial / Operational / Privacy, per ISO/SAE 21434 §15.5 scale) → threat scenarios + attack paths (STRIDE / attack trees / kill chain methods) → attack feasibility per ISO/IEC 18045 → risk determination → CAL assignment → risk treatment (avoid / reduce / share / retain) → Cybersecurity Goals. Includes the UN R155 Annex 5 coverage matrix (32 threats across 7 categories: back-end servers, vehicle comms, update procedures, unintended human actions, external connectivity, vehicle data + code, potential vulnerabilities) for type-approval scope. Cross-reference with HARA for safety-impacting threats is mandatory.
- **`templates/product-dhf/ppap/PPAP-TEMPLATE.md`** — AIAG PPAP 4th Ed. 18-element submission with status (Submitted / Retained / NA) per Submission Level. Special Characteristics summary linking IATF 16949 §8.3.3.3. Capability studies summary (typical targets: Ppk ≥ 1.67 initial, Cpk ≥ 1.33 ongoing for Critical / Key Characteristics). MSA summary (typical targets: GR&R < 10% acceptable, 10-30% marginal, >30% unacceptable per AIAG MSA). Part Submission Warrant with authorized-signatory declaration and customer disposition section.

**Registry additions (7 new standards):** IATF 16949:2016, ISO 26262:2018 (all 12 parts referenced as one standard for registry purposes), ISO/SAE 21434:2021, UN R155, UN R156, Automotive SPICE 4.0, AIAG PPAP 4th Ed.

**Jurisdiction additions (4):**
- **NHTSA** — U.S. National Highway Traffic Safety Administration. NHTSA uses the FMVSS framework (49 CFR Part 571) which does NOT require UNECE-style type approval; UN R155 / R156 / ISO 26262 / ISO/SAE 21434 are not mandatory in the US but increasingly flowed down by OEMs.
- **UNECE** — UN Economic Commission for Europe WP.29 World Forum for Harmonization of Vehicle Regulations. International type-approval forum covering EU + Japan + Korea + most non-US markets. UN R155 + UN R156 are mandatory for type approval since July 2022.
- **KBA** — Kraftfahrt-Bundesamt, German Federal Motor Transport Authority. EU type-approval authority issuing under UN regulations + EU framework.
- **TC-MVS** — Transport Canada Motor Vehicle Safety. Distinct id from aerospace `TCCA` (Transport Canada Civil Aviation).

### Example bundle — example-vehicle

`bundles/example-vehicle.yaml` + committed baseline `bundles/example-vehicle.matrix.json` demonstrate end-to-end: an ExamplePowertrainECU under NHTSA + UNECE + KBA composing `automotive + regulated-ai + iso-27001` across 12 standards (8 automotive + 4 AI / IS). Idempotent regenerate confirmed.

The regulated-ai overlay is included because the example product has a predictive battery state-of-health ML-driven function that triggers NIST AI RMF (US side) + EU AI Act Article 6 Annex III high-risk-AI scope (EU side). This composition is structurally analogous to the medical-devices + regulated-ai composition for AI/ML-enabled SaMD and the aerospace + regulated-ai composition for ML-driven avionics — confirming the AI overlay's "any vertical" claim across now three verticals.

The iso-27001 overlay is included because CSMS assessors under UN R155 increasingly expect an enterprise-wide information-security posture.

### CI — engine-tests.yml extension

- Validate step extended: automotive standalone, automotive + regulated-ai + iso-27001 composite. Aerospace + regulated-ai + iso-27001 composite + medical-devices baseline retained.
- Regenerate step extended: dry-run check on example-samd + example-aircraft + example-vehicle matrices. Any drift fails CI.

### Spec, registry, dashboard transitions

- **OQ-072** NEW `:tested`. Tier: Module. Evidence type: example-tested. Depends_on: OQ-011 (composition primitive), OQ-014 (standards-and-jurisdictions registry).
- **OQ-038** template count: 36 → 41 (5 automotive-specific templates added).
- Engine version 0.14.0 → 0.15.0 (keywords expanded: `automotive`, `iatf-16949`, `iso-26262`, `iso-21434`).
- **Status counts (post-v0.15.0):** 6 `:verified` / 44 `:tested` / 7 `:argued` / 0 `:open` / 0 `:proved` / 0 `:benchmarked`. **Total 57.**

### Forward work

- **ASIL class overlays** — ASIL-A through ASIL-D per ISO 26262 Parts 2 / 4 / 5 / 6 with progressively stringent process requirements (structural coverage, independence requirements, hardware metrics).
- **CAL class overlays** — CAL 1-4 per ISO/SAE 21434.
- **Automotive-defense overlay** — MIL-STD-882E + ITAR + EAR for armored ground vehicles + military variants of civilian platforms.
- **Motorcycle adaptation** — ISO 26262 Part 12. Overlay vs. separate vertical decision pending an adopter use case.
- **Heavy commercial vehicles + buses** — same standards apply; specific operational situations differ in HARA + per-vehicle-type tightness in cyber assessment.
- **NHTSA Part 573 recall workflow** — cross-cutting workflow analogous to medical-devices §820.198 complaints / EU MDR vigilance.

### Public commits

- `d35fedc` — automotive module + 5 templates + 7 registry standards + 4 jurisdictions + example-vehicle bundle + CI extension + engine version bump in same commit.

A0-A6 cross-audit re-run: clean.

---

## v0.14.0 DRAFT — 2026-05-23

**Aerospace vertical — first non-medical vertical regulatory module.**

**1 NEW spec entry** (OQ-059 aerospace vertical, `:tested`); spec total grows 55 → 56. Engine package version 0.13.0 → 0.14.0 (no engine code change; version bump tracks the module addition).

### Why this matters

Until v0.14.0 every shipped module was either medical-devices (the vertical) or a cross-cutting overlay (iso-27001, regulated-ai) or a medical-devices class overlay (samd, implantable, mdr-class-*, fda-class-*). The platform could plausibly have been "medical-devices QMS generator + some adjacent modules." Aerospace tests whether the composition primitive (OQ-011), the registry mechanism (OQ-014), the validation harness (OQ-013), and the template system actually generalize off the medical-devices substrate.

Result: yes. The aerospace vertical resolves against the same engine code with the same composition primitive. Cross-cutting templates (quality-policy, SOP, audit, management-review, supplier, CAPA, NCR, risk management, verification, software test) cover the aerospace QMS surface naturally — aerospace QMS is structurally similar to medical-devices QMS, just with aerospace-specific extensions for cert + safety assessment + FAI. Aerospace + regulated-ai composes (ARP4761 safety assessment and ISO 23894 AI risk management are complementary domain-specific extensions of risk discipline). Aerospace + iso-27001 composes (organizational information security is orthogonal to product certification).

### Module — aerospace vertical (commit `a480c3a`)

**`modules/aerospace/`** — civil aviation (commercial aerospace under FAA / EASA / TCCA). 27 clauses across 9 aerospace standards:

- **QMS substrate:** AS9100D §§4.4 process approach, 5.6 (renumbered to §9.3 in Rev D) management review, 7.1 resources, 7.4 communication, 7.5 documented information, 8.1.4 operational risk management, 8.4 supplier control, 8.5.1 production with Foreign Object Damage (FOD) prevention, 8.7 control of nonconforming output, 9.2 internal audit, 10.2 corrective action. ISO 9001:2015 is the upstream baseline AS9100D is built on; no separate clauses (subsumed).
- **Certification (US + EU):** 14 CFR Part 21 §§21.31 type design, 21.35 flight tests, 21.50 Instructions for Continued Airworthiness (ICA); EASA Part 21 Subpart B equivalents.
- **Avionics software:** DO-178C:2011 — PSAC submission, §6 verification process (review + analysis + test), §7 configuration management process, §9 software life-cycle data submission, §11 Stages of Involvement (SOIs) with the certification authority.
- **Airborne electronic hardware:** DO-254:2000 — PHAC submission, §6 verification + validation process.
- **System development:** ARP4754A:2010 — §5 system development process (lifecycle activities, requirements capture, allocation), §6 function development + allocation.
- **Safety assessment:** ARP4761:1996 — §3 Functional Hazard Assessment (aircraft-level + system-level FHAs), §4-5 Preliminary Aircraft / System Safety Assessment (PASA / PSSA — fault tree analysis driving derived safety requirements), §6 System Safety Assessment (final SSA verifying implementation meets safety requirements), §9 Common Cause Analysis (Zonal Safety Analysis + Particular Risks Analysis + Common Mode Analysis).
- **Production gate:** AS9102 Rev C — First Article Inspection (Forms 1/2/3).

**5 new aerospace-specific templates:**

- **`templates/product-dhf/psac/PSAC-TEMPLATE.md`** — DO-178C Plan for Software Aspects of Certification. Primary planning document submitted to FAA / EASA at SOI #1. Covers system overview, software overview, certification considerations (DAL assignment + means of compliance + issue papers), software life cycle, life cycle data, software standards, tool qualification per DO-330, configuration management, QA, four Stages of Involvement with the cert authority, DO-178C supplements (DO-330/331/332/333 if applicable).
- **`templates/product-dhf/fha/FHA-TEMPLATE.md`** — ARP4761 Functional Hazard Assessment. Identifies and classifies failure conditions per severity (Catastrophic / Hazardous / Major / Minor / No Safety Effect) which drive DAL assignments per ARP4754A §5. Aircraft-level and System-level FHA variants. Quantitative-target table per AC 25.1309-1A / AMC 25.1309.
- **`templates/product-dhf/safety-assessment/SSP-TEMPLATE.md`** — System Safety Plan per ARP4754A + ARP4761. Top-level coordination of FHA, PASA, PSSA, SSA, CCA across the system development lifecycle. Schedule table tying safety-assessment activities to SDR / PDR / CDR / Cert milestones. Methods + tools section (FTA, FMEA, Markov). Independence and audit requirements per AS9100D §9.2.
- **`templates/product-dhf/fai/FAI-REPORT-TEMPLATE.md`** — AS9102 First Article Inspection Report. Standard AS9102 Forms 1 (Part Number Accountability), 2 (Raw Material / Spec / Special Processes), 3 (Characteristic Accountability) reproduced. Characteristic accountability with Key Characteristic / Critical / Major / Minor designators per AS9103 variation management. Customer flow-down concurrence section.
- **`templates/product-dhf/type-cert/TYPE-CERT-PACK-INDEX-TEMPLATE.md`** — navigable manifest of every document constituting the Type Certificate application. Indexes by 14 CFR / EASA Part 21 section AND by airworthiness subpart (typical CS-25 layout). Aerospace analog of the medical-devices Technical File Index. Cross-references safety substantiation pack + software substantiation pack (per DO-178C item) + hardware substantiation pack (per DO-254 item) + production-readiness pack + continued-operational-safety plan.

**Registry additions (9 new standards):** ISO 9001:2015, AS9100D, 14 CFR Part 21, EASA Part 21, DO-178C:2011, DO-254:2000, ARP4754A:2010, ARP4761:1996, AS9102 Rev C.

**Jurisdiction additions (3):** FAA (U.S. Federal Aviation Administration — distinct from medical-devices FDA = Food and Drug Administration), EASA (European Union Aviation Safety Agency), TCCA (Transport Canada Civil Aviation). Each lists its typical `applicable_standards`.

### Example bundle — example-aircraft

`bundles/example-aircraft.yaml` + committed baseline `bundles/example-aircraft.matrix.json` demonstrate end-to-end: an ExampleAvionicsComputer under FAA composing `aerospace + regulated-ai + iso-27001` across 13 standards (the 9 aerospace standards + NIST AI RMF + EU AI Act + ISO/IEC 42001 + ISO/IEC 27001). Idempotent regenerate confirmed.

The regulated-ai overlay is included because modern avionics increasingly integrate ML-driven functions (autopilot enhancements, predictive maintenance, vision-based landing aids) which trigger NIST AI RMF + EU AI Act high-risk-AI requirements alongside DO-178C. This composition is structurally identical to the medical-devices + regulated-ai composition used for AI/ML-enabled SaMD — confirming the AI overlay's "any vertical" claim.

### CI — engine-tests.yml extension

- Validate step extended: aerospace standalone, regulated-ai standalone, aerospace + regulated-ai + iso-27001 composite. Medical-devices baseline still validated.
- Regenerate step extended: dry-run check on both `example-samd` AND `example-aircraft` matrices. If either drifts from its committed baseline, CI fails — operator either reverts the offending module/registry/template change or runs `openqms regenerate --bundle <name> --write-matrix` and commits the resulting matrix.

### Spec, registry, dashboard transitions

- **OQ-059** NEW `:tested`. Tier: Module. Evidence type: example-tested. Depends_on: OQ-011 (composition primitive), OQ-014 (standards-and-jurisdictions registry).
- **OQ-038** template count 31 → 36 (aerospace-specific templates added).
- Engine version 0.13.0 → 0.14.0 (commit `00de6d0`).
- **Status counts (post-v0.14.0):** 6 `:verified` / 43 `:tested` / 7 `:argued` / 0 `:open` / 0 `:proved` / 0 `:benchmarked`. **Total 56.**

### Forward work

- **Aerospace DAL class overlays** — DO-178C / DO-254 Design Assurance Levels A through E. Each DAL level mandates increasing rigor of structural coverage analysis (MC/DC for DAL-A, decision coverage for DAL-B, statement coverage for DAL-C, requirements-based testing only for DAL-D, none for DAL-E). Analogous to the medical-devices class overlay pattern (mdr-class-iii / fda-class-iii / etc.).
- **Aerospace-defense overlay** — MIL-STD-882E System Safety Program Plan, ITAR + EAR controlled-technology handling (with strict scope notes: Open QMS doesn't redistribute controlled technical data).
- **Commercial space scope** — FAA 14 CFR Part 450 (launch / re-entry vehicle licensing) as a separate vertical or as an aerospace extension.
- **Production-readiness module deepening** — Nadcap (NDT, heat treatment, plating, welding qualifications) as an aerospace cross-cutting overlay; AS9145 Advanced Product Quality Planning (APQP) integration.

### Public commits

- `a480c3a` — aerospace module + 5 templates + 9 registry standards + 3 jurisdictions + example-aircraft bundle + CI extension.
- `00de6d0` — engine 0.13.0 → 0.14.0 version bump.

A0-A6 cross-audit re-run: clean.

---

## v0.12.0 DRAFT — 2026-05-23

**Three-phase release: additional class overlays + IVD overlay + regulated-AI cross-cutting overlay.**

**5 NEW spec entries** (OQ-054 through OQ-058); spec total grows 50 → 55. Engine package version 0.11.0 → 0.12.0.

### Phase A (commit `f0d48f7`) — 3 additional class overlays

- **`modules/mdr-class-iib/`** — EU MDR Class IIb. Article 54 expert panel trigger (subset: active drug-delivery devices), Annex IX Class IIb conformity procedure, Article 84 biennial PSUR cadence.
- **`modules/mdr-class-iia/`** — EU MDR Class IIa. Annex XI production quality assurance route (alternative to full Annex IX), Article 83 as-needed PMS report (not PSUR cadence).
- **`modules/fda-class-ii/`** — FDA Class II (510(k) path). 21 CFR 807 Subpart E Premarket Notification, Special Controls per product code, 21 CFR 860 Subpart D De Novo classification path.
- **1 new template:** `510K-SUBMISSION-TEMPLATE.md` — substantial-equivalence comparison + technical sections + Special Controls compliance + De Novo path option + establishment registration.
- **Registry additions:** 21 CFR 807 (Premarket Notification), 21 CFR 860 (Classification + De Novo).
- **Spec entries:** OQ-054, OQ-055, OQ-056.

### Phase B (commit `361f4ff`) — IVD overlay

- **`modules/ivd/`** — In Vitro Diagnostic overlay. 8 clauses covering EU IVDR 2017/746 (Article 5, Annex I IVD GSPRs, Annex II, Annex IX conformity, Annex XIII performance evaluation, Article 56 PSUR cadence), 21 CFR 809 (FDA IVD labeling), ISO 15189:2022 (medical lab quality + competence).
- **2 new templates:**
  - `IVDR-GSPR-CHECKLIST-TEMPLATE.md` — 20 IVDR GSPRs across 3 chapters with per-IVDR-class applicability guidance; Chapter II §9 expanded into three sub-rows (analytical / clinical / scientific-validity).
  - `PERFORMANCE-EVALUATION-REPORT-TEMPLATE.md` — IVDR equivalent of medical-devices CER. Three-pillar evidence framework per Annex XIII (scientific validity + analytical performance + clinical performance) with CLSI EP-series methodology references.
- **Registry additions:** EU IVDR 2017/746, 21 CFR 809, ISO 15189:2022.
- **Pragmatic shipping decision:** cross-cutting overlay (not standalone vertical) — shared QMS baseline inherited from `medical-devices` via composition; adopters declare medical-devices MDR-specific clauses (MDR-Art10(9), MDR-AnnexI, etc.) as NA per IVD scope SOP. Future `medical-devices-ivd` standalone vertical excluding MDR clauses entirely remains forward work. CLIA (42 CFR 493) deferred — applies to labs not IVD manufacturers.
- **Spec entries:** OQ-057.

### Phase C (commit `3e231d5`) — Regulated-AI cross-cutting overlay

- **`modules/regulated-ai/`** — composes with ANY vertical. 13 clauses:
  - NIST AI RMF 1.0 four functions: Govern, Map, Measure, Manage.
  - EU AI Act Chapter III §2 high-risk AI requirements: Articles 9 (risk mgmt), 10 (data governance), 11 (technical doc), 12 (automatic logging), 13 (transparency), 14 (human oversight), 15 (accuracy/robustness/cybersecurity).
  - ISO/IEC 42001:2023 AIMS (consolidated).
  - ISO/IEC 23894:2023 AI risk management guidance.
- **2 new templates:**
  - `AI-SYSTEM-CARD-TEMPLATE.md` — Mitchell et al. (2019) Model Card extended with EU AI Act Article 11 + 13 + Article 12 logging coverage and IMDRF SaMD classification carry-forward.
  - `AI-IMPACT-ASSESSMENT-TEMPLATE.md` — EU AI Act Article 9 risk management + Article 14 human oversight + Article 27 fundamental rights impact + NIST AI RMF Govern/Map/Measure/Manage. 10 risk categories + risk control hierarchy + human-oversight model documentation + post-deployment monitoring.
- **Existing template bindings extended:** RMF → ISO 23894; quality-policy → ISO 42001 AIMS; SAD → EU AI Act Art 15; STP → EU AI Act Art 10; TFI → EU AI Act Art 12.
- **Registry addition:** ISO/IEC 23894:2023 (other AI standards already registered as roadmap entries at v0.5.0).
- **Cross-cutting note:** clauses primarily target EU AI Act high-risk AI scope (Annex III); limited-risk and minimal-risk scope a subset with NA declarations.
- **Spec entries:** OQ-058.

### Composition verification

7-module mega-composite (`medical-devices + ivd + samd + regulated-ai + mdr-class-iii + fda-class-iii + iso-27001`) validates cleanly. Demonstrates that AI overlay composes with any vertical combination, IVD overlay composes alongside, class overlays stack, and the dedup-by-content-equality semantics of OQ-011 handle MDR-Art54 across mdr-class-iib + mdr-class-iii without conflict.

### Status counts

42 `:tested` (post-v0.11.0) → **47 `:tested`** (post-v0.12.0) · 8 `:argued` · 0 `:open`. Total **55**.

### Cross-audit (A0-A6)

Clean.

### Public commits

`f0d48f7` (Phase A — 8 files / +410) + `361f4ff` (Phase B — 5 files / +424) + `3e231d5` (Phase C — 5 files / +568) + `093c35f` (engine version bump — 2 files / +2/-2). Range `edfc2f0..093c35f`.

---

## v0.11.0 DRAFT — 2026-05-23

**Device-class overlay modules — SaMD, implantable, EU MDR Class III, FDA Class III.**

Ships four cross-cutting overlays that compose with the medical-devices vertical to add classification-specific requirements. Each overlay validates standalone; the full 6-module composite (medical-devices + 4 device-class + iso-27001) resolves cleanly. **4 new spec entries** (OQ-050 through OQ-053); spec total grows 46 → 50.

- **`modules/samd/`** — Software as a Medical Device. Three clauses: IMDRF SaMD risk categorization (Class I-IV on State-of-Healthcare-Situation × Significance-of-Information axes), IEC 82304-1 health software product safety, SaMD cybersecurity. Binds to new SAMD-INTENDED-USE-TEMPLATE + existing SOFTWARE-REQUIREMENTS-TEMPLATE + existing RISK-MANAGEMENT-FILE-TEMPLATE. Per-class GSPR applicability note in README — SaMD adopters typically declare NA on most physical/mechanical GSPRs.

- **`modules/implantable/`** — Implantable devices. Three clauses: EU MDR Annex I §23.4 (implant card subclause), Article 32 (SSCP), ISO 14708-1 (active implantable general requirements). Binds to new IMPLANT-CARD-TEMPLATE + new SSCP-TEMPLATE + existing VERIFICATION-PROTOCOL-TEMPLATE.

- **`modules/mdr-class-iii/`** — EU MDR Class III risk class. Four clauses: Article 32 (SSCP, shared with implantable), Article 54 (expert panel consultation for implantable Class III + Class IIb active drug-delivery), Annex X (type-examination), Article 84 (PSUR cadence). Binds to SSCP-TEMPLATE + new EXPERT-PANEL-CONSULTATION-TEMPLATE + existing technical-file index + existing PMCF template.

- **`modules/fda-class-iii/`** — FDA Class III / PMA path. Four clauses: 21 CFR 814 Subpart B (PMA application), §814.39 (PMA supplements), §814.84 (PMA annual report), 21 CFR 803 (FDA MDR adverse-event reporting). Binds to new PMA-SUBMISSION-TEMPLATE + existing change-request issue template + existing complaint issue template + existing management-review template. Naming clarification: FDA's "MDR" (21 CFR 803) is **not** the EU MDR (2017/745).

- **5 new templates:**
  - `templates/product-dhf/samd-intended-use/SAMD-INTENDED-USE-TEMPLATE.md` — IMDRF SaMD framework intended-use with two-axis matrix and Category I-IV implications.
  - `templates/product-dhf/implant/IMPLANT-CARD-TEMPLATE.md` — Annex I §23.4 patient-facing card with production-time-population markers.
  - `templates/product-dhf/implant/SSCP-TEMPLATE.md` — Article 32 SSCP per MDCG 2019-9 with HCP + patient sections.
  - `templates/product-dhf/clinical/EXPERT-PANEL-CONSULTATION-TEMPLATE.md` — Article 54 expert panel record.
  - `templates/product-dhf/pma/PMA-SUBMISSION-TEMPLATE.md` — 21 CFR 814 PMA assembly index covering all 814.20(b) technical sections + manufacturing info + post-approval commitments + supplement workflow.

- **5 new standards in registry:**
  - IEC 82304-1:2016 (health software product safety)
  - ISO 14708-1:2014 (active implantable medical devices — general)
  - 21 CFR 814 (FDA PMA)
  - 21 CFR 803 (FDA Medical Device Reporting — adverse events)
  - IMDRF SaMD N12 (risk categorization framework, guidance)

- **Bundle update** at `bundles/example-samd.yaml`:
  - Adds `samd` overlay to the module list (honest about the example device's SaMD identity).
  - Adds IEC 82304-1 + IMDRF SaMD N12 standards.
  - Matrix regenerated: 3 new in-scope clauses + 1 new artifact (SaMD intended-use template). Idempotent — subsequent dry-run reports `(no changes)`.

- **Engine package version 0.10.0 → 0.11.0** (commit `edfc2f0`, follow-up to `54e93de`). Engine API unchanged.

- **Composition tested end-to-end:**
  ```bash
  openqms validate \
    --module medical-devices --module samd --module implantable \
    --module mdr-class-iii --module fda-class-iii --module iso-27001
  ```
  The 6-module composite resolves with all clause-deduplication preserved (MDR-Art32 appears in both implantable and mdr-class-iii with identical summaries → silent dedup; SSCP-TEMPLATE bound by both overlays → union of bindings).

- **Scope notes:**
  - **Class I + Class II overlays NOT shipped.** Their "additions" over the baseline medical-devices module are actually *subtractions* (Class I exemptions from §820.30 design controls; reduced 510(k) for Class II) — doesn't fit the union-based compose primitive. Adopters of Class I/II devices use medical-devices directly with applicability notes.
  - **IVD deferred.** IVDs in EU are governed by IVDR (Regulation 2017/746), not MDR. A separate `medical-devices-ivd` vertical module is required — IVDR is not overlay-able onto MDR-rooted scaffolding. Forward work.

- **Tests: 97, all green** (unchanged count). Each overlay validates standalone; composite validates; medical-devices regression baseline confirms no drift.

- **Spec deltas:**
  - **OQ-050** NEW `:tested` — SaMD overlay module.
  - **OQ-051** NEW `:tested` — implantable overlay module.
  - **OQ-052** NEW `:tested` — EU MDR Class III overlay module.
  - **OQ-053** NEW `:tested` — FDA Class III overlay module.
  - **OQ-038** notes updated: 21 → 26 document templates.
- **Status counts:** 42 `:tested` · 8 `:argued` · 0 `:open` · 0 `:proved` / `:verified` / `:benchmarked`. **Total 50** (was 46 — spec grew by 4 entries for the new overlays).

- **Cross-audit (A0-A6):** clean.

**Public commits:** `54e93de` (16 files / +1053 / −5) + `edfc2f0` (2 files / +2 / −2). `aa51574..edfc2f0`.

---

## v0.10.0 DRAFT — 2026-05-23

**OQ-044 closed: EU MDR Annex I + Annex XIV. All module-tier entries `:tested`.**

Closes the last remaining `:argued` module-tier entry. Ships device-class-agnostic templates for the two MDR annexes previously deferred (Annex I GSPRs and Annex XIV CER/PMCF), with per-class customization notes inline.

- **`templates/product-dhf/gspr/GSPR-CONFORMITY-CHECKLIST-TEMPLATE.md`** — EU MDR Annex I checklist enumerating all 23 GSPRs across the three chapters (general requirements §1-9; design and manufacture §10-22; information supplied §23.1-23.4). Per-GSPR rows for Applicable/NA, standards used, evidence references, notes. Cross-references RMF, CER, UEF, IFU, labeling. Mandatory NA-justification section. Covers MDR-AnnexI.

- **`templates/product-dhf/clinical/CLINICAL-EVALUATION-TEMPLATE.md`** — EU MDR Annex XIV Part A Clinical Evaluation Report per MDCG 2020-13 / 2020-5 / 2020-6. Sections: clinical evaluation plan, data identification (literature / clinical experience / clinical investigations / equivalence per MDCG 2020-5), data appraisal, analysis against acceptability criteria, conclusions on performance/safety/benefit-risk, PMCF integration, CER update cadence per risk class. Covers MDR-AnnexXIV-A.

- **`templates/product-dhf/clinical/PMCF-PLAN-TEMPLATE.md`** — EU MDR Annex XIV Part B Post-Market Clinical Follow-up plan per MDCG 2020-7/8. Plan scope and rationale, PMCF methods (registries, surveys, PMS data, literature surveillance, PMCF studies), specific PMCF activity table, statistical considerations, GSPR/CER mapping, RMF integration, schedule per risk class. Covers MDR-AnnexXIV-B.

- **Module manifest updates** at `modules/medical-devices/module.yaml` (version 0.2.0 → 0.3.0):
  - 3 new clauses: MDR-AnnexI, MDR-AnnexXIV-A, MDR-AnnexXIV-B.
  - 3 new artifact bindings (GSPR checklist → AnnexI; CER → AnnexXIV-A; PMCF → AnnexXIV-B).
  - Validation harness passes on the expanded manifest (**62 clauses, 31 artifacts** in the medical-devices module).

- **Baseline matrix** at `bundles/example-samd.matrix.json` regenerated to absorb the 3 new clauses + 3 new artifacts. Subsequent dry-run regenerate reports `(no changes)` and exits 0.

- **Per-class customization noted but not enforced.** The GSPR applicability column (A/NA) is device-class-dependent — SaMD declares NA on most physical/chemical/mechanical GSPRs; implantables declare A on most; IVD routes through IVDR rather than MDR. Templates ship with placeholder A/NA values; adopters customize per their intended-use and Annex VIII classification. Device-class overlay sub-modules (SaMD / implantable / IVD) remain forward work that would further automate the per-class GSPR subset selection — not on the immediate roadmap.

- **Engine package version 0.9.0 → 0.10.0** (commit `aa51574`, follow-up to `e6d15a8`). Engine API unchanged.

- **Tests: 97, all green** (unchanged count).

- **Spec deltas:**
  - **OQ-044** `:argued → :tested` — EU MDR full coverage with the 6 originally-listed elements machine-readable.
  - **OQ-038** notes updated: 18 → 21 document templates.
  - **OQ-068** notes updated: 13 populated subdirs (added gspr/ + clinical/ as new dirs).
- **Status counts:** 38 `:tested` · 8 `:argued` · 0 `:open` · 0 `:proved` / `:verified` / `:benchmarked`. Total 46.

- **Cross-audit (A0-A6):** clean.

**All 10 module-tier entries (OQ-040 through OQ-049) now `:tested`.** The medical-devices module is comprehensively populated across all 11 declared standards.

**Remaining `:argued` entries (8, all honest-effort items):**
- OQ-002 + OQ-003 (load-bearing invariant claims; upgrade gated on hypothesis-style property tests)
- OQ-022 + OQ-023 (substrate enforcement gated on adopter-org configuration)
- OQ-062 (PHI/PII architecture decision; SOP-bound)
- OQ-067 (forward-language not a script)
- OQ-070 + OQ-071 (licensing claims; manual-only by nature)

**Public commits:** `e6d15a8` (5 files / +399 / −1) + `aa51574` (2 files / +2 / −2). `cbaffba..aa51574`.

---

## v0.9.0 DRAFT — 2026-05-23

**Medical-devices module fully populated: 6 module-tier entries close.**

The medical-devices module expanded from 24 clauses across 4 standards (v0.8.0) to **59 clauses across 11 standards**. Six module-tier spec entries transition `:argued → :tested` (OQ-041 ISO 13485, OQ-042 21 CFR 820, OQ-043 21 CFR Part 11, OQ-045 IEC 62304, OQ-046 IEC 62366-1 + IEC 60601-1, OQ-047 ISTA + MDSAP). One (OQ-044 EU MDR) stays `:argued` with partial coverage — Annex I GSPRs and Annex XIV CER intentionally deferred to device-class-specific overlays.

- **4 new document templates:**
  - `templates/product-dhf/technical-file/TECHNICAL-FILE-INDEX-TEMPLATE.md` — navigable manifest of the device's technical file, indexed by EU MDR Annex II section + ISO 13485 §4.2.3 element. Covers ISO13485-4.2.3 and MDR-AnnexII. Populates the previously-empty `technical-file/` subdir.
  - `templates/qms-sops/AUDIT-PROCEDURE-TEMPLATE.md` — internal audit SOP. Audit program planning, auditor independence, procedure (scoping → opening → evidence → categorization → closing → report → findings → closure), records, management-review integration, regulatory-inspection interface. Covers ISO13485-8.2.4 and CFR820-820.22.
  - `templates/product-dhf/usability/USABILITY-ENGINEERING-FILE-TEMPLATE.md` — IEC 62366-1 UEF (new subdir). Use specification, UI specification, primary operating functions, hazard-related use scenarios, formative + summative evaluation. Bound to the RMF. Covers IEC62366-1-5.
  - `templates/product-dhf/packaging/PACKAGING-VALIDATION-TEMPLATE.md` — ISTA packaging validation report (new subdir). Test plan (conditioning, vibration, drop, compression, atmospheric), sample size, sterile-barrier integrity per ISO 11607, shelf life. Covers ISTA-2A and ISTA-3A.

- **Module manifest expanded** at `modules/medical-devices/module.yaml`:
  - Version bumped 0.1.0 → 0.2.0.
  - Standards list grows 4 → 11: adds 21 CFR Part 11, EU MDR 2017/745, IEC 62366-1, IEC 60601-1, ISTA 2A, ISTA 3A, MDSAP.
  - **35 new clauses** spanning all 7 added standards plus the missing ISO 13485 / 21 CFR 820 / IEC 62304 clauses identified in the crosswalk.
  - Quality policy template gains 12 cross-cutting bindings (ISO 13485 §4.1.6 / §4.2.5 / §6.3; CFR 820 §820.20 + §820.180; CFR Part 11 §11.10(b-d); MDR Article 10(9); MDSAP composite).
  - 21 CFR Part 11 §11.50 binds to `docs/guide/signature-meaning.md`; §11.70 / §11.100 / §11.200 / §11.300 bind to `docs/guide/gpg-signing.md` — the guides ARE the artifacts documenting the mechanism satisfying each clause. §11.10(e) operational checks bind to `release-gate.yml`.
  - Existing templates gain bindings: SOP-TEMPLATE adds production controls (§820.70); VERIFICATION-PROTOCOL adds QMS-software-validation (§4.1.6) + Part 11 §11.10(a) + IEC 60601-1 essential safety; SOFTWARE-ARCHITECTURE adds detailed design (§5.4); SOFTWARE-REQUIREMENTS adds planning (§5.1); RISK-MANAGEMENT-FILE adds software risk management (§7); CAPA / NCR issue templates bind to §820.90 / §820.100 / IEC 62304 §6 / §9; MANAGEMENT-REVIEW adds process monitoring (§8.2.3) + MDR Annex IX.

- **Example bundle expanded** at `bundles/example-samd.yaml`:
  - Standards list 5 → 12 (adds all 7 new module standards). Bundle now exercises the medical-devices module end-to-end against the full SaMD-relevant standards set plus the iso-27001 overlay.
  - `bundles/example-samd.matrix.json` regenerated. In-scope clauses jump by 35; artifacts grow to absorb the 4 new templates + 3 newly-bound existing artifacts. Subsequent dry-run regenerate reports `(no changes)` and exits 0.

- **Engine package version 0.8.0 → 0.9.0** (commit `cbaffba`, follow-up to `78ee0db`). Engine API unchanged.

- **Tests: 97, all green** (unchanged count). Validation harness passes on the expanded 59-clause / 28-artifact manifest. The shipped-example regression test continues to pass against the regenerated baseline.

- **Spec deltas:**
  - **OQ-041** `:argued → :tested` — ISO 13485:2016 clause coverage (11 clauses).
  - **OQ-042** `:argued → :tested` — 21 CFR 820 coverage (11 sections).
  - **OQ-043** `:argued → :tested` — 21 CFR Part 11 full coverage (10 subclauses; §11.50 via OQ-060 trailers, §11.70 + §11.100/200/300 via OQ-023 GPG guide).
  - **OQ-044** stays `:argued` — EU MDR partial: Article 10(9) + Annex II + Annex IX machine-readable; Annex I GSPRs and Annex XIV CER deferred (require device-class overlays).
  - **OQ-045** `:argued → :tested` — IEC 62304 coverage (12 clauses).
  - **OQ-046** `:argued → :tested` — IEC 62366-1 + IEC 60601-1 coverage.
  - **OQ-047** `:argued → :tested` — ISTA 2A/3A + MDSAP coverage.
  - **OQ-038** notes updated: 14 → 18 document templates.
  - **OQ-068** notes updated: 11 of original 15 empty subdirs now populated.
- **Status counts:** 37 `:tested` · 9 `:argued` · 0 `:open` · 0 `:proved` / `:verified` / `:benchmarked`. Total 46.

- **Cross-audit (A0-A6):** clean.

**Remaining `:argued` entries (9, all honest-effort items):**
- OQ-002 + OQ-003 (load-bearing invariant claims; upgrade gated on hypothesis-style property tests)
- OQ-022 + OQ-023 (substrate enforcement gated on adopter-org configuration)
- OQ-044 (EU MDR Annex I + Annex XIV deferred to device-class overlays)
- OQ-062 (PHI/PII architecture decision; SOP-bound)
- OQ-067 (forward-language not a script)
- OQ-070 + OQ-071 (licensing claims; manual-only by nature)

**Public commits:** `78ee0db` (8 files / +1310 / −63) + `cbaffba` (2 files / +2 / −2). `ec188b3..cbaffba`.

---

## v0.8.0 DRAFT — 2026-05-23

**OQ-063 + OQ-064 closed. Zero `:open` entries milestone.**

The last two `:open` spec entries — supplier-evaluation workflow and management-review aggregation — closed in a single commit. Every spec claim now carries at least manual evidence (`:argued`) or mechanical evidence (`:tested`); none are "we haven't started yet."

- **Supplier controls (OQ-063):**
  - `templates/qms-suppliers/APPROVED-SUPPLIER-LIST-TEMPLATE.md` — the canonical record of qualified suppliers + procurement gate. Criticality classification (Critical / Major / Minor) drives re-evaluation cadence. Disqualified-supplier record + re-evaluation triggers (scheduled, NCR-linked, complaint-linked, supplier-change, performance-threshold breach).
  - `templates/qms-suppliers/SUPPLIER-EVALUATION-TEMPLATE.md` — per-supplier evaluation record. Sections: identification, QMS assessment (cert review / audit / questionnaire), capability assessment, sample/lot qualification, supplier quality agreement status, approval decision with conditions, sign-off.
  - `.github/ISSUE_TEMPLATE/supplier-evaluation.yml` — workflow tracker. Captures supplier, ASL ID, evaluation type, criticality, trigger record link, scope, assigned reviewer, due date.
  - `docs/guide/supplier-controls.md` — process, cadence defaults table (Critical 12mo / Major 24mo / Minor 36mo), procurement gate procedural-vs-automated patterns, audit-trail integration.

- **Management review (OQ-064):**
  - `templates/qms-management-review/MANAGEMENT-REVIEW-TEMPLATE.md` — meeting record covering all ISO 13485 §5.6.2 inputs (feedback/complaints, audits, CAPAs, process performance, regulatory changes, supplier performance, risk management, resources, recommendations) and §5.6.3 outputs (QMS improvements, product improvements, resource needs, action items, effectiveness statement).
  - `.github/ISSUE_TEMPLATE/management-review.yml` — workflow tracker including the §5.6.2 input-aggregation checklist.
  - `docs/guide/management-review.md` — workflow, `gh` CLI input-aggregation patterns (per input category), three aggregation models (light-touch CLI / scripted shell-or-Python / external eQMS), cadence defaults (quarterly / semi-annually / per-product-line), triggered-review criteria. Deliberately declines to ship a single aggregator tool — a one-size-fits-all label taxonomy would force adopter assumptions; declining keeps the QMS pluggable.

- **Module manifest updates** at `modules/medical-devices/module.yaml`:
  - 4 new clauses: `ISO13485-5.6` (management review), `ISO13485-7.4` (purchasing), `CFR820-820.20(c)` (management review subset of §820.20), `CFR820-820.50` (purchasing controls).
  - 5 new artifact bindings (3 supplier + 2 management-review).
  - Validation harness passes on the expanded manifest (24 clauses, 17 artifacts).

- **CLI fix** at `engine/openqms/cli.py`:
  - `openqms regenerate --write-matrix` now exits 0 on successful write regardless of whether the diff was non-empty. Previously returned 1 in `--write-matrix` mode if changes existed, which conflated "you accepted the change" with "CI dry-run detected drift." Now the semantics are clean: with `--write-matrix` exit 0 = "write happened"; without it exit 1 = "changes detected, did not write."

- **Baseline matrix** at `bundles/example-samd.matrix.json`:
  - Regenerated to absorb the 4 new clauses + 5 new artifacts. The committed matrix now reflects the post-OQ-063/064 resolution. Subsequent `regenerate --bundle example-samd` reports `(no changes)` and exits 0.

- **Engine package version 0.7.0 → 0.8.0** (commit `ec188b3`, follow-up to `aedde0b`). Engine API unchanged from 0.7.0 modulo the CLI exit-code fix.

- **Tests: 97, all green** (unchanged count). The existing regenerate suite exercises the new exit-code semantics.

- **Spec deltas:**
  - **OQ-063** `:open → :tested` — supplier-evaluation workflow.
  - **OQ-064** `:open → :tested` — management-review aggregation.
  - **OQ-041** notes updated — ISO 13485 machine-readable coverage now 5 clauses (was 3).
  - **OQ-042** notes updated — 21 CFR 820 machine-readable coverage now 5 sections (was 3).
  - **OQ-038** notes updated — 14 document templates (was 11).
- **Status counts:** 31 `:tested` · 15 `:argued` · **0 `:open`** · 0 `:proved` / `:verified` / `:benchmarked`. **Total 46. Zero `:open` entries.**

- **Cross-audit (A0-A6):** clean.

**Remaining work surface (all `:argued`):** continued medical-devices module-coverage population — OQ-041 (5/full ISO 13485), OQ-042 (5/full 21 CFR 820), OQ-045 (7/9 IEC 62304); OQ-043 (21 CFR Part 11), OQ-044 (EU MDR), OQ-046 (IEC 62366-1 + IEC 60601-1), OQ-047 (ISTA + MDSAP) have no machine-readable bindings yet. Plus organizational gaps OQ-002 + OQ-003 (load-bearing invariant claims; verification gated on hypothesis-style property tests), OQ-022 + OQ-023 (substrate enforcement gated on adopter-org configuration), OQ-062 (PHI/PII architecture decision; SOP-bound), OQ-067 (forward-language not script), OQ-070 + OQ-071 (licensing claims; manual-only by nature).

**Public commits:** `aedde0b` (12 files / +831 / −3) + `ec188b3` (2 files / +2 / −2). `0b06381..ec188b3`.

---

## v0.7.0 DRAFT — 2026-05-23

**P8 closed: 21 CFR Part 11 §11.50 signature-meaning prototype shipped.**

GPG-signed commits handle §11.70 cryptographic identity binding (OQ-023). §11.50 separately requires the signature manifestation to display the *meaning* of the signature (approved / reviewed / authorized / released / etc.) — GPG alone doesn't encode this. v0.7.0 ships the bridge: a controlled-vocabulary commit-trailer convention plus parser, audit-trail exporter, CLI, and CI gate.

- **Trailer convention.** Every commit constituting a §11.50 signature carries:
  - `Signature-Meaning: <value>` — **required**. Meaning per §11.50(a)(3). Common values: `approved`, `reviewed`, `authorized`, `released`, `verified`, `validated`. Adopters define their controlled vocabulary in SOP.
  - `Signature-Role: <role>` — optional but recommended. E.g. `QA-Lead`, `Engineering-Manager`.
  - `Signature-Justification: <free-form>` — optional but recommended for high-risk approvals.

- **`engine/openqms/signatures.py`:**
  - `SignatureTrailer` frozen dataclass: meaning, role, justification, signer_name, signer_email, signed_at, commit_sha, gpg_verified, gpg_signer_key_id.
  - `parse_signature_trailers(message)` — lenient regex extraction of `Signature-*:` lines from anywhere in the commit message body.
  - `signature_from_commit_data()` — builds a `SignatureTrailer` from commit metadata; returns `None` if no `Signature-Meaning`. Decodes all 9 `git log %G?` GPG status codes; only `G` (good) and `U` (good/unknown-validity) set `gpg_verified=True`.
  - `extract_signatures_from_repo(repo_root, since_ref=None, paths=None)` — walks `git log` with NUL-byte (`%x00`) field separators and ASCII record separator (`%x1e`) between commits, parses each commit, returns the list of signatures matching `Signature-Meaning`.
  - `export_audit_trail(signatures)` — emits Part 11 §11.50-format JSON records: printed name, email, datetime, meaning, role, justification, git_commit pointer, GPG verification state with key id.

- **CLI subcommand: `openqms signatures verify | export`.**
  - `verify --commit <sha>` (default HEAD) — checks the commit has the required trailer; `--require-gpg` upgrades unverified signatures to errors. Exit 0/1/2.
  - `export --since <ref> --path <p>… --output <path>` — emits the JSON audit trail; `--require-gpg` fails on any unverified record.

- **CI workflow `.github/workflows/signature-check.yml`** — gates PRs touching `qms-policy/`, `qms-sops/`, `qms-forms/`, `qms-training/`, `product-*/`. Runs `openqms signatures verify` against every commit in the PR's range. Dormant in OpenQMS (no controlled documents at those paths today); active in adopter forks once they populate controlled documents.

- **Guide `docs/guide/signature-meaning.md`** — verbatim §11.50 text; why GPG alone is necessary but not sufficient; trailer convention with examples; the three-layer verification model (GPG substrate → trailer parser → audit-trail export); CLI surface; CI integration; honest limitations (trailer is discipline not security boundary; HR-to-identity mapping is procedural; controlled vocabulary is adopter's responsibility; parsing is lenient; web edits sign as GitHub).

- **engine-tests.yml** — adds `openqms signatures export` as a smoke check against OpenQMS's own git log (empty trail today; exercises the engine path).

- **Engine package version 0.6.0 → 0.7.0.**

- **Tests: 74 → 97** (+23 new in `engine/tests/test_signatures.py`):
  - Parser (4): basic, empty body returns empty, justification field, ignores non-Signature trailers.
  - signature_from_commit_data (2 + 9 parametric): returns None without meaning, full trailer construction; all 9 GPG status codes (G, U, B, X, Y, R, E, N, empty) correctly mapped to `gpg_verified` bool.
  - export_audit_trail (2): full Part 11 fields present, missing optional fields handled.
  - tmp-git-repo integration (2): mix of signed/unsigned commits extracted correctly; `paths` filter respected.
  - CLI subprocess (4): `export` against tmp repo round-trips JSON; `verify` passes on signed commit; `verify` fails on missing trailer; `verify --require-gpg` fails on unsigned.

- **READMEs.** Top-level adds a "Signatures" subsection under "Generator engine" and bumps status to v0.7.0. Engine README documents the subcommand and convention.

- **Spec deltas:**
  - **OQ-060** `:open → :tested` — Part 11 §11.50 signature-meaning prototype.
- **Status counts:** 29 `:tested` · 15 `:argued` · 2 `:open` · 0 `:proved` / `:verified` / `:benchmarked`. Total 46.
- **Cross-audit (A0-A6):** clean.

**Remaining work surface:** continued medical-devices module-coverage population (OQ-041 / 042 / 045 partial → `:tested` once full clause sets mechanized; OQ-043 / 044 / 046 / 047 still `:argued`), and two organizational-process gaps (OQ-063 supplier evaluation workflow, OQ-064 management review aggregation).

**Public commit:** `0b06381` (`3cfec2c..0b06381`) — 10 files / +891 / −5.

---

## v0.6.0 DRAFT — 2026-05-23

**P1.3 closed: re-resolution + edition supersession. Phase 1 fully closed.**

- **`openqms regenerate --bundle <name>` CLI subcommand.** Re-resolves a stored bundle definition at `bundles/<name>.yaml`, diffs against the prior matrix at `bundles/<name>.matrix.json`, prints the structured diff. Exit code: `0` (no changes), `1` (changes), `2` (error). `--write-matrix` accepts the change and overwrites the matrix file; default is dry-run. `--strict-editions` upgrades registry-supersession warnings to errors.

- **`engine/openqms/bundle.py`** — `BundleDef` frozen dataclass and `load_bundle_def(path)` loader. Required keys: `name`, `product`, `modules` (≥1). Optional: `jurisdictions`, `standards`. Loader validates structure.

- **`engine/openqms/diff.py`** — `MatrixDiff` frozen dataclass + `diff_matrices(old, new)` + `format_diff(diff)`. Diff captures standards added/removed, in-scope clauses added/removed, artifacts added/removed, per-artifact addressed-clause changes (for templates present in both matrices), module-version change. `has_changes` property is the single boolean the CLI consults.

- **Edition supersession (OQ-065).** `StandardEntry.superseded_by: str | None = None` added to the registry schema. `RegistryValidationReport.superseded_standards: tuple[tuple[str, str], ...]` carries `(old_id, new_id)` pairs found in a module's standards. CLI prints supersession as a warning by default; `--strict-editions` flag (available on `validate` and `regenerate`) treats it as an error. Shipped registry today has no actual supersessions — mechanism is in place for the first time a referenced standard is superseded.

- **`bundles/example-samd.yaml` + `bundles/example-samd.matrix.json`** — first stored bundle definition and its committed baseline matrix. Pins `ExampleSaMD` against FDA jurisdiction with the full medical-devices + iso-27001 standard set (5 standards: ISO 13485:2016, 21 CFR 820, ISO 14971:2019, IEC 62304:2006+A1:2015, ISO/IEC 27001:2022; 2 modules). The matrix records 23 in-scope clauses across 12 artifacts. Idempotent: second `regenerate --bundle example-samd` reports `(no changes)` and exits 0.

- **CI integration** at `.github/workflows/engine-tests.yml`:
  - Workflow now triggers on `bundles/**` in addition to `engine/`, `modules/`, `templates/`, `registry/`.
  - Final step: `openqms regenerate --bundle example-samd` (dry-run). If anything drifts in the example bundle's resolution, CI fails until the drift is either reverted or accepted via `--write-matrix` commit.

- **Engine package version 0.5.0 → 0.6.0.**

- **Tests: 49 → 74** (+25 new):
  - `test_bundle.py` (8): loader minimal/full, shipped example, missing-file / missing-name / missing-product / no-modules / non-list-field raises.
  - `test_diff.py` (9): no-changes, standard added/removed, clause added, artifact added+removed, addresses_changed for shared artifact, module-version change, combined diff, format_diff renders.
  - `test_regenerate.py` (8 CLI subprocess): shipped-example regression (must report no changes), baseline-on-first-run, change-detection-with-exit-1, dry-run-preserves-matrix, unknown-bundle-raises, supersession warning (default) and error (`--strict-editions`).

- **READMEs.** Engine README documents the regenerate command and supersession flag. Top-level README gains a "Regenerate" subsection and updates the architecture diagram to show `bundles/`.

- **Spec deltas:**
  - **OQ-015** `:open → :tested` — re-resolution on mutation produces Git-reviewable diff.
  - **OQ-065** `:open → :tested` — module-version drift detection via `superseded_by` + `--strict-editions`.
- **Status counts (reconciled to actual):** 28 `:tested` · 15 `:argued` · 3 `:open` · 0 `:proved` / `:verified` / `:benchmarked`. **Total 46.** Previous changelog/dashboard tallies of 40 were a long-running undercount carried forward from the v0.1.0 baseline; per-version transition records were accurate, only the running totals were off.
- **Cross-audit (A0-A6):** clean.

**Phase 1 fully closed.** All four Phase 1 priorities shipped: P1.1 composition (v0.4.0), P1.2 registry (v0.5.0), P1.3 re-resolution + supersession (v0.6.0). Remaining work surface: P8 (Part 11 §11.50 prototype, OQ-060), continued module-coverage population for medical devices (OQ-041 / 042 / 045 partial; OQ-043 / 044 / 046 / 047 still `:argued`), and the two still-open organizational-process gaps (OQ-063 supplier evaluation, OQ-064 management review aggregation).

**Public commit:** `3cfec2c` (`12b6b33..3cfec2c`) — 16 files / +1376 / −38.

---

## v0.5.0 DRAFT — 2026-05-22

**P1.2 closed: standards-and-jurisdictions registry shipped.**

- **Registry data** at `registry/`:
  - `standards.yaml` — 15 entries covering everything in the medical-devices crosswalk (ISO 13485, 21 CFR 820, 21 CFR Part 11, EU MDR, ISO 14971, IEC 62304, IEC 62366-1, IEC 60601-1, ISTA 2A, ISTA 3A, MDSAP) plus the ISO/IEC 27001 overlay plus 3 AI-regulation roadmap entries (NIST AI RMF, EU AI Act, ISO/IEC 42001). Each entry carries `id` (canonical), `name`, `publisher`, `edition`, `kind` (standard/regulation/program/guidance), `license_kind` (commercial/public), and `aliases`.
  - `jurisdictions.yaml` — 6 entries (FDA, Health Canada, EU MDR, PMDA, TGA, ANVISA) with `applicable_standards` lists. Every entry in `applicable_standards` is cross-checked against `standards.yaml` at load time.
  - `README.md` — purpose, schema, PR workflow.

- **Engine code** at `engine/openqms/registry.py`:
  - Frozen dataclasses: `StandardEntry`, `JurisdictionEntry`, `Registry`, `RegistryValidationReport`.
  - `load_registry(root)` parses both YAML files and runs the jurisdiction → standard cross-check at load time (raises if any jurisdiction references an unregistered standard).
  - `Registry.resolve_standard(name_or_alias)` returns the canonical entry for an id or alias; `canonical_standard()` returns just the canonical id string; `has_standard()` returns bool.
  - `validate_module_against_registry(module, registry)` returns a `RegistryValidationReport` flagging any module standards or per-clause standards not in the registry.

- **CLI integration** at `engine/openqms/cli.py`:
  - `--standard` arguments are normalized to canonical ids before reaching the resolver. User typing `--standard "ISO 13485"` gets `"ISO 13485:2016"` passed to the bundle.
  - Unknown standards and jurisdictions raise with a specific error listing the registered ids. Eliminates the pre-v0.5.0 footgun where typos silently produced empty resolutions.
  - Module manifests are cross-checked against the registry on every `resolve` and `validate`; a module that references an unregistered standard fails with a specific error.
  - New subcommand `openqms registry list` (tabular listing) and `openqms registry show --id <id>` (single entry).
  - Escape hatch flag `--allow-unregistered-standards` on `resolve` and `validate`. Jurisdictions remain strictly validated regardless.

- **CI** at `.github/workflows/engine-tests.yml`:
  - Workflow now triggers on `registry/**` in addition to `engine/`, `modules/`, `templates/`.
  - Validation step runs `openqms validate` against medical-devices, iso-27001, and the composite — all of which cross-check against the registry.
  - Final step runs `openqms registry list` as a smoke check.

- **Engine package version 0.4.0 → 0.5.0** (matches spec version).

- **Tests: 28 → 49** (21 new in `engine/tests/test_registry.py`):
  - Unit (8): canonical-id resolution, alias resolution, unknown-standard raises, `canonical_standard` normalizes alias, `has_standard`, jurisdiction resolution, unknown jurisdiction raises.
  - Shipped-registry (4): load completes, shipped registry contains expected entries, jurisdiction cross-check is clean, shipped medical-devices module passes registry validation, shipped iso-27001 module passes registry validation.
  - Loader negatives (2): missing files raise, dangling jurisdiction reference raises.
  - Module-vs-registry negatives (2): unregistered module standard detected, unregistered clause standard detected.
  - CLI subprocess integration (5): alias normalization works end-to-end, unknown standard rejected, unknown jurisdiction rejected, `--allow-unregistered-standards` escape hatch works (produces empty resolution like pre-v0.5.0), `registry list` prints content, `registry show --id <alias>` resolves and prints details.

- **READMEs updated.** Top-level `README.md` gains a "Registry" subsection under "Generator engine" and adds `registry/` to the architecture diagram. `engine/README.md` documents the registry CLI surface, alias normalization, escape hatch, and `registry list/show` subcommands.

- **Spec deltas:**
  - **OQ-014** `:open → :tested` — standards-and-jurisdictions registry versioned and consulted on every CLI invocation; module manifests cross-checked.
- **Status counts:** 24 `:tested` · 13 `:argued` · 3 `:open` · 0 `:proved` / `:verified` / `:benchmarked`. Total 40.

- **Cross-audit (A0-A6):** clean.

**Public commit:** `12b6b33` (`2a146ad..12b6b33`) — 11 files / +1080 / −9.

---

## v0.4.0 DRAFT — 2026-05-22

**P1.1 closed: multi-module composition primitive shipped + first cross-cutting overlay module.**

- **`openqms.module.compose(modules, name, version) -> Module`** — new public primitive. Unions clauses by `id` (identical content silently dedups; conflicting content raises `ValueError`); unions template `addresses` lists by `path` (first-seen template name wins; addresses merged in first-seen order); dedups standards. Empty input raises; single-element input returns the module unchanged (so callers can compose unconditionally).
- **CLI `--module` is now repeatable** on both `openqms resolve` and `openqms validate`. When multiple are supplied, the engine composes before the operation. The composite carries a synthetic `name` (e.g. `medical-devices+iso-27001-overlay`) and `version: composed`.
- **First overlay module: `modules/iso-27001/`** — three ISO/IEC 27001:2022 Annex A clauses (A.5.1 information security policies, A.5.31 legal/regulatory requirements, A.8.31 dev/test/prod separation) bound to three existing OpenQMS templates (quality policy, SOP template, software release record). All three templates also appear in the medical-devices vertical's binding list; composition unions the `addresses` without conflict — `quality-policy.md` ends up addressing four clauses in the composite (two from each module).
- **Engine package version 0.2.0 → 0.4.0** (matches the spec version the BUSINESS tree is tracking).
- **Test count: 15 → 28.** Thirteen new tests in `engine/tests/test_composition.py`:
  - Unit (11): empty input raises; single-element passthrough; two-module clause union; identical-clause dedup; conflicting-clause raise; template-address union for shared paths; first-seen-name precedence; standard dedup-and-order; determinism; composite self-consistency; overlay-only-module gap closure.
  - Integration (2): medical-devices + iso-27001 composes and validates; medical-devices + iso-27001 resolve produces merged `quality-policy.md` addresses (4 clauses across both modules under all 5 standards).
- **READMEs updated.** Top-level `README.md` documents the multi-module CLI usage in the "Generator engine" section; `engine/README.md` documents the composition primitive and rules. Architecture diagram updated to show `modules/iso-27001/`.
- **Spec deltas:**
  - **OQ-011** `:open → :tested` — modules compose under union; deduplication preserves invariant.
  - **OQ-012** `:open → :tested` — cross-cutting overlays compose with vertical modules.
  - **OQ-048** `:argued → :tested` — ISO/IEC 27001 overlay module ships with three-clause seed; coverage is partial (3 of ~93 Annex A controls) but the overlay primitive is mechanically demonstrated.
- **Status counts:** 23 `:tested` · 13 `:argued` · 4 `:open` · 0 `:proved` / `:verified` / `:benchmarked`. Total 40.
- **Cross-audit (A0-A6):** clean.

**Public commit:** `2a146ad` (`2625b98..2a146ad`) — 9 files / +525 / −16.

---

## v0.3.0 DRAFT — 2026-05-22

**P6 closed (partial); ISO 14971 full coverage achieved.**

- **Eight templates shipped** in `templates/product-dhf/` and `templates/product-sw/`:
  - `risk-management/RISK-MANAGEMENT-FILE-TEMPLATE.md` — ISO 14971 risk-management file (plan, hazard analysis, risk control, residual risk evaluation, overall residual risk acceptability, risk-benefit analysis, RM report, post-production information).
  - `verification/VERIFICATION-PROTOCOL-TEMPLATE.md` — Design verification per ISO 13485 §7.3.6 / 21 CFR 820.30(f).
  - `validation/VALIDATION-PROTOCOL-TEMPLATE.md` — Design validation per ISO 13485 §7.3.7 / 21 CFR 820.30(g).
  - `requirements/SOFTWARE-REQUIREMENTS-TEMPLATE.md` — SRS per IEC 62304 §5.2.
  - `architecture/SOFTWARE-ARCHITECTURE-TEMPLATE.md` — SAD per IEC 62304 §5.3.
  - `soup-register/SOUP-REGISTER-TEMPLATE.md` — SOUP register per IEC 62304 §8.1.2.
  - `test/SOFTWARE-TEST-PROTOCOL-TEMPLATE.md` — Test protocol per IEC 62304 §5.5 / §5.6 / §5.7.
  - `release/SOFTWARE-RELEASE-TEMPLATE.md` — Software release record per IEC 62304 §5.8.

  All templates use the standard document-control frontmatter (document_id, version, effective_date, owner, status, approved_by, approval_date) and will be validated by `doc-control.yml`.

- **Medical-devices module extended.** `modules/medical-devices/module.yaml` adds 14 new clauses (ISO 14971 §4 through §10, IEC 62304 §5.2 / §5.3 / §5.5 / §5.6 / §5.7 / §5.8 / §8.1.2) and 8 new template bindings. Standards list grows from 2 to 4: adds `ISO 14971:2019` and `IEC 62304:2006+A1:2015`. Module size: 6 → 20 clauses; 4 → 12 templates. Validation harness passes on the expanded manifest.

- **Spec deltas:**
  - **NEW entry OQ-049** — Medical-devices module ISO 14971:2019 full coverage. `:tested`. All seven substantive ISO 14971 clauses present in the manifest and bound to the RM template. First module-tier entry to reach `:tested` with complete (not partial) standard coverage.
  - **OQ-068 reframed.** Was "eleven of fourteen subdirs placeholder-only" (off-by-four — original count was 15). Now: 8 of original 15 populated, 7 remain (qms-{capa,forms,training,suppliers,management-review} are org-level workflows where adopters define their own; product-dhf/{design-outputs,technical-file} are product-specific). Stays `:tested`.
  - **OQ-038 updated.** Template count grows from 4 (post-v0.2.1) to 11.

- **Status counts:** 20 `:tested` · 14 `:argued` · 6 `:open` · 0 `:proved` / `:verified` / `:benchmarked`. Total **40** (was 39 pre-v0.3.0; +1 for new OQ-049).

- **Cross-audit (A0-A6):** clean.

**Public commit:** `2625b98` (`86bda4f..2625b98`) — 17 files / +696 / −0 (.gitkeep deletions counted as renames).

---

## v0.2.2 DRAFT — 2026-05-22

**P7 closed: GPG signing enforcement guide.**

- `docs/guide/gpg-signing.md` — runnable checklist for layering required-signed-commits enforcement on an Open QMS deployment. Covers signing scheme selection (GPG / SSH / S/MIME), per-individual key registration with HR-attested identity mapping, repository-level "Require signed commits" branch protection (plus the `gh api` equivalent), optional org-level enforcement, a CI workflow snippet for belt-and-suspenders verification, a quarterly-audit habit, and an honest limitations section (GitHub "Verified" certifies key→account but not account→person; web edits sign as GitHub itself; signature meaning is §11.50 / OQ-060 not §11.70).
- `scripts/setup.sh` not modified — full enforcement requires admin permissions the standard `gh` flow doesn't have.
- **OQ-023 stays `:argued`.** The mechanical posture (no automated org-level enforcement in `setup.sh`) is unchanged; the new doc closes the *actionability* gap (adopters now have a step-by-step path) but not the *enforcement* gap. Upgrading to `:tested` would require either monitoring instrumentation outside this repo or end-to-end tests that don't compose with the required admin perms.
- **Status counts unchanged:** 19 `:tested` / 14 `:argued` / 6 `:open` / total 39.

**Public commit:** `86bda4f` (`2fe3ef6..86bda4f`) — 1 file / +113 / −0.

---

## v0.2.1 DRAFT — 2026-05-22

**P5 closed: complaint intake template + PHI/PII compartmentalization architecture.**

- **Complaint intake template** at `.github/ISSUE_TEMPLATE/complaint.yml` — fixes the v0.1.0 README/repo mismatch (README listed complaints; only CAPA/change-request/design-input/nonconformance existed). Form-validated intake with product, date received, source, severity, PHI-redacted description, regulatory reportability assessment, CAPA linkage, and a required PHI-handling confirmation block at the bottom.
- **Compartmentalization architecture** at `docs/guide/complaints.md` — explicit decision document: PHI/PII-bearing complaint content does NOT live in the main repo; it goes to a separate access-restricted record. Two patterns recommended: (A) sibling private GitHub repo under same Git discipline; (B) external eQMS or encrypted document store. Either satisfies the regulatory requirement; the adopting organization documents the choice in its complaint-handling SOP.
- **Medical-devices module manifest** gains ISO 13485 §8.2.2 (feedback) and 21 CFR 820.198 (complaint files) as clauses; complaint template bound to both. Module size: 4 → 6 clauses; 3 → 4 templates. Validation harness passes.
- **Spec deltas:**
  - **OQ-069 reframed.** Was "no complaint issue template" (defect). Now "complaint issue template — gap closed at v0.2.1" with the form-validated artifact as evidence. Stays `:tested`.
  - **OQ-062 transitioned `:open → :argued`.** Architecture decision documented; mechanically the constraint is on the adopter to follow the SOP.
  - **OQ-038 updated** (3 → 4 templates including complaint intake — wait, complaint is an issue template, not a document template; updated note to clarify the bound complaint template counts as an artifact in the manifest sense).
- **Status counts:** 19 `:tested` · 14 `:argued` · 6 `:open` · total 39.
- **Cross-audit (A0-A6):** clean.

**Public commit:** `2fe3ef6` (`4a72a9f..2fe3ef6`) — 3 files / +184 / −0.

---

## v0.2.0 DRAFT — 2026-05-22

**P1 closed: generator engine MVP shipped. P2 partial: medical-devices module seeded.**

- **Engine.** Shipped Open QMS generator engine as a Python package at `engine/` (Apache-2.0, hatchling build, pyyaml runtime dep, pytest dev dep):
  - `openqms.types` — frozen dataclasses: `Clause`, `ArtifactTemplate`, `Module`, `Bundle`, `ResolvedQMS`, `ValidationReport`.
  - `openqms.module.load_module` — YAML manifest loader with structural validation.
  - `openqms.resolver.resolve(Bundle, Module) -> ResolvedQMS` — pure function emitting the bidirectional clause-to-artifact traceability map.
  - `openqms.validation.validate(Module) -> ValidationReport` — per-module harness checking for orphaned clauses and orphaned artifacts.
  - `openqms.cli` — argparse CLI: `openqms resolve …` and `openqms validate …`, also reachable as `python -m openqms`.
- **Tests.** 15-test pytest suite: loader (4), resolver (5), validation (4), medical-devices integration smoke (2). All green locally (Python 3.14.4 + pytest 9.0.3 on Darwin).
- **CI.** New workflow `.github/workflows/engine-tests.yml` running pytest + `openqms validate --module medical-devices` on every push touching `engine/`, `modules/`, or `templates/`. Will go live on next push to main.
- **Medical-devices module.** First shipped regulatory module at `modules/medical-devices/module.yaml`: 4 clauses (ISO 13485 §4.2.4 + §7.3; 21 CFR 820 §820.30 + §820.40) bound to the 3 artifact templates currently in `templates/`. Validation passes. Replaces the `.gitkeep` placeholder; module `README.md` added.
- **Top-level README.** "What's included" lists the engine; new "Generator engine" section after Quick start; architecture diagram includes `engine/`; "How it works" gains module-clause-coverage row.
- **`.gitignore`.** Expanded to cover `.venv*/`, `*.egg-info/`, `.pytest_cache/`, `.ruff_cache/`, `.mypy_cache/`.
- **Spec status transitions** (5 entries advance):
  - OQ-001 `:argued → :tested` (evidence: `engine/tests/test_resolver.py::test_resolve_bidirectional_traceability` + `engine/tests/test_medical_devices.py::test_medical_devices_resolve_smoke`).
  - OQ-010 `:open → :tested` (evidence: `engine/tests/test_resolver.py::test_resolve_is_deterministic`, plus frozen-dataclass immutability, plus type annotations on `resolve()`).
  - OQ-013 `:open → :tested` (evidence: `engine/tests/test_validation.py` covering positive + both negative cases).
  - OQ-040 `:argued → :tested` (evidence: `modules/medical-devices/module.yaml` ships; harness passes).
  - OQ-066 `:open → :tested` (gap closed; same evidence as OQ-013).
- **Status counts:** 19 `:tested` · 13 `:argued` · 7 `:open` · 0 `:proved` / `:verified` / `:benchmarked`. Total 39.
- **Priority stack restructured.** P1 closed; P2 marked partial (~15% mechanized) with explicit remaining work; P1.1 (multi-module composition), P1.2 (standards-and-jurisdictions registry), and P1.3 (re-resolution on mutation) split out from the original P1.
- **Companion doc:** `BUSINESS/companion_engine_mvp.md` per discipline.
- **Cross-audit (A0-A6):** clean.

**Public commit:** `4a72a9f` (`43acffe..4a72a9f`) — 21 files / +1033 / −6.

---

## v0.1.2 DRAFT — 2026-05-22

**P4 closed: training-trigger YAML parsing tightened.**

- `.github/workflows/training-trigger.yml` — replaced regex-based parsing of `docs/qms-config.yml` with a Python 3.12 + PyYAML parse step. The new step:
  - Loads `docs/qms-config.yml` via `yaml.safe_load` and extracts the `trainees:` list, validating it is in fact a list (warns otherwise).
  - Parses each changed document's YAML frontmatter via `yaml.safe_load` to extract the `title:` field for the issue subject — handles quoted strings, block scalars, and nested mappings.
  - Emits a JSON payload to `GITHUB_OUTPUT` consumed by a downstream `actions/github-script` step that creates the training issues.
- **Behaviour preserved.** `config-missing → no issues created + warning`; `config-present-but-empty-trainees → issues created with placeholder text`. Same issue titles, bodies, and labels.
- **OQ-061 reframed.** Old claim was "training-trigger YAML parsing is brittle" (a defect description). New claim is "uses a real YAML parser, not regex — gap closed at v0.1.2" (post-fix state). Status remains `:tested` with the evidence pointing at the PyYAML parse step.
- **Status counts:** 14 `:tested` · 15 `:argued` · 10 `:open` · 0 `:proved` / `:verified` / `:benchmarked`. Total 39. (No status transitions; OQ-061 stays `:tested`, claim+notes updated.)
- **Cross-audit (A0-A6):** clean.

**Public commit:** `43acffe` (`7d05fc3..43acffe`) on `github.com/IridiumSoftware/OpenQMS` main.

---

## v0.1.1 DRAFT — 2026-05-22

**P3 closed: removed the broken trace-matrix script reference.**

- `docs/guide/traceability.md` — replaced the bullet pointing at `./scripts/generate-trace-matrix.sh` (which never existed) with a "Repository-wide traceability matrix (forward)" subsection that honestly frames the per-PR snippet as the Phase-0 surface and the full matrix as a Phase-1 generator-engine deliverable.
- **OQ-067 reframed.** Old claim was "trace-matrix script promised but missing" (a defect). New claim is "repository-wide trace matrix is forward work, not Phase 0" (the post-fix forward state). Status: `:open → :argued`. Evidence type: `none → manual`. Test/Proof file: now points at the forward-language section in the docs.
- **Status counts:** 14 `:tested` · 15 `:argued` · 10 `:open` · 0 `:proved` / `:verified` / `:benchmarked`. Total 39.
- **Cross-audit (A0-A6):** clean.
- **Observation deferred.** The YAML job ID `generate-trace-matrix` in `.github/workflows/traceability.yml:43` echoes the same misleading name. The job's display name ("Generate traceability snippet") is accurate; the YAML ID is not. Renaming would touch Actions run history and any branch-protection required-checks configured against the old name, so it's deferred to a deliberate cleanup pass rather than bundled with the docs fix.

**Public commit:** `7d05fc3` (`a2c8dec..7d05fc3`) on `github.com/IridiumSoftware/OpenQMS` main.

---

## v0.1.0 DRAFT — 2026-05-22

**Establish the spec.**

- Created the `BUSINESS/` discipline tree inside the Open QMS repository (gitignored): `ENGINE_SPEC.md`, `DESIGN.md`, `artifact_registry.md`, `dashboard.md`, `changelog.md`, and `regulatory_modules/medical_devices_crosswalk.md`.
- Spec landed with 39 entries across seven tiers:
  - **Invariant** (3): OQ-001 bidirectional traceability, OQ-002 mutation preserves invariant by reconstruction, OQ-003 unvalidated-MVP honesty bound. All `:argued`.
  - **Architecture** (6): OQ-010..OQ-015 — bundle resolver, module composition, overlay composition, per-module validation harness, registry, re-resolution-on-mutation. All `:open` (engine not yet built).
  - **Substrate** (5): OQ-020..OQ-024 — PR + required reviewers, branch protection, immutable history, GPG-signed commits, MkDocs rendering. Three `:tested`, two `:argued`.
  - **Workflow** (9): OQ-030..OQ-038 — doc-control CI, traceability CI, change-request / CAPA / NCR / design-input issue templates, release-gate CI, training-trigger CI, document templates. All `:tested`.
  - **Module** (9): OQ-040..OQ-048 — medical-devices module + per-standard coverage (ISO 13485, 21 CFR 820, Part 11, EU MDR, IEC 62304, IEC 62366-1, IEC 60601-1, ISTA 2A/3A, MDSAP) + ISO 27001 cross-cutting overlay. All `:argued`.
  - **Gap** (5 in Gap tier + 1 in Substrate-flavored gap): OQ-060 Part 11 §11.50 signature meaning, OQ-061 training-trigger YAML brittleness, OQ-062 PHI/PII compartmentalization, OQ-063 supplier eval, OQ-064 management review aggregation, OQ-065 module-version drift, OQ-066 generator validation harness, OQ-067 missing trace-matrix script, OQ-068 eleven empty template dirs, OQ-069 missing complaint template, OQ-080 README disclaimer. Mix of `:open` (6) and `:tested` (3 + OQ-080).
  - **Licensing** (2): OQ-070 modules reference clauses by number + summary; OQ-071 Apache-2.0 doesn't extend to standards. Both `:argued`.
- Status summary: 14 `:tested` · 14 `:argued` · 11 `:open` · 0 `:proved` / `:verified` / `:benchmarked`. Phase 0 (scaffold + workflows) is mostly `:tested`; Phase 1 (generator engine) is uniformly `:open`.
- Cross-audit (A0–A6) ran clean: 100% spec coverage in registry, no orphan paths, no status-evidence mismatches, dashboard counts match ENGINE_SPEC counts.

**Background.** Prior to today, the spec lived at `~/Desktop/Research Papers/Relational_Emergence/Closure v5/BUSINESS/GitHub_QMS_Spec_Medical_Devices.md` as a single prose document (v1.0 DRAFT 2026-04-02 by NeuraSignal Operations; widened to v2.0 DRAFT 2026-05-22 to reflect the generator vision). That document is preserved as historical reference. ENGINE_SPEC.md + DESIGN.md + medical_devices_crosswalk.md are the authoritative replacement and apply TCE discipline: every named claim carries an S-ID, evidence type, status, and registry row.

**Public repository (separate from this BUSINESS/ tree).** As of 2026-05-22, the public `github.com/IridiumSoftware/OpenQMS` (commit `02f4a5c`) contains:
- README with Standards Licensing section added today (pushed live before BUSINESS/ work began).
- Five functional CI workflows (doc-control, traceability, release-gate, training-trigger, deploy-docs).
- Four functional issue templates (CAPA, change-request, design-input, nonconformance).
- Three document templates (quality policy, SOP, design input).
- Setup script with branch protection + label configuration.
- MkDocs site (docs/) with guides and regulatory reference.
- Apache-2.0 license, CODEOWNERS, CONTRIBUTING.

**Priority stack at end-of-session (full detail in `dashboard.md`):**
1. Build the generator engine MVP (CLI bundle resolver) — load-bearing for Phase 1.
2. Convert medical-devices crosswalk into machine-readable module under `modules/medical-devices/`.
3. Resolve OQ-067 (trace-matrix script promised but missing) — doc-only fix recommended now.
4. Tighten training-trigger YAML parsing (OQ-061).
5. Add complaint issue template OR document the deferral (OQ-069, OQ-062).
6. Populate high-priority empty template subdirectories (OQ-068).
7. Document org-level GPG enforcement in setup script (OQ-023).
8. Part 11 §11.50 signature-meaning prototype (OQ-060) — natural Honest Framework dock point.
9. Module-version drift detection (OQ-065) — Phase 1+.
10. Decide on public release of BUSINESS/ contents (governance posture for Open Honest engagement).

---

## Earlier history (pre-BUSINESS/)

- **2026-05-22** — Standards Licensing section added to public README (commit `02f4a5c`); v2.0 DRAFT spec written at closure-v5 location.
- **2026-05-05** — Mkdocs configuration fix + manual deploy trigger added (commits `72d057d`, `0114cb3`).
- **2026-04-21** — Initial repository scaffold (commit `2431de6`): templates, workflows, CODEOWNERS, README, mkdocs, setup script.
- **2026-04-02** — v1.0 DRAFT spec authored at NeuraSignal as a feasibility analysis for GitHub-as-QMS in the medical-device context (now historical, at closure-v5 BUSINESS location).
