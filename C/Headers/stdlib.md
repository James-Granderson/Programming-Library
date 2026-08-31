# stdlib.h

**Concept:** C
**Action:** Include
**Object:** `stdlib.h`
**Classification:** Header
**Environment:** Any C compiler
**Path Type:** N/A
**Tags:** header

---

### What It Is

A standard C header that declares general utility functions, including dynamic memory allocation functions.

### What It Does

Makes declarations such as `malloc` and `free` available to a source file.

### How to Use

Place `#include <stdlib.h>` before code that calls `malloc` or `free`.

### Requirements

C standard library  // Provides the header.

### Representation

```c
#include <stdlib.h>

int main(void) {
    void *memory = malloc(16);
    free(memory);
}
```
