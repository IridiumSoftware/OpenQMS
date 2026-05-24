# Automotive CAL-4 — Open QMS class overlay

Class overlay on the **automotive** vertical. **Highest** ISO/SAE 21434 Cybersecurity Assurance Level. Assigned when TARA identifies high-impact / high-feasibility damage scenarios — typically safety-affecting (e.g., compromise of brake / steering / acceleration ECU; back-end server controlling fleet OTA updates).

## Scope

TARA's impact-and-feasibility matrix (per Annex E informative) yields CAL-4 for damage scenarios with both high impact (Safety / Financial / Operational / Privacy) and non-low attack feasibility.

## Standards covered

- ISO/SAE 21434:2021

5 clauses encoding the highest-rigor cyber tier:

| Element | CAL-4 specifics |
|---|---|
| Independent cybersecurity assessment | **REQUIRED** (§6.4.7 + Annex C) — different organizational unit or external |
| V&V rigor (§10 + §13) | Security functional testing + vulnerability scanning + **fuzz testing** + **penetration testing** + **side-channel analysis** (where attack-feasibility analysis identifies side-channel threats) |
| Continuous activities (§11) | **Formal vulnerability monitoring** with response-time commitments in CSMS + **rehearsed incident-response playbooks** + sustained cybersecurity through end-of-support transition |
| Safety-security interaction | When item is also ASIL-rated (typically ASIL-D or ASIL-C at CAL-4 level), Cybersecurity Concept (Safety Concept Part C) must document the interaction |

## Composition

```bash
openqms validate --module automotive --module automotive-cal-4
# Top-rigor safety+cyber composite:
openqms validate --module automotive --module automotive-asil-d --module automotive-cal-4
```

## When to use

TARA yields CAL-4 (high-impact, non-low-feasibility damage scenarios — typically safety-affecting).

## When NOT to use

Lower CAL tiers (1/2/3) for less severe damage-scenario combinations.

## Standards licensing

ISO/SAE 21434:2021 commercial (ISO + SAE International).

## Forward work

- CAL-4 Cybersecurity Case template integrating independent assessment evidence
- Pentest + fuzz + side-channel test plan templates
