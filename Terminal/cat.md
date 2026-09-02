# `cat`

**Concept:** Shell
**Action:** Display
**Object:** `cat`
**Classification:** Command
**Environment:** Shell
**Path Type:** N/A
**Tags:** command

---

### What It Is

A shell command that reads and outputs files.

### What It Does

Writes one or more files to standard output.

### How to Use

Run `cat` followed by one or more file paths.

### Requirements

Shell

### Representation

```sh id="5xj8qp"
cat file.txt
cat -n file.txt
cat -b file.txt
cat -s file.txt
cat -A file.txt
```

### Flags

```text id="7m2kcx"
-n — Number all output lines.

    Example:
    cat -n file.txt

    Displays a line number beside every line, including blank lines.

-b — Number only non-blank lines.

    Example:
    cat -b file.txt

    Displays line numbers only beside lines that contain text.

-s — Squeeze repeated blank lines into one.

    Example:
    cat -s file.txt

    Multiple consecutive blank lines are reduced to a single blank
    line in the output.

-A — Show non-printing characters and line endings explicitly.

    Example:
    cat -A file.txt

    Makes characters such as tabs and line endings visible, which
    can help identify otherwise invisible formatting.
```

### Notes

`cat` can read multiple files and write them to standard output in the order provided:

```sh id="w3n8fz"
cat file1.txt file2.txt
```

The contents of `file1.txt` are followed by the contents of `file2.txt`.

Because `cat` writes to standard output, its output can also be redirected or piped into another command:

```sh id="c5x7rm"
cat file.txt > copy.txt
cat file.txt | less
```

The first command redirects the output into `copy.txt`. The second sends the output into `less` for interactive viewing.