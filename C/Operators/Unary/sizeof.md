# `sizeof`

**Concept:** C
**Action:** Measure
**Object:** `sizeof`
**Classification:** Unary Operator
**Environment:** Any C compiler
**Path Type:** N/A
**Tags:** operator
---

---

### What It Is

A unary operator that yields the size of a type or expression in bytes.

### What It Does

Evaluates to the number of bytes occupied by the given type or the type of the given expression.

### How to Use

Write `sizeof` followed by a type in parentheses or an expression.

### Requirements

C language  // Defines object and type sizes at compile time.

### Representation

```c
int n = sizeof(int);
size_t bytes = sizeof n;
```
