# eu-gpsr — Open QMS cross-cutting overlay

EU General Product Safety Regulation (Regulation (EU) 2023/988) overlay. Effective December 13, 2024. Replaces 2001 GPSD. Composes with any vertical.

## Scope

Consumer products placed on the EU market — fills gaps not covered by sector-specific safety legislation (toys → Toy Safety Directive; medical devices → MDR; etc., which continue to apply alongside GPSR).

GPSR captures consumer-product safety for: low-tech products with no sector regulation; AI-enabled products; software updates + connected products; online-marketplace product listings.

## Standards covered

PUBLIC license:

- EU GPSR — Regulation (EU) 2023/988

5 clauses:

| Article | Topic | Specifics |
|---|---|---|
| Art. 5 General safety obligation | Economic operators only place safe products on the market |
| Art. 9 Manufacturer obligations | Internal risk analysis + technical docs + product identification + manufacturer ID + instructions + safety info in EU language + accident records + recall readiness |
| Art. 19 Safety Gate notification | **Immediate** notification (formerly RAPEX) when product dangerous + serious risk; template + national-competent-authority coordination |
| Art. 20 Online marketplaces | Single contact point + cooperation + manufacturer-info requirement from sellers + dangerous-listing removal within 3 working days |
| Arts. 36-38 Recall + corrective | Voluntary recall procedures + notice content + consumer communication + right of repair/replacement/refund |

## Composition

```bash
openqms validate --module <vertical> --module eu-gpsr
# Often combined with recall-workflow:
openqms validate --module manufacturing --module eu-gpsr --module recall-workflow
```

## When to use

Economic operators placing consumer products on the EU market — manufacturers + importers + distributors + fulfilment service providers + online marketplaces.

## When NOT to use

Non-consumer-products (B2B equipment with own regulatory framework); products fully covered by sector-specific safety legislation (toys / cosmetics / medical devices / motor vehicles each have their own regimes).

## Standards licensing

PUBLIC (EUR-Lex).

## Forward work

- Safety Gate notification template (per Article 19 standard format)
- Online marketplace obligations workflow template
- Right of consumers (repair / replacement / refund) handling SOP
