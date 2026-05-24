# REACH Authorisation (Annex XIV) — Open QMS chemicals class overlay

Chemicals class overlay encoding **REACH Title VII Authorisation** obligations (Articles 55-66) for substances listed on Annex XIV.

## Scope

Substances on Annex XIV cannot be PLACED ON MARKET or USED after the substance's sunset date without:
- A specific authorisation granted by the European Commission per Article 60, OR
- A use covered by an Article 56 exemption

Currently ~60 substances on Annex XIV. New SVHC candidates migrate from Candidate List to Annex XIV via Article 58 prioritisation (volume + dispersive use + alternatives availability). High-profile entries include phthalates (DEHP/DBP/BBP/DIBP); short-chain chlorinated paraffins; chromium VI compounds; lead chromate.

## Clauses

6 clauses across Title VII obligations:
- Article 56 — Prohibition without authorisation
- Article 60 — Grant of authorisation (Adequate Control vs. Socio-Economic routes)
- Article 62 — Application content (CSR + AoA + Substitution Plan + SEA)
- Articles 65-66 — Holder obligations + downstream-user notification within 3 months of first supply
- Article 61 — Review of authorisation (review report 18 months before period end)
- Annex XIV — Listed substances + sunset dates + review periods

## Templates introduced

2 new templates:
- **`templates/product-chemicals/authorisation/REACH-AUTHORISATION-APPLICATION-TEMPLATE.md`** — Article 62 full application with route selection (Adequate Control vs. Socio-Economic per substance properties) + CSR + AoA + SEA + fee structure + joint-application provisions
- **`templates/product-chemicals/authorisation/SUBSTITUTION-PLAN-TEMPLATE.md`** — Article 60(4)(c) substitution plan with 10-action timetable + risk-management transition + contingencies + reporting cadence

Plus 1 SOP binding for Annex XIV monitoring + downstream Article 66 notification + Article 65 labelling + Article 61 review-report preparation.

## Composition

Designed for `chemicals + chemicals-authorisation`. Often pairs with `chemicals-svhc` (substances typically transit Candidate List → Annex XIV; both overlays needed during transition).

## When to use

- Manufacturer / importer / downstream user with substance on Annex XIV (mandatory)
- Manufacturer of substance being prioritised for Annex XIV inclusion (forward planning)
- Downstream user receiving authorised substance — Article 66 notification required within 3 months of first supply

## Forward work

- ECHA Authorisation List Lifecycle template (Candidate List → Annex XIV migration tracking)
- Article 66 downstream-user notification workflow
- Per-RMM monitoring + verification SOP suite
- Annex XV Restriction Dossier template (alternative regulatory route for substances not authorised)
