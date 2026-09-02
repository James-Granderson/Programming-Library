# `Protocol Typing`

**Concept:** Structural Contract
**Action:** Describe
**Object:** `Behavior`
**Classification:** Static Structural Type
**Environment:** Python Typing System
**Path Type:** Direct
**Tags:** Protocol, structural typing, static polymorphism

---

### What It Is

Protocols allow static type checkers to recognize compatible behavior without nominal inheritance.

### What It Does

They connect duck typing with static analysis.

### How to Use

Define a protocol for the operations a consumer needs and type against it.

### Requirements

Implementations must satisfy it structurally.

### Representation

```python
from typing import Protocol
class Reader(Protocol):
    def read(self) -> str: ...
|This is polymorphism formalized for static analysis.
```
