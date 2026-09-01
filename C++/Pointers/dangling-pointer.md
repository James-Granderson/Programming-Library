# `Dangling Pointer`
# Dangling Pointer

**Concept:** `C++`
**Action:** Reference
**Object:** Dangling Pointer
**Classification:** Pointer Concept
**Environment:** Any `C++` compiler
**Path Type:** N/A
**Tags:** keyword
---

---

### What It Is

A pointer whose stored address refers to an object whose lifetime has ended.

### What It Does

Does not provide valid access to the former object. Dereferencing a dangling pointer produces undefined behavior.

### How to Use

Avoid retaining or dereferencing pointers after the lifetime of their referenced object has ended.

### Requirements

Pointer  // Contains the address of an object.
Object lifetime  // Determines whether the referenced object still exists.

### Representation

```cpp
int *number = new int(42);

delete number;
number = nullptr;
```

