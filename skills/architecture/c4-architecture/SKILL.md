---
name: c4-architecture
description: Use when producing context/container/component/deployment views that explain existing or proposed software boundaries.
---

# C4 Architecture


## Selection

Choose the smallest C4 view that answers a concrete design question: system context for actors/integrations; container for deployable runtimes and data stores; component for responsibilities and public interfaces; deployment for infrastructure/security zones. **A C4 container does not mean a Docker container.**

Use real code/runtime evidence for current-state views. Distinguish verified from inferred boundaries and proposed target design. Label relation type, protocol, direction, data ownership and trust boundary as relevant. Do not equate a directory with a service or invent a system boundary for visual symmetry.

Keep diagrams as editable Mermaid/PlantUML, record source revision and references to evidence, and validate rendering with real tools when available. For migration, show coexistence, adapters and phased traffic/state ownership.
