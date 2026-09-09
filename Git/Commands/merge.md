# `git merge`

**Concept:** Git
**Action:** Merge
**Object:** `git merge`
**Classification:** Command
**Environment:** Git
**Path Type:** N/A
**Tags:** command

---

### What It Is

A Git command that integrates changes from one branch into another.

### What It Does

Combines the commit history of the specified branch into the current branch, creating a merge commit when the histories have diverged.

### How to Use

Check out the branch you want to merge into, then run `git merge` followed by the name of the branch to merge in.

### Requirements

Git  // Provides the `git merge` command.
Common commit history  // Required unless using `git merge --allow-unrelated-histories`.

### Representation

```bash
git merge feature-branch
```
