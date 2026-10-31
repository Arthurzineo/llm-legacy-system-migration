---
name: superpower-orca
description: User-facing ORCA entry superpower. Bootstrap or resume any software project, discover available agents, assign a Chief, establish contracts, phases, diaries, optional Graphify and AI Memory, then route specialized work.
---

# Superpower 0 — ORCA Project Bootstrap and Coordination

## When to use

Invoke when the user says **start ORCA**, **initialize ORCA**, **resume ORCA**, or when a project needs to be coordinated by ORCA. This skill is **project-agnostic**: it must work for new and existing repositories and for non-migration projects. The conversation may be in any language; write project skills, project structure, contracts, reports and generated documentation in English. Do not translate a legacy source file as a side effect.

A **superpower is an entrypoint/router**, not a replacement for specialist skills. It must explicitly read the selected specialist `SKILL.md` content before applying it. It must not claim that simply naming a skill has executed a tool or dispatched an agent.

## Ordered specialist skills

1. Always: `orca-project-entry` to classify the checkout, locate authoritative project state and detect real runtime capabilities.
2. **Mandatory before task allocation:** `orca-setup` to agree on a Chief-led staffing plan, map verified agents to responsibilities, establish optional contracts and offer project memory setup.
3. If project bootstrap/repair is approved: `orca-project-structure` to create additive `.orca/` files and `GRAPHIFY.md`, without moving existing application code.
4. Always for work: `orca-coordination` to decide solo vs delegated execution, source of truth and role ownership.
5. On assignments/child delegation: `orca-work-contract` to scope authority, acceptance, reviewers and diaries.
6. If memory is requested/enabled: `ai-memory-v2` (read-only diagnosis first). Do not install or rewire clients without approval.
7. Only when architectural exploration is needed: `codebase-architecture`, `architecture-audit`, `c4-architecture` and relevant other categorized skills.

## Chief discovery and execution modes

At each session start, **discover** real available agents and the version-matched ORCA runtime capabilities. A role file, installed skill, memory page or prior session does not prove an executable agent exists. Record `available_workers`, `reviewers`, `tooling` and `execution_mode` in `.orca/EXEC.md`.

- **Solo mode**: Chief owns all work, performs specialist roles sequentially, creates task/contract-equivalent records and a diary, and marks any self-review `independent: false`. Human review is mandatory for a high-risk cutover or significant unverified assumption.
- **Delegated mode**: Chief assigns one scoped contract per real worker, includes `required_skills` and `required_context`, allocates non-overlapping files/worktrees, receives status, verifies evidence and records acceptance. Reviewer/Security Reviewer/Summarizer exist as optional **roles**, not mandatory running agents.
- Reevaluate availability when a new session or agent begins; never pretend to have delegated work if the runtime cannot dispatch agents.

## Step-by-step bootstrap / resume

1. Identify project root and Git branch; inspect `.orca/PROJECT.md`, `.orca/EXEC.md`, `.orca/phases/`, active contracts, `GRAPHIFY.md`, README, source and tests.
2. Classify `NEW`, `ORCA READY`, `EXISTING WITHOUT ORCA` or `PARTIAL/DISORGANIZED` and distinguish additive setup from destructive changes.
3. Read `orca-setup` and the applicable core skills; propose Chief-only or user-approved delegation and map real agent IDs to tasks and responsibilities. Set project Chief and available agent inventory. In solo mode the Chief remains owner of each sequential step.
4. Create or reuse the standard layout in `skills/core/orca-project-structure/SKILL.md`. **No fake tasks, completed stages, or fabricated knowledge graph.** Keep `.orca/` as authoritative operational state, Git as version history, and Graphify/AI Memory as derived retrieval layers.
5. Initialize a real phase with `PHASE.md`, tasks, contracts and diaries only for authorized work. The Chief issues task-specific contracts to **verified workers only**; each accepts before execution. Preserve existing phase history. Define success and safety gates.
6. Verify Graphify for this exact project if enabled; distinguish `READY`, `STALE`, `PENDING`, `UNAVAILABLE`, `ERROR`.
7. Diagnose optional AI Memory 2.0.1 independently for binary version, server response, MCP tools per agent and hook capture per agent. Offer installation/configuration rather than silently changing the user's machine.
8. Report state, discovered capabilities, execution mode, phase/tasks, blockers and recommended next superpower. Stop if project structure normalization requires authorization.

## Folder and document contract

Use `.orca/PROJECT.md`, `.orca/EXEC.md`, `.orca/roles/`, `.orca/phases/<phase>/PHASE.md`, `tasks/`, `diaries/`, `.orca/contracts/active/`, `.orca/contracts/completed/`, `.orca/SUMMARY.md`, `.orca/LESSONS_LEARNED.md`, `GRAPHIFY.md` and `graphify-out/graph.json` **only if generated and verified**. Follow `docs/architecture/ORCA-OPERATING-MODEL.md`, `docs/architecture/ORCA-PROTOCOL.md`, and `docs/integrations/AI-MEMORY-V2.md`.

## Completion gate and next step

Completion requires a current real project state, explicit Chief, truthful solo/delegated mode, valid responsibilities and a known next task. Do not claim independent review in solo mode. For legacy migration, offer `superpower-legacy-discovery` as Part 1; do not automatically enter other phases without user intent or an active approved project plan.

## Explicit Setup ORCA invocation

A request to `setup-orca` uses this Superpower and its internal `orca-setup` skill. The Chief must plan responsibilities and contracts **before** activating Part 1/1.1/2. Agent availability is session-specific. AI Memory installation, MCP client wiring and hook capture are handled in the setup workflow by explicit opt-in; see `docs/integrations/AI-MEMORY-V2.md`. Never claim installation or memory readiness without actual verification.

