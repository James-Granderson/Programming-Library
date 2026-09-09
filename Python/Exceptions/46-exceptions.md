# `Exceptions`

**Concept:** Exceptional Control Flow
**Action:** Signal
**Object:** `Failure`
**Classification:** Control-Flow Mechanism
**Environment:** Python Runtime
**Path Type:** Direct
**Tags:** exceptions, try, except, raise, finally

---

### What It Is

An exception is an object representing an exceptional condition that interrupts ordinary control flow.

### What It Does

It lets failures propagate until code capable of handling them catches the appropriate exception.

### How to Use

Use raise to signal, try/except to handle, else for successful completion, and finally for cleanup.

### Requirements

Catch exceptions narrowly enough to avoid hiding unrelated failures.

### Representation

```python
try:
    value = int(text)
except ValueError:
    value = 0
|Exceptions are control-flow objects. They are not merely printed error messages.
```
