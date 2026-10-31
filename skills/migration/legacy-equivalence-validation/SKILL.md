---
name: legacy-equivalence-validation
description: Use to compare behavior and side effects between legacy and target implementations without accepting compilability alone as equivalence.
---

# Legacy Equivalence Validation


## Verification design

Build a behavioral oracle from recorded legacy tests and independent domain acceptance criteria. Classify an unavailable oracle as `not_observed`, never as equivalent. For each case capture input, user/permissions, initial database state, environment, request/response, errors, final state and emitted side effects.

## Comparison

1. Execute source and target in isolated repeatable environments with **equivalent fixtures**.
2. Normalize nondeterministic fields only if the interface contract explicitly allows it. Record normalizers and their justification.
3. Compare outputs, state transitions, authorization, ordering, atomicity, concurrency, idempotency and persistence. Treat clock/encoding/float behavior explicitly.
4. Categorize differences as `regression`, `approved_intentional_change`, `legacy_defect_remediated`, `environment_mismatch`, or `unknown`.
5. Run supplementary QA: unit, integration, API contract, performance, SAST/SCA and risk-scoped DAST. Ensure quality/test tooling actually executed.
6. Request reviewer acceptance when possible; self-validation cannot be called independent. Produce machine-readable reports and traceability back to use cases/business rules.

## Gate

Each critical acceptance criterion has a valid test or a recorded risk exception; failed or skipped tests are never silently hidden. No claim of equivalence is stronger than actual observed coverage.
