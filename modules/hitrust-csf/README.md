# hitrust-csf — Open QMS cross-cutting overlay

HITRUST Common Security Framework overlay. Composes with any vertical.

## Scope

Healthcare-originated but now broadly applicable IS framework. Provides a single integrated audit pathway covering multiple regulatory + industry requirements through cross-framework mapping.

## Standards covered

Commercial license (HITRUST Alliance):

- HITRUST CSF v11.x

4 clauses:

| Element | Specifics |
|---|---|
| CSF Framework architecture | 19 domains + 50 control objectives + 156 controls (v11.x); implementation levels driven by org risk factors |
| MyCSF assessment scoping | r2 (2-year risk-based) / e1 (1-year essentials) / i1 (1-year implemented) — scope determines assessment type |
| External assessor | Authorized External Assessor Firm performs validated assessment; HITRUST QA review before certification |
| Multi-framework mapping | Authoritative sources include HIPAA + HITECH + ISO 27001 + NIST SP 800-53 + PCI DSS + GDPR + state privacy + sector regs; one assessment can satisfy multiple frameworks |

## Composition

```bash
openqms validate --module <vertical> --module hitrust-csf
# Healthcare composition:
openqms validate --module medical-devices --module hitrust-csf --module iso-27001
```

## When to use

Healthcare organizations (HIPAA covered entities + business associates); SaaS serving healthcare customers; organizations valuing single-assessment-multi-framework audit efficiency.

## When NOT to use

Organizations exclusively under non-healthcare frameworks where HITRUST mapping adds no value (use direct framework instead).

## Standards licensing

HITRUST CSF commercial (HITRUST Alliance).

## Forward work

- HIPAA Security Rule standalone overlay (45 CFR Part 164 Subpart C)
- HIPAA Privacy Rule overlay (45 CFR Part 164 Subpart E)
- HITRUST AI Risk Management overlay (recent HITRUST addition)
