# Modules catalog

Comprehensive inventory of every regulatory module shipped with Open QMS as of v0.22.0. Use this page to choose the modules for your scope.

**Three module types:**

1. **Verticals** — primary regulatory modules per industry (e.g., medical-devices, pharma). One vertical per primary product type.
2. **Class overlays** — encode rigor delta or product-class delta on top of a vertical (e.g., DAL-A on aerospace; ASIL-D on automotive; ATMP on pharma; mdr-class-iii on medical-devices).
3. **Cross-cutting overlays** — apply across any vertical (e.g., iso-27001 information security; iso-14001 environmental). All follow Annex SL so they compose with each other and with every vertical without naming collisions.

**Composition is via `--module` repeatable on `openqms validate` and `openqms resolve`:**

```bash
openqms validate --module <vertical> [--module <class-overlay>] [--module <cross-cutting>] [...]
```

The OQ-011 compose primitive (built v0.4.0, unchanged since) handles compositions of arbitrary depth. 9-module compositions are tested in CI.

---

## Verticals (6)

### medical-devices

- **Module ID:** `medical-devices`
- **Standards:** ISO 13485:2016, 21 CFR 820, 21 CFR Part 11, EU MDR 2017/745, ISO 14971:2019, IEC 62304, IEC 62366-1, IEC 60601-1, ISTA 2A/3A, MDSAP
- **License mix:** majority commercial (ISO + IEC); 21 CFR + EU MDR + IMDRF public
- **Compatible class overlays:** samd, implantable, ivd, mdr-class-iii, mdr-class-iib, mdr-class-iia, fda-class-iii, fda-class-ii
- **Typical composites:** medical-devices + iso-27001; medical-devices + regulated-ai (for AI/ML SaMD); medical-devices + pharma (combination products per 21 CFR Part 4)
- **Example bundle:** [`bundles/example-samd.yaml`](../bundles/example-samd.yaml)
- **Module README:** [`modules/medical-devices/README.md`](../modules/medical-devices/README.md) (if present)

### aerospace

- **Module ID:** `aerospace`
- **Standards:** ISO 9001:2015, AS9100D, 14 CFR Part 21, EASA Part 21, DO-178C, DO-254, ARP4754A, ARP4761, AS9102 Rev C
- **License mix:** AS9100D + DO/ARP commercial (SAE/RTCA); 14 CFR + EASA Part 21 public
- **Compatible class overlays:** aerospace-dal-a through aerospace-dal-e
- **Scope:** civil aviation (commercial aerospace). Defense scope deferred.
- **Example bundle:** [`bundles/example-aircraft.yaml`](../bundles/example-aircraft.yaml)
- **Module README:** [`modules/aerospace/README.md`](../modules/aerospace/README.md)

### automotive

- **Module ID:** `automotive`
- **Standards:** ISO 9001:2015, IATF 16949:2016, ISO 26262:2018, ISO/SAE 21434:2021, UN R155, UN R156, Automotive SPICE 4.0, AIAG PPAP 4th Ed.
- **License mix:** ISO/IATF/ISO-SAE/VDA/AIAG commercial; UN R155/R156 public
- **Compatible class overlays:** automotive-asil-d, -asil-c, -asil-b, -asil-a, -qm (ISO 26262 FuSa tiers) + automotive-cal-4, -cal-3, -cal-2, -cal-1 (ISO/SAE 21434 cyber tiers)
- **Scope:** road vehicles (passenger + light commercial + heavy duty trucks). Motorcycle/off-highway/rail/defense deferred.
- **Example bundle:** [`bundles/example-vehicle.yaml`](../bundles/example-vehicle.yaml)
- **Module README:** [`modules/automotive/README.md`](../modules/automotive/README.md)

### manufacturing

- **Module ID:** `manufacturing`
- **Standards:** ISO 9001:2015 only
- **License mix:** commercial (ISO 9001 from ISO/national bodies)
- **Compatible class overlays:** none (ISO 9001 has no rigor tiers — adopters needing higher rigor migrate to a regulated vertical)
- **Scope:** general non-regulated manufacturing — machine shops, tooling, contract manufacturing, custom fab, job shops, fabrication houses, prototyping shops, light industrial. The smallest vertical.
- **Example bundle:** [`bundles/example-machine-shop.yaml`](../bundles/example-machine-shop.yaml)
- **Module README:** [`modules/manufacturing/README.md`](../modules/manufacturing/README.md)

### pharma

- **Module ID:** `pharma`
- **Standards:** ICH Q7, ICH Q9(R1), ICH Q10, 21 CFR 210, 21 CFR 211, EudraLex Vol. 4, PIC/S Annex 1 (2022), 21 CFR Part 11
- **License mix:** **all PUBLIC** (first Open QMS vertical where most cited standards are public-license — ICH from ich.org, CFR from ecfr.gov, EudraLex from EU Commission, PIC/S from PIC/S)
- **Compatible class overlays:** atmp (cell + gene therapy)
- **Scope:** API + DP; small-molecule + large-molecule (biologics); sterile + non-sterile. Out-of-scope (forward overlays): pharmacy compounding, dietary supplements, veterinary feed, IMP, generic/biosimilar specifics.
- **Example bundle:** [`bundles/example-drug-product.yaml`](../bundles/example-drug-product.yaml)
- **Module README:** [`modules/pharma/README.md`](../modules/pharma/README.md)

### food-safety

- **Module ID:** `food-safety`
- **Standards:** ISO 22000:2018, FSSC 22000 v6 (2023), Codex Alimentarius CXC 1-1969 (HACCP), 21 CFR 117 (FSMA PCHF), 21 CFR 123 (Seafood HACCP)
- **License mix:** Codex + CFR public; ISO 22000 + FSSC commercial
- **Compatible class overlays:** none yet (forward: low-acid canned, acidified, infant formula, GFSI-other-schemes)
- **Scope:** human food manufacturing under ISO 22000 + Codex HACCP + US FSMA. Out-of-scope: USDA meat+poultry (forward), animal food (forward), produce safety (forward), dietary supplements (separate vertical forward).
- **Example bundle:** [`bundles/example-food-processor.yaml`](../bundles/example-food-processor.yaml)
- **Module README:** [`modules/food-safety/README.md`](../modules/food-safety/README.md)

---

## Class overlays (22 across 4 verticals)

Class overlays are small (5-10 clauses) and compose with their parent vertical via `--module <vertical> --module <class-overlay>`.

### Medical-devices class overlays (7)

| Overlay | Purpose | Standards added |
|---|---|---|
| `samd` | Software as a Medical Device | IEC 82304-1, IMDRF SaMD N12 |
| `implantable` | Implantable devices | ISO 14708-1 |
| `ivd` | In Vitro Diagnostics (cross-cutting within medical-devices) | EU IVDR 2017/746, 21 CFR 809, ISO 15189:2022 |
| `mdr-class-iii` | EU MDR Class III (highest risk; Notified Body involvement; SSCP; expert panel for high-risk-AI) | (already in vertical) |
| `mdr-class-iib` | EU MDR Class IIb | (already in vertical) |
| `mdr-class-iia` | EU MDR Class IIa | (already in vertical) |
| `fda-class-iii` | FDA Class III (PMA pathway, 21 CFR 814; MDR adverse-event reporting per 21 CFR 803) | 21 CFR 814, 21 CFR 803 |
| `fda-class-ii` | FDA Class II (510(k) pathway, 21 CFR 807) | 21 CFR 807, 21 CFR 860 (De Novo) |

### Aerospace DAL class overlays (5 — complete set)

| Overlay | DAL | FHA classification | Structural coverage | Independence | DO-330 TQL |
|---|---|---|---|---|---|
| `aerospace-dal-a` | A | Catastrophic | MC/DC | 25-of-71 objectives | TQL-1 typical |
| `aerospace-dal-b` | B | Hazardous | Decision Coverage | 14-of-69 objectives | TQL-1/2 |
| `aerospace-dal-c` | C | Major | Statement Coverage | 2-of-62 objectives | TQL-3/4 (most common production DAL) |
| `aerospace-dal-d` | D | Minor | None required | 2-of-26 objectives (typically QA + SCM) | TQL-4/5 |
| `aerospace-dal-e` | E | No Safety Effect | N/A | NO DO-178C objectives | configuration mgmt only |

### Automotive ASIL class overlays (5 — complete set)

| Overlay | ASIL | HARA trigger | HW metrics (SPFM / LFM / PMHF) | SW coverage | Independence |
|---|---|---|---|---|---|
| `automotive-asil-d` | D | S3 × E4 × C3 | ≥99% / ≥90% / <10⁻⁸/h | 100% stmt + branch + MC/DC | I3 |
| `automotive-asil-c` | C | S3 × E4 × C2 etc. | ≥97% / ≥80% / <10⁻⁷/h | 100% stmt + branch | I3 |
| `automotive-asil-b` | B | S2 × E4 × C2 etc. | ≥90% / ≥60% / <10⁻⁷/h | 100% stmt + branch | I2 |
| `automotive-asil-a` | A | S1 × E4 × C3 etc. | no quant SPFM/LFM; <10⁻⁶/h | 100% statement | I1 |
| `automotive-qm` | QM | low (S, E, C) | none ISO 26262 specific | none ISO 26262 specific | none ISO 26262 specific |

### Automotive CAL class overlays (4 — complete set)

| Overlay | CAL | TARA trigger | Independent assessment | V&V depth | Vulnerability monitoring |
|---|---|---|---|---|---|
| `automotive-cal-4` | 4 | high-impact high-feasibility (safety-affecting) | REQUIRED | + fuzz + pentest + side-channel where applicable | formal w/ response-time + rehearsed playbooks |
| `automotive-cal-3` | 3 | moderate-to-high | RECOMMENDED | + fuzz REQUIRED; pentest recommended | formal w/ response-time commitments |
| `automotive-cal-2` | 2 | moderate | OPTIONAL | baseline + vulnerability scanning | documented triage cadence |
| `automotive-cal-1` | 1 | low (low impact AND low feasibility) | NOT required | security functional testing only | CSMS-baseline cadence |

### Pharma class overlays (1)

| Overlay | Purpose | Standards added |
|---|---|---|
| `atmp` | Advanced Therapy Medicinal Products (cell + gene therapy — CAR-T, AAV, iPSC-derived, ex vivo gene-modified HSCT, oncolytic viruses) | EU GMP Annex 2A, EU GMP Annex 2B, 21 CFR 1271, ICH Q5A(R2) — all PUBLIC license |

---

## Cross-cutting overlays (7 — common Annex-SL set complete)

Each composes with ANY vertical. All 7 follow Annex SL high-level structure → coexist cleanly even when all are composed simultaneously (verified by 9-module composite in CI).

### iso-27001 (Information Security)

- **Standard:** ISO/IEC 27001:2022
- **When to use:** any organization handling customer/proprietary data; SOC 2 + ISO 27001 are the common IS certifications.
- **Composes with:** every vertical.

### regulated-ai

- **Standards:** NIST AI RMF 1.0, EU AI Act 2024/1689, ISO/IEC 42001:2023, ISO/IEC 23894:2023
- **When to use:** products that use ML in safety/risk/decision contexts. Particularly relevant for AI/ML SaMD, ADAS/AD, predictive maintenance, vision-based quality inspection, ML-driven manufacturing optimization.
- **Composes with:** every vertical.

### iso-14001 (Environmental)

- **Standard:** ISO 14001:2015
- **When to use:** organizations pursuing environmental management certification; required for many regulated supply chains.
- **Includes:** Environmental Aspects + Impacts Register template with significance scoring → SEA determination → operational controls + emergency procedures + compliance-obligations cross-reference. Lifecycle perspective explicit.

### iso-45001 (Occupational Health + Safety)

- **Standard:** ISO 45001:2018
- **When to use:** any organization with workforce safety obligations (essentially all manufacturers).
- **Includes:** HIRA (Hazard Identification + Risk Assessment) template with **worker consultation per §5.4 as precondition** + hierarchy of controls per §8.1.2 (elimination > substitution > engineering > administrative > PPE — PPE is last resort).
- **Notable:** §5.4 worker consultation is unique to OHSMS among the Annex SL standards.

### iso-50001 (Energy)

- **Standard:** ISO 50001:2018
- **When to use:** energy-intensive operations (sterile pharma, cold-chain food, large-scale manufacturing).
- **Includes:** Energy Review + EnPIs + EnB Baseline template — **most quantitative template in Open QMS**. ISO 50001 is unique among the management-system standards in mandating a calculated, periodically-recalibrated quantitative baseline.

### iso-37001 (Anti-Bribery)

- **Standard:** ISO 37001:2016
- **When to use:** public-sector vendors, extractives, defense contractors, healthcare suppliers, infrastructure contractors, intermediary-heavy sales channels, high-CPI jurisdictions.
- **Includes:** Anti-Bribery Due Diligence Assessment template with risk-tier framework (Low/Medium/High/Prohibited) + sanctions/PEP/adverse-media/UBO screening + contractual-safeguards checklist (FCPA + UK Bribery Act + OECD Convention references).

### iso-22301 (Business Continuity)

- **Standard:** ISO 22301:2019
- **When to use:** organizations with significant disruption exposure (single-site dependencies, complex supply chains, regulated services with continuity obligations under DORA / healthcare / critical infrastructure / utilities / telecoms).
- **Includes:** Business Continuity Plan template with BIA-derived RTO/MAO/MBCO/RPO + 8 disruption scenarios + crisis management team with 24/7 contacts + communications matrix with regulatory reporting windows + exercise programme cadence (tabletop annual + comms cascade annual + IT DR annual + live activation biennial).

---

## Example bundles (11)

Validated end-to-end with committed baseline matrices that act as regression-detection in CI.

| Bundle | Vertical(s) | Cross-cutting overlays | Jurisdictions | Standards |
|---|---|---|---|---|
| `example-samd` | medical-devices | iso-27001 + regulated-ai | FDA, EU MDR | ISO 13485 + 21 CFR 820 + ISO 14971 + IEC 62304 + IMDRF SaMD N12 + ISO 27001 + NIST AI RMF + ISO 42001 |
| `example-aircraft` | aerospace | regulated-ai + iso-27001 | FAA | ISO 9001 + AS9100D + 14 CFR Part 21 + EASA Part 21 + DO-178C + DO-254 + ARP4754A + ARP4761 + AS9102 + NIST AI RMF + EU AI Act + ISO 42001 + ISO 27001 |
| `example-vehicle` | automotive | regulated-ai + iso-27001 | NHTSA, UNECE, KBA | + UN R155 + UN R156 |
| `example-machine-shop` | manufacturing | iso-27001 | (empty — general mfg) | ISO 9001 + ISO 27001 |
| `example-drug-product` | pharma | iso-27001 + regulated-ai + iso-14001 + iso-45001 + iso-50001 | FDA, EMA, MHRA | + ICH Q7/9/10 + 21 CFR 210/211 + EudraLex + PIC/S Annex 1 |
| `example-cart` | pharma + atmp | iso-27001 + iso-14001 + iso-45001 + iso-50001 | FDA, EMA, MHRA | + EU GMP Annex 2A/2B + 21 CFR 1271 + ICH Q5A(R2) |
| `example-food-processor` | food-safety | iso-14001 + iso-45001 + iso-50001 | FDA-Food, EFSA, CFIA | ISO 22000 + FSSC 22000 + Codex HACCP + 21 CFR 117 |

(Plus older example bundles from earlier releases retained for backward-compatibility regression testing.)

---

## Composition examples

### Smallest viable scaffold

```bash
# General manufacturing — single ISO 9001 module + IS
openqms validate --module manufacturing --module iso-27001
```

### Typical medical-device manufacturer

```bash
# Class II AI/ML-enabled SaMD
openqms validate \
  --module medical-devices --module samd --module fda-class-ii \
  --module regulated-ai --module iso-27001
```

### Top-rigor automotive ECU

```bash
# Brake-by-wire ECU: ASIL-D + CAL-4 + ML for predictive battery state
openqms validate \
  --module automotive \
  --module automotive-asil-d --module automotive-cal-4 \
  --module regulated-ai --module iso-27001
```

### Highest rigor scope tested

```bash
# Commercial-stage cell-therapy organization with fully-integrated MS
openqms validate \
  --module pharma --module atmp \
  --module iso-27001 --module regulated-ai \
  --module iso-14001 --module iso-45001 --module iso-50001 \
  --module iso-37001 --module iso-22301
```

This 9-module composite is the deepest tested in CI.

---

## Choosing your modules — decision flow

1. **Pick your vertical** based on product type:
   - Medical device → `medical-devices`
   - Aircraft / avionics / aerospace component → `aerospace`
   - Road vehicle / automotive component → `automotive`
   - General manufactured product (no specific regulator) → `manufacturing`
   - Drug substance or drug product → `pharma`
   - Food or beverage → `food-safety`
   - Combination product → compose multiple verticals

2. **Add the appropriate class overlay** based on risk/criticality classification:
   - Medical devices → mdr-class-iii/iib/iia (EU) and/or fda-class-iii/ii (US); plus samd/implantable/ivd for category
   - Aerospace → DAL per FHA classification (A → E)
   - Automotive → ASIL per HARA + CAL per TARA
   - Pharma → atmp if cell/gene therapy
   - Food / manufacturing → none currently

3. **Compose cross-cutting overlays** based on organizational scope:
   - Always: consider iso-27001 (IS) — universally relevant
   - If ML/AI in product: regulated-ai
   - If environmental compliance scope: iso-14001
   - Always for organizations with workers: iso-45001
   - If energy-intensive: iso-50001
   - If anti-bribery scope relevant (public-sector vendor / extractive / defense / healthcare / intermediary-heavy / high-CPI jurisdiction): iso-37001
   - If continuity-critical service or regulated continuity obligation: iso-22301

4. **Define a stored bundle** at `bundles/<your-product>.yaml` with your final composition + run `openqms regenerate --bundle <your-product> --write-matrix` to commit the baseline. CI thereafter regenerates on every push to detect drift.

5. **Validate** with `openqms validate --module <each>` to confirm the OQ-001 bidirectional clause-to-artifact traceability invariant holds.

6. **Adopt the templates** in your repository for the artifacts your bundle's matrix references. Open QMS does NOT enforce semantic correctness — that's your V&V responsibility evidenced by your certification audit (per OQ-080 disclaimer).
