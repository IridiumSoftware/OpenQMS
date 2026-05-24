# Aerospace DAL-A — Open QMS class overlay

Class overlay on the **aerospace** vertical. Encodes the highest-rigor DO-178C + DO-254 + ARP4754A requirements applicable when the FHA classifies a failure condition as **Catastrophic**.

## Scope

DAL-A applies to software / hardware functions whose failure may cause loss of the aircraft and/or fatalities. The ARP4754A §5 allocation flow assigns DAL-A based on the FHA's Catastrophic classification per AC/AMC 25.1309.

## Standards covered

- DO-178C:2011 (software)
- DO-254:2000 (hardware)
- ARP4754A:2010 (system-level allocation)

7 clauses encoding rigor delta vs. other DALs:

| Element | DAL-A specifics |
|---|---|
| Structural coverage | **MC/DC** (DO-178C Table A-7 obj 5) — strongest practical coverage criterion |
| Independence | **25-of-71 objectives** (Annex A independence column) |
| Tool qualification | DO-330 **TQL-1** typical for verification tools whose output substitutes for an objective |
| Hardware verification | DO-254 §6.2 **elemental analysis** + §6.3 **safety-specific analyses** (SEU + common-mode + analyses from ARP4761 SSA+CCA) |
| ARP4754A allocation | Rationale traced from FHA Catastrophic classification |

## Composition

```bash
openqms validate --module aerospace --module aerospace-dal-a
```

## When to use

A software / hardware item is allocated DAL-A in your ARP4754A §5 allocation flow OR your FHA classifies a relevant failure condition as Catastrophic.

## When NOT to use

If your FHA classifies the failure condition at a lower severity (Hazardous → DAL-B; Major → DAL-C; Minor → DAL-D; No Safety Effect → DAL-E), use the corresponding aerospace-dal-X overlay instead. ARP4754A §3.5 decomposition can sometimes reduce DAL on individual elements with independence argumentation.

## Standards licensing

DO-178C + DO-254 + ARP4754A + DO-330 are commercially-published copyrighted works (RTCA / SAE International). See repo-root README "Standards licensing — important" section.

## Forward work

- DAL-A class-specific PSAC + PHAC sub-templates with the 25-objective independence matrix pre-populated
- DO-330 TQL-1 tool qualification specific template
