---
document_id: VAL-ER11-001
title: "Electronic Records and Signature Controls (21 CFR Part 11 / EU GMP Annex 11)"
version: "1.0"
effective_date: YYYY-MM-DD
owner: "[Validation Lead / Quality Manager, Title]"
status: draft
approved_by: "[Quality Manager, Title]"
approval_date: YYYY-MM-DD
---

# VAL-ER11-001: Electronic Records and Signature Controls (21 CFR Part 11 / EU GMP Annex 11)

Controls for the electronic records and signatures produced or maintained by a validated computerized system. Applied **commensurate with risk** alongside the system's [Assurance Determination](ASSURANCE-DETERMINATION-TEMPLATE.md). §§1–3 give the **US (21 CFR Part 11)** controls; §4 gives the **EU (GMP Annex 11)** equivalents — use the section(s) for your market overlay(s).

## 1. Part 11 applicability (CSA §V.B)

Determine, per record kind, whether Part 11 applies. A record **required under Part 820** that is created/maintained electronically is generally a **Part 11 electronic record**. Enforcement discretion in the Part 11 scope-and-application guidance does **not** extend to the ISO 13485 §4.1.6/§7.5.6/§7.6 validation obligations.

| Record kind | Required under Part 820? | Maintained electronically? | Part 11 applies? |
|---|---|---|---|
| [e.g., assurance record / audit trail] | yes | yes | yes |
| [e.g., transient activity log] | no | yes | no |

## 2. §11.10 closed-system controls

Confirm, scaled to risk: system validation; accurate and complete human-readable + electronic copies; record protection and retention for the required period; access limited to authorized individuals; secure, computer-generated, time-stamped **audit trails**; operational/authority/device checks as applicable.

## 3. Subpart C — electronic signatures

Where the assurance/validation record is electronically signed (§11.50/§11.100/§11.200/§11.300): the signed record displays the **signer, date/time, and meaning** of the signature; signatures are unique to one individual, verified to that individual, linked to their records, and not transferable.

- **Signature-meaning convention:** see `docs/guide/signature-meaning.md` and the commit-trailer mechanism (`openqms signatures`).
- **Identity mapping:** see `templates/qms-policy/IDENTITY-MAPPING-SOP-TEMPLATE.md` (HR-attested person↔account).

## 4. EU — GMP Annex 11 equivalents

For EU-market systems, apply the Annex 11 controls (same substance, different regime):

- **Data integrity (Annex 11 §5–9, §12):** accuracy checks for critical data; secure storage with backup; **audit trails** capturing GMP-relevant changes and deletions; access controls limiting system access to authorized individuals.
- **Electronic signatures (Annex 11 §14):** e-signatures permanently linked to their records, including the time and date applied.
- **Risk basis (Annex 11 §1 / ICH Q9):** the extent of these controls follows the documented risk assessment.

The Part 11 §§1–3 controls above and these Annex 11 controls are largely congruent; a US+EU system satisfies both from one set of implemented controls, cited to each regime.

