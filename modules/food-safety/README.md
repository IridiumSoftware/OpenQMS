# Food safety — Open QMS vertical module

Vertical regulatory module for **food + beverage manufacturing** — human food under ISO 22000 FSMS + Codex HACCP + US FSMA Preventive Controls + FSSC 22000 v6 (a GFSI-benchmarked certification scheme).

The 6th Open QMS vertical (after medical-devices, aerospace, automotive, manufacturing, pharma).

## Scope

This module covers five standards:

- **FSMS substrate** — **ISO 22000:2018** (Food Safety Management Systems; follows Annex SL high-level structure so composes cleanly with ISO 9001 / ISO 27001 / ISO 14001 / ISO 45001 / ISO 50001 / ISO 37001 / ISO 22301).
- **GFSI-recognized certification scheme** — **FSSC 22000 v6** (2023; extends ISO 22000 with ISO/TS 22002 PRPs + scheme-specific additions including food defense + food fraud + allergen + environmental monitoring + product design).
- **HACCP** — **Codex Alimentarius CXC 1-1969** (General Principles of Food Hygiene + HACCP Annex, revised 2020). The globally-harmonized 7-principles + 12-steps HACCP framework.
- **US FSMA** — **21 CFR 117** (Current Good Manufacturing Practice, Hazard Analysis, and Risk-Based Preventive Controls for Human Food — the FSMA Preventive Controls Rule). 21 CFR 117 Subparts B (cGMP) + C (Food Safety Plan) + D (Recall Plan) covered.
- **Seafood HACCP** — **21 CFR 123** for facilities in seafood scope (operates alongside 21 CFR 117).

16 clauses across the five standards.

## Templates introduced by this module

Three new food-safety-specific templates plus reuse of cross-cutting templates:

- **`templates/product-food/haccp/HACCP-PLAN-TEMPLATE.md`** — HACCP Plan per Codex CXC 1-1969 + ISO 22000 §8.5 + 21 CFR 117 Subpart C + 21 CFR 123. Product + process description, HACCP team, flow diagram, hazard analysis covering B/C/P/A (biological + chemical + physical + allergens per FALCPA + FASTER Act + EU FIC Annex II), CCP determination via Codex decision tree → CCP/oPRP/PRP, critical limits + monitoring + pre-defined corrective actions + verification + record-keeping. PCQI designation per FSMA §117.180.

- **`templates/product-food/prp/PREREQUISITE-PROGRAMS-TEMPLATE.md`** — Prerequisite Programs index per ISO/TS 22002 15-element framework. Per-element status + ownership + linked SOP. Detailed §11 cleaning + sanitation per zone 1-4, §12 pest control, §13 personnel hygiene + facilities, §10+§13 allergen management with allergen matrix + changeover validation, §9 supplier program with FSVP cross-reference (21 CFR 1 Subpart L), §6 water + utilities (potability + food-contact suitability for steam/compressed air/ice), §15 recall + traceability program with mock-recall annual cadence, §18 food defense + bioterrorism with FSMA Intentional Adulteration Rule (21 CFR 121) vulnerability assessment.

- **`templates/product-food/recall/RECALL-WITHDRAWAL-PROCEDURE-TEMPLATE.md`** — Recall + Withdrawal Procedure per 21 CFR 117 Subpart D + 21 CFR 7 + Codex §5.7 + ISO 22000 §8.9. FDA Class I/II/III classification with criteria + examples. Recall team with 24/7 contacts + authority + backup. Hour-0 decision flow + hour-1-to-24 actions (<4-hour distribution-list extraction; 24h regulatory notification to FDA District Office + Reportable Food Registry per 21 USC §350f for Class I + USDA-FSIS for meat/poultry + state agencies + importing-country authorities; press release coordination; consumer crisis-line activation). Effectiveness checks per FDA guidance levels A/B/C. Recovery + destruction with witness verification. Mock recall exercise (minimum annual; FDA expects ≤4-hour distribution-list traceability).

Cross-cutting templates already in Open QMS (quality-policy, SOP, AUDIT-PROCEDURE, MANAGEMENT-REVIEW, CAPA) cover the management-system surface naturally — food safety management is structurally similar to other QMS verticals.

## Composition with overlays

- **`iso-27001`** — food companies handle customer + supplier proprietary data + FSMA records; IS posture valuable for organizations also pursuing SOC 2 / ISO 27001 alongside FSMA.
- **`regulated-ai`** — if AI is used in vision-based foreign-object detection, predictive maintenance, ML-driven quality inspection, or demand forecasting affecting food safety.
- **`iso-14001`** — environmental aspects significant: water use, hazardous waste, refrigerants, packaging waste. Composes naturally.
- **`iso-45001`** — chemical sanitizer hazards, cold rooms, machinery, slip/fall, lifting. Worker consultation per §5.4 critical for shift-heavy food production.
- **`iso-50001`** — refrigeration + freezing operations are energy-intensive; ISO 50001 EnPI tracking yields meaningful savings + carbon reduction.

## What is intentionally NOT in scope

- **USDA-regulated meat + poultry** — 9 CFR 416 sanitation + 9 CFR 417 HACCP. Forward overlay (FSIS regulatory framework is distinct from FDA Preventive Controls).
- **Animal food / feed** — 21 CFR 507 (FSMA Preventive Controls for Animal Food). Forward overlay.
- **Produce safety** — 21 CFR 112 (FSMA Produce Safety Rule). Forward overlay (farm-stage scope).
- **Dietary supplements** — 21 CFR 111 (DSHEA cGMP). Separate regulatory regime; forward vertical if needed.
- **BRCGS / SQF / IFS** — other GFSI-benchmarked schemes. Only FSSC 22000 included here to demonstrate one GFSI scheme; others forward.
- **FSMA Intentional Adulteration Rule** — 21 CFR 121. Surfaced in PRP template's §10; standalone module possible if scope significant.
- **Foreign Supplier Verification Programs (FSVP)** — 21 CFR 1 Subpart L. Surfaced in PRP template; standalone overlay possible for importers.
- **Class overlays** — low-acid canned foods (21 CFR 113), acidified foods (21 CFR 114), infant formula (21 CFR 106 + 107). Forward.

## Standards licensing

- **Public license:** Codex Alimentarius CXC 1-1969, 21 CFR 117, 21 CFR 123 (via FAO/WHO + ecfr.gov respectively).
- **Commercial license:** ISO 22000:2018, FSSC 22000 v6, ISO/TS 22002 series (from ISO + national bodies + Foundation FSSC).

See repo-root `README.md` "Standards licensing — important" for the broader licensing posture.

## Adoption guidance

If your organization:

- **Manufactures human food under FSMA scope** → use this module; ensure PCQI designation per §117.180; bind the HACCP Plan + PRPs + Recall + Withdrawal templates; consider iso-14001 + iso-45001 + iso-50001 overlays per scope.
- **Pursues GFSI-benchmarked certification** (FSSC 22000, BRCGS, SQF, IFS) → use this module; the FSSC 22000 v6 scheme is the one explicitly covered, but the foundational ISO 22000 + Codex HACCP clauses are common to all GFSI schemes.
- **Manufactures seafood specifically** → add 21 CFR 123 emphasis (already in scope); the HACCP Plan template covers it alongside FSMA.
- **Operates internationally** → Codex HACCP is the harmonized framework; ISO 22000 is the international FSMS standard. National variations (EU EFSA, UK FSA, Canadian CFIA) build on these baselines.
- **Manufactures meat / poultry / processed eggs under USDA-FSIS scope** → 9 CFR 416 + 9 CFR 417 is forward work; for now this module's framework is broadly applicable but you'll need to supplement with FSIS-specific requirements.

## Forward work

- USDA meat + poultry HACCP overlay (9 CFR 416 + 9 CFR 417)
- FSMA Animal Food cGMP + Preventive Controls overlay (21 CFR 507)
- FSMA Produce Safety Rule overlay (21 CFR 112)
- BRCGS Issue 9 / SQF Edition 9 / IFS Food v8 GFSI-scheme overlays
- FSMA Intentional Adulteration Rule standalone (21 CFR 121)
- FSVP standalone overlay for importers (21 CFR 1 Subpart L)
- Class overlays: low-acid canned (21 CFR 113), acidified (21 CFR 114), infant formula (21 CFR 106 + 107)
- Dietary supplements vertical (21 CFR 111 DSHEA — separate regulatory regime)
- Food allergen labeling standalone for facilities with allergen-mixed product lines
