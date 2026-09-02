# `Abstract Base Classes`

**Concept:** Explicit Contract
**Action:** Constrain
**Object:** `Implementations`
**Classification:** Nominal Interface
**Environment:** Python Standard Library
**Path Type:** Direct
**Tags:** ABC, abstractmethod, interface, contract

---

### What It Is

An abstract base class defines an explicit inheritance-based contract and can prevent incomplete implementations from being instantiated.

### What It Does

It provides nominal interface checking and shared abstract or concrete behavior.

### How to Use

Use ABC and abstractmethod when an explicit class hierarchy is useful.

### Requirements

Concrete subclasses must implement required abstract methods.

### Representation

```python
from abc import ABC, abstractmethod

class Shape(ABC):
    @abstractmethod
    def area(self): ...
|ABCs are stronger nominal contracts than ordinary duck typing.
```
