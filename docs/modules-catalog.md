# Modules catalog

Comprehensive inventory of every regulatory module shipped with Open QMS as of v0.41.0. Use this page to choose the modules for your scope.

**Current scope:**

| Dimension | Count |
|---|---|
| Verticals | **7** (medical-devices, aerospace, automotive, manufacturing, pharma, food-safety, chemicals) |
| Class overlays | **44** across 6 verticals (medical 9 / aerospace 7 / automotive 11 / pharma 6 / food-safety 5 / chemicals 6) |
| Cross-cutting overlays | **24** (iso-27001, regulated-ai, iso-14001, iso-45001, iso-50001, iso-37001, iso-22301, recall-workflow, iso-31000, iso-37301, soc-2, pci-dss, hitrust-csf, nist-csf, dora, eu-gpsr, tisax, defense-cui, cmmc, osha-hcs, transport-hazmat, eu-biocides, tsca-pfas, **privacy**) |
| **Total modules** | **76** + general |
| Registry standards | **~117** (v0.41.0 +2 PUBLIC: GDPR + CCPA) |
| Registry jurisdictions | **20** |
| Document templates | **92** (v0.41.0 +5 privacy: PRIVACY-POLICY / DPA / DPIA / ROPA / PERSONAL-DATA-BREACH-NOTIFICATION) |
| Example bundles | **8** (validated end-to-end with committed baseline matrices) |
| Spec entries | **92** (0 `:open`) |
| Deepest composition tested in CI | **17-module ultimate composite** (chemicals top-rigor + adjacent + IMS + privacy) |

**Three module types:**

1. **Verticals** — primary regulatory modules per industry. One per primary product type.
2. **Class overlays** — encode rigor delta or product-class delta on top of a vertical (e.g., DAL-A on aerospace; ASIL-D on automotive; ATMP on pharma; mdr-class-iii on medical-devices).
3. **Cross-cutting overlays** — apply across any vertical. Annex-SL-aligned overlays compose cleanly with each other.

**Composition is via `--module` repeatable:**

```bash
openqms validate --module <vertical> [--module <class-overlay>] [--module <cross-cutting>] [...]
```

The OQ-011 compose primitive (built v0.4.0, unchanged since) handles compositions of arbitrary depth. 11-module compositions are tested in CI.

---

## Verticals (7)

| Module ID | Standards | Compatible class overlays | Example bundle | License mix |
|---|---|---|---|---|
| `medical-devices` | ISO 13485 / 21 CFR 820 / 21 CFR Part 11 / EU MDR / ISO 14971 / IEC 62304 / IEC 62366-1 / IEC 60601-1 / ISTA / MDSAP | samd, implantable, ivd, ivdr-class-c, ivdr-class-d, mdr-class-iii/iib/iia, fda-class-iii/ii | `example-samd` | Mostly commercial |
| `aerospace` | ISO 9001 / AS9100D / 14 CFR Part 21 / EASA Part 21 / DO-178C / DO-254 / ARP4754A / ARP4761 / AS9102 | DAL-A through DAL-E, defense, commercial-space | `example-aircraft` | Mostly commercial |
| `automotive` | ISO 9001 / IATF 16949 / ISO 26262 / ISO/SAE 21434 / UN R155 / UN R156 / Automotive SPICE 4.0 / AIAG PPAP | ASIL-D/C/B/A/QM, CAL-4/3/2/1, defense, motorcycle | `example-vehicle` | Mostly commercial; UN R155/R156 public |
| `manufacturing` | ISO 9001:2015 only | (none — ISO 9001 has no rigor tiers) | `example-machine-shop` | Commercial |
| `pharma` | ICH Q7/Q9/Q10 / 21 CFR 210/211 / EudraLex Vol. 4 / PIC/S Annex 1 / 21 CFR Part 11 | atmp, pharma-sterile, pharma-biologics, pharma-imp, pharma-generic-biosimilar, pharma-clinical-stage | `example-drug-product` | **All PUBLIC** |
| `food-safety` | ISO 22000 / FSSC 22000 v6 / Codex HACCP / 21 CFR 117 / 21 CFR 123 | food-usda-fsis, food-animal, food-produce-safety, food-intentional-adulteration, food-fsvp | `example-food-processor` | Mixed (Codex + CFR public; ISO + FSSC commercial) |
| `chemicals` | EU REACH / EU CLP / UN GHS Rev. 10 / OECD GLP / TSCA | (none yet — OSHA HCS + DOT HazMat + biocides + cosmetics + pesticides forward) | `example-specialty-chemical` | **All PUBLIC** |

---

## Class overlays (44 across 6 verticals)

### Medical-devices (9 class overlays + 1 sub-vertical)

`ivd` is a **sub-vertical cross-cutting** within medical-devices (not a class-rigor delta — it adds an entire In Vitro Diagnostics regulatory scope including EU IVDR + 21 CFR 809 + ISO 15189). It in turn takes its own class overlays `ivdr-class-c` + `ivdr-class-d`. Listed here for discoverability but NOT counted in the 9 class overlays (which are all rigor / risk-class deltas).

| Overlay | Purpose | Counted in 9? |
|---|---|---|
| `samd` | Software as a Medical Device (IEC 82304-1 + IMDRF SaMD N12) | ✓ |
| `implantable` | Implantable devices (ISO 14708-1) | ✓ |
| `ivd` | In Vitro Diagnostics SUB-VERTICAL (EU IVDR + 21 CFR 809 + ISO 15189) | — (sub-vertical) |
| `ivdr-class-c` | EU IVDR Class C (Annex VIII Rule 3 — companion diagnostics + genetic + cancer); NB conformity + biennial PSUR | ✓ |
| `ivdr-class-d` | EU IVDR Class D (Annex VIII Rule 1 — highest risk: blood/tissue donor screening); EURL + annual PSUR + batch verification | ✓ |
| `mdr-class-iii` | EU MDR Class III (highest risk; Notified Body + SSCP + expert panel for high-risk-AI) | ✓ |
| `mdr-class-iib` | EU MDR Class IIb | ✓ |
| `mdr-class-iia` | EU MDR Class IIa | ✓ |
| `fda-class-iii` | FDA Class III (PMA pathway; MDR adverse-event reporting) | ✓ |
| `fda-class-ii` | FDA Class II (510(k) pathway; De Novo) | ✓ |

### Aerospace (7)

| Overlay | DAL/Type | FHA classification | Distinguishing |
|---|---|---|---|
| `aerospace-dal-a` | A | Catastrophic | MC/DC + 25-of-71 independence + TQL-1 + DO-254 §6.2 + §6.3 |
| `aerospace-dal-b` | B | Hazardous | Decision Coverage + 14-of-69 independence + TQL-1/2 |
| `aerospace-dal-c` | C | Major | Statement Coverage + 2-of-62 independence; most common production DAL |
| `aerospace-dal-d` | D | Minor | No structural coverage; 2-of-26 independence |
| `aerospace-dal-e` | E | No Safety Effect | NO DO-178C objectives apply |
| `aerospace-defense` | (overlay) | n/a | MIL-STD-882E SSPP + ITAR + EAR; deemed-export controls |
| `aerospace-commercial-space` | (overlay) | n/a | 14 CFR Part 450 FAA-AST; EC ≤ 1×10⁻⁴; FTS; financial responsibility |

### Automotive (11)

| Overlay | ASIL/CAL | HARA/TARA trigger | Distinguishing |
|---|---|---|---|
| `automotive-asil-d` | ASIL-D | S3×E4×C3 | SPFM≥99% / LFM≥90% / PMHF<10⁻⁸/h; MC/DC; I3; MISRA C mandatory |
| `automotive-asil-c` | ASIL-C | (mid-high) | SPFM≥97% / LFM≥80% / PMHF<10⁻⁷/h; I3 same as D; language subset required |
| `automotive-asil-b` | ASIL-B | (mid) | SPFM≥90% / LFM≥60% / PMHF<10⁻⁷/h; I2 |
| `automotive-asil-a` | ASIL-A | (lowest non-QM) | PMHF<10⁻⁶/h; 100% statement only; I1 |
| `automotive-qm` | QM | (positive QM claim) | Out-of-FuSa-scope; HARA rationale as load-bearing |
| `automotive-cal-4` | CAL-4 | Highest cyber | Independent assessment + fuzz/pentest/side-channel + safety-security interaction |
| `automotive-cal-3` | CAL-3 | (mid-high) | Independent recommended + fuzz required |
| `automotive-cal-2` | CAL-2 | (mid-low) | Optional assessment + vulnerability scanning |
| `automotive-cal-1` | CAL-1 | Low impact AND low feasibility | No independent + baseline V&V |
| `automotive-defense` | (overlay) | n/a | MIL-STD-882E + USML Cat VII + EAR Cat 9/0 + CMMC readiness |
| `automotive-motorcycle` | (overlay) | n/a | ISO 26262 Part 12; MSIL instead of ASIL |

### Pharma (6)

| Overlay | Scope |
|---|---|
| `atmp` | Advanced Therapy Medicinal Products (CAR-T + gene therapy + iPSC-derived + ex vivo gene-modified + oncolytic viruses); EU GMP Annex 2A + 2B + 21 CFR 1271 + ICH Q5A(R2) |
| `pharma-sterile` | PIC/S Annex 1 (2022) enforced rigor — CCS + isolator/RABS + APS + EM Grade A + line clearance |
| `pharma-biologics` | ICH Q5A/B/D/E + Q6B + Q11 + Annex 2B — cell-bank discipline + viral safety + comparability + biotech specs |
| `pharma-imp` | EU GMP Annex 13 + 21 CFR 312 — sponsor model + blinding + IMP QP + Phase 1 enforcement discretion |
| `pharma-generic-biosimilar` | ANDA + 351(k) — bioequivalence + Paragraph IV + interchangeability |
| `pharma-clinical-stage` | Phase 1-3 staged-expectations + evolving specs + supply forecasting + pre-commercial readiness |

### Food-safety (5)

| Overlay | Scope |
|---|---|
| `food-usda-fsis` | 9 CFR 416 + 417 — meat + poultry + processed-egg under FSIS jurisdiction; continuous-inspector model |
| `food-animal` | 21 CFR 507 — FSMA Preventive Controls for Animal Food |
| `food-produce-safety` | 21 CFR 112 — FSMA Produce Safety Rule (farm-stage) |
| `food-intentional-adulteration` | 21 CFR 121 — FSMA IA Rule (Food Defense Plan + FDQI) |
| `food-fsvp` | 21 CFR 1 Subpart L — Foreign Supplier Verification (US importers) |

---

## Cross-cutting overlays (24)

Each composes with ANY vertical. Annex-SL-aligned overlays compose cleanly with each other (verified by 11-module mega-composite in CI).

| Overlay | Standards | When to use |
|---|---|---|
| `iso-27001` | ISO/IEC 27001:2022 | Information security; SOC 2 + ISO 27001 common IS certifications |
| `regulated-ai` | NIST AI RMF + EU AI Act + ISO/IEC 42001 + ISO/IEC 23894 | Products using ML in safety/risk/decision contexts |
| `iso-14001` | ISO 14001:2015 | Environmental management |
| `iso-45001` | ISO 45001:2018 | Occupational H&S; **worker consultation §5.4** unique requirement |
| `iso-50001` | ISO 50001:2018 | Energy management; **only MS standard mandating calculated EnB baseline** |
| `iso-37001` | ISO 37001:2016 | Anti-bribery; independent compliance function + due diligence |
| `iso-22301` | ISO 22301:2019 | Business continuity; BIA with RTO/RPO + exercise programme |
| `recall-workflow` | NHTSA Part 573/577/579 + FDA 21 CFR 7/806 + CPSIA §15 | Cross-vertical recall discipline parametrized by framework |
| `iso-31000` | ISO 31000:2018 | **META-framework** unifying domain-specific risk standards |
| `iso-37301` | ISO 37301:2021 | Compliance Management (replaces ISO 19600; broader than 37001) |
| `soc-2` | AICPA TSC 2017 | US service-organization examination (alternative or parallel to ISO 27001) |
| `pci-dss` | PCI DSS v4.0 | Payment card industry data security; scope-driven by cardholder data flow |
| `hitrust-csf` | HITRUST CSF v11.x | Multi-framework mapping (HIPAA + HITECH + ISO 27001 + NIST SP 800-53 + PCI DSS + GDPR) |
| `nist-csf` | NIST CSF v2.0 | General-purpose cybersecurity framework; 6 functions incl. new Govern |
| `dora` | EU Regulation 2022/2554 | EU financial entities + ICT third-party providers; effective Jan 17 2025 |
| `eu-gpsr` | EU Regulation 2023/988 | EU consumer products (replaces GPSD); Safety Gate notification |
| `tisax` | VDA-ISA v6.0 | Automotive supply-chain IS (German + European OEM requirement) |
| `defense-cui` | DFARS 252.204-7012 + NIST SP 800-171 Rev 3 | US DoD contractors handling CDI; 14 control families + SPRS scoring |
| `cmmc` | CMMC 2.0 (32 CFR Part 170) | DoD CUI certification; Levels 1/2/3 with C3PAO; phased rollout 2025-2028 |
| `privacy` | EU GDPR + US CCPA/CPRA | Personal data protection; universally applicable; closes last major management-system gap |

---

## Example bundles (8)

Each ships with a committed baseline matrix that acts as regression detection in CI.

| Bundle | Vertical(s) | Cross-cutting | Jurisdictions |
|---|---|---|---|
| `example-samd` | medical-devices + samd | iso-27001 + regulated-ai | FDA, EU MDR |
| `example-aircraft` | aerospace | regulated-ai + iso-27001 | FAA |
| `example-vehicle` | automotive | regulated-ai + iso-27001 | NHTSA, UNECE, KBA |
| `example-machine-shop` | manufacturing | iso-27001 | (empty — general mfg) |
| `example-drug-product` | pharma | iso-27001 + regulated-ai + iso-14001 + iso-45001 + iso-50001 | FDA, EMA, MHRA |
| `example-cart` | pharma + atmp | iso-27001 + iso-14001 + iso-45001 + iso-50001 | FDA, EMA, MHRA |
| `example-food-processor` | food-safety | iso-14001 + iso-45001 + iso-50001 | FDA-Food, EFSA, CFIA |
| `example-specialty-chemical` | chemicals | iso-27001 + iso-14001 + iso-45001 + iso-31000 | (empty — multi-region by composition) |

---

## Composition examples — from smallest to deepest

```bash
# Smallest viable scaffold — general manufacturer with IS
openqms validate --module manufacturing --module iso-27001

# Typical medical-device manufacturer — Class II AI/ML-enabled SaMD
openqms validate \
  --module medical-devices --module samd --module fda-class-ii \
  --module regulated-ai --module iso-27001

# Top-rigor automotive ECU with recall discipline
openqms validate \
  --module automotive \
  --module automotive-asil-d --module automotive-cal-4 \
  --module recall-workflow --module regulated-ai --module iso-27001

# DoD aerospace contractor stack
openqms validate \
  --module aerospace --module aerospace-defense \
  --module defense-cui --module cmmc --module iso-27001

# Clinical-stage cell-therapy organization (commercial-ATMP shape)
openqms validate \
  --module pharma --module atmp \
  --module iso-27001 --module regulated-ai \
  --module iso-14001 --module iso-45001 --module iso-50001 \
  --module iso-37001 --module iso-22301

# Deepest tested composition (11-module mega-composite — CI-validated)
openqms validate \
  --module pharma --module pharma-sterile --module pharma-biologics --module atmp \
  --module iso-27001 --module soc-2 --module iso-31000 \
  --module iso-22301 --module iso-14001 --module iso-45001 --module iso-50001
# → invariant_holds: True
```

---

## Decision flow

1. **Pick your vertical** based on product type:
   - Medical device → `medical-devices`
   - Aircraft / avionics / aerospace component → `aerospace`
   - Road vehicle / automotive component → `automotive`
   - General manufactured product (no specific regulator) → `manufacturing`
   - Drug substance or drug product → `pharma`
   - Food or beverage → `food-safety`
   - Combination product → compose multiple verticals (e.g., `medical-devices + pharma`)

2. **Add the appropriate class overlay** based on risk/criticality:
   - Medical devices → mdr-class-iii/iib/iia + fda-class-iii/ii (regulatory) + samd/implantable/ivd (category) + ivdr-class-c/d (IVDs)
   - Aerospace → DAL per FHA + defense + commercial-space if applicable
   - Automotive → ASIL per HARA + CAL per TARA + defense + motorcycle if applicable
   - Pharma → atmp + sterile + biologics + imp + generic-biosimilar + clinical-stage as applicable
   - Food → usda-fsis + animal + produce + intentional-adulteration + fsvp as applicable

3. **Compose cross-cutting overlays** based on organizational scope:
   - **Universally relevant**: iso-27001 (IS) + iso-31000 (risk framework)
   - **If ML/AI in product**: regulated-ai
   - **EHS scope**: iso-14001 + iso-45001 + iso-50001
   - **Compliance scope**: iso-37001 (anti-bribery) + iso-37301 (broader compliance)
   - **Continuity-critical**: iso-22301
   - **Recall obligations**: recall-workflow
   - **Service organization**: soc-2
   - **Payment data**: pci-dss
   - **Healthcare**: hitrust-csf
   - **US federal contractor**: nist-csf
   - **EU financial**: dora
   - **EU consumer products**: eu-gpsr
   - **Automotive Tier-1+**: tisax
   - **DoD contractor**: defense-cui + cmmc

4. **Define a stored bundle** at `bundles/<your-product>.yaml` + run `openqms regenerate --bundle <your-product> --write-matrix` to commit baseline.

5. **Validate** with `openqms validate --module <each>` to confirm OQ-001 invariant.

6. **Adopt the templates** in your repository for the artifacts your bundle's matrix references.
