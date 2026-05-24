---
document_id: PROCESS-MAP-XXX
title: "[Organization / Site Scope] — QMS Process Map"
version: "1.0"
effective_date: YYYY-MM-DD
owner: "[Quality Director]"
status: draft
approved_by: "[Top Management — Quality Director + each process owner per §3]"
approval_date: YYYY-MM-DD
review_cadence: "Annually + on material organizational/process change"
---

# PROCESS-MAP-XXX: QMS Process Map

Per ISO 9001:2015 §4.4 — "The organization shall determine the processes needed for the quality management system + their application throughout the organization, and shall: determine the inputs required and the outputs expected from these processes; determine the sequence and interaction of these processes; determine and apply the criteria and methods, including monitoring, measurements and related performance indicators, needed to ensure the effective operation and control of these processes; determine the resources needed for these processes and ensure their availability; assign the responsibilities and authorities for these processes; address the risks and opportunities as determined in 6.1; evaluate these processes and implement any changes needed to ensure that these processes achieve their intended results; improve the processes and the quality management system."

This document is the master process inventory + interaction map. Companion to QM-XXX Quality Manual §4.4.

## 1. Process inventory

Per ISO 9001:2015 §4.4 the organization documents each QMS process. Process categories (typical 4-category model):

### Management processes

| Process # | Process | Owner | Purpose | Inputs | Outputs | Linked SOP |
|---|---|---|---|---|---|---|
| MGT-01 | Strategic planning + objectives | Top Management | Set + cascade quality objectives | Context analysis; interested-party needs | Quality objectives; QM updates | |
| MGT-02 | Management review | Top Management | Periodic QMS effectiveness review | Audit results + KPI dashboards + complaint trends + supplier performance + risk + improvement opportunities | Decisions + actions + resource commitments | MANAGEMENT-REVIEW SOP |
| MGT-03 | Internal audit program | Quality Director | Verify QMS conformance + effectiveness | Audit plan + risk-prioritization | Audit reports + nonconformities + CAPA | AUDIT-PROCEDURE SOP |
| MGT-04 | Continual improvement | Quality Director | Drive performance improvement | Trends + customer feedback + audit findings + risk register | Improvement projects + CAPA | |
| MGT-05 | Risk + opportunity management | Quality Director | Identify + manage QMS-relevant risks + opportunities | Context + interested parties + processes | RISK-AND-OPPORTUNITY-REGISTER | |
| MGT-06 | Change management | Quality Director | Control QMS changes | Change requests | Approved changes + training + validation | CHANGE-CONTROL SOP |

### Customer-facing processes

| Process # | Process | Owner | Purpose | Inputs | Outputs | Linked SOP |
|---|---|---|---|---|---|---|
| CUST-01 | Requirements determination | Sales + Engineering | Capture + clarify customer requirements | RFP/RFQ; customer dialog | Specifications; contracts | |
| CUST-02 | Design + development | Engineering | Translate requirements into product/service design | Specifications; design inputs | Design outputs; verification; validation | Per vertical (DHF / TCC / etc.) |
| CUST-03 | Customer satisfaction monitoring | Quality | Measure + respond to customer perception | Surveys; complaint data; warranty data | Improvement actions; trends | |
| CUST-04 | Complaint handling | Quality | Receive + investigate + respond to complaints | Customer complaints; field reports | Investigations; corrective actions; customer responses | Complaint workflow + issue template |

### Realization processes

| Process # | Process | Owner | Purpose | Inputs | Outputs | Linked SOP |
|---|---|---|---|---|---|---|
| REAL-01 | Procurement + supplier control | Procurement | Select + qualify + monitor suppliers | Purchase requirements; supplier evaluations | Approved Supplier List; PO; received conforming product | Supplier qualification SOP |
| REAL-02 | Production / service delivery | Operations | Execute production / service delivery per specifications | Approved design; resources; instructions | Conforming product / service | Per vertical (MBR / control plan / etc.) |
| REAL-03 | In-process + final inspection | Quality | Verify product/service conformity | Acceptance criteria; sampling plans | Conformity records; rejection records | |
| REAL-04 | Identification + traceability | Operations | Maintain product identity + lot/batch traceability | Production records | Traceability records | |
| REAL-05 | Nonconforming output control | Quality | Segregate + disposition nonconforming product | NCR triggers | Disposition decisions + corrective actions | NCR issue template |
| REAL-06 | Post-delivery activities | Operations + Service | Support customer post-delivery (warranty, service, recall) | Customer requests; field reports; recall triggers | Service records; recall execution | Recall procedure (where applicable) |

### Support processes

| Process # | Process | Owner | Purpose | Inputs | Outputs | Linked SOP |
|---|---|---|---|---|---|---|
| SUP-01 | People + competence | HR + Training | Recruit + train + maintain competence | Role requirements; gap analysis | Trained personnel; training records | Training SOP |
| SUP-02 | Infrastructure management | Facilities + Engineering | Maintain physical + IT infrastructure | Capacity requirements; reliability targets | Maintained equipment + facilities | Maintenance SOP |
| SUP-03 | Work environment | Facilities + EHS | Maintain suitable work environment | Process requirements; EHS requirements | Conforming environment | EHS SOPs |
| SUP-04 | Monitoring + measuring resource control | Metrology | Calibrate + maintain M+M equipment | Equipment inventory; calibration cycles | Calibrated equipment; calibration records | Calibration SOP |
| SUP-05 | Documented information control | Quality | Control creation + change + access + retention of QMS docs | Doc creation/revision requests | Controlled documents | Document control SOP |
| SUP-06 | Knowledge management | Quality + relevant teams | Maintain organizational knowledge | Lessons learned; expertise inventory | Knowledge artifacts | |

## 2. Process sequence + interaction diagram

[Insert process-interaction diagram. Typical formats: turtle diagrams per process; SIPOC; high-level interaction map showing arrows between processes. Format choice per organization preference; diagram is required, not its format.]

## 3. Process performance indicators (KPIs)

For each process, the organization documents performance indicators. Examples:

| Process # | KPI | Target | Frequency | Owner | Reporting |
|---|---|---|---|---|---|
| CUST-03 | Customer satisfaction NPS / CSAT | ≥ 8/10 | Quarterly | Quality | Mgmt review |
| CUST-04 | Complaint response time | ≤ 5 business days | Monthly | Quality | Dashboard |
| REAL-01 | Supplier on-time delivery | ≥ 95% | Monthly | Procurement | Dashboard |
| REAL-03 | First-time-yield | ≥ 99% | Weekly | Production | Floor dashboard |
| REAL-05 | NCR rate per kU | ≤ 100 ppm | Weekly | Quality | Floor dashboard |
| SUP-01 | Training-completion rate (assigned vs. completed within due date) | ≥ 95% | Monthly | HR | Dashboard |

## 4. Process risks + opportunities

Cross-reference to RISK-AND-OPPORTUNITY-REGISTER-XXX per ISO 9001 §6.1. Each process row in §1 has corresponding risk + opportunity entries in the register.

## 5. Outsourced processes

Per ISO 9001:2015 §8.4 — where the organization outsources any process, control over it is determined + applied. Outsourced processes:

| Process # | Outsourced to | Control mechanism | Verification |
|---|---|---|---|
| | (e.g., sterilization service) | Supplier qualification + audit + per-batch CoC | Incoming verification |

## 6. Process change history

| Date | Process # | Change | Approver | Linked CC# |
|---|---|---|---|---|

## 7. Sign-off

| Role | Name | Date | Signature |
|---|---|---|---|
| Quality Director | | | |
| Top Management | | | |
| (Each process owner from §1) | | | |

## 8. References

- ISO 9001:2015 §4.4 — Quality management system and its processes.
- ISO 9001:2015 §6.1 — Actions to address risks and opportunities.
- ISO 9001:2015 §8.4 — Control of externally provided processes, products and services.
- Per applicable vertical equivalent §4.4 (ISO 13485, AS9100D, IATF 16949, ICH Q10, ISO 22000).
- Linked: QM-XXX (Quality Manual), RISK-AND-OPPORTUNITY-REGISTER-XXX, individual SOPs per process.

## 9. Revision history

| Version | Date | Author | Changes |
|---|---|---|---|
| 1.0 | YYYY-MM-DD | [Name] | Initial release. |
