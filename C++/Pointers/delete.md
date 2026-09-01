# `delete`

**Concept:** `C++`
**Action:** Deallocate
**Object:** `delete`
**Classification:** Pointer Concept
**Environment:** Any `C++` compiler
**Path Type:** N/A
**Tags:** keyword
---

---

### What It Is

A C++ operator that destroys a dynamically allocated object created with `new`.

### What It Does

Ends the lifetime of a dynamically allocated object and releases the memory associated with it.

For a single object, use `delete`. For an array created with `new[]`, use `delete[]`.

The allocation and deallocation forms must correspond:

```text
new     → delete
new[]   → delete[]

```

### How to Use

Apply `delete` to a pointer returned by `new`. Apply `delete[]` to a pointer returned by `new[]`.

### Requirements

Pointer // Refers to the dynamically allocated object or array.

### Representation

```cpp
int *number = new int(42);
delete number;

int *numbers = new int[10];
delete[] numbers;

```

