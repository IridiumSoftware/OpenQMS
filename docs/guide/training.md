# Training Management

## How training triggers work

When a controlled document (SOP or policy) is updated on the `main` branch, the `training-trigger.yml` workflow automatically creates a training assignment issue.

### What happens

1. An SOP is merged to `main`
2. The workflow detects the changed document
3. It reads `docs/qms-config.yml` for the trainee list
4. It creates a GitHub issue titled "Training Required: [Document Title]"
5. The issue is labeled `training` and `auto-generated`
6. Each trainee is mentioned in the issue

### Completing training

Trainees complete training by:

1. Reading the updated document
2. Checking the confirmation box in the issue
3. Closing the issue

### Training records

The closed training issues serve as training records:
- **Who** was trained (issue assignee / commenter)
- **What** document (linked in issue body)
- **When** training was completed (issue close date)
- **Which version** (commit SHA referenced in issue)

### Configuration

Edit `docs/qms-config.yml` to set the trainee list:

```yaml
trainees:
  - alice
  - bob
  - charlie
```
