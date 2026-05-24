# REACH Tonnage Band ≥10 t/y — Open QMS chemicals class overlay

Chemicals class overlay encoding **REACH Annex VIII** incremental data + **mandatory Chemical Safety Report (CSR)** at ≥10 t/y per manufacturer/importer.

## Clauses

- Annex VIII incremental (sub-acute 28-day repeated dose; reproductive screening if not yet; toxicokinetics basic; short-term fish toxicity; activated sludge respiration; hydrolysis vs pH; adsorption/desorption screening; biodegradation extension)
- Article 14 CSR mandatory from ≥10 t/y
- Article 31(7) Extended SDS (eSDS) with CSR-derived exposure scenarios

## Composition

`chemicals + chemicals-tonnage-10`. Includes-and-supersedes `chemicals-tonnage-1`.

## Adopter-cost note

The 10 t/y threshold is the major cost cliff:
- CSR preparation: €30-100k per substance (per ECHA Cost Estimate Guidance R.16)
- eSDS derivation + distribution: ongoing per-customer per-use coordination cost
- Annex VIII vertebrate studies: €20-100k incremental (28-day RDT typically €40-80k)
- Exposure scenario development for each identified use
