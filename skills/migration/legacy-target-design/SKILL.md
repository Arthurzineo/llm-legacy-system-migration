---
name: legacy-target-design
description: Use after user intake to design and approve a target architecture, migration mode, data mapping and staged rollback strategy.
---

# Legacy Target Design


## Decision workflow

1. Compare version upgrade, replatforming, incremental strangler with compatibility adapters, hybrid coexistence and total rewrite. State constraints, trade-offs and conditions favoring each.
2. Recover stable requirements, domain invariants, use cases, data ownership, interfaces, error semantics, idempotency and concurrency guarantees.
3. Draw the simplest target architecture: C4 context/container/component as needed; modules vs services justified by independent change/deployment requirements; frontend/database/API layouts; trust boundaries, observability and deployment topology.
4. Compare each legacy business rule and state transition to its approved target behavior. Record deliberate security or UX changes in ADRs; no accidental breaking changes.
5. Design a data migration and reconciliation plan, rollback/dual-run constraints, and vertical-slice order. Include unknowns, performance and operational criteria.
6. Save `docs/target/architecture.md`, `requirements.md`, `data-migration.md`, `adrs/`, and traceability links. Obtain a real Chief/user gate before implementation.

## Completion criteria

Architecture is not selected merely because a target language was named. Critical requirements and data invariants have verification plans; no component is approved based only on a generated class diagram.

## Evidence and completion contract

- **Activation:** Read only for a relevant task; record NOT_APPLICABLE when its conditions do not hold.
- **Concrete result:** Versioned ADRs, invariants, migration seams and tests for approved target structure.
- **Verification:** Cite source revision, file/symbol, executed command, exit status, observation scope, artifacts, timestamps and exceptions where applicable. A written plan is not an executed check. Use PASS, FAIL, PARTIAL, NOT_RUN, NOT_APPLICABLE rather than an unsupported green status.
- **Stop and escalate:** Missing source, tooling, authorization, or objective evidence blocks a completion claim. Chief-only reviews are non-independent.
