# Traceability

## Design control traceability

Open QMS uses GitHub's native issue-PR linking for design traceability:

```
Design Input (Issue) → Design Output (PR) → Verification (linked test/PR) → Validation
```

### How to maintain traceability

1. **Create design inputs as issues** using the Design Input template
2. **Reference the input issue in your PR** using `Closes #123` or `Fixes #123`
3. **Link verification** by referencing test results or verification PRs in the design output
4. **The traceability workflow** checks that PRs are linked to issues and generates a trace snippet

### Traceability matrix

The `traceability.yml` workflow generates a traceability snippet for each PR showing:
- Which issues are referenced
- Which files were changed
- The PR number

### Repository-wide traceability matrix (forward)

A repository-wide traceability matrix walking the full issue/PR linkage graph (and, eventually, the clause-to-artifact bindings published by each regulatory module) is forward work and will ship with the Open QMS generator engine. Until then, the per-PR snippet above plus GitHub's native issue-PR linkage graph are the working traceability surface.
