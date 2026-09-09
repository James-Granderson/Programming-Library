# `Iterables`

**Concept:** Iteration Protocol
**Action:** Produce
**Object:** `Elements`
**Classification:** Protocol
**Environment:** Python Runtime
**Path Type:** Direct
**Tags:** iterable, iteration, protocol, for loop

---

### What It Is

An iterable is an object from which Python can obtain an iterator, commonly through __iter__.

### What It Does

It gives for loops, comprehensions, and built-ins a common consumption interface.

### How to Use

Pass iterables to for, list, tuple, sum, any, all, and similar consumers.

### Requirements

The object must provide an iterable protocol.

### Representation

```python
for item in iterable:
    print(item)
|The consumer should not need to know how the iterable stores its values.
```
