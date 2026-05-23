---
document_id: SE-XXX
title: "Supplier Evaluation — [Supplier Name]"
version: "1.0"
effective_date: YYYY-MM-DD
owner: "[QA Reviewer, Title]"
status: draft
approved_by: "[QA Lead, Title]"
approval_date: YYYY-MM-DD
---

# SE-XXX: Supplier Evaluation — [Supplier Name]

Per ISO 13485 §7.4.1, 21 CFR 820.50(a). Records the initial qualification or periodic re-evaluation of a single supplier. Output: a binding decision (approve / approve-with-conditions / reject) that updates the Approved Supplier List (ASL-001).

## 1. Supplier identification

- **Supplier name:** [legal name]
- **Address / manufacturing site:** [physical location relevant to the supply]
- **ASL ID:** [SUP-xxx if existing; "PENDING" if new]
- **Evaluation type:** [Initial qualification / Periodic re-evaluation / Triggered re-evaluation]
- **Trigger** (for triggered re-eval): [link to NCR / complaint / supplier change notification]
- **Supplier criticality:** [Critical / Major / Minor — per ASL §2]
- **Scope of supply being evaluated:** [specific products / services / categories]

## 2. Quality system assessment

| Element | Method | Evidence | Adequate? |
|---|---|---|---|
| Quality management system | [Certificate review (ISO 13485, ISO 9001) / On-site audit / Postal questionnaire] | [Cert# + expiry, audit report link, questionnaire ref] | [Yes/No/Partial] |
| Regulatory inspection history | Review (FDA 483s, EU MDR notified-body findings) | [Link to inspection records or supplier statement] | [Yes/No] |
| Cybersecurity posture (if applicable) | Questionnaire + SOC 2 / ISO 27001 evidence | [Link] | [Yes/No/N/A] |
| Risk-based controls match the supply scope | Review against the criticality classification | [Notes] | [Yes/No] |

## 3. Capability assessment

[For Critical and Major suppliers: technical/process capability evaluation — does the supplier have the equipment, processes, qualified personnel, and validated processes to consistently meet the agreed specifications? Reference any first-article inspection (FAI), process capability (Cpk), or lot-qualification data.]

## 4. Sample / lot qualification (if applicable)

| Sample / Lot ID | Receipt date | Inspection results | Disposition |
|---|---|---|---|

## 5. Supplier Quality Agreement (SQA)

- **SQA status:** [Executed / In negotiation / N/A]
- **SQA reference:** [document id, effective date]
- **Key SQA terms verified:** notification of change, right to audit, change control, on-time delivery target, defect rate threshold, regulatory reporting obligations.

## 6. Approval decision

- **Decision:** [Approve / Approve with conditions / Reject]
- **Conditions** (if any): [enumerated conditions; tracking issues opened]
- **Effective dates:** [from / through next re-evaluation]
- **Re-evaluation interval:** [12 / 24 / 36 months per criticality]
- **Next re-evaluation due:** YYYY-MM-DD
- **ASL update:** [Updated to vN.M; link to PR]

## 7. Sign-off

| Role | Name | Date | Signature |
|---|---|---|---|
| QA Reviewer | | | |
| QA Lead | | | |
| Operations / Procurement | | | |

## 8. References

- ISO 13485:2016 §7.4 — Purchasing.
- 21 CFR 820.50 — Purchasing controls.
- EU MDR Article 10(9)(c) — Resources and supplier responsibility.
- Linked artifacts: ASL-001 Approved Supplier List; supplier quality agreement; first-article inspection; trigger record (NCR-xxx / complaint-xxx if applicable).

## 9. Revision history

| Version | Date | Author | Changes |
|---|---|---|---|
| 1.0 | YYYY-MM-DD | [Name] | Initial release. |
