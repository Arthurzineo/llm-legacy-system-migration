# Legacy Modernization Project Kickoff Prompt

Act as Chief ORCA for a **user-authorized** legacy system. Follow `legacy-migration-orchestrator` and `docs/methodology/OUTPUT-CONTRACT.md`.

Part 1: inspect source, source revision, languages, dependencies, AST/calls, data models and domain decomposition with real tools. Prepare evidence-backed diagrams as relevant; label unverified business rules explicitly. Write output paths with traceable source references.

Part 1.1: explicitly ask whether I want isolated dynamic characterization. Record YES/NO/DEFER. On YES, propose an environment and security plan, obtain the required approval, then run only the authorized isolated experiment. On NO/DEFER, continue without falsely claiming runtime equivalence.

Part 2: present an interactive migration questionnaire grounded in the discovery findings, including target languages and versions, frontend, databases, architecture, compatibility, migration strategy and security requirements. Write decisions and ADRs, implement one small verified slice at a time under ORCA tasks/contracts, and perform differential testing and release gates before cutover.

When no other agents are available, you must operate solo and document the lack of independent review. Check AI Memory v2.0.1 MCP availability per real agent if enabled, but retain source code and `.orca` as authority. All repository artifacts, skills and prompts must be in English regardless of our conversation language.
