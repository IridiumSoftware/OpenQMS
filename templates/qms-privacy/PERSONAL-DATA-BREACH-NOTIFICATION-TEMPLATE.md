---
document_id: PRIV-BREACH-XXX
version: "1.0"
effective_date: YYYY-MM-DD
owner: "[Privacy Officer + Legal Counsel + Security Officer]"
status: draft
---

# Personal Data Breach Notification

**Template for:** Multi-regime personal data breach notification covering GDPR Article 33 (supervisory authority within 72 hours) + Article 34 (data subjects without undue delay when high risk) + CCPA §1798.150 documented incident record (basis for potential consumer civil action) + US state attorney-general breach notification laws cross-reference.
**Use:** One form per incident. Records retained even when notification thresholds not met (Article 33(5) documentation obligation applies regardless).
**Internal SLA:** Initial intake within 1 hour of discovery; preliminary assessment + SA notification decision within 12 hours; SA notification (if required) within 72 hours per Article 33(1); data subject notification (if required) without undue delay per Article 34(1).

---

## 1. Incident identification

| Field | Value |
|---|---|
| Internal incident ID | |
| Date + time of discovery (UTC) | |
| Date + time of incident start (best estimate) | |
| Date + time of incident end (or "ongoing") | |
| Detector (name + role + how detected) | |
| Initial classification | ☐ Confirmed ☐ Suspected ☐ Near miss |
| 72-hour clock starts at (UTC) | |
| 72-hour clock deadline (UTC) | |
| Lead incident manager | |
| DPO informed (date + time) | |
| Senior management informed (date + time) | |
| Legal informed (date + time) | |
| Forensics engaged (provider + scope) | |

## 2. Nature of breach (Article 33(3)(a))

### 2.1 CIA triad classification

| Type | Applicable? | Detail |
|---|---|---|
| **Confidentiality breach** — unauthorised disclosure / access | ☐ | |
| **Integrity breach** — unauthorised alteration | ☐ | |
| **Availability breach** — accidental/unlawful loss of access or destruction | ☐ | |

### 2.2 Cause

| Category | Applicable? | Detail |
|---|---|---|
| External attack — phishing | ☐ | |
| External attack — credential stuffing / brute force | ☐ | |
| External attack — vulnerability exploit | ☐ | |
| External attack — ransomware / malware | ☐ | |
| External attack — social engineering | ☐ | |
| Misconfiguration (storage / network / IAM) | ☐ | |
| Insider — malicious | ☐ | |
| Insider — accidental (e.g., misdirected email, lost device) | ☐ | |
| Third-party / processor breach | ☐ | |
| Physical loss / theft (device, paper records) | ☐ | |
| Disposal failure (improper destruction) | ☐ | |
| Other | ☐ | |

## 3. Categories + approximate number of data subjects (Article 33(3)(a))

| Category of data subject | Approximate number affected | Geographic spread |
|---|---|---|
| Customers | | |
| Employees | | |
| Suppliers | | |
| Patients | | |
| Children (<16) | | |
| Other | | |
| **TOTAL** | | |

## 4. Categories + approximate number of personal data records (Article 33(3)(a))

| Personal data category | Approximate records | Special category (Art 9)? | CCPA SPI (§1798.140(ae))? |
|---|---|---|---|
| Identifiers (name, email, address) | | | |
| Account credentials (username, hashed password, etc.) | | | |
| Financial info | | | ☐ |
| Government identifier (SSN, driver's license, passport) | | | ☐ |
| Precise geolocation | | | ☐ |
| Health data | | ☐ | ☐ |
| Genetic / biometric | | ☐ | ☐ |
| Racial / ethnic origin | | ☐ | ☐ |
| Religious beliefs | | ☐ | ☐ |
| Sex life / sexual orientation | | ☐ | ☐ |
| Trade-union membership | | ☐ | ☐ |
| Children's data | | | |
| Other | | | |

**Encryption / pseudonymisation state at time of breach:**

| Data subset | Encrypted at rest? | Encrypted in transit? | Pseudonymised? | Key compromised? |
|---|---|---|---|---|
| | ☐ | ☐ | ☐ | ☐ |

Article 34(3)(a) exemption (data subject notification not required if data was rendered unintelligible — encrypted / pseudonymised + key not compromised): ☐ Applies ☐ Does not apply

CCPA §1798.150 statutory damages risk: turns on whether data was **non-encrypted AND non-redacted** — both required for the private right of action. ☐ Encryption protects ☐ Both encrypted + non-redacted → no §1798.150 PRA risk

## 5. Likely consequences (Article 33(3)(c))

Per WP250 (Notification of personal data breaches under GDPR) consequence categories:

| Consequence | Likelihood (Low/Med/High) | Severity (Low/Med/High) | Affected subjects |
|---|---|---|---|
| Identity theft / fraud | | | |
| Financial loss | | | |
| Discrimination | | | |
| Reputation damage | | | |
| Physical harm | | | |
| Loss of control over personal data | | | |
| Loss of confidentiality (professionally protected) | | | |
| Limitation of rights | | | |
| Social / professional disadvantage | | | |

**Overall risk to rights + freedoms:**
- ☐ Unlikely → Article 33(1) notification to SA may NOT be required (rare; document reasoning)
- ☐ Likely → Article 33(1) notification TO SA REQUIRED within 72 hours
- ☐ High risk → Article 34(1) notification TO DATA SUBJECTS REQUIRED without undue delay

## 6. Measures taken or proposed (Article 33(3)(d))

| Measure | Status | Owner | Completion target |
|---|---|---|---|
| Immediate containment | | | |
| Eradication (remove cause) | | | |
| Recovery (restore service / data) | | | |
| Affected accounts/credentials reset | | | |
| Affected data subjects identified for notification | | | |
| Legal hold + forensic preservation | | | |
| Vendor/processor notified (if breach via processor) | | | |
| Insurance carrier notified | | | |
| Long-term remediation (architecture / process / training change) | | | |

## 7. Notification decisions

### 7.1 Supervisory authority notification (GDPR Article 33)

| Item | Detail |
|---|---|
| Required? | ☐ Yes ☐ No (unlikely risk to rights + freedoms; document reasoning per §5 above) |
| Lead SA identified (one-stop-shop per Article 56) | |
| Other SAs to notify (cross-border processing) | |
| Notification submission method | ☐ SA online portal ☐ Email ☐ Postal |
| Notification submitted (date + time UTC) | |
| Acknowledgement received | |
| Phased notification per Article 33(4) (if all info not available within 72h) — followup planned | |

### 7.2 Data subject notification (GDPR Article 34)

| Item | Detail |
|---|---|
| Required? | ☐ Yes (high risk to rights + freedoms) ☐ No — exception ☐ Article 34(3)(a) encryption ☐ Article 34(3)(b) subsequent measures eliminate high risk ☐ Article 34(3)(c) disproportionate effort + public communication used instead |
| Notification method | ☐ Direct (email / postal / in-app) ☐ Public communication (Article 34(3)(c)) |
| Notification date | |
| Content (per Article 34(2)): nature of breach + DPO contact + likely consequences + measures taken | ✓ |
| Translation needs (multi-MS / multi-language subjects) | |

### 7.3 CCPA / US state notifications

| Item | Detail |
|---|---|
| California residents affected? | ☐ Yes — Cal. Civ. Code §1798.82 notification triggered if encrypted+redacted exception does not apply |
| California AG notification (if >500 CA residents) | ☐ Submitted: |
| Other state-AG notifications triggered | ☐ Texas (Bus. & Com. Code §521.053) ☐ New York (Gen. Bus. §899-aa) ☐ Florida (Stat. §501.171) ☐ Illinois (815 ILCS 530) ☐ Others: |
| HIPAA Breach Notification Rule applicable? (45 CFR §164.400-414) | ☐ Yes — HHS OCR notification + media if ≥500 individuals |
| FTC Health Breach Notification Rule (16 CFR Part 318)? | ☐ Yes — for vendor of personal health records not subject to HIPAA |
| §1798.150 CCPA private right of action exposure? | ☐ Yes — non-encrypted + non-redacted CA-resident SPI; 30-day cure notice when no actual harm |
| Other regulator (sector-specific — DFS for NY financial; SEC for public companies per Item 1.05 of 8-K) | |

### 7.4 Customer / contractual notification

| Recipient | Notification obligation source | Notified |
|---|---|---|
| Affected customers (account-level) | DPA + customer contracts + Trust + Brand | |
| Affected processors (where this org is processor's controller) | DPA Article 28 flow-down | |
| Insurance carrier | Cyber insurance policy | |
| Stockholders / public | SEC Item 1.05 8-K (4 business days from materiality determination, US public companies) | |
| Press | Communications team coordination | |

## 8. Documentation per Article 33(5)

Required regardless of notification thresholds — internal record sufficient for SA to verify Article 33 compliance.

| Item | Reference |
|---|---|
| Facts relating to breach | |
| Effects | |
| Remedial action taken | |
| Reasoning for notification decisions (notify SA / notify subjects / why not) | |

## 9. Lessons learned + CAPA

| Item | Detail |
|---|---|
| Root cause analysis | |
| Preventive actions | |
| Corrective actions | |
| Detection improvements | |
| Response improvements | |
| Training updates | |
| ROPA / DPIA / privacy policy updates triggered | |
| Linked CAPA ID | |
| Post-incident review date | |
| Post-incident review attendees | |

## 10. Approvals + signoffs

| Role | Name | Signature | Date |
|---|---|---|---|
| Incident manager | | | |
| DPO | | | |
| CISO / Information Security lead | | | |
| Legal | | | |
| Senior management | | | |

---

**Trace evidence.** This breach notification record addresses GDPR-Art-33-34-breach + GDPR-Art-32-security + CCPA-1798-150-data-breach-civil-action per `modules/privacy/module.yaml`. WP250 (Article 29 WP, endorsed by EDPB) + EDPB Guidelines 9/2022 on examples regarding personal data breach notification supplement.

**Cross-reference.** US state AG breach notification deadlines vary widely (some "as expeditiously as possible"; some specific deadlines like 30 days CA / 30 days FL / no later than 60 days TX). Track per-state deadlines in §7.3 for each notification triggered. SEC Item 1.05 8-K applies separately for material cybersecurity incidents at US-public-company controllers (effective 2023-12-15).
