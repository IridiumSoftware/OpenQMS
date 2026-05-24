# Chemicals — Open QMS vertical module

7th Open QMS vertical (after medical-devices, aerospace, automotive, manufacturing, pharma, food-safety). Covers **chemical substance + mixture manufacturing + import** under EU REACH + EU CLP + UN GHS + OECD GLP + US TSCA regulatory frameworks.

## Scope

Chemical industry — industrial chemicals, formulators, distributors. Also applies to **importers of chemicals into the EU** (REACH-Only Representative model for non-EU manufacturers placing substances on the EU market).

## Standards covered

**All 5 PUBLIC license** — meaningful adopter cost reduction for chemical-industry startups + SMEs + academic spinouts:

- **EU REACH** (Regulation (EC) 1907/2006) — Registration, Evaluation, Authorisation, and Restriction of Chemicals
- **EU CLP** (Regulation (EC) 1272/2008) — Classification, Labelling, Packaging (EU implementation of UN GHS)
- **UN GHS Rev. 10** (2023) — Globally Harmonized System of Classification and Labelling of Chemicals
- **OECD GLP Principles** — Good Laboratory Practice for non-clinical safety studies (ENV/MC/CHEM(98)17, 1997 as revised)
- **US TSCA** (15 USC §2601 et seq.; 40 CFR Parts 700-799) — Toxic Substances Control Act with 2016 Lautenberg amendments

21 clauses across the 5 standards.

## Templates introduced

4 new chemical-industry-specific templates:

- **`templates/product-chemicals/sds/SAFETY-DATA-SHEET-TEMPLATE.md`** — 16-section SDS per GHS Rev. 10 + EU REACH Annex II + EU CLP + OSHA HCS Appendix D. Foundational risk-communication artifact. Update triggers per REACH Article 31(9) (new hazard info / new SVHC listing / authorisation / restriction / exposure scenario update).

- **`templates/product-chemicals/reach/REACH-REGISTRATION-DOSSIER-TEMPLATE.md`** — REACH Article 10 + Annex VI structure + tonnage-band-specific information per Annexes VII-X + Annex I Chemical Safety Report (CSR) for substances ≥10 t/y. Covers joint submission via SIEF + IUCLID 6 dossier preparation + REACH-IT submission + post-submission update obligations + SVHC/Authorisation/Restriction considerations.

- **`templates/product-chemicals/clp/CLP-NOTIFICATION-LABEL-TEMPLATE.md`** — CLP Article 13 C&L Inventory notification + Article 17 label per Annex II + UFI + Poison Centre Notification per Annex VIII. Full classification tables across all GHS hazard classes (physical / health / environmental) + EUH supplementary statements + Annex VI CLH harmonised classification.

- **`templates/product-chemicals/glp/GLP-STUDY-PLAN-REPORT-TEMPLATE.md`** — Combined Study Plan + Final Report per OECD GLP Principles 8.1 + 9.1. QA Programme Statement per Principle 9.1(j). Archive per Principle 9.2 (minimum 10-year retention typical for chemical industry).

## What is intentionally NOT in scope

- **OSHA HCS** (29 CFR 1910.1200) — US workplace HazCom; cross-cutting workplace health-and-safety (partially covered by iso-45001 overlay).
- **DOT HazMat** (49 CFR Parts 100-185) + IMDG + IATA + ADR/RID — transport classifications. Standalone overlay forward.
- **Pesticides** — FIFRA (US) + EU Plant Protection Products Regulation 1107/2009. Separate regulatory framework.
- **Cosmetics** — EU Cosmetic Regulation 1223/2009 + US MoCRA. Separate vertical (cosmetics).
- **Biocides** — EU Biocidal Products Regulation 528/2012.
- **Detergents** — EU Detergent Regulation 648/2004.

## Composition with overlays

Composes cleanly with:

- **`iso-27001`** — chemical companies handle customer proprietary formulations + product safety data subject to IS controls
- **`regulated-ai`** — if ML used in QSAR / read-across modeling / process control
- **`iso-14001`** — chemical manufacturing has highly significant environmental aspects (emissions / waste / spills / contamination)
- **`iso-45001`** — chemical + worker safety hazards (acute + chronic + reproductive toxicity exposure)
- **`iso-50001`** — chemical processes often energy-intensive
- **`iso-37001`** — government-procurement scope (e.g., specialty-chemicals supplier to military)
- **`iso-22301`** — supply continuity for critical chemical inputs
- **`recall-workflow`** — chemical product recalls under various authority jurisdictions
- **`iso-31000`** — meta-framework unifying REACH risk + ECHA risk + EPA risk + OECD GLP study risk

## Adoption guidance

If your organization:

- **Manufactures industrial chemicals for EU market** → core scope. REACH registration mandatory ≥1 t/y; CLP classification + notification mandatory; SDS mandatory for hazardous substances/mixtures.
- **Imports chemicals into EU** → REACH applies even without manufacturing; REACH-Only Representative (Article 8) appointment recommended for non-EU manufacturers.
- **Manufactures chemicals for US market** → TSCA inventory check + PMN for new chemicals + CDR every 4 years.
- **Operates non-clinical safety studies (toxicology + ecotoxicology labs)** → OECD GLP applies; Member State or US EPA/FDA GLP monitoring authority registration required.
- **Multi-region operations** → both REACH + TSCA apply; differing inventory + notification requirements per jurisdiction.

## Standards licensing

All cited standards PUBLIC. ECHA Guidance Documents (R.x series) supplementary + PUBLIC. IUCLID 6 software PUBLIC (free download from ECHA).

## Forward work

- US OSHA HCS standalone overlay
- DOT HazMat + IMDG + IATA + ADR/RID transport overlay
- EU Biocides (Regulation 528/2012) overlay
- EU Cosmetics (Regulation 1223/2009) vertical OR standalone
- EU Pesticides / Plant Protection Products vertical OR standalone
- US FIFRA (Federal Insecticide, Fungicide, and Rodenticide Act) vertical
- TSCA PFAS reporting (40 CFR 705) specific standalone
- ECHA SCIP database notification workflow template
- Substance Authorisation application (REACH Article 60) template (substitution plan + AoA + SEA)
- Read-across justification template per ECHA RAAF
- Multi-language SDS coordination workflow (EU 24 languages)
- OECD Test Guidelines cross-reference (TG 401-501+ series for tox + TG 201+ ecotox)
