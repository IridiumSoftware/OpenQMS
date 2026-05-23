# FDA Class II overlay (510(k) path)

Cross-cutting overlay adding FDA Class II-specific requirements. Class II is the most common FDA classification — devices include most diagnostic equipment, infusion pumps, surgical instruments, syringes, etc. Class II is the moderate-risk tier where 510(k) Premarket Notification is the typical submission path.

Use via:

```bash
openqms resolve --module medical-devices --module fda-class-ii ...
```

## What this overlay adds

- **510(k) Premarket Notification** (21 CFR 807 Subpart E) — substantial-equivalence demonstration against a predicate device.
- **Special Controls** — performance standards, post-market surveillance, patient registries, special labeling, etc., per product code.
- **De Novo classification** (21 CFR 860 Subpart D) — pathway for novel low-to-moderate risk devices without a predicate, allowing risk-based classification instead of automatic Class III.

## When to use which submission path

| Situation | Path |
|---|---|
| Class II device, has predicate | 510(k) Premarket Notification |
| Class II device, no predicate, low-to-moderate risk | De Novo |
| Class II device, exempt from 510(k) per product code | Establishment registration + listing only |
| Class III device | PMA (see `modules/fda-class-iii/`) |

## Establishment registration & listing

§807 Subparts B + D require US-based manufacturers (and foreign manufacturers shipping to US) to register their establishment and list their devices annually. This is procedural and applies regardless of class; the overlay's clauses focus on Subpart E (510(k)) as the Class II-specific submission gate.
