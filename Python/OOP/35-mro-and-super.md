# `MRO and super`

**Concept:** Method Resolution
**Action:** Resolve
**Object:** `Methods`
**Classification:** MRO
**Environment:** Python Object Model
**Path Type:** Direct
**Tags:** MRO, super, multiple inheritance

---

### What It Is

The method resolution order is the deterministic sequence Python uses when searching classes. super follows that cooperative chain.

### What It Does

It makes multiple inheritance and cooperative calls predictable.

### How to Use

Inspect Class.mro or __mro__; use super in cooperative designs.

### Requirements

Multiple inheritance requires a consistent MRO.

### Representation

```python
print(Dog.mro())
return super().speak()
|super means next in the MRO, which is why cooperative multiple inheritance works.
```
