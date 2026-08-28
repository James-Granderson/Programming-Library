# push

**Concept:** Git  
**Action:** Push  
**Object:** `git push`  
**Classification:** Command  
**Environment:** Git  
**Path Type:** N/A  
**Tags:** command  

---

### What It Is

A Git command used to upload local commits to a remote repository.

### What It Does

Sends commits from the local repository to the configured remote repository.

### How to Use

Use `git push` when Git is installed and available through the system PATH.

When Git is not available through PATH in PowerShell, invoke the Git executable using `&` and its absolute path before providing the `push` command.

### Requirements

Git  // Provides the `git push` command.
Committed changes  // Provides commits that can be sent to the remote repository.
Remote repository  // Provides the destination for the pushed commits.

### Representation

Git available in PATH:

```bash
git push