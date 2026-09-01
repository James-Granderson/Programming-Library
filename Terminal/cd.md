# `cd`

**Concept:** Shell  
**Action:** Access Path  
**Object:** `cd`  
**Classification:** Command  
**Environment:** Shell  
**Path Type:** N/A  
**Tags:** command

---

### What It Is

A shell builtin used to change the current working directory.

### What It Does

Changes the shell's current working directory.

### How to Use

Run `cd` followed by a directory path.

### Requirements

Shell

### Representation

```sh
cd /path/to/directory

```

Flags

```text
-P — Resolve the physical path by following symbolic links.
-L — Use the logical path and preserve symbolic-link components.

```

