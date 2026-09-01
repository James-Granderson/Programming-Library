# `find`

**Concept:** Shell
**Action:** Search
**Object:** `find`
**Classification:** Command
**Environment:** Shell
**Path Type:** N/A
**Tags:** command

---

### What It Is

A shell command used to search for files and directories within a directory tree.

### What It Does

Starts at a specified directory, examines the files and directories beneath it, and applies search conditions to determine which objects match.

### How to Use

Run `find` followed by the directory where the search should begin, then provide one or more search conditions.

### Requirements

Shell

### Representation

```sh
find [path] [expression]
```

Example:

```sh
find . -type f -name "*.md"
```

This means:

* `find` — Starts the search.
* `.` — Starts the search from the current directory.
* `-type f` — Matches only regular files.
* `-name "*.md"` — Matches files whose names end in `.md`.

For example, if the current directory contains:

```text
./README.md
./Terminal/head.md
./Terminal/find.md
./C++/Pointers/pointer.md
./notes.txt
```

the command returns:

```text
./README.md
./Terminal/head.md
./Terminal/find.md
./C++/Pointers/pointer.md
```

The important part is that `find` recursively searches the directory tree, so you do not have to manually search each subdirectory.

Flags

```text
-name PATTERN — Match files and directories by name, case-sensitive.
-iname PATTERN — Match files and directories by name, case-insensitive.
-type f — Match regular files.
-type d — Match directories.
-type l — Match symbolic links.
-maxdepth N — Search only N levels below the starting path.
-mindepth N — Ignore objects above N levels below the starting path.
-size N — Match objects according to their file size.
-mtime N — Match objects according to their modification time in days.
-exec CMD {} — Execute a command for each matched object.
-delete — Delete matched files and directories.
```

