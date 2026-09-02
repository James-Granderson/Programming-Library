# `&`

**Concept:** C
**Action:** Address
**Object:** `&`
**Classification:** Unary Operator
**Environment:** Any C compiler
**Path Type:** N/A
**Tags:** operator

---

### What It Is

The unary address-of operator.

### What It Does

Produces the memory address of an object.

### How to Use

Place `&` before a variable to obtain a pointer to that object.

### Requirements

Pointer  // Receives the address produced by `&`.

### Representation

```c
int x = 10;
int *p = &x;
```
