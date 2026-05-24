# pharma-sterile — Open QMS class overlay

Class overlay on the **pharma** vertical. Encodes PIC/S Annex 1 (2022) enforced-rigor sterile-manufacturing requirements beyond the baseline pharma vertical's references.

## Scope

Applies to sterile drug products that cannot be terminally sterilized (aseptic fill — most parenterals, ophthalmics, biologics, ATMPs) AND to terminally-sterilized products with sterility-critical processing.

PIC/S Annex 1 (August 2022; effective August 2023) is the globally most stringent sterile-manufacturing standard.

## Standards covered

- PIC/S Annex 1 (already in pharma vertical; this overlay adds enforced-rigor clauses)

6 clauses encoding enforced sterile-manufacturing detail:

| Element | Specifics |
|---|---|
| **Contamination Control Strategy (CCS)** | Site-level documented strategy spanning facility / personnel / materials / equipment / processes / EM / product-protection technologies. Absence is a major inspection observation |
| **Isolator + RABS** | Annex 1 2022 explicitly prefers isolator/RABS over Grade A in Grade B; closed-system processing where feasible; glove integrity testing |
| **APS (Media fill)** | Initial 3 consecutive successful + semi-annual re-qualification per shift per line; worst-case design; zero contaminated units acceptance |
| **EM Grade A continuous** | Continuous viable + non-viable particle monitoring (≥0.5 + ≥5.0 µm); particle counter at point of fill |
| **Personnel aseptic qualification** | Initial gowning + APS participation + periodic re-qualification + behavior monitoring; minimize Grade A/B personnel count |
| **Line clearance** | Documented removal of prior-batch product/components/labels; independent two-person verification for product + label changeover |

## Composition

```bash
openqms validate --module pharma --module pharma-sterile
```

## When to use

Sterile drug product manufacturing — aseptic fill (most parenterals, biologics, ATMPs) OR terminally-sterilized products with sterility-critical processing.

## When NOT to use

Non-sterile manufacturing scope (oral solid dosage forms, topical, suppositories, packaging, distribution).

## Standards licensing

PIC/S Annex 1 PUBLIC license (PIC/S).

## Forward work

- Annex 1 §9.51-§9.79 (cleanrooms grade qualification) standalone CSS + qualification protocol template
- Single-use systems integrity qualification template
