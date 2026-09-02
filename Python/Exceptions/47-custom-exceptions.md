# `Custom Exceptions`

**Concept:** Domain Failure
**Action:** Define
**Object:** `Failure Type`
**Classification:** Exception Hierarchy
**Environment:** Python Runtime
**Path Type:** Direct
**Tags:** custom exceptions, hierarchy, domain errors

---

### What It Is

Custom exceptions are application-specific exception classes derived from suitable built-ins.

### What It Does

They give callers precise ways to distinguish domain failures.

### How to Use

Define descriptive exception classes and raise them at the domain boundary.

### Requirements

Choose a meaningful base exception.

### Representation

```python
class InvalidOrderError(ValueError):
    pass
|A good exception type communicates what went wrong at the abstraction level the caller understands.
```
