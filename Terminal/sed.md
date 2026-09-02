# `sed`

**Concept:** Shell  
**Action:** Filter  
**Object:** `sed`  
**Classification:** Command  
**Environment:** Shell  
**Path Type:** N/A  
**Tags:** command

---

### What It Is

A stream editor used to search, filter, transform, and manipulate text.

### What It Does

Reads text line by line and applies specified editing commands to the input.

### How to Use

Run `sed` followed by options, an editing command, and an input source.

### Requirements

Shell

### Representation

```sh
sed 's/old/new/' file.txt
sed 's/old/new/g' file.txt
sed -n '1,5p' file.txt
sed -i '' 's/old/new/g' file.txt

```

### Flags

```text
-n — Suppress the normal output. Only print text when explicitly requested by a command such as p.
-i — Edit the input file directly instead of only printing the modified text.
      On macOS, -i is commonly followed by '' to specify no backup file.
      Example: sed -i '' 's/old/new/g' file.txt

```

### Editing Commands

```text
s — Substitute one piece of text for another.
      Example: sed 's/old/new/' file.txt

g — Replace every occurrence on each line instead of only the first occurrence.
      Example: sed 's/old/new/g' file.txt

p — Print the selected line or text.
      Example: sed -n '1,5p' file.txt

d — Delete the selected line or text from the output.
      Example: sed '5d' file.txt

a — Append text after the selected line.
      Example: sed '1a\New line' file.txt

i — Insert text before the selected line.
      Example: sed '1i\New line' file.txt

```

### Notes

`sed` normally reads the input and writes the transformed text to standard output. It does not modify the original file unless the `-i` option is used.

The `s` command uses the form:

```text
s/pattern/replacement/

```

For example:

```sh
sed 's/cat/dog/' file.txt

```

replaces the first occurrence of `cat` on each line with `dog`.

Adding `g`:

```sh
sed 's/cat/dog/g' file.txt

```

replaces every occurrence of `cat` on each line.

The `-n` option is particularly useful with `p`:

```sh
sed -n '1,5p' file.txt

```

prints only lines 1 through 5.

The `-i` option makes the transformation happen directly to the file:

```sh
sed -i '' 's/cat/dog/g' file.txt

```

On macOS, `''` tells `sed` not to create a backup file.

