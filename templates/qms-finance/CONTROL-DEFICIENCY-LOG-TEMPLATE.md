---
document_id: FIN-DEFLOG-001
title: "Control Deficiency Log"
version: "1.0"
effective_date: YYYY-MM-DD
owner: "[SOX Program Lead, Title]"
status: effective
approved_by: "[CFO / Audit Committee, Title]"
approval_date: YYYY-MM-DD
---

# FIN-DEFLOG-001: Control Deficiency Log

Evaluates and tracks control deficiencies through remediation (PCAOB AS 2201). Each deficiency is classified by **likelihood × magnitude** into deficiency → significant deficiency → material weakness; material weaknesses are disclosed in the §404 assessment.

> **Instance-trace (P15 Tier-2).** A control deficiency is modelled as an `NCR`-kind node and its remediation as a `CAPA` — so the log plugs into `openqms trace-instances` using the existing record vocabulary. Each row's `ID` + `Trace links` columns are walked by the engine.

| ID | Control ID | Deficiency | Likelihood | Magnitude | Classification | Remediation | Status | Trace links |
|---|---|---|---|---|---|---|---|---|
| `NCR-FIN-0001` | C-REV-02 | Cutoff review not evidenced for 1 of 3 months | reasonably possible | inconsequential | deficiency | [re-perform + add reviewer sign-off] | open | `triggers:CAPA-FIN-0001` |
| `NCR-FIN-0002` | ITGC-AC-01 | Quarterly access review missed for [system] | probable | material | **material weakness** | [remediate + disclose in §404] | open | `triggers:CAPA-FIN-0002; relates_to:NCR-FIN-0001` |

The `CAPA-FIN-NNNN` remediations live as CAPA records (file or GitHub issue) and close the loop back via `triggered_by:NCR-FIN-NNNN`.
