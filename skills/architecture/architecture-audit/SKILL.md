---
name: architecture-audit
description: Use when evaluating a current codebase for dependency cycles, coupling, cohesion, hidden state and reversible migration seams.
---

# Architecture Audit


## Method

Before proposing architecture, build a factual map of modules, data writes, entry points, integrations, runtime processes and public contracts. Trace several representative changes end-to-end rather than relying on package names. Measure package cycles and centrality where tools are available; document how the metric was computed.

Flag only evidenced issues: multi-module changes caused by one business rule, duplicated domain logic, inappropriate shared writes, temporal coupling, implicit global state, framework leakage, slow cross-boundary calls and unclear failure/retry semantics. For each issue record source references, triggering scenario, consequence, change cost, risk and **smallest reversible seam**.

Evaluate original code as legacy constraints; do not recommend microservices, layered architecture or full rewrite by fashion. Maintain current architecture diagrams separately from target design. Request review on coupling changes that may affect transactions or public APIs.

## Output

An ordered architecture risk report, verified dependency view, candidate migration seams and risk-weighted verification plan. No invented cohesion score.
