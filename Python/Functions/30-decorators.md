# `Decorators`

**Concept:** Higher-Order Behavior
**Action:** Wrap
**Object:** `Callables`
**Classification:** Decorator
**Environment:** Python Runtime
**Path Type:** Direct
**Tags:** decorators, wrappers, functools, wraps

---

### What It Is

A decorator is a callable that receives a callable and returns a callable, often adding behavior around it.

### What It Does

It attaches cross-cutting behavior such as logging, timing, caching, or registration.

### How to Use

Write a wrapper, preserve metadata with functools.wraps, and apply it with @decorator.

### Requirements

The wrapper must preserve or intentionally change the callable contract.

### Representation

```python
from functools import wraps

def logged(fn):
    @wraps(fn)
    def wrapper(*args, **kwargs):
        print(fn.__name__)
        return fn(*args, **kwargs)
    return wrapper
|A decorator is not magic syntax; @name is a compact way to apply a callable transformation.
```
