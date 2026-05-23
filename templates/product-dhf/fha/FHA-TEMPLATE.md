---
document_id: FHA-XXX
title: "[Product Name] — Functional Hazard Assessment"
version: "1.0"
effective_date: YYYY-MM-DD
owner: "[Safety Engineer / Cert Engineer, Title]"
status: draft
approved_by: "[Safety / Cert Engineering Lead, Title]"
approval_date: YYYY-MM-DD
---

# FHA-XXX: [Product Name] Functional Hazard Assessment

Per ARP4761:1996 §3 (Aircraft FHA + System FHA). The FHA is performed early in the aircraft / system development lifecycle to identify and classify the failure conditions of aircraft + system functions according to their severity. The resulting severity classifications drive the Design Assurance Levels (DAL A-E) assigned to the systems, items, hardware (per DO-254), and software (per DO-178C) that implement those functions.

The FHA is the first formal safety-assessment activity in the ARP4754A / ARP4761 process and is supplemented downstream by PSSA, SSA, and CCA.

## 1. Scope

- **Subject:** [aircraft / system / sub-system being assessed]
- **Level:** [Aircraft FHA / System FHA]
- **Linked system documentation:** SSP-XXX (system safety plan); ARP4754A system development plan
- **Certification basis:** [14 CFR / CS-XX.1309 + AC/AMC 25.1309 + applicable special conditions]
- **Phase:** [Conceptual design / Preliminary design / Detailed design]

## 2. Functions identified

[Per the level (aircraft or system), enumerate the functions in scope. Aircraft FHA: high-level aircraft functions (e.g. "provide thrust", "maintain controlled flight"). System FHA: functions allocated to the subject system per ARP4754A §6.]

| Function ID | Function | Operating mode(s) | Phase of flight relevance |
|---|---|---|---|

## 3. Failure conditions

[For each function, identify the failure conditions — total loss, partial loss, malfunction, erroneous operation, undetected vs detected, etc. Each failure condition gets a row.]

| FC ID | Function ID | Failure condition (textual description) | Operating mode | Phase of flight |
|---|---|---|---|---|

## 4. Effect analysis

For each failure condition, document:

| FC ID | Effect on aircraft | Effect on crew | Effect on occupants | Effect on certification basis |
|---|---|---|---|---|

## 5. Severity classification

Per ARP4761 §3.4 + AC/AMC 25.1309. Each failure condition is classified into one of:

| Classification | Description | DAL implication |
|---|---|---|
| **Catastrophic** | Failure conditions that would prevent continued safe flight and landing | DAL A |
| **Hazardous / Severe-Major** | Failure conditions that would reduce the capability of the aircraft or crew to cope with adverse operating conditions to the extent there would be a large reduction in safety margins or functional capabilities; physical distress to flight crew; injuries to occupants | DAL B |
| **Major** | Failure conditions that would reduce capability of aircraft or crew to cope with adverse conditions; significant reduction in safety margins or functional capabilities; physical discomfort to occupants possibly including injuries | DAL C |
| **Minor** | Failure conditions that would not significantly reduce aircraft safety; involve crew actions that are well within their capabilities; minor inconvenience to occupants | DAL D |
| **No Safety Effect** | Failure conditions that would have no effect on safety | DAL E |

## 6. Failure condition table

| FC ID | Severity | Quantitative target | Rationale | DAL assigned to implementing items |
|---|---|---|---|---|

**Quantitative targets** (per AC/AMC 25.1309) for transport-category aircraft:

| Classification | Probability per flight hour |
|---|---|
| Catastrophic | < 1×10⁻⁹ |
| Hazardous | < 1×10⁻⁷ |
| Major | < 1×10⁻⁵ |
| Minor | < 1×10⁻³ |
| No Safety Effect | No requirement |

## 7. DAL assignment summary

| Implementing item | DAL | Driving failure condition(s) |
|---|---|---|

[The DAL assignment table flows directly into the DO-178C PSAC (software) and DO-254 PHAC (hardware) for items implementing functions identified in the FHA.]

## 8. Update triggers

The FHA shall be updated when:

- New functions are added to the aircraft / system
- Failure-mode understanding changes based on PSSA / SSA findings
- Service experience reveals previously-unidentified failure conditions
- Certification basis changes (new regulation, special condition, equivalent safety finding)

## 9. Sign-off

| Role | Name | Date | Signature |
|---|---|---|---|
| Safety Engineer | | | |
| Certification Engineering | | | |
| Systems Engineering Lead | | | |
| QA Lead | | | |

## 10. References

- ARP4761:1996 §3 — Functional Hazard Assessment.
- ARP4754A:2010 — Guidelines for Development of Civil Aircraft and Systems.
- AC 25.1309-1A / AMC 25.1309 — System design and analysis.
- FAA Order 8110.49 — Software Approval Guidelines.
- Linked artifacts: SSP-XXX, PSAC-XXX, RMF-XXX-001 (operational risk — distinct from safety risk).

## 11. Revision history

| Version | Date | Author | Changes |
|---|---|---|---|
| 1.0 | YYYY-MM-DD | [Name] | Initial release. |
