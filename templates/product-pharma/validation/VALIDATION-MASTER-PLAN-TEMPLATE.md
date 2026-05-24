---
document_id: VMP-XXX
title: "[Site or Product Scope] — Validation Master Plan"
version: "1.0"
effective_date: YYYY-MM-DD
owner: "[Validation Lead / Validation Manager, Title]"
status: draft
approved_by: "[QA Director + Site Head]"
approval_date: YYYY-MM-DD
review_cadence: "Annually + on significant change in facility/equipment/process/product portfolio + post-validation findings indicating plan revision"
---

# VMP-XXX: Validation Master Plan

Per ICH Q9 (Quality Risk Management) + ICH Q10 (Pharmaceutical Quality System) + EU GMP Annex 15 (Qualification and Validation) + FDA Process Validation Guidance (2011). The Validation Master Plan (VMP) is the site-level (or product-portfolio-level) document defining the scope, organization, planning, responsibilities, and acceptance criteria for all qualification + validation activities. It is the navigation map across IQ / OQ / PQ for equipment + cleaning validation + process validation + analytical-method validation + computer-system validation.

QA approval per ICH Q10 is mandatory. The VMP is a living document — every change to the validation scope (new product, new equipment, decommissioned line, re-validation requirement) is reflected via change control.

## 1. Scope

- **Site / facility covered:** [name + address]
- **Product portfolio in scope:** [enumerated drug substances + drug products]
- **Manufacturing operations in scope:** [API manufacturing / formulation / sterile filling / packaging / labeling / warehousing]
- **Lifecycle phase covered:** [Stage 1 process design + Stage 2 process qualification + Stage 3 continued process verification per FDA 2011]
- **Out of scope:** [explicitly enumerated — e.g., R&D-scale; non-GMP utilities; clinical-supply manufacturing if separately validated]

## 2. Regulatory + quality basis

- **Applicable regulations / guidances:** ICH Q7, ICH Q9, ICH Q10, 21 CFR 210/211 (US), EudraLex Vol. 4 Annex 15 (EU), PIC/S Annex 1 (sterile), USP / Ph. Eur. / JP monographs as applicable, FDA Process Validation Guidance 2011, EU GMP Annex 11 (computerized systems), GAMP 5.
- **Site quality policy reference:** [link to quality manual]
- **Risk management approach** (per ICH Q9): [FMEA / FMECA / fault-tree / HAZOP / qualitative — describe selection rationale]

## 3. Validation strategy

### 3.1 Equipment qualification (IQ / OQ / PQ)

| Equipment category | Equipment ID(s) | Qualification scope (IQ + OQ + PQ) | Risk class | Lead | Schedule | Deliverable references |
|---|---|---|---|---|---|---|

- **Installation Qualification (IQ):** documented verification that equipment is installed per design specification + manufacturer documentation + applicable codes + utilities are present + materials of construction are correct.
- **Operational Qualification (OQ):** documented verification that equipment operates per specification across the intended operating ranges + alarms + interlocks + boundary conditions.
- **Performance Qualification (PQ):** documented verification that equipment + process consistently produces product meeting predetermined acceptance criteria under simulated or actual production conditions.

### 3.2 Cleaning validation

| Equipment / Train | Worst-case product matrix | Cleaning agents | Sampling method (swab + rinse) | Analytical method | Acceptance criterion | Schedule |
|---|---|---|---|---|---|---|

- **Acceptance criteria** per FDA Process Validation Guidance + EU GMP Annex 15: PDE / ADE-based limits (per the Permitted Daily Exposure approach), or 10-ppm / 1/1000 minimum-daily-dose criterion (traditional approach), visually clean, microbial limits.

### 3.3 Process validation

| Product | Stage 1 (process design) | Stage 2 (PQ — typically 3 consecutive batches at full scale) | Stage 3 (continued process verification) | CPV monitoring metrics |
|---|---|---|---|---|

Stage 3 CPV uses statistical methods (control charts, capability indices) on critical process parameters + critical quality attributes from routine batches.

### 3.4 Analytical method validation

| Method ID | Analyte | Matrix | Validation per ICH Q2 (R1) (specificity / accuracy / precision / range / linearity / LoD / LoQ / robustness / system suitability) | Lead | Schedule |
|---|---|---|---|---|---|

### 3.5 Computer-system validation (CSV)

| System ID | Function | GAMP 5 category (1-5) | EU GMP Annex 11 + 21 CFR Part 11 applicability | Risk-based validation scope | Lead | Schedule |
|---|---|---|---|---|---|---|

## 4. Risk-based prioritization (ICH Q9)

Risk assessment scoring per system + per equipment + per process, driving validation depth + frequency:

| Asset | Risk category | Patient/product/data impact | Detectability | Validation depth (full / reduced) | Re-validation cadence |
|---|---|---|---|---|---|

## 5. Schedule + responsibilities

| Activity | Asset | Phase (IQ / OQ / PQ / CV / PV / AMV / CSV) | Owner | Planned start | Planned end | Status | Linked protocol# |
|---|---|---|---|---|---|---|---|

## 6. Deliverables + documentation control

Each qualification / validation activity produces:

1. **Protocol** — pre-approved test plan describing scope, tests, acceptance criteria, sampling.
2. **Execution data** — raw records + observations + deviations.
3. **Report** — analysis vs. acceptance criteria, deviations + their resolution, conclusion, sign-off.
4. **Linked artifacts** — calibration records, SOPs created/updated, training records.

All under document control per the site's documented-information SOP.

## 7. Re-validation triggers

- Significant change to facility, equipment, materials, formulation, process, supplier, packaging, computerized system, or analytical method.
- Deviation pattern indicating control loss.
- Trend in CPV metrics indicating process drift.
- Periodic re-validation per the established cadence (typically 3-5 years for legacy systems; risk-driven for newer systems under continued process verification).
- Regulatory inspection finding requiring re-validation.

## 8. Validation team + responsibilities

| Role | Responsibility |
|---|---|
| Validation Lead | Overall VMP execution; coordination; reporting to QA Director |
| Subject-Matter Experts (engineering, production, QC, IT) | Protocol authorship + execution + analysis per discipline |
| QA Validation Reviewer | Independent review + approval per ICH Q10 |
| Operations Owner | Ownership of validated asset; continued process verification |
| QA Director | VMP approval; re-validation decisions |
| QP (EU) | Awareness of validation status as input to batch release decisions |

## 9. Training

All personnel involved in validation activities shall be trained per the site training program. Training records cross-referenced in each validation report.

## 10. Sign-off (VMP template approval)

| Role | Name | Date | Signature |
|---|---|---|---|
| Validation Lead | | | |
| Engineering Lead | | | |
| Production Lead | | | |
| QC Lead | | | |
| IT Lead (CSV scope) | | | |
| QA Director (mandatory approval per ICH Q10) | | | |
| Site Head | | | |

## 11. References

- ICH Q7 §12 — Validation (API GMP).
- ICH Q8(R2) — Pharmaceutical Development (informs Stage 1 process design).
- ICH Q9(R1) — Quality Risk Management.
- ICH Q10 §3.2.4 — Process performance and product quality monitoring system.
- ICH Q2(R1) — Validation of Analytical Procedures (for AMV).
- EudraLex Vol. 4 Annex 15 — Qualification and Validation.
- EudraLex Vol. 4 Annex 11 — Computerized Systems.
- 21 CFR Part 11 — Electronic Records / Electronic Signatures.
- FDA Process Validation: General Principles and Practices (Guidance for Industry, January 2011).
- GAMP 5 — A Risk-Based Approach to Compliant GxP Computerized Systems (ISPE).
- Linked: SMF-XXX (Site Master File), MBR-XXX (Master Batch Record references), DEV-XXX (Deviation SOP), CC-XXX (Change Control), individual qualification + validation protocols + reports.

## 12. Revision history

| Version | Date | Author | Changes | Linked CC# |
|---|---|---|---|---|
| 1.0 | YYYY-MM-DD | [Name] | Initial release. | CC-XXX |
