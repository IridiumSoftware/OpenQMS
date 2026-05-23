---
document_id: SSP-XXX
title: "[Product Name] — System Safety Plan"
version: "1.0"
effective_date: YYYY-MM-DD
owner: "[Safety Engineering Lead, Title]"
status: draft
approved_by: "[Engineering / Safety / Cert Lead, Title]"
approval_date: YYYY-MM-DD
---

# SSP-XXX: [Product Name] System Safety Plan

Per ARP4754A:2010 + ARP4761:1996. The System Safety Plan is the top-level planning document for the safety-assessment process across the system / sub-system / item development lifecycle. It coordinates the FHA, PASA, PSSA, SSA, and CCA activities; defines their inputs / outputs / methods / responsibilities; and ties the safety assessment to the system development process per ARP4754A.

## 1. Scope

- **System / sub-system covered:** [name + level]
- **Linked system development plan:** [reference per ARP4754A]
- **Aircraft type / certification basis:** [as applicable]
- **Certification authority:** [FAA / EASA / TCCA / etc.]

## 2. Safety assessment activities

### 2.1 Functional Hazard Assessment (FHA) — ARP4761 §3

- **Purpose:** identify and classify failure conditions of aircraft / system functions per severity (Catastrophic / Hazardous / Major / Minor / No Safety Effect)
- **Performed at:** conceptual + preliminary design phases
- **Linked deliverable:** FHA-XXX
- **Output drives:** DAL assignments per ARP4754A §5

### 2.2 Preliminary Aircraft Safety Assessment (PASA) — ARP4761 §4

- **Purpose:** evaluate aircraft-level safety implications of proposed architectures + identify safety requirements at aircraft level
- **Performed at:** preliminary design
- **Method:** Fault Tree Analysis (FTA) for aircraft-level failure conditions
- **Output:** derived safety requirements feeding ARP4754A §6 requirements allocation

### 2.3 Preliminary System Safety Assessment (PSSA) — ARP4761 §5

- **Purpose:** evaluate proposed system architecture against system-level safety requirements
- **Performed at:** preliminary design
- **Method:** FTA + qualitative FMEA (Failure Modes and Effects Analysis)
- **Output:** derived safety requirements allocated to items / hardware / software

### 2.4 System Safety Assessment (SSA) — ARP4761 §6

- **Purpose:** verify that the implemented design meets the safety requirements
- **Performed at:** detailed design + verification
- **Methods:** quantitative FTA + FMEA + Markov analysis (where applicable)
- **Output:** SSA report submitted as part of the certification package

### 2.5 Common Cause Analysis (CCA) — ARP4761 §9

CCA comprises three sub-analyses:

- **Zonal Safety Analysis (ZSA)** — physical-zone analysis identifying shared installation risks
- **Particular Risks Analysis (PRA)** — analysis of specific hazards (fire, bird strike, tire burst, etc.) affecting multiple systems
- **Common Mode Analysis (CMA)** — analysis of design / manufacturing / installation / maintenance commonalities that could violate independence assumptions

## 3. Schedule + integration with system development

| Activity | Trigger | Predecessor | Deliverable | Reviewed at |
|---|---|---|---|---|
| FHA (initial) | Conceptual design complete | System concept definition | FHA-XXX v1 | SDR (System Design Review) |
| FHA (update) | Architecture changes; service experience | FHA v1 | FHA-XXX vN | PDR / CDR / Cert |
| PASA / PSSA | Architecture defined | FHA | PASA + PSSA reports | PDR (Preliminary Design Review) |
| SSA (initial) | Detailed design complete | PSSA + design | SSA preliminary | CDR (Critical Design Review) |
| SSA (final) | Verification complete | All V&V results | SSA final | Certification |
| CCA | Detailed design + installation defined | Design baseline | ZSA + PRA + CMA reports | CDR + Cert |

## 4. Responsibilities

| Role | Responsibility |
|---|---|
| Safety Engineering Lead | Overall SSP execution; coordination with cert authority |
| Systems Engineering | Architecture inputs; requirements allocation |
| Software Engineering Lead | DO-178C activities aligned to assigned DAL |
| Hardware Engineering Lead | DO-254 activities aligned to assigned DAL |
| QA | Audit of safety-assessment process per AS9100D §9.2 |
| DER / Compliance Verification Engineer | Certification-authority interface |

## 5. Methods + tools

- **Fault Tree Analysis (FTA):** [tool — e.g. Isograph FaultTree+, FAA's CSRA, etc.]
- **Failure Modes and Effects Analysis (FMEA):** [tool / methodology]
- **Markov analysis:** [if applicable]
- **Reliability data sources:** [MIL-HDBK-217, IEC 62380, vendor-supplied data, in-service data]

## 6. Independence + verification

- **Reviewer independence:** safety assessments shall be reviewed by personnel not involved in the design being assessed, per AS9100D §9.2 + DO-178C / DO-254 DAL-A/B independence requirements.
- **Verification of safety-assessment process:** internal audit per AS9100D §9.2.

## 7. Certification deliverables

| Deliverable | Submitted? | Available on request? |
|---|---|---|
| SSP-XXX (this document) | Y | — |
| FHA-XXX | Y | — |
| PASA report | Y | — |
| PSSA report | Y | — |
| SSA report (final) | Y | — |
| ZSA report | Y | — |
| PRA report | Y | — |
| CMA report | Y | — |

## 8. Sign-off

| Role | Name | Date | Signature |
|---|---|---|---|
| Safety Engineering Lead | | | |
| Systems Engineering Lead | | | |
| Software Lead | | | |
| Hardware Lead | | | |
| QA Lead | | | |
| Certification Engineering | | | |

## 9. References

- ARP4754A:2010 — Guidelines for Development of Civil Aircraft and Systems.
- ARP4761:1996 — Guidelines and Methods for Conducting the Safety Assessment Process on Civil Airborne Systems and Equipment.
- AC 25.1309-1A / AMC 25.1309 — System design and analysis.
- DO-178C:2011 — Software Considerations in Airborne Systems and Equipment Certification.
- DO-254:2000 — Design Assurance Guidance for Airborne Electronic Hardware.
- AC 20-174 — Development of Civil Aircraft and Systems (FAA recognition of ARP4754A).
- Linked artifacts: FHA-XXX, PSAC-XXX (software), PHAC (hardware), TFC-XXX (type-cert pack index).

## 10. Revision history

| Version | Date | Author | Changes |
|---|---|---|---|
| 1.0 | YYYY-MM-DD | [Name] | Initial release. |
