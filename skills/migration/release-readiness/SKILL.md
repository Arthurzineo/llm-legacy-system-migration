---
name: release-readiness
description: Assess release evidence and issue a reproducible go/no-go recommendation before a migration deployment.
---

# Release Readiness

## Use
P007 of Part 3; not for performing deployments.

## Actions
1. Resolve source commit, target environment, signed/hash-verified artifact identity, dependencies, SBOM and build provenance. Validate that evidence refers to the same revision.
2. Check scoped CI results, functional/differential/security tests, unresolved regressions, client/API/database compatibility and target SLO/capacity constraints.
3. Check backups, **tested** restore, data migration/reconciliation, rollback limitations and ownership approvals.
4. Produce a checklist with PASS / FAIL / NOT_MEASURED / NOT_APPLICABLE for each item and direct links to evidence.
5. Recommend GO only when all mandatory gates pass; CONDITIONAL requires written risk owner acceptance, never silently bypass a failing security/data gate.

## Output
`docs/operations/release-readiness.md`: revision, decision, findings, evidence, approver, conditions and expiration. Planning is not an approval or authorization to deploy.
