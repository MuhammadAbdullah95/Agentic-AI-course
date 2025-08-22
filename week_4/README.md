# Week 4 — Git & Version Control (Complete Guide)

This file explains the Git/GitHub topics shown in the supplied image and provides practical commands, workflows, and tips for collaboration. Use it as a classroom reference and quick command cheat-sheet.

## Overview

Git is a distributed version control system used to track changes in source code and collaborate with others. GitHub is a popular hosting service for Git repositories that adds collaboration features (pull requests, issues, CI integrations).

Core topics covered:
- Git/GitHub workflow & CLI commands
- Commit / Push / Pull
- Branching & Merging
- GUI vs CLI
- Collaboration techniques (PRs, code review, branching strategies)

## Installation & Basic Configuration

Install Git: https://git-scm.com/downloads

Set your identity once per machine:

```powershell
git config --global user.name "Your Name"
git config --global user.email "you@example.com"
git config --global core.editor "code --wait"
```

Verify configuration:

```powershell
git config --list
```

## Repository Basics

Initialize a new repository in a project folder:

```powershell
cd path\to\project
git init
```

Clone an existing repository (from GitHub):

```powershell
git clone https://github.com/owner/repo.git
```

Check repository status and history:

```powershell
git status
git log --oneline --graph --decorate --all
```

## The Standard Local Workflow (Edit → Commit → Push)

1. Edit files locally.
2. Stage changes you want to include in the next commit.
3. Commit staged changes with a message.
4. Push commits to a remote repository.

Common commands:

```powershell
# Stage all changes (new/modified/deleted)
git add .

# Stage a specific file
git add src/app.py

# Commit staged changes with a descriptive message
git commit -m "Fix input parsing and add tests"

# Push the current branch to the remote named 'origin'
git push origin main

# Pull remote changes and merge into current branch
git pull origin main
```

Notes:
- Use small, focused commits that capture a single logical change.
- Write clear commit messages. A common format: "<type>: short description" (e.g., "fix: handle empty input").

## Understanding Commit / Push / Pull

- Commit: records a snapshot in your local repository. Commits are local until pushed.
- Push: uploads your local commits to a remote repository (e.g., GitHub).
- Pull: fetches remote changes and merges them into your current branch (fetch + merge). Use `git fetch` + `git merge` for more control.

Useful variants:

```powershell
# Fetch only (does not modify working tree)
git fetch origin

# View differences between your branch and remote
git log --oneline HEAD..origin/main
git diff origin/main

# Pull and rebase (linear history)
git pull --rebase origin main
```

## Branching — Why and How

Branches let you work on features, fixes, or experiments in isolation. Keep `main`/`master` stable and create branches for work.

Create and switch to a new branch:

```powershell
git checkout -b feature/add-login
```

Push a branch to remote:

```powershell
git push -u origin feature/add-login
```

List branches:

```powershell
git branch        # local
git branch -r     # remote
git branch -a     # all
```

Merge a branch into main (fast-forward or merge commit):

```powershell
# switch to main
git checkout main
git pull origin main
# merge
git merge feature/add-login
git push origin main
```

Delete a branch (local and remote):

```powershell
git branch -d feature/add-login
git push origin --delete feature/add-login
```

## Merging vs Rebasing

- Merge: preserves historical branching structure. Creates a merge commit when histories diverge.
- Rebase: moves your commits onto the tip of another branch, creating a linear history. Good for small, private branches.

Commands:

```powershell
# Merge (safe, preserves history)
git checkout main
git merge feature/add-login

# Rebase your feature branch onto main (clean history for review)
git checkout feature/add-login
git fetch origin
git rebase origin/main
```

Tips:
- Avoid rebasing public branches that others may have based work on.
- Use rebase to keep your feature branch up-to-date before opening a PR.

## Resolving Merge Conflicts

When two branches change the same lines, Git marks conflicts. Workflow:

1. Git stops the merge/rebase and marks conflicted files.
2. Open the conflicted files, look for conflict markers (<<<<<<<, =======, >>>>>>>).
3. Edit to choose or combine the changes.
4. After resolving, stage the files and continue the merge/rebase:

```powershell
git add resolved_file.py
# If merging
git commit
# If rebasing
git rebase --continue
```

Always run tests and review behavior after resolving conflicts.

## Pull Requests (PRs) & Collaboration Workflow

Common flow for collaborative teams:

1. Create a feature branch from `main`.
2. Push branch to remote and open a Pull Request (PR) on GitHub.
3. Request reviewers, run CI (tests/linting), and address feedback.
4. Merge PR once approvals pass (use Merge, Squash, or Rebase policies defined by the team).

PR tips:
- Keep PRs small and focused.
- Add a clear description, steps to reproduce, and testing notes.
- Link issues and use descriptive branch names.

## GUI vs CLI — Pros and Cons

CLI (git commands)
- Pros: full power and precision, scriptable, fastest for experienced users.
- Cons: steeper learning curve, easy to run dangerous commands if unfamiliar.

GUI tools (GitHub Desktop, SourceTree, GitKraken, VS Code built-in)
- Pros: visual diff/commit history, easier conflict resolution for beginners, lower entry barrier.
- Cons: may hide details; not all advanced workflows are exposed.

Recommendation: learn CLI basics first (clone, add, commit, push, branch, merge). Then use a GUI as a productivity aid.

## Collaboration Techniques & Branching Strategies

- Git Flow: long-lived `develop` and `main`, feature branches, release branches. Good for release-driven teams but more complex.
- GitHub Flow: simple — short-lived feature branches, PRs to `main`. Good for continuous deployment.
- Trunk-Based Development: short-lived branches or direct commits to trunk with feature flags. Emphasizes frequent integration.

Pick a strategy suitable for team size and release cadence.

Code review best practices
- Provide constructive feedback, focus on behavior and readability.
- Request small changes via targeted comments.
- Use CI checks to catch style/test regressions automatically.

## Handy Commands / Cheat Sheet

```powershell
# Show status
git status

# Stage changes
git add <file>
git add .

# Commit
git commit -m "message"

# Amend last commit (if not pushed)
git commit --amend -m "updated message"

# Push
git push origin <branch>

# Pull (fetch + merge)
git pull origin <branch>

# Fetch only
git fetch origin

# Show log graph
git log --oneline --graph --decorate --all

# Create and switch to branch
git checkout -b <branch>

# Switch branch
git checkout <branch>

# Merge branch into current
git merge <branch>

# Rebase current branch onto another
git rebase <branch>

# Stash changes (temporary save)
git stash
git stash apply

# Undo local changes to a file
git checkout -- <file>

# Remove file from staging (keep file)
git reset <file>

# Delete local branch
git branch -d <branch>

# Delete remote branch
git push origin --delete <branch>
```

## Safety Tips

- Commit small, tested changes.
- Pull frequently to minimize conflicts.
- Use feature branches for any non-trivial work.
- Protect `main`/`master` by using branch protection rules on GitHub.
- Use `.gitignore` to avoid committing build artifacts, secrets, or large files.

## Advanced Topics (short notes)

- Tags: use `git tag` for release snapshots.
- Submodules: embed other Git repos — powerful but complex.
- Hooks: run scripts on commit/push for linting or tests.

## Classroom Exercises

1. Initialize a repo, create a branch, add a file, commit, push, open a PR and merge it.
2. Create conflicting edits in two branches and practice resolving the conflict.
3. Practice interactive rebase to squash multiple commits into a clean change.

---

If you want, I can also add:
- A printable one-page cheat sheet with the most used commands.
- Example `gitignore` templates for Python/Node projects.
- A small script that automates a common workflow (create branch, push, open PR link).
