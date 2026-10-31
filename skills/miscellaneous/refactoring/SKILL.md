---
name: refactoring
description: Use for behavior-preserving refactoring, removal of genuine duplication, simplified dependencies and safe change sequencing.
---

# Refactoring


## Workflow

1. Describe the concrete design problem and intended maintenance outcome; map affected public behavior and consumers.
2. Stabilize tests including boundary, error, persistence and concurrent paths. Use characterization tests if no historical tests exist.
3. Make one reversible structural change (extract function, introduce adapter, isolate invariant owner, break dependency cycle, remove verified dead code). Do not silently change business rules or authentication semantics.
4. Verify compile, tests, mutation/complexity/duplication evidence where available and review neighboring change impact. An extraction that increases coupling is not automatically better.
5. Update architecture diagram/ADR if interface or dependency ownership changed, record original vs target behavioral contract and any intentional deviation.

## Completion

Same approved observable behavior; smaller dependency/change surface; measured outcome or candidly unknown metrics; rollback possible.
