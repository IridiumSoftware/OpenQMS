# PCI DSS SAQ-A — Open QMS sub-overlay

Sub-overlay on the `pci-dss` cross-cutting overlay. **PCI DSS v4.0 Self-Assessment Questionnaire A** — card-not-present merchants with all CHD functions fully outsourced to PCI-validated TPSPs.

## Scope

Smallest SAQ (~22 requirements vs ~300 for full SAQ-D). E-commerce iframe/redirect; mail/telephone-order with payment provider handling CHD.

## Composition

`pci-dss + pci-dss-saq-a`. Mutually exclusive with other SAQ sub-overlays for a given merchant scope.

## When to use

- E-commerce merchant using iframe / redirect / hosted payment page to a PCI-validated payment provider
- Merchant page JS does NOT touch CHD (no client-side tokenisation, no field-capture)
- Mail/telephone-order merchant with full payment outsourcing

## When NOT to use

- Direct-post or any JS-based CHD capture → SAQ-A-EP
- Card-present terminal scope → SAQ-B / SAQ-B-IP / SAQ-C-VT
- General merchant scope → SAQ-D-Merchant
- Service provider scope → SAQ-D-SP
- P2PE-validated solution → SAQ-P2PE
