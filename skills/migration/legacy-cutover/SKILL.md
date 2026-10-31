---
name: legacy-cutover
description: Use only after verified migration to plan data reconciliation, release transition, monitoring, rollback and final retirement of the legacy system.
---

# Legacy Cutover


## Required approvals

The Chief obtains user/operator authorization for production-affecting deployment and confirms who can execute database migrations or modify live infrastructure. Never auto-deploy merely because a migration task completed.

## Plan

Record versioned backups, test restore result, migration scripts and checksums, mapping/reconciliation reports, access control changes, deployment order, health checks, traffic shift criteria, rollback window and explicit rollback commands. Choose blue/green, strangler routing or canary only when compatible with state/data ownership. For irreversible schema changes, design forward recovery and test it.

## Gate

Go/no-go requires verified smoke and integration tests, data reconciled, security risks approved, clear monitoring/alerts, operator on-call and a tested rollback or accepted irreversible plan. Only then retire the legacy paths and update documentation, ORCA records and derived memory/graph indexes.
