# ivdr-class-c — Open QMS class overlay

Class overlay on the **medical-devices** vertical (typically composed with the `ivd` overlay). Adds EU IVDR risk class C requirements per Annex VIII classification rules.

## Scope

Class C is the second-highest IVD risk class — high individual risk and/or moderate public-health risk. Examples per Annex VIII Rule 3:

- Detection of infectious agents (HIV, HCV, HBV, transmissible agents in blood/tissue/cells for transplantation)
- Genetic testing
- Companion diagnostics
- Cancer diagnosis + staging
- Near-patient testing for life-threatening conditions
- Pre-natal screening for congenital disorders

## Standards covered

PUBLIC license:

- EU IVDR Annex VIII (Classification Rules)
- EU IVDR Annex IX + X + XIII + Article 81 cross-references

4 clauses:

| Element | Specifics |
|---|---|
| Class C classification (Rules 2-4) | Per Annex VIII Rule 3 most common; Rules 2 + 4 for blood/tissue/cell donation suitability |
| NB conformity (Annex IX + X) | Notified Body involvement required; full QA per Annex IX OR combination Annex XI + Annex IX Ch. II; TD review + QMS audit |
| Clinical evidence (Annex XIII A) | Scientific validity + analytical + clinical performance; significant clinical evidence required; PMCF mandatory |
| PSUR (Article 81) | Annual first 2 years post-CE; biennial thereafter |

## Composition

```bash
# Composes with medical-devices + ivd overlay
openqms validate --module medical-devices --module ivd --module ivdr-class-c
```

## When to use

IVDs classified as Class C per IVDR Annex VIII Rules 2/3/4. Most companion diagnostics + most genetic tests + most infectious-disease detection fall here.

## When NOT to use

Class A (low risk; self-declaration) — no overlay needed beyond `ivd`. Class B (low-to-moderate risk; NB only for sterile + measurement). Class D (highest risk — see `ivdr-class-d`).

## Standards licensing

PUBLIC.

## Forward work

- Class-C PSUR template (annual format for first 2 years; biennial format thereafter)
- Annex IX QMS audit readiness checklist
- Companion diagnostic specific overlay (sub-class of Class C with co-development requirements per drug therapy)
