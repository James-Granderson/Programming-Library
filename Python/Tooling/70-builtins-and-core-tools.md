# `Built-ins and Core Tools`

**Concept:** Runtime Utilities
**Action:** Use
**Object:** `Built-in Functions`
**Classification:** Built-ins
**Environment:** Python Runtime
**Path Type:** Direct
**Tags:** len, range, enumerate, zip, map, filter, sorted, any, all

---

### What It Is

Python built-ins operate through common protocols rather than requiring every object to be a specific concrete class.

### What It Does

They provide reusable operations for iteration, inspection, construction, conversion, and control.

### How to Use

Learn the protocol each built-in expects: len for size, iter for iteration, next for advancement, enumerate for indexed traversal, zip for coordinated traversal.

### Requirements

Supplied objects must support the relevant protocol.

### Representation

```python
for i, value in enumerate(values):
    print(i, value)
|Built-ins are where Python's protocol-oriented design becomes visible in everyday code.
```
