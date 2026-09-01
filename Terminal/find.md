# find

**Concept:** Shell
**Action:** Search
**Object:** find
**Classification:** Command
**Environment:** Shell
**Path Type:** N/A
**Tags:** command
---
### What It Is
What It Is

A shell command that searches directory trees for files and directories matching specified conditions.
### What It Does
What It Does

Traverses a directory hierarchy and evaluates expressions against each filesystem object.
### How to Use
How to Use

Run find followed by a starting path and optional expressions.
### Requirements
Requirements

Shell
### Representation
Representation
find . -name "*.md"
Flags
-name PATTERN — Match files by name, case-sensitive.
-iname PATTERN — Match files by name, case-insensitive.
-type f|d|l — Restrict matches to regular files, directories, or symbolic links.
-maxdepth N / -mindepth N — Limit how many directory levels ize N — Match objects by file size.
-mtime N — Match objects by modification time in days.
-exec CMD {} \; — Execute a command for each matched result.
-delete — Delete matched files.
