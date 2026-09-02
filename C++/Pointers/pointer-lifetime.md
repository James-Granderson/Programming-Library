# `Pointer Lifetime`
# Pointer Lifetime

**Concept:** `C++`
**Action:** Measure
**Object:** Pointer Lifetime
**Classification:** Pointer Concept
**Environment:** Any `C++` compiler
**Path Type:** N/A
**Tags:** keyword

---

### What It Is

The period during which a pointer object exists and can be used as a pointer.

### What It Does

Separates the lifetime of the pointer from the lifetime of the object to which it refers.

### How to Use

Track the lifetime of the pointer separately from the lifetime of its referenced object.

### Requirements

Pointer  // The pointer has its own lifetime.
Object  // The referenced object may have a different lifetime.

### Representation

```cpp
int *number = new int(42);

{
    int *alias = number;
}

delete number;
```

