---
document_id: DEV-XXX
title: "[Brief Deviation Description] — Deviation Report"
version: "1.0"
opened_date: YYYY-MM-DD
opened_by: "[Operator / Supervisor reporting the deviation]"
owner: "[Investigation Lead — typically Production Supervisor or QA Investigator]"
status: open
qa_approver: "[QA — assigned at categorization]"
closure_date: YYYY-MM-DD
---

# DEV-XXX: Deviation Report

Per 21 CFR 211.100 + 21 CFR 211.192 + EudraLex Vol. 4 Part I Chapter 1 §1.4(xiv) + ICH Q10 §3.2.2.2. A deviation is any departure from approved procedures (MBR, SOP, specification, sampling plan, analytical method, validated process parameters, environmental controls, equipment qualification, computer-system validation, etc.) during GMP activities — **including deviations where the product still meets specification**. This makes the deviation system broader than the nonconformance (NCR) system: NCRs capture conformance failures; deviations capture procedural departures regardless of conformance outcome.

The deviation report shall be opened within the timeframe specified by site SOP (typically the same shift, certainly the same business day). QA categorization sets the investigation depth + timeline + batch-impact assessment requirements.

## 1. Description

- **Date + time of deviation:** [YYYY-MM-DD HH:MM]
- **Location:** [room / line / suite]
- **Operation in progress:** [step from MBR / SOP — reference MBR-XXX or SOP-XXX]
- **Product / batch affected:** [product name + batch number(s)]
- **Other batches potentially affected** (concurrent or sequential on same equipment): [enumerated; "none" if asserted after investigation]
- **Personnel involved:** [redacted to roles where appropriate — operator, supervisor, etc.]
- **What happened (factual; no root-cause hypothesizing yet):** [narrative]

## 2. Immediate containment

- [ ] Batch placed on hold? Yes / No + rationale
- [ ] Equipment / area quarantined? Yes / No
- [ ] Subsequent operations stopped? Yes / No
- [ ] Other immediate actions: [enumerated]

## 3. Categorization (QA-assigned)

| Category | Criteria | Investigation depth | Investigation timeline (typical) |
|---|---|---|---|
| **Critical** | Patient safety impact OR product quality impact OR regulatory commitment impact OR data-integrity issue OR cGMP fundamental breach (e.g., release without QC testing; bypass of validation) | Full root-cause investigation with multi-functional team; documented batch impact assessment; QA + QP review; regulatory-impact assessment | 30 days |
| **Major** | Significant departure from approved procedure WITHOUT critical impact; recurring minor deviations | Root-cause investigation; documented batch impact assessment; QA review | 30 days |
| **Minor** | Limited departure; no batch impact; no recurrence pattern | Documented assessment + corrective note; QA review | 14 days |

**Assigned category:** [Critical / Major / Minor]
**Categorized by + date:** [QA name + YYYY-MM-DD]
**Categorization rationale:** [explicit justification — required so a later reviewer can audit whether the categorization was appropriate]

## 4. Root-cause investigation

Apply structured methodology (5-Whys / Ishikawa fishbone / FMEA-derived / FTA — adopter's choice per SOP, ICH Q9 risk-based approach):

| Hypothesis | Evidence for | Evidence against | Status |
|---|---|---|---|

**Root cause(s) identified:**
- **Primary:** [statement]
- **Contributing factors:** [enumerated]
- **Why not detected sooner (detection gap):** [if applicable]

## 5. Batch impact assessment

Required for **Critical** + **Major** deviations. For **Minor**, brief statement sufficient.

- **Affected batch(es):** [enumerated]
- **Quality attribute(s) potentially impacted:** [enumerated with rationale]
- **Additional testing required to confirm batch acceptability:** [enumerated; if required, link the executed test results once available]
- **Stability implications:** [if any — link Annual Product Quality Review]
- **Patient-safety implications:** [if any — informs disposition decision]

## 6. Disposition decision

| Disposition | Authority |
|---|---|
| [ ] **Release** — batch meets all specifications + the deviation does not compromise product quality / safety / efficacy. Rationale documented. | QA + QP (EU) |
| [ ] **Release with concession** — batch meets specification but the deviation requires customer notification or other condition. Rationale + condition documented. | QA Director + QP (EU); customer notification per agreement |
| [ ] **Rework** — batch reworked per approved rework instruction (which itself must be approved per change control if not already validated). Re-tested before release. | QA + Production |
| [ ] **Reject** — batch destroyed or returned to supplier. | QA |

**Disposition decision:** [Release / Release with concession / Rework / Reject]
**Decided by + date:** [QA name + YYYY-MM-DD]
**Rationale:** [explicit]

## 7. Corrective + Preventive Action (CAPA)

Link this deviation to one or more CAPA records. Critical + Major deviations typically require formal CAPA (CAPA-XXX). Minor deviations may close with a corrective note inline.

| CAPA # | Type (Corrective / Preventive) | Description | Owner | Due date | Effectiveness check method |
|---|---|---|---|---|---|

## 8. Regulatory impact assessment

- **Reportable to regulator?** Yes / No
- **Regulatory body:** [FDA Field Alert per 21 CFR 314.81(b)(1)(ii) for distributed product / EMA via national competent authority / MHRA / etc.]
- **Reporting timeline:** [3 working days for FDA Field Alert; varies by jurisdiction]
- **Linked regulatory notification:** [reference]

## 9. Effectiveness check

For Critical + Major deviations with CAPA, the corrective + preventive actions shall be evaluated for effectiveness at a defined interval (typically 3-6 months post-implementation).

- **Effectiveness check date:** [YYYY-MM-DD]
- **Method:** [trend analysis / re-audit / surveillance / customer feedback / etc.]
- **Result:** [effective / partially effective + additional action / ineffective + re-investigation triggered]

## 10. Closure + sign-off

| Role | Name | Date | Signature |
|---|---|---|---|
| Investigation Lead | | | |
| Production Supervisor | | | |
| QC Lead (where QC involvement) | | | |
| QA Investigator | | | |
| QA Director (Critical + Major closure) | | | |
| QP (EU jurisdictions, where batch release impacted) | | | |

## 11. References

- 21 CFR 211.100 — Written procedures; deviations.
- 21 CFR 211.192 — Production record review.
- 21 CFR 211.180(e) — Records to be reviewed annually (deviations feed APQR).
- 21 CFR 314.81(b)(1)(ii) — Field Alert Reports.
- EudraLex Vol. 4 Part I Ch. 1 §1.4(xiv) — Pharmaceutical Quality System (deviations + change control).
- EudraLex Vol. 4 Ch. 8 — Complaints, quality defects, product recalls.
- ICH Q9(R1) — Quality Risk Management (informs categorization + investigation methodology).
- ICH Q10 §3.2.2.2 — Corrective Action and Preventive Action.
- Linked: MBR-XXX (where deviation occurred against MBR), SOP-XXX (where against SOP), CAPA-XXX (corrective action), CC-XXX (change control if process change indicated), APQR-XXX (annual aggregation).

## 12. Revision history

| Version | Date | Author | Changes |
|---|---|---|---|
| 1.0 | YYYY-MM-DD | [Name] | Initial deviation entry. |
