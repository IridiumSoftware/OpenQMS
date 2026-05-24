# pharma-biologics — Open QMS class overlay

Class overlay on the **pharma** vertical. Adds biologics-specific requirements (cell-bank discipline + characterization + viral safety + comparability) that don't apply to small-molecule chemical drugs.

## Scope

Biologics = products whose active ingredient is biological in nature: recombinant proteins, monoclonal antibodies, vaccines, blood + blood derivatives, hyperimmune sera, ATMPs (cell + gene therapies — also use the atmp overlay for those specifics).

The key distinguishing characteristic: biologics are defined by their manufacturing process. Comparability cannot be established by structural analysis alone — multi-attribute orthogonal analysis is required.

## Standards covered

All PUBLIC license (ICH + EU GMP):

- ICH Q5A(R2) 2023 — viral safety evaluation
- ICH Q5B — expression construct analysis
- ICH Q5D — cell substrate characterization
- ICH Q5E — comparability
- ICH Q6B — biotech specifications (incl. mandatory biological activity / potency assay)
- ICH Q11 — drug substance development
- EU GMP Annex 2B — biological active substances + medicinal products

7 clauses encoding the biologics-specific additions vs. baseline pharma.

## Composition

```bash
openqms validate --module pharma --module pharma-biologics
# For ATMPs (cell + gene therapy), compose all three:
openqms validate --module pharma --module pharma-biologics --module atmp
```

## When to use

Manufacturing of biologics — recombinant proteins, mAbs, vaccines, blood derivatives, hyperimmune sera. ATMPs additionally compose with `atmp` overlay for cell + gene therapy specifics.

## When NOT to use

Small-molecule chemical drugs (use pharma alone — Q1A(R2) stability + Q6A chemical specifications apply; Q5 series + Q6B do not).

## Standards licensing

All cited standards PUBLIC license.

## Forward work

- Vaccine-specific class overlay (more stringent characterization per vaccine type)
- Plasma derivatives overlay (additional Annex 14 EU GMP for blood products)
- Cell + Tissue procurement overlay (where biologic uses primary human/animal tissue)
