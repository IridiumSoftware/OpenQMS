# Implantable medical device overlay

Cross-cutting overlay module adding requirements specific to implantable medical devices. Composes with the medical-devices vertical:

```bash
openqms resolve \
  --module medical-devices \
  --module implantable \
  ...
```

## What this overlay adds

- **Implant card** (EU MDR Annex I §23.4) — patient-facing card with device identification, hazards, precautions, expected lifetime, post-implant care.
- **SSCP** (EU MDR Article 32) — Summary of Safety and Clinical Performance for Class III and implantable devices. Two audiences (patient + HCP); published on EUDAMED.
- **ISO 14708-1** (active implantable medical devices, general requirements) — for the subset of implantables that are active (powered).

## Composition with class overlays

Most implantables are EU MDR Class IIb or Class III; adopters typically compose this overlay with the relevant class overlay:

```bash
# Implantable Class III device
openqms resolve --module medical-devices --module implantable --module mdr-class-iii ...
```

The compose primitive dedupes shared clauses (e.g. `MDR-Art32` appears in both implantable and mdr-class-iii) — the resulting matrix has each clause once with the union of template bindings.
