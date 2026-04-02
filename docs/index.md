# Open QMS

An open-source, GitHub-native Quality Management System.

Open QMS provides the infrastructure to run a compliant QMS directly on GitHub. Pull requests for approvals, CI/CD for enforcement, Git for the audit trail.

## Why

Traditional QMS platforms are expensive, inflexible, and disconnected from where engineering work actually happens. If your team already lives in GitHub, your quality system should too.

Open QMS doesn't replace your quality processes. It gives them a better home.

## How it works

| QMS Activity | GitHub Mechanism |
|---|---|
| Document approval | PR with required reviewers |
| Change control | Issue → PR → review → merge |
| CAPA | Issue with structured template |
| Training | Auto-generated issues on doc update |
| Release | Tag → CI verification → GitHub Release |
| Audit trail | Git history (immutable) |

## Getting started

See the [Quick Start Guide](guide/quickstart.md).
