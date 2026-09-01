# `touch`

## **Concept:** Shell
**Action:** Create
**Object:** touch
**Classification:** Command
**Environment:** Shell
**Path Type:** N/A
**Tags:** command

---

### What It Is

A shell command used to create files or update file timestamps.

### What It Does

Creates a file if it does not exist, or updates its access and modification timestamps when it does.

### How to Use

Run touch followed by one or more file paths.

### Requirements

Shell

### Representation

```text
touch file.txt
Flags
-a — Update only the access time.
-m — Update only the modification time.
-c — Do not create the file if it does not already exist.
-r FILE — Use another file's timestamps.
-t TIMESTAMP — Set a specific timestamp.
```

