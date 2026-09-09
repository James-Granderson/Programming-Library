# `Types`

**Concept:** Classification
**Action:** Classify
**Object:** `Objects`
**Classification:** Type
**Environment:** Python Runtime
**Path Type:** Direct
**Tags:** types, dynamic typing, isinstance

---

### What It Is

A type describes an object and supplies or determines behavior. Python is dynamically typed: names do not have permanent declared types, but objects have types.

### What It Does

Types participate in construction, method lookup, protocols, and dispatch.

### How to Use

Use type() for direct inspection and isinstance() for type relationships.

### Requirements

The object must be available.

### Representation

```python
x = 10
print(type(x))
print(isinstance(x, int))
|Dynamic typing does not mean no types. It means type decisions are made at runtime.
```
