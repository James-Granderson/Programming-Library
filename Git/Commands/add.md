# add

**Concept:** Git  
**Action:** Stage  
**Object:** `git add`  
**Classification:** Command  
**Environment:** Git  
**Path Type:** N/A  
**Tags:** command  

---

### What It Is

A Git command used to stage changes for a commit.

### What It Does

Adds selected changes to the staging area so they can be included in the next commit.

### How to Use

Specify the files or directories whose changes you want to stage.

The `.` represents the current directory, so `git add .` stages changes throughout the current directory and its contents. You can also specify individual files or directories when you only want to stage particular changes.

### Requirements

Git  // Provides the `git add` command.

### Representation

```bash
git add .
git add README.md
git add C/Data-Types/char.md
git add C/