# `echo`

**Concept:** Shell  
**Action:** Print  
**Object:** `echo`  
**Classification:** Command  
**Environment:** Shell  
**Path Type:** N/A  
**Tags:** command

---

### What It Is

A shell command or builtin used to write text to standard output.

### What It Does

Prints its arguments followed by a newline by default.

### How to Use

Run `echo` followed by the text to display.

### Requirements

Shell

### Representation

```sh
echo "hello"
echo -n "hello"
echo -e "hello\nworld"

```

### Flags

```text
-n — Suppress the trailing newline.

    Example:
    echo -n "hello"

    Output:
    hello

    The shell prompt appears immediately after "hello" instead of
    starting on a new line.

-e — Enable interpretation of backslash escapes on implementations
     that support this behavior.

    Example:
    echo -e "hello\nworld"

    Output:
    hello
    world

    The \n escape is interpreted as a newline.

```

### Notes

`echo` writes its arguments to standard output. By default, it adds a newline after the text:

```sh
echo "hello"

```

Output:

```text
hello

```

The `-n` option removes that trailing newline:

```sh
echo -n "hello"

```

The `-e` option allows certain backslash escape sequences to be interpreted:

```sh
echo -e "hello\tworld"

```

Output:

```text
hello    world

```

Support for `-e` and the exact behavior of escape sequences can vary between shells and implementations. For portable shell scripting, `printf` is generally preferred when precise output formatting is required.

