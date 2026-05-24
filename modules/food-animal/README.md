# food-animal — Open QMS class overlay

Class overlay on the **food-safety** vertical. Adds FSMA Preventive Controls for **Animal Food** (21 CFR 507) — separate regulation from human food (21 CFR 117) but mostly parallel structure with animal-food-specific hazard panel.

## Scope

Pet food + livestock feed manufacturers under FDA jurisdiction. Includes by-products of human food manufacturing diverted to animal-food use.

## Standards covered

PUBLIC license:

- 21 CFR 507 (FSMA Preventive Controls for Food for Animals)

4 clauses:

| Element | Specifics |
|---|---|
| Subpart B cGMP | Personnel hygiene + facilities + processes + animal-food-specific medication carry-over prevention; human-food by-product handling |
| Subpart C Food Safety Plan | Animal-food-specific hazards (mycotoxins + nutrient toxicity + drug carryover + zoonotic pathogens + heavy metals + adventitious materials); PCQI with animal-food competence per §507.4 |
| Subpart E Supply-chain | For hazards requiring supply-chain control; approved suppliers + verification activities; FSVP cross-reference for imports |
| §507.38 Recall Plan | Per FDA-Vet recall coordination + 21 CFR 7; notification to veterinarians + retailers + consumers; Reportable Food Registry applies |

## Composition

```bash
openqms validate --module food-safety --module food-animal
```

## When to use

Pet food + livestock feed + animal-food ingredient manufacturers; human-food manufacturers diverting by-products to animal-food.

## When NOT to use

Human-food-only manufacturers (food-safety vertical alone).

## Standards licensing

PUBLIC license.

## Forward work

- Pet food specific overlay (additional AAFCO model regulations adopted by states)
- Medicated feed overlay (21 CFR 558 + 21 CFR 225 + VFD per 21 CFR 558.6)
