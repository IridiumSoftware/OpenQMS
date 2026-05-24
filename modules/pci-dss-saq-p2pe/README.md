# PCI DSS SAQ-P2PE — Open QMS sub-overlay

Sub-overlay on the `pci-dss` cross-cutting overlay. **PCI DSS v4.0 Self-Assessment Questionnaire P2PE** — merchants using a PCI-listed Point-to-Point Encryption validated solution.

Smallest in-scope requirement set for card-present merchants — ~33 requirements vs ~300 for SAQ-D Merchant.

## Composition

`pci-dss + pci-dss-saq-p2pe`. Mutually exclusive with other SAQ sub-overlays.

## When to use

- Card-present merchant using PCI-listed P2PE-validated solution exclusively
- All channels use the same P2PE solution
- No ability to decrypt CHD (only Solution Provider holds decryption keys)

## P2PE Instruction Manual (PIM)

Primary control basis — merchant must comply with the Solution Provider's PIM covering device delivery + installation + handling + change-detection + tamper-evident packaging + secure return-for-repair.
