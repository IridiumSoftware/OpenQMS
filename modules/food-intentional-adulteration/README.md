# food-intentional-adulteration — Open QMS class overlay

Class overlay on the **food-safety** vertical. Adds FSMA Intentional Adulteration Rule (21 CFR 121) — addresses food defense protecting food from intentional adulteration intended to cause wide-scale public health harm (terrorism + economically motivated adulteration).

Distinct from accidental contamination (handled by HACCP / Preventive Controls per food-safety vertical).

## Scope

Domestic + foreign facilities required to register with FDA per 21 CFR 1 Subpart H AND that manufacture / process / pack / hold food for consumption in the US, with compliance dates staged by business size (largest first).

Exemptions per §121.5: very small businesses; certain types of food (e.g., alcoholic beverages with TTB jurisdiction); holding of food (except at containers + bulk storage); packing/repacking + labeling/relabeling under certain conditions; on-farm activities.

## Standards covered

PUBLIC license:

- 21 CFR 121 (FSMA Intentional Adulteration Rule)

5 clauses:

| Element | Specifics |
|---|---|
| Food Defense Plan (§121.126) | Written plan + 3-year reanalysis cadence |
| Vulnerability assessment (§121.130) | Per-step evaluation; identify Actionable Process Steps (APS — significant vulnerabilities) |
| Mitigation strategies (§121.135) | Per-APS controls (access controls + input inspection + supervision + tamper-evident packaging) |
| Monitoring + corrective + verification (§121.140) | Implementation monitoring + corrective actions + verification |
| FDQI (§121.4) | Food Defense Qualified Individual — training or experience qualified to perform VA + select mitigation + prepare FDP + reanalysis |

## Composition

```bash
openqms validate --module food-safety --module food-intentional-adulteration
```

## When to use

Food facilities subject to §121.3 applicability. Particularly relevant for: large-scale processors (high public health impact if compromised); facilities with public-access vulnerabilities; facilities handling concentrated additives where small contamination could affect large product volumes.

## When NOT to use

Very small businesses + exempt facility types per §121.5.

## Standards licensing

PUBLIC license.

## Forward work

- Food fraud (EMA — economically motivated adulteration) standalone overlay (related to but distinct from IA Rule)
- FDA Food Defense Plan Builder tool integration
