---
document_id: HARA-XXX
title: "[Item Name] — Hazard Analysis and Risk Assessment"
version: "1.0"
effective_date: YYYY-MM-DD
owner: "[Functional Safety Engineering Lead, Title]"
status: draft
approved_by: "[FuSa Manager + Confirmation Reviewer, Title]"
approval_date: YYYY-MM-DD
---

# HARA-XXX: [Item Name] Hazard Analysis and Risk Assessment

Per ISO 26262:2018 Part 3 §6. The HARA is the systematic identification of hazardous events arising from malfunctions of the item, classification of each event per Severity / Exposure / Controllability, assignment of Automotive Safety Integrity Level (ASIL) per the ASIL determination table, and derivation of Safety Goals.

The HARA's output drives every downstream FuSa activity: ASIL determines process rigor through Parts 4-6; Safety Goals are the top-level safety requirements refined into FSRs (FSC) → TSRs (TSC) → element-level requirements (HW SW). A HARA that misses a hazardous event misses every safety requirement that should have addressed it.

## 1. Item context

- **Item under analysis:** [name]
- **Linked Item Definition:** ITM-XXX
- **HARA scope:** [whole item / specific function / specific operating mode]
- **Analysis team:** [enumerated; multi-disciplinary required per ISO 26262]
- **Independence per ASIL target:** [reviewer independence applies; confirmation review per Part 2 §6 mandatory]

## 2. Operational situations

Enumerate the operational situations the item operates in. Each is the context for hazardous-event classification.

| Situation # | Description | Driving / Parked | Speed range | Road / environment | Other notes |
|---|---|---|---|---|---|
| OS-1 | [e.g., urban driving at 30-50 km/h, dry road, daytime] | Driving | 30-50 km/h | Urban dry asphalt | |
| OS-2 | [e.g., highway cruise at 100-130 km/h, wet road] | Driving | 100-130 km/h | Highway wet asphalt | |

Coverage check: every reasonably-foreseeable operational situation enumerated? Sleep / charge / diagnostic states explicitly considered?

## 3. Item functions + malfunctions

For each function identified in the Item Definition, enumerate the malfunction modes.

| Function # | Function | Malfunction modes |
|---|---|---|
| F-1 | [function name from Item Definition] | M-1.1: function lost; M-1.2: function provides wrong value (high / low / inverted / stuck); M-1.3: function provides intermittent value; M-1.4: function active when not commanded; M-1.5: function delayed beyond allowable timing |

## 4. Hazardous events

Cross-product of functions × malfunctions × operational situations, filtered to hazardous combinations.

| HE # | Function + Malfunction | Operational situation | Hazard at vehicle level | Severity (S) | Exposure (E) | Controllability (C) | ASIL |
|---|---|---|---|---|---|---|---|
| HE-1 | F-1 / M-1.1 | OS-1 | [vehicle-level consequence — what happens to occupants / other road users] | S0..S3 | E0..E4 | C0..C3 | A / B / C / D / QM |

### Severity classes (per ISO 26262 Part 3 §6 Annex B)
- **S0** No injuries
- **S1** Light + moderate injuries
- **S2** Severe + life-threatening injuries (survival probable)
- **S3** Life-threatening + fatal injuries (survival uncertain or impossible)

### Exposure classes
- **E0** Incredible
- **E1** Very low probability (<1% operating time or once a year)
- **E2** Low probability (1-10% or few times a year)
- **E3** Medium probability (10-90% or once a month / fewer per week)
- **E4** High probability (>90% or every drive)

### Controllability classes
- **C0** Controllable in general
- **C1** Simply controllable
- **C2** Normally controllable
- **C3** Difficult to control or uncontrollable

### ASIL determination

| S \ E | E1 | E2 | E3 | E4 |
|---|---|---|---|---|
| **S1**, C1 | QM | QM | QM | QM |
| **S1**, C2 | QM | QM | QM | A |
| **S1**, C3 | QM | QM | A | B |
| **S2**, C1 | QM | QM | QM | A |
| **S2**, C2 | QM | QM | A | B |
| **S2**, C3 | QM | A | B | C |
| **S3**, C1 | QM | QM | A | B |
| **S3**, C2 | QM | A | B | C |
| **S3**, C3 | A | B | C | D |

Higher ASIL → more rigorous safety lifecycle. ASIL D is the most stringent.

## 5. Safety Goals

For each hazardous event with ASIL A or higher, derive a Safety Goal stating the top-level functional safety requirement.

| SG # | Safety Goal | ASIL | Hazardous events addressed | Safe state |
|---|---|---|---|---|
| SG-1 | [imperative: "the item shall [prevent / detect / mitigate] [hazard]"] | A/B/C/D | HE-1, HE-2 | [from Item Definition or refined here] |

ASIL of SG = highest ASIL among the hazardous events it addresses. ASIL inheritance applies — derived FSRs inherit unless ASIL decomposition per Part 9 §5 is invoked.

## 6. Fault tolerance + reaction times

For each Safety Goal, define:

- **Fault Tolerant Time Interval (FTTI):** [maximum duration the item can remain in fault state without entering hazardous state]
- **Emergency Operation Time Interval (EOTI):** [time between fault detection and reaching safe state, if applicable]
- **Maximum Reaction Time:** [must be ≤ FTTI − fault detection time]

## 7. Argumentation for completeness

Per ISO 26262 Part 3 §6.5.4, argue why the set of operational situations + functions + malfunctions + hazardous events is sufficiently complete. Reference:

- Brainstorming method (HAZOP guide-words, FMEA-style, expert workshop)
- Coverage of all functions from Item Definition
- Coverage of all reasonably-foreseeable operational situations
- Consideration of all malfunction patterns (loss, wrong, intermittent, unintended activation, delay)
- Lessons learned from field data on similar items
- Field reports of accidents involving similar items

## 8. Confirmation review (per ISO 26262 Part 2 §6)

Confirmation review per ASIL applicability — for ASIL B/C/D, mandatory; for ASIL A, recommended; conducted by reviewer at the required level of independence.

| Reviewer | Role | Date | Findings | Status |
|---|---|---|---|---|

## 9. Sign-off

| Role | Name | Date | Signature |
|---|---|---|---|
| Functional Safety Engineering Lead | | | |
| Systems Engineering Lead | | | |
| FuSa Manager | | | |
| Confirmation Reviewer | | | |
| Customer Safety Representative (if flow-down requires) | | | |

## 10. References

- ISO 26262:2018 Part 3 §6 — Hazard analysis and risk assessment.
- ISO 26262:2018 Part 3 Annex B — Examples of hazardous events.
- ISO 26262:2018 Part 9 §5 — ASIL decomposition (if invoked to reduce ASIL on individual elements).
- ISO 26262:2018 Part 2 §6 — Confirmation measures (this HARA requires confirmation review).
- Linked: ITM-XXX (Item Definition), FSC (downstream), Safety Case.

## 11. Revision history

| Version | Date | Author | Changes |
|---|---|---|---|
| 1.0 | YYYY-MM-DD | [Name] | Initial release. |
