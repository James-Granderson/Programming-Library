# `Methods, Class Methods, and Static Methods`

**Concept:** Method Binding
**Action:** Dispatch
**Object:** `Objects or Classes`
**Classification:** Method Kind
**Environment:** Python Object Model
**Path Type:** Direct
**Tags:** methods, self, cls, classmethod, staticmethod

---

### What It Is

Instance methods receive an instance, class methods receive a class, and static methods receive neither automatically.

### What It Does

They express different relationships between callable behavior and its owning type.

### How to Use

Choose the method kind based on which state the behavior actually needs.

### Requirements

The decorator changes how attribute access binds the callable.

### Representation

```python
class Factory:
    @classmethod
    def make(cls):
        return cls()
|Understanding binding makes self and cls much less mysterious.
```
