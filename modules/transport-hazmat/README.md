# Transport HazMat — Open QMS cross-cutting overlay

21st Open QMS cross-cutting overlay. **Dangerous-goods transport discipline** covering the four major regulatory regimes: US DOT HMR + IMDG (sea) + IATA DGR (air) + ADR (EU road) / RID (EU rail).

## Scope

Any organisation shipping hazardous materials by road, rail, sea, or air — broad scope:

- **Chemicals** (primary) — bulk + drum + IBC outbound shipments
- **Pharma** — solvents, active ingredients, intermediates between sites
- **Manufacturing** — intermediate transfers, hazardous waste streams
- **Automotive** — UN3480/UN3481/UN3091 Li-ion batteries; UN0503 airbag pyrotechnic inflators
- **Aerospace** — UN3480 batteries; UN0354 ejection-seat pyrotechnics; UN1977 LN2 / UN1073 LO2 cryogenics
- **Food-safety** — UN1013 CO2 for refrigeration; phase-out UN1062 methyl bromide fumigation
- **Medical devices** — UN3373 Biological Substance Category B specimens; UN2814 Cat A infectious; UN3257 elevated-temperature samples

## Standards covered

**5 standards across 4 modes:**

- **US DOT HMR — 49 CFR Parts 100-185** (PUBLIC) — domestic US road/rail. PHMSA enforcement.
- **IMDG Code** (commercial; IMO; Amendment 42-24 mandatory 2026-01-01) — international maritime transport.
- **IATA DGR** (commercial; 66th edition effective 2026-01-01; operationalises ICAO Technical Instructions Doc 9284 2025-2026) — international air transport.
- **ADR 2025** (PUBLIC; UNECE) — European road transport (applicable from 2025-01-01).
- **RID 2025** (PUBLIC; OTIF) — European rail transport.

17 clauses across the 5 standards.

## Standards licensing note

IMDG Code + IATA DGR are **commercial license** — adopters must purchase the current edition (~USD 200-400 per edition; biennial updates) before placing international shipments. The Open QMS overlay encodes the *discipline* — adopters reference the current commercial editions for the actual UN-numbered classification + packing-instruction lookup.

DOT HMR + ADR + RID are PUBLIC (ecfr.gov / UNECE / OTIF). For purely US-domestic or purely EU-overland operations, full compliance is achievable at zero standards-licensing cost.

## Templates introduced

2 new templates:

- **`templates/qms-logistics/SHIPPING-PAPER-TEMPLATE.md`** — Multimodal Dangerous Goods Form per IMO/ILO/UNECE Guidelines; covers DOT shipping paper (§172.202-205), IMDG DG Declaration (Part 5 Ch. 5.4), IATA Shipper's Declaration (Section 8), ADR/RID shipping documentation in a single form. Reduces error risk for multimodal shipments.

- **`templates/qms-logistics/HMT-TRAINING-RECORD-TEMPLATE.md`** — Multi-regime training record covering DOT four-component training (§172.704), IATA CBTA (§1.5), ADR driver vocational training (§8.2), and DGSA appointment + revalidation (§1.8.3).

Plus 1 cross-cutting binding (quality-policy) addressing the remaining placarding + marking + emergency-response + classification + packaging clauses through policy commitment rather than per-shipment artifacts.

## Composition

Composes naturally with:

- **`chemicals + transport-hazmat`** — full chemicals manufacturer outbound logistics chain
- **`automotive + transport-hazmat`** — Li-ion battery + airbag pyrotechnic shipping
- **`aerospace + transport-hazmat`** — battery + pyrotechnic + cryogenic shipping
- **`pharma + transport-hazmat`** — controlled-substance + active-pharmaceutical-intermediate shipping
- **`medical-devices + transport-hazmat`** — IVD specimen transport (UN3373 Category B) + reagent shipping
- **`iso-45001 + transport-hazmat`** — worker safety alongside transport-DG safety
- **`recall-workflow + transport-hazmat`** — return shipments of recalled DG product

## When to use + when NOT to use

**Use when:**
- Ship any hazardous material by any mode (road, rail, sea, air)
- Have hazmat employees per DOT §171.8 (anyone whose job involves DG transport-related function)
- Have ADR drivers + a DGSA obligation in EU operations
- Need a multimodal shipping-paper template + multi-regime training record framework

**Do not use when:**
- No outbound or inbound DG transport (very rare — even office sites typically ship Li-ion batteries in returned laptops)
- Shipments fall entirely within Limited-Quantity (§3.4) + Excepted-Quantity (§3.5) thresholds where most regime requirements relax — though even then, applicable §172.704 training still applies

## Operational notes

- **24-hour-monitored emergency-response telephone** required per DOT §172.604 — contract with Chemtrec / Infotrac / 3E or maintain own. Number on every shipping paper.
- **Driver / shipper training** has hard regulatory windows (DOT 3-year recurrent; ADR 5-year; IATA ≤ 24-month CBTA reassessment) — drift triggers acceptance refusal at carrier handover.
- **Classification is shipper responsibility** — getting the UN number wrong is the #1 root cause of acceptance refusals + non-conformance reports. Trained chemists/EHS staff classifying, not random untrained operators.

## Forward work

- TDG (Canada) — Transportation of Dangerous Goods Regulations overlay
- ICAO Technical Instructions standalone (vs. IATA's operationalisation)
- IMSBC Code overlay (bulk solid cargoes — distinct from IMDG packaged DG)
- IGC Code / IGF Code (LNG + low-flashpoint fuels as cargo + as bunkers)
- US 49 CFR 173 Special Permit / DOT-SP framework template
- Lithium battery package marking + testing per UN 38.3 standalone subset
- Limited Quantity / Excepted Quantity / De Minimis shipper-side workflow template
- DGSA annual report template per ADR §1.8.3.3
- Hazardous-waste manifest cross-reference (US RCRA Uniform Hazardous Waste Manifest distinct from DG transport paper)
