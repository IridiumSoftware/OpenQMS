# Cell Therapy Supply Chain — Open QMS cross-overlay

**Cross-overlay.** Binds pharma + atmp + transport-hazmat to encode the cold-chain logistics regulatory framework for autologous + allogeneic cell therapies.

## Scope

Vein-to-vein autologous CAR-T; manufacturer-to-patient allogeneic ATMP; cryogenic shipping; chain-of-identity (COI) + chain-of-custody (COC); critical timeline-from-collection-to-infusion.

## Standards covered

7 clauses across EU GMP Annex 2A + 21 CFR 1271 HCT/P + IATA DGR cryogenic UN1977 + ICH Q5C cold-chain integrity + autologous failure-mode handling + Time-Out-of-Storage (TOS) cumulative budget tracking.

## Composition

Most natural: `pharma + atmp + transport-hazmat + cell-therapy-supply-chain`. Often also composes with `regulated-ai` (if release decision-support AI used), `recall-workflow` (for product recall in active treatment scenarios), `privacy + hipaa` (PHI in COI tracking).

## Key adopter pain points addressed

1. **Chain of Identity (COI)** — vein-to-vein same-patient tracking for autologous; donor + lot + recipient for allogeneic; bidirectional traceability mandatory 30-year EU / indefinite US
2. **Cryogenic shipping (UN1977)** — LN2 dry-shipper Dewar per IATA PI 202; 7-14 day vapor-shipper hold time; temperature continuous logging
3. **Time-Out-of-Storage (TOS)** — cumulative budget across manufacturing + transport + clinical site; CMC stability defines max
4. **Autologous failure mode** — no batch-pool backup; product loss = retreatment from new apheresis; specific escalation pathway

## Templates

Reuses + extends ATMP traceability template + transport-hazmat shipping paper template + cross-cutting SOP template. No new templates.

## When to use

- Autologous CAR-T manufacturers
- Allogeneic ATMP manufacturers
- Apheresis-to-manufacturing-to-clinical-site logistics operators
- ATMP CDMO with cold-chain scope
