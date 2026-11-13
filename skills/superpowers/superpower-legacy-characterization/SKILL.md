---
name: superpower-legacy-characterization
description: User-facing optional Part 1.1 superpower. Chief asks YES, NO or DEFER before any isolated legacy runtime, then plans and executes safe behavioral characterization and golden-master evidence only if approved.
---

# Superpower 1.1 — Optional Dynamic Characterization (Part 1.1 / P002)

## When to use

Invoke when the user requests **start Part 1.1**, **run the legacy application safely**, or reaches the post-discovery dynamic-characterization decision. **Optional does not mean silently skipped**. Always present the choice `YES / NO / DEFER` with cost, risk and information gained. This superpower must not launch containers, pull images, expose network services or install tooling before explicit approval.

## Ordered specialist dispatch

1. `orca-project-entry` + `orca-coordination`: discover solo/delegated operation, verify G1 and source/data scope.
2. `legacy-dynamic-characterization`: feasibility, observation strategy, representative boundary/error/state/concurrency scenarios, normalization and determinism.
3. `isolated-legacy-runtime` + `docker` + `linux` if necessary: design isolated Docker or disposable VM with read-only source, controlled egress, no production credentials, no Docker socket and resettable synthetic fixtures.
4. `qa-methodology`, `bdd`, `differential-testing`: formal characterization scenarios and golden-master oracles; test data, negative cases, side effects and non-determinism.
5. `orca-work-contract` for actual agents, with security reviewer where available; `ai-memory-v2` only if enabled.

## Explicit decision gate

- **NO**: write `docs/legacy/characterization/decision.md` with `decision: NO`, date, user confirmation, inability to assert runtime equivalence and the next permissible phase. Do not run anything.
- **DEFER**: same decision record with prerequisites and blocked tasks. Do not run anything.
- **YES**: approve a **plan first**: runtime dependencies, network and trust boundaries, fixtures, threat model, resource budget, command list, teardown, rollback and logs. Obtain specific authorization for risky external operations and then proceed step by step.

## Execution steps if YES

1. Inspect legacy runtime requirements and list unsupported libraries or insecure dependencies. Prefer a disposable VM for untrusted/high-risk legacy binaries; Docker is not a hardened security boundary by itself.
2. Prepare an offline/local isolated environment where possible; never connect to production services or copy production personal data.
3. Run health/build checks, record tool versions and failures, then execute representative workflows. Capture request/response, DB state differences, relevant files/events, logs, timezone effects and hidden external side effects.
4. Repeat representative tests after reset to detect flaky/nondeterministic outcomes; label unstable observations.
5. Save portable fixtures and source-backed golden-master expectations; classify tests as verified, partially verified, inferred or blocked.
6. Chief/Reviewer records independent vs self review and an explicit G1.1 outcome; update task diaries and derived knowledge indexes afterward.

## Expected output contract

Use `.orca/phases/002-characterization/`, `docs/legacy/characterization/decision.md`, `environment/` (pin image versions, network policy and runtime config with no secrets), `fixtures/`, `observations/`, `golden-master/`, `limitations.md`, and `reviews/G1-1-*.md`. See `docs/methodology/OUTPUT-CONTRACT.md`. Do not fabricate executable outputs when original runtime is unavailable.

## Gate and handoff

For approved and executed characterization, record scenario coverage, command evidence and limitations. For NO/DEFER record exactly that, rather than implying a pass. Offer `superpower-legacy-migration` for Part 2 only with the known verification boundaries in its planning inputs.

## Evidence and completion contract

- **Activation:** Read only for a relevant task; record NOT_APPLICABLE when its conditions do not hold.
- **Concrete result:** Recorded YES/NO/DEFER and original-runtime observations under isolation or explicit blocker.
- **Verification:** Cite source revision, file/symbol, executed command, exit status, observation scope, artifacts, timestamps and exceptions where applicable. A written plan is not an executed check. Use PASS, FAIL, PARTIAL, NOT_RUN, NOT_APPLICABLE rather than an unsupported green status.
- **Stop and escalate:** Missing source, tooling, authorization, or objective evidence blocks a completion claim. Chief-only reviews are non-independent.
