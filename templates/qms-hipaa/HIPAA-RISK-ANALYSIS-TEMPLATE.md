# HIPAA Security Rule Risk Analysis

**Template for:** HIPAA Security Rule §164.308(a)(1)(ii)(A) Risk Analysis — foundational Security Rule artifact. Required for CEs + BAs. Updated at least annually + on material change to systems / threats / business operations / regulations.
**Scope:** ePHI (electronic Protected Health Information). Distinct from organisation-wide risk assessment though may be combined.
**Retention:** 6 years from date created OR last in effect per §164.316(b)(2)(i).

---

## 1. Identification

| Field | Value |
|---|---|
| Organisation legal name | |
| Risk Analysis version | |
| Coverage period | [YYYY-MM-DD to YYYY-MM-DD] |
| Last updated | [YYYY-MM-DD] |
| Next scheduled update | [YYYY-MM-DD — annual recommended] |
| Analyst(s) + qualifications | |
| Security Officer + approval signature | |
| Privacy Officer review | |
| Senior management approval | |
| Reference HHS Guidance | "Guidance on Risk Analysis Requirements under the HIPAA Security Rule" |

## 2. Scope statement

| Item | Detail |
|---|---|
| Covered facilities | |
| Systems in scope (ePHI-creating / -receiving / -maintaining / -transmitting) | |
| Systems explicitly OUT of scope + justification | |
| Workforce in scope | |
| BAs in scope (with reference to BAAs) | |
| Sub-contractor sub-BAs in scope | |
| Geographic scope (US + non-US PHI storage / processing) | |

## 3. ePHI inventory

For each system handling ePHI, inventory the data flows.

| System / Application | Data classification (PHI / ePHI / non-PHI) | Volume of records | Source(s) | Destination(s) | Retention | Encryption at rest | Encryption in transit | Owner |
|---|---|---|---|---|---|---|---|---|
| | | | | | | ☐ | ☐ | |

## 4. Threat catalog

Catalog reasonably anticipated threats per HHS Guidance. Threat sources include natural, human (intentional + unintentional), environmental.

| # | Threat | Source | Affected ePHI assets | Threat likelihood (per §6) |
|---|---|---|---|---|
| T01 | Unauthorized network intrusion | External attacker | All internet-exposed ePHI | |
| T02 | Phishing / credential theft | External attacker | User-account-accessible ePHI | |
| T03 | Ransomware | External attacker | All ePHI | |
| T04 | Insider — malicious | Workforce member | Role-accessible ePHI | |
| T05 | Insider — accidental (misdirected email, misconfigured share) | Workforce member | Role-accessible ePHI | |
| T06 | Lost / stolen device | Workforce member + external | Device-resident ePHI | |
| T07 | Improper disposal (media, paper) | Workforce + waste-handler | Disposed ePHI | |
| T08 | BA / sub-BA breach | BA / Sub-BA | BA-held ePHI | |
| T09 | Cloud-provider compromise | Cloud provider | Cloud-hosted ePHI | |
| T10 | Natural disaster (fire, flood, earthquake) | Environment | Facility-resident ePHI | |
| T11 | Power outage / system failure | Environment / infrastructure | Availability of ePHI | |
| T12 | Software vulnerability exploit | External attacker | Vulnerable systems | |
| T13 | DDoS — availability | External attacker | Internet-facing ePHI systems | |
| T14 | Supply-chain compromise (vendor SW update, dependency injection) | External attacker | Dependent systems | |
| T15 | [organisation-specific threat] | | | |

## 5. Vulnerability assessment

Per system, identify vulnerabilities that could be exploited by threats.

| # | Vulnerability | Affected system(s) | Existing controls | Control effectiveness (High / Med / Low) |
|---|---|---|---|---|
| V01 | Missing patches | | | |
| V02 | Weak authentication (no MFA) | | | |
| V03 | Insufficient access logging | | | |
| V04 | Unencrypted data at rest | | | |
| V05 | Unencrypted transmission | | | |
| V06 | Inadequate workforce training | | | |
| V07 | No automatic logoff | | | |
| V08 | Workstation physical exposure | | | |
| V09 | No BAA with vendor | | | |
| V10 | No DR / contingency plan | | | |
| V11 | No audit log review | | | |
| V12 | Default credentials | | | |
| V13 | Outdated unsupported software | | | |
| V14 | [organisation-specific vulnerability] | | | |

## 6. Risk determination per threat × vulnerability

For each plausible threat × vulnerability combination, determine likelihood + impact → risk level.

| # | Threat (T##) | Vulnerability (V##) | Affected system(s) | Likelihood (High / Med / Low) | Impact (High / Med / Low — based on # records + sensitivity + breach-notification consequences + operational disruption + reputational) | Inherent risk level | Residual risk level after current controls |
|---|---|---|---|---|---|---|---|
| R001 | T01 | V01, V12 | | | | | |
| R002 | T02 | V02, V06 | | | | | |
| R003 | T03 | V01, V10, V11 | | | | | |
| R004 | T04 | V03, V07 | | | | | |
| R005 | T05 | V06 | | | | | |
| R006 | T06 | V04, V08 | | | | | |
| R007 | T07 | (none — process control) | | | | | |
| R008 | T08 | V09 | | | | | |
| R009 | T09 | V04 | | | | | |
| R010 | T10 | V10 | | | | | |
| R011 | T11 | V10 | | | | | |
| R012 | T12 | V01, V13 | | | | | |
| R013 | T13 | (process control) | | | | | |
| R014 | T14 | V01 | | | | | |
| R015 | [organisation-specific] | | | | | | |

## 7. Risk treatment plan

For each risk per §6 with residual risk Medium or High, define treatment.

| Risk # | Treatment strategy | Specific control(s) | Implementation owner | Implementation deadline | Post-treatment residual risk target | Status |
|---|---|---|---|---|---|---|
| R### | ☐ Mitigate (apply control) ☐ Transfer (insurance, BAA) ☐ Avoid (cease activity) ☐ Accept (document rationale) | | | | | ☐ Planned ☐ In-progress ☐ Complete |

## 8. Security Rule implementation specification status

For each required/addressable implementation specification per §164.308 / §164.310 / §164.312, document status.

### 8.1 Administrative Safeguards (§164.308)

| Specification | Type | Status | Documentation reference |
|---|---|---|---|
| §164.308(a)(1)(ii)(A) Risk Analysis | R | ☐ This document | |
| §164.308(a)(1)(ii)(B) Risk Management | R | | |
| §164.308(a)(1)(ii)(C) Sanction Policy | R | | |
| §164.308(a)(1)(ii)(D) Information System Activity Review | R | | |
| §164.308(a)(2) Assigned Security Responsibility | R | | |
| §164.308(a)(3)(ii)(A) Authorization + Supervision | A | ☐ Implemented ☐ Alternative ☐ Justified absence | |
| §164.308(a)(3)(ii)(B) Workforce Clearance | A | | |
| §164.308(a)(3)(ii)(C) Termination Procedures | A | | |
| §164.308(a)(4)(ii)(A) Isolating Healthcare Clearinghouse Functions | R (if clearinghouse) | | |
| §164.308(a)(4)(ii)(B) Access Authorization | A | | |
| §164.308(a)(4)(ii)(C) Access Establishment + Modification | A | | |
| §164.308(a)(5)(ii)(A) Security Reminders | A | | |
| §164.308(a)(5)(ii)(B) Protection from Malicious Software | A | | |
| §164.308(a)(5)(ii)(C) Log-in Monitoring | A | | |
| §164.308(a)(5)(ii)(D) Password Management | A | | |
| §164.308(a)(6)(ii) Response + Reporting (incident response) | R | | |
| §164.308(a)(7)(ii)(A) Data Backup Plan | R | | |
| §164.308(a)(7)(ii)(B) Disaster Recovery Plan | R | | |
| §164.308(a)(7)(ii)(C) Emergency Mode Operation Plan | R | | |
| §164.308(a)(7)(ii)(D) Testing + Revision Procedures | A | | |
| §164.308(a)(7)(ii)(E) Applications + Data Criticality Analysis | A | | |
| §164.308(a)(8) Evaluation (periodic technical + non-technical) | R | | |
| §164.308(b)(1) Business Associate Contracts | R | | |

### 8.2 Physical Safeguards (§164.310)

| Specification | Type | Status |
|---|---|---|
| §164.310(a)(2)(i) Contingency Operations | A | |
| §164.310(a)(2)(ii) Facility Security Plan | A | |
| §164.310(a)(2)(iii) Access Control + Validation Procedures | A | |
| §164.310(a)(2)(iv) Maintenance Records | A | |
| §164.310(b) Workstation Use | R | |
| §164.310(c) Workstation Security | R | |
| §164.310(d)(2)(i) Disposal | R | |
| §164.310(d)(2)(ii) Media Re-Use | R | |
| §164.310(d)(2)(iii) Accountability | A | |
| §164.310(d)(2)(iv) Data Backup + Storage | A | |

### 8.3 Technical Safeguards (§164.312)

| Specification | Type | Status |
|---|---|---|
| §164.312(a)(2)(i) Unique User Identification | R | |
| §164.312(a)(2)(ii) Emergency Access Procedure | R | |
| §164.312(a)(2)(iii) Automatic Logoff | A | |
| §164.312(a)(2)(iv) Encryption + Decryption (at rest) | A | |
| §164.312(b) Audit Controls | R | |
| §164.312(c)(2) Mechanism to Authenticate ePHI (integrity) | A | |
| §164.312(d) Person or Entity Authentication | R | |
| §164.312(e)(2)(i) Integrity Controls (transmission) | A | |
| §164.312(e)(2)(ii) Encryption (transmission) | A | |

For each Addressable (A) specification not implemented, document why (alternative + documented decision + justification per §164.306(d)(3)).

## 9. Approvals + revision history

| Role | Name | Signature | Date |
|---|---|---|---|
| Security Officer | | | |
| Privacy Officer | | | |
| CIO / CISO | | | |
| Senior management | | | |

| Version | Date | Material changes | Approved by |
|---|---|---|---|
| 1.0 | | Initial | |

---

**Trace evidence.** This Risk Analysis addresses HIPAA-164-306-308-security-administrative-safeguards + HIPAA-164-310-physical-safeguards + HIPAA-164-312-technical-safeguards + HIPAA-164-316-documentation-retention per `modules/hipaa/module.yaml`. HHS Guidance "Guidance on Risk Analysis Requirements under the HIPAA Security Rule" + NIST SP 800-66 Rev 2 "Implementing the HIPAA Security Rule" supplementary.
