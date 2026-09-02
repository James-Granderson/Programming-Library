# `cp`

**Concept:** Shell  
**Action:** Combine  
**Object:** `cp`  
**Classification:** Command  
**Environment:** Shell  
**Path Type:** N/A  
**Tags:** command

---

### What It Is

A shell command used to copy files and directories.

### What It Does

Creates a copy of one or more source filesystem objects at a destination.

### How to Use

Run `cp` followed by optional flags, source paths, and a destination.

### Requirements

Shell

### Representation

```sh
cp source.txt destination.txt
cp -r source-directory/ destination-directory/
cp -i source.txt destination.txt
cp -v source.txt destination.txt
cp -p source.txt destination.txt
cp -f source.txt destination.txt

```

### Flags

```text
-r / -R — Recursively copy directories and their contents.

    Example:
    cp -r project/ project-backup/

    Copies the directory and everything contained inside it.

-i — Prompt before overwriting an existing destination file.

    Example:
    cp -i source.txt destination.txt

    If destination.txt already exists, `cp` asks for confirmation
    before replacing it.

-v — Print each file as it is copied.

    Example:
    cp -v source.txt backup.txt

    Displays the files being copied as the operation runs.

-p — Preserve file attributes such as permissions and timestamps.

    Example:
    cp -p source.txt backup.txt

    Attempts to preserve attributes from the source file on the copy.

-f — Force overwriting of destination files.

    Example:
    cp -f source.txt destination.txt

    Removes an existing destination file if necessary and copies
    the source without prompting.

```

### Notes

The basic form:

```sh
cp source.txt destination.txt

```

copies `source.txt` to `destination.txt`.

When the destination does not exist, a new file is created. When the destination already exists, `cp` normally replaces its contents, subject to permissions and other options.

Directories require recursive copying:

```sh
cp -r project/ project-backup/

```

Without `-r` or `-R`, `cp` normally will not copy a directory and its contents.

Flags can be combined:

```sh
cp -rv project/ project-backup/

```

This recursively copies the directory while printing each file as it is copied.

