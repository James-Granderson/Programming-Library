# `NULL`

**Concept:** C
**Action:** Assign Value
**Object:** `NULL`
**Classification:** Macro
**Environment:** Any C compiler
**Path Type:** N/A
**Tags:** expression
---

---

### What It Is

A macro that represents a null pointer constant.

### What It Does

Provides a value that represents a pointer to no object.

### How to Use

Assign `NULL` to a pointer when it should point to no object.

### Requirements

`<stddef.h>`  // Defines `NULL`.
Pointer  // Required because `NULL` is used as a pointer value.

### Representation

```c
#include <stddef.h>

int *p = NULL;
