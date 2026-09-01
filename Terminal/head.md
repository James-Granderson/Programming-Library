# `head`

**Concept:** Shell
**Action:** Display
**Object:** `head`
**Classification:** Command
**Environment:** Shell
**Path Type:** N/A
**Tags:** command

---

### What It Is

A shell command that displays the beginning of a file or input stream.

### What It Does

Outputs the first portion of its input.

### How to Use

Run `head` followed by optional flags and one or more files.

### Requirements

Shell

### Representation

```sh
head file.txt
```

### Flags

```text

-n N — Show the first N lines instead of the default number.

-c N — Show the first N bytes instead of lines.

-q — Suppress filename headers when given multiple files.

-v — Always show filename headers, even for a single file.
```



### Examples



```text

head file.txt

head -n 5 file.txt

head -c 20 file.txt

head -q file1.txt file2.txt

head -v file.txt

```

