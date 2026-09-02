# `touch`

**Concept:** Shell  
**Action:** Create  
**Object:** `touch`  
**Classification:** Command  
**Environment:** Shell  
**Path Type:** N/A  
**Tags:** command

---

### What It Is

A shell command used to create files or update file timestamps.

### What It Does

Creates a file if it does not exist, or updates its access and modification timestamps when it does.

### How to Use

Run `touch` followed by one or more file paths.

### Requirements

Shell

### Representation

```sh
touch file.txt
touch file1.txt file2.txt
touch -a file.txt
touch -m file.txt
touch -c file.txt
touch -r reference.txt file.txt
touch -t 202608311200 file.txt

```

### Flags

```text
-a — Change only the access time.

    Example:
    touch -a file.txt

    Updates the file's access time without intentionally changing
    its modification time.

-m — Change only the modification time.

    Example:
    touch -m file.txt

    Updates the file's modification time without intentionally
    changing its access time.

-c — Do not create the file if it does not already exist.

    Example:
    touch -c file.txt

    If file.txt does not exist, nothing is created. If it does
    exist, its timestamps can still be updated.

-r FILE — Use another file's timestamps.

    Example:
    touch -r reference.txt file.txt

    Sets the timestamps of file.txt to match the timestamps of
    reference.txt.

-t TIMESTAMP — Set a specific timestamp instead of using the
               current time.

    Example:
    touch -t 202608311200 file.txt

    Sets the file's timestamp to the specified date and time,
    using the timestamp format supported by the system.

```

### Notes

When `touch` is run on a file that does not exist, it normally creates an empty file:

```sh
touch file.txt

```

The important behavior, however, is what happens when the file **already exists**:

```sh
touch file.txt

```

does not erase or replace the contents of `file.txt`. Instead, it updates its timestamps.

A file has multiple timestamps associated with it. Two important ones are:

```text
Access time — When the file was last accessed.
Modification time — When the file's contents were last modified.

```

The `-a` and `-m` options allow these timestamps to be controlled independently.

Without either option:

```sh
touch file.txt

```

normally updates both the access and modification times to the current time.

The `-c` option changes the behavior when the target does not exist:

```sh
touch -c missing.txt

```

does not create `missing.txt`.

The `-r` option copies timestamps from another file:

```sh
touch -r reference.txt target.txt

```

This is useful when the target file needs to have the same timestamps as an existing file.

`touch` can also operate on multiple files at once:

```sh
touch one.txt two.txt three.txt

```

This creates each file if it does not already exist, or updates the timestamps of existing files.

The command can therefore be thought of as performing two related operations:

```text
File does not exist → create an empty file.
File already exists → update its timestamps.

```

It does **not** modify the existing contents of a file merely because `touch` was run on it.

