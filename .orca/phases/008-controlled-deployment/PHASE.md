---
id: P008
title: Part 3 — Controlled Deployment and Parity
status: planned
owner: unassigned
depends_on: []
---

# Part 3 — Controlled Deployment and Parity

## Entry
Read authoritative prior ORCA state and actual release source revision. Confirm tool access and action authorization. Production writes require separate explicit approval. Neither a completed directory nor a green CI job is proof of readiness.

## Exit gate
G5: target deployment facts, health checks, cross-client behavior/version matrix, observed monitoring and rollback outcome.

Record PASS / FAIL / PARTIAL / NOT_RUN / NOT_APPLICABLE for every required criterion. Capture observed timestamps, actual commands, operator, commit, environment, evidence link, rollback status, limitations and approver. An unexecuted or unobserved step is never marked PASS.

## Handoff
Keep evidence under docs/operations/ and task diaries in this phase. Continue only after authorized gate acceptance.
