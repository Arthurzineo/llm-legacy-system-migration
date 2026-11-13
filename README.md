# LLM - LEGACY SYSTEM MIGRATION

> **Design-stage project.** This private repository is published on `main`. No migration engine has run and no real legacy application has been analyzed.

A reusable, agent-agnostic operating model for reverse-engineering and migrating unsupported legacy software. It combines ORCA work ownership, agent skills, evidence-backed diagrams, optional isolated characterization, AI Memory v2.0.1, and incremental migration with executable acceptance criteria.

## Principles

1. **Chief-first, single-agent capable.** A single Chief may execute every role; delegate only when extra agents are available and useful. Agent availability is rechecked every session.
2. **No fictional evidence.** Source, tests, runtime observations, and verified schemas outrank inferred diagrams and AI memory.
3. **Behavior before rewrite.** Preserve observable business behavior or explicitly approve deviations. Security defects are not automatically compatibility requirements.
4. **Skills are modular.** The ORCA coordination model is reusable outside legacy migration. Skills are discovered by their `SKILL.md` metadata and activated only when relevant.
5. **English repository artifacts.** Skills, prompts, documentation, variable names, commit templates, and reports are in English. Users may interact in any language, including Portuguese.
6. **Opt-in operations.** Do not install tools, start containers, alter user agent configuration, publish code, or connect external services without authorization.

## Five user-facing Superpowers

Instead of making users remember dozens of skills, the Chief exposes exactly **five primary Superpowers**. Each one reads and routes to the appropriate specialized skills and uses existing ORCA contracts and diaries. The Chief can run **alone** or delegate if other real agents are available; agent availability is checked in the current session, never inferred from a role name.

| User command | Superpower | Scope |
| --- | --- | --- |
| Start ORCA / Setup ORCA | `superpower-orca` → `orca-setup` | Discover real agents, agree on role assignments, issue optional worker contracts, establish project state and configure memory only when approved |
| Start Part 1 | `superpower-legacy-discovery` | Static reverse engineering, source evidence and diagrams |
| Start Part 1.1 | `superpower-legacy-characterization` | Optional, explicit YES / NO / DEFER, isolated runtime and characterization |
| Start Part 2 | `superpower-legacy-migration` | Questionnaire, target architecture, incremental implementation, validation and cutover |
| Start Part 3 | `superpower-operational-assurance` | Release readiness (P007), controlled deployment and cross-client parity (P008), operational acceptance and recovery (P009) |

See the [Superpowers guide](docs/skills/SUPERPOWERS.md) and the [routing manifest](docs/skills/superpowers.json). Inspect the read-only routing plan with:

```bash
python3 scripts/superpower_plan.py --list
python3 scripts/superpower_plan.py --stage part1
python3 scripts/superpower_plan.py --stage part1.1
```

Superpowers are **orchestration instructions**, not an automatic agent dispatcher. Their selected child `SKILL.md` files are loaded just in time. Actual dispatch, tool execution and installation depend on the current agent runtime, contract and explicit authorization.

## User-facing methodology

| Step | Internal ORCA phase | Objective | Gate |
| --- | --- | --- | --- |
| Foundation | P000 | Configure generic ORCA, agents, memory, skills | ORCA project-entry status checked |
| Part 1 | P001 | Static analysis, decomposition, architecture/UML/ERD documentation | Evidence and diagram review |
| Part 1.1 (optional) | P002 | Isolated runtime, synthetic data, characterization tests | Behavior evidence or justified skip |
| Part 2 — planning | P003 | Interactive intake, architecture target, migration plan | Plan and risk approval |
| Part 2 — implementation | P004 | Incremental implementation with ORCA contracts | Component acceptance |
| Part 2 — verification | P005 | Differential/regression/security verification | Independent evidence or human risk acceptance |
| Part 2 — transition | P006 | Data reconciliation, controlled cutover, rollback plan | Deployment approval |
| Part 3 — readiness | P007 | Versioned release evidence, approval and recovery preparation | G4 |
| Part 3 — deployment | P008 | Approved rollout, live verification and client parity | G5 |
| Part 3 — operations | P009 | SLO, restore, alerts, handoff and lifecycle controls | G6 |

The Chief **must ask whether Part 1.1 should be attempted**, explain feasibility and security implications, and record YES / NO / DEFER. If NO, do not claim behavioral equivalence proven by dynamic testing.

## Folder layout

```text
AGENTS.md                       Project entry and routing rules
.orca/                          Work contracts, phases, roles, diaries, Chief state
GRAPHIFY.md                     Optional derived graph configuration
skills/
  superpowers/                  Only four main user-facing stage entrypoints
  core/                         Generic ORCA protocol and session routing
  migration/                    End-to-end and per-stage migration workflows
  programming-languages/        Go, Python; extensible by users
  architecture/                 C4, architectural audits, design patterns
  design/                       Design systems and interface consistency
  system/                       Docker, Linux, isolated runtime
  testing/                      TDD, BDD, QA, differential and mutation testing
  miscellaneous/                AI Memory, Clean Code, quality gates, refactoring
scripts/                         Opt-in integration, skills installer, validators
schemas/                         JSON contracts for findings and observations
docs/                            Architecture, methodology, memory, security, plans
examples/                        Synthetic examples, never live data
tests/                           Scaffolding and integration script tests
```

User-supplied skills belong at `skills/<category>/<slug>/SKILL.md` with unique frontmatter `name`. The installer makes flat, standard `skills/<slug>/SKILL.md` copies in a **selected target directory**; it does not overwrite other agents' skills by default.

## Start locally

```bash
python3 scripts/validate_project.py
python3 -m unittest discover -s tests -v
python3 scripts/install_skills.py --list
python3 scripts/install_skills.py --target /tmp/orca-skills-preview
python3 scripts/ai_memory_doctor.py --json
```

Installation and lifecycle changes are always opt-in; see [AI Memory 2.0.1](docs/integrations/AI-MEMORY-V2.md) and [skills installation](docs/skills/CATALOG.md).

## Primary documentation

- [Four Superpowers and invocation guide](docs/skills/SUPERPOWERS.md)

- [ORCA coordination model](docs/architecture/ORCA-OPERATING-MODEL.md) and [protocol](docs/architecture/ORCA-PROTOCOL.md)
- [Migration workflow](docs/methodology/METHODOLOGY.md)
- [Expected outputs and directory contract](docs/methodology/OUTPUT-CONTRACT.md)
- [Skill catalog](docs/skills/CATALOG.md)
- [AI Memory v2.0.1 setup](docs/integrations/AI-MEMORY-V2.md)
- [Traceability and evidence](docs/methodology/TRACEABILITY.md)
- [Quality and equivalence](docs/verification/TEST-STRATEGY.md)
- [Security constraints](docs/security/THREAT-MODEL.md)
- [Original methodology drawing](docs/architecture/original-methodology.png)
- [Third-party references and licenses](docs/research/REFERENCES.md)
- [Prompt to start ORCA](prompts/ORCA-PROJECT-ENTRY.md) and [migration prompt](prompts/LEGACY-MIGRATION-START.md)
- [Repository status and versioning](BRANCH.md)

## Operational assurance and skills quality

Part 3 adds five specialist skills: `release-readiness`, `controlled-rollout`, `cross-client-parity`, `operational-observability` and `operational-recovery`. It is a **methodology and routing specification**, not proof that a release engine has run. See [skill quality audit](docs/skills/SKILL-QUALITY-AUDIT.md).

## Status and non-goals

The published `main` branch establishes **workflow specifications and local validation scripts**, not a finished migration product. Static parsers, automatic diagram accuracy, environment reconstruction, and the AI Memory server have **not** been executed or verified against a legacy codebase. The original methodology drawing is included as reference material.

## Optional external analyzers

[Uncle Bob's Crapper, Dryer and Mutator](docs/integrations/OPTIONAL-UNCLE-BOB-TOOLS.md) are included as **pinned Git submodules** under `tools/third-party/`, preserving original source, commit IDs and 0BSD licenses. These are optional and support Clojure, Java, Go, TypeScript/JavaScript, Rust and Python only. Their presence does **not** automatically run them on a legacy project.

~~~bash
git submodule update --init tools/third-party/crapper tools/third-party/dryer tools/third-party/mutator
python3 scripts/setup_optional_quality_tools.py --target /path/to/legacy --json
# Optional explicit dependency installation after source review:
python3 scripts/setup_optional_quality_tools.py --prepare
~~~

The Clean Code skill chooses tools only after source-language discovery, supported-file scoping, baseline test checks and user permission for execution. Unsupported languages are analyzed with other suitable tools or recorded as not measured.

## ORCA setup and AI Memory

`superpower-orca` always loads the **`orca-setup` internal skill** after project entry. The Chief proposes a solo/delegated staffing plan, records who owns each work item, and creates contracts only for verified available agents. Setup also offers **AI Memory v2.0.1** (official pinned version), including separate CLI install, server startup, per-client MCP registration, lifecycle-hook setup and an actual `memory_status` check in each client. See [Project Memory setup](docs/integrations/AI-MEMORY-V2.md) and `scripts/ai_memory_doctor.py`. All modifications to agent configuration remain opt-in.

