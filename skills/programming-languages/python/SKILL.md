---
name: python
description: Use for Python architecture, modernization, typing, packaging, testing, async correctness and API compatibility in target projects.
---

# Python


## Workflow

1. Identify Python runtime, requirements/lockfiles, imports, package layout and binary extensions. Prefer isolated environments; pin dependencies and avoid unsupported versions.
2. Make public contracts explicit through meaningful type hints, dataclasses/Pydantic only when justified, typed exceptions and documented serialization. Avoid hidden runtime imports and fragile monkeypatch dependencies.
3. Preserve business behaviors for date/time, decimal precision, truthiness, encoding and mutable defaults when migrating from another language; document deliberate changes.
4. Keep synchronous and asynchronous paths unambiguous; review cancellation, connection pooling, transaction rollback, idempotency and exception propagation.
5. Use pytest/unittest and appropriate typing/lint tools if installed. Validate real command output; do not treat static type correctness as runtime equivalence.
6. Test negative paths, schema changes, dependency pinning and race conditions where applicable. Cross-check with golden-master behavior.

## Completion

Reproducible environment, bounded module change, passing tests, known incompatibilities and migration evidence recorded.
