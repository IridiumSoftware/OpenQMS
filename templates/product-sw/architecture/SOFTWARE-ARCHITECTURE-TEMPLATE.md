---
document_id: SAD-XXX-001
title: "[Software Item Name] — Software Architecture Description"
version: "1.0"
effective_date: YYYY-MM-DD
owner: "[Software Architect, Title]"
status: draft
approved_by: "[Software Lead, Title]"
approval_date: YYYY-MM-DD
---

# SAD-XXX-001: [Software Item Name] Software Architecture Description

Per IEC 62304 §5.3.

## 1. Purpose and scope

[State which software item this SAD describes; reference its SRS.]

- **Software item:** [name + version]
- **Software safety class:** [A / B / C — same as SRS]
- **Linked SRS:** SRS-XXX-001

## 2. Architectural overview

[Block diagram or narrative describing the top-level architecture. Identify the major software items, their responsibilities, and how they interact.]

## 3. Software item decomposition

[Per IEC 62304 §5.3.2 — decompose into software items and (for Class B/C) software units. Each item gets a safety classification; segregation is documented if items of different classes share a process/address space.]

| Item ID | Name | Class | Description | Hosts SOUP? |
|---|---|---|---|---|
| ITEM-001 | [Acquisition service] | C | [reads sensors, applies signal conditioning] | No |
| ITEM-002 | [UI layer] | A | [renders patient-facing readout] | Yes (see SOUP-XXX-001) |

## 4. Interfaces

- **Internal interfaces:** [API contracts between items; data formats; thread/process boundaries.]
- **External interfaces:** [other devices, network protocols, OS calls — cross-reference SRS §4.]
- **SOUP interfaces:** [each SOUP item's API surface used by application code — cross-reference SOUP-XXX-001.]

## 5. Risk-control architecture

[Per IEC 62304 §5.3.5 — how the architecture supports the risk control measures specified in the SRS and ultimately the RMF. For Class C software, this is where segregation of safety-critical items from non-safety items is documented.]

| RMF hazard | Risk control SRS requirement | Architectural mechanism |
|---|---|---|
| H-001 (thermal runaway) | FR-002 (thermal shutoff) | ITEM-001 runs in its own RTOS task with hardware watchdog; thermal-monitor interrupt is non-maskable. |

## 6. Security architecture

[Authentication, authorization, audit logging, cryptographic mechanisms, secrets management. Reference any IEC 62443, NIST 800-53, or ISO 27001 controls in scope.]

## 7. SOUP integration map

[High-level: which SOUP items are used by which architectural items, and what the SOUP failure modes are (per SOUP-XXX-001) that the architecture must tolerate.]

## 8. References

- IEC 62304:2006+A1:2015 §5.3 — Software architectural design.
- Linked artifacts: SRS-XXX-001; RMF-XXX-001; SOUP-XXX-001.

## 9. Revision history

| Version | Date | Author | Changes |
|---|---|---|---|
| 1.0 | YYYY-MM-DD | [Name] | Initial release. |
