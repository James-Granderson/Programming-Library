# `this`
# this

**Concept:** `C++`
**Action:** Reference
**Object:** `this`
**Classification:** Pointer Concept
**Environment:** Any `C++` compiler
**Path Type:** N/A
**Tags:** keyword

---

### What It Is

A C++ keyword that refers to the current object inside a non-static member function.

### What It Does

Provides access to the current object's address and members from within a member function.

### How to Use

Use `this` inside a non-static member function when the current object's identity or address needs to be referenced explicitly.

### Requirements

Class object  // Provides the current object for the member function.

### Representation

```cpp
class Client {
public:
    uintptr_t ClientId() const {
        return reinterpret_cast<uintptr_t>(this);
    }
};
```

