# Repository Status and Versioning

The canonical repository is **[Arthurzineo/llm-legacy-system-migration](https://github.com/Arthurzineo/llm-legacy-system-migration)**, published on the `main` branch with **private** visibility. The original local development branch was named `feat/orca-core-migration-skills`; its content has been imported into `main`.

## Getting started

```bash
git clone git@github.com:Arthurzineo/llm-legacy-system-migration.git
cd llm-legacy-system-migration
git status --short --branch
python3 -m unittest discover -s tests
```

Authenticate to GitHub to access this private repository. For HTTPS checkout, use `https://github.com/Arthurzineo/llm-legacy-system-migration.git` with your configured credential helper.

## Development policy

- Keep the ORCA core generic and reusable outside legacy migrations.
- Use the four Superpowers as user entry points; specialized skills remain modular.
- Preserve evidence and required reviews before declaring an implementation complete.
- Do not commit secrets, production data, or live AI Memory tokens.
- Treat AI Memory installation and agent MCP configuration as opt-in.
- Do not interpret published documentation as proof that a migration pipeline, legacy runtime, or MCP server has been implemented and validated.

This repository contains methodology, orchestration contracts, skills, scripts and tests. Real migration capability must be validated against representative legacy projects.
