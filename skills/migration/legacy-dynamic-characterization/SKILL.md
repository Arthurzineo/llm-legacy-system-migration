---
name: legacy-dynamic-characterization
description: Use only after explicit user opt-in for Part 1.1 to run an isolated legacy application and capture repeatable behavioral baselines.
---

# Legacy Dynamic Characterization


## Authorization gate

The Chief must ask: **"Would you like to attempt Part 1.1 dynamic characterization in an isolated environment?"** Explain runtime feasibility, unsupported dependencies, security/egress risks, synthetic data and compute requirements. Record `YES`, `NO`, or `DEFER` in `docs/legacy/characterization/decision.md`. NO/DEFER means stop and continue with documented static limitations.

## YES path

1. Threat-model the legacy runtime. Read `isolated-legacy-runtime`; prefer disposable VMs for high-risk or privileged code. Review Dockerfiles/images/dependencies before any execution. Never run untrusted code against production infrastructure.
2. Inventory exact OS, CPU architecture, language/runtime, application services, database version, configuration, clock and external integrations. Preserve environment rebuild steps and version pins.
3. Build a sanitized, deterministic fixture set: normal, boundary, invalid, authorization, database, error/retry, concurrency and persistence cases. Use simulation only for named unavailable services and disclose fidelity gaps.
4. Run legacy scenarios, collect canonical input/output/status/error, DB pre/post state and files/events/network effects. Re-run to assess determinism. No production secrets or data.
5. Write `docs/legacy/characterization/observations/`, `golden-master/`, `fixtures/`, and an environment manifest. Every observation identifies environment/tool versions and reproduction commands.
6. If execution fails, classify the failure, attempt only authorized safe fixes to the harness, then record `partially-executed` or `not-executable` with evidence rather than fabricating tests.

## Acceptance

Confirmed outcomes are repeatable or explicitly stochastic; side effects are captured; mock limitations and denied operations are listed; user opt-in and sandbox permissions exist in writing.

## Evidence and completion contract

- **Activation:** Read only for a relevant task; record NOT_APPLICABLE when its conditions do not hold.
- **Concrete result:** Repeatable oracle runs, fixture revisions, observed states and explicit mock limitations.
- **Verification:** Cite source revision, file/symbol, executed command, exit status, observation scope, artifacts, timestamps and exceptions where applicable. A written plan is not an executed check. Use PASS, FAIL, PARTIAL, NOT_RUN, NOT_APPLICABLE rather than an unsupported green status.
- **Stop and escalate:** Missing source, tooling, authorization, or objective evidence blocks a completion claim. Chief-only reviews are non-independent.
