# Release Management

## Release gate workflow

When you push a tag matching `v*` or `release-*`, the `release-gate.yml` workflow runs:

1. **Checks required documents exist** (quality policy, quality manual)
2. **Checks for open blocking issues** (labels: `release-blocker`, `capa-open`, `ncr-open`)
3. **Checks document statuses** (warns on draft documents)
4. **Creates a GitHub Release** if all checks pass

## How to release

```bash
# Tag the release
git tag v1.0.0
git push origin v1.0.0

# The release gate runs automatically
# If it passes, a GitHub Release is created
```

## Blocking conditions

A release is blocked if:
- Required documents are missing from the repository
- Any issue has the `release-blocker`, `capa-open`, or `ncr-open` label

## Customization

Edit the `required_files` array in `.github/workflows/release-gate.yml` to define which documents must exist for a release.

Edit the `blockingLabels` array to change which issue labels block releases.
