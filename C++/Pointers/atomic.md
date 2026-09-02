# `std::atomic`
**Concept:** `C++`
**Action:** Create
**Object:** `std::atomic`
**Classification:** Class Construct
**Environment:** Any `C++11` or later compiler
**Path Type:** N/A
**Tags:** keyword

---

### What It Is

A C++ standard library class template for storing a value that may be accessed by multiple threads.

### What It Does

Prevents concurrent threads from interfering with supported operations on the same stored value.

Without atomic access, an operation such as:

```text
read → modify → write

```

can overlap with the same operation in another thread. Both threads can read the same old value and then write their results, causing an update to be lost.

`std::atomic` provides operations that coordinate access to the stored value so that these operations cannot collide in that way.

### How to Use

Include `<atomic>` and declare the shared value as `std::atomic<T>`. Use its atomic operations instead of separately reading, modifying, and writing the value.

### Requirements

`<atomic>` // Declares `std::atomic`.

### Representation

```cpp
#include <atomic>

std::atomic<int> count{0};

count.fetch_add(1);

```

