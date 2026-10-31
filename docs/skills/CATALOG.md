# Categorized Skills Catalog

The repository uses `skills/<category>/<skill>/SKILL.md` for human organization and plug-and-play extensions. Many Agent Skills clients load flat skills directly; run `scripts/install_skills.py` to copy selected sources to a user-controlled **flat** install directory (`<target>/<skill>/SKILL.md`) without touching a user's existing skills unless explicitly requested. This is an organizational layer, not a guarantee that ORCA runtime discovers nested skills by itself.

## Categories

- `superpowers/`: exactly four user-facing entrypoint skills (generic ORCA, Part 1, optional Part 1.1, Part 2); see [Superpowers](SUPERPOWERS.md).
- `core/`: ORCA project entry, mandatory `orca-setup`, contracts, role discovery and coordination.
- `migration/`: orchestration, part 1 static analysis, decomposition, evidence, diagrams, optional part 1.1, part 2 questionnaire, implementation and verification.
- `programming-languages/`: Go and Python; add any language-specific SKILL.md here.
- `architecture/`: codebase structure, C4, architecture reviews, requirements engineering and design patterns.
- `design/`: design system consistency and UI considerations.
- `system/`: Linux, Docker and isolated runtime boundaries.
- `testing/`: TDD, BDD, QA, differential validation and mutation.
- `miscellaneous/`: memory integration, refactoring, quality gates and supporting topics.

## Add a skill

1. Create `skills/<category>/<unique-slug>/SKILL.md` with frontmatter `name` and `description`.
2. Specify when to use, when **not** to use, real tool dependencies, execution steps, expected artifacts and completion criteria.
3. Avoid conflicting global policies; the ORCA Chief always routes to only necessary skills.
4. Run `python3 scripts/validate_project.py` and `python3 scripts/install_skills.py --list`.
5. Preview before applying: `python3 scripts/install_skills.py --target /path/to/skills`; then use `--apply` only after confirming the target.

Never use the generic GitHub repo publication script to install skills or change system configuration. Do not assume a tool is installed solely because a skill names it.

## Entry routing

Do not ask users to invoke the many specialist skills manually. The four `superpower-*` entry skills route to relevant specialists via `superpowers.json` and their own stage instructions. The runtime must read and apply the child skills rather than assume name references execute code. Use `python3 scripts/superpower_plan.py --list` to view entrypoints.

## Third-party tools versus agent skills

The `tools/third-party/` directory contains pinned Git submodules for optional upstream Crapper, Dryer and Mutator. **They are external programs, not Agent Skills and not universal analyzers.** Use `python3 scripts/setup_optional_quality_tools.py --target /path/to/project --json` for a read-only language inventory, then explicitly initialize/install as documented in `docs/integrations/OPTIONAL-UNCLE-BOB-TOOLS.md`. The specialized quality skill decides whether to run them only after verifying supported files and an actual test baseline.

