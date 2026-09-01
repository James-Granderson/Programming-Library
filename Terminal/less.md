# `less`

**Concept:** Shell
**Action:** Display
**Object:** less
**Classification:** Command
**Environment:** Shell
**Path Type:** N/A
**Tags:** command
---

---

### What It Is

A terminal pager used to view text one screen at a time.
### What It Does

Displays file or command output interactively without requiring the entire input to fit on the screen.
### How to Use

Run less followed by a file or pipe input into it.
### Requirements

Shell
### Representation
less file.txt
Flags
-N — Show line numbers.
-S — Chop long lines instead of wrapping them.
-i — Make searches case-insensitive unless the search pattern contains uppercase characters.
-F — Exit immediately when the entire content fits on one screen.
-X — Prevent the terminal from being cleared when less exits.
