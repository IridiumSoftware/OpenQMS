---
document_id: RA-XXX
title: "[Subject / Decision Scope] — Risk Assessment"
version: "1.0"
assessment_date: YYYY-MM-DD
owner: "[Lead Assessor — typically Risk Manager or Subject-Matter Expert]"
status: draft
approved_by: "[Management approver per the decision level — e.g., Top Management for strategic; Process Owner for operational]"
approval_date: YYYY-MM-DD
applicable_methodology: "[FMEA / FTA / HAZOP / What-If / bow-tie / qualitative L×C / quantitative; per ISO 31010]"
---

# RA-XXX: Standalone Risk Assessment

A standalone risk assessment — distinct from the living Risk and Opportunity Register (ROR-XXX) — applied to a specific decision, change, scope expansion, project, or event. The ROR is the steady-state QMS-level register; this template is for *bounded* risk assessments where a specific question demands a deeper or one-time-use analysis.

Use cases:
- New product launch — pre-launch risk assessment
- Site relocation or new facility
- Major IT system migration
- New supplier qualification at a substantive scope
- Pre-merger due-diligence risk review
- Regulatory-change impact assessment
- BCMS scenario assessment (per ISO 22301 §8.2.3)
- Cybersecurity-specific TARA (when this template is used in lieu of TARA-TEMPLATE)

This template is methodology-flexible per ISO 31010 — adopters select the technique that fits the assessment scope.

## 1. Scope + objective

- **Subject of assessment:** [the decision / change / project / event being assessed]
- **Objective:** [what question this assessment is answering — e.g., "Is the proposed second-source supplier acceptable from a quality + continuity + cybersecurity perspective?"]
- **Assessor team:** [list with roles + competence]
- **Method selected per ISO 31010:** [name + rationale for selection]
- **Scope boundary:** [what's in + what's out]
- **Time horizon:** [over what period are risks being assessed]
- **Assumptions:** [enumerated]
- **Information sources used:** [enumerated]

## 2. Risk identification

| Risk # | Risk statement | Source | Category | Impact axes |
|---|---|---|---|---|

Categories: strategic / financial / operational / regulatory / safety / cybersecurity / reputational / supply-chain / environmental / human-resources / technology / legal / political.

Impact axes: quality / safety / financial / reputational / regulatory / schedule / operational / strategic.

## 3. Risk analysis

Per the selected ISO 31010 method:

### Method: [FMEA / FTA / HAZOP / etc.]

[Method-specific analysis — RPN for FMEA; fault tree for FTA; HAZOP guide-word table; bow-tie diagram; etc.]

| Risk # | Likelihood | Consequence | Inherent risk rating | Existing controls | Control effectiveness | Residual risk rating |
|---|---|---|---|---|---|---|

## 4. Risk evaluation

For each risk:

| Risk # | Residual risk | Acceptable per criterion? | Treatment recommendation |
|---|---|---|---|

## 5. Risk treatment plan

For risks above acceptance threshold:

| Risk # | Treatment | Method (avoid / reduce / share / retain) | Owner | Resource | Due date | Effectiveness check |
|---|---|---|---|---|---|---|

## 6. Residual risk acceptance

Risks accepted in their residual state (treatment not pursued OR treatment maxed-out but residual still above threshold) require explicit acceptance at the appropriate management level:

| Risk # | Residual rating | Acceptor | Rationale | Re-evaluation date |
|---|---|---|---|---|

## 7. Communication + consultation

Per ISO 31000 §6.4 — risk-assessment results communicated to + consulted with affected stakeholders:

| Stakeholder | Communication channel | Date | Feedback |
|---|---|---|---|

## 8. Monitoring + review (post-assessment)

This assessment is reviewed [periodically per scope] OR [on trigger event] OR [as part of next decision cycle].

- **Next scheduled review:** [date]
- **Triggers for early re-review:** [enumerated]

## 9. Linkage to other risk artifacts

- **Risk-and-Opportunity Register (ROR-XXX):** risks from this assessment that persist as steady-state concerns are added to the ROR
- **Domain-specific risk artifacts (RMF / HARA / TARA / Donor Eligibility / etc.):** cross-referenced where this assessment touches product/process safety
- **Business Impact Analysis (BIA-XXX):** if this is a BCMS scenario assessment per ISO 22301 §8.2.3

## 10. Decision + sign-off

**Decision:** [proceed / proceed with conditions / do not proceed / further information needed]

**Rationale:** [explicit summary citing the assessment results]

**Conditions (if proceed-with-conditions):** [enumerated]

| Role | Name | Date | Signature |
|---|---|---|---|
| Lead Assessor | | | |
| Assessor team members | | | |
| Subject-matter approver | | | |
| Decision approver (per decision-rights matrix) | | | |

## 11. References

- ISO 31000:2018 — Risk management — Guidelines.
- ISO/IEC 31010:2019 — Risk management — Risk assessment techniques.
- ISO 9001:2015 §6.1 (and Annex SL equivalents in 13485, AS9100D, IATF 16949, etc.).
- ICH Q9(R1) — Quality Risk Management (informs pharma assessments).
- Linked: ROR-XXX (Risk and Opportunity Register — steady-state); domain-specific risk artifacts (RMF / HARA / TARA / etc.); BIA-XXX (if BCMS scope); applicable SOPs; management-review records.

## 12. Revision history

| Version | Date | Author | Changes |
|---|---|---|---|
| 1.0 | YYYY-MM-DD | [Name] | Initial release. |
