---
document_id: SOP-AUDIT-001
title: "Internal Audit Procedure"
version: "1.0"
effective_date: YYYY-MM-DD
owner: "[QA Manager, Title]"
status: draft
approved_by: "[Quality Lead, Title]"
approval_date: YYYY-MM-DD
---

# SOP-AUDIT-001: Internal Audit Procedure

Per ISO 13485 §8.2.4 (Internal audit) and 21 CFR 820.22 (Quality audit). Defines how internal audits of the QMS are planned, conducted, recorded, and followed up.

## 1. Purpose and scope

[This SOP applies to every internal audit of the QMS. External audits (notified body, FDA inspection, MDSAP) are out of scope.]

## 2. Audit program planning

- **Audit cadence:** [Risk-based — every QMS process audited at minimum once per [interval]; high-risk or recently-changed processes more frequently.]
- **Annual audit schedule:** Documented in the management-review record for the prior period; published in `qms-audits/audit-schedule.md` (or equivalent).
- **Auditor independence:** Auditors shall not audit their own work. Cross-functional auditor rotation is required.

## 3. Auditor qualification

- **Internal auditor training:** Documented training on ISO 13485, 21 CFR 820, the organization's QMS, and audit technique.
- **Lead auditor:** Additional qualification per the auditor-qualification record.
- **Qualification records:** Maintained per the training-record SOP.

## 4. Audit procedure

1. **Scoping.** Lead auditor publishes the audit plan: scope (which QMS processes, which products, which time period), schedule, team, criteria (the standards / SOPs being audited against), and expected outputs.
2. **Opening meeting.** Confirm scope, schedule, communication channels.
3. **Evidence gathering.** Document review, process observation, personnel interviews. Each evidence item recorded with reference.
4. **Findings categorization.**
   - **Major nonconformity** — systemic failure or absence of a required QMS element.
   - **Minor nonconformity** — isolated lapse not constituting a systemic failure.
   - **Observation** — opportunity for improvement; not a nonconformity.
5. **Closing meeting.** Auditor reviews findings with auditee; clarifies disputes.
6. **Audit report.** Lead auditor publishes the audit report within [N business days].
7. **Findings disposition.** Major and minor nonconformities each get a CAPA issue opened (`capa.yml` template). Observations may or may not, per management discretion.
8. **Closure.** CAPA effectiveness checks complete; report is filed; findings are inputs to the next management review.

## 5. Records

- **Audit reports** — `qms-audits/` (or per organizational structure).
- **Audit-finding CAPAs** — issue tracker, labeled `audit-finding` + `capa`.
- **Auditor qualification records** — training file.
- **Audit schedule** — published; updated per period.

## 6. Management review input

Audit results are a required input per `docs/guide/management-review.md` (§3.2 internal audit results). Each periodic management review covers: audits completed, findings by severity, CAPAs opened from findings, open findings with target closure dates.

## 7. Regulatory inspection interface

When external regulators (FDA, notified body, MDSAP auditor) request audit records, this procedure governs what is provided and how. Internal audit records are quality records under 21 CFR 820.180; access is per the organization's records-control SOP.

## 8. References

- ISO 13485:2016 §8.2.4 — Internal audit.
- 21 CFR 820.22 — Quality audit.
- EU MDR Annex IX §2.2 — QMS audit by notified body (related, not in scope of this SOP).
- ISO 19011 — Guidelines for auditing management systems (informative).

## 9. Revision history

| Version | Date | Author | Changes |
|---|---|---|---|
| 1.0 | YYYY-MM-DD | [Name] | Initial release. |
