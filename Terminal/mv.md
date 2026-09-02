# `mv`

**Concept:** Shell  
**Action:** Combine  
**Object:** `mv`  
**Classification:** Command  
**Environment:** Shell  
**Path Type:** N/A  
**Tags:** command

---

### What It Is

A shell command used to move or rename files and directories.

### What It Does

Moves filesystem objects to a new path or changes their names.

### How to Use

Run `mv` followed by optional flags, a source path, and a destination path.

### Requirements

Shell

### Representation

```text
mv old-name.txt new-name.txt

mv -i old-name.txt new-name.txt
mv -f old-name.txt new-name.txt
mv -v old-name.txt new-name.txt
mv -n old-name.txt new-name.txt

```

### Flags

```text
-i — Prompt before overwriting destination.
-f — Force overwriting without prompting.
-v — Print each file as it is moved.
-n — Never overwrite an existing destination.

```

