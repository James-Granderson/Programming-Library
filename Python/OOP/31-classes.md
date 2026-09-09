# `Classes`

**Concept:** Object Construction
**Action:** Define
**Object:** `Objects`
**Classification:** Class
**Environment:** Python Object Model
**Path Type:** Direct
**Tags:** class, type, methods, attributes

---

### What It Is

A class is itself an object and defines a type whose instances can carry state and behavior.

### What It Does

It provides a common structure for related objects and participates in inheritance and method lookup.

### How to Use

Define a class body and instantiate it by calling the class.

### Requirements

The class definition and bases must be valid.

### Representation

```python
class User:
    def __init__(self, name):
        self.name = name
|The class object is part of the runtime, not merely a compile-time template.
```
