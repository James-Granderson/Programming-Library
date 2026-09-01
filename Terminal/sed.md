# `sed`

**Concept:** Shell
**Action:** Filter
**Object:** `sed`
**Classification:** Command
**Environment:** Shell
**Path Type:** N/A
**Tags:** command
---

---

### What It Is

A stream editor used to search, filter, transform, and manipulate text.

### What It Does

Reads text line by line and applies specified editing commands to the input.

### How to Use

Run `sed` followed by options, editing commands, and an input source.

### Requirements

Shell

### Representation

```sh
sed 's/old/new/' file.txt
```

### Notes

The `sed` command can modify text streams without opening the file in an interactive editor.

Common options and flags include:

```sh
sed -n '...' file.txt
sed -i '' '...' file.txt

```

