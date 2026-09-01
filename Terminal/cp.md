# `cp`

**Concept:** Shell  
**Action:** Combine  
**Object:** `cp`  
**Classification:** Command  
**Environment:** Shell  
**Path Type:** N/A  
**Tags:** command

---

### What It Is

A shell command used to copy files and directories.

### What It Does

Creates a copy of one or more source filesystem objects at a destination.

### How to Use

Run `cp` followed by optional flags, source paths, and a destination.

### Requirements

Shell

### Representation

```sh
cp source.txt destination.txt

```

Flags

```text
-r / -R — Recursively copy directories and their contents.
-i - Prompt before overwriting an existing destination file.
-v — Print each file as it is copied.
-p — Preserve file attributes such as permissions and timestamps.
-f — Force overwriting of destination files.

```

