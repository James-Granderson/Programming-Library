# `uniq`

**Concept:** Shell  
**Action:** Filter  
**Object:** `uniq`  
**Classification:** Command  
**Environment:** Shell  
**Path Type:** N/A  
**Tags:** command

---

### What It Is

A shell command that filters adjacent repeated lines from input.

### What It Does

Compares neighboring lines and reports or removes repeated occurrences according to its options.

### How to Use

Run `uniq` with optional flags and an input file or piped input.

### Requirements

Shell

### Representation

```sh
uniq file.txt
sort file.txt | uniq
uniq -c file.txt
uniq -d file.txt
uniq -u file.txt
uniq -i file.txt

```

### Flags

```text
-c — Prefix each line with its number of occurrences.

    Example:
    uniq -c file.txt

    Input:
    apple
    apple
    banana
    banana
    banana

    Output:
    2 apple
    3 banana

-d — Output only lines that appear more than once.

    Example:
    uniq -d file.txt

    Input:
    apple
    apple
    banana
    orange
    orange

    Output:
    apple
    orange

-u — Output only lines that appear exactly once.

    Example:
    uniq -u file.txt

    Input:
    apple
    apple
    banana
    orange
    orange

    Output:
    banana

-i — Perform case-insensitive comparisons.

    Example:
    uniq -i file.txt

    Input:
    Apple
    apple
    banana

    Output:
    Apple
    banana

```

### Notes

`uniq` compares **adjacent lines**. It does not search the entire input for duplicates.

For example:

```text
apple
banana
apple

```

Running:

```sh
uniq file.txt

```

does not remove either occurrence of `apple` because the two `apple` lines are not next to each other.

This is why `uniq` is commonly combined with `sort`:

```sh
sort file.txt | uniq

```

`sort` places identical lines next to each other, allowing `uniq` to identify and filter them.

The same idea can be used with `-c` to count occurrences:

```sh
sort file.txt | uniq -c

```

For example:

```text
apple
apple
banana
orange
orange
orange

```

becomes:

```text
2 apple
1 banana
3 orange

```

