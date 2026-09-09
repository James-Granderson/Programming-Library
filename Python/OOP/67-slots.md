# `__slots__`

**Concept:** Instance Layout
**Action:** Constrain
**Object:** `Instance Attributes`
**Classification:** Memory Optimization
**Environment:** Python Object Model
**Path Type:** Direct
**Tags:** __slots__, attributes, memory, layout

---

### What It Is

__slots__ can declare a fixed set of instance attributes and may prevent the normal per-instance __dict__.

### What It Does

It can reduce per-instance overhead and constrain attribute creation.

### How to Use

Declare __slots__ when the layout constraint is useful and understand inheritance implications.

### Requirements

Slot behavior interacts with inheritance and descriptors.

### Representation

```python
class Point:
    __slots__ = ("x", "y")
|Optimization is a consequence; the more fundamental concept is instance layout.
```
