---
name: operational-recovery
description: Validate disaster recovery, backup restore, incident rollback and safe decommissioning of legacy services after migration.
---

# Operational Recovery and Handoff

## Use
P009 and G6, before claiming production acceptance or legacy shutdown.

## Procedure
1. Identify stateful assets, RPO/RTO objectives, offsite and immutable backup needs, restore dependencies, keys and owners.
2. Test restore in an approved isolated environment; verify integrity and application behavior. Backup existence alone never proves recoverability.
3. Distinguish code rollback, configuration rollback and database backward migration; rehearse compatible recovery paths and state data-loss exposure.
4. Provide failure escalation, access/credential rotation, operational handoff and explicit legacy decommission authorization.
5. Preserve last-known-good artifacts, versioned runbooks and unresolved issues.

## Output
Recovery report with exact test timestamps, results, measured RPO/RTO, gaps, reviewer and signoff. Do not delete old components automatically.
