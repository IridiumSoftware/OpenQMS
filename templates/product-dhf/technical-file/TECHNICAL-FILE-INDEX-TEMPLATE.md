---
document_id: TFI-XXX
title: "[Product Name] — Technical File Index"
version: "1.0"
effective_date: YYYY-MM-DD
owner: "[Regulatory Affairs, Title]"
status: draft
approved_by: "[QA / RA Lead, Title]"
approval_date: YYYY-MM-DD
---

# TFI-XXX: [Product Name] Technical File Index

Per ISO 13485 §4.2.3 (Medical device file) and EU MDR Annex II (Technical documentation). The Technical File Index is the navigable manifest of every document that constitutes the device's technical file. Notified bodies and regulators expect a structured, addressable view — this index is that view.

Open QMS organizes the underlying documents under `product-*/` (DHF, software lifecycle, etc.); this index aggregates them with versions, document IDs, and submission-pack readiness state.

## 1. Device identification

- **Product name:** [name]
- **Model(s) / variant(s):** [list]
- **Risk classification:** [FDA Class I/II/III; MDR Class I/IIa/IIb/III; per applicable jurisdiction]
- **Intended use:** [as approved by management; full statement]
- **Indications for use:** [if distinct from intended use]
- **GMDN / SRN / UDI:** [where applicable]
- **Manufacturer:** [legal name + registered address]
- **Authorized representative** (EU MDR): [name + address]

## 2. Index by Annex II section (EU MDR mapping)

| Annex II § | Topic | Document(s) | Version | DocID | Status |
|---|---|---|---|---|---|
| 1 | Device description and specification, including variants and accessories | [Product specification doc] | [vN] | [DOC-ID] | [Released / Draft / Pending] |
| 1.1 | Device description, intended purpose, intended users | TFI-XXX §1 (this doc) + [intended-use statement] | | | |
| 1.2 | Reference to previous and similar generations | [predicate analysis] | | | |
| 2 | Information to be supplied by the manufacturer (labeling + IFU) | [labeling spec; IFU] | | | |
| 3 | Design and manufacturing information | [design history file index; manufacturing instructions] | | | |
| 4 | General Safety and Performance Requirements (GSPR) | [GSPR checklist with evidence references] | | | |
| 5 | Benefit-risk analysis and risk management | RMF-XXX-001 | | | |
| 6 | Product verification and validation | VP-XXX-001; VAL-XXX-001 | | | |
| 6.1 | Pre-clinical / clinical data | [test reports; clinical evaluation report (CER)] | | | |
| 6.2 | PMCF (if applicable) | [PMCF plan + reports] | | | |

## 3. Index by ISO 13485 §4.2.3 (Medical device file mapping)

| ISO 13485 §4.2.3 element | Document(s) | Notes |
|---|---|---|
| Device description, intended use, labeling | §1 + [labeling spec] | |
| Specifications | [product spec, drawings, BOM] | |
| Manufacturing, packaging, storage, handling, distribution specs | [manufacturing instructions; packaging spec; ISTA validation report] | |
| Measurement and monitoring procedures | [SOPs] | |
| Installation requirements (where applicable) | [installation guide] | |
| Servicing procedures (where applicable) | [service manual; field service SOP] | |

## 4. Software (IEC 62304) sub-index

| IEC 62304 § | Topic | Document |
|---|---|---|
| 5.1 / 5.2 | Software development plan + requirements | SRS-XXX-001 |
| 5.3 / 5.4 | Architectural + detailed design | SAD-XXX-001 |
| 5.5–5.7 | Unit / integration / system test | STP-XXX-001 |
| 5.8 | Release record | SRR-XXX-001 |
| 7 | Software risk management | RMF-XXX-001 software-specific sections |
| 8.1.2 | SOUP register | SOUP-XXX-001 |
| 9 | Software problem resolution | (issue templates: nonconformance + CAPA) |

## 5. Cross-cutting QMS evidence

| Topic | Document |
|---|---|
| Quality policy | QP-001 |
| Document control SOP | SOP-XXX-DOC |
| Supplier controls | ASL-001 + SE-XXX records |
| Complaint handling | (issue template: complaint) |
| Management review | MR-XXX (most recent + period covered) |
| Internal audit | (audit reports) |
| CAPA | (issue tracker: capa label) |

## 6. Submission pack assembly

For regulatory submissions, this index is filtered to the submission's scope and exported. The export process (typically `gh` API or a script) produces a single PDF / archive containing every referenced document at its referenced version, plus a cover that maps the submission's required-document list to the entries above.

## 7. References

- ISO 13485:2016 §4.2.3 — Medical device file.
- EU MDR 2017/745 Annex II — Technical documentation.
- EU MDR Annex IX — Conformity assessment based on QMS and assessment of technical documentation.
- 21 CFR 820.181 — Device Master Record.
- IEC 62304:2006+A1:2015 — Software life cycle processes.

## 8. Revision history

| Version | Date | Author | Changes |
|---|---|---|---|
| 1.0 | YYYY-MM-DD | [Name] | Initial release. |
