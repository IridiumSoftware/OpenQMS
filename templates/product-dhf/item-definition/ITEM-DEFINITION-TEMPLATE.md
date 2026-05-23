---
document_id: ITM-XXX
title: "[Item Name] — Item Definition"
version: "1.0"
effective_date: YYYY-MM-DD
owner: "[Functional Safety Engineering Lead, Title]"
status: draft
approved_by: "[Systems Engineering + FuSa Manager, Title]"
approval_date: YYYY-MM-DD
---

# ITM-XXX: [Item Name] Item Definition

Per ISO 26262:2018 Part 3 §5. The Item Definition is the first concept-phase deliverable. It establishes the boundary of the "item" — the system or array of systems — subject to functional safety analysis. Everything downstream (HARA, Functional Safety Concept, Technical Safety Concept, hardware/software development per Parts 4/5/6) is scoped to what this document says is part of the item.

A correct Item Definition prevents downstream rework: missing boundaries surface as missing safety requirements; missing assumptions surface as missing safe-state definitions; missing dependencies surface as missing dependent-failure analyses in Part 9.

## 1. Item identification

- **Item name:** [name]
- **Item scope:** [single ECU / multi-ECU function / vehicle-level function / cross-domain]
- **Vehicle platform(s):** [platform name + variants]
- **Customer / OEM:** [as applicable]
- **Linked Safety Plan:** SP-XXX
- **Linked HARA:** HARA-XXX (to be created from this definition)

## 2. Functional definition

- **Primary functions:** [enumerated; what the item DOES]
- **Functional groups:** [if multi-function, group them]
- **Non-functional requirements:** [performance, timing, availability, durability]
- **Operating modes:** [enumerated; e.g. drive / park / charge / sleep / diagnostic]
- **State transitions:** [or reference state diagram]

## 3. Boundary

What is IN the item:

- **Components:** [ECUs, sensors, actuators, harness segments]
- **Software:** [identifiable software items running on each ECU]
- **Mechanical:** [mechanical elements where their failure affects function]

What is OUT of the item (and therefore an external interface):

- **External systems:** [other vehicle systems consuming the item's output or providing input]
- **External actors:** [driver, passenger, service technician, OTA back-end, charging infrastructure]

## 4. External interfaces

| Interface | Direction | Medium | Information exchanged | Failure-mode impact on item |
|---|---|---|---|---|
| [name] | in / out / bi | CAN / LIN / Ethernet / analog / mechanical | [signals] | [does loss / wrong / late value compromise function?] |

## 5. Environmental conditions

- **Operating temperature range:** [min..max °C]
- **Storage temperature range:** [min..max °C]
- **Mechanical environment:** [vibration profile, shock, IP rating]
- **Electrical environment:** [voltage range, transient profile per ISO 7637, ESD per ISO 10605]
- **EMC requirements:** [emission + immunity per applicable standard]
- **Lifetime expectations:** [operating hours, calendar years, drive cycles, key cycles]

## 6. Legal + regulatory requirements

Enumerated regulations the item must comply with:

- **Type-approval regulations:** [e.g., UN R79 steering, UN R13 braking, UN R155 cybersecurity, UN R156 software update]
- **Regional standards:** [FMVSS for US, etc.]
- **Customer-Specific Requirements (CSRs):** [reference CSR documents]

Compliance demonstration approach: [reference]

## 7. Preliminary architecture (concept-level)

[Block diagram or textual decomposition. Detail not at the level of TSC — only enough to support HARA hazard identification and to communicate the item's structure.]

- **Major elements:** [ECU(s), sensor(s), actuator(s)]
- **Element allocation rationale:** [why this decomposition; alternative architectures considered]

## 8. Dependencies on other items

| Other item | Dependency type | Direction | FuSa scope of other item | Allocation of safety responsibility |
|---|---|---|---|---|
| [item name] | [data / control / power / mechanical / coordination] | [in / out / bi] | [ASIL X / QM] | [this item's responsibility / other item's / shared] |

Per ISO 26262 Part 8 §5 distributed development: if any of these other items are developed by a different organization, the FuSa interface agreement (DIA — Development Interface Agreement) is referenced here.

## 9. Assumptions of use

What the item assumes about its operating context. Each assumption becomes a safety-relevant boundary condition.

- **Driver assumptions:** [licensed driver / driver attentive / responsibility for driver-initiated actions]
- **Maintenance assumptions:** [scheduled service intervals respected / authorized parts used / authorized SW only]
- **Operational assumptions:** [paved road / temperature within rated range / battery state of charge within limits]
- **Misuse / foreseeable misuse:** [enumerated]

## 10. Preliminary safe state(s)

Concept-level safe state(s) the item should achieve when a fault is detected. Refined to FSR-level safe states in the FSC.

- **Safe state SS-1:** [description; functional implications]
- **Safe state SS-2:** [description; functional implications]

## 11. Allocation of preliminary classification

- **Preliminary ASIL allocation per top-level function:** [to be refined by HARA]
- **Preliminary Cybersecurity Assurance Level (CAL) per top-level function:** [if cybersecurity in scope per ISO/SAE 21434; refined by TARA]

## 12. Open issues / decisions pending

[Anything that needs to be resolved before HARA can complete. Item Definition iterates with HARA.]

## 13. Sign-off

| Role | Name | Date | Signature |
|---|---|---|---|
| Functional Safety Engineering Lead | | | |
| Systems Engineering Lead | | | |
| FuSa Manager | | | |
| Project Manager | | | |

## 14. References

- ISO 26262:2018 Part 3 §5 — Item definition.
- ISO 26262:2018 Part 2 §6 — Confirmation measures (this item definition requires confirmation review).
- Linked: SP-XXX (Safety Plan), HARA-XXX, FSC, TSC, DIAs.

## 15. Revision history

| Version | Date | Author | Changes |
|---|---|---|---|
| 1.0 | YYYY-MM-DD | [Name] | Initial release. |
