# `cd`

**Concept:** Shell
**Action:** Access Path
**Object:** `cd`
**Classification:** Command
**Environment:** Shell
**Path Type:** N/A
**Tags:** command

---

### What It Is

A shell builtin used to change the current working directory.

### What It Does

Changes the shell's current working directory.

### How to Use

Run `cd` followed by a directory path.

### Requirements

Shell

### Representation

```sh
cd /path/to/directory
cd ..
cd ~
cd -
cd -P /path/to/directory
cd -L /path/to/directory
```

### Flags

```text
-P — Resolve the physical path by following symbolic links.

    Example:
    cd -P /path/to/symlink

    The shell resolves symbolic links in the path and sets the
    working directory to the physical directory.

-L — Use the logical path and preserve symbolic-link components.

    Example:
    cd -L /path/to/symlink

    The shell preserves symbolic-link components when determining
    the logical working directory.
```

### Notes

`cd` changes the current working directory of the **current shell**. Unlike commands such as `ls` or `cp`, it is normally implemented as a shell builtin because an external program cannot change the working directory of its parent shell.

Some common forms of `cd` do not use flags:

```sh
cd ..
```

Moves to the parent directory.

```sh
cd ~
```

Moves to the user's home directory.

```sh
cd -
```

Returns to the previous working directory.

The `-P` and `-L` options matter when symbolic links are involved. For example, if `~/project` is a symbolic link to `/actual/projects/project`, `cd -P ~/project` resolves the link and uses the physical path, while `cd -L ~/project` preserves the logical path represented by the symbolic link.