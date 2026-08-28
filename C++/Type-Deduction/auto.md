# auto

**Concept:** C++
**Action:** Deduce Type
**Object:** `auto`
**Classification:** Type Deduction Specifier
**Environment:** Any C++11 or later compiler
**Path Type:** N/A

---

### What It Is

A specifier that allows the compiler to deduce a variable's type from its initializer.

### What It Does

Automatically determines the type of a variable from the value used to initialize it.

### How to Use

Use `auto` in place of an explicit variable type when the initializer provides the required type information.

### Requirements

`C++11`  // Introduced `auto` type deduction for variables.

### Representation

```cpp
auto number = 42;
```
