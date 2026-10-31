# Verification Strategy

## Evidence tiers

1. Static source and schema inspections support structural claims, not observed runtime equivalence.
2. A reproducible baseline test against the original legacy system supports observed behaviors within its fixture coverage.
3. Differential tests compare canonical outputs, database transitions, emitted events/files and security-relevant side effects on equivalent inputs.
4. Quality gates measure compilation, test success, duplication, complexity/coverage, mutation strength and dependency direction. A metric tool that did not run is marked `not_measured`.
5. Independent reviewer approval is required when available; Chief-only self-review is reported as non-independent.

## Comparators

Normalize timestamps, random IDs and order only when the contract explicitly allows it. Distinguish intentional security fixes from regressions. For concurrency verify retries, idempotency, transaction atomicity and conflict resolution.

## Testing pyramid and process

Use characterization tests before migration when possible, then contract/unit, integration, database, end-to-end, property-based and mutation tests proportionate to risk. TDD follows red/green/refactor; BDD expresses domain outcomes in Given/When/Then and must execute rather than remain prose. Introduce smoke/regression gates at each slice, not only at cutover.

## Report minimum

Capture source and target commit SHAs, fixture revision, environment/tool versions, tests run, passed/failed/skipped counts, observed differences, false positives, manual approvals, unresolved risks, reviewer identity and whether independent.
