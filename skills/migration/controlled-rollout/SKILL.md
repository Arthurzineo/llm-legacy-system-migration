---
name: controlled-rollout
description: Plan and verify a versioned, approved deployment with health checks, staged rollout and bounded rollback.
---

# Controlled Rollout

## Use
P008 after G4 approval; also read-only assessment of an existing deployment. Not permission to modify live systems.

## Procedure
1. Map host, delivery mode, release provenance, artifact digest, database schema, ingress, TLS/mTLS, DNS and dependent clients.
2. Choose staged/canary, blue-green or maintenance-window release based on rollback feasibility and statefulness.
3. Record preflight checks, backups and verified restore path; ask for explicit approval before each production change.
4. Execute only via tools truly available in the current runtime. Record command, operator, time, output, commit, image digest, configuration revision and health evidence.
5. Check readiness/liveness, critical workflows, authz, backward compatibility and logs; rollback on agreed breach. State explicitly if rollback was only attempted, not confirmed.
6. Preserve postdeployment observations and release manifest. No deploy claim from a Git push or successful build alone.

## Output
`docs/operations/deployment-evidence.md`, approved runbook, exact rollback plan, outcome and unresolved risks.
