# `sort`

**Concept:** Shell  
**Action:** Sort  
**Object:** `sort`  
**Classification:** Command  
**Environment:** Shell  
**Path Type:** N/A  
**Tags:** command

---

### What It Is

A shell command that sorts lines of text.

### What It Does

Reads input and outputs its lines in sorted order.

### How to Use

Run `sort` followed by optional flags and an input source.

### Requirements

Shell

### Representation

```sh
sort file.txt
sort -n numbers.txt
sort -r file.txt
sort -k 2 file.txt
sort -u file.txt
sort -f file.txt

```

### Flags

```text
-n — Sort numerically instead of comparing values as text.

    Example:
    sort -n numbers.txt

    Input:
    10
    2
    30
    4

    Output:
    2
    4
    10
    30

-r — Reverse the sort order.

    Example:
    sort -r file.txt

    If the normal order is:
    apple
    banana
    orange

    The reverse order is:
    orange
    banana
    apple

-k N — Sort according to a specified field or key.

    Example:
    sort -k 2 people.txt

    If the file contains:
    James 25
    Alex 19
    Sarah 31

    The second field is used for sorting.

-u — Output only unique lines.

    Example:
    sort -u file.txt

    Input:
    apple
    banana
    apple
    orange
    banana

    Output:
    apple
    banana
    orange

-f — Perform a case-insensitive comparison.

    Example:
    sort -f file.txt

    This treats uppercase and lowercase letters as equivalent
    when comparing lines.

```

### Notes

By default, `sort` compares lines as text rather than as numerical values. This is why numbers can produce unexpected results:

```sh
sort numbers.txt

```

can produce:

```text
10
2
30
4

```

because the comparison is based on the characters, not the numerical values.

Using `-n` tells `sort` to interpret the values numerically:

```sh
sort -n numbers.txt

```

which produces:

```text
2
4
10
30

```

The `-k` option is useful when each line contains multiple fields. For example:

```text
James 25
Alex 19
Sarah 31

```

```sh
sort -k 2 people.txt

```

sorts according to the second field rather than the entire line.

