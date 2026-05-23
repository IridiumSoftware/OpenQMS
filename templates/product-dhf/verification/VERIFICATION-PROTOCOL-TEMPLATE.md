---
document_id: VP-XXX-001
title: "[Product Name] — Verification Protocol"
version: "1.0"
effective_date: YYYY-MM-DD
owner: "[V&V Lead, Title]"
status: draft
approved_by: "[QA / Engineering Lead, Title]"
approval_date: YYYY-MM-DD
---

# VP-XXX-001: [Product Name] Verification Protocol

## 1. Purpose and scope

[State the design outputs being verified — typically a specific subsystem, software item, or product version. Verification answers "did we build the product right" against the design inputs.]

- **Design inputs verified:** [link to DI-* issues or DESIGN-INPUT-TEMPLATE records]
- **Design outputs verified:** [link to specific deliverables — drawings, code revs, parts]
- **Product version under test:** [SW version, HW rev, etc.]

## 2. Verification methods

- [Inspection / analysis / test / demonstration — per design output type.]
- [Sample size justification — typically driven by risk analysis.]
- [Test environment specification — bench setup, simulated load, calibrated instruments.]
- [Acceptance criteria — explicit pass/fail thresholds per requirement.]

## 3. Per-requirement verification table

| Req ID | Requirement (summary) | Method | Acceptance criterion | Test case ID | Evidence link | Pass / Fail |
|---|---|---|---|---|---|---|
| REQ-001 | [Device shall display battery percentage] | Test | [accuracy ±2% from 0–100%] | TC-001 | [results URL] | Pass |

## 4. Deviations

[Document any deviations from the protocol — instrument substitution, test condition variance, etc. Each deviation gets an impact assessment and disposition.]

## 5. Conclusion

[Statement that all requirements in scope have been verified and acceptance criteria met (or, if not, what is open). Sign-off by V&V lead and quality.]

## 6. References

- 21 CFR 820.30(f) — Design verification.
- ISO 13485:2016 §7.3.6 — Design and development verification.
- IEC 62304 §5.5 (software unit verification), §5.6 (software integration testing), §5.7 (software system testing) — if software is in scope.
- Linked artifacts: DI-* design inputs; DO-* design outputs; RMF-XXX-001 risk management file.

## 7. Revision history

| Version | Date | Author | Changes |
|---|---|---|---|
| 1.0 | YYYY-MM-DD | [Name] | Initial release. |
