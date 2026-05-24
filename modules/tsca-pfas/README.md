# TSCA PFAS Reporting Rule — Open QMS cross-cutting overlay

23rd Open QMS cross-cutting overlay. **US EPA TSCA Section 8(a)(7) PFAS Reporting and Recordkeeping** per 40 CFR Part 705 (final rule October 2023).

## Scope — broader than expected

**Applies to anyone who manufactured (including imported) a PFAS-listed substance in any year 2011-2022 for commercial purpose.** Critical scope-creep dimensions:

- **No de minimis exemption.** Trace concentrations trigger reporting.
- **No exemption for substances already in commerce** (unlike many TSCA rules).
- **No exemption for impurities or byproducts.** Unintended PFAS contamination triggers reporting.
- **Articles containing PFAS are in scope** if the importer knew or reasonably should have known. This catches importers far outside the chemicals industry — textiles, semiconductors, food packaging, cookware, automotive, medical devices, electronics, outdoor gear, cosmetics, firefighting foam stockpiles.
- **Broad PFAS structural definition** per §705.5(b) covering ~1,400+ substances meeting any of three structural criteria (R-CF2-CF2-R; R-CF2-O-CF2-R; CF3-).

If your organisation manufactured, imported, or imported articles containing fluorinated chemistry between 2011-2022 — this rule probably applies.

## Standards covered

**1 PUBLIC standard:**

- **40 CFR Part 705** — TSCA Section 8(a)(7) PFAS Reporting and Recordkeeping Requirements. 7 clauses covering applicability (§705.3); due dates (§705.15 — currently 2025-07-11 to 2026-01-11 standard, extended to 2026-07-11 for small-mfr/article-only; verify at submission time); information to be reported per substance per year per site (§705.20-30); 5-year recordkeeping (§705.25); CBI claims (§705.35); CDX/CISS submission mechanism (§705.40); plus the preamble-derived "knowability" standard for article importers.

## Templates introduced

1 new substantial template:

- **`templates/product-chemicals/pfas/PFAS-REPORTING-FORM-TEMPLATE.md`** — Per-substance per-year per-site data structure across 11-year lookback. CBI / non-CBI dual-version organisation per §703.5 substantiation requirements. Article-importer due-diligence record with common-article-categories checklist (catches non-obvious PFAS-containing imports). Worker exposure + environmental release + disposal data tables. Records retention table (5 years from last day of submission window).

Plus 1 cross-cutting template binding:
- **SOP template** — PFAS recordkeeping SOP for 5-year retention + substantiation files + article-importer due-diligence files

## Composition

Natural compositions:

- **`chemicals + tsca-pfas`** — chemicals manufacturer reporting overlay
- **`automotive + tsca-pfas`** — automotive manufacturer importing PFAS-containing fuel hoses + brake lines + EV thermal-management fluids + refrigerants
- **`medical-devices + tsca-pfas`** — medical device importer covering fluoropolymer catheter coatings + implant components
- **`aerospace + tsca-pfas`** — aerospace manufacturer with firefighting foam stockpiles + fluoropolymer hydraulic + valve components
- **`food-safety + tsca-pfas`** — food packaging supplier importer for greaseproof barriers (largely phased out but lookback period catches it)
- **`manufacturing + tsca-pfas`** — general manufacturer importing PFAS-treated textiles, ski wax, refrigerants, plating chemistries

## When to use + when NOT to use

**Use when:**
- US manufacturer or importer with any 2011-2022 activity involving fluorinated chemistry
- Importer of articles in any of the common PFAS-containing categories
- Want a defensible due-diligence record for non-reporting determinations (just as important as reporting itself — EPA may inquire)

**Do not use when:**
- Genuinely zero US activity 2011-2022 involving any PFAS substance OR article containing PFAS (rare — even most office-only operations imported electronics + ski wax + cosmetics with knowable PFAS content)

## Key adopter-cost gotchas

- **Reporter is the importer of record**, not the manufacturer. EU manufacturers selling into US markets through a US distributor: the US distributor is the reporter.
- **Affiliated entity reporting**: §705.3 "person" definition + TSCA legal-entity framework typically requires consolidated reporting at parent level. Subsidiary-level reporting often non-compliant.
- **Article-importer "knowability" standard** is the hardest part operationally. Common SME mistakes: assuming "we don't make chemicals so this doesn't apply"; missing imported PFAS-content in routine purchasing.
- **CBI claims require substantiation per §703.5** — generic claims unsupported by competitive-harm analysis fail; substantiation is non-trivial.
- **5-year retention starts from last day of submission window**, not from individual record date. Retention end is roughly 2031-01-11 for standard reporters.

## Forward work

- EU REACH SVHC PFAS-additions tracking template (Annex XIV authorisation candidates)
- EU REACH Restriction proposal on universal PFAS (ECHA/RAC/SEAC ongoing process)
- Stockholm Convention POPs PFAS substance tracking (PFOA + PFOS + PFHxS + currently under-review LC-PFCAs)
- California Prop 65 PFAS warnings cross-reference
- Maine LD 1503 (Act To Stop PFAS Pollution) intentionally-added PFAS reporting overlay
- TSCA Section 8(a)(5) Information Submission Workflow + TSCA Section 8(d) Health and Safety Study Reporting overlay
- Stewardship-program comparison template (US EPA PFOA Stewardship 2010-2015 historical context)
- Article 33 EU REACH SVHC supply-chain communication PFAS-specific subset
