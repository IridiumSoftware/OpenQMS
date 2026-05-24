# automotive-motorcycle — Open QMS class overlay

Class overlay on the **automotive** vertical. Adds ISO 26262 Part 12 motorcycle adaptations for 2-3 wheeled vehicles.

## Scope

Motorcycles + similar 2-3 wheeled vehicles intended for public road use. Excludes mopeds + e-bikes per regional regulatory definitions (varies).

Motorcycle functional safety presents challenges distinct from cars:
- Rider not enclosed in vehicle body (severity of any incident higher)
- Lateral dynamics + stability much harder to control via vehicle systems
- Smaller margin for fault detection + warning
- Rider-vehicle interaction qualitatively different

## Standards covered

- ISO 26262 Part 12 (motorcycle adaptation) — **commercial license** (ISO)

4 clauses:

| Element | Specifics |
|---|---|
| Scope | 2-3 wheeled public-road motor vehicles |
| **MSIL (instead of ASIL)** | Motorcycle Safety Integrity Level A-D — analogous to ASIL but with motorcycle-specific S × E × C criteria |
| Controllability for rider | Rider skill + reaction + lateral-stability control; controllability classes adapted |
| Architectural adaptations | Limited space + power; redundancy strategies (rider sometimes serves as fall-back) |

## Composition

```bash
openqms validate --module automotive --module automotive-motorcycle
```

## When to use

Motorcycle + 2-3 wheeled vehicle manufacturers under ISO 26262 scope.

## When NOT to use

Cars + light trucks (use automotive vertical with ASIL overlays; Parts 1-11 apply directly without motorcycle adaptation).

## Standards licensing

ISO 26262 Part 12 commercial.

## Forward work

- Specific MSIL-A/B/C/D class overlays (analogous to automotive-asil-X structure)
- Electric motorcycle-specific overlay (battery + power-electronics integration distinct from cars)
- Off-road motorcycle / ATV overlay (different regulatory scope)
