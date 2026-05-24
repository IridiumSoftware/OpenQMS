# Companion — HSE + energy cross-cutting overlays (v0.18.0)

**Session date:** 2026-05-23
**Engine version transition:** 0.17.0 → 0.18.0
**Commit:** `ef13f46` (3 overlay modules + 3 new templates + 3 new registry standards + CI extension + engine version bump in one commit)

---

## §1 Computational basis

### What was built

Three cross-cutting management-system overlays — ISO 14001:2015 (environmental), ISO 45001:2018 (OH&S), ISO 50001:2018 (energy). Each composes with any vertical (medical-devices / aerospace / automotive / manufacturing). All three follow the Annex SL high-level structure that ISO 9001 / ISO 27001 / ISO 42001 already use, so composition is structurally clean even when adopters layer all five management systems.

The EHS-and-energy block (14001 + 45001 + 50001) is the natural pairing — mid-size manufacturers integrating sustainability + safety want all three together. Shipping them in one release maximizes the compose-surface expansion: 3 new overlays × 4 verticals = 12 new validated composites.

### Files added

| Path | Purpose | Clauses |
|---|---|---|
| `modules/iso-14001/module.yaml` | EMS overlay covering ISO 14001:2015 substantive additions over Annex SL baseline | 11 |
| `modules/iso-45001/module.yaml` | OHSMS overlay; worker consultation per §5.4 + hierarchy of controls per §8.1.2 are the unique-to-OH&S elements | 11 |
| `modules/iso-50001/module.yaml` | EnMS overlay; the only management-system standard mandating a calculated, periodically-recalibrated quantitative baseline | 10 |
| `templates/qms-environmental/ENVIRONMENTAL-ASPECTS-REGISTER-TEMPLATE.md` | ISO 14001 §6.1.2 + §6.1.3 + §8.1 + §8.2 register: significance scoring → SEA → operational controls → emergency procedures → compliance-obligations cross-reference, lifecycle perspective explicit | — |
| `templates/qms-ohs/HAZARD-IDENTIFICATION-RISK-ASSESSMENT-TEMPLATE.md` | ISO 45001 §6.1.2 HIRA with worker consultation evidence per §5.4 as precondition, hierarchy-of-controls action per §8.1.2, cross-references to §6.1.3 legal + §8.1.3 MoC + §8.1.4 procurement + §8.2 emergency. Includes psychosocial hazards explicitly per the standard | — |
| `templates/qms-energy/ENERGY-REVIEW-AND-ENPI-BASELINE-TEMPLATE.md` | ISO 50001 §6.3 + §6.4 + §6.5 + §6.6 combined: energy review → SEU identification → improvement opportunities → EnPI definitions with formula + normalization → EnB calculation with recalibration triggers → data collection plan → operational + procurement implications | — |

### Files modified

| Path | Change |
|---|---|
| `registry/standards.yaml` | +3 standards: ISO 14001:2015, ISO 45001:2018, ISO 50001:2018 (all commercial license) |
| `.github/workflows/engine-tests.yml` | Validate step extended with 8 new lines: 3 standalone + 4 cross-vertical composites + 1 full-stack mega-composite |
| `engine/openqms/__init__.py` | `__version__ = "0.18.0"` |
| `engine/pyproject.toml` | `version = "0.18.0"`; keywords gained 6 (iso-14001, iso-45001, iso-50001, environmental-management, occupational-health-safety, energy-management) |

### Build / test commands run

```bash
# Standalone validates
for ov in iso-14001 iso-45001 iso-50001; do
  openqms validate --module $ov
done
# all three → invariant_holds: True

# Each overlay × each vertical
for v in medical-devices aerospace automotive manufacturing; do
  for ov in iso-14001 iso-45001 iso-50001; do
    openqms validate --module $v --module $ov
  done
done
# 12/12 composites → invariant_holds: True

# 6-module everything-shop mega-composite
openqms validate \
  --module manufacturing \
  --module iso-14001 \
  --module iso-45001 \
  --module iso-50001 \
  --module iso-27001 \
  --module regulated-ai
# → invariant_holds: True

# Full test suite
pytest engine/tests -q
# → 108 passed in 9.88s
```

### Dependencies

No engine code changes; no new dependencies. 3 new registry standards. 3 new templates in 3 new template subdirectories (`templates/qms-environmental/`, `templates/qms-ohs/`, `templates/qms-energy/`).

### Clause breakdown (32 total)

**ISO 14001 (11):** ISO14001-4.2 (interested parties); ISO14001-5.2 (env policy); ISO14001-6.1.2 (aspects — the defining EMS artifact); ISO14001-6.1.3 (compliance obligations); ISO14001-6.1.4 (planning action); ISO14001-6.2 (objectives); ISO14001-7.4 (communication); ISO14001-8.1 (operational control of SEAs); ISO14001-8.2 (emergency preparedness); ISO14001-9.1.2 (evaluation of compliance); ISO14001-10.2 (NC + CA).

**ISO 45001 (11):** ISO45001-4.2 (interested parties incl. workers + their reps); ISO45001-5.2 (OH&S policy); **ISO45001-5.4 (consultation + participation of workers — THE foundational OHSMS requirement)**; ISO45001-6.1.2 (hazard ID + risk assessment + opportunities — psychosocial factors explicit); ISO45001-6.1.3 (legal + other requirements); ISO45001-6.1.4 (planning action); ISO45001-7.3 (awareness — incl. right to remove self from imminent danger); **ISO45001-8.1.2 (hierarchy of controls — elimination > substitution > engineering > administrative > PPE)**; ISO45001-8.1.3 (management of change); ISO45001-8.1.4 (procurement incl. contractor coordination); ISO45001-8.2 (emergency); ISO45001-10.2 (incident + NC + CA with worker participation).

**ISO 50001 (10):** ISO50001-5.2 (energy policy); **ISO50001-6.3 (energy review — analytical foundation of EnMS)**; ISO50001-6.4 (EnPIs); **ISO50001-6.5 (EnB — calculated baseline, the unique mandate)**; ISO50001-6.6 (planning for collection of energy data); ISO50001-8.1 (operational control of SEUs); ISO50001-8.2 (design); ISO50001-8.3 (procurement of energy services + products + energy); ISO50001-9.1.1 (monitoring + measurement + analysis with deviation investigation); ISO50001-10.2 (NC + CA).

---

## §2 Results

### All 3 overlays validate standalone + with all 4 verticals

12 composites validated (3 overlays × 4 verticals). The OQ-013 validation harness asserts the OQ-001 invariant (bidirectional clause-to-artifact traceability) holds for each composed module. The Annex SL structural compatibility means the overlay clauses interleave cleanly with vertical clauses without naming collisions or template conflicts.

### 6-module everything-shop composite validates

The realistic shape of a small-to-mid manufacturer pursuing full management-system integration: `manufacturing + iso-14001 + iso-45001 + iso-50001 + iso-27001 + regulated-ai`. This composes 6 modules — the deepest composition tested in the project to date. The OQ-011 compose primitive (built in medical-devices context at v0.4.0, unchanged since) handles this without engine code change.

The 6-module composition is structurally meaningful because it represents the QMS surface for an organization that wants ISO 9001 (quality) + ISO 14001 (environmental) + ISO 45001 (occupational H&S) + ISO 50001 (energy) + ISO 27001 (information security) + AI governance (NIST AI RMF + EU AI Act + ISO 42001) — the full Annex-SL management-system stack. Adopters seeking integrated-management-system certification (IMS — common pursuit in mid-size manufacturers) would compose exactly this shape.

### Cross-cutting overlay set now substantial

Before v0.18.0: 2 cross-cutting overlays (iso-27001, regulated-ai). After v0.18.0: 5 cross-cutting overlays. The compose-surface expansion is multiplicative — each new overlay × 4 verticals = 4 new realistic adopter shapes. v0.18.0 added 3 overlays = 12 new realistic adopter shapes immediately.

### Annex SL structural compatibility validated

ISO 9001 (which underlies all 4 verticals), ISO 27001, ISO 42001 (in regulated-ai), and now ISO 14001 + ISO 45001 + ISO 50001 all follow the Annex SL high-level structure. The fact that the 6-module composite validates clean is concrete evidence that the platform's composition model respects this structural compatibility — clauses from different management-system standards that target the same Annex-SL section (e.g., §5.2 policy) coexist in the composed module without conflict because each is scoped by its standard id.

### Test suite unchanged

108 tests pass. Overlays + templates are content.

### ISO 50001's quantitative character surfaced in the template

The Energy Review + EnPIs + EnB Baseline template is the most quantitative artifact in Open QMS — it includes per-EnPI normalization formulas (regression vs. engineering), per-EnB calculation methods, recalibration triggers, capability-style targets (Cpk-analogous: "EnPI-organization ≤ EnB × 0.97 = 3% YoY improvement target"). This reflects ISO 50001's unique mandate among the management-system standards: adopters must produce real numbers, not just process discipline. The template surfaces this character at the document boundary so adopters can't accidentally treat it as a checklist standard.

---

## §3 Verification

### OQ-089, OQ-090, OQ-091 — example-tested → `:tested` (three entries)

**Evidence type:** example-tested (all three).

**Test surface for each overlay:**

1. `openqms validate --module <overlay>` exercises the OQ-013 validation harness against the overlay manifest; harness asserts the OQ-001 invariant.
2. `openqms validate --module <vertical> --module <overlay>` exercises the OQ-011 + OQ-012 + OQ-013 composition path; composed module validates clean across all 4 verticals.
3. CI workflow extension at `.github/workflows/engine-tests.yml` runs the standalone + per-vertical-composite validates on every push touching `engine/`, `modules/`, `registry/`, `templates/`, or `bundles/`. Plus the full-stack mega-composite validate exercises the OQ-011 compose primitive at depth 6.

**What's covered:** structural well-formedness; composability with each vertical; multi-overlay composability (6-module mega-composite); CI regression-detection.

**What's not covered:** semantic correctness of the rigor-delta claims (Open QMS does not adjudicate whether the Energy Review template's normalization-model construction is methodologically sound for any specific facility — that's the adopter's responsibility, evidenced by certification audit). OQ-080 disclaimer covers this.

**Status:** all three at `:tested`. Property-test upgrade to `:verified` may become tractable for the cross-cutting overlay class once enough overlays exist to share invariants — currently 5 cross-cutting overlays (iso-27001 + regulated-ai + iso-14001 + iso-45001 + iso-50001); pattern emerging.

### Existing entries unaffected

No status transitions. OQ-089..OQ-091 are strictly additive. Engine code paths exercised by the new content; their `:verified` status unchanged.

---

## §4 Spec impact

### New entries

| S-ID | Tier | Evidence type | Status | Depends_on | Claim summary |
|---|---|---|---|---|---|
| **OQ-089** | Module | example-tested | `:tested` | OQ-011, OQ-012, OQ-014 | ISO 14001:2015 environmental management cross-cutting overlay; 11 clauses + 1 new template (Environmental Aspects Register) |
| **OQ-090** | Module | example-tested | `:tested` | OQ-011, OQ-012, OQ-014 | ISO 45001:2018 OH&S cross-cutting overlay; 11 clauses (worker consultation §5.4 + hierarchy of controls §8.1.2 are unique-to-OH&S) + 1 new template (HIRA) |
| **OQ-091** | Module | example-tested | `:tested` | OQ-011, OQ-012, OQ-014 | ISO 50001:2018 energy cross-cutting overlay; 10 clauses (only management-system standard mandating calculated EnB baseline) + 1 new template (Energy Review + EnPIs + EnB) |

### Status transitions on existing entries

None.

### Adjusted entries

- **OQ-038** template count: 41 → 44 (Environmental Aspects Register + HIRA + Energy Review).

### Counts

- **Before v0.18.0:** 6 `:verified` / 59 `:tested` / 7 `:argued` / 0 `:open` (total 72).
- **After v0.18.0:** 6 `:verified` / 62 `:tested` / 7 `:argued` / 0 `:open` (total **75**).
- Module-tier entries: 36 → 39.
- Cross-cutting overlay set: 2 → 5.

### Forward spec entries (not opened, surfaced for future sessions)

- **Compliance Obligations Register template** (dedicated; for ISO 14001 §6.1.3 — currently the register concept lives only inside Environmental Aspects Register cross-reference).
- **OH&S legal + other requirements register** (ISO 45001 §6.1.3).
- **Energy Objectives + Targets register** (ISO 50001 §6.6).
- **ISO 37001 anti-bribery overlay** — 4th common compliance-management-system standard alongside 14001/45001/50001.
- **ISO 22301 business continuity management overlay** — operational resilience.
- Forward verticals from prior companion: food safety (ISO 22000 + FSSC 22000 + HACCP), pharma GMP, industrial machinery functional safety.
- **Rigor-level overlay generator** — with 5 cross-cutting overlays now, plus 21 class overlays, the parameterized-overlay-generator question becomes more tractable; revisit when ~10 cross-cutting or ~30 class overlays exist.

### Engine version

0.17.0 → 0.18.0. No engine code change; version + keyword expansion.

---

## Cross-audit (A0-A6) — clean

| Check | Result |
|---|---|
| A0 — Self-audit | Pass — this companion exists; 3 registry rows added; dashboard updated; changelog entry added; spec total reconciled to 75 |
| A1 — Coverage | Pass — OQ-089..OQ-091 each added to artifact_registry.md in same session |
| A2 — Logic & Status parity | Pass — all three `:tested` / Module / example-tested in both spec and registry |
| A3 — Evidence exists | Pass — 3 module.yaml + 3 template .md files on disk; registry/standards.yaml updated; CI workflow extension references real `openqms validate` invocations |
| A4 — Status honesty | Pass — example-tested supports `:tested`, not `:verified` or `:proved` |
| A5 — Stale counts | Pass — dashboard updated to 75 in same session |
| A6 — Test sync | Pass — CI workflow extended with 8 new validate steps on every push touching the relevant paths |
