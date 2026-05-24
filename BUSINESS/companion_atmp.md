# Companion — ATMP class overlay (v0.22.0)

**Session date:** 2026-05-23
**Engine version transition:** 0.21.0 → 0.22.0
**Commit:** `2efc102` (ATMP module + 3 templates + 4 registry standards + example bundle + CI extension + engine version bump in one commit)

---

## §1 Computational basis

### What was built

First pharma class overlay — **ATMP (Advanced Therapy Medicinal Products)** covering cell + gene therapy manufacturing. Composes on top of the pharma vertical (OQ-092 from v0.19.0). Highest-prestige + most-stringent pharma scope; the regulatory frontier of pharmaceutical manufacturing.

Notable that this is a **class overlay** (small overlay encoding the rigor delta over the baseline vertical) rather than a new vertical — same architectural pattern as the medical-devices class overlays (samd, implantable, mdr-class-iii, fda-class-iii, etc.) and the aerospace DAL + automotive ASIL/CAL overlays.

### Files added

| Path | Purpose | Clauses |
|---|---|---|
| `modules/atmp/module.yaml` | ATMP class overlay encoding the substantive ATMP-specific requirements beyond baseline pharma | 10 |
| `templates/product-atmp/donor-eligibility/DONOR-ELIGIBILITY-ASSESSMENT-TEMPLATE.md` | 21 CFR 1271 Subpart C + EU Directive 2004/23/EC — RCDA screening + testing + determination + §1271.65 exception handling with PHI compartmentalization | — |
| `templates/product-atmp/traceability/TISSUE-CELL-TRACEABILITY-RECORD-TEMPLATE.md` | EU GMP Annex 2A §10 + Directive 2004/23/EC Art. 8 + Single European Code per Directive 2015/565 + 21 CFR 1271.290 — bidirectional chain with 30-year EU retention + format-stability planning | — |
| `templates/product-atmp/viral-safety/VIRAL-SAFETY-EVALUATION-REPORT-TEMPLATE.md` | ICH Q5A(R2) 2023 three-pillar framework — cell substrate testing + raw material viral risk + viral clearance studies (non-vector) OR vector-specific RCV testing | — |
| `bundles/example-cart.yaml` + `.matrix.json` | Autologous CD19-targeted CAR-T at US+EU dual-licensed site | — |

### Files modified

| Path | Change |
|---|---|
| `registry/standards.yaml` | +4 standards (all PUBLIC license): EU GMP Annex 2A, EU GMP Annex 2B, 21 CFR 1271, ICH Q5A(R2) |
| `.github/workflows/engine-tests.yml` | Validate step extended with 2 new lines (pharma + atmp standalone; 9-module deepest composite); regenerate step extended with example-cart |
| `engine/openqms/__init__.py` | `__version__ = "0.22.0"` |
| `engine/pyproject.toml` | `version = "0.22.0"`; keywords +6 (atmp, cell-therapy, gene-therapy, car-t, ich-q5a, hct-p) |

### Build / test commands run

```bash
# ATMP composes with pharma
openqms validate --module pharma --module atmp
# → invariant_holds: True

# 9-module deepest composite (pharma + atmp + 7 cross-cutting overlays)
openqms validate \
  --module pharma --module atmp \
  --module iso-27001 --module regulated-ai \
  --module iso-14001 --module iso-45001 --module iso-50001 \
  --module iso-37001 --module iso-22301
# → invariant_holds: True

# CAR-T example bundle baseline + idempotence
openqms regenerate --bundle example-cart --write-matrix
openqms regenerate --bundle example-cart
# → exit 0; (no changes)

# Full test suite
pytest engine/tests -q
# → 108 passed in 10.00s (unchanged — overlay is content)
```

### Clause breakdown (10 total)

- **Annex2A-risk-based** (§2) — risk-based approach scaled to product-specific risks
- **Annex2A-personnel-aseptic** (§4 + §7) — aseptic technique + closed-system processing + isolator/RABS + PIC/S Annex 1 ATMP adaptations
- **Annex2A-donor-starting-material** (§3 + §6) — Directive 2004/23/EC + 21 CFR 1271 donor + starting material requirements
- **Annex2A-traceability** (§10) — bidirectional with Single European Code + 30-year EU retention
- **Annex2A-OOS-autologous** (§8 + §11) — risk-based release strategy for autologous (cannot easily reject)
- **Annex2B-biological-active** — cross-cutting biological-GMP framework
- **CFR1271-Subpart-C-donor-eligibility** — RCDA screening + testing + determination + §1271.65 exceptions
- **CFR1271-Subpart-D-CGTP** — establishment registration + personnel + procedures + facilities + EM through complaint file
- **CFR1271-350-reporting** — HCT/P deviation reporting
- **Q5A-R2-viral-safety** — three-pillar framework with Q5A(R2) 2023 vector-product extension

---

## §2 Results

### Validates standalone + in 9-module deepest composite

- **pharma + atmp** — pass
- **pharma + atmp + iso-27001 + regulated-ai + iso-14001 + iso-45001 + iso-50001 + iso-37001 + iso-22301** — pass (9 modules; deepest composition tested in project history)

The 9-module composite represents the realistic shape for a commercial-stage cell therapy organization pursuing fully-integrated management system certification:

- **PQS** (Pharmaceutical Quality System per ICH Q10)
- **ATMP-specific GMP** (cell + gene therapy specifics per EU GMP Annex 2A + 21 CFR 1271 + Q5A(R2))
- **IS** (Information Security per ISO 27001)
- **AI governance** (per regulated-ai overlay — NIST AI RMF + EU AI Act + ISO 42001 + ISO 23894; cell therapy is increasingly ML-enhanced for vector selection, manufacturing optimization, donor matching)
- **EMS** (Environmental per ISO 14001)
- **OHSMS** (Occupational H&S per ISO 45001 — biological hazards prominent)
- **EnMS** (Energy per ISO 50001 — cryogenic + cleanroom intensive)
- **ABMS** (Anti-bribery per ISO 37001 — cell therapy involves clinician relationships + investigator-initiated studies + public-sector procurement)
- **BCMS** (Business continuity per ISO 22301 — autologous product distribution chain has ultra-low fault tolerance)

### All ATMP standards are PUBLIC license

Same character as the parent pharma vertical (which itself was the first vertical where most cited standards were public). EU GMP Annex 2A + 2B (EU Commission), 21 CFR 1271 (ecfr.gov), ICH Q5A(R2) 2023 (ich.org) — adopters can read every cited requirement for free. Meaningful adopter cost reduction for ATMP organizations specifically (typically venture-backed startups + academic spinouts with limited budget for ISO standards licenses).

### Most distinguishing template characteristics

**Donor Eligibility Assessment** — explicit PHI compartmentalization is the load-bearing design choice. The template captures the eligibility *decision* + the *non-PHI traceability identifiers* (pseudonymized donor UDI); the full identifiable PHI lives in a separate access-restricted record per HIPAA + GDPR Special Category data + 21 CFR 1271.270. This mirrors the OQ-062 PHI compartmentalization architecture from v0.2.1 and is even more critical for HCT/Ps where donor identity links chain back to donation event including potentially sensitive medical + behavioral risk factors.

**Tissue/Cell Traceability Record** — format + media stability planning is novel in Open QMS. 30 years EU retention is longer than most operational systems' typical lifetime, so the template explicitly addresses:
- Electronic-record format obsolescence (PDF/A + CSV + XML; periodic format migration with checksums; vendor independence)
- Physical-media degradation (replicated storage; periodic media refresh)
- Personnel turnover (archival system documented; multi-person knowledge)
- Organizational change (contractual transfer of records-retention obligation)
- Encryption-key custody (long-term key escrow)

**Viral Safety Evaluation Report** — most quantitatively-rigorous template in Open QMS (alongside ISO 50001 Energy Review). Per-step viral clearance reduction factors with confidence intervals + cumulative log reduction calculation + model-virus panel covering diverse classes. Q5A(R2) 2023 explicitly extends to viral vector products, which the template surfaces with separate vector-characterization + RCV-testing sections.

### Open QMS surface after this release

| Dimension | Before v0.22.0 | After v0.22.0 |
|---|---|---|
| Verticals | 6 | 6 (unchanged) |
| Class overlays | 21 across 3 verticals | **22 across 4 verticals** (+atmp on pharma) |
| Cross-cutting overlays | 7 | 7 (unchanged) |
| Spec entries | 79 | **80** |
| Templates | 54 | **57** (+3) |
| Registry standards | 59 | **63** (+4) |
| Registry jurisdictions | 20 | 20 (unchanged) |
| Example bundles | 10 | **11** (+example-cart) |
| Deepest composition tested | 8 modules | **9 modules** |

Class overlay distribution now:

| Vertical | Class overlays | Count |
|---|---|---|
| medical-devices | samd, implantable, mdr-class-iii, mdr-class-iib, mdr-class-iia, fda-class-iii, fda-class-ii | 7 |
| aerospace | DAL-A through DAL-E | 5 |
| automotive | ASIL D/C/B/A/QM + CAL 4/3/2/1 | 9 |
| pharma | **atmp** | **1** |
| **Total class overlays** | | **22** |

### Test count unchanged at 108

ATMP overlay + 3 templates are content; engine paths exercised via CI validate + regenerate steps.

### Pharma's class-overlay roadmap

ATMP is the first pharma class overlay; pharma still has many class-overlay candidates surfaced as forward work in `companion_pharma_food_governance.md`: sterile vs. non-sterile + biologics vs. small-molecule + commercial vs. clinical-stage. Plus the ATMP-specific extensions surfaced in this companion (reproductive tissue / non-ATMP HCT/P / veterinary / in-situ gene editing).

---

## §3 Verification

### OQ-096 — ATMP class overlay — example-tested → `:tested`

**Evidence type:** example-tested.

**Test surface:**

1. `openqms validate --module pharma --module atmp` exercises the OQ-013 validation harness against the composed pharma + ATMP module; harness asserts the OQ-001 invariant.
2. `openqms validate` against the 9-module deepest composite exercises the OQ-011 compose primitive across 9 modules including 2 from the same vertical (pharma + atmp) — confirming that vertical + class-overlay-on-vertical + multiple cross-cutting overlays all coexist cleanly.
3. `openqms regenerate --bundle example-cart` exercises OQ-014 (registry lookup for all 16 cited standards including the 4 new ATMP-specific) + OQ-015 (regenerate); baseline write succeeds; idempotent re-run yields no diff.
4. CI workflow extension runs all of the above on every push touching `engine/`, `modules/`, `registry/`, `templates/`, or `bundles/`.

**What's covered:** structural well-formedness of the ATMP overlay manifest; composability with pharma vertical; composability with 7 cross-cutting overlays simultaneously; CI regression-detection.

**What's not covered:** semantic correctness of the rigor-delta claims (Open QMS does not adjudicate whether Q5A(R2) viral clearance studies have been correctly *designed* for a specific cell-line / process — that is the adopter's V&V responsibility per OQ-080).

**Status:** `:tested`. Property-test upgrade to `:verified` may become tractable now that class overlays exist across 4 verticals (22 total) — the pattern is rich enough for hypothesis-based property generation.

### Existing entries unaffected

No status transitions. OQ-096 is strictly additive. Engine code paths exercised; their `:verified` status unchanged.

---

## §4 Spec impact

### New entries

| S-ID | Tier | Evidence type | Status | Depends_on | Summary |
|---|---|---|---|---|---|
| **OQ-096** | Module | example-tested | `:tested` | OQ-011, OQ-092 | ATMP class overlay (cell + gene therapy) on pharma vertical — 10 clauses across EU GMP Annex 2A + 2B + 21 CFR 1271 + ICH Q5A(R2); 3 new ATMP-specific templates (Donor Eligibility Assessment, Tissue/Cell Traceability Record, Viral Safety Evaluation Report) |

### Adjusted entries

- **OQ-038** template count: 54 → 57 (+3 ATMP-specific templates).

### Counts

- Before this release: 6 `:verified` / 66 `:tested` / 7 `:argued` / 0 `:open` (total 79).
- After this release: 6 `:verified` / **67** `:tested` / 7 `:argued` / 0 `:open` (total **80**).
- Module-tier entries: 43 → 44.
- Class overlay count: 21 (across 3 verticals) → 22 (across 4 verticals — adds atmp on pharma).
- Cross-vertical class overlays: 7 (medical) + 5 (aerospace) + 9 (automotive) + 1 (pharma).

### Forward spec entries (surfaced for future sessions)

- **Reproductive tissue / gametes overlay** — 21 CFR 1271 reproductive-tissue-specific subprovisions; different regulatory + ethical framework.
- **HCT/P-only overlay (non-ATMP)** — products regulated only under 21 CFR 1270 + 1271 without IND/BLA pathway; minimum-manipulation + homologous-use criteria per §1271.10 + §1271.15.
- **Veterinary ATMP overlay** — emerging space; EMA + FDA-CVM regulatory frameworks.
- **In situ gene editing overlay** — CRISPR direct administration without ex vivo cell processing (e.g., CASGEVY base-editing in situ administration); fundamentally different manufacturing model.
- **Site Master File template for ATMPs** — PIC/S Explanatory Notes equivalent + ATMP-specific facility descriptions.
- **Comparability protocol template (ICH Q5E)** — particularly critical for autologous ATMPs without reference standard.
- **CAR-T-specific release-testing template** — flow cytometry + cytotoxicity assay + vector copy number + integration site analysis + sterility.
- **AAV-specific release-testing template** — empty/full capsid ratio + vector genome copy number + dose-determination math.
- **Pharma additional class overlays** — sterile vs. non-sterile; biologics vs. small-molecule; commercial vs. clinical-stage.

### Engine version

0.21.0 → 0.22.0. No engine code change; version + keyword expansion.

---

## Cross-audit (A0-A6) — clean

| Check | Result |
|---|---|
| A0 — Self-audit | Pass — this companion exists; OQ-096 registry row added; dashboard updated; changelog v0.22.0 entry added; spec total reconciled to 80 |
| A1 — Coverage | Pass — OQ-096 added to artifact_registry.md |
| A2 — Logic & Status parity | Pass — `:tested` / Module / example-tested in both spec and registry |
| A3 — Evidence exists | Pass — module.yaml + 3 template .md + example-cart bundle + baseline matrix all on disk; CI workflow extension references real `openqms` invocations |
| A4 — Status honesty | Pass — example-tested supports `:tested`, not `:verified` or `:proved` |
| A5 — Stale counts | Pass — dashboard updated to 80 in same session |
| A6 — Test sync | Pass — CI workflow extended with 2 new validate steps + 1 new regenerate dry-run on every push touching the relevant paths |
