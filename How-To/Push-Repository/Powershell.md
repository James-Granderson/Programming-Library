# Push Repository

**Concept:** `PowerShell`
**Action:** Push
**Object:** Repository
**Classification:** How-To
**Environment:** `PowerShell`
**Path Type:** Absolute Path
**Tags:** command

---

### What It Is

A procedure for pushing local Git commits to a remote repository using PowerShell.

### What It Does

Stages, commits, and pushes local changes to the configured remote repository.

### How to Use

Run Git using its absolute path, stage the changes, create a commit, then push the commit to the remote repository.

### Requirements

Git  // Provides the Git commands used to stage, commit, and push changes.
Remote repository  // Provides the destination for the pushed commits.

### Representation

```powershell
& "C:\Program Files\Microsoft Visual Studio\2022\Community\Common7\IDE\CommonExtensions\Microsoft\TeamFoundation\Team Explorer\Git\cmd\git.exe" add .

& "C:\Program Files\Microsoft Visual Studio\2022\Community\Common7\IDE\CommonExtensions\Microsoft\TeamFoundation\Team Explorer\Git\cmd\git.exe" commit -m "Update programming library"

& "C:\Program Files\Microsoft Visual Studio\2022\Community\Common7\IDE\CommonExtensions\Microsoft\TeamFoundation\Team Explorer\Git\cmd\git.exe" push