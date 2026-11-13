---
name: design-patterns
description: Use to select, identify or refactor design patterns only when a concrete maintainability or change-coupling problem warrants them.
---

# Design Patterns


## Selection discipline

Start with the changing requirement and a documented pain point; prefer simpler direct code until an abstraction is justified. Consider Strategy for varying algorithms, Adapter/anti-corruption layer for legacy API interoperability, Facade for integration boundaries, Factory when construction rules change, Observer for explicit event propagation, Repository for storage isolation and State for complex transition rules. Never select patterns to maximize pattern count.

For every pattern proposal: state the problem, alternative without the pattern, new interfaces, effects on testability/dependencies, migration risk and removal costs. Prevent circular dependency, service locators, shared mutable singletons and "god" mediator classes. Add contract tests proving old and new behavior and record intentional differences.

## Evidence and completion contract

- **Activation:** Read only for a relevant task; record NOT_APPLICABLE when its conditions do not hold.
- **Concrete result:** Observed design problem, alternatives, costs and compatibility tests; no pattern for fashion.
- **Verification:** Cite source revision, file/symbol, executed command, exit status, observation scope, artifacts, timestamps and exceptions where applicable. A written plan is not an executed check. Use PASS, FAIL, PARTIAL, NOT_RUN, NOT_APPLICABLE rather than an unsupported green status.
- **Stop and escalate:** Missing source, tooling, authorization, or objective evidence blocks a completion claim. Chief-only reviews are non-independent.
