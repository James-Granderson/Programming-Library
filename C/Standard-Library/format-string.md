# `Format String`

**Concept:** C
**Action:** Format
**Object:** Format String
**Classification:** Format String
**Environment:** Any C compiler
**Path Type:** N/A
**Tags:** format-string
---

---

### What It Is

A string containing ordinary text and conversion specifiers for a formatted input or output function.

### What It Does

Tells a function such as `printf` how to convert values to text. For example, `%d` formats an `int` value.

### How to Use

Pass a format string as the first argument to `printf` and provide one matching value for each conversion specifier.

### Requirements

`<stdio.h>`  // Declares `printf`.

### Representation

```c
#include <stdio.h>

int main(void) {
    int count = 3;
    printf("Count: %d\n", count);
}
```
