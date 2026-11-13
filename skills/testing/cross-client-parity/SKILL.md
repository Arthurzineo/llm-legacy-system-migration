---
name: cross-client-parity
description: Verify shared business behavior between desktop, web, mobile or API clients across a real backend and explicit compatibility contract.
---

# Cross-Client Parity

## Use
P008 when two or more client channels exist, or when migrating an API consumed by old and new clients. Otherwise document NOT_APPLICABLE.

## Procedure
1. Inventory clients and deployed version matrix. Extract common domain invariants and explicitly permitted channel differences.
2. Use isolated disposable fixtures with equivalent identities, permissions, input and database snapshots.
3. Execute actual client journeys against the same test backend for state creation, retrieval, updates, errors, retries, authorization and version skew. Distinguish mocks from native/browser end-to-end evidence.
4. Compare API responses, persistence, emitted events, UI outcomes and security boundaries; classify regressions, intended differences and unmeasured paths.
5. Publish coverage by journey/client/version, evidence links, failed cases and owner-approved exceptions.

## Output
`docs/operations/client-parity.md` and machine-readable matrix. A sample of passing journeys is not universal parity.
