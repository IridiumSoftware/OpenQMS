---
document_id: BCP-XXX
title: "[Organization / Site / Service Scope] — Business Continuity Plan"
version: "1.0"
effective_date: YYYY-MM-DD
owner: "[Business Continuity Manager / BCMS Lead, Title]"
status: draft
approved_by: "[Top Management + Crisis Management Team Lead]"
approval_date: YYYY-MM-DD
exercise_cadence: "Tabletop minimum annually + live exercise minimum every 2 years + full activation post-incident review"
---

# BCP-XXX: Business Continuity Plan

Per ISO 22301:2019 §8.4 (Business continuity strategies and solutions) + §8.5 (Business continuity plans and procedures). The Business Continuity Plan (BCP) is the documented response to disruptive incidents — how the organization will continue delivering products + services at acceptable predefined levels following disruption.

This plan is informed by:
- The **Business Impact Analysis (BIA)** per ISO 22301 §8.2.2 which identified prioritized activities + their Maximum Acceptable Outage (MAO) / Recovery Time Objectives (RTO) / Recovery Point Objectives (RPO).
- The **Risk Assessment** per ISO 22301 §8.2.3 which identified relevant disruption scenarios.
- The **Continuity Strategies + Solutions** per §8.4 selected to meet the RTO/RPO targets.

## 1. Scope

- **Organization / site / service covered:** [name]
- **Linked BIA:** BIA-XXX
- **Linked Risk Assessment:** RA-XXX
- **Linked BCMS Policy:** ABMS-POL-XXX
- **Prioritized activities in scope:** [enumerated]
- **Out of scope:** [explicit — e.g., R&D activities not subject to BC; non-prioritized administrative functions]

## 2. Recovery objectives summary (from BIA)

| Activity / Product / Service | Maximum Acceptable Outage (MAO) | Recovery Time Objective (RTO) | Recovery Point Objective (RPO) | Minimum Business Continuity Objective (MBCO) |
|---|---|---|---|---|

**Definitions:**
- **MAO** — point beyond which the organization's viability would be irrevocably threatened if product/service delivery cannot be resumed.
- **RTO** — period of time within which the prioritized activities + their dependencies must be resumed after a disruption.
- **RPO** — point in time to which data must be recovered after a disruption.
- **MBCO** — minimum level of products/services that is acceptable to the organization to achieve its business objectives during a disruption.

## 3. Disruption scenarios planned for

Per the Risk Assessment:

| Scenario | Likelihood | Impact category | Primary impact | Plan section addressing |
|---|---|---|---|---|
| Loss of primary site | | | Facility | §5.1 |
| Loss of key supplier | | | Supply chain | §5.2 |
| Cyber attack — ransomware / data exfiltration | | | IT systems + data | §5.3 |
| Loss of key personnel (concentrated knowledge) | | | People | §5.4 |
| Utility outage (power / network / water) | | | Infrastructure | §5.5 |
| Public-health event (pandemic / outbreak) | | | People + facility | §5.6 |
| Natural disaster (earthquake / flood / fire / storm) | | | Facility + people | §5.7 |
| Transportation disruption | | | Logistics | §5.8 |

## 4. Crisis management team (CMT)

| Role | Primary | Backup | 24/7 contact | Authority |
|---|---|---|---|---|
| CMT Lead | | | | Activation decision; resource commitment; escalation to top management |
| BCMS Manager | | | | Plan execution coordination |
| IT / Cybersecurity Lead | | | | IT recovery; cyber incident response |
| Operations Lead | | | | Production continuity |
| Communications Lead | | | | Internal + external communications |
| HR Lead | | | | People-related response; family contact |
| Legal Counsel | | | | Regulatory + customer-contract obligations during disruption |
| Finance Lead | | | | Emergency expenditure authorization |
| Security Lead | | | | Physical security; access management |
| External-relations Lead | | | | Customer + regulator + media interface |

## 5. Response procedures per scenario

### 5.1 Loss of primary site

- **Detection + activation trigger:** [criteria for invoking this section]
- **Immediate actions (Hour 0-1):** evacuation per emergency plan; head count; CMT activation; situation assessment
- **Short-term actions (Hour 1-24):** activation of alternate site; relocation of critical personnel; redirection of inbound shipments + customers
- **Recovery actions (Day 1-30):** restoration of operations to MBCO level; recovery to RTO; communication cadence
- **Linked resources:** alternate site contract reference; relocation plan; alternate-supplier contacts

### 5.2 Loss of key supplier

- **Pre-arranged alternate suppliers per Approved Supplier List:** [reference]
- **Inventory buffer policy:** [N days of safety stock per critical material]
- **Activation procedure:** [authorization; communication; logistics]
- **Single-source-of-supply mitigation status:** [enumerated for any material where no alternate exists]

### 5.3 Cyber attack

- **Incident response team activation:** cross-reference with information-security incident-response procedure
- **Containment:** network segmentation + system isolation + endpoint quarantine
- **Communication:** customer notification per data-breach obligations + regulatory notification per GDPR Article 33 + state breach-notification laws + sector-specific reporting (HIPAA + SEC + DORA + etc.)
- **Recovery:** restore from clean backups per IT DR procedure; rebuild affected systems; restore data to RPO
- **Forensic preservation:** preserve evidence per legal-hold protocol
- **Linked:** information-security incident response procedure + IT DR plan + cyber insurance contact

### 5.4 Loss of key personnel

- **Critical-role + critical-knowledge inventory:** [reference]
- **Succession plans for critical roles:** [reference]
- **Knowledge-management practices reducing concentration:** documented procedures + cross-training + paired-working
- **Activation actions:** designated backup activation + accelerated recruiting if backup not viable + external interim staffing

### 5.5 Utility outage

- **Critical utilities + their continuity provisions:** power (UPS + generator + fuel-supply contract); network (redundant ISPs + cellular failover); water (storage); gas; steam
- **Utility failure-mode response:** [per utility]
- **Maximum tolerable utility outage before MAO breach:** [per activity]

### 5.6 Public-health event

- **Pandemic preparedness plan:** [reference if separate]
- **Remote-work capability for prioritized activities:** [enumerated]
- **Onsite-essential-only protocols + PPE + screening:** [reference]
- **Supply-chain resilience under multi-region restrictions:** [reference]

### 5.7 Natural disaster

- **Hazard-specific responses per local hazard profile:** [reference local emergency plan]
- **Evacuation + shelter-in-place + assembly procedures:** [reference]
- **Salvage + damage-assessment procedures:** [reference]
- **Insurance coordination:** [reference]

### 5.8 Transportation disruption

- **Alternate logistics providers:** [reference]
- **Inventory positioning policy enabling continuity through transport disruption:** [reference]

## 6. Internal + external communications

| Audience | Channel | Frequency during incident | Owner | Pre-approved holding statement |
|---|---|---|---|---|
| Employees | Email + SMS + intranet + town hall | Hourly initially → daily | HR + Communications | |
| Customers | Direct contact + portal + status page | Hourly initially → daily | Customer Success + Sales | |
| Suppliers | Direct contact | As needed | Procurement | |
| Regulators | Per regulatory channel + within mandatory reporting window | Per requirement | Regulatory Affairs + Legal | |
| Insurers | Direct contact within policy notification window | Immediate + per policy | Finance + Legal | |
| Media + public | Press release + spokesperson | Coordinated; minimum daily during active incident | Communications | |
| Investors / shareholders | Per material-information disclosure rules | Per regulation | CFO + IR | |

## 7. Resource requirements

| Resource | Source | Activation lead time |
|---|---|---|
| Alternate site | Pre-contracted | |
| Backup IT systems | DR site | |
| Backup data | Backup retention per RPO | |
| Emergency funding | Treasury reserve | |
| External recovery providers (forensics, restoration, transport) | Pre-contracted | |
| Insurance | Per active policy | |

## 8. Plan exercise + testing

| Exercise type | Cadence | Last exercised | Next scheduled | Lessons-learned register |
|---|---|---|---|---|
| Tabletop walkthrough | Annual | | | |
| Communications cascade test | Annual | | | |
| IT DR test (failover + recovery) | Annual | | | |
| Live activation exercise (single scenario, end-to-end) | Biennial | | | |
| Post-incident review (when actual disruption occurs) | After every activation | | | |

## 9. Maintenance + review

- **Review triggers:** annually + on organization change + on incident learning + on regulator request + on technology change + on supplier change
- **Last reviewed:** [YYYY-MM-DD]
- **Next scheduled review:** [YYYY-MM-DD]
- **Change log:** maintained in §11 revision history

## 10. Sign-off

| Role | Name | Date | Signature |
|---|---|---|---|
| Business Continuity Manager | | | |
| CMT Lead | | | |
| IT / Cybersecurity Lead | | | |
| Operations Lead | | | |
| HR Lead | | | |
| Legal Counsel | | | |
| Top Management representative | | | |

## 11. References

- ISO 22301:2019 §8.2.2 — Business impact analysis.
- ISO 22301:2019 §8.2.3 — Risk assessment.
- ISO 22301:2019 §8.4 — Business continuity strategies and solutions.
- ISO 22301:2019 §8.5 — Business continuity plans and procedures.
- ISO 22301:2019 §8.6 — Exercise programme.
- ISO 22301:2019 §9.1 — Monitoring, measurement, analysis and evaluation.
- ISO/TS 22317 — Business impact analysis guidance.
- ISO/TS 22318 — Supply chain continuity guidance.
- ISO/TS 22330 — People aspects of business continuity.
- ISO/TS 22331 — Strategy guidance for business continuity.
- Linked: BIA-XXX (Business Impact Analysis), RA-XXX (Risk Assessment), incident-response procedures (cyber + physical + people), IT DR plan, communication-cascade SOP, exercise records.

## 12. Revision history

| Version | Date | Author | Changes |
|---|---|---|---|
| 1.0 | YYYY-MM-DD | [Name] | Initial release. |
