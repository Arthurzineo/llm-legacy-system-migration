# User Methodology — ORCA Phases and Gates

The user-facing entrypoints are the four `superpower-*` skills documented in `docs/skills/SUPERPOWERS.md`. Each superpower routes to the relevant specialist skills; the Chief performs this workflow alone or delegates tasks to available agents.

This workflow implements the hand-drawn concept in `docs/architecture/original-methodology.png`. It is a **methodological specification**, not proof that the migration tools already exist.

## Part 1 — Static analysis (P001)

1. Acquire an authorized, immutable source snapshot with SHA and inventory language/runtime versions, build files, dependencies, APIs, licensing, integration endpoints and database artifacts.
2. Run language-appropriate parsers and static tools to derive AST, call graph, import/dependency graph, data model, migrations, triggers and public endpoints. If tools are missing, register the missing coverage rather than filling gaps with guesses.
3. Decompose by domain capability, entry points and dependency clusters. Classes/functions are supporting units, not automatic architectural boundaries. Save independent decomposition reports.
4. Recover selected diagrams with source-backed metadata: use cases, class models, ERD, components/C4, sequence, activities/BPMN, DFD, deployment and dependency relationships. Generate only diagrams answering relevant questions.
5. Persist diagram sources (Mermaid/PlantUML), evidence IDs, confidence and review records. Any agent may report uncertainty and request targeted inspection.

## Part 1.1 — Optional dynamic evaluation (P002)

Chief explicitly asks **"Do you want me to attempt isolated dynamic characterization of the legacy application?"** plus security and resource caveats. Record `YES`, `NO`, or `DEFER`. For YES: plan environment, review Docker/VM restrictions, approve image and dependencies, restore synthetic fixtures, run test scenarios, capture output, state changes and side effects, then reset and repeat. If impossible, document the blocker. Static analysis is still useful without a running legacy system.

## Gate G1 — Discovery review

Require a versioned inventory; provenance for high-priority claims; dependency and integration coverage; documented unknowns; baseline tests or justified absence; no secrets in generated docs; and human review of inferred high-impact business rules. An unsupported confidence score is not evidence.

## Part 2 — Planning and migration (P003–P006)

- **P003:** user questionnaire, functional/nonfunctional requirements, bounded domains, target language/runtime/framework/database/UI decisions, security requirements, ADRs, migration mode (in-place, replatform, strangler, selective rewrite), rollback and data strategy. Chief can ask multiple related questions conversationally and capture answers in one questionnaire file; unanswered items remain explicit.
- **P004:** select one behavior-backed vertical slice; define compatibility seam and test contract; implement deterministically where possible and use LLMs only for adaptation requiring semantic judgment; make small reviewable changes.
- **P005:** verify independent observed results, database state, security controls, invariants, concurrency, performance and approved deviations. No agent's textual self-claim constitutes a passed test.
- **P006:** rehearse backup/restore, database conversion, reconciliation, rollout and rollback; monitor and remove old paths only when the cutover gate passes.

## QA before implementation

Prefer red-green-refactor TDD for code and acceptance-first Gherkin/BDD for domain behavior. Build differential oracles from recorded legacy behavior when possible. Do not freeze known legacy security vulnerabilities as required behavior; document intentional safe differences explicitly.

## Phase progression

Phases and contracts follow the generic ORCA protocol. In Chief-only mode the Chief performs scoped roles sequentially with documented non-independent review; extra agents can execute in parallel only when work ownership and environment permissions are safe.

## Part 3 — Operational assurance (P007–P009)

After Part 2 cutover preparation, `superpower-operational-assurance` verifies artifact and source provenance, approves operational GO/NO-GO (G4), performs only specifically authorized controlled deployment and cross-client parity checks (G5), and evaluates post-release SLOs, restoration, alerting, credential lifecycle and operational handoff (G6). A web pilot can be deployed without being approved for general production. Each gate requires exact observed evidence and human signoff; a documentation update is not a passed gate. See `docs/skills/SUPERPOWERS.md`.
