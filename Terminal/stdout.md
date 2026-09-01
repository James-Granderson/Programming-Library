# `stdout`

**Concept:** Shell
**Action:** Print
**Object:** stdout
**Classification:** Shell Concept
**Environment:** Shell
**Path Type:** N/A
**Tags:** shell
---

---

---

### What It Is

The standard output stream of a process.

### What It Does

Carries normal output produced by a command or program.

### How to Use

Output normally appears in the terminal, but it can be piped or redirected.

### Requirements

Shell

### Representation

```text
command
   │
   ▼
 stdout
   │
   ├──→ terminal
   ├──→ file
   └──→ pipe

```

### Example

```sh
echo "hello" > output.txt

```

Here, `echo` writes `"hello"` to stdout, and `>` redirects that stdout into `output.txt`.
