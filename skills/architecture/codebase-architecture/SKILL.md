---
name: codebase-architecture
description: Use when choosing modular boundaries, API contracts, data ownership and dependency direction in existing or new software.
---

# Codebase Architecture


## Design sequence

1. Identify business capabilities, invariant owners, data writers, public contracts, change reasons and operational constraints.
2. Group code by cohesion of change; define allowed dependency direction and separate replaceable infrastructure from stable policy where useful.
3. Define interface inputs/outputs, authorization, error semantics, retries, ordering, idempotency and consistency. Avoid cross-module direct writes that bypass an invariant.
4. Compare modular monolith against services based on deployment/scaling/failure boundaries, not trend.
5. Plan a safe migration path using characterization tests, adapters and incremental routing; identify the evidence that permits retiring the old path.
6. Verify with realistic change scenarios and check for cycles, duplicated rules, unnecessary abstraction, too-wide interfaces and untested shared state.

## Output

Current and proposed boundaries, dependencies, public contracts, consequences and ADRs with a verified test strategy.

## Evidence and completion contract

- **Activation:** Read only for a relevant task; record NOT_APPLICABLE when its conditions do not hold.
- **Concrete result:** Evidence-backed dependency diagram, decision record and behavioral contract checks.
- **Verification:** Cite source revision, file/symbol, executed command, exit status, observation scope, artifacts, timestamps and exceptions where applicable. A written plan is not an executed check. Use PASS, FAIL, PARTIAL, NOT_RUN, NOT_APPLICABLE rather than an unsupported green status.
- **Stop and escalate:** Missing source, tooling, authorization, or objective evidence blocks a completion claim. Chief-only reviews are non-independent.
