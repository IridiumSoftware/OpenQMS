# aerospace-commercial-space — Open QMS class overlay

Class overlay on the **aerospace** vertical. Adds FAA commercial space launch + re-entry licensing requirements (14 CFR Part 450).

## Scope

Commercial space launch + re-entry vehicle operators under FAA-AST jurisdiction. Distinct from civil aviation type certification (Part 21).

## Standards covered

PUBLIC license:

- 14 CFR Part 450 (Commercial Space Launch + Re-entry Licensing)

5 clauses:

| Element | Specifics |
|---|---|
| Subpart B — License application | Vehicle operator license; covers operator qualifications + safety/payload/policy reviews + financial responsibility |
| Subpart C — Safety review | EC ≤ 1×10⁻⁴ per mission collective risk; individual risk ≤ 1×10⁻⁶; system safety + FSS + collision avoidance + flight termination |
| Subpart E — Flight Termination System | Autonomous or operator-controlled; coverage + reliability; pre-flight test |
| Subpart D — Launch + re-entry area control | FAA-AST + spaceport + airspace + maritime + downrange coordination |
| Subpart G — Financial responsibility | MPL for third-party + US government property; insurance or demonstrated financial resources |

## Composition

```bash
openqms validate --module aerospace --module aerospace-commercial-space
```

## When to use

Commercial space launch operators (SpaceX, Blue Origin, Rocket Lab, ULA commercial missions, etc.); re-entry vehicle operators.

## When NOT to use

Civil aviation manufacturers; military space operations (separate DoD framework); satellites (FCC licensing for spectrum, NOAA for Earth observation, but Part 450 only for launch vehicles).

## Standards licensing

PUBLIC.

## Forward work

- Sub-orbital human spaceflight regulatory overlay
- Reusable launch vehicle (RLV) re-entry-specific overlay
- Launch site operator license overlay (Part 420)
