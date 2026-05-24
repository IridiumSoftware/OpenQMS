# PCI DSS SAQ-D Service Provider — Open QMS sub-overlay

Sub-overlay on the `pci-dss` cross-cutting overlay. **PCI DSS v4.0 Self-Assessment Questionnaire D — Service Provider** — distinct requirement set from SAQ-D Merchant.

## Composition

`pci-dss + pci-dss-saq-d-sp`. Mutually exclusive with other SAQ sub-overlays.

## When to use

- Payment gateways, processors, tokenisation services
- Hosting providers handling merchant CDE
- MSSPs managing merchant security infrastructure
- Fraud detection / risk scoring service providers
- Any entity storing/processing/transmitting CHD on behalf of merchants

## Service-provider-only requirements

- Req 11.5.1.1 IDS on critical systems (v4.0)
- Req A1 multi-tenant separation
- Req A2 per-customer encryption keys (where applicable)
- Quarterly internal scans by qualified independent personnel
- Quarterly customer attestation of compliance
- Customer-facing AOC + Responsibility Matrix (Req 12.9.1)
