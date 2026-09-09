# `git merge --allow-unrelated-histories`

**Concept:** Git
**Action:** Merge
**Object:** `git merge --allow-unrelated-histories`
**Classification:** Command
**Environment:** Git
**Path Type:** N/A
**Tags:** command

---

### What It Is

A variant of `git merge` that permits merging two branches with no shared commit history.

### What It Does

Bypasses Git's default refusal to merge histories that share no common ancestor commit.

### How to Use

Add the `--allow-unrelated-histories` flag when running `git merge` against a branch with disconnected history.

### Requirements

`git merge`  // The base command this flag modifies.

### Representation

```bash
git merge other-branch --allow-unrelated-histories
```
