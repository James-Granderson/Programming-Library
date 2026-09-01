# `return`

**Concept:** C
**Action:** Return
**Object:** `return`
**Classification:** Statement
**Environment:** Any C compiler
**Path Type:** N/A
**Tags:** keyword
---

---

### What It Is

A C statement that exits the current function and optionally supplies a value.

### What It Does

Ends function execution immediately and passes a value back to the caller when a return type is not `void`.

### How to Use

Write `return` inside a function, optionally followed by an expression whose type matches the function return type.

### Requirements

C language  // Defines function scope and return types.

### Representation

```c
int add(int a, int b) {
    return a + b;
}
```
