# `printf`

**Concept:** C
**Action:** Print
**Object:** `printf`
**Classification:** Function
**Environment:** Any C compiler
**Path Type:** N/A
**Tags:** function

---

### What It Is

A standard library function that writes formatted output to standard output.

### What It Does

Converts values to text according to a format string and prints the result.

### How to Use

Include `<stdio.h>`, provide a format string, and pass a value for each conversion specifier in that string.

### Requirements

`<stdio.h>`  // Declares `printf`.

### Representation

```c
#include <stdio.h>

int main(void) {
    printf("%d\n", 42);
}
```
