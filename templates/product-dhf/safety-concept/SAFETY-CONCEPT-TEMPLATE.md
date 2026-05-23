---
document_id: SAFC-XXX
title: "[Item Name] — Functional + Technical Safety Concept"
version: "1.0"
effective_date: YYYY-MM-DD
owner: "[Functional Safety Engineering Lead, Title]"
status: draft
approved_by: "[FuSa Manager + Confirmation Reviewer + Cybersecurity Engineering Lead (if cyber scope), Title]"
approval_date: YYYY-MM-DD
---

# SAFC-XXX: [Item Name] Functional and Technical Safety Concept

This template covers two related ISO 26262 deliverables that adopters frequently combine into a single Safety Concept document:

1. **Functional Safety Concept (FSC)** per ISO 26262 Part 3 §7 — derives Functional Safety Requirements (FSRs) from the Safety Goals identified in HARA-XXX, allocates them to a preliminary architecture, and defines safe states + fault detection + warning + degradation strategies. Output of the concept phase.
2. **Technical Safety Concept (TSC)** per ISO 26262 Part 4 §6 — refines the FSRs into Technical Safety Requirements (TSRs) bound to the actual system architecture (hardware + software allocation). Bridges the concept phase and product development.

If cybersecurity is in scope per ISO/SAE 21434, the **Cybersecurity Concept** per ISO/SAE 21434 §9 is structured analogously (Cybersecurity Goals from TARA-XXX → Cybersecurity Requirements → allocation to architecture); adopters may include it in this document or maintain a parallel cyber-concept artifact. Cross-references between safety and security concepts are critical when their controls interact.

---

## Part A — Functional Safety Concept (ISO 26262 Part 3 §7)

### A.1 FSC context

- **Item under analysis:** [name]
- **Linked Item Definition:** ITM-XXX
- **Linked HARA:** HARA-XXX
- **Safety Goals refined by this FSC:**
  - SG-1 (ASIL [X]): [restated]
  - SG-2 (ASIL [X]): [restated]

### A.2 Preliminary architecture (FSC level)

Refine the Item Definition's preliminary architecture to the level needed to allocate FSRs.

[Block diagram or textual decomposition. Identify all elements that will host an FSR. ASIL allocation per element documented.]

| Element | Type | ASIL allocation | Rationale |
|---|---|---|---|
| [name] | ECU / sensor / actuator / SW item | A/B/C/D/QM | [inherits from SG / from ASIL decomposition / from independence claim] |

### A.3 Functional Safety Requirements

For each Safety Goal, derive FSRs that, taken together, achieve the goal.

| FSR # | FSR text | Source SG | ASIL | Allocated to element | Operating mode applicability | Verifiable by |
|---|---|---|---|---|---|---|
| FSR-1.1 | [imperative requirement] | SG-1 | [X] | [element name] | [drive / charge / all] | [analysis / test / review] |

### A.4 Safe states + fault reaction

| Safe state | Triggering FSRs | Achieved by | Time to safe state ≤ FTTI? |
|---|---|---|---|
| SS-1 | FSR-1.1, FSR-1.2 | [strategy] | Yes / No (analysis ref) |

### A.5 Warning + degradation strategies

| Strategy | Scope | Driver-facing? | Implementation outline |
|---|---|---|---|
| [name] | [item or function] | Yes / No | [warning lamp + telltale / audio / haptic / functional degradation] |

### A.6 ASIL decomposition (if invoked, per ISO 26262 Part 9 §5)

If ASIL decomposition is invoked to reduce ASIL requirements on individual elements via redundancy + independence:

| Original FSR ASIL | Decomposed into | Independence argument | Independence verification |
|---|---|---|---|
| ASIL D | ASIL B(D) + ASIL B(D) | [no common-cause failure between branches; independent power / clocking / signal paths] | [DFA reference] |

### A.7 Verification of FSC

Confirmation review per ISO 26262 Part 2 §6 with reviewer at the required level of independence for the highest ASIL in this concept.

| Reviewer | Role | Date | Status |
|---|---|---|---|

---

## Part B — Technical Safety Concept (ISO 26262 Part 4 §6)

### B.1 TSC context

- **Linked FSC:** Part A above (or earlier version)
- **System architecture this TSC binds to:** [reference architecture document]

### B.2 System architectural design

[Refined architecture with hardware + software allocation. ASIL per element per allocation rationale below.]

### B.3 Technical Safety Requirements

For each FSR, derive one or more TSRs bound to specific architectural elements.

| TSR # | TSR text | Source FSR | ASIL | Allocated to | Type (HW / SW / mixed) | Verifiable by |
|---|---|---|---|---|---|---|
| TSR-1.1.1 | [implementation-specific imperative] | FSR-1.1 | [X] | [HW component or SW module] | HW / SW / mixed | [analysis / test / formal] |

### B.4 System architecture safety analyses

| Analysis | Reference | Findings | Closed by |
|---|---|---|---|
| System FMEA | [analysis ref] | [summary] | [TSRs that close failure modes] |
| System FTA | [analysis ref] | [top events analyzed] | [TSRs] |
| Dependent Failure Analysis (Part 9 §7) | [analysis ref] | [common-cause + cascading findings] | [TSRs + independence arguments + barriers] |

### B.5 Allocation of TSRs to hardware + software

Allocation table is the bridge to Part 5 (hardware) and Part 6 (software) deliverables.

| TSR # | Allocated HW | Allocated SW | DIA reference (if cross-organisation) |
|---|---|---|---|

### B.6 System V&V plan (TSC scope)

Brief — full V&V plan tracked separately. List the system-integration tests and system-validation tests that exercise the TSRs.

| TSR # | Verification method | Validation method | Reference |
|---|---|---|---|

### B.7 Confirmation review (TSC)

Same independence requirements as FSC.

| Reviewer | Role | Date | Status |
|---|---|---|---|

---

## Part C — Cybersecurity Concept (ISO/SAE 21434 §9 — if cyber scope applies)

If cybersecurity engineering is in scope (e.g., the item has external interfaces and UN R155 type-approval applies):

### C.1 Cybersecurity Goals

From TARA-XXX (linked).

| CG # | Cybersecurity Goal | CAL | Damage scenarios addressed |
|---|---|---|---|

### C.2 Cybersecurity Requirements

| CSR # | Cybersecurity Requirement | Source CG | CAL | Allocated to element | Interaction with FSR? |
|---|---|---|---|---|---|

### C.3 Safety-security interaction

Where cybersecurity controls and functional-safety mechanisms could interact (e.g., crypto verification on a brake message must not exceed FTTI), document the joint analysis and decisions.

| Interaction | FSR # | CSR # | Resolution |
|---|---|---|---|

---

## Sign-off

| Role | Name | Date | Signature |
|---|---|---|---|
| Functional Safety Engineering Lead | | | |
| Systems Engineering Lead | | | |
| FuSa Manager | | | |
| Cybersecurity Engineering Lead (if cyber scope) | | | |
| Confirmation Reviewer | | | |
| Project Manager | | | |

## References

- ISO 26262:2018 Part 3 §7 — Functional Safety Concept.
- ISO 26262:2018 Part 4 §6 — Technical Safety Concept (formerly Specification of the technical safety requirements).
- ISO 26262:2018 Part 9 §5 — ASIL decomposition; §7 — Analysis of dependent failures.
- ISO/SAE 21434:2021 §9 — Concept phase (Cybersecurity Goals + Concept).
- ISO 26262:2018 Part 2 §6 — Confirmation measures.
- Linked: ITM-XXX (Item Definition), HARA-XXX, TARA-XXX (if cyber), Part-5 HW deliverables, Part-6 SW deliverables, Safety Case, Cybersecurity Case.

## Revision history

| Version | Date | Author | Changes |
|---|---|---|---|
| 1.0 | YYYY-MM-DD | [Name] | Initial release. |
