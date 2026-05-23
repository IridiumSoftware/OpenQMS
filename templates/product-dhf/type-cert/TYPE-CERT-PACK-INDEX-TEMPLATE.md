---
document_id: TCC-XXX
title: "[Product Name] — Type Certificate Pack Index"
version: "1.0"
effective_date: YYYY-MM-DD
owner: "[Certification Engineering Lead, Title]"
status: draft
approved_by: "[Cert Eng / QA + Designated Engineering Representative (FAA) or Compliance Verification Engineer (EASA), Title]"
approval_date: YYYY-MM-DD
---

# TCC-XXX: [Product Name] Type Certificate Pack Index

Per 14 CFR Part 21 (FAA) + EASA Part-21 Subpart B. The Type Certificate Pack is the navigable manifest of every document constituting the application for and substantiation of a type certificate (TC) — for aircraft, engines, propellers, or appliances under the relevant certification specifications (CS-23, CS-25, CS-27, CS-29, CS-E, CS-P depending on product type).

This index is to aerospace what the medical-devices Technical File Index (TFI) is to medical devices: the structured manifest that certification authorities review, with each section referencing the controlled documents that constitute the actual content.

## 1. Product identification

- **Product name + designation:** [name]
- **Product type:** [aircraft / engine / propeller / appliance]
- **Type Certificate number (assigned by authority on issuance):** [TC# / TCDS#]
- **Applicant:** [legal name + registered address]
- **Country of design / production:** [as applicable]
- **Manufacturer's design organisation approval (DOA) reference** (EASA): [reference]
- **Production organisation approval (POA) reference** (EASA): [reference]
- **FAA Production Certificate** (if US): [PC#]
- **Linked SSP:** SSP-XXX
- **Linked safety-substantiation packs:** FHA-XXX, PSAC-XXX, PHAC (hardware)

## 2. Certification basis

- **Applicable airworthiness regulations:** [14 CFR Part 23 / 25 / 27 / 29 / 33 / 35; CS-23 / 25 / 27 / 29 / E / P]
- **Effective date of cert basis:** [date / amendment level]
- **Special conditions:** [enumerated]
- **Equivalent safety findings:** [enumerated]
- **Exemptions granted:** [enumerated]
- **Means of Compliance (MoC):** [Type Certification Plan reference]

## 3. Cert pack index — by 14 CFR / EASA section

| Section | Topic | Document(s) | Version | Doc ID | Status |
|---|---|---|---|---|---|
| 21.31 (FAA) / Part-21A.31 (EASA) | Type design | [drawings + specs] | | | |
| 21.33 (FAA) / Part-21A.33 (EASA) | Inspections and tests | [test plans + reports] | | | |
| 21.35 (FAA) / Part-21A.35 (EASA) | Flight tests | [flight test plan + results] | | | |
| 21.41 (FAA) / Part-21A.41 (EASA) | Type Certificate Data Sheet (TCDS) | [TCDS draft] | | | |
| 21.50 (FAA) / Part-21A.61 (EASA) | Instructions for Continued Airworthiness (ICA) | [maintenance manual + service letters + AD plan] | | | |
| 21.97 (FAA) / Part-21A.93 (EASA) | Design changes | [change-control records; major vs minor classification] | | | |

## 4. Cert pack index — by airworthiness section (typical CS-25 / 14 CFR Part 25 layout)

| Subpart | Topic | Document(s) | Compliance Method | Substantiation |
|---|---|---|---|---|
| A | General | | | |
| B | Flight | | flight tests | |
| C | Structure | | analysis + test | |
| D | Design and construction | | analysis + test | |
| E | Powerplant | | bench test + flight test | |
| F | Equipment | | DO-178C SW + DO-254 HW per ARP4754A | |
| G | Operating limitations and information | | | |

## 5. Safety substantiation pack

| Item | Reference | Version |
|---|---|---|
| System Safety Plan | SSP-XXX | |
| FHA (aircraft level) | FHA-XXX-AC | |
| FHA (per-system) | FHA-XXX-SYS-N | |
| PASA report | | |
| PSSA reports | | |
| SSA report | | |
| ZSA + PRA + CMA reports | | |

## 6. Software substantiation pack (per DO-178C, per software item)

| Software Item | DAL | PSAC | SAS | SCI | Status |
|---|---|---|---|---|---|

## 7. Hardware substantiation pack (per DO-254, per hardware item)

| Hardware Item | DAL | PHAC | HAS (Hardware Accomplishment Summary) | HCI (Hardware Configuration Index) | Status |
|---|---|---|---|---|---|

## 8. Production-readiness substantiation

| Item | Reference |
|---|---|
| First Article Inspection records | FAI-XXX (per part) |
| AS9100D QMS certification | [cert# + body + expiry] |
| Process specifications + Nadcap certifications (special processes) | [list] |

## 9. Continued operational safety (COS) plan

Per 14 CFR 21.50 / EASA Part-21A.3A:

- **Issuer of ICA:** [organization]
- **ICA scope:** scheduled maintenance, inspection, troubleshooting, overhaul
- **Service Letter / Service Bulletin process:** [reference to SOP]
- **Airworthiness Directive (AD) response process:** [reference to SOP]
- **In-service data collection:** [system; reliability data feedback into RMF + SSA updates]

## 10. Submission package assembly

For TC application, this index is exported with all referenced documents bundled. The export process (typically `gh` API or a script) produces:

- **TC application package** — FAA Form 8110-12 / EASA application form + this index + all referenced documents at their referenced versions.
- **Type Certificate Data Sheet (TCDS)** — issued by authority on TC grant.

## 11. Sign-off

| Role | Name | Date | Signature |
|---|---|---|---|
| Certification Engineering Lead | | | |
| Engineering (per discipline) | | | |
| QA Lead | | | |
| DER (FAA) / CVE (EASA) | | | |
| Authorized Signatory (Applicant) | | | |

## 12. References

- 14 CFR Part 21 — Certification Procedures for Products and Articles.
- EASA Part 21 — Certification of aircraft and related products, parts and appliances, and of design and production organisations.
- 14 CFR Parts 23 / 25 / 27 / 29 / 33 / 35 — Airworthiness standards per product type.
- EASA CS-23 / CS-25 / CS-27 / CS-29 / CS-E / CS-P — Certification specifications per product type.
- AC 20-174 / AMC 20-174 — Development of civil aircraft + systems (ARP4754A recognition).
- AC 20-115 / AMC 20-115 — Software development per DO-178C.
- Linked artifacts: SSP-XXX, FHA-XXX, PSAC-XXX, PHAC, FAI-XXX (per part), AS9100D QMS certificate.

## 13. Revision history

| Version | Date | Author | Changes |
|---|---|---|---|
| 1.0 | YYYY-MM-DD | [Name] | Initial release. |
