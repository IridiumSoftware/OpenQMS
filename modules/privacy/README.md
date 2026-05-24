# Privacy (GDPR + CCPA/CPRA) — Open QMS cross-cutting overlay

24th Open QMS cross-cutting overlay. **Personal data protection** under the two dominant global privacy frameworks: EU GDPR (Regulation 2016/679) + US CCPA/CPRA (Cal. Civ. Code §1798.100-199).

Last major management-system gap in the Open QMS overlay set — universally applicable since virtually every adopter processes personal data (customers, employees, suppliers, clinical-trial subjects, complaint reporters, safety reporters).

## Scope

| Framework | Edition | Effective | License |
|---|---|---|---|
| EU GDPR | Regulation (EU) 2016/679 | 2018-05-25 | PUBLIC (EUR-Lex) |
| UK GDPR + Data Protection Act 2018 | Near-identical to EU GDPR, retained at Brexit | 2021-01-01 | PUBLIC (legislation.gov.uk) — addressed under EU GDPR clauses with UK ICO as supervisory authority |
| California CCPA + CPRA | Cal. Civ. Code §1798.100-199 | CCPA 2020-01-01; CPRA amendments 2023-01-01; CPPA final regs ADMT + Risk Assessment + Cybersecurity Audit 2025-2026 | PUBLIC (leginfo.legislature.ca.gov) |

21 clauses across the two frameworks.

## Clause breakdown

### GDPR (15 clauses)

**Principles + lawful bases (4):**
- Article 5 — Principles (lawfulness + purpose limitation + minimisation + accuracy + storage limitation + integrity + accountability)
- Article 6 — Lawful bases (6 options)
- Article 7 — Conditions for consent
- Article 9 — Special categories

**Data subject rights (3):**
- Article 12 — Modalities
- Articles 13-14 — Information at collection
- Articles 15-22 — Substantive rights (access / rectification / erasure / restriction / portability / object / automated decision-making)

**Controller + processor obligations (4):**
- Article 25 — Data protection by design + default
- Article 28 — Processor + DPA
- Article 30 — ROPA
- Article 32 — Security

**Breach + DPIA + DPO + international (4):**
- Articles 33-34 — Breach notification (72-hour SA + without undue delay to subjects)
- Article 35 — DPIA
- Articles 37-39 — DPO
- Articles 44-49 — International transfers (incl. Schrems II considerations)

### CCPA/CPRA (6 clauses)

**Consumer rights (6):**
- §1798.100/110/115 — Right to know
- §1798.105 — Right to delete
- §1798.106 — Right to correct (CPRA)
- §1798.120/135 — Opt-out of sale + sharing (+ GPC signal honoring per CPPA §7025)
- §1798.121 — Right to limit use of SPI
- §1798.130 — Methods + response deadlines

**Business obligations (4):**
- §1798.135 + CPPA §7012 — Notice at collection
- §1798.140 + CPPA §7050-7053 — Service Provider / Contractor / Third Party classification
- §1798.150 — Private right of action for data breach
- §1798.185 — CPPA regulatory regime (ADMT + Risk Assessment + Cybersecurity Audit)

## Templates introduced

5 new privacy-specific templates:

1. **`PRIVACY-POLICY-TEMPLATE.md`** — Public-facing policy covering GDPR Articles 13-14 information + CCPA notice-at-collection in one document. Includes the 11 CCPA personal-information categories (A-K + SPI L) table, GDPR Article 6 lawful-basis-per-purpose grid, special-category / SPI handling, CCPA + GDPR rights, Global Privacy Control honoring, international transfer disclosure, cookies + tracking, children's privacy, dispute channels with supervisory-authority + state-AG contacts.

2. **`DPA-TEMPLATE.md`** — Multi-regime Data Processing Agreement covering GDPR Article 28 required content + CCPA §1798.140 service-provider/contractor/third-party classification per CPPA §7050-7053 + 2021/915 SCC reference + Schrems II Transfer Impact Assessment + sub-processor authorisation modes + audit rights (with SOC 2 / ISO 27001 / ISO 27701 acceptable-attestation alternatives) + breach 24-hour notification SLA + deletion/return at termination + CPPA Cybersecurity Audit + Risk Assessment + ADMT assistance.

3. **`DPIA-TEMPLATE.md`** — GDPR Article 35 DPIA + CCPA Risk Assessment per CPPA §7150-7157. Threshold assessment (Article 35(3) automatic triggers + lead SA positive/negative list + EDPB WP248 rev.01 9-criteria scoring + CCPA Risk Assessment triggers) + systematic description (nature / scope / context / purposes) + necessity + proportionality + risk assessment (per WP250 + EDPB Guidelines 4/2019 consequence categories with likelihood × severity) + measures (Article 25 by-design + Article 32 security) + DPO + data subject consultation + decision (proceed / with conditions / Article 36 prior consultation / not proceed).

4. **`ROPA-TEMPLATE.md`** — GDPR Article 30 Records of Processing Activities. Part A controller variant (all 7 required fields per 30(1)(a)-(g) + supplementary metadata) + Part B processor variant (all 4 required fields per 30(2)(a)-(d)). Maintenance discipline table mapping triggering events (new purpose / modified purpose / retirement / new recipient / retention change / Article 32 measure change / annual review / SA request) to ROPA actions.

5. **`PERSONAL-DATA-BREACH-NOTIFICATION-TEMPLATE.md`** — Multi-regime breach record covering GDPR Article 33 (72-hour SA notification) + Article 34 (data subject notification when high risk) + Article 33(5) documentation obligation (records retained even when notification not required) + CCPA §1798.150 documented incident record + US state AG breach notification cross-reference (Cal. Civ. Code §1798.82, TX/NY/FL/IL state laws) + HIPAA Breach Notification Rule + FTC Health Breach Notification Rule + SEC Item 1.05 8-K for material cybersecurity incidents at US-public-company controllers. CIA-triad classification + cause categorisation + encryption/pseudonymisation state (which determines Article 34(3)(a) exemption + CCPA §1798.150 private-action exposure) + WP250 consequence-category risk assessment + notification decision matrix per regime + Article 33(5) Article 33(3) info elements.

Plus 1 cross-cutting binding (SOP-TEMPLATE) for privacy operational SOPs (consent management + DSR intake + DPO escalation + identity verification per CPPA §7060-7064 3-2-1 tier model + transfer impact assessment per Schrems II).

## Composition

Composes with ANY vertical. Particularly natural compositions:

- **`<any vertical> + privacy`** — universal baseline; every adopter processes personal data
- **`medical-devices + privacy`** — patient data, complainant data, clinician identifiers
- **`pharma + privacy`** — clinical trial subject data (special category Article 9 health), pharmacovigilance, named-patient programs
- **`food-safety + privacy`** — consumer complaints, recall customer notifications, food-allergy disclosures
- **`automotive + privacy`** — telematics, infotainment, EV charging, ADAS data
- **`chemicals + privacy`** — workforce exposure monitoring data, downstream-user contact data
- **`privacy + iso-27001`** — privacy is the WHY; ISO 27001 is the HOW for technical+organisational measures (Article 32 maps directly to Annex A controls)
- **`privacy + soc-2`** — SOC 2 Privacy criterion overlaps; this overlay adds the legal-framework specificity
- **`privacy + hitrust-csf`** — HITRUST already maps to HIPAA + GDPR + CCPA internally; privacy overlay sits alongside, not subsumed
- **`privacy + regulated-ai`** — GDPR Article 22 + CCPA ADMT regulations both govern automated decision-making with significant effect
- **`privacy + recall-workflow`** — recall customer notifications process personal data; breach + recall workflows often coordinate

## When to use + when NOT to use

**Use when:**
- ANY processing of personal data of EU/EEA/UK/Swiss residents
- ANY processing of personal data of California consumers AND business meets one of the CCPA thresholds ($25M revenue / 100k consumers/households / 50% revenue from sale of PI)
- Any organisation operating ANY public-facing service (privacy policy is universally required)

**Do not use when:**
- Pure B2B service with no consumer personal data + no employee data crosses jurisdictions (rare; usually still applies to employee personal data)
- Genuinely zero personal data processing (very rare)

## Forward work

- **UK GDPR specialist overlay** — UK ICO-specific guidance + UK IDTA for transfers (currently covered under EU GDPR; specialisation forward)
- **PIPEDA (Canada)** standalone overlay
- **LGPD (Brazil)** standalone overlay
- **APPI (Japan)** standalone overlay
- **PIPL (China)** standalone overlay — including cross-border data transfer assessment via CAC
- **State privacy overlays** — Virginia VCDPA / Colorado CPA / Connecticut CTDPA / Utah UCPA / Texas TDPSA / Oregon OCPA / Montana MCDPA / Iowa ICDPA / Florida FDBR / Delaware DPDPA / New Jersey NJDPA / Tennessee TIPA / Indiana INCDPA / New Hampshire NHPA — most follow VCDPA template; could ship as single `us-state-privacy` overlay with variations
- **HIPAA** dedicated overlay — covers covered entities + business associates; protected health information; HHS OCR enforcement; coordinates with privacy overlay for non-HIPAA data
- **GLBA Safeguards Rule** — financial-services-specific
- **COPPA** — children under 13 in the US
- **FERPA** — education records
- **EU ePrivacy** standalone (cookies + tracking; awaiting ePrivacy Regulation finalisation)
- **CCPA ADMT regulations** sub-overlay once final (currently embedded in §1798.185 reference)
- **Cybersecurity Audit regulations** sub-overlay once final
- **Risk Assessment regulations** sub-overlay once final
- **DSR Workflow** issue templates (GitHub-native consumer request intake — analog to complaint.yml + supplier-evaluation.yml)
- **TIA (Transfer Impact Assessment)** standalone template per Schrems II
- **Cookie banner content standards** template per EDPB Guidelines 03/2022
- **DPO appointment letter** template per Article 37
- **Article 27 EU representative appointment** template

## Standards licensing

Both GDPR + CCPA are PUBLIC. Supplementary EDPB guidelines (WP248 rev.01 DPIA + WP250 breach + Guidelines 07/2019 processor + 07/2020 controller-processor + 03/2022 cookies + 4/2019 DPIA + 9/2022 breach examples) all PUBLIC (edpb.europa.eu). CPPA regulations PUBLIC (cppa.ca.gov). SCCs (2021/915 + UK IDTA) PUBLIC.

Meaningful adopter cost reduction — comprehensive privacy compliance achievable at zero standards-licensing cost.
