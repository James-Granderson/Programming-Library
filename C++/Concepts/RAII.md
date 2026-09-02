# `RAII`
**Concept:** `C++`
**Action:** Create
**Object:** RAII
**Classification:** Pointer Concept
**Environment:** Any `C++11` or later compiler
**Path Type:** N/A
**Tags:** keyword

---

### What It Is

A C++ programming pattern where an object's lifetime controls the lifetime of a resource it owns.

### What It Does

Automatically releases a resource when the object responsible for it is destroyed.

Instead of manually releasing a resource, the program ties the resource to an object's lifetime.

### How to Use

Create an object that acquires the resource when it is initialized. When the object leaves its lifetime, its destructor releases the resource.

### Requirements

Object  // Owns or manages the resource.

Destructor  // Releases the resource when the object is destroyed.

### Representation

```cpp
#include <memory>

int main() {
    {
        std::unique_ptr<int> number =
            std::make_unique<int>(42); // object acquires ownership
    } // number dies → owned object is automatically destroyed
}
```

### Notes

The basic RAII relationship is:

```text
object created
      ↓
resource acquired
      ↓
resource used
      ↓
object destroyed
      ↓
resource released
```
