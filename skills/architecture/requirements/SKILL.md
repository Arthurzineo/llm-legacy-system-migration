---
name: requirements
description: Use when reconstructing observable requirements and business rules from a legacy system or defining testable behavior for a target architecture, with explicit evidence and uncertainty.
---

# Requirements Engineering for Legacy Modernization

## When to use

Use during Part 1 to reconstruct candidate requirements from observed code and tests, and during Part 2 to confirm target requirements with users and stakeholders. Requirements cannot be established merely by naming code symbols or asking an LLM to describe a repository. Do not use this skill to assume approval of inferred requirements.

## Evidence-first workflow

1. Identify system boundaries, actors, roles, integrations, domain entities and observable goals. Differentiate the user's actual requested outcomes from implementation constraints.
2. Inspect routes, CLI commands, forms, validation code, stored procedures, triggers, event consumers, error handling, tests, user manuals and runtime traces. Capture source revision, file/symbol/line, conditions and confidence for each proposed behavior.
3. Reconstruct functional requirements as `Given <initial state>, when <event>, the system shall <observable result>`. Include negative paths, permissions, concurrency, retries, idempotency, recoverability and failure cases.
4. Derive nonfunctional requirements (security, integrity, availability, performance, capacity, observability, accessibility and legal constraints) with measurable verification criteria. Do not invent service-level objectives.
5. Group behavior into use cases and activity/state/sequence diagrams where those models clarify contracts. Create diagrams only when they add new understanding, and link them to source evidence.
6. Mark each statement `observed`, `tested`, `inferred`, `user-confirmed`, or `unknown`. Record conflicting evidence and request human confirmation where it affects migration correctness.
7. Maintain `requirement_id -> evidence_id -> model_id -> target_component -> acceptance_test_id` traceability, and reflect authorized changes in ORCA contract scope, ADRs, and affected verification steps.

## Outputs

Part 1: `docs/legacy/rules/business-rules.md`, relevant use-case models and `docs/legacy/uncertainty-register.md`. Part 2: `docs/target/requirements.md`, verified acceptance criteria, changes to `docs/target/questionnaire.md` and `docs/verification/traceability.csv`.

## Completion gate

All high-impact requirements have an explicit source or user approval; each approved requirement has a testable expected result and a traceability path. Unverified historical behavior remains a risk, not a promised compatibility requirement.

## Evidence and completion contract

- **Activation:** Read only for a relevant task; record NOT_APPLICABLE when its conditions do not hold.
- **Concrete result:** Requirements with evidence IDs, owner approvals and executable acceptance expectations.
- **Verification:** Cite source revision, file/symbol, executed command, exit status, observation scope, artifacts, timestamps and exceptions where applicable. A written plan is not an executed check. Use PASS, FAIL, PARTIAL, NOT_RUN, NOT_APPLICABLE rather than an unsupported green status.
- **Stop and escalate:** Missing source, tooling, authorization, or objective evidence blocks a completion claim. Chief-only reviews are non-independent.
