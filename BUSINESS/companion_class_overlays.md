# Companion — Aerospace + Automotive class overlays (v0.16.0)

**Session date:** 2026-05-23
**Engine version transition:** 0.15.0 → 0.16.0
**Commits:** `ffad042` (6 class overlays + CI extension + engine version bump in one commit)

---

## §1 Computational basis

### What was built

Six class overlay modules deepening the aerospace and automotive verticals. Each overlay encodes the rigor delta between assurance levels — the per-DAL / per-ASIL / per-CAL requirements that scale from "process discipline only" at the lowest tier to "MC/DC + max independence + tightest HW metrics" at the highest.

- **Aerospace** — DAL-A (Catastrophic), DAL-B (Hazardous), DAL-C (Major). DAL-D (Minor) and DAL-E (No Safety Effect) left as forward work — lower-rigor and less common in production.
- **Automotive** — ASIL-D (highest FuSa), ASIL-B (mid-tier; common production), CAL-4 (highest cybersecurity). ASIL-A, ASIL-C, QM, CAL-1, CAL-2, CAL-3 left as forward work — the shipped ASILs bracket the spectrum and CAL-4 is the highest-rigor cyber tier.

This pattern mirrors the medical-devices class overlay batch from v0.11.0+v0.12.0 (samd / implantable / mdr-class-iii / mdr-class-iib / mdr-class-iia / fda-class-iii / fda-class-ii). Aerospace + automotive class overlays bring the same discipline to the two non-medical verticals.

### Files added

| Path | Purpose | Clauses |
|---|---|---|
| `modules/aerospace-dal-a/module.yaml` | DO-178C / DO-254 DAL-A overlay (Catastrophic; MC/DC; 25-of-71 independence; DO-330 TQL-1; DO-254 §6.2 + §6.3) | 7 |
| `modules/aerospace-dal-b/module.yaml` | DAL-B overlay (Hazardous; Decision Coverage; 14-of-69 independence; TQL-1/2; DO-254 §6.2) | 6 |
| `modules/aerospace-dal-c/module.yaml` | DAL-C overlay (Major; Statement Coverage; 2-of-62 independence; TQL-3/4; ARP4754A §3.5 decomposition) | 5 |
| `modules/automotive-asil-d/module.yaml` | ISO 26262 ASIL-D overlay (S3 × E4 × C3; SPFM ≥ 99% / LFM ≥ 90% / PMHF < 10⁻⁸/h; 100% stmt + branch + MC/DC; I3 independence; MISRA C 2012 mandatory; Part 9 §5 decomposition options) | 6 |
| `modules/automotive-asil-b/module.yaml` | ASIL-B overlay (SPFM ≥ 90% / LFM ≥ 60% / PMHF < 10⁻⁷/h; 100% stmt + branch (no MC/DC); I2 independence; MISRA C 2012 recommended) | 5 |
| `modules/automotive-cal-4/module.yaml` | ISO/SAE 21434 CAL-4 overlay (highest; independent cybersecurity assessment per §6.4.7 + Annex C; fuzz/pentest/side-channel V&V per §10+§13; continuous monitoring per §11; safety-security interaction analysis) | 5 |

Total: 6 modules, 34 clauses, ~720 lines of YAML.

### Files modified

| Path | Change |
|---|---|
| `.github/workflows/engine-tests.yml` | Validate step extended with 7 new lines: 6 per-overlay validates (each composed with its vertical) + 1 mega-composite validate (automotive + ASIL-D + CAL-4 + regulated-ai + iso-27001) |
| `engine/openqms/__init__.py` | `__version__ = "0.16.0"` |
| `engine/pyproject.toml` | `version = "0.16.0"` |

### Build / test commands run

```bash
# Per-overlay validates
for overlay in aerospace-dal-a aerospace-dal-b aerospace-dal-c; do
  openqms validate --module aerospace --module $overlay
done

for overlay in automotive-asil-d automotive-asil-b automotive-cal-4; do
  openqms validate --module automotive --module $overlay
done

# Mega-composite — top-rigor safety-critical + cyber-critical + ML-enabled ECU
openqms validate \
  --module automotive \
  --module automotive-asil-d \
  --module automotive-cal-4 \
  --module regulated-ai \
  --module iso-27001
# → invariant_holds: True
```

All 6 per-overlay validates returned `invariant_holds: True`. The 5-module mega-composite returned `invariant_holds: True`.

### Dependencies

No engine code changes; no new dependencies. No new registry standards (overlays cite standards already added by their verticals — DO-178C, DO-254, ARP4754A, ISO 26262, ISO/SAE 21434 are all from v0.14.0/v0.15.0). No new templates (overlays bind to PSAC, Software Test Protocol, Verification Protocol, SSP, Safety Concept, TARA, SOP — all from the verticals).

### Clause breakdown by overlay

**Aerospace DAL-A (7 clauses):** DAL-A-applicability (ARP4754A §5 from FHA), DO178C-MCDC (Table A-7 obj 5), DO178C-independence-25 (Annex A), DO178C-tool-qual-TQL (§12.2 + DO-330), DO254-elemental-analysis (§6.2), DO254-safety-specific-analyses (§6.3 SEU + common-mode), ARP4754A-DAL-allocation (§5 rationale).

**Aerospace DAL-B (6 clauses):** DAL-B-applicability, DO178C-DC (Table A-7 obj 6 — major delta from DAL-A), DO178C-independence-14 (Annex A), DO178C-tool-qual-DAL-B, DO254-elemental-analysis-DAL-B (still required), ARP4754A-DAL-B-allocation.

**Aerospace DAL-C (5 clauses):** DAL-C-applicability, DO178C-SC (Table A-7 obj 7 — major delta from DAL-B), DO178C-independence-2 (only 2-of-62 — cost-of-process reduction is the reason DAL-C is common), DO178C-tool-qual-DAL-C, ARP4754A-DAL-C-allocation (with §3.5 decomposition note).

**Automotive ASIL-D (6 clauses):** ASIL-D-applicability (Part 3 §6 Table 4), ASIL-D-HW-metrics (SPFM/LFM/PMHF per Part 5 §8-9 + Annex F), ASIL-D-SW-coverage (Part 6 Tables 12-15: 100% stmt+branch+MC/DC unit + 100% func+call integration), ASIL-D-confirmation-I3 (Part 2 §6 Table 1), ASIL-D-SW-methods (Part 6 Tables 1-3 — formal notations + MISRA C mandatory + defensive programming + restricted pointers + restricted dynamic memory), ASIL-D-decomposition (Part 9 §5 — D = C(D)+A(D), B(D)+B(D), D+QM(D)).

**Automotive ASIL-B (5 clauses):** ASIL-B-applicability (multiple S×E×C combinations yielding ASIL-B per Table 4), ASIL-B-HW-metrics (SPFM ≥ 90% / LFM ≥ 60% / PMHF < 10⁻⁷/h), ASIL-B-SW-coverage (100% stmt + 100% branch; MC/DC recommended-not-required is the major delta from ASIL-D), ASIL-B-confirmation-I2, ASIL-B-SW-methods (MISRA C recommended-not-required).

**Automotive CAL-4 (5 clauses):** CAL-4-applicability (Annex E informative impact-and-feasibility matrix), CAL-4-independent-assessment (§6.4.7 + Annex C), CAL-4-V-and-V-rigor (§10 + §13 — fuzz, pentest, side-channel), CAL-4-vulnerability-monitoring (§11 — formal monitoring + rehearsed playbooks + end-of-support transition), CAL-4-safety-security-interaction (cross-reference ISO 26262 Part 2 §6).

---

## §2 Results

### All 6 overlays validate standalone

Each overlay validates clean composed with its baseline vertical. The OQ-013 validation harness asserts the OQ-001 invariant (bidirectional clause-to-artifact traceability) holds for the union of (vertical clauses + overlay clauses, vertical template bindings + overlay template bindings). Overlay clauses bind to templates already shipped by the vertical (PSAC, SOP, Software Test Protocol, Verification Protocol, SSP, Safety Concept, TARA) — no new templates needed.

### Mega-composite validates

The 5-module composition `automotive + automotive-asil-d + automotive-cal-4 + regulated-ai + iso-27001` validates clean. This represents a realistic and load-bearing scenario: a top-rigor safety-critical AND cyber-critical AND ML-enabled ECU under enterprise information-security posture. Examples of products that would resolve this bundle: next-generation ADAS / automated-driving controllers; central computing platforms with safety-critical functions integrated with predictive ML; battery management systems for high-voltage EVs with ML-driven SOH estimation + cybersecurity-critical OTA exposure.

The fact that the OQ-011 compose primitive (built in medical-devices context at v0.4.0; unchanged since) handles this 5-module composition without engine code change is a load-bearing structural validation of the platform. The compose primitive is associative (verified at v0.13.0 via hypothesis property tests; OQ-011 status `:verified`) so the order of composition doesn't matter, but in practice adopters compose `vertical + class-overlay + cross-cutting-overlays`.

### Class-overlay pattern now demonstrated across three verticals

| Vertical | Class overlays shipped | Total class overlays | Forward |
|---|---|---|---|
| medical-devices | samd, implantable, mdr-class-iii, mdr-class-iib, mdr-class-iia, fda-class-iii, fda-class-ii | 7 | ivdr-class-c, ivdr-class-d |
| aerospace | dal-a, dal-b, dal-c | 3 | dal-d, dal-e |
| automotive | asil-d, asil-b, cal-4 | 3 | asil-a, asil-c, qm, cal-1, cal-2, cal-3 |
| **Total** | | **13** | |

Each vertical's class overlays follow the same structural pattern: small overlay (5-7 clauses), composes with the vertical via OQ-011, binds to templates already in the vertical (no new templates needed for the rigor-delta clauses since the rigor is encoded in the clause requirements, not in new artifact types).

### Test count unchanged

108 tests pass. Overlays are content, not engine code. The validation surface is exercised through CI (7 new validate steps in `engine-tests.yml`).

### Pattern observation surfaced for future sessions

With 13 class overlays now shipped across three verticals, a future session may want to evaluate a parameterized "rigor-level overlay" generator — a single Python data-class encoding the rigor matrix (DAL × structural-coverage × independence × tool-qualification levels for aerospace; ASIL × HW-metric × SW-coverage × independence × method-recommendations levels for automotive) and emitting all per-class overlays from one definition. This would reduce duplication and make rigor-level deltas auditable in one place. Counter-argument: per-class hand-written overlays let adopters read each one independently, with all the clause text inline, which may be the right granularity for QMS clarity. The decision can wait until DAL-D + DAL-E + the remaining ASILs + CAL-1/2/3 are needed; revisit then.

---

## §3 Verification

### OQ-073 through OQ-078 — class overlays — example-tested → `:tested` (six entries)

**Evidence type:** example-tested (all six).

**Test surface for each overlay:**

1. `openqms validate --module <vertical> --module <overlay>` exercises the OQ-013 validation harness against the composed module; harness asserts the OQ-001 invariant on the union of (vertical clauses + overlay clauses, vertical bindings + overlay bindings). Run locally pre-commit: all `invariant_holds: True`.
2. CI workflow extension at `.github/workflows/engine-tests.yml` runs the per-overlay validate on every push touching `engine/`, `modules/`, `registry/`, `templates/`, or `bundles/`. Drift in either the overlay or its vertical fails CI.

Additional cross-overlay verification:

3. `openqms validate --module automotive --module automotive-asil-d --module automotive-cal-4 --module regulated-ai --module iso-27001` exercises the OQ-011 compose primitive across 5 modules including two class overlays for the same vertical. Returns `invariant_holds: True`. This is the realistic shape for top-rigor automotive products and the most aggressive composition test in the suite to date.

**What's covered:** structural well-formedness of each overlay; composability with its vertical and with other overlays; CI regression-detection if any module/registry/template change breaks the overlay or its composition.

**What's not covered:** semantic correctness of the rigor-delta claims (Open QMS does not adjudicate whether MC/DC has been correctly *implemented* in adopter test cases — that is the adopter's V&V responsibility evidenced by their certification audit). OQ-080 scope-boundary disclaimer covers this.

**Status:** all six at `:tested` per the evidence-type → status table. Upgrade to `:verified` would require property tests holding across a generated population of class overlays — pattern emerging (13 overlays now) so this may be tractable in a future property-test session.

### Existing entries unaffected

No status transitions on existing entries. OQ-073..OQ-078 are strictly additive. Engine code paths (OQ-010, OQ-011, OQ-013) are exercised by the new content; their `:verified` status (from v0.13.0 property tests) is unchanged.

---

## §4 Spec impact

### New entries

| S-ID | Tier | Evidence type | Status | Depends_on | Claim summary |
|---|---|---|---|---|---|
| **OQ-073** | Module | example-tested | `:tested` | OQ-011, OQ-059 | Aerospace DAL-A overlay (MC/DC + 25-of-71 independence + DO-330 TQL-1 + DO-254 §6.2 + §6.3 + ARP4754A §5 allocation; 7 clauses) |
| **OQ-074** | Module | example-tested | `:tested` | OQ-011, OQ-059 | Aerospace DAL-B overlay (Decision Coverage + 14-of-69 independence + TQL-1/2 + DO-254 elemental; 6 clauses) |
| **OQ-075** | Module | example-tested | `:tested` | OQ-011, OQ-059 | Aerospace DAL-C overlay (Statement Coverage + 2-of-62 independence + TQL-3/4 + decomposition note; 5 clauses) |
| **OQ-076** | Module | example-tested | `:tested` | OQ-011, OQ-072 | Automotive ASIL-D overlay (SPFM ≥ 99% / LFM ≥ 90% / PMHF < 10⁻⁸/h + 100% stmt+branch+MC/DC + I3 + MISRA C mandatory + Part 9 §5 decomposition options; 6 clauses) |
| **OQ-077** | Module | example-tested | `:tested` | OQ-011, OQ-072 | Automotive ASIL-B overlay (SPFM ≥ 90% / LFM ≥ 60% / PMHF < 10⁻⁷/h + 100% stmt+branch + I2 + MISRA C recommended; 5 clauses) |
| **OQ-078** | Module | example-tested | `:tested` | OQ-011, OQ-072 | Automotive CAL-4 overlay (independent assessment + fuzz/pentest/side-channel + vulnerability monitoring + safety-security interaction; 5 clauses) |

### Status transitions on existing entries

None.

### Counts

- **Before v0.16.0:** 6 `:verified` / 44 `:tested` / 7 `:argued` / 0 `:open` (total 57).
- **After v0.16.0:** 6 `:verified` / 50 `:tested` / 7 `:argued` / 0 `:open` (total **63**).
- Module-tier entries: 21 → 27 (OQ-040..OQ-059 + OQ-072..OQ-078).

### S-ID numbering note

OQ-073 through OQ-078 are contiguous, sitting immediately after OQ-072 (automotive vertical from v0.15.0). The other contiguous high-id block is OQ-080 (singleton Gap). The next free S-ID for a future Module entry is OQ-079; the next Gap S-ID is OQ-081.

### Forward spec entries (not opened, surfaced for future sessions)

- **Remaining aerospace DAL overlays** — DAL-D (Minor failure-condition; light process), DAL-E (No Safety Effect; no DO-178C objectives at all — process discipline only).
- **Remaining automotive ASIL overlays** — ASIL-A (S × E × C combinations yielding the lowest non-QM ASIL — e.g., S1 × E4 × C3), ASIL-C (S3 × E3 × C3 etc.; common high-rigor production scope), QM (Quality Management baseline only; functions whose failure has no safety impact).
- **Remaining CAL overlays** — CAL-1 (lowest), CAL-2, CAL-3.
- **Rigor-level overlay generator** — meta-pattern question; revisit after the next ~5 class overlays land.

### Engine version

0.15.0 → 0.16.0. No engine code change; version bump tracks the class-overlay batch.

---

## Cross-audit (A0-A6) — clean

| Check | Result |
|---|---|
| A0 — Self-audit | Pass — this companion exists; 6 registry rows added; dashboard updated; changelog entry added; spec total reconciled to 63 |
| A1 — Coverage | Pass — OQ-073..OQ-078 each added to artifact_registry.md in same session |
| A2 — Logic & Status parity | Pass — all six `:tested` / Module / example-tested in both spec and registry |
| A3 — Evidence exists | Pass — all 6 `module.yaml` files exist on disk; CI workflow extension references real `openqms validate` invocations |
| A4 — Status honesty | Pass — example-tested supports `:tested`, not `:verified` or `:proved` |
| A5 — Stale counts | Pass — dashboard updated to 63 in same session; CLAUDE.md doesn't cite total counts (only per-tier breakdowns) |
| A6 — Test sync | Pass — CI workflow extended with 7 new validate steps (6 per-overlay + 1 mega-composite) on every push touching the relevant paths |
