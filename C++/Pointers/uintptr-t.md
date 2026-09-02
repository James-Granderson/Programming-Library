# `uintptr_t`
# uintptr_t

**Concept:** `C++`
**Action:** Represent
**Object:** `uintptr_t`
**Classification:** Data Type
**Environment:** Any `C++` compiler
**Path Type:** N/A
**Tags:** keyword

---

### What It Is

An unsigned integer type capable of representing a converted pointer value when the implementation provides the type.

### What It Does

Provides an integer representation of a pointer value.

### How to Use

Include `<cstdint>` and use `reinterpret_cast<uintptr_t>` when an address needs to be represented as an integer.

### Requirements

`<cstdint>`  // Declares `uintptr_t` when supported.

### Representation

```cpp
#include <cstdint>

int value = 42;

uintptr_t address =
    reinterpret_cast<uintptr_t>(&value);
```

