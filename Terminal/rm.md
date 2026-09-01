# `rm`

**Concept:** Shell  
**Action:** Delete  
**Object:** `rm`  
**Classification:** Command  
**Environment:** Shell  
**Path Type:** N/A  
**Tags:** command

---

### What It Is

A shell command used to remove files and directories.

### What It Does

Deletes filesystem objects specified as operands.

### How to Use

Run `rm` followed by optional flags and one or more paths.

### Requirements

Shell

### Representation

```sh
rm file.txt

```

Flags

```text
-r — Recursively remove directories and their contents.
-f — Force removal and suppress errors for nonexistent files.
-i — Prompt before each removal.
-v — Print each file as it is removed.
-d — Remove empty directories.

```

