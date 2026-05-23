---
document_id: SRS-XXX-001
title: "[Software Item Name] — Software Requirements Specification"
version: "1.0"
effective_date: YYYY-MM-DD
owner: "[Software Lead, Title]"
status: draft
approved_by: "[Software / QA Lead, Title]"
approval_date: YYYY-MM-DD
---

# SRS-XXX-001: [Software Item Name] Software Requirements Specification

Per IEC 62304 §5.2.

## 1. Purpose and scope

[State the software item this SRS covers — typically a single application, embedded firmware image, or service. Reference the software safety classification (Class A / B / C) per IEC 62304 §4.3 and its justification in the RMF.]

- **Software item:** [name + version]
- **Software safety class:** [A / B / C]
- **Intended use context:** [reference intended-use statement]

## 2. Functional requirements

| Req ID | Requirement | Source | Risk control? | Verification method |
|---|---|---|---|---|
| FR-001 | [The system shall display battery percentage accurate to ±2%.] | User Need UN-005 | No | Test (TC-001) |
| FR-002 | [The system shall halt operation if battery temperature exceeds 60°C.] | RMF H-001 control measure | Yes | Test (TC-012) + analysis |

## 3. Non-functional requirements

| Req ID | Requirement | Type | Verification method |
|---|---|---|---|
| NFR-001 | [System startup time shall not exceed 5 s under nominal conditions.] | Performance | Test |
| NFR-002 | [System shall meet IEC 62443-4-2 SL-2 for cybersecurity.] | Security | Inspection / analysis |
| NFR-003 | [Audit log entries shall not be deletable by application code.] | Security / regulatory | Architectural review |

## 4. Interface requirements

- **External interfaces** — [other devices, networks, services]
- **User interfaces** — [reference to UI specification or wireframes]
- **Hardware interfaces** — [sensors, communication buses]
- **Internal interfaces** — covered in `SAD-XXX-001`.

## 5. Risk-control software requirements

[Per IEC 62304 §5.2.2 — software requirements that implement risk control measures from the RMF. Each must trace back to a hazard in `RMF-XXX-001`.]

| Req ID | Hazard / risk control | RMF reference |
|---|---|---|
| FR-002 | Thermal-runaway shutoff | RMF-XXX-001 H-001 |

## 6. Traceability matrix

[Forward: requirement → architectural element → unit → test. Maintained as a separate artifact or generated from this SRS plus SAD-XXX-001 plus STP-XXX-001 plus VP-XXX-001.]

## 7. Open issues

[Requirements that are not yet finalized, contingent on input from clinical, regulatory, or external dependencies.]

## 8. References

- IEC 62304:2006+A1:2015 §5.2 — Software requirements analysis.
- ISO 13485 §7.3.3 — Design and development inputs (this SRS is the software-item version of the design inputs).
- Linked artifacts: RMF-XXX-001; SAD-XXX-001; STP-XXX-001.

## 9. Revision history

| Version | Date | Author | Changes |
|---|---|---|---|
| 1.0 | YYYY-MM-DD | [Name] | Initial release. |
