---
document_id: RMF-CARDIO-0100
title: "Risk Management File — Cardio Infusion Pump (worked example)"
version: "1.0"
effective_date: 2026-06-01
owner: "[Risk Manager]"
status: effective
---

# RMF-CARDIO-0100: Risk Management File (worked example)

**Tier-2 demonstration.** This document is a *container* (no `record_kind` in its frontmatter, so it isn't itself a trace node) — instead, its **hazards and mitigations are rows in trace tables**. Each row's `ID` + `Trace links` columns are parsed by `openqms trace-instances`, so the items participate in the instance graph individually. Illustrative; not a real device record.

## 1. Hazard analysis

| ID | Hazard | Severity | Trace links |
|---|---|---|---|
| `HAZ-CARDIO-0050` | Air-in-line not detected | Critical | mitigated_by:MIT-CARDIO-0051 |

## 2. Risk controls

| ID | Mitigation | Trace links |
|---|---|---|
| `MIT-CARDIO-0051` | Ultrasonic air-in-line detector + alarm + occlusion stop | verified_by:TST-CARDIO-0021 |

Note the cross-tier link: the Tier-2 row `MIT-CARDIO-0051` is `verified_by` `TST-CARDIO-0021`, a Tier-1 whole-record file in this same example set — the two tiers compose into one graph.
