# `Assignment and Unpacking`

**Concept:** Binding
**Action:** Bind
**Object:** `Names and Objects`
**Classification:** Assignment
**Environment:** Python Runtime
**Path Type:** Direct
**Tags:** assignment, unpacking, augmented assignment

---

### What It Is

Assignment changes bindings. Unpacking assigns multiple targets from an iterable.

### What It Does

It provides the basic mechanism for moving references into namespaces.

### How to Use

Use ordinary assignment, tuple unpacking, starred unpacking, and augmented assignment.

### Requirements

Targets and produced values must have compatible structure.

### Representation

```python
first, *middle, last = range(5)
|Assignment is a binding operation; it is not automatically a copying operation.
```
