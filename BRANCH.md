# Local Development Branch

This project is intentionally maintained as a **local Git repository** for now. The active branch is `feat/orca-core-migration-skills`, branched from the preserved initial draft on `main`. No GitHub repository, remote, pull request, or public/private publication was created as part of this iteration.

After extracting the archive, inspect the local branch with:

```bash
git status -sb
git branch -a
git log --oneline --max-count=3
```

The owner has subsequently requested private publication, but this execution environment has no authenticated GitHub CLI or API operation to create the remote repository. Publication must remain pending until an authorized channel is available. Never make the repository public. Changes to the ORCA protocol, agent permissions, skills registry, or external MCP configuration should be reviewed together before any deployment or publication.

## Publish this local branch to a private GitHub repository

The repository does not yet exist remotely. This local branch can be published with:

```bash
# Run from an extracted checkout that includes .git
gh auth login
bash scripts/publish_private_github.sh
```

The script validates the existing branch, refuses a public destination, creates a private repository if necessary, pushes `main` first, and then pushes `feat/orca-core-migration-skills`. It performs **no** network writes until the user runs it in an authenticated environment.
