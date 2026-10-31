---
name: design-patterns
description: Use to select, identify or refactor design patterns only when a concrete maintainability or change-coupling problem warrants them.
---

# Design Patterns


## Selection discipline

Start with the changing requirement and a documented pain point; prefer simpler direct code until an abstraction is justified. Consider Strategy for varying algorithms, Adapter/anti-corruption layer for legacy API interoperability, Facade for integration boundaries, Factory when construction rules change, Observer for explicit event propagation, Repository for storage isolation and State for complex transition rules. Never select patterns to maximize pattern count.

For every pattern proposal: state the problem, alternative without the pattern, new interfaces, effects on testability/dependencies, migration risk and removal costs. Prevent circular dependency, service locators, shared mutable singletons and "god" mediator classes. Add contract tests proving old and new behavior and record intentional differences.
