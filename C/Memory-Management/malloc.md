# `malloc`

**Concept:** C
**Action:** Allocate
**Object:** `malloc`
**Classification:** Function
**Environment:** Any C compiler
**Path Type:** N/A
**Tags:** function
---

---

### What It Is

A standard library function that allocates a requested number of bytes.

### What It Does

Reserves dynamically allocated memory and returns a pointer to its first byte, or `NULL` when allocation fails.

### How to Use

Include `<stdlib.h>`, call `malloc` with the required byte count, check the returned pointer against `NULL`, and release a successful allocation with `free`.

### Requirements

`<stdlib.h>`  // Declares `malloc`.
Pointer  // Receives the address of the allocated memory.

### Representation

```c
#include <stdlib.h>

int main(void) {
    int *number = malloc(sizeof *number);
    if (number != NULL) {
        *number = 42;
        free(number);
    }
}
```
