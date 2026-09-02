# `Dataclasses`

**Concept:** Data-Oriented Classes
**Action:** Generate
**Object:** `Fields and Methods`
**Classification:** Class Utility
**Environment:** Python Standard Library
**Path Type:** Direct
**Tags:** dataclass, fields, repr, equality

---

### What It Is

A dataclass decorator generates common methods from declared fields.

### What It Does

It reduces boilerplate for data-oriented classes.

### How to Use

Use @dataclass with annotated fields and configure generated behavior when necessary.

### Requirements

Generated behavior depends on decorator options and fields.

### Representation

```python
from dataclasses import dataclass

@dataclass
class Point:
    x: int
    y: int
|Dataclasses are convenience built on top of ordinary classes, annotations, and generated methods.
```
