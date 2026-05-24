---
document_id: ROR-XXX
title: "[Organization / Scope] — Risk and Opportunity Register"
version: "1.0"
effective_date: YYYY-MM-DD
owner: "[Quality Director / Risk Manager]"
status: draft
approved_by: "[Top Management — risk register reviewed at management review per §9.3]"
approval_date: YYYY-MM-DD
review_cadence: "Quarterly + on material change in context / interested parties / processes / regulatory framework"
---

# ROR-XXX: Risk and Opportunity Register

Per ISO 9001:2015 §6.1 + the equivalent §6.1 in **every** Annex-SL management-system standard (ISO 13485 §6.1, AS9100D §6.1, IATF 16949 §6.1, ICH Q10 (informed by ICH Q9), ISO 22000 §6.1, ISO 27001 §6.1, ISO 14001 §6.1, ISO 45001 §6.1, ISO 50001 §6.1, ISO 37001 §6.1, ISO 22301 §6.1, ISO/IEC 42001 §6.1).

"Risk-based thinking" is the cross-cutting Annex SL discipline. This register is the documented evidence of the organization's risk-and-opportunity determination + planning + action + effectiveness evaluation. It is a LIVING document — updated quarterly minimum + on material change triggers.

This register sits ALONGSIDE domain-specific risk artifacts (medical-devices Risk Management File per ISO 14971; automotive HARA per ISO 26262; ATMP Donor Eligibility per 21 CFR 1271; etc.). The ROR captures QMS-level + management-system-level risk; the domain-specific artifacts capture product/process-level safety + regulatory risk.

## 1. Scope + methodology

- **Scope:** [QMS scope per QM-XXX §4.3]
- **Risk-assessment methodology:** [qualitative L × C matrix / quantitative / FMEA-derived / scenario analysis / hybrid]
- **Likelihood scale:** [e.g., 1=Rare to 5=Almost Certain — describe]
- **Consequence scale:** [e.g., 1=Insignificant to 5=Catastrophic — describe by impact axis: quality / safety / financial / reputational / regulatory]
- **Risk-rating matrix:** [L × C → Low/Medium/High/Critical]
- **Acceptability criterion:** [risk level above which treatment is required]
- **Opportunity-rating approach:** [value × ease of implementation × strategic alignment, or similar]
- **Review cadence:** quarterly + on context/IP/process/regulatory change

## 2. Risk register

| Risk # | Risk description | Source (process # from PROCESS-MAP / external) | Likelihood (L) | Consequence (C) | Inherent risk | Existing controls | Residual risk | Treatment decision | Owner | Due date | Effectiveness check |
|---|---|---|---|---|---|---|---|---|---|---|---|
| R-01 | Supplier consolidation in single-source component creates supply continuity risk | REAL-01 (procurement) | 3 | 4 | High | Approved Supplier List with alternate-supplier identification; 30-day safety stock | Medium | Treat (qualify second source by Q2) | Procurement | YYYY-MM-DD | Annual review of safety-stock + alternate-source readiness |
| R-02 | Regulatory change (new EU regulation) requires QMS update | MGT-05 (risk + opportunity) | 4 | 3 | High | Regulatory monitoring program; quarterly horizon scan | Medium | Treat (gap analysis Q1) | Quality Director | YYYY-MM-DD | Post-implementation audit |
| R-03 | Key-person dependency in [specific role] | SUP-01 (people) | 3 | 4 | High | Documented procedures; partial cross-training | Medium-High | Treat (formal succession plan + cross-train backup) | HR | YYYY-MM-DD | Backup-coverage drill |
| R-04 | Cybersecurity incident affecting GxP IT systems | Cross-cutting (iso-27001 + iso-22301) | 3 | 5 | Critical | ISMS controls per Annex A; incident response plan; backups | Medium | Reduce (additional MFA + EDR rollout) | IT | YYYY-MM-DD | Tabletop exercise + KPIs |

**Treatment decision categories:**

- **Avoid** — eliminate the risk (e.g., discontinue activity)
- **Reduce** — implement additional controls (most common)
- **Share** — transfer to third party (insurance; contractor; supplier)
- **Retain** — accept the residual risk (must be approved at appropriate level)

## 3. Opportunity register

| Opp # | Opportunity description | Source | Value | Ease | Strategic fit | Decision | Owner | Due date | Realization check |
|---|---|---|---|---|---|---|---|---|---|
| O-01 | Adopt FSSC 22000 to qualify for higher-margin GFSI-required customer | Customer dialog | High | Medium | High | Pursue Q3 | Quality Director | | Customer-share gain |
| O-02 | Apply ML-driven predictive maintenance to reduce unplanned downtime | Engineering | Medium | Medium | Medium | Pilot Q2 | Engineering | | OEE improvement |

## 4. Linkage to product/process-level risk artifacts

Risks identified here that have product/process safety implications are cross-referenced to domain-specific risk artifacts:

| Risk # | Linked artifact | Reason |
|---|---|---|
| R-04 | TARA-XXX (cybersecurity) + RMF-XXX (medical-device risk) + HARA-XXX (FuSa) as applicable | Cyber incident may affect product safety; coordinated risk reduction across artifacts |

## 5. Aggregate risk dashboard

Quarterly snapshot for management review:

| Tier | Count | % of total | Trend (vs. last quarter) |
|---|---|---|---|
| Critical | | | |
| High | | | |
| Medium | | | |
| Low | | | |

Critical + High risks reviewed individually at management review per §9.3.

## 6. Effectiveness evaluation (§6.1.2)

The organization evaluates the effectiveness of risk treatments:

| Risk # | Treatment | Implementation date | Effectiveness check method | Result | Action |
|---|---|---|---|---|---|

Ineffective treatments trigger CAPA per [CAPA workflow].

## 7. Review cadence

- **Quarterly:** full register review + new-risk identification + opportunity-pipeline review
- **At management review (annual minimum):** aggregate dashboard + critical/high risks + treatment-effectiveness trends
- **On trigger:** material change in context (§4.1); new interested party + needs (§4.2); new process + change (§4.4); regulatory change; significant incident; audit finding

## 8. Sign-off

| Role | Name | Date | Signature |
|---|---|---|---|
| Quality Director / Risk Manager | | | |
| Top Management (annual at management review) | | | |
| (Process / function owners for risks they own) | | | |

## 9. References

- ISO 9001:2015 §6.1 — Actions to address risks and opportunities (and equivalent §6.1 in every Annex-SL management-system standard listed above).
- ISO 31000:2018 — Risk management guidelines (broader risk-management framework; informs methodology).
- ICH Q9(R1) — Quality Risk Management (pharma — informs methodology for pharma adopters).
- Linked: QM-XXX (Quality Manual); PROCESS-MAP-XXX (process inventory feeding §2 risk sources); RISK-ASSESSMENT-XXX (standalone risk assessments for major scope changes); RMF-XXX / HARA-XXX / TARA-XXX (domain-specific risk artifacts cross-referenced in §4); management-review records.

## 10. Revision history

| Version | Date | Author | Changes |
|---|---|---|---|
| 1.0 | YYYY-MM-DD | [Name] | Initial release. |
