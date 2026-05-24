# PCI DSS SAQ-D Merchant — Open QMS sub-overlay

Sub-overlay on the `pci-dss` cross-cutting overlay. **PCI DSS v4.0 Self-Assessment Questionnaire D — Merchant** — general merchant SAQ covering all ~300+ requirements.

## Composition

`pci-dss + pci-dss-saq-d-merchant`. Mutually exclusive with other SAQ sub-overlays.

## When to use

- Merchant cannot use any simpler SAQ (A / A-EP / B / B-IP / C / C-VT / P2PE)
- Stores CHD electronically
- Multi-channel (e-commerce + in-store + MOTO)
- Custom-built payment systems
- Acquirer-mandated SAQ-D

## Level + validation

By brand-defined merchant Level (1-4); Level 1 typically requires external QSA Report on Compliance instead of self-assessment. SAQ-D Merchant is effectively full PCI DSS in self-assessment form.

## v4.0 transition

PCI DSS v4.0 mandatory 2024-03-31; future-dated v4.0 requirements (script management Req 6.4.3, payment-page integrity Req 11.6.1, IDS Req 11.5.1.1, etc.) effective 2025-03-31.
