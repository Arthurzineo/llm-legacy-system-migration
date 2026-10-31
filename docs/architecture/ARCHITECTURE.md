# Migration Architecture

The **generic ORCA layer** owns agent session discovery, contract/role authority, worktree ownership, diaries, task state and review gates. The **migration layer** owns static inspection, selected documentation, optional isolated runtime, user questionnaire, target design, incremental implementation and acceptance verification.

```mermaid
flowchart TD
  User[User or sponsor] --> Chief[ORCA Chief: always present]
  Runtime[Actual ORCA agent roster] --> Chief
  Chief --> Contract{Runtime capacity?}
  Contract -->|Chief only| Solo[Solo scoped tasks + explicit self-review]
  Contract -->|More agents| Workers[Delegated workers and optional reviewers]
  Solo --> P1[Part 1: static discovery]
  Workers --> P1
  P1 --> G1[Evidence and diagram gate]
  G1 --> Optional{Part 1.1: user opt-in?}
  Optional -->|Yes| Dynamic[Isolated runtime and characterization]
  Optional -->|No / Defer| NoDynamic[Record decision and uncertainty]
  Dynamic --> P2[Part 2: questionnaire and target design]
  NoDynamic --> P2
  P2 --> Migrate[Incremental migration]
  Migrate --> Verify[Independent verification or disclosed limitation]
  Verify --> Release[Reconciliation, rollout and rollback]
  Chief -.-> Records[.orca + versioned evidence: authoritative]
  Records -.-> Graphify[Graphify: derived relationships]
  Records -.-> Memory[AI Memory v2.0.1: derived cross-agent memory]
```

Mermaid is explanatory. No external service is implied to be connected. Companion modules must accept absence of Graphify, workers, and AI Memory without fabricating results. See `docs/architecture/ORCA-OPERATING-MODEL.md`.
