# Routed Agent Skills Quality Audit — 2026-11-13

## Scope and limits
Reviewed all **44 unique skills referenced by the five Superpowers**, covering entry skills, always-required children and conditional children. Inspected text, metadata, routing and references. This is a source-level review; no actual legacy migration, Docker sandbox, memory connector, worker dispatch, production deployment or external quality program was executed as part of this audit. A skill's presence is not proof it ran.

## External engineering references
- Agent Skills format and progressive disclosure: https://github.com/agentskills/agentskills/blob/main/docs/specification.mdx
- Anthropic's skills collection: https://github.com/anthropics/skills
- obra Superpowers framework (skill-centered engineering workflow, TDD, explicit gates): https://github.com/obra/superpowers
These are **design references, not copied source or dependencies**. GitHub stars reflect popularity rather than effectiveness or security assurance. Licensing and compatibility must be reviewed before adopting any scripts.

## Review findings
- **P1: P007–P009 operational assurance was absent.** Added the fifth Superpower, five specialized skills, phase templates, G4–G6 boundaries and Part 2 handoff.
- **P1: Activity-versus-evidence ambiguity.** Added an evidence-and-completion contract to every routed skill: actual version and observed commands/results; statuses PASS, FAIL, PARTIAL, NOT_RUN, NOT_APPLICABLE. Do not upgrade an inference, proposed plan, model statement or generated report to PASS.
- **P1: Non-executable orchestration.** Manifest routing is read-only. Live agent delegation and runtime execution still depend on a verified external runtime. No false claims of an implemented dispatch engine.
- **P2: Specialized instructions vary in completeness.** A few original skills were only 14–20 lines, with implicit rather than explicit triggering, artifact scope, or failure criteria. Preserved task-specific procedures and appended concrete outcomes and stop conditions.
- **P2: Potential overlap:** `qa-methodology` defines test strategy while `tdd`, `bdd`, `mutation-testing`, `differential-testing` perform specific methods; `codebase-architecture`, `architecture-audit`, `c4-architecture` cover design, auditing and representation. **Do not merge them** unless a controlled benchmark demonstrates shorter context with equivalent test quality.
- **P2: No validated automatic migration engine.** Skills route tasks; callers must check real parsers, compiler, deployment commands, and tool permissions before invoking. Missing tools must be NOT_RUN, not success.

## Quality requirements for every routed skill
1. Valid YAML frontmatter, unique lower-case skill name equal to directory, specific description.
2. Activate only on a matching user objective or authorized workflow phase; do not load all skills indiscriminately.
3. Document exact tool prerequisites and fallback when missing; prefer deterministic inspection/tests over model assertions.
4. Require revision-pinned evidence, observed outcomes, applicability, security boundaries, explicit owner when high-impact.
5. Clearly distinguish plan, execution, review and verified acceptance, preserving negative and skipped evidence.
6. Human or independent review where required; solo-Chief review must be labeled as non-independent.
7. The skill produces a bounded deliverable; it does not create placeholder files, invented diagrams, green test results, fake agents, or an implicit authorization.

## Acceptance criteria for follow-up
- Repository validation and routing plan run successfully locally against the branch (not executed by this audit).
- All five entrypoint routes and conditional skills resolve to real files.
- Pilot a fresh, small, authorized legacy application in a reproducible test environment; record accuracy of diagrams, functional equivalence, security and labor/token costs with and without new skills.
- Test operational G4/G5/G6 with authorized deployment or read-only evidence; avoid treating a historical WebAlgo2 document as a direct current production observation.
- Consider a dedicated skill test harness with fixture input, expected artifacts, negative cases and reproducible grading for each critical task.
