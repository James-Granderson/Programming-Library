# `stdin`

**Concept:** Shell
**Action:** Reference
**Object:** stdin
**Classification:** Shell Concept
**Environment:** Shell
**Path Type:** N/A
**Tags:** shell

---

### What It Is

The standard input stream of a process.

### What It Does

Provides input to a command or program.

### How to Use

Input can come from the terminal, another process through a pipe, or a redirected file.

### Requirements

Shell

### Representation

```text
keyboard
   │
   ▼
 stdin
   │
   ▼
 command
```

```sh
sort < names.txt
```
