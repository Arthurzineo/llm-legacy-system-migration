---
name: legacy-migration-intake
description: Use at the beginning of Part 2 to obtain user migration objectives, language, frontend, database, deployment, compatibility and additional requirements.
---

# Legacy Migration Intake


## Inputs

Read G1 findings, currently unsupported behavior, source-language/tool constraints, business capabilities, data and integrations. Avoid a generic questionnaire that ignores known evidence. User answers can be supplied in Portuguese, while the **saved questionnaire is in English**.

## Minimum interview

Ask for target language and supported version; framework/runtime; target UI/frontend and UX continuity; database engine/schema strategy; deployment/platform; migration mode; in-scope modules; compatibility requirements; performance/SLO; security policy; licensing and operational constraints; token/human budget; acceptable intentional differences; release/rollback ownership; extra constraints and unknowns.

## Execution

1. Present discovered options and reasonable defaults, distinguishing confirmed constraints from proposals.
2. Ask only material unknowns, grouping independent choices when practical. Do not demand every optional answer before producing a provisional plan.
3. Record answers and date in `docs/target/questionnaire.md`; unresolved entries remain `open` with owner and risk.
4. Convert needs to functional/nonfunctional requirements and observable acceptance criteria; map evidence to target modules and tests.
5. Hand off to `legacy-target-design` only when major irreversible choices have explicit approval.

## Exit

The user can inspect an English questionnaire and a visible decisions/unknowns register. No hidden architecture assumptions or premature rewrite.

## Evidence and completion contract

- **Activation:** Read only for a relevant task; record NOT_APPLICABLE when its conditions do not hold.
- **Concrete result:** User-confirmed architecture decisions, unresolved questions and target constraints.
- **Verification:** Cite source revision, file/symbol, executed command, exit status, observation scope, artifacts, timestamps and exceptions where applicable. A written plan is not an executed check. Use PASS, FAIL, PARTIAL, NOT_RUN, NOT_APPLICABLE rather than an unsupported green status.
- **Stop and escalate:** Missing source, tooling, authorization, or objective evidence blocks a completion claim. Chief-only reviews are non-independent.
