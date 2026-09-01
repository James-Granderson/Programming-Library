# `std::unique_ptr`

**Concept:** `C++`
**Action:** Create
**Object:** `std::unique_ptr`
**Classification:** Pointer Concept
**Environment:** Any `C++11` or later compiler
**Path Type:** N/A
**Tags:** keyword
---

---

### What It Is

A smart pointer that provides exclusive ownership of an object.

### What It Does

Automatically manages the lifetime of its owned object. Ownership can be transferred to another `std::unique_ptr` with `std::move`.

### How to Use

Include `<memory>` and create the object with `std::make_unique`.

### Requirements

`<memory>`  // Declares `std::unique_ptr` and `std::make_unique`.

### Representation

```cpp
#cpp
#include <memory>

int main() {
    std::unique_ptr<int> number = std::make_unique<int>(42); // number now owns the object
    std::unique_ptr<int> other = std::move(number); // number transfers ownership to other 
}


```

