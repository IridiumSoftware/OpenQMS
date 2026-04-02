# Document Control

## How document control works in Open QMS

Every controlled document lives in a Git repository. Changes follow the PR workflow:

1. **Author** creates a branch and edits the document
2. **Author** opens a Pull Request
3. **CI** checks document metadata (document_id, version, effective_date, owner, status)
4. **CODEOWNERS** routes the PR to required reviewers
5. **Reviewers** approve (this is the controlled document approval)
6. **Merge to main** = document is effective

## Document metadata

Every controlled document must include YAML frontmatter:

```yaml
---
document_id: SOP-QA-001
title: "Document Title"
version: "2.1"
effective_date: 2026-04-15
owner: "Jane Smith, Quality Manager"
status: effective
approved_by: "John Doe, VP Quality"
approval_date: 2026-04-14
---
```

The `doc-control.yml` workflow will fail the PR if required fields are missing.

## Version control

- **Version** must be incremented on every change. The CI workflow warns if it isn't.
- **Effective date** should be set to the planned go-live date, not the merge date.
- **Status** should be `draft` during development and `effective` when approved.

## Obsolete documents

Obsolete documents are not deleted — they remain in Git history. To mark a document obsolete:

1. Change `status: effective` to `status: obsolete`
2. Add `obsolete_date: YYYY-MM-DD` and `superseded_by: [new document_id]`
3. Merge via normal PR process

The document remains accessible in history but the current version clearly shows it's obsolete.
