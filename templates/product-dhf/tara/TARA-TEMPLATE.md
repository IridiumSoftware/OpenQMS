---
document_id: TARA-XXX
title: "[Item Name] — Threat Analysis and Risk Assessment"
version: "1.0"
effective_date: YYYY-MM-DD
owner: "[Cybersecurity Engineering Lead, Title]"
status: draft
approved_by: "[Cybersecurity Manager + Confirmation Reviewer, Title]"
approval_date: YYYY-MM-DD
---

# TARA-XXX: [Item Name] Threat Analysis and Risk Assessment

Per ISO/SAE 21434:2021 §15. The TARA is the systematic identification of damage scenarios, threat scenarios, attack paths, rating of impact + attack feasibility, determination of cybersecurity risk, and assignment of Cybersecurity Assurance Level (CAL). It is the cyber-domain analog of HARA — it drives every downstream cybersecurity activity in the same way HARA drives functional safety.

For items in scope of UN R155 (cybersecurity type approval), the TARA must demonstrate coverage of the Annex 5 threat categories. Cross-reference with HARA-XXX is mandatory where cyber compromise could induce a functional-safety hazard (e.g., compromise of brake-by-wire ECU induces unintended deceleration / acceleration).

## 1. Item context

- **Item under analysis:** [name]
- **Linked Item Definition:** ITM-XXX
- **Linked HARA:** HARA-XXX (cross-reference for safety-impacting threats)
- **Linked Safety Concept:** SAFC-XXX
- **TARA scope:** [whole item / specific external interface / specific data flow]
- **Analysis team:** [enumerated; multi-disciplinary required — cyber engineering + functional safety + systems]
- **UN R155 in scope?** [Yes / No; if yes, Annex 5 coverage matrix in §9 below]

## 2. Asset identification

Enumerate the cybersecurity-relevant assets of the item. Assets are anything whose compromise of confidentiality, integrity, availability, or authenticity (CIA-A) could cause damage.

| Asset # | Asset | Type | Cybersecurity properties | Owner of damage |
|---|---|---|---|---|
| AS-1 | [name] | data / code / credential / key / signal / function / metadata | Confidentiality (C) / Integrity (I) / Availability (A) / Authenticity (Au) | Vehicle user / OEM / supplier / third party |

Typical asset categories:
- **External interfaces:** OBD-II port, telematics modem, infotainment USB, wireless interfaces (cellular, Wi-Fi, Bluetooth, V2X, NFC), charging interface.
- **In-vehicle communication:** CAN, CAN-FD, LIN, FlexRay, Automotive Ethernet, MOST.
- **Update process:** boot loader, SW package, signatures, OTA back-end interaction.
- **Vehicle data:** PII, location, biometrics, vehicle health data, diagnostic data.
- **Code:** firmware, application SW, configuration, calibration data.
- **User identity:** authentication credentials, keys (physical + cryptographic), digital identities.

## 3. Damage scenarios

For each asset, enumerate damage scenarios.

| DS # | Damage scenario | Asset compromised | Cybersecurity property violated | Consequence to whom |
|---|---|---|---|---|
| DS-1 | [scenario: attacker [action] causing [damage]] | AS-1 | C / I / A / Au | Vehicle occupants / other road users / OEM / fleet operator |

## 4. Impact rating

For each damage scenario, rate impact across four categories.

| DS # | Safety (S) | Financial (F) | Operational (O) | Privacy (P) | Overall impact rating |
|---|---|---|---|---|---|

### Impact rating scale (per ISO/SAE 21434 §15.5)

- **Severe** — Life-threatening / debilitating injuries (S); high financial loss (F); high operational impairment (O); highly sensitive personal information disclosed (P).
- **Major** — Light to moderate injuries (S); moderate financial loss (F); moderate operational impairment (O); sensitive personal information disclosed (P).
- **Moderate** — Minor injuries (S); minor financial loss (F); partial degradation of vehicle function (O); identifiable personal information (P).
- **Negligible** — No injuries (S); negligible loss (F); usability nuisance (O); non-sensitive data (P).

## 5. Threat scenarios + attack paths

For each damage scenario, enumerate the threat scenarios that could realize it, then the attack paths (sequences of actions) the attacker would take.

| TS # | Threat scenario | Realizes DS | Attack paths (AP) |
|---|---|---|---|
| TS-1 | [adversary [action] on [asset / interface] leading to [intermediate effect]] | DS-1 | AP-1.1: [step-by-step: gain initial access → escalate → reach asset → effect damage] |

Methods commonly used: STRIDE (Spoofing / Tampering / Repudiation / Information disclosure / Denial of service / Elevation of privilege); attack trees; threat libraries (CWE, ATT&CK for ICS / Automotive); kill chain.

## 6. Attack feasibility rating

For each attack path, rate feasibility per the chosen approach (ISO/SAE 21434 supports multiple — attack potential per ISO/IEC 18045; CVSS; attack vector).

| AP # | Elapsed time | Specialist expertise | Knowledge of item | Window of opportunity | Equipment | Feasibility rating |
|---|---|---|---|---|---|---|

### Attack feasibility scale

- **High** — Feasible with limited time + expertise + standard equipment + ready knowledge.
- **Medium** — Requires moderate time / specialist expertise / restricted knowledge / dedicated equipment.
- **Low** — Requires high time + expert team + secret knowledge + bespoke equipment.
- **Very low** — Conditions extremely improbable to combine in practice.

## 7. Risk determination

Risk = function(impact, feasibility). Per the chosen risk matrix.

| TS # | Impact | Attack feasibility | Risk level |
|---|---|---|---|

Typical risk levels: Critical / High / Medium / Low / Very low.

## 8. CAL assignment + risk treatment

CAL (Cybersecurity Assurance Level — CAL 1 / 2 / 3 / 4) is the analogue of ASIL for cybersecurity. Higher CAL → more rigorous cybersecurity engineering.

| TS # | CAL | Risk treatment | Decision | Cybersecurity Goal # |
|---|---|---|---|---|

### Risk treatment options
- **Avoid risk** — remove the asset, the interface, or the function.
- **Reduce risk** — implement controls to reduce impact or feasibility.
- **Share risk** — transfer to a third party (insurance, supplier).
- **Retain risk** — accept the residual risk (must be approved at appropriate level).

## 9. UN R155 Annex 5 coverage matrix (if applicable)

Required when this item is in scope of UN R155 type approval. Each Annex 5 threat category must be addressed by at least one cybersecurity goal + control or explicitly justified as not applicable.

| Annex 5 category | Threats | Addressed by | Status |
|---|---|---|---|
| 4.3.1 Back-end servers | [threats 1-3] | CG-X / control Y | Addressed / NA + rationale |
| 4.3.2 Vehicle communication channels | [threats 4-6] | | |
| 4.3.3 Update procedures | [threats 7-9] | | |
| 4.3.4 Unintended human actions | [threats 10-11] | | |
| 4.3.5 External connectivity + connections | [threats 12-15] | | |
| 4.3.6 Vehicle data + code | [threats 16-22] | | |
| 4.3.7 Potential vulnerabilities that could be exploited if not protected | [threats 23-32] | | |

## 10. Cybersecurity Goals

For each TS that requires treatment, derive a Cybersecurity Goal.

| CG # | Cybersecurity Goal | CAL | TS addressed | Linked Safety Goal (if interacts) |
|---|---|---|---|---|

CGs are refined into Cybersecurity Requirements in the Cybersecurity Concept (linked SAFC-XXX Part C or separate Cybersecurity Concept document).

## 11. Confirmation review

| Reviewer | Role | Date | Findings | Status |
|---|---|---|---|---|

## 12. Sign-off

| Role | Name | Date | Signature |
|---|---|---|---|
| Cybersecurity Engineering Lead | | | |
| Functional Safety Engineering Lead (cross-review for safety-impacting threats) | | | |
| Cybersecurity Manager | | | |
| Confirmation Reviewer | | | |

## 13. References

- ISO/SAE 21434:2021 §15 — Threat Analysis and Risk Assessment.
- ISO/SAE 21434:2021 §9 — Concept phase (Cybersecurity Goals + Concept).
- ISO/IEC 18045 — Vulnerability assessment (attack potential method).
- UN R155 Annex 5 — Threat categories (if applicable).
- HARA-XXX (cross-reference for safety-impacting threats).
- Linked: ITM-XXX, SAFC-XXX (Cybersecurity Concept section), Cybersecurity Case.

## 14. Revision history

| Version | Date | Author | Changes |
|---|---|---|---|
| 1.0 | YYYY-MM-DD | [Name] | Initial release. |
