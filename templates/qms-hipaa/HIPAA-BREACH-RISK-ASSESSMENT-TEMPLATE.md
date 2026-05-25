---
document_id: HIPAA-BRA-XXX
version: "1.0"
effective_date: YYYY-MM-DD
owner: "[Privacy Officer + Security Officer]"
status: draft
---

# HIPAA Breach 4-Factor Risk Assessment

**Template for:** HIPAA Breach Notification Rule §164.402(2) 4-factor presumption-rebuttal assessment. Used to determine whether an impermissible use/disclosure of PHI constitutes a reportable "Breach" requiring §164.404 individual / §164.406 media / §164.408 HHS notification.
**Default presumption:** Any acquisition / access / use / disclosure of unsecured PHI not permitted by Privacy Rule IS a breach, unless this 4-factor assessment demonstrates LOW probability that PHI has been compromised.
**Retention:** ≥ 6 years per §164.316 + §164.530(j).

---

## 1. Incident identification

| Field | Value |
|---|---|
| Internal incident ID | |
| Discovery date + time (UTC) | |
| Incident start date + best estimate | |
| Reporter (name + role) | |
| Reporter contact | |
| Suspected? ☐ Yes ☐ No | |
| Confirmed? ☐ Yes ☐ No | |
| Privacy Officer informed (date + time) | |
| Security Officer informed (date + time) | |
| Legal informed (date + time) | |
| Forensics engaged (yes/no + provider) | |
| Insurance carrier notified | |
| BA-discovered? ☐ Yes — see §164.410 BA notification to CE (60 days from BA's discovery; this incident's clock for CE individual notification starts at CE's discovery) | |

## 2. Threshold question — is this an impermissible use/disclosure of PHI?

| Question | Response |
|---|---|
| Was PHI involved? | ☐ Yes ☐ No (if no — not a Breach Notification Rule incident; document briefly) |
| Was the use/disclosure permitted by Privacy Rule §164.502-514? | ☐ Yes — permitted (not a breach) ☐ No — impermissible (continue) |
| Was the use/disclosure made by a covered entity, business associate, or workforce member? | ☐ Yes (in scope) ☐ No (not in scope) |

If impermissible use/disclosure → presumption of breach. Proceed to §3.

## 3. Threshold question — was the PHI "unsecured"?

Per HHS Guidance on encryption/destruction safe harbor:

| Question | Response |
|---|---|
| Was the PHI encrypted to NIST-acceptable standards (NIST SP 800-111 at rest; NIST SP 800-52/77 in transit; FIPS 140-2/3 validated) AND were decryption keys NOT compromised? | ☐ Yes (PHI is "secured" → SAFE HARBOR — no breach notification required; document this assessment + retain 6 years) ☐ No (continue to §4) |
| Was the PHI destroyed (paper PHI shredded/burned; electronic PHI cleared/purged/destroyed per NIST SP 800-88)? | ☐ Yes (PHI is "secured" → SAFE HARBOR) ☐ No (continue) |

If encryption/destruction safe harbor applies → **NO BREACH NOTIFICATION REQUIRED.** Document assessment + retain.

## 4. Four-factor risk assessment (§164.402(2))

Required when impermissible use/disclosure of unsecured PHI occurred. Each factor analysed; aggregate determines if LOW probability of compromise rebuts the presumption.

### 4.1 Factor 1 — Nature + extent of PHI involved

| Sub-factor | Detail | Risk increase contribution |
|---|---|---|
| Types of identifiers involved (name, SSN, DOB, address, account #, etc.) | | High / Med / Low |
| Categories of clinical info (diagnosis, treatment, medications, mental health, substance use, HIV/AIDS, reproductive health, genetic) | | |
| Particularly sensitive categories (§164.508(a)(2) psychotherapy notes; reproductive health post-2024 Final Rule; substance use 42 CFR Part 2) | | |
| Number of affected individuals | | |
| Possibility of re-identification of de-identified data | | |

**Factor 1 contribution to compromise probability:** ☐ Low ☐ Medium ☐ High

### 4.2 Factor 2 — Unauthorized person who used PHI or to whom disclosure made

| Sub-factor | Detail | Risk-contribution |
|---|---|---|
| Recipient identity known? | | |
| Recipient is another CE / BA bound by HIPAA? | ☐ Yes (lower risk per HHS Guidance) ☐ No | |
| Recipient is a public-facing party (general public, posted online) vs. internal-workforce (limited audience) | | |
| Recipient's ability to re-identify or aggregate the PHI? | | |
| Recipient's likely intent (malicious vs. accidental vs. legitimate-but-unauthorized) | | |

**Factor 2 contribution:** ☐ Low ☐ Medium ☐ High

### 4.3 Factor 3 — Whether the PHI was actually acquired or viewed

| Sub-factor | Detail | Risk-contribution |
|---|---|---|
| Forensic evidence of actual access (logs, screenshots, witness statements)? | | |
| Forensic evidence that access did NOT occur (e.g., file accessed = no per logs, despite vulnerability)? | | |
| Was data ever transmitted / received / downloaded? | | |
| For physical disclosures (lost/stolen device or paper) — recovered intact + forensically determined no access? | | |

**Factor 3 contribution:** ☐ Low ☐ Medium ☐ High

### 4.4 Factor 4 — Extent to which the risk to the PHI has been mitigated

| Sub-factor | Detail | Risk-reduction |
|---|---|---|
| Recipient destroyed/returned PHI + provided written attestation? | | |
| Recipient provided enforceable assurances of non-use/non-disclosure (e.g., signed confidentiality agreement)? | | |
| Recipient is HIPAA-bound + has its own breach obligations? | | |
| PHI access revoked + credentials rotated + accounts disabled? | | |
| Affected systems re-imaged + scanned + cleared? | | |
| Continuing-risk-management measures in place? | | |

**Factor 4 mitigation contribution:** ☐ Strong ☐ Moderate ☐ Weak

## 5. Aggregate determination

Based on the 4-factor analysis, determine probability that PHI has been compromised:

| Outcome | Decision |
|---|---|
| ☐ **LOW probability** of compromise — presumption rebutted; impermissible use/disclosure is NOT a reportable breach; documentation retained per §164.316(b)(2)(i) | No external notification; internal incident log + CAPA |
| ☐ **NOT LOW** probability of compromise — presumption of breach STANDS; this IS a reportable Breach; proceed to §6 notification | Proceed with §164.404 / §164.406 / §164.408 notifications |

**Rationale for determination** (detailed narrative tying analysis to outcome):

> [Document specifically how each factor was weighed + how aggregate determination reached. This narrative is CRITICAL — HHS OCR scrutinises 4-factor assessments + their rationales in investigations.]

## 6. Notification matrix (if breach confirmed)

### 6.1 Individual notification (§164.404)

| Item | Detail |
|---|---|
| Number of affected individuals | |
| Method | ☐ First-class mail to last-known address ☐ Email if individual agreed ☐ Substitute notice per §164.404(d)(2) if 10+ individuals' contact info insufficient |
| Substitute notice method | ☐ Posting on home page for 90 days OR major print/broadcast media |
| Content (per §164.404(c)) | (1) brief description of incident + date of breach + discovery; (2) types of PHI involved; (3) steps individual should take; (4) what we are doing to investigate + mitigate + protect; (5) contact info — toll-free + email + website + postal |
| Deadline | **60 calendar days** from discovery (CE clock) — §164.404(b) |
| Sent date | |

### 6.2 Media notice (§164.406) — if ≥500 residents of a state or jurisdiction

| Item | Detail |
|---|---|
| ≥500 residents of a state/jurisdiction affected? | ☐ Yes ☐ No |
| Prominent media outlets selected | |
| Content (same as individual notice) | |
| Issued date | |

### 6.3 HHS notification (§164.408)

| Item | Detail |
|---|---|
| Breach affecting ≥500 individuals — submit to HHS within 60 days at https://ocrportal.hhs.gov/ocr/breach/breach_form.jsf | ☐ Submitted (date) |
| Breach affecting <500 individuals — log + submit annually by March 1 covering prior calendar year | ☐ Logged for annual submission |

### 6.4 BA notification to CE (§164.410, when BA discovers)

| Item | Detail |
|---|---|
| BA discovery date | |
| BA notification to CE (within 60 days of BA discovery) | |
| BA notification content per §164.410(c) | ☐ Identification of affected individuals ☐ Description of breach ☐ All info necessary for CE to satisfy §164.404 |

## 7. CAPA + lessons learned

| Item | Detail |
|---|---|
| Root cause | |
| Preventive actions | |
| Corrective actions | |
| Process changes | |
| Training updates | |
| Policy updates | |
| Linked CAPA ID | |
| Linked HIPAA Risk Analysis update (per §164.308(a)(1)(ii)(A)) | |
| Post-incident review date | |

## 8. Approvals

| Role | Name | Signature | Date |
|---|---|---|---|
| Privacy Officer | | | |
| Security Officer | | | |
| Legal | | | |
| Senior management | | | |

---

**Trace evidence.** This breach risk assessment addresses HIPAA-164-400-414-breach-notification + HIPAA-164-530-administrative-requirements per `modules/hipaa/module.yaml`. HHS Guidance "Guidance to Render Unsecured Protected Health Information Unusable, Unreadable, or Indecipherable to Unauthorized Individuals" + HHS Breach Notification regulations + OCR "Breach Notification Rule" guidance supplementary.
