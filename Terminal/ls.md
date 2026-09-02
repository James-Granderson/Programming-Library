# `ls`

**Concept:** Shell  
**Action:** Display  
**Object:** `ls`  
**Classification:** Command  
**Environment:** Shell  
**Path Type:** N/A  
**Tags:** command

---

### What It Is

A shell command that lists directory contents.

### What It Does

Displays files and directories at a specified path.

### How to Use

Run `ls` followed by optional flags and a path.

### Requirements

Shell

### Representation

```sh
ls
ls -l
ls -a
ls -lh
ls -R
ls -t
ls -S
ls -1

```

### Flags

```text
-l — Use long listing format.

    Example:
    ls -l

    Displays additional information such as permissions, ownership,
    file size, and modification time.

-a — Include hidden files.

    Example:
    ls -a

    Includes entries whose names begin with ".".

-h — Display human-readable file sizes.

    Example:
    ls -lh

    Displays sizes using units such as KB, MB, or GB instead of
    only raw byte counts. It is normally used with -l.

-R — Recursively list subdirectories.

    Example:
    ls -R project/

    Lists the contents of project/ and then continues into its
    subdirectories.

-t — Sort by modification time.

    Example:
    ls -lt

    Lists the most recently modified entries first.

-S — Sort by file size.

    Example:
    ls -lS

    Lists entries from largest to smallest.

-1 — Display one entry per line.

    Example:
    ls -1

    Prints each directory entry on its own line.

```

### Notes

Flags can be combined when their behaviors complement each other.

For example:

```sh
ls -lah

```

combines:

```text
-l — Long listing format.
-a — Include hidden files.
-h — Human-readable sizes.

```

Another useful combination is:

```sh
ls -lt

```

which uses long listing format while sorting entries by modification time.

The `-R` option is different from the other flags because it changes **how far** `ls` **searches** rather than simply changing how the entries are displayed:

```sh
ls -R

```

lists the current directory and then recursively lists the contents of its subdirectories.

