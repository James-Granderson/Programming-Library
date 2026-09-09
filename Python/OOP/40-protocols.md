# `Protocols`

**Concept:** Structural Contract
**Action:** Specify
**Object:** `Behavior`
**Classification:** Structural Type
**Environment:** Python Typing System
**Path Type:** Direct
**Tags:** Protocol, structural typing, interfaces

---

### What It Is

A typing.Protocol describes required behavior without requiring implementation classes to inherit from it.

### What It Does

It connects Python's behavioral style with static type checking.

### How to Use

Define the operations a consumer needs and type the consumer against the protocol.

### Requirements

Implementations must satisfy the protocol structurally for the type checker.

### Representation

```python
from typing import Protocol

class Writer(Protocol):
    def write(self, text: str) -> None: ...
|Protocols are particularly useful when the real abstraction is behavior rather than ancestry.
```
