# EU MDR Class III overlay

Cross-cutting overlay adding EU MDR Class III-specific requirements. Class III is the most stringent risk class under MDR — implantable life-supporting devices, drug-device combination devices, certain CNS-contacting devices, etc.

Use via:

```bash
openqms resolve --module medical-devices --module mdr-class-iii ...
```

## What this overlay adds

- **SSCP** (Article 32) — Summary of Safety and Clinical Performance; required for Class III + implantables.
- **Expert panel consultation** (Article 54) — clinical evaluation consultation procedure for implantable Class III and certain Class IIb active devices.
- **Type-examination** (Annex X) — conformity assessment route involving notified-body examination of a representative sample.
- **PSUR cadence** (Article 84) — Periodic Safety Update Report prepared at least annually and submitted via EUDAMED.

## Composition patterns

```bash
# Class III implantable
openqms resolve --module medical-devices --module implantable --module mdr-class-iii ...

# Class III combination product (drug-delivery device)
openqms resolve --module medical-devices --module mdr-class-iii ...
# (Combination product overlay is forward work — Annex VIII Rule 14 logic.)
```

Class III non-implantable + non-IVD is rare but possible (e.g. blood substitutes, certain CNS-contacting catheters). For non-implantable Class III, omit the implantable overlay.
