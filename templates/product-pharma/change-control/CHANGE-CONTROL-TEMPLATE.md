---
document_id: CC-XXX
title: "[Change Title] — Change Control"
version: "1.0"
opened_date: YYYY-MM-DD
opened_by: "[Requester — typically Engineering / Manufacturing / QC / IT / Regulatory]"
owner: "[Change Coordinator — typically QA Change Manager]"
status: open
classification: "[Minor / Major / Critical — assigned at QA review]"
qa_approver: "[QA Director (Major + Critical) or QA Change Manager (Minor)]"
implementation_target: YYYY-MM-DD
---

# CC-XXX: Change Control

Per ICH Q10 §3.2.3 + EudraLex Vol. 4 Part I Chapter 1 §1.4(xiv) + 21 CFR 211.100. Change control is the QA-gated change-management process for pharmaceutical manufacturing. Every proposed change to a GMP-relevant element — facility, equipment, utility, material, supplier, specification, formulation, manufacturing process, packaging, labeling, analytical method, computerized system, documentation, organization, contractor, or supplier qualification — requires evaluation + risk assessment + cross-functional review + approval BEFORE implementation. The post-implementation effectiveness check closes the loop.

**Distinct from Deviation:** a Deviation is an *unplanned* departure from approved procedures; Change Control is a *planned* modification to approved procedures.

## 1. Proposed change

- **Change title (concise):** [title]
- **GMP element affected:** [facility / equipment / utility / material / supplier / specification / formulation / process / packaging / labeling / analytical method / computerized system / documentation / organization / contractor / qualified supplier]
- **Current state (what exists today):** [description with references to current MBR, SOPs, drawings, specifications]
- **Proposed state (what will exist after change):** [description]
- **Reason for change:** [continuous improvement / corrective action / regulatory commitment / supplier change / obsolescence / yield + efficiency / new product / etc.]
- **Linked deviation / CAPA / audit finding / customer request / regulatory commitment:** [reference]
- **Products affected:** [enumerated]
- **Manufacturing sites affected:** [enumerated]

## 2. Classification (QA-assigned at intake)

| Classification | Criteria | Approval authority | Implementation gate |
|---|---|---|---|
| **Critical** | Affects product safety / efficacy / regulatory commitment / patient-impacting attributes; OR requires regulatory pre-approval (variation, supplement) | QA Director + Site Head + Regulatory Affairs; QP awareness (EU) | Regulatory approval received + cross-functional sign-off |
| **Major** | Affects validated state of a system / process / equipment; OR triggers re-validation / requalification; OR affects multiple sites / products | QA Director; cross-functional Change Control Board | Cross-functional sign-off + verification of pre-implementation actions |
| **Minor** | Editorial / clarification / like-for-like replacement with no validation impact | QA Change Manager | QA approval + documentation update |

**Assigned classification:** [Minor / Major / Critical]
**Classified by + date:** [QA name + YYYY-MM-DD]
**Classification rationale:** [explicit]

## 3. Risk assessment (ICH Q9)

Required for **Major** + **Critical**. For **Minor**, brief statement sufficient.

| Risk dimension | Pre-change state | Post-change state | Impact (none/low/moderate/high) | Likelihood | Mitigation |
|---|---|---|---|---|---|
| Product quality | | | | | |
| Patient safety | | | | | |
| Regulatory compliance | | | | | |
| Data integrity | | | | | |
| Cross-product contamination | | | | | |
| Supply continuity | | | | | |

**Overall risk rating:** [Low / Medium / High]
**Risk-acceptance rationale:** [explicit]

## 4. Regulatory impact assessment

| Jurisdiction | Submission required? | Submission type | Lead time | Implementation gate |
|---|---|---|---|---|
| FDA (US) | Yes / No | [Type II DMF amendment / CBE-0 / CBE-30 / PAS / Annual Report] | [days] | [pre-approval / post-implementation reporting] |
| EMA / national CA (EU) | Yes / No | [Type IA / IAIN / IB / II variation] | | |
| MHRA (UK) | Yes / No | | | |
| Health Canada | Yes / No | | | |
| PMDA (Japan) | Yes / No | | | |
| Other markets | | | | |

**Linked regulatory tasks:** [reference numbers in regulatory tracking system]

## 5. Pre-implementation actions

| # | Action | Owner | Due date | Status | Reference (protocol / SOP / qualification / training) |
|---|---|---|---|---|---|

Typical pre-implementation actions:

- [ ] Validation / qualification per VMP (IQ / OQ / PQ as applicable)
- [ ] Cleaning validation re-execution (if process / equipment change)
- [ ] Analytical method (re)validation (if method change)
- [ ] CSV per GAMP 5 (if computerized-system change)
- [ ] SOP creation / revision
- [ ] MBR revision
- [ ] Specification revision
- [ ] Training delivery + documentation
- [ ] Customer / supplier notification
- [ ] Regulatory submission(s)
- [ ] Stability protocol initiation (if formulation / packaging change affecting stability)

## 6. Implementation

- **Planned implementation date:** [YYYY-MM-DD]
- **Implementation method:** [step-change / phased rollout / parallel run / etc.]
- **Implementation verification:** [who confirms each pre-implementation action complete + change is operative]
- **Communication plan:** [who is informed when]

## 7. Effectiveness check

Required for **Major** + **Critical**. Performed at a defined interval after implementation (typically 3-6 months).

- **Effectiveness check date:** [YYYY-MM-DD]
- **Method:** [trend analysis on intended-improvement metric / re-audit / process capability study / customer feedback / etc.]
- **Acceptance criterion:** [pre-defined, measurable]
- **Result:** [effective / partially effective + additional action / ineffective + roll-back or re-design]

## 8. Annual review reference

This change is captured in the Annual Product Quality Review (APQR) of all affected products per 21 CFR 211.180(e) + EU GMP Ch. 1 §1.10.

## 9. Sign-off

| Role | Name | Date | Signature |
|---|---|---|---|
| Requester | | | |
| Engineering / Validation Lead | | | |
| Production Lead | | | |
| QC Lead | | | |
| Regulatory Affairs Lead (Critical + Major) | | | |
| IT Lead (CSV changes) | | | |
| QA Change Manager | | | |
| QA Director (Major + Critical) | | | |
| Site Head (Critical) | | | |
| QP (EU jurisdictions, where batch release impacted) | | | |

## 10. References

- ICH Q10 §3.2.3 — Change Management System.
- ICH Q9(R1) — Quality Risk Management.
- ICH Q12 — Technical and Regulatory Considerations for Pharmaceutical Product Lifecycle Management (post-approval change framework).
- EudraLex Vol. 4 Part I Ch. 1 §1.4(xiv) — Pharmaceutical Quality System.
- 21 CFR 211.100 — Written procedures; deviations.
- FDA Guidance for Industry — Changes to an Approved NDA or ANDA (April 2004 + supplements).
- EU Variations Regulation (EC) No 1234/2008 + Guidelines on Variations.
- Linked: VMP-XXX (validation plan updates), DEV-XXX (if change triggered by deviation), CAPA-XXX (if change is a CAPA action), MBR-XXX (if MBR revised), SOP-XXX (if SOP revised), APQR-XXX (annual aggregation).

## 11. Revision history

| Version | Date | Author | Changes |
|---|---|---|---|
| 1.0 | YYYY-MM-DD | [Name] | Initial change request. |
