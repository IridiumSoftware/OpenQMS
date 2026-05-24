# REACH SVHC — Open QMS chemicals class overlay

Chemicals class overlay encoding **Substance of Very High Concern (SVHC)** supply-chain communication + ECHA notification obligations under REACH.

## Scope

Applies to any chemicals adopter whose substances or articles contain substances on the ECHA Candidate List per REACH Article 59. SVHC scope per Article 57:
- (a) CMR Category 1A or 1B
- (b) PBT (Persistent + Bioaccumulative + Toxic per Annex XIII)
- (c) vPvB (very Persistent + very Bioaccumulative per Annex XIII)
- (d) Equivalent level of concern — endocrine disruptors etc.

Candidate List currently ~240 substances; refreshed approximately 2x/year by ECHA.

## Clauses

5 clauses across REACH supply-chain + ECHA notification obligations:
- Article 7(2) — SVHC-in-articles ECHA notification (>1 t/y AND >0.1% w/w)
- Article 33(1) — Communication to recipients
- Article 33(2) — Consumer response within 45 days
- Waste Framework Directive (EU) 2018/851 Article 9(1)(i) — SCIP database notification
- Annex XV — SVHC identification dossier (for adopters proposing additions)

## Templates introduced

- **`templates/product-chemicals/svhc/SVHC-COMMUNICATION-LETTER-TEMPLATE.md`** — Article 33(1) + 33(2) + SCIP cross-reference
- SOP binding for monthly Candidate List monitoring + 6-month Article 7(2) notification window + SCIP database submission workflow

## Composition

Designed for `chemicals + chemicals-svhc`. Composes with cross-cutting overlays especially iso-27001 (CBI substance identity) and recall-workflow (if SVHC inclusion triggers product change).

## When to use

- Article producer/importer with substances >1 t/y per substance AND substance present in articles >0.1% w/w
- Substance supplier with SVHCs in mixtures sold to industrial/professional users
- Consumer-facing article supplier subject to Article 33(2) consumer-request response window
- Any EU article supplier subject to SCIP database (effective 2021-01-05)

## Forward work

- Annex XV SVHC identification dossier template (Member State CA / ECHA submitter)
- ECHA SCIP IUCLID 6 dossier template
- Article 7(3) exemption justification template
- Per-article-component SVHC concentration calculator (per *FCD* CJEU C-106/14)
