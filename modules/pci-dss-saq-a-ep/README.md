# PCI DSS SAQ-A-EP — Open QMS sub-overlay

Sub-overlay on the `pci-dss` cross-cutting overlay. **PCI DSS v4.0 Self-Assessment Questionnaire A-EP** — e-commerce merchants where the merchant website controls payment-page context but CHD is still processed by PCI-validated TPSP.

~191 requirements covering vulnerability management + secure SDLC + script integrity + quarterly ASV scan + annual pen test.

## Composition

`pci-dss + pci-dss-saq-a-ep`. Mutually exclusive with other SAQ sub-overlays.

## When to use

- E-commerce merchant where the website controls redirection / iframe / direct-post / client-side encryption
- Merchant website may affect CHD security even without storing/processing/transmitting it directly
- Primary scope when SAQ-A criteria not met but full SAQ-D not required

## Key v4.0 additions (effective 2025-03-31)

- Req 6.4.3 — payment-page script inventory + integrity (SRI / CSP / equivalent)
- Req 11.6.1 — HTTP header + script content tamper detection
- These two controls are the primary defence against Magecart-style supply-chain attacks
