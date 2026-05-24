# automotive-defense — Open QMS class overlay

Class overlay on the **automotive** vertical. Adds defense-specific requirements for military ground vehicles + defense variants of commercial platforms.

## Scope

Tanks, armored personnel carriers, MRAPs, JLTV, military trucks, military variants of commercial heavy vehicles.

## Standards covered

All PUBLIC license:

- MIL-STD-882E
- ITAR (USML Category VII — Ground Vehicles)
- EAR

4 clauses:

| Element | Specifics |
|---|---|
| MIL-STD-882E ground-vehicle | PHA / SHA / SSHA / O&SHA covering crew protection + ballistic/blast survivability + mobility safety + weapon-system integration + EW exposure + NBC protection |
| USML Cat VII | Tanks + military ground vehicles + specially-designed components; commercial-platform modifications trigger ITAR |
| EAR Cat 9 + 0 | ECCNs 9A991 (commercial aircraft parts) / 0A606 (military ground items not in USML) / 0A987 (optical sighting) — relevant for dual-use components |
| CMMC readiness | DFARS 252.204-7012 + NIST SP 800-171 + CMMC tiers; composes with iso-27001 + regulated-ai |

## Composition

```bash
openqms validate --module automotive --module automotive-defense
```

## Standards-licensing scope-boundary

PUBLIC license for the regulations; ADOPTER-RESTRICTED for controlled data handled under them. **Do NOT commit ITAR-restricted technical data to a public Git repository.**

## When to use

DoD ground-vehicle acquisition contractors; military variants of commercial platforms; CMMC-pursuing automotive contractors.

## When NOT to use

Civil automotive (automotive alone).

## Standards licensing

PUBLIC; adopter-restricted data scope.

## Forward work

- CMMC Level 2/3 detailed overlay
- DFARS 252.204-7012 + NIST SP 800-171 standalone overlay (cross-cutting for any DoD contractor across all verticals)
