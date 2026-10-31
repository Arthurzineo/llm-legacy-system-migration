---
name: differential-testing
description: Use for golden-master and differential verification of two versions or languages with explicit normalization and side-effect comparison.
---

# Differential Testing


## Oracle construction

For each scenario store source/target revision and environment, original fixture, request, expected response, database pre/post state, emitted events, files, permission outcomes and timing semantics where meaningful. Approve normalizers for time/order/random IDs before comparing.

## Execution

Run both environments under equivalent conditions, capture observations, canonicalize approved nondeterminism and produce a structured diff. Classify every mismatch; do not automatically weaken expected results. Confirm unexpected changes with repeat runs and fixtures. Generate `docs/verification/equivalence` reports with actual commands/exit codes.

## Failure mode

If the legacy version cannot execute, use independent requirements and static evidence as weaker oracles, explicitly noting that behavior equivalence cannot be claimed. Manual acceptance is not a machine test result.
