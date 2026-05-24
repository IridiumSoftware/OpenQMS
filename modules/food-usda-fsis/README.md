# food-usda-fsis — Open QMS class overlay

Class overlay on the **food-safety** vertical. Adds USDA-FSIS-specific requirements for meat + poultry + processed-egg-products manufacturers under the Federal Meat Inspection Act, Poultry Products Inspection Act, and Egg Products Inspection Act.

## Scope

USDA-FSIS regulatory framework (distinct from FDA FSMA Preventive Controls):
- Different agency: USDA-FSIS vs. FDA-CFSAN
- Different inspection model: **continuous on-site inspectors** (Public Health Veterinarians + Consumer Safety Inspectors) with authority to suspend operations
- Different recall coordination: 9 CFR 418 + FSIS Directive 8080.1
- Different HACCP regulation: 9 CFR 417 (vs. FDA 21 CFR 117 Subpart C Food Safety Plan)

## Standards covered

PUBLIC license:

- 9 CFR 416 (Sanitation)
- 9 CFR 417 (HACCP Systems)

5 clauses:

| Element | FSIS specifics |
|---|---|
| SSOPs | Written pre-operational + operational sanitation procedures; daily records signed + dated |
| Establishment + grounds + facilities | Construction, lighting, ventilation, plumbing, water/ice/steam |
| HACCP plan | Hazard analysis + CCPs + critical limits + monitoring + corrective + verification; **annual reassessment** + on triggering event |
| Ongoing verification | Direct observation + records review by establishment employee (different from performer) **at least daily** for CCPs |
| Continuous inspector presence | FSIS authority to suspend; establishment must maintain inspector access + records + office space |

## Composition

```bash
openqms validate --module food-safety --module food-usda-fsis
```

## When to use

Meat + poultry + processed-egg manufacturers under FSIS jurisdiction. Often facilities operate under both FSIS (for one product line) + FDA (for other lines) — both vertical+overlays compose for combined-scope facilities.

## When NOT to use

FDA-only food manufacturers (use food-safety alone; 21 CFR 117 framework already in vertical).

## Standards licensing

PUBLIC license.

## Forward work

- FSIS recall directive 8080.1 standalone workflow
- Catfish inspection program (transferred from FDA to FSIS per 2008 Farm Bill)
- FSIS export certification workflow
