# `Mutability`

**Concept:** State
**Action:** Change
**Object:** `Objects`
**Classification:** Mutability
**Environment:** Python Runtime
**Path Type:** Direct
**Tags:** mutable, immutable, state

---

### What It Is

Mutability describes whether an object's state can be changed after creation.

### What It Does

It determines whether aliases can observe in-place state changes.

### How to Use

Know the mutability of objects you pass between functions and store in collections.

### Requirements

The type determines mutation semantics.

### Representation

```python
items = [1, 2]
items.append(3)
|Immutable does not mean an object cannot contain references to mutable objects.
```
