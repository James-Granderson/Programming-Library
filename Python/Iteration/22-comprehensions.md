# `Comprehensions`

**Concept:** Collection Construction
**Action:** Construct
**Object:** `Collections`
**Classification:** Expression Form
**Environment:** Python Runtime
**Path Type:** Direct
**Tags:** list, set, dict comprehensions

---

### What It Is

Comprehensions construct collections from iterables using expressions and optional filters.

### What It Does

They compress common transformation and filtering loops.

### How to Use

Use them when the logic remains readable.

### Requirements

The source must be iterable.

### Representation

```python
squares = [x*x for x in range(10) if x % 2 == 0]
|If a comprehension becomes a miniature program, use a normal loop.
```
