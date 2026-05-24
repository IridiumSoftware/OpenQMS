---
document_id: DEA-XXX
title: "[Donor ID — Pseudonymized] — Donor Eligibility Assessment"
version: "1.0"
assessment_date: YYYY-MM-DD
owner: "[Donor Eligibility Reviewer — typically a licensed physician or qualified medical professional, per 21 CFR 1271.50]"
status: draft
qa_approver: "[QA Reviewer responsible for donor-eligibility determination per organization's HCT/P SOP]"
approval_date: YYYY-MM-DD
phi_classification: "PHI — restricted access; this assessment record contains protected health information and shall be stored per the organization's PHI compartmentalization architecture (see project_aaron_medical_context analog: PHI must NOT live in the main GxP repository; OpenQMS captures the eligibility decision + non-PHI traceability; the full assessment lives in a separate access-restricted record per 21 CFR 1271.270 record requirements)"
---

# DEA-XXX: Donor Eligibility Assessment

Per 21 CFR Part 1271 Subpart C — Donor Eligibility (US, applicable to all HCT/Ps including ATMPs derived from cell + tissue donors) + EU Directive 2004/23/EC + Directive 2006/17/EC (EU technical requirements for donation, procurement, testing) + EU GMP Annex 2A §3 (ATMP-specific donor + starting material requirements).

A donor eligibility determination is required for every HCT/P (Human Cells, Tissues, and Cellular and Tissue-Based Products) donor before the cells or tissue may be used in manufacturing — including:

- **Autologous donors** (donor is also recipient — eligibility determination + testing typically simplified per 21 CFR 1271.90(a)(1); but ATMP-specific aseptic + safety considerations remain)
- **Directed allogeneic donors** (specific known donor for specific recipient)
- **Anonymous allogeneic donors**
- **Reproductive-tissue donors** (where in scope; additional requirements apply)

The determination involves: (1) donor screening (interview + medical record review + physical assessment), (2) donor testing for Relevant Communicable Disease Agents (RCDAs), (3) a written determination by a licensed physician or qualified responsible person, (4) documentation retention.

**PHI compartmentalization:** This template captures the eligibility *decision* + the *non-PHI traceability identifiers*. Full donor screening interviews, medical records, test results, and identifiable health information MUST be stored in a separate access-restricted record per 21 CFR 1271.270 retention requirements + applicable privacy law (HIPAA in US; GDPR Special Category data in EU). Open QMS's GitHub-native scope is for the GxP decision + traceability metadata only.

## 1. Donor identification (pseudonymized)

- **Donor unique identifier (UDI; pseudonymized):** [string — links to PHI-bearing record]
- **Donor type:** [autologous / directed allogeneic / anonymous allogeneic / reproductive]
- **Date of donation procedure:** [YYYY-MM-DD]
- **Procurement site:** [licensed facility name + reference number per 21 CFR 1271.10]
- **Intended product / batch:** [ATMP product ID + batch ID]
- **Recipient identifier (autologous + directed allogeneic only; pseudonymized):** [string]

## 2. Donor screening summary (PHI-restricted detail in separate record)

The following ATTESTATIONS reference the full PHI-bearing screening record. The Donor Eligibility Reviewer attests that each item has been reviewed in the source record.

| Screening element | Performed? | Reviewer attestation | Reference to PHI record |
|---|---|---|---|
| Donor medical history interview (per 21 CFR 1271.75(a)(1)) | Y/N | | |
| Physical assessment / examination (per 21 CFR 1271.75(a)(2)) | Y/N | | |
| Relevant medical records review (per 21 CFR 1271.75(a)(3)) | Y/N | | |
| Risk factors for RCDA assessment (per 21 CFR 1271.75(b)) | Y/N | | |
| Behavioral risk factors per FDA Guidance evaluated | Y/N | | |
| Reproductive-tissue-specific screening (if applicable, per 21 CFR 1271.75(d)) | Y/N / NA | | |
| EU-specific screening per Directive 2004/23/EC Annex (if EU jurisdiction) | Y/N / NA | | |

## 3. Donor testing for Relevant Communicable Disease Agents

Per 21 CFR 1271.85 + EU Directive 2006/17/EC Annex II + Annex IV. Testing performed by an FDA-licensed (US) or EU-approved (EU) testing laboratory using FDA-cleared / EU-CE-marked test kits.

| RCDA | Test method | Donor specimen date | Result | Lab reference | Performed by licensed lab? | Notes |
|---|---|---|---|---|---|---|
| HIV-1 + HIV-2 (antibody + NAT) | | | | | Y | |
| HBV (HBsAg + anti-HBc + NAT) | | | | | Y | |
| HCV (anti-HCV + NAT) | | | | | Y | |
| HTLV-1/2 (antibody) | | | | | Y | |
| *Treponema pallidum* (syphilis serology) | | | | | Y | |
| *Trypanosoma cruzi* (anti-T. cruzi — Chagas; for at-risk donors) | | | | | Y | |
| West Nile Virus (NAT — seasonal risk-based per FDA guidance) | | | | | Y / NA | |
| Zika Virus (NAT — if applicable per FDA guidance) | | | | | Y / NA | |
| CMV (relevant for some product categories — e.g., HPCs intended for immunocompromised recipients) | | | | | Y / NA | |
| **Reproductive-tissue-specific RCDAs** (if applicable): Chlamydia + Gonorrhea (NAT) | | | | | Y / NA | |
| **EU-additional** (if EU jurisdiction): Malaria (where risk-based; serology + per donor-history) | | | | | Y / NA | |
| **Risk-based additional testing per donor history:** | | | | | | |

### Testing specimen window

Per 21 CFR 1271.80(b): testing specimen collected at the time of recovery OR within 7 days before or after (whichever requirement applies per HCT/P category). Reproductive-tissue-specific windows per §1271.80(d).

**Specimen-collection-window compliance:** [Yes / No + rationale]

## 4. Determination

| Outcome | Determination |
|---|---|
| [ ] **Eligible** — donor eligible per 21 CFR 1271.50; HCT/Ps may be used in manufacturing | |
| [ ] **Ineligible** — donor ineligible per 21 CFR 1271.50; HCT/Ps shall not be used UNLESS exception per §1271.65 (e.g., autologous use; reproductive-tissue directed donation for sexually intimate partner — with required label + recipient consent) | |
| [ ] **Ineligible — exception invoked per §1271.65** — specify which exception + label + consent documentation: | |
| [ ] **Pending — additional information required** | |

**Determination by:** [licensed physician or qualified responsible person — name + credentials + date]

## 5. Exception handling (per 21 CFR 1271.65 + 1271.90)

If the donor is determined ineligible but HCT/Ps will be used under an exception:

- **Exception cited:** [§1271.65(a) autologous / §1271.65(b)(1) reproductive intimate partner / §1271.65(b)(2) urgent medical need with no suitable alternative / §1271.90(a)(1) autologous use exemption from testing]
- **Required labeling per §1271.65(c):** "FOR AUTOLOGOUS USE ONLY" or applicable warning labels affixed
- **Recipient informed consent documented per §1271.65(d):** [reference]
- **Recipient physician notification of donor ineligibility per §1271.65(d):** [reference]
- **Risk assessment documented in this record:** [summary]

## 6. EU-specific determination (if EU jurisdiction)

Per Directive 2004/23/EC + Annex IV of Directive 2006/17/EC. National competent authority (e.g., Paul-Ehrlich-Institut in DE; ANSM in FR; AEMPS in ES) accreditation/authorization of procurement organization + testing laboratory required.

- **Procurement organization authorization:** [reference]
- **Testing laboratory authorization:** [reference]
- **National competent authority:** [agency]

## 7. Traceability linkage

This DEA links to:

- **Cell/Tissue Traceability Record:** TCTR-XXX
- **Manufacturing Batch Record:** MBR-XXX-batch-N
- **ATMP product:** [product ID]
- **Recipient(s)** (when distributed): per TCTR-XXX bidirectional chain

## 8. Records retention

Per 21 CFR 1271.270 — records retained at least 10 years after the date of administration of the HCT/P (US). Per EU Directive 2004/23/EC Article 8 — records retained at least 30 years after clinical use (EU ATMPs). The longer retention applies for multi-jurisdiction distribution.

- **Retention start date:** [date of HCT/P administration to recipient]
- **Retention end date:** [start + 30 years (EU) OR + 10 years (US-only)]

## 9. Sign-off

| Role | Name | Date | Signature |
|---|---|---|---|
| Donor Eligibility Reviewer (licensed physician / qualified responsible person per 21 CFR 1271.50) | | | |
| QA Reviewer | | | |
| Medical Director (where org policy requires) | | | |
| Responsible Person per EU Directive 2004/23/EC Art. 17 (EU jurisdictions) | | | |

## 10. References

- 21 CFR Part 1271 — Human Cells, Tissues, and Cellular and Tissue-Based Products (HCT/Ps).
  - Subpart C — Donor Eligibility.
  - §1271.50 — How do I determine whether a donor is eligible?
  - §1271.65 — Use of an HCT/P from an ineligible donor.
  - §1271.75 — How do I screen a donor?
  - §1271.80 — What are the general requirements for donor testing?
  - §1271.85 — What are the specific donor testing requirements?
  - §1271.90 — Are there exceptions to the determination + testing requirements?
  - §1271.270 — Records.
- EU Directive 2004/23/EC — Setting standards of quality and safety for the donation, procurement, testing, processing, preservation, storage and distribution of human tissues and cells.
- EU Directive 2006/17/EC — Technical requirements for the donation, procurement and testing of human tissues and cells.
- EU GMP Annex 2A — Manufacture of Advanced Therapy Medicinal Products for Human Use (donor + starting material requirements per §3).
- FDA Guidance for Industry — Eligibility Determination for Donors of Human Cells, Tissues, and Cellular and Tissue-Based Products (August 2007 + subsequent updates).
- Linked: TCTR-XXX (Tissue/Cell Traceability Record), MBR-XXX (Master Batch Record), VSE-XXX (Viral Safety Evaluation Report at the cell-substrate + raw-material level), SOP-XXX (organization's donor-eligibility-determination SOP).

## 11. Revision history

| Version | Date | Author | Changes |
|---|---|---|---|
| 1.0 | YYYY-MM-DD | [Name] | Initial determination. |
