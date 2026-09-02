# `Repository`

**Concept:** PowerShell
**Action:** Clone
**Object:** Repository
**Classification:** How-To
**Environment:** PowerShell
**Path Type:** Absolute
**Tags:** command

---

### What It Is

A procedure for cloning a Git repository onto a Windows computer using PowerShell.

### What It Does

Downloads the repository and creates a local working copy that can be opened in Cursor.

### How to Use

Navigate to the desired location, execute Git using its absolute path, provide the repository URL, then enter the cloned directory and launch it with Cursor.

### Requirements

Git  // Provides the `clone` command.
Repository URL  // Provides the repository to clone.
Cursor  // Opens the local repository.

### Representation

```powershell
cd "$env:USERPROFILE"

& "$env:LOCALAPPDATA\Programs\Git\cmd\git.exe" clone <REPOSITORY-URL>

cd ".\<REPOSITORY-NAME>"

& "$env:LOCALAPPDATA\Programs\cursor\Cursor.exe" .
