# `Heap`

**Concept:** Data Structures
**Action:** Store
**Object:** Heap
**Classification:** Data Structure
**Environment:** Language-independent
**Path Type:** N/A
**Tags:** data-structure

---

### What It Is

A complete tree that maintains a priority relationship between parents and children.

### What It Does

Makes the highest- or lowest-priority value available at the root.

### How to Use

Store the tree in an array and restore the heap property after insertion or removal.

### Representation

```
Array: [10, 8, 9, 4, 7, 5]

Parent(i) = (i - 1) / 2
Left(i)   = 2i + 1
Right(i)  = 2i + 2
```

