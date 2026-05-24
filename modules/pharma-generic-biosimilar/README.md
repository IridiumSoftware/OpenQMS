# pharma-generic-biosimilar — Open QMS class overlay

Class overlay on the **pharma** vertical. Adds the abbreviated approval pathway requirements for **generics** (small-molecule equivalents of approved drugs via ANDA) and **biosimilars** (highly-similar versions of approved biologics via 351(k)).

## Scope

Generics: small-molecule, demonstrate bioequivalence to Reference Listed Drug (RLD) via §320 studies. ANDA per 21 CFR §314.94. Orange Book RLD reference.

Biosimilars: biological products, demonstrate biosimilarity to FDA-licensed reference per 42 USC §262(k) / Public Health Service Act §351(k) (BPCI Act 2009). Reduced clinical data vs. originator BLA but analytical similarity bar is high. Optional interchangeability designation requires additional switching studies.

## Standards covered

PUBLIC license:

- 21 CFR 314 (Applications for FDA Approval to Market a New Drug; includes ANDA per §314.94)
- 42 USC 262(k) / PHSA §351(k) (Biosimilar pathway)

5 clauses:

| Element | Specifics |
|---|---|
| ANDA bioequivalence | Demonstrate BE to RLD; pharmaceutical equivalence; identical labeling |
| ANDA Paragraph IV patent certification | Where applicable; 30-month stay + first-filer 180-day exclusivity per Hatch-Waxman |
| Biosimilar 351(k) pathway | Analytical similarity + animal studies + clinical (PK/PD + immunogenicity + ≥1 safety/purity/potency study) |
| Biosimilar interchangeability | Optional designation; requires switching studies; substitutable without prescriber intervention |
| Post-approval reporting | Same as originator (FAR + annual + PADR + safety; manufacturing change supplements) |

## Composition

```bash
# Generic small-molecule
openqms validate --module pharma --module pharma-generic-biosimilar

# Biosimilar — also compose pharma-biologics for biologics-specific
openqms validate --module pharma --module pharma-biologics --module pharma-generic-biosimilar
```

## When to use

ANDA generic-drug manufacturer OR biosimilar 351(k) sponsor. Note: pharma vertical alone covers originator NDA/BLA holders.

## When NOT to use

Originator manufacturers (pharma alone). Compounded drugs (separate regulatory regime per FDCA §503A/503B; not in scope).

## Standards licensing

PUBLIC license.

## Forward work

- EU generic pathway overlay (10-year data-exclusivity then abridged Article 10 application per Directive 2001/83/EC)
- EU biosimilar pathway overlay (CHMP biosimilar guidance + Article 10(4))
- Hatch-Waxman patent strategy SOP template
