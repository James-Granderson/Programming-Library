# `mkdir`

**Concept:** Shell  
**Action:** Create  
**Object:** `mkdir`  
**Classification:** Command  
**Environment:** Shell  
**Path Type:** N/A  
**Tags:** command

---

### What It Is

A shell command used to create directories.

### What It Does

Creates one or more directories in the filesystem.

### How to Use

Run `mkdir` followed by one or more directory paths.

**Example:**

```sh
mkdir projects
mkdir projects/src

```

### Requirements

Shell

### Representation

```sh
mkdir directory

```

Flags

```text
-p — Create parent directories as needed and do not report an error if the requested directory already exists.
-m MODE — Set permissions on the new directory.
-v — Print a message for each directory created.

```

