---
document_id: HIPAA-RRL-XXX
version: "1.0"
effective_date: YYYY-MM-DD
owner: "[Privacy Officer]"
status: draft
---

# HIPAA Restriction Request Log

**Template for:** HIPAA Privacy Rule §164.522(a) restriction request handling. Individuals have the right to request restrictions on uses/disclosures of their PHI for TPO + uses/disclosures to persons involved in their care.
**CE response options:** CE is **not generally required to agree** EXCEPT for the **HITECH §13405(a) mandatory restriction**: when individual pays out-of-pocket in full for an item or service AND requests restriction of disclosure to health plan for payment/operations purposes — CE MUST agree.
**Documentation:** Log all requests received + responses + any agreed-restrictions in effect; 6-year retention per §164.316 + §164.530(j).

---

## 1. Request intake log

One entry per request. Maintain ongoing.

| # | Date received | Individual name + MRN | Request method (written / online / in-person) | Identity verified? | Type of request (see §2 below) | Decision (Agree / Deny) | Decision date | Decision reason | In-effect tracking link |
|---|---|---|---|---|---|---|---|---|---|
| 1 | | | | ☐ | | | | | |
| 2 | | | | ☐ | | | | | |

## 2. Request type categories

### 2.1 Permissive restrictions (§164.522(a)(1)(i))

Individual may request restriction of CE's use or disclosure of PHI for:
- (A) TPO purposes per §164.506 — CE is **NOT REQUIRED** to agree
- (B) Disclosures to persons involved in individual's care or payment per §164.510(b) — CE is **NOT REQUIRED** to agree

If CE agrees, CE must comply with the restriction EXCEPT (i) for emergency treatment use to provide care to individual, AND (ii) restriction does not affect disclosures required for breach notification per Subpart D, OR (iii) HHS-required disclosures, OR (iv) other disclosures permitted under §164.502(a)(2) (required disclosures).

### 2.2 MANDATORY restriction (§164.522(a)(1)(vi) — HITECH §13405(a))

Individual request:
1. Individual pays out-of-pocket in FULL for a healthcare item or service
2. Individual requests restriction of disclosure of PHI to their HEALTH PLAN
3. Disclosure is for PAYMENT or HEALTHCARE OPERATIONS purposes (NOT for treatment)
4. Disclosure is NOT otherwise required by law

→ CE **MUST AGREE** to the restriction per HITECH §13405(a).

Operational implications:
- Provider segregates patient + service from claim submission
- Provider does not bill insurance for the item/service
- Provider tracks the out-of-pocket payment + corresponding restriction internally
- Any subsequent collection efforts must not involve the health plan disclosure

## 3. Detail per request — request #[N]

| Field | Value |
|---|---|
| Internal request ID | |
| Individual name + MRN | |
| Request date | |
| Identity verification method + date | |
| Request type (per §2 above) | ☐ Permissive (§164.522(a)(1)(i)(A) TPO) ☐ Permissive (§164.522(a)(1)(i)(B) §510(b) involvement) ☐ **MANDATORY** (§164.522(a)(1)(vi) HITECH out-of-pocket) |
| Specific PHI in scope | |
| Specific use/disclosure to be restricted | |
| Specific recipient(s) to be restricted from | |
| Effective period (start + end OR until terminated) | |
| Individual's payment-in-full confirmation (if mandatory restriction) | ☐ Receipt date + amount + service description |

## 4. Decision

| Field | Value |
|---|---|
| Decision | ☐ Agree ☐ Deny (only valid for permissive; mandatory MUST agree) |
| Decision date | |
| Decision rationale (operational feasibility / clinical concerns / mandatory-per-HITECH) | |
| If denied — written explanation to individual (recommended; not strictly required for permissive denials but best practice) | |
| If agreed — operational scope documented (who needs to know; system flags set; staff training notification) | |

## 5. In-effect restrictions registry

Active restrictions tracked in dedicated registry for ongoing enforcement.

| # | Individual MRN | Restriction type | Effective from | Effective through (or "until terminated") | Specific scope | Systems flagged | Staff notified | Termination event | Termination date |
|---|---|---|---|---|---|---|---|---|---|
| | | | | | | ☐ EHR ☐ Billing ☐ Other | | | |

## 6. Termination of restriction (§164.522(a)(2))

Either party may terminate a permissive restriction:

| Field | Value |
|---|---|
| Termination initiated by | ☐ Individual ☐ CE |
| If by individual — written or oral agreement | (oral termination — document; CE should request written confirmation) |
| If by CE — written notice required (CE may terminate); termination effective only for PHI created or received AFTER notice | |
| Notice date | |
| Effective date | |
| Pre-termination PHI continues under restriction | ☐ Yes |
| Post-termination PHI not subject | ☐ Yes |

**MANDATORY restrictions per HITECH §13405(a) — generally cannot be unilaterally terminated by CE.** Individual may rescind; CE must continue compliance for the restricted disclosure regardless of subsequent payment status.

## 7. Confidential communications (§164.522(b)) — distinct right, often co-administered

Distinct right from restriction: individual may request that CE communicate with them about PHI by alternative means (e.g., phone not mail) or alternative locations (e.g., work address not home).

CE must accommodate REASONABLE requests. For health plans, may require written request with statement that disclosure of all or part of the PHI could endanger the individual.

Log confidential-communication requests in separate table or combined registry:

| # | Date | Individual MRN | Alternative method requested | Alternative location requested | Reasonable accommodation? | Decision | Effective | Termination |
|---|---|---|---|---|---|---|---|---|
| | | | | | ☐ | | | |

## 8. Recordkeeping (§164.530(j))

| Field | Value |
|---|---|
| Request retention | 6 years from later of created date or last in effect |
| Decision retention | 6 years |
| Termination record retention | 6 years |
| Storage location | |
| Custodian | |
| Audit log of restriction-enforcement actions (e.g., refusals to disclose under restriction) | |

## 9. Approvals

| Role | Name | Signature | Date |
|---|---|---|---|
| Privacy Officer (request approval) | | | |
| Operations / Billing lead (if mandatory restriction — segregation of payment) | | | |
| Compliance review | | | |

---

**Trace evidence.** This Restriction Request log addresses HIPAA-164-520-528-individual-rights + HIPAA-164-530-administrative-requirements per `modules/hipaa/module.yaml`. HHS Privacy Rule guidance on §164.522 + HITECH §13405(a) mandatory restriction guidance supplementary. Critical that **mandatory out-of-pocket restrictions** are operationalised in the billing system — adopter failure to enforce these triggers OCR enforcement.
