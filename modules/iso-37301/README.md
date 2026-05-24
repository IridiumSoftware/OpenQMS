# iso-37301 — Open QMS cross-cutting overlay

ISO 37301:2021 Compliance Management System overlay. Replaces ISO 19600:2014. Composes with any vertical.

## Scope

Broader than ISO 37001 anti-bribery — covers compliance with ALL obligations: legal + regulatory + contractual + voluntary + standards + organizational policies. Follows Annex SL → composes cleanly with every other MS overlay.

## Standards covered

Commercial license (ISO):

- ISO 37301:2021

6 clauses:

| Element | Specifics |
|---|---|
| §5.2 Compliance policy | Commits to obligation compliance + continual improvement + whistleblower protection + non-compliance sanctions |
| §5.3 Compliance function | Independent + authoritative + competent + resourced + direct reporting to governing body. **Broader than ISO 37001's anti-bribery compliance function** |
| §6.1.2-3 Obligation ID + risk | Determine + maintain compliance obligations; risk assessment per ISO 31000 framework |
| §8.1-2 Operational planning + controls | Financial + non-financial + procurement + outsourcing + training/awareness/communication |
| §8.3 Raising concerns + investigation | Confidential + anonymous channel + non-reprisal + investigation + disciplinary |
| §9.1 Monitoring + measurement | Compliance performance indicators + reporting to governing body |

## Composition

```bash
openqms validate --module <vertical> --module iso-37301
# Often combined with ISO 37001 anti-bribery (37301 is broader):
openqms validate --module <vertical> --module iso-37301 --module iso-37001
```

## When to use

Organizations with broad multi-domain compliance obligations: financial services, healthcare, large multi-jurisdictional enterprises, regulated industries with multi-framework exposure.

## When NOT to use

Single-narrow-domain compliance scope (anti-bribery only → use iso-37001; information security only → use iso-27001).

## Standards licensing

ISO 37301 commercial.

## Forward work

- Compliance Maturity Assessment template (per ISO 37301 maturity progression)
- Compliance Officer designation + JD template
