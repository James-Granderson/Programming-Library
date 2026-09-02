# `new`
# new

**Concept:** `C++`
**Action:** Allocate
**Object:** `new`
**Classification:** Pointer Concept
**Environment:** Any `C++` compiler
**Path Type:** N/A
**Tags:** keyword

---

### What It Is

A C++ operator that dynamically creates an object and returns a pointer to it.

### What It Does

Creates an object whose lifetime is independent of the scope of the pointer that receives its address.

### How to Use

Apply `new` to a type or expression that creates the desired object.

### Requirements

Pointer  // Receives the address of the dynamically allocated object.

### Representation

```cpp
int *number = new int(42);
delete number;
```

