---
document_id: STAB-XXX
title: "[Product / API + Strength + Container] — Stability Protocol"
version: "1.0"
effective_date: YYYY-MM-DD
owner: "[Stability Coordinator / QC Manager]"
status: draft
approved_by: "[QC Manager + QA Director + Regulatory Affairs]"
approval_date: YYYY-MM-DD
---

# STAB-XXX: Stability Protocol

Per ICH Q1A(R2) — Stability Testing of New Drug Substances and Products + ICH Q1B (Photostability) + ICH Q1C (Stability Testing for New Dosage Forms) + ICH Q1D (Bracketing + Matrixing) + ICH Q1E (Evaluation of Stability Data) + 21 CFR 211.166 (Stability testing). For biological/biotechnological products: ICH Q5C (Stability Testing of Biotechnological/Biological Products).

The stability protocol defines the design (storage conditions, time points, tests, container-closure systems, batches) of a stability program intended to support a proposed shelf life + storage conditions for a new product OR to verify continued stability of a commercial product OR to support a manufacturing change.

## 1. Product identification

- **Product name + dosage form + strength:** [details]
- **API + INN:** [name]
- **Container-closure system(s):** [primary pack + secondary pack + closure with material specs]
- **Linked Master Batch Record:** MBR-XXX
- **Proposed / approved shelf life:** [duration]
- **Proposed / approved storage conditions per label:** [e.g., "Store at 20-25°C (68-77°F); excursions permitted to 15-30°C (59-86°F)"]
- **In-use stability (where applicable for reconstituted / opened products):** [duration after first opening / after reconstitution]

## 2. Stability program purpose

- [ ] **Registration / new product** — supporting initial NDA / MAA / BLA submission per ICH Q1A(R2) §2 + §2.1
- [ ] **Annual / ongoing commitment** — per ICH Q1A(R2) §2.2 (at least one batch per year per product per market)
- [ ] **Significant change study** — supporting a manufacturing change per ICH Q1A(R2) §2.3 + ICH Q5E (biologics)
- [ ] **In-use stability** — supporting label claim for use after first opening / reconstitution
- [ ] **Stress / forced-degradation** — characterizing degradation pathways per ICH Q1A(R2) §2.1.2

## 3. Batch + container selection

### 3.1 Batches included

| Batch # | Manufacturing date | Batch size | Manufacturing site | Process scale | Notes (R&D / pilot / commercial; for biologics: same Master Cell Bank?) |
|---|---|---|---|---|---|

Per ICH Q1A(R2) §2.1.3: registration program shall include AT LEAST 3 PRIMARY BATCHES of the drug product manufactured by a process simulating that to be applied to manufacturing batches at commercial scale. Two batches shall be at least pilot scale + third may be smaller.

### 3.2 Container-closure systems

| Container | Closure | Other components | Manufacturing process | Surface area / volume |
|---|---|---|---|---|

### 3.3 Bracketing / matrixing (where applied per ICH Q1D)

- **Bracketing approach:** [extremes-only testing per Q1D §2 + §3]
- **Matrixing approach:** [reduced time-point or attribute testing per Q1D §4]
- **Justification for reduced design vs. full factorial:** [explicit per Q1D Annex 1]

## 4. Storage conditions

### 4.1 General case (per ICH Q1A(R2) §2.1.7)

| Study | Storage condition | Minimum time period at submission | Tested at time points |
|---|---|---|---|
| Long-term | 25°C ± 2°C / 60% RH ± 5% RH OR 30°C ± 2°C / 65% RH ± 5% RH (Zone II baseline) | 12 months | 0, 3, 6, 9, 12, 18, 24, 36, 48, 60 months |
| Intermediate | 30°C ± 2°C / 65% RH ± 5% RH (when long-term is 25°C) | 6 months | 0, 6, 12 months |
| Accelerated | 40°C ± 2°C / 75% RH ± 5% RH | 6 months | 0, 3, 6 months |

### 4.2 Refrigerated drug substances + products (per ICH Q1A(R2) §2.2.7.1)

| Study | Storage condition | Minimum time period | Time points |
|---|---|---|---|
| Long-term | 5°C ± 3°C | 12 months | 0, 3, 6, 9, 12, 18, 24, 36 months |
| Accelerated | 25°C ± 2°C / 60% RH ± 5% RH | 6 months | 0, 3, 6 months |

### 4.3 Frozen drug substances + products (per ICH Q1A(R2) §2.2.7.2)

| Study | Storage condition | Minimum time period | Time points |
|---|---|---|---|
| Long-term | -20°C ± 5°C (or per product label) | 12 months | 0, 3, 6, 9, 12, 18, 24, 36 months |
| Accelerated | 5°C ± 3°C | Per justification | Per justification |

### 4.4 Climate zone considerations

The submission market(s) determine the most-stringent storage condition requirement:

- **Zone I:** Temperate (e.g., UK, Northern Europe, Canada) — 21°C / 45% RH long-term
- **Zone II:** Subtropical, Mediterranean (e.g., US, Japan, Southern Europe) — 25°C / 60% RH long-term
- **Zone III:** Hot dry — 30°C / 35% RH long-term
- **Zone IVA:** Hot humid — 30°C / 65% RH long-term
- **Zone IVB:** Hot very humid (e.g., ASEAN) — 30°C / 75% RH long-term

For global products, the most stringent zone in scope drives the long-term condition selection.

### 4.5 Photostability (per ICH Q1B where photosensitivity established)

| Study | Light source | Exposure | Sample condition (with / without container; with / without secondary pack) | Time points |
|---|---|---|---|---|

## 5. Tests + acceptance criteria per time point

| Time point | Tests performed | Specification | Method | Acceptance |
|---|---|---|---|---|

### Standard stability-indicating attributes

For drug product (chemical) per ICH Q1A(R2) §2.1.5 + Q6A:

| Attribute | Spec | Method | Frequency in study |
|---|---|---|---|
| Appearance + color | [description] | Visual | All time points |
| Assay (active) | NLT X% NMT Y% of label | HPLC stability-indicating | All time points |
| Related substances / degradants | Per ICH Q3B threshold + specified impurities | HPLC stability-indicating | All time points |
| Dissolution / disintegration (oral solid) | Per spec | USP <711> / <701> | All time points |
| Microbial limits / preservative effectiveness (multidose / aqueous) | Per spec | USP <61> + <62> + <51> | Per matrixing |
| Sterility (sterile) | Pass | USP <71> | Per matrixing; end-of-study + key intervals |
| Endotoxin (parenterals) | Per spec | USP <85> | Per matrixing |
| Container/closure integrity (sterile) | Pass | Validated method | Per matrixing |
| Water content (where moisture-sensitive) | Per spec | Karl Fischer | All time points |
| pH | Per spec | USP <791> | All time points (liquids) |

For drug substance (chemical) per ICH Q1A(R2) §2.1.4 + Q6A:

| Attribute | Spec | Method | Frequency |
|---|---|---|---|

For biological products per ICH Q5C: stability-indicating biophysical + biochemical + biological-activity assays; include potency assay at all time points.

## 6. Sample handling + storage

- **Stability chambers used:** [chamber IDs + qualification status]
- **Sample storage orientation:** [upright + inverted for liquids; per ICH where applicable]
- **Sample-retrieval procedure:** [SOP reference]
- **Cumulative excursions tracking:** [chamber excursion log; impact assessment per excursion]

## 7. Acceptance criteria + significant change

Per ICH Q1A(R2) §2.1.6 — "Significant change" for drug product = (a) 5% loss in assay from initial; OR (b) any degradation product exceeding its acceptance criterion; OR (c) failure to meet specs for appearance, physical attributes, functionality (e.g., dissolution); OR (d) failure to meet specs for pH; OR (e) failure to meet specs for dissolution.

A significant change observed during accelerated study triggers additional intermediate-condition testing.

## 8. Statistical evaluation (per ICH Q1E)

- **Approach:** [individual batch evaluation vs. pooled-batch analysis per Q1E §2]
- **Regression analysis applied?** [Yes / No — typically yes for quantitative attributes]
- **Confidence interval for shelf-life determination:** [typically 95% one-sided lower confidence limit]
- **Shelf-life proposed based on stability data:** [duration]
- **Extrapolation beyond observed time points:** [per Q1E §2.4.1 — extrapolation up to 2× observed time, capped at 12 months beyond observed, with justification]

## 9. Reporting

- **Interim stability reports:** at scheduled milestones per regulatory commitment
- **Final stability report:** STAB-XXX-final-report
- **Stability data submitted in regulatory filings:** [reference]
- **Annual stability commitment reporting:** per Annual Product Quality Review (APQR-XXX)

## 10. Out-of-trend / out-of-specification handling

OOS at any stability time point triggers:
- Investigation per OOS-INVESTIGATION SOP
- Batch impact assessment for all batches in distribution from same MBR / process
- Potential field-alert reporting per 21 CFR 314.81(b)(1)(ii)
- Potential shelf-life shortening; potential recall

## 11. Sign-off

| Role | Name | Date | Signature |
|---|---|---|---|
| Stability Coordinator | | | |
| QC Manager | | | |
| QA Director | | | |
| Regulatory Affairs | | | |

## 12. References

- ICH Q1A(R2) — Stability Testing of New Drug Substances and Products.
- ICH Q1B — Photostability Testing of New Drug Substances and Products.
- ICH Q1C — Stability Testing for New Dosage Forms.
- ICH Q1D — Bracketing and Matrixing Designs for Stability Testing.
- ICH Q1E — Evaluation of Stability Data.
- ICH Q5C — Stability Testing of Biotechnological/Biological Products.
- ICH Q6A / Q6B — Specifications (chemical / biological).
- 21 CFR 211.166 — Stability testing.
- EudraLex Vol. 4 Part I Ch. 6 — Quality Control (ongoing stability programme §6.32).
- WHO Technical Report Series 953 — Stability testing of active pharmaceutical ingredients and finished pharmaceutical products.
- Linked: MBR-XXX (product manufacturing reference), MBR registry for batches included; CoA-XXX format (results); APQR-XXX (annual rollup); validated analytical method SOPs; stability-chamber qualification + monitoring records.

## 13. Revision history

| Version | Date | Author | Changes |
|---|---|---|---|
| 1.0 | YYYY-MM-DD | [Name] | Initial release. |
