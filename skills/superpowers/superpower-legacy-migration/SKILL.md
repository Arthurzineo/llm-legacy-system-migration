---
name: superpower-legacy-migration
description: User-facing Part 2 superpower. Orchestrate questionnaire, target design, incremental migration, differential/security validation and controlled cutover with ORCA contracts and explicit human approval gates.
---

# Superpower 2 — Legacy Migration and Verification (Part 2 / P003–P006)

## When to use

Invoke when the user requests **start Part 2**, **plan the target migration**, or **migrate the legacy application**. This superpower encompasses planning, implementation, independent verification and controlled transition. It is **not** permission to deploy or delete legacy state. If G1 is incomplete, report the missing evidence and plan safe discovery rather than assuming completion.

## Ordered specialist dispatch by phase

1. **P003 — Intake and target design**: `legacy-migration-intake` → `legacy-target-design`; selectively read `requirements`, `system-design`, `codebase-architecture`, `c4-architecture`, `design-system`, `design-patterns`, `golang`, `python`, `docker` or owner-supplied skills. Ask only missing consequential questions; record answers and unknowns. Decide in-place upgrade, replatform, strangler or justified rewrite. Approval gate G2.
2. **P004 — Incremental implementation**: `legacy-incremental-implementation` with relevant language skills, `tdd`, `bdd`, `clean-code-quality-gates`, `refactoring` and `qa-methodology`. Use ORCA contracts, isolated worktrees where applicable, one capability/behavioral slice at a time, deterministic changes when possible and evidence from real compiler/tests.
3. **P005 — Verification**: `legacy-equivalence-validation` plus `differential-testing`, `qa-methodology`, `mutation-testing` and `clean-code-quality-gates`. Evaluate observable compatibility, schema invariants, latency/performance, concurrency, explicit security differences, SAST/SCA/DAST when available. Reviewers are separate agents only if actually available; in solo mode self-review is not independent.
4. **P006 — Cutover**: `legacy-cutover` with `system-design`, `docker`, `linux`, `qa-methodology` and security review as needed. Require human authorization, backups/restore rehearsal, data mapping, reconciliation, incremental rollout and rollback. Gate G3.
5. At every phase boundary use `orca-coordination` and `orca-work-contract` for scope, diaries, acceptance and blocker escalation. Optionally diagnose `ai-memory-v2`; memory cannot replace source evidence or approval.

## Step-by-step Chief workflow

1. Read `.orca` state, source revision, Part 1 evidence/G1 and Part 1.1 `decision.md`. State what has not been observed dynamically. Discover available agents and choose solo or delegated mode.
2. Present findings and run the migration intake questionnaire: target language/runtime/framework, database, UI, architecture constraints, data handling, security, integrations, performance, supported deployment environments, costs and acceptance conditions. Save the answers in English, preserve unresolved items.
3. Draft target architecture, migration strategy, domain boundaries, contracts, ADRs, target data model, source↔target behavior matrix and a slice sequence. Obtain **G2 approval** before writing target production code.
4. For each slice issue a bounded ORCA task; start from acceptance tests or characterization oracles, write minimal code, run and record compilation/tests, and review clean-code metrics without treating arbitrary thresholds as truth. Document approved behavior deviations (especially security fixes).
5. Run differential checks and security/integration/regression suites. Do not infer correctness from LLM output or a passing compile. If source behavior is unknown, mark `not verified` and escalate the test-plan gap.
6. Prepare migration/cutover plan with data safety, verification gates, restore testing, deployment rollback and owner approval. Execute destructive or production transition tasks **only under separate authorization**.
7. Preserve task/diary/contract history, evidence and final report; refresh Graphify and AI Memory only after authoritative updates.

## Expected directories / gates

Use `.orca/phases/003-planning/`, `004-migration/`, `005-verification/`, `006-cutover/`; `docs/target/{questionnaire,requirements,architecture,data-migration}.md`, `docs/target/adrs/`, `docs/verification/{traceability.csv,equivalence/,quality/,security/,release/}`. See `docs/methodology/OUTPUT-CONTRACT.md`. G2 requires decisions with rationale and user approval; slice gates require tests and affected-file evidence; G3 requires independent compatibility/security evidence or explicit known-risk human acceptance, data reconciliation and rollback feasibility.

## Stop conditions

Stop and escalate on production credentials, missing data-migration safety, unapproved schema changes, untrusted or unsandboxed execution, missing source authorization, or missing release decision. No role is permitted to report a task done based solely on its own text.

## Handoff to Part 3

Once P005 verification and P006 cutover planning are documented, offer `superpower-operational-assurance` for P007–P009 release readiness, controlled deployment, cross-client parity, monitoring and recovery. Do not assume deploying in P006 automatically satisfies operational release acceptance.
