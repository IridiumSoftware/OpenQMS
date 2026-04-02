# Regulatory Overview

Open QMS is designed to support compliance with regulated quality systems. It does not guarantee compliance — that depends on how you configure it, how disciplined your team is, and what supplementary controls you implement.

## What GitHub provides natively

- **Immutable history** (if force-push is disabled)
- **Timestamped, author-identified changes** (Git commits)
- **Approval workflows** (PR reviews with required reviewers)
- **Automated enforcement** (CI/CD status checks)
- **Access control** (organization, team, and repository permissions)
- **Configuration management** (Git was literally designed for this)

## What requires supplementary tooling

| Gap | Regulation | Suggested approach |
|---|---|---|
| Electronic signatures with "meaning" | 21 CFR Part 11 | GPG commit signing + role attestation in commit message, or external e-signature integration |
| Training management | ISO 13485 §6.2, 820.25 | Training trigger workflow (included) + LMS for completion tracking |
| Document rendering for non-technical users | 820.70 | MkDocs (included) or PDF generation via CI |
| Traceability matrix | ISO 13485 §7.3 | CI-generated matrix (included) + periodic manual audit |
| Document-level access control | 820.22 (audit confidentiality) | Separate repos with restricted access |
| QMS metrics dashboard | ISO 13485 §8.2.3 | GitHub API + custom dashboard |
| Binary file management | General | Git LFS for files > 1 MB |

## Validation

Before using Open QMS for regulated activities, you must validate it. A validation protocol should cover:

1. **IQ:** Configuration matches requirements (branch protection, permissions, CODEOWNERS)
2. **OQ:** Workflows function correctly (unauthorized merges blocked, training triggers fire, traceability checks catch missing links)
3. **PQ:** End-to-end scenarios (design change lifecycle, CAPA lifecycle, document revision with training)
4. **Revalidation triggers:** Platform updates, configuration changes, new workflow additions
