# Companion — v0.52.0 through v0.63.0 (12-release omnibus: trust gate + reviewer-feedback closures + Pages refresh)

**Session date:** 2026-05-25 (continuation arc from the v0.48-v0.51 omnibus session)
**Engine version transitions:** 0.51.0 → 0.63.0 (12 releases)
**Why combined companion:** 12 small-to-medium releases sharing one continuous arc — the post-v0.51 build picked up adopter feedback (P1-P4) and an independent reviewer's technical assessment (P5-P14), then iterated through the forward-work queue in priority order. Combining into one omnibus is proportionate per the v0.46-v0.47 + v0.48-v0.51 omnibus precedents; no single release warrants standalone treatment but the combination is substantial (9 new spec entries, 6 module-shape closures of P-items, +122 pytest tests, +1 CLI subcommand, +2 SOP templates, +4 preset bundles, +5 issue templates, +5 role/process guides, +1 trust-gate document, +1 cadence governance document, +1 audit-artifact emission workflow, +1 verify-deployment workflow, refreshed Pages site).

## §1 Computational basis

13 sequential releases (12 substantive + 1 polishing) closing the v0.46-v0.50 arc and the entire v0.52-v0.62 forward-work P-series:

| Version | Theme | Public commit | Spec entries |
|---|---|---|---|
| v0.51.0 | Polishing pass closing v0.46-v0.50 arc | `be6f606` | (none — bookkeeping) |
| v0.52.0 | Compliance architecture trust-gate document (adopter-feedback P1) | `debdb13` | OQ-119 NEW `:tested` |
| v0.53.0 | Reviewer-feedback integration — forward-work expansion (P5-P14 added) | `d5e3eed` | (none — doc refinement) |
| v0.54.0 | Effort qualifiers on forward-work tables | `8922608` | (none — doc refinement) |
| v0.55.0 | Light-batch hardening release (closes P6 + P7 + P8 + P12 + P13 + P14) | `ee76126` | OQ-120 NEW `:tested` |
| v0.56.0 | P15 added (integration-architecture cross-record trace network) | `361a9c9` | (none — doc refinement) |
| v0.57.0 | Non-technical UX batch (closes P3) | `04ff572` | OQ-121 NEW `:tested` |
| v0.58.0 | Template frontmatter schema validation (closes P9) | `448bba7` | OQ-122 NEW `:tested` Architecture-tier |
| v0.59.0 | Negative-path test suite for bad modules (closes P10) | `3789072` | OQ-123 NEW `:tested` |
| v0.60.0 | Doc-control workflow hardening (closes P5) | `a8e4e1c` | OQ-124 NEW `:tested` Architecture-tier |
| v0.61.0 | Startup-stage presets (closes P4) | `c872026` | OQ-125 NEW `:tested` |
| v0.62.0 | Verify-deployment subcommand (closes P11) — closes medium queue | `353bc3c` | OQ-126 NEW `:tested` Architecture-tier |
| v0.63.0 | Pages site refresh | `9702568` | OQ-127 NEW `:tested` |

**Aggregate deliverables:**

- **9 NEW spec entries** (OQ-119 + OQ-120 + OQ-121 + OQ-122 + OQ-123 + OQ-124 + OQ-125 + OQ-126 + OQ-127)
- **3 NEW Architecture-tier entries** (OQ-122 + OQ-124 + OQ-126 — all new CLI / workflow surfaces parallel to OQ-115/116/117 pattern)
- **6 forward-work priorities CLOSED via OQ-120 light batch** (P6 lockfile + P7 signed tags + P8 CI archival + P12 identity-mapping SOP + P13 backup-restore SOP + P14 regulatory-review cadence)
- **6 forward-work priorities CLOSED via dedicated releases** (P1 OQ-119 + P3 OQ-121 + P9 OQ-122 + P10 OQ-123 + P5 OQ-124 + P4 OQ-125 + P11 OQ-126) → 12 total closed in this arc
- **2 NEW engine modules** (`engine/openqms/template_schema.py` + `engine/openqms/doc_control.py` + `engine/openqms/verify_deployment.py` = 3 actually)
- **3 NEW CI scripts** (`scripts/lint-template-frontmatter.py` + `scripts/doc-control-check.py` + `scripts/verify-deployment.sh`)
- **1 NEW CLI subcommand** (`openqms verify-deployment`) — count 9 → 10
- **5 NEW issue templates** (training-completion + document-review + access-review + restoration-test + regulatory-review) — count 7 → 12
- **5 NEW role/process guides** (onboarding + role-quality-manager + role-engineer + document-routing + capa-lifecycle) — `docs/guide/` count 12 → 17 → 19 (also added template-frontmatter + verify-deployment)
- **2 NEW SOP templates** (IDENTITY-MAPPING-SOP + BACKUP-RESTORE-SOP) — template count 103 → 105
- **4 NEW preset bundles** (pre-seed + seed + series-a + series-b-plus) with matrix baselines + per-stage READMEs
- **1 NEW workflow** (`.github/workflows/release-artifact.yml`)
- **1 REWRITTEN workflow** (`.github/workflows/doc-control.yml` — PyYAML parsing + state-machine + audit-artifact emission)
- **1 NEW compliance-architecture trust-gate document** (`docs/compliance-architecture.md`)
- **1 NEW regulatory-review cadence governance document** (`BUSINESS/regulatory_review_cadence.md`)
- **1 NEW maturity-model guide** (`docs/guide/maturity-model.md`)
- **1 NEW deployment-policy example** (`deployment-policy.example.yaml`)
- **1 NEW engine lockfile** (`engine/uv.lock`)
- **Refreshed Pages site** (`mkdocs.yml` nav 4-item → 7-section ~25 entries; `docs/index.md` rewritten)
- **Pytest count 129 → 251** (+122 across the arc):
  - +13 in v0.49 (test_coverage + test_crosswalk + test_jurisdictions_query — pre-arc)
  - +23 in v0.58 (test_template_schema)
  - +23 in v0.59 (test_negative_modules)
  - +38 in v0.60 (test_doc_control)
  - +15 in v0.61 (test_presets)
  - +23 in v0.62 (test_verify_deployment)
- **Cross-overlay count unchanged at 12** (final batch shipped at v0.50.0)
- **Module count unchanged at 116** (all P-closures shipped without new modules; OQ-125 presets reference existing modules)
- **Cross-cutting overlay count unchanged at 26** (us-state-privacy at v0.48.0 was the last)

## §2 Results — closed forward-work priorities

The two reviewer-feedback inputs (adopter-experience P1-P4 from 2026-05-25 round 1; independent-technical P5-P14 from 2026-05-25 round 2; P15 from 2026-05-25 round 3) drove the arc. Status after v0.63.0:

| Priority | Effort | Status | Closing release |
|---|---|---|---|
| P1 | medium | ✓ closed | v0.52.0 (OQ-119) |
| P2 | hard | open | — |
| P3 | medium | ✓ closed | v0.57.0 (OQ-121) |
| P4 | medium | ✓ closed | v0.61.0 (OQ-125) |
| P5 | medium | ✓ closed | v0.60.0 (OQ-124) |
| P6 | light | ✓ closed | v0.55.0 (OQ-120 batch) |
| P7 | light | ✓ closed | v0.55.0 (OQ-120 batch) |
| P8 | light | ✓ closed | v0.55.0 (OQ-120 batch) |
| P9 | medium | ✓ closed | v0.58.0 (OQ-122) |
| P10 | medium | ✓ closed | v0.59.0 (OQ-123) |
| P11 | medium | ✓ closed | v0.62.0 (OQ-126) |
| P12 | light | ✓ closed | v0.55.0 (OQ-120 batch) |
| P13 | light | ✓ closed | v0.55.0 (OQ-120 batch) |
| P14 | light | ✓ closed | v0.55.0 (OQ-120 batch) |
| P15 | hard | open | — |

**13 of 15 priorities closed across this 13-release arc** (12 substantive + 1 polishing). The 2 remaining are both hard (P2 validation package + P15 integration trace network); both are multi-session deliverables requiring dedicated scope decisions.

## §3 Verification

Per-entry verification status (all `:tested` via example-tested evidence; specific tests cited in `BUSINESS/artifact_registry.md`):

- **OQ-119** — Document-review check + every spec-entry citation resolves + every file pointer resolves via `git ls-files` + CLI examples reference shipped subcommands.
- **OQ-120** — `engine/uv.lock` generated + CI workflow asserts lockfile presence + `release-artifact.yml` ships + SOP templates ship with frontmatter + addresses bindings + 129/129 pytest pass.
- **OQ-121** — All 5 issue templates use the GitHub Issue Forms YAML schema + all 5 guides follow docs/guide/ markdown convention with linkage to spec entries + 129/129 pytest pass.
- **OQ-122** — 23 new tests in `test_template_schema.py` (parse + validate per-field + lint + aggregate + **repo-wide invariant** asserting all shipped templates pass schema); CI gate runs `scripts/lint-template-frontmatter.py` as pre-pytest step; 152/152 pytest pass.
- **OQ-123** — 23 new tests in `test_negative_modules.py` covering 6 categories of broken-by-construction fixtures; 175/175 pytest pass.
- **OQ-124** — 38 new tests in `test_doc_control.py` (state-transition allowed/disallowed + version-drift exemptions + audit-artifact serialization + Markdown rendering); 213/213 pytest pass.
- **OQ-125** — 15 new tests in `test_presets.py` (bundle-loads-cleanly + module-count + modules-exist-on-disk + monotonic-progression + matrix-files-present + READMEs-present); CI-gated via `openqms regenerate --bundle presets/<name>.yaml` dry-run; 228/228 pytest pass.
- **OQ-126** — 23 new tests in `test_verify_deployment.py` using injected `gh_invoker` callable for testability; 251/251 pytest pass.
- **OQ-127** — `mkdocs build --strict` runs clean (zero broken links / no warnings); local build smoke test produced `site/` directory with all 19+ pages.

All entries pass verification at v0.63.0.

## §4 Spec impact

Status counts progression across the arc:

| Release | :verified | :tested | :argued | :open | Total |
|---|---|---|---|---|---|
| v0.51.0 (start of arc) | 6 | 91 | 5 | 0 | **102** |
| v0.52.0 | 6 | 92 | 5 | 0 | **103** (+OQ-119) |
| v0.53.0-v0.54.0 | 6 | 92 | 5 | 0 | 103 (doc-only) |
| v0.55.0 | 6 | 93 | 5 | 0 | **104** (+OQ-120) |
| v0.56.0 | 6 | 93 | 5 | 0 | 104 (doc-only) |
| v0.57.0 | 6 | 94 | 5 | 0 | **105** (+OQ-121) |
| v0.58.0 | 6 | 95 | 5 | 0 | **106** (+OQ-122) |
| v0.59.0 | 6 | 96 | 5 | 0 | **107** (+OQ-123) |
| v0.60.0 | 6 | 97 | 5 | 0 | **108** (+OQ-124) |
| v0.61.0 | 6 | 98 | 5 | 0 | **109** (+OQ-125) |
| v0.62.0 | 6 | 99 | 5 | 0 | **110** (+OQ-126) |
| v0.63.0 | 6 | 100 | 5 | 0 | **111** (+OQ-127) |

Net: +9 spec entries across the arc; status mix unchanged (still 6 `:verified` + 5 `:argued` + 0 `:open` + 0 `:proved` + 0 `:benchmarked`; only `:tested` grew).

## §5 Lessons + observations

- **The forward-work model worked.** Effort qualifiers (light / medium / hard) added at v0.54.0 enabled the v0.55.0 light-batch decision ("ship 6 lights in one release") which would have been awkward without the labels. Per-priority effort assessment is a small upfront investment that compounds across the arc.
- **Light-batching is high-leverage.** 6 priorities closed in 1 release at v0.55.0; would have been 6 releases otherwise. The pattern works when items share enough common infrastructure (in this case: SOP templates + governance docs + light CI/workflow additions).
- **OQ-122 → OQ-124 → OQ-126 are a natural chain.** Each Architecture-tier addition builds on the prior — template_schema (static-shape) → doc_control (temporal-shape, depends on schema) → verify-deployment (deployment-shape, depends on identity-mapping SOP which depends on template_schema). The chain reflects a real architectural layering, not coincidence.
- **OQ-122/OQ-123 + OQ-124/OQ-122 pairs.** Each Architecture-tier release that adds a rejection-surface (template schema; doc-control state machine) is followed within 1-2 releases by an explicit negative-path test suite (OQ-123) or close-companion test suite (OQ-124's 38 tests). Pattern: surface-then-test.
- **OQ-127 Pages refresh closed an OQ-097 carry-over.** OQ-097 (v0.23.0 public adopter-surface release) refreshed README + introduced docs/modules-catalog.md but didn't include mkdocs.yml + docs/index.md. The omission lingered ~40 releases until user flagged "Pages demo looks stale" at v0.62-retrospective. Lesson: when scope explicitly carves out a deliverable, name what's NOT in scope so it goes in the forward-work queue rather than being silently deferred.
- **`mkdocs build --strict` is a worthwhile local gate.** Caught zero issues at v0.63 because the rewrite was careful, but the lack of `--strict` in the deploy workflow means a sloppy commit could deploy broken links. (Forward improvement candidate, light effort.)
- **Per-release scope-cell update discipline was lapsing** (audit F-A + F-B + F-C). Caught at this audit; remediated inline. Future improvement: add "update README + catalog scope cells" to per-release CLAUDE.md checklist — but this is project-specific discipline, not engine code.

## §6 What's still open after v0.63.0

| Priority | Why open |
|---|---|
| **P2** — Validation package templates (URS + IQ/OQ/PQ + Change Assessment + CSV protocol + Validation Master Plan) | Hard effort; multi-session; the largest customer-facing deliverable remaining. The natural compose-partner is OQ-122 template schema (validation templates will inherit the frontmatter pattern). |
| **P15** — Integration-architecture cross-record trace network (requirements ↔ hazards ↔ mitigations ↔ testing ↔ CAPA ↔ complaints ↔ PMS) | Hard effort; multi-session. The strategic differentiator per reviewer #2 ("connectedness is where modern systems win"). Builds on OQ-001 + OQ-067 clause-level trace + new instance-level trace primitives. |

These are genuinely hard. Each warrants its own session plan + scope decision before kickoff.

## §7 Linkage

- `audit_2026-05-25_v0_63.md` — A0-A6 cross-audit run as part of v0.64.0 omnibus release
- `companion_v0_48_to_51.md` — prior omnibus (v0.48-v0.51 arc)
- `companion_v0_46_v0_47.md` — prior pair-arc (v0.46-v0.47)
- `compliance-architecture.md` §"Forward work" — per-priority closed-state callouts
- `dashboard.md` §"Latest" — v0.64.0 entry summarizes this companion
- `changelog.md` — per-release detail (v0.51.0 through v0.64.0)
