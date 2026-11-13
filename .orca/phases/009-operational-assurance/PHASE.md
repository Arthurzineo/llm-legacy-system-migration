---
id: P009
title: Part 3 — Operational Assurance and Handoff
status: planned
owner: unassigned
depends_on: []
---

# Part 3 — Operational Assurance and Handoff

## Entry
Read authoritative prior ORCA state and actual release source revision. Confirm tool access and action authorization. Production writes require separate explicit approval. Neither a completed directory nor a green CI job is proof of readiness.

## Exit gate
G6: SLO and alert verification, backup restore drill, RPO/RTO evidence, incident runbook and explicit operational signoff.

Record PASS / FAIL / PARTIAL / NOT_RUN / NOT_APPLICABLE for every required criterion. Capture observed timestamps, actual commands, operator, commit, environment, evidence link, rollback status, limitations and approver. An unexecuted or unobserved step is never marked PASS.

## Handoff
Keep evidence under docs/operations/ and task diaries in this phase. Continue only after authorized gate acceptance.
