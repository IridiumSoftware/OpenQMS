# SaMD (Software as a Medical Device) overlay

Cross-cutting overlay module adding requirements specific to standalone software medical devices. Composes with the medical-devices vertical module:

```bash
openqms resolve \
  --module medical-devices \
  --module samd \
  --standard "ISO 13485:2016" \
  --standard "IEC 62304:2006+A1:2015" \
  --standard "IEC 82304-1:2016" \
  --standard "IMDRF SaMD N12" \
  ...
```

## What this overlay adds

- **IMDRF SaMD risk categorization** — Class I-IV based on State of Healthcare Situation × Significance of Information. Drives the rigor of clinical evaluation, post-market surveillance, and risk controls.
- **IEC 82304-1** — health software product safety requirements beyond IEC 62304's lifecycle (post-market plan, decommissioning, use-environment validation).
- **Cybersecurity** — threat modeling, secure development lifecycle, vulnerability disclosure, coordinated handling, post-market security updates.

## Per-class GSPR applicability note

When the SaMD overlay is composed with the medical-devices module, the GSPR conformity checklist's applicability column should be declared **NA** for most physical/mechanical GSPRs (Annex I §10 chemical, §11 microbial, §14 environmental, §16 radiation, §18 active devices in the physical sense, §19 mechanical/thermal, §20 energy delivery — though some apply to AI-driven decisions that affect physical state). SaMD specifically engages §17 (electronic programmable systems) at depth. The adopter's GSPR checklist documents the NA justifications per device.

## Forward — IVD

SaMD-IVD (in-vitro diagnostic software) is governed by IVDR (Regulation 2017/746) in the EU, not MDR. A separate `medical-devices-ivd` module is required for IVD-SaMD; this overlay does not cover IVD-specific requirements.
