# `First-Class Functions`

**Concept:** Function Objects
**Action:** Pass
**Object:** `Functions`
**Classification:** First-Class Object
**Environment:** Python Runtime
**Path Type:** Direct
**Tags:** first-class functions, callbacks, higher-order

---

### What It Is

Functions are ordinary objects and can be assigned, passed, returned, and stored.

### What It Does

This enables callbacks, decorators, factories, and functional patterns.

### How to Use

Pass a function by name when another function expects a callable.

### Requirements

The receiver must invoke it with compatible arguments.

### Representation

```python
def apply(fn, value):
    return fn(value)
|Once behavior is an object, program structure becomes much more flexible.
```
