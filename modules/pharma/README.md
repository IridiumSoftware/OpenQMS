# Pharma — Open QMS vertical module

Vertical regulatory module for **pharmaceutical manufacturing** — both Active Pharmaceutical Ingredient (API; drug substance) and Drug Product (DP; finished pharmaceutical form). Covers small-molecule + large-molecule (biologics) + sterile + non-sterile manufacturing scope under FDA + EMA + MHRA + WHO Prequalification regulatory frameworks.

The fifth Open QMS vertical (after medical-devices, aerospace, automotive, manufacturing). Naturally complements the medical-devices vertical for combination-product organizations.

## Scope

This module covers eight standards across four discipline tracks:

- **Harmonized Pharmaceutical Quality System (PQS)** — **ICH Q10** (PQS framework) + **ICH Q9(R1)** (Quality Risk Management). Adopted by FDA / EMA / MHRA / PMDA / Health Canada as the unified PQS architecture.
- **Active Pharmaceutical Ingredient (API) GMP** — **ICH Q7**. The harmonized API GMP guide; adopted globally.
- **US cGMP** — **21 CFR 210** (general cGMP for drugs) + **21 CFR 211** (cGMP for finished pharmaceuticals — Subparts B + D + E + F + G + I + J covered).
- **EU GMP** — **EudraLex Vol. 4** Parts I + II + III + Annexes. Chapter 1 (PQS), Chapter 2 (Personnel including the QUALIFIED PERSON), Chapter 6 (QC including OOS), Annex 15 (Qualification + Validation), Annex 16 (QP certification + batch release).
- **Sterile manufacturing** — **PIC/S Annex 1** (August 2022; effective August 2023) — Contamination Control Strategy, Aseptic Process Simulation, environmental monitoring + cleanroom classification (Grade A through D). Globally the most stringent sterile-manufacturing standard.
- **Electronic records + signatures** — **21 CFR Part 11** (covered via the existing medical-devices module reference but reused here for pharma computerized systems — LIMS, MES, electronic batch records, electronic logbooks, analytical instruments).

23 clauses total across the eight standards.

## Templates introduced by this module

Six new pharma-specific templates plus reuse of cross-cutting templates:

- **`templates/product-pharma/batch-record/MASTER-BATCH-RECORD-TEMPLATE.md`** — Master Batch Record (MBR / BMR) per 21 CFR 211.186 + EU GMP Part I Chapter 4. Defines how each batch is manufactured — composition, equipment, process flow with CPPs, IPCs, yield calculation, packaging, deviations log, QA release sign-off. The MBR is the spec; the executed Batch Record is the evidence. Per 21 CFR 211.188.

- **`templates/product-pharma/validation/VALIDATION-MASTER-PLAN-TEMPLATE.md`** — Validation Master Plan per ICH Q9 + Q10 + EU GMP Annex 15 + FDA Process Validation 2011. Site-level navigation map across IQ / OQ / PQ for equipment + cleaning validation + process validation (Stage 1 design + Stage 2 PQ + Stage 3 continued process verification) + analytical-method validation per ICH Q2(R1) + computer-system validation per GAMP 5.

- **`templates/product-pharma/deviation/DEVIATION-TEMPLATE.md`** — Deviation Report per 21 CFR 211.100 + 211.192 + EU GMP Ch. 1 §1.4(xiv) + ICH Q10 §3.2.2.2. Categorization (Critical / Major / Minor) with QA-assignment criteria + investigation depth + timeline. Root-cause investigation, batch-impact assessment, disposition decision, CAPA linkage, regulatory-reporting triggers (FDA Field Alert per 21 CFR 314.81), effectiveness check. Distinct from nonconformance — covers procedural departures regardless of product-conformance outcome.

- **`templates/product-pharma/change-control/CHANGE-CONTROL-TEMPLATE.md`** — pharma Change Control per ICH Q10 §3.2.3 + EU GMP Ch. 1 §1.4(xiv) + 21 CFR 211.100. QA-gated planned-change management for facility / equipment / utility / material / supplier / specification / formulation / process / packaging / labeling / analytical method / computerized system / documentation / organization / contractor. Classification (Critical / Major / Minor), risk assessment per ICH Q9, regulatory-impact assessment (FDA + EMA + MHRA + Health Canada + PMDA submissions), pre-implementation actions, effectiveness check.

- **`templates/product-pharma/oos/OOS-INVESTIGATION-TEMPLATE.md`** — Out-of-Specification Investigation per FDA Guidance for Industry "Investigating OOS Test Results for Pharmaceutical Production" (October 2006) + 21 CFR 211.192 + EU GMP Ch. 6 §6.34 + USP <1010>. Two-phase structure: Phase 1 (Laboratory Investigation — 24-48 hours, identifying assignable lab cause without retesting) and Phase 2 (Full-Scale Investigation — 30 days, multi-functional, retesting only with documented protocol). Batch disposition decision, impact on other batches, regulatory reporting (FDA Field Alert 21 CFR 314.81), CAPA linkage.

- **`templates/product-pharma/apqr/APQR-TEMPLATE.md`** — Annual Product Quality Review per 21 CFR 211.180(e) (US) + EU GMP Ch. 1 §1.10 (PQR — EU). Annual per-product review aggregating manufacturing + quality data: critical IPC + CQA trends (with Cpk/Ppk), starting materials review + supplier performance, finished-product CoA results, deviations summary, change controls summary, OOS summary, complaints, recalls + Field Alerts, stability data review, validation status, conclusions + recommendations. EU PQR mandatory annually with QP review.

## Composition with overlays

- **`iso-27001`** — GxP-relevant IT systems (LIMS, MES, electronic batch records) require elevated information-security posture; many pharma organizations pursue ISO 27001 alongside cGMP.
- **`regulated-ai`** — when AI is used in manufacturing control or decision support (continuous-process verification ML, predictive maintenance, advanced process control); cross-references ICH Q9 risk-management framework.
- **`iso-14001`** — pharma manufacturing has significant environmental aspects (solvent handling, hazardous waste, process water use, energy).
- **`iso-45001`** — chemical + biological + ergonomic + radiation hazards prominent in pharma operations; HIRA template's psychosocial category important for shift-work-heavy 24/7 sterile production.
- **`iso-50001`** — sterile manufacturing is especially energy-intensive due to HVAC + cleanroom requirements; ISO 50001 EnPI tracking can produce meaningful savings.

## Forward work (overlays + class overlays not yet shipped)

- **Cell + gene therapy (ATMP) overlay** — EU GMP Annex 2A + 2B; FDA 21 CFR 1271; ICH Q5A(R2). Most stringent biologics scope.
- **Radiopharmaceuticals overlay** — EU GMP Annex 3; USP <823>.
- **Veterinary medicines overlay** — EudraLex Vol. 4 veterinary-specific guidance.
- **Investigational Medicinal Products (IMP) overlay** — EU GMP Annex 13; FDA IND-stage cGMP per 21 CFR 312.
- **Generic + biosimilar overlay** — ANDA / 351(k) pathways (US); EU centralized + decentralized generic procedures.
- **Site Master File (SMF) template** — EU GMP requirement; PIC/S "Explanatory Notes for Pharmaceutical Manufacturers on the Preparation of a Site Master File."
- **Batch Certificate of Analysis (CoA) template** — finished-product release certificate.
- **Stability Protocol template** — ICH Q1A(R2) + Q1E.
- **Class overlays:** sterile (PIC/S Annex 1 enforced rigor) vs. non-sterile; biologics (ICH Q5A-Q5E) vs. small-molecule; commercial vs. clinical-stage.

## What is intentionally NOT in scope

- **Medical device combination products** → compose `medical-devices + pharma` for combination products; the medical-devices vertical handles device + the pharma vertical handles drug component; combination-product cGMP per 21 CFR Part 4 spans both.
- **Pharmacy compounding** — 21 CFR 503A + 503B; different regulatory framework (FDCA §503A patient-specific + §503B outsourcing facility) outside cGMP scope.
- **Dietary supplements** — 21 CFR 111 (DSHEA cGMP) is a separate regulatory regime.
- **Veterinary feed** — 21 CFR 226; separate framework.

## Standards licensing

**Notable for this vertical:** most pharma regulatory references are PUBLIC license. ICH Q7 / Q9 / Q10 are publicly available from ich.org. 21 CFR 210/211 are public US regulations. EudraLex Vol. 4 + PIC/S Annex 1 are publicly available from EU Commission + PIC/S respectively. The only commercial-license standard referenced is 21 CFR Part 11 *guidance* documents (the regulation itself is public).

This is the first Open QMS vertical where adopters can read every cited regulation/guidance for free — meaningful cost reduction vs. medical-devices / aerospace / automotive where most cited standards are commercial-license ISO/IEC/SAE works. See repo-root `README.md` "Standards licensing — important" for the broader licensing posture.

## Adoption guidance

If your organization:

- **Manufactures only drug product (formulation + finishing)** → use this module with 21 CFR 211 + EU GMP Part I + Annex 15 + PIC/S Annex 1 (if sterile) as primary scope.
- **Manufactures API only** → use this module with ICH Q7 + 21 CFR 210 + EU GMP Part II as primary scope.
- **Combination product** → compose `medical-devices + pharma`.
- **Sterile manufacturing in scope** → PIC/S Annex 1 clauses become highly load-bearing; consider also building a sterile-specific class overlay (forward work).
- **EU market release** → ensure QP designation + QP batch-release SOP per EU GMP Annex 16; Chapter 2 §§2.5–2.7 personnel structure required.
- **Cell + gene therapy / ATMP** → wait for the ATMP overlay (forward), OR use the pharma vertical with awareness that EU GMP Annex 2A + 2B add substantive ATMP-specific requirements not covered here.
