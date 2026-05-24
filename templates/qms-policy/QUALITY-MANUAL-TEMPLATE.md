---
document_id: QM-XXX
title: "[Organization Name] — Quality Manual"
version: "1.0"
effective_date: YYYY-MM-DD
owner: "[Top Management — typically CEO or designated Quality Director]"
status: draft
approved_by: "[Top Management — signed by individual identified in §5.3]"
approval_date: YYYY-MM-DD
review_cadence: "Annually + on material change in scope / organization / QMS / regulatory framework"
applicable_standards: "[ISO 9001:2015 + any vertical: ISO 13485 / AS9100D / IATF 16949 / ICH Q10 / ISO 22000 — list those in scope]"
---

# QM-XXX: Quality Manual

Top-level documented information establishing the organization's Quality Management System. Per ISO 9001:2015 §4 + §5 (and equivalent §4 + §5 in ISO 13485, AS9100D, IATF 16949, ICH Q10, ISO 22000 — all Annex SL or Annex SL-aligned). ISO 9001:2015 dropped the explicit "quality manual" requirement that earlier editions had, but most adopters retain a quality manual as the navigable top-level document organizing the QMS for internal use + customer/regulator review.

The quality manual is the on-ramp document — it does not replicate every SOP; it points to them and defines the QMS architecture + scope + responsibilities.

## 1. Organization context (§4.1)

- **Organization legal name + DBA:** [name]
- **Headquarters + principal facility addresses:** [addresses]
- **Products + services covered by this QMS:** [enumerated]
- **Markets + jurisdictions:** [list]
- **Scope statement (per §4.3):** [explicit boundary — what's in + what's out]
- **External issues relevant to the QMS:** regulatory landscape, supply-chain risks, technology trends, market expectations, customer relationships
- **Internal issues relevant to the QMS:** organizational maturity, culture, knowledge base, available resources

## 2. Interested parties (§4.2)

| Interested party | Relevant needs + expectations | Compliance obligation? |
|---|---|---|
| Customers | Conforming product + service; on-time delivery; price; warranty | Contractual |
| Regulators (FDA / EU / others per scope) | Compliance with applicable regulations | Statutory |
| Employees | Safe workplace; competence development; fair treatment | Contractual + legal |
| Suppliers | Clear specifications; timely payment; collaborative relationship | Contractual |
| Investors / shareholders | Financial performance; risk management; ESG performance | Fiduciary |
| Communities | Environmental responsibility; ethical operation; local economic contribution | Reputational + legal |

## 3. QMS scope (§4.3)

[Explicit scope statement including: products/services in scope; sites covered; processes covered; processes outsourced (with the manufacturer remaining responsible for conformity per §8.4); any clauses determined NOT applicable with justification (per §4.3 — typically rare).]

## 4. QMS processes (§4.4 — see PROCESS-MAP-XXX for detail)

The organization has determined the processes needed for the QMS, their sequence + interaction, criteria + methods for effective operation + control, resources, responsibilities, risks + opportunities, monitoring + measurement, and improvement actions. The full process map is maintained at PROCESS-MAP-XXX. Summary categories:

- **Management processes:** strategy + leadership + management review + audit program + improvement
- **Customer-facing processes:** requirements determination + design + development + customer satisfaction
- **Realization processes:** procurement + production + service delivery + post-delivery
- **Support processes:** people + infrastructure + environment + documented information + competence

## 5. Leadership (§5)

### 5.1 Leadership + commitment

Top management demonstrates leadership + commitment by:
- Taking accountability for the QMS effectiveness
- Establishing this quality manual + the quality policy
- Ensuring integration of QMS requirements into business processes
- Promoting process + risk-based thinking
- Ensuring resources are available
- Communicating the importance of effective QMS + conforming to QMS requirements
- Ensuring the QMS achieves intended results
- Engaging + directing + supporting persons contributing to QMS effectiveness
- Promoting improvement
- Supporting other relevant management roles to demonstrate leadership in their areas

### 5.2 Quality policy (see QUALITY-POLICY-XXX)

The organization's quality policy is established at QUALITY-POLICY-XXX. Top management reviews it annually + on material change.

### 5.3 Organizational roles, responsibilities + authorities

| Role | Responsibility | Authority | Reports to |
|---|---|---|---|
| [Top Management individual] | Overall QMS effectiveness | Final QMS decisions | Board / Owner |
| Quality Director | QMS administration | QA process design + management review chair | Top Management |
| [Per applicable vertical] | (Pharma: QP per EU GMP Annex 16) (Aerospace: DER / CVE) (Auto: Functional Safety Manager) | | |
| Production Lead | Operational conformity | Production process control | Top Management |
| Engineering Lead | Design + development | Design changes per change control | Top Management |
| Procurement Lead | Supplier qualification | Approved Supplier List authority | Top Management |

## 6. Planning (§6)

### 6.1 Risk + opportunity (see RISK-AND-OPPORTUNITY-REGISTER-XXX)

The organization determines risks + opportunities to give assurance that the QMS achieves its intended results, prevents or reduces undesired effects, and achieves continual improvement. Risk-based thinking is the §6.1 core; the Risk-and-Opportunity Register at RISK-AND-OPPORTUNITY-REGISTER-XXX is the documented evidence.

### 6.2 Quality objectives

Quality objectives are established at relevant functions + levels, consistent with the quality policy, measurable, monitored, communicated, updated. Documented in [objectives register location — typically maintained per function in management-review records].

### 6.3 Planning of changes

When changes to the QMS are needed, they are planned + carried out in a controlled manner per the change-control SOP.

## 7. Support (§7)

### 7.1 Resources

People + infrastructure + environment + monitoring/measuring resources + organizational knowledge. Calibration discipline per [SOP reference]; competence per §7.2.

### 7.2 Competence

Competence determined per role; training + experience + records maintained.

### 7.3 Awareness

Personnel made aware of quality policy, relevant quality objectives, contribution to QMS effectiveness, implications of nonconformity.

### 7.4 Communication

Internal + external communications per [communication SOP].

### 7.5 Documented information

This quality manual is the top-level QMS document. The full documented-information hierarchy is per [document control SOP]:
- Level 1: Quality Manual (this document)
- Level 2: Procedures (SOPs) — process-level instructions
- Level 3: Work instructions — task-level
- Level 4: Forms + records — evidence

## 8. Operation (§8)

Operational planning + control + product realization processes. The operational details are in domain-specific SOPs + templates per [operational SOP index].

## 9. Performance evaluation (§9)

- **9.1 Monitoring + measurement** — per [monitoring SOP]
- **9.2 Internal audit** — per [audit SOP + AUDIT-PROCEDURE-TEMPLATE-XXX]
- **9.3 Management review** — per [management-review SOP + MANAGEMENT-REVIEW-TEMPLATE-XXX]; minimum annual cadence

## 10. Improvement (§10)

- **10.2 Nonconformity + corrective action** — per [CAPA SOP + .github/ISSUE_TEMPLATE/capa.yml]
- **10.3 Continual improvement** — per [improvement SOP]

## 11. Vertical-specific extensions (where applicable)

This section documents the extensions to the ISO 9001 baseline imposed by the vertical(s) in scope:

| Vertical | Standard | Key additions | Linked SOPs |
|---|---|---|---|
| (If medical-devices) | ISO 13485:2016 + 21 CFR 820 + EU MDR | Design History File; Risk Management File per ISO 14971; Software Lifecycle per IEC 62304 | DHF-XXX, RMF-XXX, etc. |
| (If aerospace) | AS9100D + 14 CFR Part 21 + EASA Part 21 | Type Certificate Pack; Configuration Management; First Article Inspection | TCC-XXX, FAI-XXX |
| (If automotive) | IATF 16949 + ISO 26262 + ISO/SAE 21434 | Special Characteristics; HARA-driven Safety Plan; TARA-driven Cybersecurity Plan; PPAP | HARA-XXX, TARA-XXX, PPAP-XXX |
| (If pharma) | ICH Q10 + 21 CFR 210/211 + EU GMP | Master Batch Record; Validation Master Plan; Site Master File | MBR-XXX, VMP-XXX, SMF-XXX |

## 12. Sign-off (Top Management)

| Role | Name | Date | Signature |
|---|---|---|---|
| [Top Management individual per §5.3] | | | |
| Quality Director | | | |

## 13. References

- ISO 9001:2015 §4 + §5 + §6 + §7 + §8 + §9 + §10.
- Per applicable vertical: ISO 13485 / AS9100D / IATF 16949 / ICH Q10 / ISO 22000 / ISO 14001 / ISO 45001 / ISO 27001 / etc.
- Linked: QUALITY-POLICY-XXX, PROCESS-MAP-XXX, RISK-AND-OPPORTUNITY-REGISTER-XXX, AUDIT-PROCEDURE-TEMPLATE-XXX, MANAGEMENT-REVIEW-TEMPLATE-XXX, CAPA workflow + issue template.

## 14. Revision history

| Version | Date | Author | Changes |
|---|---|---|---|
| 1.0 | YYYY-MM-DD | [Name] | Initial release. |
