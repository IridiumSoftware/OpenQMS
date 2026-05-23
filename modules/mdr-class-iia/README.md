# EU MDR Class IIa overlay

Cross-cutting overlay adding EU MDR Class IIa-specific requirements. Class IIa is medium-risk — devices include software-as-medical-device (most SaMD per Rule 11), hearing aids, surgical instruments (reusable beyond Class Ir), etc.

Use via:

```bash
openqms resolve --module medical-devices --module mdr-class-iia ...
```

## What this overlay adds

- **Annex XI production quality assurance** — streamlined NB conformity assessment route covering production + product-control aspects, alternative to full Annex IX QMS audit.
- **PMS report (as-needed cadence)** — Class IIa devices maintain a PMS report updated based on PMS plan triggers, not on a mandatory PSUR cadence. Full PSUR is required only for Class IIb (biennial) and Class III (annual).

## Composition patterns

```bash
# Standard Class IIa SaMD
openqms resolve --module medical-devices --module samd --module mdr-class-iia ...

# Class IIa implantable (uncommon but possible)
openqms resolve --module medical-devices --module implantable --module mdr-class-iia ...
```

The implantable overlay adds the implant card (Annex I §23.4) and SSCP (Article 32); SSCP applies to implantables regardless of class.
