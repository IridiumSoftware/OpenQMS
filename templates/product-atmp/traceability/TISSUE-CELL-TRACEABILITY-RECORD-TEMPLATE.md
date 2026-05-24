---
document_id: TCTR-XXX
title: "[ATMP Product + Batch ID] — Tissue / Cell Traceability Record"
version: "1.0"
effective_date: YYYY-MM-DD
owner: "[QA Traceability Lead, Title]"
status: open (active for life of product + retention period)
qa_approver: "[QA Director]"
approval_date: YYYY-MM-DD
retention_target_eu: "30 years after clinical administration per Directive 2004/23/EC Article 8"
retention_target_us: "10 years after administration per 21 CFR 1271.270"
---

# TCTR-XXX: Tissue / Cell Traceability Record

Per EU GMP Annex 2A §10 (Traceability) + Directive 2004/23/EC Article 8 + Directive 2006/86/EC + 21 CFR 1271.290 (Traceability and Reporting). Establishes the bidirectional traceability chain from donor through starting material → manufacturing intermediates → finished ATMP → distribution → recipient administration. The chain must enable:

- **Donor → product → recipient** ("forward" traceability — for recipient adverse-event investigation)
- **Recipient → product → donor** ("reverse" traceability — for donor-source-related adverse event affecting multiple recipients)
- **Recall capability** — rapid identification of all recipients of product derived from a specific donor or batch

For ATMPs, traceability is uniquely critical because:

1. **Autologous products** — single donor = single recipient; mismatch is patient-safety-critical (giving Patient A's cells to Patient B can be lethal).
2. **Allogeneic products** — single donor may produce multiple batches over time; donor-derived hazard (latent infection, donor cell-line abnormality) may affect many recipients.
3. **Long retention** — 30 years EU / 10 years US means traceability records outlive most operational systems → archival + format-stability planning required.

## 1. Product identification

- **ATMP product name + classification:** [name] [autologous CAR-T / allogeneic CAR-T / iPSC-derived / gene-modified HSCT / oncolytic virus / etc.]
- **Marketing authorization / IND reference:** [MA# or IND#]
- **Manufacturing site:** [licensed facility]
- **Batch identifier:** [unique batch ID]
- **Manufacturing date:** [YYYY-MM-DD start to YYYY-MM-DD finish]
- **Expiry date / use-by:** [YYYY-MM-DD]
- **Storage requirements:** [cryogenic / refrigerated / ambient; specific temperature + LN2 vapor-phase as applicable]

## 2. Donor → starting material chain

| Donor UDI (pseudonymized) | Donor Eligibility Record | Donation date | Procurement site | Starting material UDI | Collection volume / count | Transit chain (controlled temperature; chain-of-custody) | Receipt at manufacturing site |
|---|---|---|---|---|---|---|---|
| | DEA-XXX | | | | | | |

For **autologous products**, this row is a single donor → single starting material → single batch.

For **allogeneic products**, multiple donations may pool into a single starting material (with corresponding multi-DEA reference), OR a single donor may yield multiple manufacturing batches over time.

## 3. Manufacturing chain (intermediate-by-intermediate)

| Manufacturing step | In-process material UDI | Date | Operator | Equipment ID | Linked MBR step | Hold / transfer chain-of-custody | Notes |
|---|---|---|---|---|---|---|---|

Each manufacturing step must be linked to:
- The MBR step that produced it (with its CPP results)
- The next downstream material it became
- The personnel + equipment involved

## 4. Finished product → distribution chain

| Finished product UDI (label code) | Pack date | Initial storage location | Distribution event date | Carrier | Chain-of-custody / temperature log | Receipt at clinical site | Recipient unique identifier (pseudonymized) | Administration date |
|---|---|---|---|---|---|---|---|---|

For autologous products, the recipient UDI is determined at the time of starting-material collection (the recipient IS the donor). The full chain is donor → manufacturing → administration to same patient.

For allogeneic products, the recipient UDI is assigned at the time of clinical-site delivery and recorded here.

## 5. Bidirectional traceability assertions

The following queries shall be answerable from this record (combined with linked records — DEA-XXX, MBR-XXX, distribution records):

### Forward (donor → recipient)
- "Donor UDI [D] produced which finished products?" → list of finished-product UDIs
- "Donor UDI [D]'s product(s) went to which recipient(s)?" → list of recipient UDIs

### Reverse (recipient → donor)
- "Recipient UDI [R] received which finished product UDI?" → finished-product UDI
- "Recipient UDI [R]'s product was derived from which donor UDI?" → donor UDI

### Recall scope
- "If donor [D] is later determined ineligible (e.g., latent infection diagnosed), which recipients require notification?" → list of recipient UDIs
- "If batch [B] fails post-distribution testing, which finished-product UDIs from this batch are at which clinical sites?" → list of UDIs + sites

## 6. Format + media stability for long retention

EU 30-year + US 10-year retention requires media + format stability planning:

| Concern | Mitigation |
|---|---|
| Electronic-record format obsolescence | Use long-stable formats (PDF/A, CSV, XML); periodic format migration with checksums; vendor independence in archival storage |
| Physical-media degradation | Replicated storage; periodic media refresh; redundant offsite backup |
| Personnel turnover | Archival system documented; access protocols maintained; multi-person knowledge |
| Organizational change (merger / acquisition / dissolution) | Records-retention obligation transferred contractually; regulator notification per Directive 2004/23/EC Art. 4 if procurement organization changes |
| Encryption-key custody | Long-term key escrow; key-rotation discipline |

## 7. PHI / GDPR considerations

This TCTR uses pseudonymized UDIs. The linkage back to identifiable patient/donor information lives in a separate access-restricted system per the organization's PHI compartmentalization architecture (cross-reference to OQ-062 and the project's "PHI compartmentalization architecture" decision).

- **Donor UDI → identifiable donor record:** lives in separate registry per 21 CFR 1271.270 + HIPAA + GDPR Special Category data requirements
- **Recipient UDI → identifiable recipient record:** lives in clinical-site records + the procurement organization's tracking system
- **Re-identification authority:** [pseudonymization-link-controller role and authorization process]

## 8. Reporting obligations (per 21 CFR 1271.350 + Directive 2004/23/EC Art. 11)

Adverse-reaction + adverse-event reporting:

- **HCT/P deviation reports** per 21 CFR 1271.350(a) — any event that represents a deviation from applicable regulations / standards / specifications that may relate to the transmission or potential transmission of a communicable disease to a recipient + any event that is unexpected.
- **EU Serious Adverse Reaction / Serious Adverse Event (SAR / SAE)** reporting per Directive 2004/23/EC Art. 11.
- **MA-holder reporting** under EU pharmacovigilance + FDA postmarketing for products with MA / BLA approval.

## 9. Sign-off (current version)

| Role | Name | Date | Signature |
|---|---|---|---|
| QA Traceability Lead | | | |
| Production Manager | | | |
| Distribution / Logistics Lead | | | |
| Responsible Person per EU Directive 2004/23/EC Art. 17 (EU jurisdictions) | | | |
| QA Director | | | |

## 10. References

- EU GMP Annex 2A — Manufacture of ATMPs for Human Use; §10 Traceability.
- EU Directive 2004/23/EC — Quality + safety standards for human tissues and cells; Article 8 (Traceability) + Article 11 (Notification of serious adverse events and reactions).
- EU Directive 2006/86/EC — Technical requirements for coding, processing, preservation, storage, distribution + traceability of human tissues and cells.
- 21 CFR 1271.290 — Tracking + tracing.
- 21 CFR 1271.270 — Records (retention).
- 21 CFR 1271.350 — Reporting.
- EU Single European Code (SEC) — coding system for human tissues and cells, mandatory under Directive 2015/565.
- Linked: DEA-XXX (Donor Eligibility Assessment for each donor in the chain), MBR-XXX (Master Batch Record), VSE-XXX (Viral Safety Evaluation if applicable to product type), SOP-XXX (organization's traceability + chain-of-custody SOP), distribution records, clinical-site administration records.

## 11. Revision history (track each material update — appending only; do NOT overwrite prior entries; this record may stay open for decades)

| Version | Date | Author | Changes |
|---|---|---|---|
| 1.0 | YYYY-MM-DD | [Name] | Initial record open. |
