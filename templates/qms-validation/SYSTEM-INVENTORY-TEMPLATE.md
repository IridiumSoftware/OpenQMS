---
document_id: VAL-SYSINV-001
title: "Computerized System Inventory"
version: "1.0"
effective_date: YYYY-MM-DD
owner: "[Validation Lead / Quality Manager, Title]"
status: draft
approved_by: "[Quality Manager, Title]"
approval_date: YYYY-MM-DD
---

# VAL-SYSINV-001: Computerized System Inventory

The register of computerized systems used as part of production or the quality management system (ISO 13485 §4.1.6). Each system is classified by **intended use**, **GAMP software category**, and **risk**, which together scope the assurance approach recorded in its [Assurance Determination](ASSURANCE-DETERMINATION-TEMPLATE.md).

## 1. Scope

- **Systems in scope:** software used *directly* in, or *in support of*, production or the QMS. Software *not* part of production/QMS (e.g., email, accounting, generic infrastructure) is out of scope and recorded as such for traceability.
- **Monitoring & measurement software** (ISO 13485 §7.6) is in scope and flagged in the M&M column.

## 2. Inventory (P15 Tier-2 trace table)

Each row is a `SYS` trace node. `Trace links` uses the P15 `rel:ID` grammar.

| ID | System | Intended use (directly / support / not) | GAMP category (1/3/4/5) | M&M software? | Validation status | Trace links |
|---|---|---|---|---|---|---|
| `SYS-[SYSTEM]-001` | [System name + version] | directly | 4 | no | validated | `comprises:FUNC-[SYSTEM]-001` |
| `SYS-[SYSTEM]-002` | [System name + version] | support | 3 | yes | in progress | `comprises:FUNC-[SYSTEM]-010` |

## 3. Maintenance

- Reviewed on each system addition/retirement and at the cadence defined in the [Validation Master Plan](VALIDATION-MASTER-PLAN-TEMPLATE.md).
- A retired system keeps its row (status `retired`) for record continuity (ISO 13485 §4.2.5).
