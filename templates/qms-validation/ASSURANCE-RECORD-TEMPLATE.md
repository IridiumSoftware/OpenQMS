---
document_id: VAL-ASSURREC-[SYSTEM]-001
title: "Assurance Record"
version: "1.0"
effective_date: YYYY-MM-DD
owner: "[Tester / Validation Lead, Title]"
status: draft
approved_by: "[Quality Manager, Title]"
approval_date: YYYY-MM-DD
record_kind: VREC
record_id: VREC-[SYSTEM]-001
trace_links:
  assures:
    - FUNC-[SYSTEM]-001
  verifies:
    - URS-[SYSTEM]-003
---

# VAL-ASSURREC-[SYSTEM]-001: Assurance Record

Objective evidence that one feature/function was assessed and performs as intended (ISO 13485 §4.2.5; CSA §V.A.6). **Required sections gate on the declared assurance tier.**

## 1. Always required

- **Intended use:** [of the feature/function]
- **Risk-based analysis result:** [high / not-high + rationale; ref `FUNC-[SYSTEM]-001`]
- **Assurance tier:** [scripted-robust / scripted-limited / unscripted-scenario / unscripted-exploratory]
- **Testing performed:** [description]
- **Issues found:** [deviations / defects / failures, or "none"]
- **Conclusion of acceptability:** [acceptable for intended use; with resolution or risk justification of any issues]
- **Performed by / date:** [name, role] / YYYY-MM-DD
- **Review / approval:** [signature + date where appropriate]

## 2. Tier-dependent evidence

- **Scripted — robust** *(≈ classic CSV / IQ-OQ-PQ)*: detailed test protocol (objectives + step-by-step cases + expected results), result for each case, detailed report, independent review/approval.
- **Scripted — limited**: limited step-by-step cases + expected results; identify the unscripted methods also applied.
- **Unscripted — scenario / error-guessing**: summary of features/failure-modes tested (no per-case protocol).
- **Unscripted — exploratory**: high-level objectives with pass/fail criteria; summary of objectives tested.

## 3. Digital record

Prefer system-generated evidence — logs, audit trails, automated traceability — over manual screenshots (CSA §V.A.6). In a git-native QMS, the commit + CI run is part of the record.
