# `std::move`

**Concept:** `C++`
**Action:** Reference
**Object:** `std::move`
**Classification:** Function
**Environment:** Any `C++11` or later compiler
**Path Type:** N/A
**Tags:** function
---

---

### What It Is

A standard library function that converts an expression into an rvalue reference so that move operations can be selected.

### What It Does

Enables resources to be transferred instead of copied when the object's type provides move semantics.

### How to Use

Include `<utility>` and pass the object to `std::move`.

### Requirements

`<utility>`  // Declares `std::move`.

### Representation

```cpp
#cpp
#include <memory>

int main() {
    std::unique_ptr<int> number = std::make_unique<int>(42); // number now owns the object
    std::unique_ptr<int> other = std::move(number); // number transfers ownership to other 
}

```

