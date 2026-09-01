# `std::weak_ptr`

**Concept:** `C++`
**Action:** Reference
**Object:** `std::weak_ptr`
**Classification:** Pointer Concept
**Environment:** Any `C++11` or later compiler
**Path Type:** N/A
**Tags:** keyword
---

---

### What It Is

A smart pointer that observes an object managed by `std::shared_ptr` without owning it.

### What It Does

Observes a shared object without gaining ownership or extending its lifetime. 

### How to Use

Include `<memory>`, construct a `std::weak_ptr` from a `std::shared_ptr`, and use `lock()` when temporary shared ownership is required.

### Requirements

`<memory>`  // Declares `std::weak_ptr`.

### Representation

```cpp
#include <memory>

int main() {
    std::shared_ptr<int> owner = std::make_shared<int>(42);
    std::weak_ptr<int> observer = owner;

    if (auto locked = observer.lock()) // gaining temporary access via lock 
    {
    }
}
```

