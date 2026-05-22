# Open QMS — medical-devices regulatory module

First reference module shipped with Open QMS. Targets the medical-device QMS surface across ISO 13485:2016, 21 CFR 820, 21 CFR Part 11, EU MDR 2017/745, IEC 62304, IEC 62366-1, IEC 60601-1, ISTA 2A/3A, MDSAP, and (as cross-cutting overlay) ISO 27001.

## Status (v0.1.0)

`module.yaml` is a **minimal seed**. It declares four clauses as in-scope and binds them to the three artifact templates the public repository currently ships:

| Clause | Title | Bound templates |
|---|---|---|
| `ISO13485-4.2.4` | Document control | Quality policy, SOP template |
| `ISO13485-7.3` | Design and development | Design input template |
| `CFR820-820.30` | Design controls | Design input template |
| `CFR820-820.40` | Document controls | Quality policy, SOP template |

The validation harness (`openqms validate --module medical-devices`) passes on this manifest: every clause has at least one binding, no template binds a non-existent clause.

## Coverage roadmap

The full medical-devices regulatory crosswalk — ISO 13485 clauses 4.1.6 / 4.2.3 / 4.2.4 / 4.2.5 / 6.3 / 7.3 / 8.2.3, 21 CFR 820 sections 820.20 / 820.22 / 820.30 / 820.40 / 820.70 / 820.90 / 820.100 / 820.180–198, 21 CFR Part 11 (including the §11.50 signature-meaning gap), EU MDR articles and annexes, IEC 62304, IEC 62366-1, IEC 60601-1, ISTA, MDSAP, ISO 27001 — is maintained in the project's private spec discipline tree (not redistributed in this public repo).

As additional artifact templates land in `templates/`, additional clauses are progressively added to `module.yaml` and bound to those templates. Every addition must keep `openqms validate` green.

## Standards licensing

Clauses are referenced by number and normative summary only. The summaries are paraphrases written by the module maintainer; the standard text itself is not redistributed. Adopters implementing against these standards must obtain their own licensed copies of ISO 13485, IEC 62304, IEC 62366-1, IEC 60601-1, ISTA 2A/3A, MDSAP audit-model documents, and ISO 27001 from their respective publishers. See the repo-root `README.md` "Standards licensing — important" section.
