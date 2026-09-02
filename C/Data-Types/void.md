# `void`

**Concept:** C
**Action:** Declare
**Object:** `void`
**Classification:** Data Type
**Environment:** Any C compiler
**Path Type:** N/A
**Tags:** keyword

---

### What It Is

A C type that represents the absence of a value.

### What It Does

Declares functions that return no value, or pointer types with an unspecified pointee type.

### How to Use

Write `void` as a function return type, or as `void *` when a pointer must not be tied to a specific type.

### Requirements

C language  // `void` is a built-in C type.

### Representation

```c
void greet(void);

void *handle;
```
