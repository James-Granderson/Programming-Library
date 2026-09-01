# `grep`

**Concept:** Shell
**Action:** Search
**Object:** grep
**Classification:** Command
**Environment:** Shell
**Path Type:** N/A
**Tags:** command
---

---

### What It Is

A shell command that searches input for lines matching a pattern.
### What It Does

Reads files or standard input and outputs lines that match a specified pattern.
### How to Use

Run grep followed by optional flags, a search pattern, and an input source.
### Requirements

Shell
### Representation
grep "pattern" file.txt
Flags
-i — Perform a case-insensitive match.
-v — Invert the match and show non-matching lines.ecursively search directories.
-n — Show line numbers with matching lines.
-c — Show only the count of matching lines.
-l — Show only filenames containing a match.
-w — Match whole words only.
-E — Enable extended regular expressions.
