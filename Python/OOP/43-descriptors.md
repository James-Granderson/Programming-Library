# `Descriptors`

**Concept:** Attribute Machinery
**Action:** Control
**Object:** `Attribute Access`
**Classification:** Descriptor Protocol
**Environment:** Python Object Model
**Path Type:** Direct
**Tags:** descriptor, __get__, __set__, __delete__

---

### What It Is

A descriptor is an object whose special methods participate in another object's attribute lookup.

### What It Does

Descriptors power properties, bound methods, and many framework abstractions.

### How to Use

Implement __get__, __set__, or __delete__, then place the descriptor on a class.

### Requirements

Attribute lookup precedence determines which object handles the access.

### Representation

```python
class Field:
    def __get__(self, obj, owner):
        ...
|Descriptors are one of Python's deepest explanations for why attribute access is so powerful.
```
