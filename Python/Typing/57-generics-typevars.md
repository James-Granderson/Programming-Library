# `Generics and Type Variables`

**Concept:** Type Relationships
**Action:** Parameterize
**Object:** `Types`
**Classification:** Generic Type
**Environment:** Python Typing System
**Path Type:** Direct
**Tags:** generics, TypeVar, Generic, type parameters

---

### What It Is

Generics describe reusable code while preserving relationships between types.

### What It Does

They let static analysis express relationships that Any would erase.

### How to Use

Use type parameters when an input/output or container relationship matters.

### Requirements

The relationship must be expressed consistently.

### Representation

```python
from typing import TypeVar
T = TypeVar("T")
def identity(x: T) -> T: return x
|Generics are about preserving information through abstraction.
```
