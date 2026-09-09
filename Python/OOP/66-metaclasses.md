# `Metaclasses`

**Concept:** Class Construction
**Action:** Construct
**Object:** `Classes`
**Classification:** Class Factory
**Environment:** Python Object Model
**Path Type:** Direct
**Tags:** metaclass, type, class creation, metaprogramming

---

### What It Is

A metaclass is the type of a class object and can customize class creation.

### What It Does

It provides hooks for advanced frameworks and metaprogramming.

### How to Use

Use metaclasses only when class creation itself needs customization.

### Requirements

The metaclass hierarchy and construction protocol must remain coherent.

### Representation

```python
class Meta(type):
    pass

class Model(metaclass=Meta):
    pass
|If a decorator, descriptor, or ordinary class design solves the problem, prefer it over a metaclass.
```
