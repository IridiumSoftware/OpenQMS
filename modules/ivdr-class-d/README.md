# ivdr-class-d — Open QMS class overlay

Class overlay on the **medical-devices** vertical. Adds EU IVDR **highest-risk** Class D requirements per Annex VIII Rule 1.

## Scope

Class D captures the highest-risk IVDs:
- Transmissible-agent detection in blood/blood components/cells/tissues/organs/derivatives for **transfusion / transplantation suitability** assessment
- Infectious load monitoring for **life-threatening disease** where monitoring is critical
- Detection of transmissible agents causing **life-threatening disease with high or suspected risk of propagation**

Examples: HIV NAT for blood-donor screening; HCV / HBV blood-donor screening; HTLV-I/II blood-donor screening; high-risk HPV screening.

## Standards covered

PUBLIC license:

- EU IVDR Annex VIII (Rule 1)
- EU IVDR Articles 58, 81, 100 + Annexes IX, XI, XIII cross-references

5 clauses:

| Element | Class D specifics |
|---|---|
| Classification (Rule 1) | Transfusion/transplantation suitability assessment OR life-threatening disease monitoring/detection with propagation risk |
| EU Reference Laboratory (EURL) | Article 100 + Annex IX §4.9 — EURL consultation in conformity assessment; batch verification may be required |
| Clinical evidence rigor | Most extensive package — large multi-site multi-population performance studies; clinical performance studies per Article 58 |
| Annual PSUR (Article 81) | Annual throughout lifecycle (more frequent than Class C which is biennial after first 2 years) |
| Batch verification | NB + EURL pre-release verification may be required, especially for blood/tissue screening |

## Composition

```bash
openqms validate --module medical-devices --module ivd --module ivdr-class-d
```

## When to use

The most stringent IVD category — typically blood/tissue donor screening assays + life-threatening infectious disease detection where erroneous results could cause widespread harm.

## When NOT to use

Lower IVDR risk classes (Class A self-declaration; Class B limited NB scope; Class C significant NB scope but less stringent than D — use `ivdr-class-c`).

## Standards licensing

PUBLIC.

## Forward work

- EURL coordination workflow template
- Class-D batch verification record template
- Class-D performance study (Article 58) protocol template
