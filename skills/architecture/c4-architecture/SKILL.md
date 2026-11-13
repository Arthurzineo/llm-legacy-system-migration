---
name: c4-architecture
description: Use when producing context/container/component/deployment views that explain existing or proposed software boundaries.
---

# C4 Architecture


## Selection

Choose the smallest C4 view that answers a concrete design question: system context for actors/integrations; container for deployable runtimes and data stores; component for responsibilities and public interfaces; deployment for infrastructure/security zones. **A C4 container does not mean a Docker container.**

Use real code/runtime evidence for current-state views. Distinguish verified from inferred boundaries and proposed target design. Label relation type, protocol, direction, data ownership and trust boundary as relevant. Do not equate a directory with a service or invent a system boundary for visual symmetry.

Keep diagrams as editable Mermaid/PlantUML, record source revision and references to evidence, and validate rendering with real tools when available. For migration, show coexistence, adapters and phased traffic/state ownership.

## Execution-quality contract

- **Selection:** Activate only when this skill's named task is necessary; otherwise explicitly mark NOT_APPLICABLE. Do not load adjacent skills by default.
- **Minimum verifiable result:** Editable diagrams linked to source, boundaries and rendering verification; inference labels.
- **Evidence status:** Attach exact source revision, tool invocation, exit status, observed output, scope and timestamp for every executed check. Label proposals as PLANNED, missing tools as NOT_RUN, incomplete observations as PARTIAL and observed checks as PASS/FAIL. Never convert a generated document, skill activation or model assertion into test evidence.
- **Failure behavior:** On missing authority, input, tool or acceptance evidence, stop the affected operation, record a blocker and report the narrowest safe next action. Do not claim independent review when run by the Chief alone.
