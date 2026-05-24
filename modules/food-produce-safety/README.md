# food-produce-safety — Open QMS class overlay

Class overlay on the **food-safety** vertical. Adds FSMA Produce Safety Rule (21 CFR 112) — farm-stage scope covering growing, harvesting, packing, and holding of fresh produce normally consumed raw.

## Scope

Farms growing covered produce. Distinct from the food-safety vertical's primarily-processor scope.

**Covered produce** = fruits + vegetables normally consumed raw (per §112.2 RAC list — apples, berries, melons, leafy greens, etc.). Excluded: produce that receives commercial processing adequate to reduce naturally occurring microorganisms (canning + freezing + cooking).

**Compliance dates** are staged by farm size (largest farms first; smallest deferred); see §112.3-§112.5.

## Standards covered

PUBLIC license:

- 21 CFR 112 (FSMA Produce Safety Rule)

6 clauses:

| Element | Specifics |
|---|---|
| Subpart C Personnel | Training in food hygiene + safety + health + hygiene |
| Subpart D Health + hygiene | Illness/wound restrictions; handwashing; toilet facilities; smoking/eating/drinking restrictions |
| Subpart E Agricultural water | Water quality criteria + testing + corrective measures; distinct pre-harvest vs. post-harvest (post-harvest = drinking water equivalent) |
| Subpart F BSAAO | Biological Soil Amendments of Animal Origin — raw manure + composted; treatment + application intervals + records |
| Subpart I Equipment + tools + buildings | Sanitary design + maintenance + pest control |
| Subpart K Sprouts | Specific requirements given historical outbreak record (seed treatment + agricultural water + environmental + spent-irrigation-water testing) |

## Composition

```bash
openqms validate --module food-safety --module food-produce-safety
```

## When to use

Farms growing covered produce; produce packinghouses; sprouting operations.

## When NOT to use

Produce that receives commercial processing adequate to reduce microorganisms (canning + freezing + cooking); excluded per §112.2. Animal feed (use food-animal). Meat + poultry (use food-usda-fsis).

## Standards licensing

PUBLIC license.

## Forward work

- Sprout-specific standalone overlay (Subpart K is detailed enough to warrant)
- GAP (Good Agricultural Practices) certification overlay (USDA-AMS audit scheme)
- Wine + cider farm overlay (some overlap with TTB jurisdiction)
