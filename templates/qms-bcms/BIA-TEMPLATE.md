---
document_id: BIA-XXX
title: "[Organization / Site / Service Scope] — Business Impact Analysis"
version: "1.0"
effective_date: YYYY-MM-DD
owner: "[Business Continuity Manager]"
status: draft
approved_by: "[Top Management + BCMS Lead]"
approval_date: YYYY-MM-DD
review_cadence: "Annually + on material organizational/service/dependency change"
---

# BIA-XXX: Business Impact Analysis

Per ISO 22301:2019 §8.2.2 + ISO/TS 22317. The BIA is the analytical foundation of the BCMS: it identifies the organization's prioritized activities, the impacts of their disruption over time, the resources they depend on, and the timeframes for resumption. The BIA outputs (MAO / RTO / RPO / MBCO per activity) drive the selection of business-continuity strategies + solutions (§8.4) and the content of business-continuity plans (§8.5).

The BIA is methodology-driven + repeatable — re-performed at least annually + on material change.

## 1. Scope

- **Organizational scope:** [sites / business units / services in scope]
- **Out of scope:** [explicit — e.g., R&D activities; non-prioritized administrative functions]
- **Linked BCMS Policy:** BCMS-POL-XXX
- **Linked Risk Assessment:** RA-XXX (BCMS scenario assessment per §8.2.3)

## 2. Activity inventory + criticality

Every activity within scope is enumerated + assessed for criticality. Criticality determines whether the activity is "prioritized" (warranting BC strategies + plans) or "non-prioritized" (acceptable to suspend during disruption).

| Activity # | Activity | Product / service supported | Owner | Function | Customer impact if disrupted | Regulatory impact if disrupted | Financial impact if disrupted | Prioritized? (Y/N) |
|---|---|---|---|---|---|---|---|---|

## 3. Impact-over-time analysis (per prioritized activity)

For each prioritized activity, the BIA assesses how impact escalates over time:

| Activity # | 0-4 hours | 4-24 hours | 24-72 hours | 3-7 days | 7-30 days | > 30 days |
|---|---|---|---|---|---|---|

Impact categories evaluated per time bucket: customer impact (lost revenue + contractual penalty + customer attrition); regulatory impact (notification obligations + enforcement risk); financial impact (revenue loss + cost of recovery + insurance); reputational impact; safety impact (where applicable — particularly for healthcare / pharma / critical infrastructure); employee impact; supply-chain ripple impact.

## 4. Maximum Acceptable Outage (MAO) determination

The MAO is the point beyond which the organization's viability would be irrevocably threatened if product/service delivery cannot be resumed. Above MAO, the activity is considered non-recoverable — the organization itself fails or is permanently impaired.

| Activity # | MAO | Justification |
|---|---|---|

## 5. Recovery Time Objective (RTO) + Recovery Point Objective (RPO)

| Activity # | RTO (target resumption time after disruption) | RPO (target data loss tolerance after disruption) | Rationale |
|---|---|---|---|

RTO must be ≤ MAO (typically with safety margin).

## 6. Minimum Business Continuity Objective (MBCO)

The MBCO is the minimum level of products/services acceptable to the organization to achieve its business objectives during a disruption — typically a degraded mode of operation that satisfies the most critical customer + regulatory + safety requirements.

| Activity # | MBCO | Description of degraded mode | Acceptable for how long |
|---|---|---|---|

## 7. Resource dependencies

For each prioritized activity, the resources it depends on are inventoried per ISO 22301 §8.4 resource categories:

### People

| Activity # | Critical roles | Headcount required at MBCO | Skills / certifications required | Single-point-of-failure individuals? |
|---|---|---|---|---|

### Information + Communication Technology (ICT)

| Activity # | Critical IT systems | Data dependencies | RPO per system | Recovery prerequisite |
|---|---|---|---|---|

### Infrastructure

| Activity # | Facilities | Equipment | Utilities (power / network / water / gas / steam) | Specialized environment (cleanroom / cold-chain / hazmat / SCIF) |
|---|---|---|---|---|

### Supplies

| Activity # | Critical materials / components / consumables | Single-source? | Safety stock (days at MBCO) |
|---|---|---|---|

### Partners + suppliers

| Activity # | Critical external dependencies | Alternates available? | Contractual continuity provisions |
|---|---|---|---|

### Financial resources

| Activity # | Working capital requirement at MBCO | Treasury reserve / credit line | Insurance coverage |
|---|---|---|---|

## 8. Inter-activity dependencies

Activities often depend on each other. The BIA documents these dependency chains:

| Activity # | Depends on (upstream activities) | Depended on by (downstream activities) | Cascading impact if disrupted |
|---|---|---|---|

## 9. Aggregation: prioritized-activity recovery schedule

The combined view: which prioritized activities resume in what order, with which resources, by when:

| Recovery hour | Activity # | Resources required by this point | Cumulative resource demand |
|---|---|---|---|

## 10. Methodology + assumptions

- **Method:** [described — interview-based / workshop-based / survey-based / hybrid]
- **Information sources:** [stakeholder interviews; financial records; SLAs; historical incident data]
- **Assumptions:** [explicitly enumerated; affects validity of MAO/RTO/RPO determinations]
- **Limitations:** [acknowledged]

## 11. Validation

The BIA outputs (MAO / RTO / RPO / MBCO + resource dependencies) are validated by:

- Workshop validation with activity owners
- Cross-check vs. historical incident data
- Sanity-check vs. customer contractual obligations + regulatory requirements
- Sanity-check vs. existing BC strategies + solutions (per §8.4)

## 12. Output to BCMS

The BIA outputs feed:

- **§8.4 BC strategies + solutions** — selected to meet RTO/RPO/MBCO targets
- **§8.5 BC plans + procedures** — BCMS-PLAN-XXX scenarios per disruption type
- **§8.6 exercise programme** — exercises validate BIA accuracy + recovery capability
- **§9.1 monitoring + measurement** — performance against MAO/RTO/RPO measured

## 13. Sign-off

| Role | Name | Date | Signature |
|---|---|---|---|
| Business Continuity Manager | | | |
| Activity owners (each) | | | |
| Top Management representative | | | |

## 14. References

- ISO 22301:2019 §8.2.2 — Business impact analysis.
- ISO/TS 22317:2021 — Guidelines for business impact analysis.
- ISO/TS 22330 — People aspects of business continuity.
- ISO/TS 22318 — Supply chain continuity guidance.
- Linked: BCMS-PLAN-XXX (BC plan informed by this BIA), RA-XXX (BCMS scenario risk assessment), IT-DR-PLAN-XXX (IT disaster recovery plan per ICT dependencies in §7), management-review records.

## 15. Revision history

| Version | Date | Author | Changes |
|---|---|---|---|
| 1.0 | YYYY-MM-DD | [Name] | Initial release. |
