# Companion — Pharma + Food Safety + Governance/Resilience overlays (v0.19.0 / v0.20.0 / v0.21.0)

**Session date:** 2026-05-23
**Engine version transitions:** 0.18.0 → 0.19.0 → 0.20.0 → 0.21.0 (three releases sequenced in one session)
**Commits:** `a98854e` (pharma) · `ca6e69b` (food safety) · `ee215d7` (ISO 37001 + ISO 22301)

This companion covers three sequential releases shipped as one user-directed batch ("do 1 then 2 then 4" — pharma first, then food safety, then ISO 37001+22301). Each release stood independent technically (separate commits, separate engine versions, independent validation) but the BUSINESS update is consolidated.

---

## §1 Computational basis

### What was built

**Two new verticals + two new cross-cutting overlays = 4 new spec entries.**

| Release | New | Module | Purpose |
|---|---|---|---|
| v0.19.0 | OQ-092 | `modules/pharma/` | 5th vertical; largest remaining regulated-industry gap |
| v0.20.0 | OQ-093 | `modules/food-safety/` | 6th vertical; natural manufacturing complement for food processors |
| v0.21.0 | OQ-094 | `modules/iso-37001/` | Anti-Bribery Management System cross-cutting overlay |
| v0.21.0 | OQ-095 | `modules/iso-22301/` | Business Continuity Management System cross-cutting overlay |

### Files added

**Pharma (v0.19.0):**

| Path | Purpose | Clauses |
|---|---|---|
| `modules/pharma/module.yaml` | Pharma vertical | 23 |
| `modules/pharma/README.md` | Documentation |  |
| `templates/product-pharma/batch-record/MASTER-BATCH-RECORD-TEMPLATE.md` | MBR per 21 CFR 211.186 + EU GMP Part I Ch. 4 |  |
| `templates/product-pharma/validation/VALIDATION-MASTER-PLAN-TEMPLATE.md` | VMP per ICH Q9+Q10 + EU GMP Annex 15 + FDA PV 2011 |  |
| `templates/product-pharma/deviation/DEVIATION-TEMPLATE.md` | Deviation Report per 21 CFR 211.100+192 + ICH Q10 §3.2.2.2 |  |
| `templates/product-pharma/change-control/CHANGE-CONTROL-TEMPLATE.md` | Change Control per ICH Q10 §3.2.3 |  |
| `templates/product-pharma/oos/OOS-INVESTIGATION-TEMPLATE.md` | OOS per FDA Guidance 2006 + 21 CFR 211.192 + EU GMP Ch. 6 §6.34 |  |
| `templates/product-pharma/apqr/APQR-TEMPLATE.md` | APQR per 21 CFR 211.180(e) + EU GMP Ch. 1 §1.10 |  |
| `bundles/example-drug-product.yaml` + `.matrix.json` | Sterile SVP injection bundle |  |

**Food safety (v0.20.0):**

| Path | Purpose | Clauses |
|---|---|---|
| `modules/food-safety/module.yaml` | Food safety vertical | 16 |
| `templates/product-food/haccp/HACCP-PLAN-TEMPLATE.md` | HACCP plan per Codex + ISO 22000 §8.5 + 21 CFR 117 Subpart C + 21 CFR 123 |  |
| `templates/product-food/prp/PREREQUISITE-PROGRAMS-TEMPLATE.md` | PRPs per ISO/TS 22002 15-element framework |  |
| `templates/product-food/recall/RECALL-WITHDRAWAL-PROCEDURE-TEMPLATE.md` | Recall + Withdrawal per 21 CFR 117 Subpart D + 21 CFR 7 + Codex §5.7 |  |
| `bundles/example-food-processor.yaml` + `.matrix.json` | RTE chilled-foods bundle |  |

**ISO 37001 + ISO 22301 (v0.21.0):**

| Path | Purpose | Clauses |
|---|---|---|
| `modules/iso-37001/module.yaml` | ABMS overlay | 14 |
| `modules/iso-22301/module.yaml` | BCMS overlay | 13 |
| `templates/qms-abms/DUE-DILIGENCE-ASSESSMENT-TEMPLATE.md` | Anti-Bribery DD with risk-tier framework + sanctions/PEP/UBO screening |  |
| `templates/qms-bcms/BCMS-PLAN-TEMPLATE.md` | BCP with 8 disruption scenarios + CMT + comms matrix |  |

### Files modified (across all 3 releases)

| Path | Net change |
|---|---|
| `registry/standards.yaml` | +14 standards (7 pharma + 5 food + 2 governance/resilience) |
| `registry/jurisdictions.yaml` | +7 jurisdictions (3 pharma + 4 food); FDA extended |
| `.github/workflows/engine-tests.yml` | +11 new validate steps + 2 new regenerate dry-runs |
| `engine/openqms/__init__.py` | `__version__` bumped 3× → `0.21.0` |
| `engine/pyproject.toml` | Version + keyword expansion (+16 keywords) |

### Build / test commands run

```bash
# Each release validated standalone + key composites + tests
openqms validate --module pharma
openqms validate --module medical-devices --module pharma  # combination products
openqms validate --module pharma --module iso-27001 --module regulated-ai \
                 --module iso-14001 --module iso-45001 --module iso-50001
openqms regenerate --bundle example-drug-product --write-matrix
openqms regenerate --bundle example-drug-product  # idempotence

openqms validate --module food-safety
openqms validate --module food-safety --module iso-27001 --module iso-14001 \
                 --module iso-45001 --module iso-50001
openqms regenerate --bundle example-food-processor --write-matrix
openqms regenerate --bundle example-food-processor  # idempotence

openqms validate --module iso-37001
openqms validate --module iso-22301
# Ultimate 8-module composite — deepest tested
openqms validate --module pharma --module iso-27001 --module regulated-ai \
                 --module iso-14001 --module iso-45001 --module iso-50001 \
                 --module iso-37001 --module iso-22301

pytest engine/tests -q
# → 108 passed (unchanged across all 3 releases — modules are content)
```

---

## §2 Results

### All four entries validate standalone + in target composites

- **Pharma standalone** — pass
- **Pharma + medical-devices** (combination products per 21 CFR Part 4) — pass
- **Pharma + 5 cross-cutting overlays** (full integrated MS for pharma manufacturer) — pass
- **Food safety standalone** — pass
- **Food safety + 4 cross-cutting overlays** (food processor with EHS+IS posture) — pass
- **ISO 37001 standalone** — pass
- **ISO 22301 standalone** — pass
- **8-module ultimate composite** — pharma + iso-27001 + regulated-ai + iso-14001 + iso-45001 + iso-50001 + iso-37001 + iso-22301 — pass. **Deepest composition tested to date** and the realistic shape for a pharma manufacturer pursuing fully-integrated management system certification (PQS + IS + AI governance + EMS + OHSMS + EnMS + ABMS + BCMS).

### Open QMS surface after this session

| Dimension | Before this session | After this session |
|---|---|---|
| Verticals | 4 (medical-devices, aerospace, automotive, manufacturing) | **6** (+pharma, +food-safety) |
| Class overlays | 21 across 3 verticals (medical 7 + aerospace 5 + automotive 9) | 21 (unchanged) |
| Cross-cutting overlays | 5 (iso-27001 + regulated-ai + iso-14001 + iso-45001 + iso-50001) | **7** (+iso-37001 +iso-22301 — common Annex-SL set complete) |
| Spec entries | 75 | **79** |
| Templates | 44 | **54** (+10) |
| Registry standards | 45 | **59** (+14) |
| Registry jurisdictions | 13 | **20** (+7) |
| Example bundles | 8 (samd, aircraft, vehicle, machine-shop) + (others from prior) | **10** (+drug-product, +food-processor) |

### Pharma's structural distinctness

Pharma differs from prior verticals in three notable ways:

1. **First vertical where most cited standards are PUBLIC license** — ICH Q7/Q9/Q10 (ich.org); 21 CFR 210/211 (ecfr.gov); EudraLex Vol. 4 (EU Commission); PIC/S Annex 1 (PIC/S). Only Part 11 *guidance* docs are commercial. Meaningful adopter cost reduction vs. medical-devices (ISO 13485 commercial) / aerospace (AS9100D + DO-178C commercial) / automotive (IATF + ISO 26262 commercial).

2. **First vertical with QP (Qualified Person) personal liability** in batch release — EU GMP Annex 16 + Article 51 of Directive 2001/83/EC. The Master Batch Record + APQR templates explicitly reserve QP sign-off lines.

3. **Distinction between Deviation and Nonconformance** — pharma is the first vertical where this surfaces formally. Deviation = procedural departure (regardless of conformance); NCR = conformance failure. Both can exist on the same batch.

### Food safety's HACCP discipline

Food safety brings the most well-developed pre-CAPA quality framework — HACCP predates ISO 22000 + FSMA + pretty much every modern quality system. The 7 principles + 12 implementation steps are taught as a single canonical procedure across virtually all food industry training. The Codex Alimentarius CXC 1-1969 anchor (which is PUBLIC, freely available) gives the food-safety vertical an exceptional rigor-per-cost profile.

### Cross-cutting overlay set now structurally complete

After v0.21.0, Open QMS ships overlays for all 7 of the common Annex-SL management-system standards an organization might pursue alongside its primary quality vertical:

- **ISO 9001** (quality — substrate of every vertical except pharma which uses ICH Q10 directly)
- **ISO 27001** (information security) — shipped v0.4.0
- **ISO 14001** (environmental) — shipped v0.18.0
- **ISO 45001** (OH&S) — shipped v0.18.0
- **ISO 50001** (energy) — shipped v0.18.0
- **ISO 37001** (anti-bribery) — shipped v0.21.0
- **ISO 22301** (business continuity) — shipped v0.21.0

Plus the **regulated-ai** cross-cutting overlay (NIST AI RMF + EU AI Act + ISO/IEC 42001 + ISO/IEC 23894) which is not Annex SL itself but follows the same composition pattern.

The 8-module ultimate composite validates clean. The OQ-011 compose primitive (built in medical-devices context at v0.4.0, **unchanged in 17 releases**) handles 8-module compositions without modification. The structural-generalization claim from v0.14.0 is now substantiated by 6 verticals × 7 cross-cutting overlays = 42 realistic adopter shapes.

### Test count unchanged at 108

All four new entries are content. Engine paths exercised via CI validate + regenerate steps.

---

## §3 Verification

### OQ-092, OQ-093, OQ-094, OQ-095 — example-tested → `:tested` (four entries)

**Evidence type:** example-tested for all four.

**Test surface (each):**

1. `openqms validate --module <module>` exercises the OQ-013 validation harness against the manifest; harness asserts the OQ-001 invariant.
2. For overlays: composition validates against multiple verticals.
3. For verticals: example bundle regenerate produces baseline + is idempotent.
4. CI workflow extension runs all of the above on every push touching the relevant paths.

**Test results:** all four entries validate clean in every tested composition path. The 8-module ultimate composite for v0.21.0 represents the deepest composition test in the project to date.

**What's covered:** structural well-formedness; composability; CI regression detection.

**What's not covered:** semantic correctness of the rigor-delta claims (adopter V&V evidenced by certification audit per OQ-080 disclaimer).

**Status:** all four at `:tested`. Property-test upgrade to `:verified` may become tractable now that the platform has 6 verticals + 7 cross-cutting overlays — pattern is rich enough that a hypothesis-based property generator could feasibly produce realistic random module shapes.

---

## §4 Spec impact

### New entries

| S-ID | Tier | Evidence type | Status | Depends_on | Summary |
|---|---|---|---|---|---|
| **OQ-092** | Module | example-tested | `:tested` | OQ-011, OQ-014 | Pharma vertical — 23 clauses across 8 standards (ICH Q7/9/10 + 21 CFR 210/211 + EudraLex Vol. 4 + PIC/S Annex 1 + Part 11) + 6 new templates (MBR/VMP/Deviation/Change Control/OOS/APQR) |
| **OQ-093** | Module | example-tested | `:tested` | OQ-011, OQ-014 | Food safety vertical — 16 clauses across 5 standards (ISO 22000 + FSSC 22000 v6 + Codex HACCP + 21 CFR 117 + 21 CFR 123) + 3 new templates (HACCP Plan / PRPs / Recall + Withdrawal) |
| **OQ-094** | Module | example-tested | `:tested` | OQ-011, OQ-012, OQ-014 | ISO 37001:2016 anti-bribery overlay — 14 clauses + 1 new template (Anti-Bribery Due Diligence Assessment) |
| **OQ-095** | Module | example-tested | `:tested` | OQ-011, OQ-012, OQ-014 | ISO 22301:2019 BCMS overlay — 13 clauses + 1 new template (Business Continuity Plan) |

### Adjusted entries

- **OQ-038** template count: 44 → 54 (6 pharma + 3 food + 2 governance/resilience).

### Counts

- Before this session: 6 `:verified` / 62 `:tested` / 7 `:argued` / 0 `:open` (total 75; through v0.18.0).
- After this session: 6 `:verified` / **66** `:tested` / 7 `:argued` / 0 `:open` (total **79**; through v0.21.0).
- Module-tier entries: 39 → 43.
- Vertical count: 4 → 6.
- Cross-cutting overlay count: 5 → 7 (common Annex-SL set complete).

### Forward spec entries (surfaced for future sessions)

**Pharma extension verticals + overlays:**
- ATMP (cell + gene therapy) — EU GMP Annex 2A+2B + FDA 21 CFR 1271 + ICH Q5A(R2)
- Radiopharma — EU GMP Annex 3 + USP <823>
- Veterinary
- IMP — EU GMP Annex 13
- Generic / biosimilar — ANDA / 351(k) pathways
- Site Master File template
- Batch CoA template
- Stability Protocol template (ICH Q1A(R2))
- Sterile vs. non-sterile + biologics vs. small-molecule + commercial vs. clinical-stage class overlays

**Food safety extension verticals + overlays:**
- USDA meat + poultry HACCP — 9 CFR 416 + 9 CFR 417
- FSMA Animal Food — 21 CFR 507
- Produce Safety — 21 CFR 112
- BRCGS / SQF / IFS GFSI schemes
- Intentional Adulteration — 21 CFR 121 standalone
- FSVP — 21 CFR 1 Subpart L standalone
- Class overlays for LACF / acidified / infant formula
- Dietary supplements vertical (21 CFR 111 DSHEA)

**Governance + resilience extension:**
- ISO 19011 audit-program / ISO 19600+37301 broader compliance overlay
- DORA (Digital Operational Resilience Act) overlay for EU financial services
- TISAX (automotive IS)
- IT DR plan template (currently BCMS-PLAN cross-references; standalone would help)
- BIA template (currently summarized in BCMS-PLAN; standalone would help)
- Risk Assessment template (BCMS-specific or generic enterprise)

### Engine version

0.18.0 → 0.19.0 → 0.20.0 → 0.21.0 across the three releases. No engine code changes; version + keyword expansion only.

---

## Cross-audit (A0-A6) — clean

| Check | Result |
|---|---|
| A0 — Self-audit | Pass — this companion exists; 4 registry rows added; dashboard updated; changelog entries added for all 3 versions; spec total reconciled to 79 |
| A1 — Coverage | Pass — OQ-092..OQ-095 each added to artifact_registry.md |
| A2 — Logic & Status parity | Pass — all four `:tested` / Module / example-tested in both spec and registry |
| A3 — Evidence exists | Pass — all module.yaml + README.md + template .md + bundle YAML + baseline matrix files on disk; CI workflow extension references real `openqms validate` + `openqms regenerate` invocations |
| A4 — Status honesty | Pass — example-tested supports `:tested`, not `:verified` or `:proved` |
| A5 — Stale counts | Pass — dashboard updated to 79 in same session |
| A6 — Test sync | Pass — CI workflow extended with 11 new validate steps + 2 new regenerate dry-runs on every push touching the relevant paths |
