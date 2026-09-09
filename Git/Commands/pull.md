# `git pull`

**Concept:** Git
**Action:** Pull
**Object:** `git pull`
**Classification:** Command
**Environment:** Git
**Path Type:** N/A
**Tags:** command

---

### What It Is

A Git command that updates the current branch with changes from a remote branch.

### What It Does

Runs `git fetch` followed by `git merge` (or rebase, depending on configuration) in a single step.

### How to Use

Run `git pull` from within a branch that tracks a remote branch.

### Requirements

`git fetch`  // Retrieves the remote data this command merges.
`git merge`  // Integrates the retrieved data into the current branch.

### Representation

```bash
git pull origin main
```
