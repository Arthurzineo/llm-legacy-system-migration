---
name: clean-code-quality-gates
description: Use for Clean Code/TDD metrics, near-duplicate function detection, coupling/dependency violations, structural duplication and mutation quality.
---

# Clean Code Quality Gates


## Inspiration and copyright boundary

This skill is an **original adaptation** of the documented practices in `https://github.com/unclebob/ub-mode`. It references external tools, does not copy their SKILL.md or vendor their code, and does not imply Uncle Bob endorsed this project.

First run `python3 scripts/quality_gate_doctor.py --json` to detect **possible** tool paths; do not treat discovery as an executed quality measurement.

## Run actual checks

1. Ensure the relevant build/tests are functioning; capture source revision and toolchain versions. First make the tested behavior work, then improve design. Never use aesthetic refactoring to break behavior equivalence.
2. Complexity and coverage: where the tool is compatible, use `unclebob/crapper` or equivalent to compute `CRAP = CC^2 * (1 - coverage)^3 + CC`. Reference `ub-mode` quality target `CRAP < 10` as a configurable **starting threshold**, not a universal proof of good code. If coverage is missing, report complexity without pretending to know CRAP.
3. Structural duplication: use `unclebob/dryer` where compatible and inspect candidate function pairs with high normalized structural similarity. `ub-mode` suggests review around `>= 0.8`; upstream dryer currently defaults to `0.82`. Treat a match as a review **candidate** (two independent domain rules can look similar), not automatic justification to extract a shared function.
4. Mutation tests: run `unclebob/mutator` with verified prerequisites and bounded scope; inspect surviving mutants. Do not infer test quality from line coverage alone.
5. Coupling: inspect verified import/call/dependency graphs for cycles, forbidden edges, shared mutable state, inappropriate data ownership, excessive fan-out, and broad interfaces. Calculate coupling metrics only when a real tool produces the measurement; no invented afferent/efferent numbers.
6. Duplicate behavior vs duplicate syntax: verify if near-identical functions implement the *same invariant* before combining them. Record affected callers, behavior fixtures and API risks. Use root-cause refactoring, minimal patches and test reruns.
7. Review clean structure: clear names, single focused responsibility, useful interfaces, error handling, boundary discipline, idempotency and dead-code evidence. Avoid introducing abstractions simply to satisfy a score.

## Exit gates

Produce a versioned quality report (tool name, version, command, measured functions/files, thresholds, warnings, exceptions) under `docs/verification/quality/`. Mark unavailable tools `not_measured`. If a threshold is exceeded, open a remediation issue or record a justified waiver; **never** claim a passing gate without tool output.
