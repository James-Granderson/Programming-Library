# `Generator Expressions`

**Concept:** Lazy Construction
**Action:** Generate
**Object:** `Values`
**Classification:** Generator Expression
**Environment:** Python Runtime
**Path Type:** Direct
**Tags:** generator expression, lazy evaluation

---

### What It Is

A generator expression is the lazy counterpart to a collection comprehension.

### What It Does

It produces values on demand.

### How to Use

Use parentheses around the expression and feed it to a consumer.

### Requirements

The source must be iterable.

### Representation

```python
total = sum(x*x for x in range(100))
|Lazy versus eager construction is a recurring systems tradeoff.
```
