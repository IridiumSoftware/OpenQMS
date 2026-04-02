# Auditor Walkthrough

This guide helps auditors navigate a GitHub-based QMS. If you're accustomed to traditional document management systems, this page maps familiar concepts to their GitHub equivalents.

## Key concepts

| Traditional QMS | GitHub Equivalent |
|---|---|
| Document management system | Git repository |
| Current effective version | `main` branch |
| Document revision history | Git log / commit history |
| Document approval signature | Pull request approval |
| Change control record | Pull request (with linked issue) |
| CAPA record | GitHub issue (CAPA template) |
| Nonconformance report | GitHub issue (NCR template) |
| Training record | GitHub issue (auto-generated, closed = complete) |
| Design input | GitHub issue (design input template) |
| Audit trail | Git log + GitHub audit log |
| Quality record archive | Git history (immutable) |

## How to find things

### Current effective documents
Browse the `main` branch of the repository. Everything on `main` is the current effective version.

### Revision history of a specific document
Click the document, then click "History" to see all changes with dates, authors, and diffs.

### Who approved a document change
Find the Pull Request that merged the change. The "Reviewers" section shows who approved and when.

### CAPA and NCR records
Go to Issues. Filter by label: `capa` or `ncr`. Open issues are active; closed issues are complete.

### Training records
Go to Issues. Filter by label: `training`. Each closed issue is a completed training record.

### Design traceability
Issues labeled `design-input` link to PRs (design outputs) which link to verification records. Follow the links.

## Generating reports

For a formatted view of the QMS, visit the GitHub Pages site (if enabled). This renders all markdown documents as a browsable website.

For a PDF export of any document, use the browser's print function on the rendered page.
