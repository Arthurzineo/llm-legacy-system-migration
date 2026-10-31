# Optional Uncle Bob Quality Tools — Pinned Git Submodules

The repository includes **source links** (Git submodules), not modified or copied snapshots, for three upstream projects. The original license in each submodule is **0BSD**. Respect license and upstream project boundaries. The code does not run merely because submodules are present.

| Tool | Git submodule | Pinned upstream commit | Purpose |
| --- | --- | --- | --- |
| [Crapper](https://github.com/unclebob/crapper) | `tools/third-party/crapper` | `6fd92c4c9bcc56efb64a2f8743d5a2993bcfd42d` | Cyclomatic complexity and measured test coverage combined into CRAP |
| [Dryer](https://github.com/unclebob/dryer) | `tools/third-party/dryer` | `66ff6d21a42c04afcad89c78a80066176d1294b0` | Candidate near-duplicate functions based on normalized syntax |
| [Mutator](https://github.com/unclebob/mutator) | `tools/third-party/mutator` | `a5a0cb803b66e0cdb8bf471b3b08af701d424a41` | Test mutation strength; requires Crapper checked out alongside it |

## Language compatibility

All three support Clojure, Java, Go, TypeScript/JavaScript, Rust and Python in the referenced upstream versions. They are **not universal source analyzers**. PHP, COBOL, C/C++, C#, Ruby, and other languages require independent suitable tools. A mixed-language project may use these tools **only for explicitly scoped supported-language files**. Recognizing a suffix is a discovery heuristic, not proof that a particular syntax variant, build, or test runner works.

## Clone and optionally install

~~~bash
git clone --recurse-submodules https://github.com/Arthurzineo/llm-legacy-system-migration.git
# Alternatively, from an existing checkout:
git submodule update --init tools/third-party/crapper tools/third-party/dryer tools/third-party/mutator

# Read-only evaluation of the legacy project's language mix and tool status:
python3 scripts/setup_optional_quality_tools.py --target /path/to/legacy --json

# Explicitly initialize the submodules in an existing checkout:
python3 scripts/setup_optional_quality_tools.py --install

# Explicitly create separate virtual environments and install upstream packages:
python3 scripts/setup_optional_quality_tools.py --prepare
~~~

The `--prepare` command runs `pip install -e .` within each pinned upstream source directory, which may execute package installation code and contact dependency indexes. Review the source, licenses and dependency manifests before approval. It does not run the analyzers against any project.

## Execution policy for agents

1. Use the read-only language/status report. Select only supported source files/directories; explicitly exclude repositories, fixtures and vendored dependencies.
2. Confirm upstream tool compatibility with the selected source, baseline tests and coverage format. If unsupported or ambiguous, select a language-appropriate alternative or mark `not_measured`.
3. Ask for permission before installing dependencies, automatically modifying a build/test environment, or running expensive mutation suites.
4. Run small targeted scopes first. Use the **actual** wrapper options in the pinned submodule READMEs; no unverified flags.
5. Crapper: only calculate CRAP when real coverage data is available; Dryer: similarity indicates review candidates, not logically identical behavior; Mutator: require a green baseline and account for surviving/uncovered mutants.
6. Store real command, source revision, tool revision, scope, measurements, failures and waivers in `docs/verification/quality/`. A skipped tool is not a successful gate.

This setup applies to both discovering legacy software and quality assurance of the target application, but optional tool execution is typically most useful during Part 2.
