# `*`

**Concept:** C
**Action:** Dereference
**Object:** `*`
**Classification:** Unary Operator
**Environment:** Any C compiler
**Path Type:** N/A
**Tags:** operator
---

---

### What It Is

The unary indirection operator.

### What It Does

Uses the address stored in a pointer to access the object at that address.

### How to Use

Place `*` before a pointer variable to access the object it points to.

### Requirements

Pointer  // Required because `*` accesses the object stored at a pointer's address.

### Representation

```c
int x = 10;
int *p = &x;
*p
