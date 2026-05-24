---
document_id: CLP-XXX
title: "[Substance or Mixture Name] — CLP Classification Notification + Label"
version: "1.0"
effective_date: YYYY-MM-DD
owner: "[Regulatory Affairs / Product Stewardship Lead]"
status: draft
approved_by: "[Regulatory Affairs Director]"
notified_to: "ECHA Classification and Labelling Inventory via REACH-IT (per CLP Article 13)"
notification_date: YYYY-MM-DD
---

# CLP-XXX: CLP Classification Notification + Label for [Substance/Mixture]

Per **EU CLP Regulation (EC) 1272/2008** Article 4 (self-classification) + Article 13 (C&L Inventory notification) + Article 17 + Annex II (label content) + Annex VIII (UFI requirements for mixtures classified for health or physical hazards).

CLP is the EU implementation of UN GHS. Notification to the ECHA C&L Inventory is required for:
- All substances subject to REACH registration
- All substances classified as hazardous + placed on EU market regardless of tonnage
- Mixtures classified as hazardous (via UFI per Annex VIII)

## 1. Substance / mixture identification

- **Trade name(s):** [list]
- **For substance:** IUPAC name + CAS # + EC # + REACH registration #
- **For mixture:** components ≥1% w/w identified (≥0.1% for SVHC/CMR/PBT); **UFI** (Unique Formula Identifier) per Annex VIII
- **Notifier:** legal entity name + ECHA legal-entity ID + address

## 2. Classification per CLP

### 2.1 Physical hazards

| Class | Category | Hazard statement (H-code) | Source data |
|---|---|---|---|
| Explosives | Div 1.1-1.6 / Unstable explosive | H200-H205 | |
| Flammable gases | Cat 1A / 1B / 2 | H220-H221 | |
| Flammable aerosols | Cat 1 / 2 | H222-H223 | |
| Oxidising gases | Cat 1 | H270 | |
| Gases under pressure | Compressed / Liquefied / Refrigerated / Dissolved | H280-H281 | |
| Flammable liquids | Cat 1-4 | H224-H227 | |
| Flammable solids | Cat 1 / 2 | H228 | |
| Self-reactive | Type A-G | H240-H242 | |
| Pyrophoric liquids | Cat 1 | H250 | |
| Pyrophoric solids | Cat 1 | H250 | |
| Self-heating | Cat 1 / 2 | H251-H252 | |
| Substances + mixtures emitting flammable gases in contact with water | Cat 1-3 | H260-H261 | |
| Oxidising liquids / solids | Cat 1-3 | H271-H272 | |
| Organic peroxides | Type A-G | H240-H242 | |
| Corrosive to metals | Cat 1 | H290 | |
| Desensitised explosives | Cat 1-4 | H206-H209 | |

### 2.2 Health hazards

| Class | Category | H-code | Source |
|---|---|---|---|
| Acute toxicity (oral/dermal/inhalation) | Cat 1-4 | H300-H332 | |
| Skin corrosion / irritation | Cat 1A/1B/1C / Cat 2 | H314/H315 | |
| Eye damage / irritation | Cat 1 / Cat 2 | H318/H319 | |
| Respiratory / skin sensitisation | Cat 1A/1B | H334/H317 | |
| Germ-cell mutagenicity | Cat 1A/1B/2 | H340-H341 | |
| Carcinogenicity | Cat 1A/1B/2 | H350-H351 | |
| Reproductive toxicity | Cat 1A/1B/2 + lactation | H360-H362 | |
| STOT single exposure | Cat 1/2/3 | H370-H336 | |
| STOT repeated exposure | Cat 1/2 | H372-H373 | |
| Aspiration hazard | Cat 1 | H304 | |

### 2.3 Environmental hazards

| Class | Category | H-code | Source |
|---|---|---|---|
| Hazardous to aquatic environment (acute) | Cat 1 | H400 | |
| Hazardous to aquatic environment (chronic) | Cat 1-4 | H410-H413 | |
| Hazardous to ozone layer | Cat 1 | H420 | |

### 2.4 EU-additional supplementary information

EUH-statements (EU-specific; not GHS): EUH014 reacts violently with water; EUH029 contact with water liberates toxic gas; EUH066 repeated exposure may cause skin dryness; EUH070 toxic by eye contact; EUH201 contains lead; EUH202 cyanoacrylate danger bonds skin + eyes; EUH204 contains isocyanates; EUH208 contains [sensitising substance name].

### 2.5 Harmonised classification (Annex VI of CLP)

If the substance has a CLH (harmonised classification) entry in CLP Annex VI Table 3, that classification **is mandatory** for all suppliers + supersedes self-classification for the listed hazard endpoints.

- **CLH entry:** [Annex VI Index No. + classification] OR "No CLH entry — full self-classification"

## 3. Label content (CLP Article 17 + Annex II)

The label on the container shall include in the language(s) of the Member State(s) where placed on the market:

- **Supplier name + address + phone number**
- **Nominal quantity** (where placed on market for general public; per Annex III)
- **Product identifier** (per Article 18 — trade name + substance identity for substances; trade name + identity of components contributing to classification for mixtures)
- **UFI** (mixtures classified for health/physical hazards — Annex VIII)
- **Hazard pictograms** (Annex V — GHS pictograms in EU red-border format)
- **Signal word**: "Danger" or "Warning" per most severe hazard
- **Hazard statements (H + EUH)**
- **Precautionary statements (P)** — selected per Annex IV; max 6 typical unless additional needed
- **Supplemental information (EUH supplemental)**

### Label preview (text representation)

```
[Pictograms — e.g., GHS02 Flame + GHS07 Exclamation]

[SIGNAL WORD — e.g., DANGER]

[Product identifier]
[UFI: XXXX-XXXX-XXXX-XXXX]

[H-statements concatenated]
- H225: Highly flammable liquid and vapour.
- H319: Causes serious eye irritation.

[P-statements concatenated]
- P210: Keep away from heat / sparks / open flames / hot surfaces. No smoking.
- P233: Keep container tightly closed.
- P280: Wear protective gloves / protective clothing / eye protection / face protection.
- P305+P351+P338: IF IN EYES: Rinse cautiously with water for several minutes. Remove contact lenses, if present and easy to do. Continue rinsing.

[Supplier name + address + phone]
[Nominal quantity if to general public]
```

## 4. UFI generation (mixtures only — Annex VIII)

The Unique Formula Identifier is a 16-character alphanumeric code generated from:
- The mixture composition (specifically the VAT number of the formulator + the formulator's mixture-specific code)
- Generated via ECHA's UFI Generator OR the open-source `python-ufi` library

UFI appears on:
- Product label
- Poison-centre notification submission (per Annex VIII)

UFI changes when mixture composition changes outside the permitted variability ranges (per Annex VIII §1.4).

## 5. Poison-centre notification (Annex VIII)

For hazardous mixtures placed on EU market, a **harmonised submission** to the appointed body (poison centres) per Member State is required via the ECHA Poison Centres Notification Portal (PCN Portal). Contents include:
- Mixture composition (full disclosure to poison centres; commercial-confidentiality protected)
- UFI
- Toxicological information
- Product category per EuPCS (European product categorisation system)

Compliance dates staged: consumer use → effective 2021; professional use → effective 2021; industrial use → effective 2024.

## 6. C&L Inventory notification (CLP Article 13)

For each substance, notification to ECHA C&L Inventory via REACH-IT containing:
- Substance identity + CAS + EC + IUPAC
- Notifier identity + ECHA legal-entity ID
- Classification + labelling (as per §2 above)
- Reason for differing from a previously-submitted notification if applicable

Multiple notifiers for same substance encouraged to harmonise classification via REACH-IT joint-notification mechanism.

## 7. Update triggers

Re-notification + label update required on:
- New hazard information becoming available
- Reclassification due to harmonised classification (Annex VI) addition
- New SVHC listing affecting the substance
- Restriction (Annex XVII) imposed
- Composition change for mixtures triggering UFI change
- New precautionary statement guidance

## 8. Sign-off

| Role | Name | Date | Signature |
|---|---|---|---|
| Regulatory Affairs Lead | | | |
| Toxicologist (Section 2 classification review) | | | |
| Ecotoxicologist (environmental hazards classification) | | | |
| Translator(s) for each Member State language | | | |
| QA approver | | | |

## 9. References

- EU CLP Regulation (EC) 1272/2008 — Articles 4, 13, 17, 18; Annexes I, II, III, IV, V, VI, VIII.
- ECHA Guidance on Labelling and Packaging.
- ECHA Guidance on Information Requirements and Chemical Safety Assessment.
- UN GHS Rev. 10 — basis for CLP classification.
- ECHA C&L Inventory + Poison Centres Notification Portal.
- Linked: SDS-XXX (Section 2 classification + Section 15 regulatory info derive from this CLP-XXX), REACH-DOSSIER-XXX, poison-centre PCN submission.

## 10. Revision history

| Version | Date | Author | Changes |
|---|---|---|---|
| 1.0 | YYYY-MM-DD | [Name] | Initial release. |
