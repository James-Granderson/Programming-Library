# free

**Concept:** C
**Action:** Deallocate
**Object:** `free`
**Classification:** Function
**Environment:** Any C compiler
**Path Type:** N/A
**Tags:** function

---

### What It Is

A standard library function that releases memory previously allocated dynamically.

### What It Does

Returns allocated memory to the allocator so it can be reused.

### How to Use

Pass `free` a pointer returned by an allocation function after the program no longer needs the allocation. Do not use the pointer after freeing it.

### Requirements

`<stdlib.h>`  // Declares `free`.
`malloc`  // Commonly provides the allocation that `free` releases.

### Representation

```c
#include <stdlib.h>

int main(void) {
    int *number = malloc(sizeof *number);
    if (number != NULL) {
        free(number);
    }
}
```
