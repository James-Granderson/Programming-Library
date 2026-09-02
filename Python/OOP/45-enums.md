# `Enums`

**Concept:** Finite Symbolic Choices
**Action:** Name
**Object:** `Choices`
**Classification:** Enumeration
**Environment:** Python Standard Library
**Path Type:** Direct
**Tags:** Enum, IntEnum, symbolic constants

---

### What It Is

An enum defines named members representing a finite set of choices.

### What It Does

It replaces scattered magic values with explicit symbolic members.

### How to Use

Subclass Enum and define members.

### Requirements

Choose an enum class appropriate to the semantics of the values.

### Representation

```python
from enum import Enum

class Status(Enum):
    READY = "ready"
|Names make finite domains explicit.
```
