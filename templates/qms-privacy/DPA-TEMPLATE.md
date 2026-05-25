---
document_id: PRIV-DPA-XXX
version: "1.0"
effective_date: YYYY-MM-DD
owner: "[Privacy Officer + Legal Counsel]"
status: draft
---

# Data Processing Agreement (DPA)

**Template for:** Controller-Processor agreement satisfying GDPR Article 28(3) required content + CCPA §1798.140 service provider / contractor / third party contractual restrictions per §7050-7053 CPPA regs.
**Scope:** Use as standalone DPA OR as schedule to a Master Services Agreement.
**International transfers:** If processor located outside EU/EEA without adequacy decision, attach Commission Standard Contractual Clauses (Implementing Decision 2021/915) — Modules 1-4 per the controller/processor configuration.

---

## 1. Parties

| Field | Controller | Processor |
|---|---|---|
| Legal entity name | | |
| Registered address | | |
| EU representative (if non-EU; GDPR Art 27) | | |
| Authorised signatory + title | | |
| DPO + contact (if designated) | | |

## 2. Subject-matter + duration

| Field | Value |
|---|---|
| Underlying service / agreement | |
| Subject-matter of processing | |
| Duration of processing | Co-terminus with underlying agreement OR [specific term] |
| Effective date | |

## 3. Nature + purpose of processing

| Field | Value |
|---|---|
| Nature (operations performed) | e.g., storage, hosting, transmission, analytics, support |
| Purpose of processing | |
| Business purpose category (CCPA §7050(b)) | ☐ Auditing ☐ Security ☐ Debugging ☐ Short-term transient ☐ Performing services ☐ Internal research ☐ Improving services ☐ Other (specify) |

## 4. Type of personal data + categories of data subjects (GDPR Art 28(3))

| Category of data subject | Categories of personal data | Special categories (Art 9)? |
|---|---|---|
| Customers | | ☐ |
| Customer's employees | | ☐ |
| Suppliers | | ☐ |
| Patients / participants | | ☐ Health data |
| Children (<16 GDPR / <16 CCPA / <13 COPPA) | | |

## 5. Controller obligations + rights

- Controller has determined lawful basis under GDPR Article 6 (and Article 9 condition where SPI involved) for each processing purpose
- Controller has provided GDPR Article 13/14 information to data subjects
- Controller has authority to instruct Processor as set out in this DPA
- Controller is responsible for accuracy of personal data submitted to Processor
- Controller retains data-subject-request triage; Processor assists per §7 below

## 6. Processor obligations (GDPR Article 28(3))

### 6.1 Documented instructions only

Processor processes personal data only on **documented instructions from Controller**, including with regard to international transfers, unless required to do so by Union or Member State law (in which case Processor informs Controller of that legal requirement before processing, unless that law prohibits notification).

### 6.2 Confidentiality

Processor ensures persons authorized to process personal data have committed themselves to confidentiality or are under appropriate statutory obligation of confidentiality.

### 6.3 Security (Article 32)

Processor implements appropriate technical + organisational measures to ensure level of security appropriate to the risks. Minimum measures per Annex 1 — Technical and Organisational Measures (attached).

### 6.4 Sub-processor authorisation (Article 28(2) + 28(4))

| Option | Selected |
|---|---|
| ☐ Specific prior written authorisation per sub-processor | |
| ☐ General written authorisation with right-to-object on changes; Processor maintains list of sub-processors at [URL]; 30-day prior notification of additions/replacements; Controller may object on reasonable grounds; if objection cannot be resolved, Controller may terminate the affected portion of services | |

Each sub-processor flow-down must impose same data-protection obligations as in this DPA.

### 6.5 Data subject rights assistance (Article 28(3)(e))

Processor assists Controller with appropriate technical + organisational measures, insofar as possible, in fulfilling Controller's obligation to respond to data subject requests under Chapter III of GDPR.

Response SLA: Processor acknowledges DSR-assistance request within **N business days**; provides requested data/action within **N business days** of acknowledgement, in any case sufficient to allow Controller to meet GDPR 1-month / CCPA 45-day deadline.

### 6.6 Breach + DPIA + consultation assistance (Article 28(3)(f))

Processor assists Controller with Articles 32-36 obligations: notifying Processor-side personal data breach to Controller **without undue delay AND in any case within 24 hours** of becoming aware (sufficient to allow Controller to meet 72-hour SA notification); assisting with DPIA (Article 35); assisting with prior consultation of supervisory authority (Article 36).

### 6.7 Deletion / return at end of services (Article 28(3)(g))

At Controller's choice, Processor deletes OR returns all personal data after the end of the provision of services, and deletes existing copies, unless Union or Member State law requires storage.

| Option | Selected |
|---|---|
| ☐ Delete | within N days of termination; certificate of destruction provided |
| ☐ Return | in [format] within N days of termination |

### 6.8 Audit + information (Article 28(3)(h))

Processor makes available to Controller all information necessary to demonstrate compliance with Article 28 + allows for + contributes to audits, including inspections, conducted by Controller or another auditor mandated by Controller.

| Audit configuration | Detail |
|---|---|
| Frequency | Once per year (more often if reasonable cause incl. breach / regulatory inquiry) |
| Notice required | 30 days |
| Reasonable hours | Yes — during business hours |
| Confidentiality requirements | Reasonable NDA required |
| Cost | Borne by Controller unless audit reveals material breach by Processor |
| Independent attestation acceptable in lieu | ☐ SOC 2 Type II ☐ ISO 27001 ☐ ISO 27701 ☐ HITRUST ☐ Other: |

## 7. International transfers (GDPR Articles 44-49)

| Item | Detail |
|---|---|
| Personal data transferred outside EU/EEA? | ☐ No ☐ Yes — see §7.1 below |
| Adequacy decision applies? | ☐ Yes — country: |
| Standard Contractual Clauses 2021/915 attached? | ☐ Yes — Module(s): ☐ 1 C-C ☐ 2 C-P ☐ 3 P-P ☐ 4 P-C |
| Transfer Impact Assessment (Schrems II) completed | ☐ Yes — dated: ; ☐ Supplementary measures identified |
| Binding Corporate Rules in place? | ☐ Yes — reference: |
| EU-US Data Privacy Framework certification (for US destinations) | ☐ Yes — DPF list link: |

## 8. CCPA service provider / contractor / third party classification (§7050-7053)

| Item | Selected |
|---|---|
| Processor is | ☐ Service Provider (§1798.140(ag)) ☐ Contractor (§1798.140(j)) ☐ Third Party (sale/share) |
| Permitted uses | Limited to business purposes specified in §3 above |
| Certification of CCPA compliance | Processor certifies understanding of restrictions + agreement to comply per §1798.140(ag)(1)(D) |
| Prohibitions | No selling/sharing PI received from Controller; no retaining/using/disclosing for purposes other than business purpose specified in §3 OR as permitted by §7050; no combining PI received from Controller with PI from another source except for §7050(c) limited purposes |
| Sub-processor flow-down per §7050(a)(5) | Required |
| Consumer-request assistance per §1798.130 | Required |
| Cybersecurity audit assistance | Required when applicable per CPPA Cybersecurity Audit regulations |
| Risk assessment assistance | Required when applicable per CPPA Risk Assessment regulations |
| ADMT assistance | Required when applicable per CPPA ADMT regulations |
| Deletion notification flow-down | Processor directs sub-processors to delete on Controller's deletion request |

## 9. Liability + indemnification

Per underlying agreement, with the following privacy-specific carve-outs:
- Article 82 GDPR joint + several liability framework respected
- §1798.150 CCPA private right of action — Processor indemnifies for breach caused by Processor's failure to implement reasonable security
- [Per-controller-policy: cap exclusion for privacy-law fines, regulatory penalties, breach-notification costs]

## 10. Term + termination

Effective on signature; terminates with underlying agreement OR on Controller's written notice for material breach with 30-day cure period (no cure for §6.1 documented-instructions breach OR §6.4 unauthorised sub-processor).

Post-termination, §6.7 (return/deletion) applies.

## 11. Notices

| Recipient | Method | Address |
|---|---|---|
| Controller (privacy-related notices) | | |
| Processor (privacy-related notices) | | |
| Controller DPO | | |

Notification SLAs:
- Personal data breach (Processor → Controller): within 24 hours of awareness
- Sub-processor addition/replacement (Processor → Controller): 30 days prior
- DSR assistance request: per §6.5 above
- Audit notice: 30 days prior

## 12. Governing law + dispute resolution

Per underlying agreement; provided that for processing of EU/EEA data subjects' personal data, EU/EEA data protection law governs the data-protection-specific obligations.

## 13. Annexes

| Annex | Content |
|---|---|
| 1 | Technical + Organisational Measures (TOM) per Article 32 |
| 2 | List of sub-processors authorised at signature |
| 3 | Standard Contractual Clauses (Implementing Decision 2021/915) — selected Module + Appendices |
| 4 | UK International Data Transfer Addendum (UK IDTA) where UK transfers in scope |
| 5 | Transfer Impact Assessment (where SCCs required) |

## 14. Signatures

| Party | Name + title | Signature | Date |
|---|---|---|---|
| Controller | | | |
| Processor | | | |

---

**Trace evidence.** This DPA addresses GDPR-Art-28-processor-agreements + GDPR-Art-44-49-transfers + CCPA-1798-140-service-provider-contractor per `modules/privacy/module.yaml`. EDPB Guidelines 07/2020 on the concepts of controller and processor under GDPR + EDPB Recommendations 01/2020 on supplementary measures (post-Schrems II) supplement. Annexes 1-5 site-specific.
