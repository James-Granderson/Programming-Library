# `Properties`

**Concept:** Attribute Interface
**Action:** Control
**Object:** `Attribute Access`
**Classification:** Descriptor Interface
**Environment:** Python Object Model
**Path Type:** Direct
**Tags:** property, getter, setter, computed attributes

---

### What It Is

A property makes attribute syntax invoke methods behind the scenes.

### What It Does

It lets an API expose attribute-like access while validating or computing state.

### How to Use

Use @property and add a setter or deleter when needed.

### Requirements

Accessor behavior determines what reads and writes do.

### Representation

```python
class Account:
    @property
    def balance(self):
        return self._balance
|Properties are a user-friendly application of descriptor machinery.
```
