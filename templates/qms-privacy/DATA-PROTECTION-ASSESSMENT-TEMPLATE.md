---
document_id: PRIV-DPA-US-XXX
version: "1.0"
effective_date: YYYY-MM-DD
owner: "[Privacy Officer / DPO]"
status: draft
---

# Data Protection Assessment (US State Privacy)

**Template for:** Data Protection Assessment (DPA) required by US state comprehensive privacy laws (VCDPA template). Parallel to GDPR DPIA + CCPA Risk Assessment; ONE assessment may satisfy multiple regimes when scope overlaps.
**Trigger:** Processing presents heightened risk of harm including: (a) targeted advertising; (b) sale of personal data; (c) processing sensitive data; (d) profiling presenting reasonably foreseeable risk of (i) unfair/deceptive/discriminatory treatment, (ii) financial / physical / reputational injury, (iii) physical/intrusion-of-privacy, (iv) other substantial injury; (e) processing personal data of children.
**Retention:** Maintained + available to state AG on request. Per CLAUDE.md analog to GDPR Article 35 DPIA retention.

---

## 1. Identification

| Field | Value |
|---|---|
| Assessment reference | |
| Project / processing activity name | |
| Assessment version | |
| Assessment date | |
| Last review date | |
| Next review due | |
| Assessor + qualifications | |
| Business owner | |
| Privacy Officer review | |
| Legal review | |
| Senior management approval | |
| States in scope (per US-STATE-PRIVACY-MATRIX) | |
| Coordinated with GDPR DPIA? (single-assessment-multi-regime) | |
| Coordinated with CCPA Risk Assessment? | |

## 2. Heightened-risk trigger determination

Check all applicable triggers — if any apply, DPA required:

| Trigger | Applicable? | States imposing this trigger |
|---|---|---|
| (a) Targeted advertising | ☐ | All VCDPA-template states; Florida FDBR; Maryland MODPA |
| (b) Sale of personal data | ☐ | All states (Maryland MODPA bans sale of sensitive data outright) |
| (c) Processing sensitive data | ☐ | All states (per-state sensitive-data scope varies) |
| (d) Profiling for legal/significant decisions | ☐ | All states |
| (e) Children's data | ☐ | All states (Maryland MODPA bans targeted ads to under-18) |

**DPA required?** ☐ Yes — proceed ☐ No — document non-applicability + retain

## 3. Processing description

### 3.1 Nature

| Field | Value |
|---|---|
| Processing operations (collect / record / store / use / disclose / transmit / combine / erase) | |
| Technologies used | |
| Geographic locations | |
| Sources of data | |
| Recipients / destinations | |
| Cross-state data flows (relevant for per-state risk assessment) | |

### 3.2 Scope

| Field | Value |
|---|---|
| Categories of consumers | |
| Approximate number per state | |
| Categories of personal data | |
| Sensitive data categories (per most-restrictive state in scope) | |
| Children's data scope (per under-13 COPPA + under-16 GDPR + under-18 Maryland MODPA) | |
| Volume of records per consumer | |
| Retention period | |

### 3.3 Context

| Field | Value |
|---|---|
| Source of data (collected directly / from third party / public) | |
| Relationship with consumers | |
| Reasonable expectations (per industry norms + prior disclosures) | |
| Power imbalance considerations | |
| Sensitivity of context (e.g., healthcare / financial / children) | |
| Public visibility / brand reputation | |

### 3.4 Purposes

| Purpose | Description | Lawful purpose category | Sensitive-data condition (where applicable) |
|---|---|---|---|

## 4. Benefits + risks assessment

### 4.1 Direct + indirect benefits

| Beneficiary | Benefit | Materiality |
|---|---|---|
| Consumer | | |
| Controller | | |
| Public interest | | |
| Third parties | | |

### 4.2 Risks to consumer rights + freedoms

| # | Risk | Affected consumers | Likelihood (Low/Med/High) | Severity (Low/Med/High) | Overall | Considerations specific to state-law context |
|---|---|---|---|---|---|---|
| 1 | Unfair / deceptive / discriminatory treatment | | | | | |
| 2 | Financial injury | | | | | |
| 3 | Physical injury | | | | | |
| 4 | Reputational injury | | | | | |
| 5 | Physical/intrusion of privacy | | | | | |
| 6 | Other substantial injury | | | | | |
| 7 | Unauthorized access / data breach | | | | | |
| 8 | Function creep / use beyond stated purpose | | | | | |
| 9 | Inaccurate or outdated data leading to wrong decisions | | | | | |
| 10 | Children-specific risks (targeted advertising / behavioral profiling) | | | | | |

### 4.3 Maryland MODPA-specific data-minimization assessment

If Maryland in scope AND processing sensitive data:

| Item | Detail |
|---|---|
| Is the sensitive data processing "strictly necessary" for the disclosed purpose? | ☐ Yes — specific necessity rationale: ☐ No → modify processing |
| Could less-intrusive alternative achieve the purpose? | |
| Documented rationale supports strict-necessity conclusion? | ☐ Yes (attached) |

### 4.4 Florida FDBR scope check (if applicable)

| Item | Detail |
|---|---|
| Organisation meets FDBR threshold per US-STATE-PRIVACY-MATRIX? | ☐ Yes ☐ No (FDBR out of scope; skip) |
| If yes — sale of sensitive data specific opt-out implemented? | |

## 5. Safeguards + risk-mitigation measures

| # (matches §4.2) | Mitigation | Type (technical / organisational / contractual) | Owner | Implementation date | Residual risk level |
|---|---|---|---|---|---|

### 5.1 Required common safeguards

- ☐ Data minimization (collection limited to adequate + relevant + reasonably necessary)
- ☐ Purpose limitation (no incompatible secondary use)
- ☐ Reasonable security per Article 32-equivalent
- ☐ Vendor (processor) DPA contracts in place
- ☐ Sub-processor flow-down
- ☐ UOOM (GPC) honoring where state requires
- ☐ Right-to-opt-out back-end propagation (sale + targeted advertising + profiling)
- ☐ Right-to-appeal mechanism (state-specific)
- ☐ Identity verification proportionate to request sensitivity
- ☐ Children's data parental-consent mechanism where applicable
- ☐ Non-discrimination policy for consumers exercising rights
- ☐ Consumer-rights response within state-specific deadline (45-90 days)

### 5.2 Sensitive-data specific safeguards

- ☐ Consent capture pre-processing (where state requires consent for sensitive data)
- ☐ Maryland MODPA strict-necessity assessment documented
- ☐ Targeted-advertising opt-out (and Maryland under-18 absolute prohibition)
- ☐ Sensitive-data segregation from non-sensitive
- ☐ Sale-of-sensitive-data prohibition (Maryland; Florida)

## 6. Risk-benefit balance

| Outcome | Decision |
|---|---|
| ☐ Benefits substantially outweigh residual risks → proceed | |
| ☐ Benefits + risks roughly balanced; additional safeguards reduce residual risk → proceed with conditions | |
| ☐ Residual risks substantially outweigh benefits → DO NOT proceed |

### 6.1 Conditions if proceeding with conditions

| Condition | Owner | Verification date |
|---|---|---|

### 6.2 Re-assessment triggers

- New state law effective date affecting scope
- Material change to processing purpose / scope / data types
- New sensitive data category
- Vendor / processor change
- Incident or breach affecting this processing
- AG inquiry or settlement affecting this processing
- Annual review

## 7. Approvals

| Role | Name | Signature | Date |
|---|---|---|---|
| Assessor | | | |
| Privacy Officer / DPO | | | |
| US privacy counsel | | | |
| Business owner | | | |
| Senior management approver | | | |

---

**Trace evidence.** This Data Protection Assessment addresses USP-data-protection-assessment-DPA-state + USP-controller-obligations per `modules/us-state-privacy/module.yaml`. Coordinated with GDPR DPIA template + CCPA Risk Assessment (per CPPA §7150-7157 final) when those regimes also apply — same risk assessment may satisfy multiple state regimes when scope properly cross-referenced.
