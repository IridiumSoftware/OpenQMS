# EU MDR Class IIb overlay

Cross-cutting overlay adding EU MDR Class IIb-specific requirements. Class IIb is the second-highest risk class under MDR — medium-high risk devices typically including therapeutic devices, infusion pumps (non-implantable), surgical lasers, ventilators, anesthesia machines.

Use via:

```bash
openqms resolve --module medical-devices --module mdr-class-iib ...
```

## What this overlay adds

- **Article 54 expert panel consultation** — triggers ONLY for the subset of Class IIb devices that are active and intended to administer or remove a medicinal product (e.g. infusion pumps, dialysis machines). Most Class IIb devices do not require expert panel review.
- **Annex IX Class IIb conformity assessment** — QMS audit + technical documentation assessment. More rigorous than Class IIa (Annex XI alternative); less stringent than Class III (which adds Annex X type-examination).
- **PSUR biennial cadence** — Article 84 requires PSUR prepared at least every 2 years for Class IIb (vs annually for Class III; vs as-needed PMS report for I/IIa).

## Class compatibility

If your Class IIb device is also implantable, compose with `implantable`:

```bash
openqms resolve --module medical-devices --module implantable --module mdr-class-iib ...
```

The implantable overlay adds the implant card (Annex I §23.4) and SSCP (Article 32) which apply to implantable Class IIb devices.

`MDR-Art54` is declared identically across mdr-class-iib + mdr-class-iii + implantable contexts; compose() silently dedupes.
