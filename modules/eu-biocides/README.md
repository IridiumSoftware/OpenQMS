# EU Biocides (BPR) — Open QMS cross-cutting overlay

22nd Open QMS cross-cutting overlay. **EU biocidal-products-on-market authorisation** per Biocidal Products Regulation (BPR) 528/2012.

## Scope

Biocidal products + treated articles placed on the EU market. BPR governs the *product-on-market authorisation* path that is distinct from REACH (which governs substance registration). Biocidal products are subject to BPR rather than REACH for their primary regulatory route, though REACH still applies to the chemical substance characterisation aspects.

**22 Product Types per Annex V** in 4 main groups:
- **PT 1-5** disinfectants — human hygiene; surfaces; veterinary; food + feed area; drinking water
- **PT 6-13** preservatives — in-can; film; wood; fibre/leather/rubber; construction; liquid cooling; slimicides; cutting fluids
- **PT 14-20** pest control — rodenticides; avicides; molluscicides; piscicides; insecticides; repellents/attractants; control of other vertebrates
- **PT 21-22** other — antifouling; embalming

## Standards covered

**1 PUBLIC standard:**

- **EU BPR — Regulation (EU) No 528/2012** (EUR-Lex). 10 clauses across the regulation covering active-substance approval pathway (Articles 4-9), product authorisation (Articles 17-23 with Article 19 conditions), data protection + Article 95 supplier list (Articles 49-50), treated articles (Article 58), research + development exemption (Article 56), classification/labelling/packaging additions over CLP (Articles 69-72), Annex V product types, Annex VI common principles for dossier evaluation.

## Templates introduced

1 new template:

- **`templates/product-chemicals/biocides/BPR-AUTHORISATION-APPLICATION-TEMPLATE.md`** — full Article 17 product-authorisation application template covering pathway selection (national / MR-parallel / MR-sequence / Union authorisation / simplified); composition + Article 95 supplier-list verification + LoA reference; Article 19(1) conditions check; efficacy + HHRA + ERA dossier framework; CLP-aligned C+L+P with Article 69 biocide-specific label additions; specific use conditions; substances of concern; Annex dossier index; post-authorisation obligation operationalisation.

Plus 2 cross-cutting template bindings:
- **SDS template** (shared with chemicals + osha-hcs) — extended with PT identification + authorisation number + biocide-specific Article 69 labelling cross-reference
- **SOP template** — for Article 56 R&D notification workflow + Article 95 supplier-list maintenance + post-authorisation change notification per Implementing Regulation (EU) 354/2013

## Composition

Natural compositions:

- **`chemicals + eu-biocides`** — full chemicals manufacturer placing biocidal products on EU market (REACH for substance + BPR for biocidal-product authorisation)
- **`eu-biocides + iso-27001`** — biocides authorisation dossiers contain commercially-sensitive efficacy + toxicology data
- **`eu-biocides + iso-14001`** — biocides primary lifecycle environmental aspects
- **`eu-biocides + recall-workflow`** — biocidal product recall + Article 47 adverse-effect reporting integration

## When to use + when NOT to use

**Use when:**
- Placing biocidal products on EU market under any of the 22 PTs
- Placing treated articles on EU market where biocidal property is claimed OR where active-substance approval requires labelling
- Conducting R&D on new active substances OR new biocidal products requiring Article 56 notification

**Do not use when:**
- Cosmetics (EU Regulation 1223/2009 separate; some preservative overlap)
- Medicinal products with biocidal-like activity (Directive 2001/83/EC dominant regulator)
- Plant protection products (Regulation 1107/2009 — pesticides, separate framework, sometimes confused with biocides)
- Medical devices with biocidal active substance (MDR 2017/745 dominant; biocidal active substance ancillary)

## Key adopter-cost gotchas

- **Article 95 supplier list** is the gating compliance check often missed by SME importers. As of 2015-09-01, biocidal products containing an active substance whose supplier is NOT on the Article 95 List for the relevant PT cannot be placed on the EU market. Even one missing supplier = product withdrawal. Quarterly verification recommended; small suppliers without LoA face existential commercial risk.

- **Joint submission for vertebrate-animal data** is *mandatory* per Article 62 — data-sharing negotiation under Article 63. Failure to negotiate in good faith → ECHA dispute resolution per Article 63(3). Adopters often underestimate the time required.

- **Candidate for substitution** status per Article 10 shortens authorisation period to 5 years (vs. typical 10) + triggers comparative assessment per Article 23. Substance lifecycle planning matters.

- **Treated articles** scope catches manufacturers who don't think of themselves as "biocides" companies — e.g., textile manufacturers using treated yarns; paint manufacturers; food packaging coated with antimicrobial. Article 58 labelling obligations bite even when biocidal property is incidental.

## Forward work

- US EPA FIFRA pesticide registration overlay — partial overlap with biocides but legally distinct (cosmetics fungicide / antimicrobial vs. pesticide distinction varies by jurisdiction)
- UK BPR (post-Brexit retained law with HSE as Competent Authority replacing ECHA)
- ECHA R4BP 3 portal-submission workflow template
- Inquiry per Article 62 (vertebrate study data inquiry) template
- BPR Article 95 List verification SOP
- Annex II per-PT data requirements per-PT detailed templates
- ECHA Guidance Volume I-V cross-reference index
