# `rm`

**Concept:** Shell  
**Action:** Delete  
**Object:** `rm`  
**Classification:** Command  
**Environment:** Shell  
**Path Type:** N/A  
**Tags:** command

---

### What It Is

A shell command used to remove files and directories.

### What It Does

Deletes filesystem objects specified as operands.

### How to Use

Run `rm` followed by optional flags and one or more paths.

### Requirements

Shell

### Representation

```sh
rm file.txt
rm -r directory/
rm -f file.txt
rm -i file.txt
rm -v file.txt
rm -d empty-directory/

```

### Flags

```text
-r — Recursively remove directories and their contents.

    Example:
    rm -r project/

    Removes the directory and the files and directories contained inside it.

-f — Force removal and suppress errors for nonexistent files.

    Example:
    rm -f file.txt

    Removes file.txt without prompting and does not report an error
    if file.txt does not exist.

-i — Prompt before each removal.

    Example:
    rm -i file.txt

    Asks for confirmation before removing the file.

-v — Print each file as it is removed.

    Example:
    rm -v file.txt

    Displays the file being removed.

-d — Remove empty directories.

    Example:
    rm -d empty-directory/

    Removes the directory only if it is empty.

```

### Notes

`rm` normally removes files without moving them to a recycle bin or trash. Once removed, recovery may not be possible.

Directories require special handling. The `-r` option tells `rm` to recursively descend into a directory and remove its contents:

```sh
rm -r project/

```

Because `rm -r` can remove an entire directory tree, it should be used carefully.

The `-f` option suppresses confirmation and certain errors:

```sh
rm -rf project/

```

Combining `-r` and `-f` allows an entire directory tree to be removed without prompting, making this a particularly destructive command.

