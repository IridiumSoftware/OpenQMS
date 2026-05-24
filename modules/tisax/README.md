# tisax — Open QMS cross-cutting overlay

Trusted Information Security Assessment Exchange (TISAX) overlay. Composes with any vertical.

## Scope

Automotive industry-specific IS framework based on VDA-ISA. Required by most German + European OEMs for Tier-1+ suppliers handling customer-proprietary information:

- Design data (CAD + simulation + specifications)
- Prototype data (pre-series vehicles + concept cars + camouflaged test vehicles)
- Vehicle test data
- Customer/dealer/owner personal data

## Standards covered

Commercial license (ENX Association on behalf of VDA):

- TISAX (VDA-ISA v6.0)

5 clauses:

| Element | Specifics |
|---|---|
| Information Security Management | ISMS aligned with ISO 27001 principles; automotive-supply-chain-specific control catalog |
| Prototype Protection | Pre-series prototypes + concept vehicles + camouflaged test vehicles; physical + procedural + personnel controls; photography prevention |
| Data Protection | GDPR-aligned controls for personal data in automotive context |
| Assessment Objectives + Levels | Info High / Very High + Prototype + Data Protection labels; AL 1 self / AL 2 remote-document / AL 3 full onsite |
| Assessor + Exchange | ENX-approved audit providers; results on ENX Portal shareable with multiple OEMs; certificate valid 3 years |

## Composition

```bash
openqms validate --module automotive --module tisax
# Often combined with iso-27001:
openqms validate --module automotive --module tisax --module iso-27001
```

## When to use

Automotive Tier-1+ suppliers handling OEM proprietary information; engineering services providers (development partners); test + validation service providers; prototype builders + coachbuilders.

## When NOT to use

Non-automotive industries (TISAX is automotive-specific). If only ISO 27001 is required (no OEM mandate), use iso-27001 directly.

## Standards licensing

VDA-ISA commercial. ENX assessment + label issuance commercial (audit-provider fee + ENX listing fee).

## Forward work

- Prototype Protection specific workflow template (camouflage release authority + photography incident response)
- Multi-OEM share-permissions matrix template
- TISAX assessment-readiness checklist per Assessment Level
