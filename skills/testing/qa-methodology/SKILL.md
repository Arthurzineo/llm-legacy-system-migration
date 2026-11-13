---
name: qa-methodology
description: Use for risk-based QA across unit, integration, contract, security, performance, exploratory and release validation.
---

# Qa Methodology


## Test portfolio

Map important user journeys, irreversible operations, data sensitivity, external integrations, concurrency and current code coverage. Choose the lowest reliable level for each behavior: unit, integration, contract, end-to-end, property-based, differential or exploratory. Ensure at least one representative real integration test for contracts where mocks would hide incompatibilities.

Define fixture creation, reproducible setup/reset, environment equivalence, test data minimization and nondeterminism. Every defect fix should introduce a durable regression check when feasible. Require release gates for failures on high-risk flows; explicitly report flaky, skipped and not-run tests instead of replacing evidence with an LLM summary.

## Output

Traceable risk-based test plan and actual execution results, with coverage limitations and review status.

## Evidence and completion contract

- **Activation:** Read only for a relevant task; record NOT_APPLICABLE when its conditions do not hold.
- **Concrete result:** Risk-based test matrix with executed results and explicit exclusions.
- **Verification:** Cite source revision, file/symbol, executed command, exit status, observation scope, artifacts, timestamps and exceptions where applicable. A written plan is not an executed check. Use PASS, FAIL, PARTIAL, NOT_RUN, NOT_APPLICABLE rather than an unsupported green status.
- **Stop and escalate:** Missing source, tooling, authorization, or objective evidence blocks a completion claim. Chief-only reviews are non-independent.
