## Architecture

```mermaid
flowchart TD

A[Developer Laptop]
A --> B[Git]
A --> C[DVC]
A --> D[Python]

B --> E[GitHub Repository]
C --> F[AWS S3 Bucket]

E --> G[Team Members]
F --> G
```

## Workflow

1. Developer tracks dataset using DVC
2. Dataset stored in S3
3. Code stored in GitHub
4. Team clones repo
5. Team runs `dvc pull`
