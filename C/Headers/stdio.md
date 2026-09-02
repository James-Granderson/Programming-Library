# `stdio.h`

**Concept:** C
**Action:** Include
**Object:** `stdio.h`
**Classification:** Header
**Environment:** Any C compiler
**Path Type:** N/A
**Tags:** header

---

### What It Is

A standard C header that declares input and output facilities.

### What It Does

Makes declarations such as `printf` available to a source file.

### How to Use

Place `#include <stdio.h>` before code that calls a function declared by the header.

### Requirements

C standard library  // Provides the header.

### Representation

```c
#include <stdio.h>

int main(void) {
    printf("Hello, world!\n");
}
```
