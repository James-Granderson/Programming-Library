# `References and Aliasing`

**Concept:** Reference Semantics
**Action:** Share
**Object:** `Objects`
**Classification:** Aliasing
**Environment:** Python Runtime
**Path Type:** Direct
**Tags:** references, aliasing, shared state

---

### What It Is

Multiple names can refer to one object. This is aliasing.

### What It Does

It explains why assignment does not inherently duplicate mutable data.

### How to Use

When independence is required, explicitly copy at the needed depth.

### Requirements

The object must support the operation.

### Representation

```python
a = []
b = a
b.append(1)
print(a)
|Shared state is powerful but must be intentional.
```
