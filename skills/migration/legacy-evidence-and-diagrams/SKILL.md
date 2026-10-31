---
name: legacy-evidence-and-diagrams
description: Use for source- and behavior-traceable reverse-engineered diagrams, rules, ERDs, C4 components, sequences, use cases and confidence grading.
---

# Legacy Evidence And Diagrams


## Principle

A diagram is a **derived model**, not a proof of software behavior. Keep original editable Mermaid/PlantUML source, evidence IDs and review notes. Never invent use cases, classes, database relations or call sequences to complete a visually appealing diagram.

## Artifact selection

Generate only views needed to answer migration questions:

- Use-case UML: actors, goals, authorization and external systems; infer only with explicit confidence and human review.
- Class UML: real classes, interfaces, inheritance and visibility, usually derived from AST; avoid reproducing every private method without purpose.
- ERD: actual tables/columns/keys/constraints; inferred foreign keys labeled as hypotheses.
- C4/components: verified module/deployment boundaries; remember C4 containers are deployable units, **not necessarily Docker containers**.
- Sequence: trace representative use cases and asynchronous side effects, with evidence for order assumptions.
- Activity/BPMN: observable branches, business decisions and exceptions.
- Dependency/DFD/deployment: when integration, trust boundaries or data transformation justify them.

## Workflow

1. Collect source evidence IDs and revision. Associate each diagram element/relationship with evidence or `status: inferred`.
2. Generate diagram text under `docs/legacy/diagrams/`, business rules under `docs/legacy/rules/` and evidence JSON under `docs/legacy/evidence/`; save a diagram-to-evidence index.
3. Parse/render actual diagrams with available Mermaid/PlantUML tools; if tools are not installed, mark rendering unverified rather than claiming success.
4. Run a consistency pass: all described files and symbols exist at source revision; ERD columns map to actual schema; no invented class hierarchy; actor permissions are not derived from names alone.
5. Request review on high-impact inferred rules. Record confidence as `high/medium/low` with rationale **not** model likelihood.

## Exit

Deliver diagram list, file paths, evidence coverage, excluded optional diagrams, uncertainty register and review outcome. Each confirmed claim can be reproduced without relying on AI Memory.
