# Companion — Class-overlay completion + general manufacturing vertical (v0.17.0)

**Session date:** 2026-05-23
**Engine version transition:** 0.16.0 → 0.17.0
**Commit:** `f617b2e` (8 class overlays + manufacturing vertical + example bundle + CI extension + engine version bump in one commit)

---

## §1 Computational basis

### What was built

Two parallel deliverables:

1. **Completes class-overlay coverage** for aerospace and automotive. v0.16.0 shipped 6 class overlays bracketing the rigor spectrum but leaving gaps. v0.17.0 fills the gaps: 2 aerospace DALs (D, E) + 3 automotive ASILs (C, A, QM) + 3 automotive CALs (3, 2, 1) = 8 new class overlays.
2. **New 4th vertical: general manufacturing** — ISO 9001:2015 only. The baseline QMS for non-regulated manufacturing (machine shops, tooling, contract manufacturing, custom fab, job shops, fabrication houses, prototyping shops, light industrial). Opens Open QMS to a new audience: organizations that need a credible QMS without a domain-specific regulatory framework.

### Files added

**Class overlays (8 modules, 34 clauses, ~620 LOC of YAML):**

| Path | Encodes | Clauses |
|---|---|---|
| `modules/aerospace-dal-d/module.yaml` | DAL-D — Minor failure condition; no structural coverage; 2-of-26 independence; TQL-4/5 | 5 |
| `modules/aerospace-dal-e/module.yaml` | DAL-E — No Safety Effect; NO DO-178C objectives; configuration management only | 4 |
| `modules/automotive-asil-c/module.yaml` | ASIL-C — SPFM ≥ 97% / LFM ≥ 80% / PMHF < 10⁻⁷/h; 100% stmt+branch; I3; MISRA C required | 5 |
| `modules/automotive-asil-a/module.yaml` | ASIL-A — PMHF < 10⁻⁶/h (no SPFM/LFM); 100% statement; I1; MISRA C recommended | 5 |
| `modules/automotive-qm/module.yaml` | QM — positive QM claim with HARA rationale; explicit out-of-FuSa-scope Safety Plan listing | 4 |
| `modules/automotive-cal-3/module.yaml` | CAL-3 — independent assessment recommended; fuzz required; formal monitoring | 5 |
| `modules/automotive-cal-2/module.yaml` | CAL-2 — independent assessment optional; vulnerability scanning; triage cadence | 4 |
| `modules/automotive-cal-1/module.yaml` | CAL-1 — no independent assessment; baseline V&V; CSMS-baseline monitoring | 4 |

**General manufacturing vertical:**

| Path | Purpose | Clauses |
|---|---|---|
| `modules/manufacturing/module.yaml` | ISO 9001:2015 across all 7 §-groups; all bindings to existing cross-cutting templates | 17 |
| `modules/manufacturing/README.md` | Module documentation — scope, target audience, when to use vs. migrate up to regulated vertical, forward work | — |
| `bundles/example-machine-shop.yaml` | Example bundle for a precision machine shop composing manufacturing + iso-27001 (empty jurisdictions list) | — |
| `bundles/example-machine-shop.matrix.json` | Committed baseline matrix | — |

### Files modified

| Path | Change |
|---|---|
| `.github/workflows/engine-tests.yml` | Validate step extended with 15 new lines (2 new aerospace DALs + 3 ASILs + 3 CALs + 1 manufacturing standalone + 1 composite + 5 minor reorderings); regenerate step extended with example-machine-shop |
| `engine/openqms/__init__.py` | `__version__ = "0.17.0"` |
| `engine/pyproject.toml` | `version = "0.17.0"`; keywords gained `manufacturing`, `iso-9001`, `machine-shop` |

### Build / test commands run

```bash
# Aerospace DALs
for dal in d e; do
  openqms validate --module aerospace --module aerospace-dal-$dal
done
# both → invariant_holds: True

# Automotive ASILs
for asil in c a qm; do
  openqms validate --module automotive --module automotive-asil-$asil 2>/dev/null \
    || openqms validate --module automotive --module automotive-$asil
done
# all three → invariant_holds: True (asil-c, asil-a, qm — qm doesn't have the asil- prefix)

# Automotive CALs
for cal in 3 2 1; do
  openqms validate --module automotive --module automotive-cal-$cal
done
# all three → invariant_holds: True

# Manufacturing standalone + composite
openqms validate --module manufacturing
# → invariant_holds: True
openqms validate --module manufacturing --module iso-27001
# → invariant_holds: True

# Bundle baseline + idempotence
openqms regenerate --bundle example-machine-shop --write-matrix
openqms regenerate --bundle example-machine-shop
# → exit 0; (no changes)

# Full test suite
pytest engine/tests -q
# → 108 passed in 10.71s
```

### Dependencies

No engine code changes. No new dependencies. No new registry standards (overlays cite standards already in the registry from v0.14.0/v0.15.0; manufacturing cites ISO 9001:2015 which was added at v0.14.0 with aerospace). No new templates (overlays bind to existing PSAC, SSP, Safety Concept, TARA, SOP, Software Test Protocol, Verification Protocol templates; manufacturing binds to existing cross-cutting templates).

### Class-overlay clause breakdown (delta-pattern by overlay)

**Aerospace DAL-D (5):** DAL-D-applicability, DO178C-no-structural-coverage (Table A-7 N/A), DO178C-independence-DAL-D (2-of-26 typically QA + SCM), DO178C-tool-qual-DAL-D (TQL-4/5), ARP4754A-DAL-D-allocation.

**Aerospace DAL-E (4):** DAL-E-applicability (FHA No-Safety-Effect substantiation is load-bearing), DO178C-no-objectives (§2.2.4 — no DO-178C process discipline), DAL-E-configuration-management (still required so cert authority can verify deployed software), ARP4754A-DAL-E-allocation (isolation + failure-impact substantiation).

**Automotive ASIL-C (5):** ASIL-C-applicability (S3 × E4 × C2, S3 × E3 × C3, S2 × E4 × C3 per Table 4); ASIL-C-HW-metrics (SPFM ≥ 97% / LFM ≥ 80% / PMHF < 10⁻⁷/h — mid-high between ASIL-D 99%/90%/10⁻⁸ and ASIL-B 90%/60%/10⁻⁷); ASIL-C-SW-coverage (100% stmt + 100% branch; MC/DC recommended — the major delta from ASIL-D); ASIL-C-confirmation-I3 (same as ASIL-D — the major delta from ASIL-B's I2 — this is the often-underappreciated cost-jump between ASIL-B and ASIL-C); ASIL-C-SW-methods (language subset REQUIRED — vs. recommended at ASIL-B).

**Automotive ASIL-A (5):** ASIL-A-applicability (S1 × E4 × C3, S2 × E2 × C3, S2 × E3 × C2; S1 × E4 × C1 → QM, not ASIL-A); ASIL-A-HW-metrics (PMHF < 10⁻⁶/h, NO quantitative SPFM/LFM targets); ASIL-A-SW-coverage (100% statement only — branch + MC/DC recommended; major delta from ASIL-B which mandates branch); ASIL-A-confirmation-I1 (different person within the same team); ASIL-A-SW-methods (all recommended-not-required).

**Automotive QM (4):** QM-applicability (S1 × E4 × C1, S0 × any × any, S2 × E1 × any); QM-no-ISO26262-rigor (Part 2 §5.4.1 — baseline IATF 16949 + ISO 9001 applies); QM-HARA-rationale (load-bearing — mis-classification omits required FuSa rigor); QM-safety-plan-listing (explicit out-of-FuSa-scope with HARA cross-reference — enables confirmation reviewer / FuSa auditor to verify appropriate scoping, not silent omission).

**Automotive CAL-3 (5):** CAL-3-applicability (Annex E moderate-impact/high-feasibility or high-impact/moderate-feasibility); CAL-3-recommended-independent-assessment (vs. required at CAL-4, optional at CAL-2); CAL-3-V-and-V-fuzz (fuzz REQUIRED; pentest recommended; side-channel not required vs. required-where-applicable at CAL-4); CAL-3-formal-monitoring (response-time commitments in CSMS + defined playbooks; rehearsal recommended); CAL-3-safety-security-when-ASIL (when item is also ASIL-rated).

**Automotive CAL-2 (4):** CAL-2-applicability; CAL-2-optional-independent-assessment; CAL-2-V-and-V-scanning (baseline + vulnerability scanning; fuzz + pentest recommended); CAL-2-monitoring-triage (documented triage cadence; no formal response-time for fix deployment).

**Automotive CAL-1 (4):** CAL-1-applicability (low impact AND low feasibility); CAL-1-no-independent-assessment; CAL-1-baseline-V-and-V (functional only — no fuzz / pentest / side-channel); CAL-1-CSMS-baseline-monitoring.

### Manufacturing vertical clause breakdown (17 total)

By §-group: Context (§4) — 2 clauses (4.1, 4.4); Leadership (§5) — 2 (5.1, 5.2); Planning (§6) — 1 (6.1); Support (§7) — 4 (7.1, 7.1.5.2, 7.4, 7.5); Operation (§8) — 5 (8.1, 8.4, 8.5, 8.5.5, 8.7); Performance evaluation (§9) — 3 (9.1, 9.2, 9.3); Improvement (§10) — 1 (10.2).

All bind to cross-cutting templates already in Open QMS: quality-policy.md, SOP-TEMPLATE.md, AUDIT-PROCEDURE-TEMPLATE.md, MANAGEMENT-REVIEW-TEMPLATE.md, APPROVED-SUPPLIER-LIST-TEMPLATE.md, SUPPLIER-EVALUATION-TEMPLATE.md, capa.yml, nonconformance.yml. NO new templates required — manufacturing is the smallest vertical in the project, intentionally minimal.

---

## §2 Results

### All 8 class overlays validate standalone

Each overlay validates clean composed with its baseline vertical (aerospace or automotive). The OQ-013 validation harness asserts the OQ-001 invariant (bidirectional clause-to-artifact traceability) holds for the composed union. Overlay clauses bind to templates already shipped by the vertical — no new templates needed.

### Manufacturing vertical validates standalone + composite

Validates clean as `manufacturing` standalone and as `manufacturing + iso-27001` composite. The empty `jurisdictions:` list in the example bundle is accepted by the resolver — general manufacturing has no specific regulator, which is correct modeling for the use case.

### Class-overlay coverage now complete

| Vertical | Overlay set | Completeness |
|---|---|---|
| medical-devices | samd, implantable, mdr-class-iii, mdr-class-iib, mdr-class-iia, fda-class-iii, fda-class-ii | 7 / 7 — complete for shipped scope; IVDR-class-c/d forward |
| aerospace DAL | A, B, C, D, E | 5 / 5 — **complete** |
| automotive ASIL | D, C, B, A, QM | 5 / 5 — **complete** |
| automotive CAL | 4, 3, 2, 1 | 4 / 4 — **complete** |

Total 21 class overlays across three regulated verticals. Plus the new general-manufacturing vertical (no class overlays — ISO 9001 has no equivalent of DAL/ASIL/CAL rigor tiers).

### Vertical count: 3 → 4

Open QMS now ships verticals for:

- **medical-devices** (ISO 13485 + 21 CFR 820 + Part 11 + EU MDR + ISO 14971 + IEC 62304 + IEC 62366-1 + IEC 60601-1 + ISTA + MDSAP — 62 clauses across 11 standards)
- **aerospace** (ISO 9001 + AS9100D + 14 CFR Part 21 + EASA Part 21 + DO-178C + DO-254 + ARP4754A + ARP4761 + AS9102 — 27 clauses across 9 standards)
- **automotive** (ISO 9001 + IATF 16949 + ISO 26262 + ISO/SAE 21434 + UN R155 + UN R156 + Automotive SPICE 4.0 + AIAG PPAP — 28 clauses across 8 standards)
- **manufacturing** (ISO 9001 — 17 clauses across 1 standard — the smallest and most foundational vertical)

Open QMS now serves both regulated (medical/aero/auto) AND non-regulated (manufacturing) manufacturing scopes — an audience expansion.

### Test count unchanged at 108

Modules are content, not engine code. Validation surface exercised through CI (16 net new validate + regenerate steps).

### Pattern observation: structural-generalization claim now hardens significantly

The v0.14.0 (aerospace) → v0.15.0 (automotive) arc established a 2-data-point case that the platform composition generalizes off the medical-devices substrate. v0.17.0's manufacturing addition brings the 4th vertical — a substantively different shape (smallest, no class overlays, no domain-specific extensions, pure ISO 9001 baseline). The same OQ-011 compose primitive (built in medical-devices context at v0.4.0, unchanged) handles this 4th-vertical case without engine code change. The structural-generalization claim from v0.14.0/v0.15.0 is now substantiated by 4 data points across 3 markedly different shapes (regulated FuSa+cyber+QMS; non-regulated baseline QMS).

---

## §3 Verification

### OQ-079, OQ-081 through OQ-088 — example-tested → `:tested` (nine entries)

**Evidence type:** example-tested (all nine).

**Test surface for each class overlay:**

1. `openqms validate --module <vertical> --module <overlay>` exercises the OQ-013 validation harness against the composed module; harness asserts the OQ-001 invariant on the union of (vertical clauses + overlay clauses, vertical bindings + overlay bindings). All locally pre-commit: `invariant_holds: True`.
2. CI workflow extension at `.github/workflows/engine-tests.yml` runs the per-overlay validate on every push touching `engine/`, `modules/`, `registry/`, `templates/`, or `bundles/`.

**Test surface for OQ-088 (manufacturing vertical):**

1. `openqms validate --module manufacturing` — OQ-013 harness verifies the OQ-001 invariant; OQ-014 registry verifies the single standard (ISO 9001:2015).
2. `openqms validate --module manufacturing --module iso-27001` — exercises OQ-011 + OQ-012 + OQ-013 composition path with vertical + overlay.
3. `openqms regenerate --bundle example-machine-shop --write-matrix` — OQ-014 (registry lookup) + OQ-015 (regenerate). Baseline written; idempotent re-run yields no diff.

**What's covered:** structural well-formedness; composability; CI regression-detection.

**What's not covered:** semantic correctness of the rigor-delta claims for class overlays + the ISO 9001 clause-to-artifact mapping for manufacturing — adopter V&V evidenced by certification audit (OQ-080 disclaimer).

**Status:** all nine at `:tested`. Property-test upgrade to `:verified` may become tractable once enough class overlays exist to share invariants — pattern emerging strongly with 21 class overlays now shipped, perhaps revisit in a future session.

### Existing entries unaffected

No status transitions. OQ-079..OQ-088 are strictly additive. Engine code paths (OQ-010, OQ-011, OQ-013, OQ-014, OQ-015) are exercised by the new content; their `:verified` status (from v0.13.0 property tests) is unchanged.

---

## §4 Spec impact

### New entries

| S-ID | Tier | Evidence type | Status | Depends_on | Claim summary |
|---|---|---|---|---|---|
| **OQ-079** | Module | example-tested | `:tested` | OQ-011, OQ-059 | Aerospace DAL-D overlay (Minor; no structural coverage; 2-of-26 independence; TQL-4/5; 5 clauses) |
| **OQ-081** | Module | example-tested | `:tested` | OQ-011, OQ-059 | Aerospace DAL-E overlay (No Safety Effect; NO DO-178C objectives; config-mgmt-only; 4 clauses) |
| **OQ-082** | Module | example-tested | `:tested` | OQ-011, OQ-072 | Automotive ASIL-C overlay (SPFM ≥ 97% / LFM ≥ 80% / PMHF < 10⁻⁷/h; I3 — same as ASIL-D; language subset required; 5 clauses) |
| **OQ-083** | Module | example-tested | `:tested` | OQ-011, OQ-072 | Automotive ASIL-A overlay (PMHF < 10⁻⁶/h; 100% statement only; I1; recommended methods; 5 clauses) |
| **OQ-084** | Module | example-tested | `:tested` | OQ-011, OQ-072 | Automotive QM overlay (positive QM claim with HARA rationale + explicit Safety Plan listing as out-of-FuSa-scope; 4 clauses) |
| **OQ-085** | Module | example-tested | `:tested` | OQ-011, OQ-072 | Automotive CAL-3 overlay (independent assessment recommended; fuzz required; formal monitoring; safety-security interaction when ASIL-rated; 5 clauses) |
| **OQ-086** | Module | example-tested | `:tested` | OQ-011, OQ-072 | Automotive CAL-2 overlay (optional assessment; vulnerability scanning; triage cadence; 4 clauses) |
| **OQ-087** | Module | example-tested | `:tested` | OQ-011, OQ-072 | Automotive CAL-1 overlay (no independent assessment; baseline V&V; CSMS-baseline monitoring; 4 clauses) |
| **OQ-088** | Module | example-tested | `:tested` | OQ-011, OQ-014 | General manufacturing vertical (ISO 9001:2015 only; 17 clauses across all 7 §-groups; all bindings to cross-cutting templates) |

### Status transitions on existing entries

None.

### Counts

- **Before v0.17.0:** 6 `:verified` / 50 `:tested` / 7 `:argued` / 0 `:open` (total 63).
- **After v0.17.0:** 6 `:verified` / 59 `:tested` / 7 `:argued` / 0 `:open` (total **72**).
- Module-tier entries: 27 → 36 (OQ-040..OQ-059 + OQ-072..OQ-079 + OQ-081..OQ-088).
- Vertical count: 3 → 4 (medical-devices / aerospace / automotive / manufacturing).
- Class-overlay count across all verticals: 13 → 21 (medical-devices 7 + aerospace 5 + automotive 9).

### S-ID numbering note

OQ-080 was previously assigned to a Gap entry (README disclaimers). The Module entries skip from OQ-079 to OQ-081 to preserve the OQ-080 assignment. The next free S-ID for a future Module entry is OQ-089.

### Forward spec entries (not opened, surfaced for future sessions)

- **Food safety vertical** — ISO 22000 + FSSC 22000 + HACCP.
- **Pharma GMP vertical** — ICH Q7 + 21 CFR 210/211 + EudraLex Vol. 4 + PIC/S Annex 1.
- **Industrial machinery functional safety** — IEC 61508 + ISO 13849.
- **Cross-cutting overlays** — ISO 14001 environmental, ISO 45001 OH&S, ISO 50001 energy, ISO 37001 anti-bribery.
- **IVDR class overlays** — ivdr-class-c, ivdr-class-d.
- **Aerospace defense overlay** — MIL-STD-882, ITAR, EAR procedural discipline.
- **Automotive defense overlay** — MIL-STD-882 + ITAR + EAR.
- **NHTSA Part 573 recall workflow** — cross-cutting workflow.
- **Quality manual + process map + risk-and-opportunity register templates for manufacturing** — surfaced in `modules/manufacturing/README.md` forward-work list.
- **Rigor-level overlay generator** — meta-pattern question (with 21 class overlays now).

None opened as `:open` today; pending adopter need.

### Engine version

0.16.0 → 0.17.0. No engine code change; version + keyword expansion (`manufacturing`, `iso-9001`, `machine-shop`).

---

## Cross-audit (A0-A6) — clean

| Check | Result |
|---|---|
| A0 — Self-audit | Pass — this companion exists; 9 registry rows added; dashboard updated; changelog entry added; spec total reconciled to 72 |
| A1 — Coverage | Pass — OQ-079, OQ-081..OQ-088 each added to artifact_registry.md in same session |
| A2 — Logic & Status parity | Pass — all nine `:tested` / Module / example-tested in both spec and registry |
| A3 — Evidence exists | Pass — 8 class-overlay `module.yaml` files + manufacturing `module.yaml` + README + example bundle YAML + baseline matrix all on disk; CI workflow extension references real `openqms validate` invocations |
| A4 — Status honesty | Pass — example-tested supports `:tested`, not `:verified` or `:proved` |
| A5 — Stale counts | Pass — dashboard updated to 72 in same session; CLAUDE.md doesn't cite total counts (only per-tier breakdowns) |
| A6 — Test sync | Pass — CI workflow extended with 15 new validate + 1 new regenerate dry-run on every push touching the relevant paths |
