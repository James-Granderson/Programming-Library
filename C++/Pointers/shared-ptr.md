# `std::shared_ptr`

**Concept:** `C++`
**Action:** Create
**Object:** `std::shared_ptr`
**Classification:** Pointer Concept
**Environment:** Any `C++11` or later compiler
**Path Type:** N/A
**Tags:** keyword
---

---

### What It Is

A smart pointer that provides shared ownership of an object.

### What It Does

Allows multiple `std::shared_ptr` objects to own the same object. The object remains alive while owning `std::shared_ptr` instances remain. All owning `shared_ptr` copies must be gone before the managed object is destroyed.

### How to Use

Include `<memory>` and create the object with `std::make_shared`.

### Requirements

`<memory>`  // Declares `std::shared_ptr` and `std::make_shared`.

### Representation

```cpp
#include <memory>

int main() {
    std::shared_ptr<int> first = std::make_shared<int>(42);
    std::shared_ptr<int> second = first;
}
```

