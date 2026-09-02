# `Parameters and Arguments`

**Concept:** Function Interface
**Action:** Receive
**Object:** `Arguments`
**Classification:** Call Interface
**Environment:** Python Runtime
**Path Type:** Direct
**Tags:** parameters, positional, keyword, args, kwargs

---

### What It Is

Parameters describe a function interface; arguments are concrete values supplied by the caller.

### What It Does

They control how values enter a function.

### How to Use

Use positional-only /, keyword-only *, *args, and **kwargs deliberately.

### Requirements

Calls must conform to the signature.

### Representation

```python
def connect(host, /, port=443, *, timeout=5):
    ...
|An interface is a contract between caller and function.
```
