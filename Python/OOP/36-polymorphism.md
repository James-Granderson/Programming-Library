# `Polymorphism`

**Concept:** Behavioral Substitutability
**Action:** Dispatch
**Object:** `Objects`
**Classification:** Polymorphism
**Environment:** Python Object Model
**Path Type:** Direct
**Tags:** polymorphism, overriding, dispatch, interfaces

---

### What It Is

Polymorphism means a consumer can depend on an operation while different concrete objects provide different implementations.

### What It Does

It lets one algorithm operate across different types without enumerating every concrete class.

### How to Use

Design consumers around behavior and let runtime dispatch reach the implementation supplied by the object.

### Requirements

The supplied object must satisfy the behavior the consumer actually uses.

### Representation

```python
def render(shape):
    return shape.render()
|Python's polymorphism is often behavioral rather than inheritance-centered.
```
