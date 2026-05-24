# pci-dss — Open QMS cross-cutting overlay

Payment Card Industry Data Security Standard v4.0 overlay. Composes with any vertical.

## Scope

Any entity that stores, processes, or transmits **cardholder data (CHD)** or **sensitive authentication data (SAD)** — merchants, processors, acquirers, issuers, service providers.

v4.0 published March 2022; v4.0.1 minor update June 2024. v3.2.1 retired March 31, 2024.

## Standards covered

Public license (PCI SSC):

- PCI DSS v4.0

8 clauses across the 6 goals + 12 requirements:

| Goals | Requirements | Topic |
|---|---|---|
| CDE Scope | (scoping) | Network segmentation reduces scope |
| 1-2 | Build + maintain secure network/systems | Firewalls + hardened configurations |
| 3-4 | Protect account data | Stored encryption + transmission crypto |
| 5-6 | Vulnerability management | Anti-malware + secure SDLC + patches |
| 7-9 | Strong access control | Need-to-know + MFA (v4.0 broader) + physical |
| 10-11 | Monitor + test | Logging + ASV quarterly + pentests |
| 12 | Information security policy | Risk + training + IR planning |
| (v4.0) | Customized Approach | Alternative for mature programs; QSA validates |

## Composition

```bash
openqms validate --module <vertical> --module pci-dss
# Common composition for payment-handling SaaS:
openqms validate --module manufacturing --module soc-2 --module pci-dss --module iso-27001
```

## When to use

Any organization in the cardholder data flow — payment-facing e-commerce; payment processors; payment-handling SaaS; fintech; retail POS systems; restaurants; etc.

## When NOT to use

Organizations not touching cardholder data. PCI DSS is scope-driven by data, not industry.

## Standards licensing

PCI DSS v4.0 PUBLIC license (download free from pcisecuritystandards.org). QSA / ISA training + certification commercial.

## Forward work

- PCI 3DS Core Security Standard overlay (3D-Secure SDK + ACS protection)
- PCI P2PE (Point-to-Point Encryption) standalone overlay
- PCI PA-DSS (Payment Application) overlay — retired but legacy systems still cite
- Self-Assessment Questionnaire (SAQ) workflow templates per merchant level
