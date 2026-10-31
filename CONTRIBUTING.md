# Contributing Skills and Workflow Changes

All repository artifacts must be in English, even when discussions or prompts are conducted in Portuguese or another language.

To add a reusable skill, create `skills/<category>/<unique-name>/SKILL.md`, add valid `name` and `description` YAML frontmatter, and describe preconditions, non-use boundaries, real execution steps, expected folder outputs and acceptance criteria. Do not assume external tools exist or mark synthetic tests as completed. Run `python3 scripts/validate_project.py` and `python3 -m unittest discover -s tests -v`.

To install selected skills in your local agent environment, first preview `python3 scripts/install_skills.py --target ~/.agents/skills`, then explicitly add `--apply`. The installer does not overwrite existing, differing skills unless `--force` is specified. Changes to an existing ORCA project should preserve source files and authoritative contracts.

Do not commit credentials, real customer data, production database exports, or AI Memory authentication tokens. External third-party skills/code must have their licenses reviewed and attributions preserved before copying.
