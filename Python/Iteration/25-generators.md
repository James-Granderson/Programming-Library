# `Generators`

**Concept:** Lazy Iteration
**Action:** Yield
**Object:** `Values`
**Classification:** Generator
**Environment:** Python Runtime
**Path Type:** Direct
**Tags:** generator, yield, lazy, streaming

---

### What It Is

A generator function pauses at yield and resumes when another value is requested.

### What It Does

It enables lazy production without materializing all values at once.

### How to Use

Write generator functions with yield and consume them through iteration.

### Requirements

Execution is driven by requests for another value.

### Representation

```python
def count_up(n):
    for i in range(n):
        yield i
|Generators are especially useful for streams, pipelines, and large data.
```
