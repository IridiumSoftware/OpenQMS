# food-fsvp — Open QMS class overlay

Class overlay on the **food-safety** vertical. Adds Foreign Supplier Verification Program (FSVP) requirements per 21 CFR 1 Subpart L. **For US IMPORTERS of food** — requires verification that foreign suppliers' food meets the same US safety standards as domestic food.

## Scope

US importers of food for humans + animals — the entity identified as "FSVP importer" at entry (DUNS + name + email per CBP entry filing). Compliance dates staged by business size.

## Standards covered

PUBLIC license:

- 21 CFR 1 Subpart L (FSVP)

5 clauses:

| Element | Specifics |
|---|---|
| FSVP importer identification (§1.500-505) | DUNS + name + email per CBP entry filing; importer = US owner/consignee OR US agent if no US owner |
| Hazard analysis (§1.504) | Per food + per supplier; biological + chemical + physical + radiological + decomposition (fish) + drug-residue + pesticide-residue + heavy metals + allergens + nutrient-toxicity + IA hazards |
| Supplier evaluation (§1.505) | Written evaluation of supplier performance + food risk; consider audit + sampling + records + FDA inspections + compliance history |
| Supplier verification (§1.506-508) | Per-supplier-and-food: onsite audit (required for SAHCODHA hazards) OR sampling + testing OR records review OR other appropriate activity |
| Corrective actions (§1.508) | Discontinue supplier + investigate + revise FSVP when supplier fails to provide equivalent US protection |

## Composition

```bash
openqms validate --module food-safety --module food-fsvp
```

## When to use

US importers of food (human or animal). Note: domestic-only food manufacturers don't need FSVP; food-safety vertical alone is sufficient.

## When NOT to use

Foreign-supplier-of-food-to-US exports without US-side importer responsibility (the foreign supplier's home-country regulations apply; FSVP is an importer obligation).

Some exemptions per §1.501: alcoholic beverages with TTB jurisdiction; food for personal consumption; juice + seafood manufacturers subject to 21 CFR 120 + 123 with their own importer-equivalent requirements.

## Standards licensing

PUBLIC license.

## Forward work

- VQIP (Voluntary Qualified Importer Program) overlay — FDA priority program for FSVP importers
- SAHCODHA-hazard-specific audit template
- Brand-owner FSVP delegation template (where brand-owner delegates FSVP to manufacturer or distributor)
