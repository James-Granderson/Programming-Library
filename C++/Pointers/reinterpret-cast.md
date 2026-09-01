# `reinterpret_cast`
**Concept:** `C++`
**Action:** Represent
**Object:** `reinterpret_cast`
**Classification:** Pointer Concept
**Environment:** Any `C++` compiler
**Path Type:** N/A
**Tags:** keyword
---

---

### What It Is

A C++ cast operator that converts a value between certain low-level representations without changing the underlying bit pattern.

### What It Does

Allows a pointer to be represented as an integer value, or one pointer type to be represented as another pointer type.

For example, a pointer containing a memory address can be represented as `uintptr_t`, allowing that address to be stored and compared as an integer.

### How to Use

Write the destination type inside `reinterpret_cast<>` and place the value being converted inside the parentheses.

### Requirements

Pointer // Provides the address to be represented.

`uintptr_t` // Provides an unsigned integer representation capable of holding a converted pointer value when supported.

### Representation

```cpp
#include <cstdint>

int value = 42;

int *pointer = &value;

uintptr_t address =
    reinterpret_cast<uintptr_t>(pointer);

```

Here:

```text
pointer
   │
   │ contains
   ▼
memory address
   │
   │ reinterpret_cast
   ▼
uintptr_t
   │
   ▼
integer representation of that address

```

