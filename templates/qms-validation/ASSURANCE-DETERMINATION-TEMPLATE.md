---
document_id: VAL-ASSURDET-[SYSTEM]-001
title: "Assurance Determination (Risk-Based)"
version: "1.0"
effective_date: YYYY-MM-DD
owner: "[Validation Lead, Title]"
status: draft
approved_by: "[Quality Manager, Title]"
approval_date: YYYY-MM-DD
---

# VAL-ASSURDET-[SYSTEM]-001: Assurance Determination for [System name]

The **documented risk decision** that scopes assurance per feature/function. Format mirrors FDA CSA's worked-example tables; authored as a **P15 Tier-2 trace table** so each `FUNC` row links to its requirements and assurance record.

> **Honesty bound (OQ-080):** this template *records* the risk judgment. Whether a function is high process risk, and which tier is appropriate, is the manufacturer's determination — Open QMS does not make it.

## 1. System

- **System:** [name + version] — inventory ref `SYS-[SYSTEM]-001`
- **GAMP category:** [1 / 3 / 4 / 5]
- **Overall intended use:** [directly / support / not part of production or QMS]

## 2. Per-function determination

`Intended use` ∈ {directly, support, not}. `Risk` ∈ {high process risk, not high process risk} — *high* = failure foreseeably compromises safety. `Tier` ∈ {scripted-robust, scripted-limited, unscripted-scenario, unscripted-exploratory}; the risk→tier mapping is **not rigid** (CSA §V.A.4).

| ID | Feature / function / operation | Intended use | Risk-based analysis (+ rationale) | Assurance tier | Trace links |
|---|---|---|---|---|---|
| `FUNC-[SYSTEM]-001` | [e.g., automated acceptance decision with no human review] | directly | high process risk — [rationale] | scripted-robust | `part_of:SYS-[SYSTEM]-001; assured_by:VREC-[SYSTEM]-001; validates:URS-[SYSTEM]-003` |
| `FUNC-[SYSTEM]-002` | [e.g., record-keeping / reporting] | directly | not high — [rationale] | unscripted-exploratory | `part_of:SYS-[SYSTEM]-001; assured_by:VREC-[SYSTEM]-002` |

## 3. Vendor leverage (CSA §V.A.5)

Record existing controls leveraged to reduce assurance effort: vendor evaluation/validation records, SOC 2 / ISO certifications, monitoring data, established downstream controls. Cross-reference the [supplier evaluation](../qms-suppliers/) where applicable.
