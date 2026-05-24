---
document_id: IT-DR-XXX
title: "[Organization / IT Scope] — IT Disaster Recovery Plan"
version: "1.0"
effective_date: YYYY-MM-DD
owner: "[IT Director / DR Coordinator]"
status: draft
approved_by: "[CIO + Business Continuity Manager + Top Management]"
approval_date: YYYY-MM-DD
test_cadence: "Tabletop minimum annually + technical failover test minimum annually + full DR test minimum biennially"
---

# IT-DR-XXX: IT Disaster Recovery Plan

The IT-specific subset of the broader Business Continuity Plan (BCMS-PLAN-XXX). Covers the recovery of IT systems + data + services in response to a disruption — distinct from BCMS in that IT DR is technology-focused (failover, restoration, backup-recovery) while BCMS is business-process-focused.

Aligned with the BCMS BIA (BIA-XXX §7 ICT section) which establishes the per-system RTO + RPO that this plan must meet.

## 1. Scope

- **IT systems in scope:** [enumerated — typically: ERP / MES / LIMS / EBR / CRM / financial / email + collaboration / authentication / network / cloud services / specialty manufacturing software / etc.]
- **Out of scope:** [enumerated]
- **Linked BCMS Plan:** BCMS-PLAN-XXX
- **Linked BIA:** BIA-XXX (provides per-system RTO + RPO targets)

## 2. System inventory + recovery objectives

| System # | System | Function | Business owner | IT owner | Criticality | RTO (from BIA) | RPO (from BIA) | Recovery method (failover / restore / rebuild) |
|---|---|---|---|---|---|---|---|---|

## 3. DR site + infrastructure architecture

### 3.1 Primary site

- **Location:** [address]
- **Critical infrastructure:** [data center; on-prem servers; network; storage; UPS + generator capacity]
- **Hosting model:** [on-prem / colocation / IaaS / SaaS]

### 3.2 DR site / failover capability

- **DR site location:** [address — typically geographically separated from primary by sufficient distance to avoid same regional disruption]
- **DR architecture:** [hot site / warm site / cold site / cloud-based DRaaS / multi-region active-active]
- **Activation time:** [for each architecture type — hot is minutes; warm is hours; cold is days]
- **Network connectivity:** [primary + secondary paths; bandwidth; latency]
- **Personnel + access:** [who can access DR site + how; 24/7 access procedures]

### 3.3 Cloud + SaaS considerations

For cloud-hosted + SaaS systems:

| System | Provider | Provider's RTO/RPO commitment (SLA) | Customer-side configuration for DR | Multi-region failover available? | Customer-controlled backups (yes/no/escrow) |
|---|---|---|---|---|---|

## 4. Backup strategy

### 4.1 Backup inventory

| System | Data type | Backup frequency | Backup type (full / incremental / differential) | Retention | Off-site copy (where) | Encryption | Last verified-restore date |
|---|---|---|---|---|---|---|---|

### 4.2 3-2-1 rule + air-gap

Per standard backup practice:
- **3** copies of data
- **2** different media types
- **1** off-site (and ideally air-gapped to defeat ransomware)

Current state per system:

| System | Meets 3-2-1? | Air-gapped backup? | Ransomware-recovery-tested? |
|---|---|---|---|

### 4.3 Restore testing

| System | Restore-test cadence | Last restore-test date | Restore-test result | Restore-time observed | Within RTO? |
|---|---|---|---|---|---|

## 5. Recovery procedures (per system)

For each in-scope system, the step-by-step recovery procedure:

### System: [name]

- **Recovery prerequisite:** [infrastructure + access + people that must be available before recovery can begin]
- **Recovery sequence:**
  1. [Step 1 with owner + estimated time]
  2. [Step 2 ...]
  3. [Step N — verification + handoff to business owner]
- **Verification criteria:** [how to confirm successful recovery]
- **Rollback criteria:** [conditions under which to abort + fallback]
- **Communication during recovery:** [who is notified at which milestones]
- **Estimated total recovery time:** [hours] (target: ≤ RTO)

## 6. Disruption scenarios + IT response

### 6.1 Single-system outage (e.g., one critical application server fails)

- Activation: monitoring alert → on-call IT engineer → severity assessment
- Response: standard incident response per IT runbook
- Recovery: per system-specific procedure in §5

### 6.2 Data center / primary site loss

- Activation: site unavailable (fire / flood / extended power loss / network loss)
- Response: full DR site activation
- Recovery: per §3.2 DR architecture sequence + §5 per-system procedures
- Communication: IT-wide + executive + customer-facing (per BCMS-PLAN comms matrix)

### 6.3 Cyber attack (ransomware / data exfiltration / destructive malware)

- Activation: cybersecurity incident response per [iso-27001 incident response procedure]
- Response: containment + isolation + forensic preservation
- Recovery: restore from CLEAN backups (verified pre-encryption); rebuild affected systems from scratch where contamination uncertain
- Special considerations: do NOT pay ransom (per organization policy); preserve evidence; regulator + insurance + law-enforcement notification
- Linked: cybersecurity incident response procedure; cyber insurance policy; legal-hold protocol

### 6.4 Cloud provider outage

- Activation: cloud provider service-status notification
- Response: cloud-specific failover (multi-region failover if available)
- Recovery: monitor provider's recovery; if provider RTO exceeds business RTO, invoke business-side workarounds per BCMS-PLAN

### 6.5 Insider threat / privileged-access abuse

- Activation: anomaly detection + investigation
- Response: account suspension + forensic preservation
- Recovery: data + system integrity verification; restore from pre-incident state if integrity compromised

## 7. Communication during DR

| Audience | Channel | Frequency | Owner |
|---|---|---|---|
| IT team | Slack + bridge + war-room | Continuous | DR Coordinator |
| Business owners | Email + phone + dashboard | Hourly initially → daily | DR Coordinator |
| Executive | Email + phone | Per significant milestone | CIO |
| Customers (external-facing services) | Status page + direct contact + portal | Hourly initially → daily | Customer Success |
| Regulators (if reporting obligation) | Per regulatory channel | Per requirement | Compliance |
| Cyber insurance | Phone within policy window | Immediate + per policy | Finance + Legal |

## 8. Plan exercise + testing

| Exercise type | Cadence | Last exercised | Next scheduled | Lessons-learned register |
|---|---|---|---|---|
| Tabletop walkthrough | Annual | | | |
| Communications cascade test | Annual | | | |
| Single-system failover test | Per system, annually | | | |
| Full DR site failover (live) | Biennial minimum | | | |
| Ransomware-recovery exercise (restore-from-clean-backup verified) | Annual | | | |
| Cloud-failover test (per cloud system) | Annual | | | |

## 9. Maintenance + review

Triggers for re-review beyond scheduled annual:
- IT architecture change (new system added / system retired / migration to cloud)
- Material change to BIA RTO/RPO targets
- New regulatory IT-availability requirement (DORA for EU financial services; HIPAA; etc.)
- Cyber attack or near-miss
- DR exercise lessons-learned

## 10. Sign-off

| Role | Name | Date | Signature |
|---|---|---|---|
| IT Director / DR Coordinator | | | |
| Cybersecurity Lead | | | |
| Business Continuity Manager | | | |
| CIO | | | |
| Top Management representative | | | |

## 11. References

- ISO 22301:2019 §8.4 + §8.5 — BC strategies + plans (IT DR is the IT subset).
- ISO/IEC 27031:2011 — Guidelines for information and communication technology readiness for business continuity.
- NIST SP 800-34 Rev. 1 — Contingency Planning Guide for Federal Information Systems.
- ISO/IEC 27001:2022 Annex A.5.29 + A.5.30 — ICT readiness for business continuity (where iso-27001 in scope).
- Linked: BCMS-PLAN-XXX (broader BC plan), BIA-XXX (provides RTO/RPO targets), iso-27001 ISMS controls + incident response procedure, cyber insurance policy.

## 12. Revision history

| Version | Date | Author | Changes |
|---|---|---|---|
| 1.0 | YYYY-MM-DD | [Name] | Initial release. |
