# `Iterators`

**Concept:** Iteration State
**Action:** Yield
**Object:** `Next Element`
**Classification:** Protocol
**Environment:** Python Runtime
**Path Type:** Direct
**Tags:** iterator, __iter__, __next__, StopIteration

---

### What It Is

An iterator represents an ongoing traversal and supplies one next value at a time.

### What It Does

It provides stateful consumption of a sequence or stream.

### How to Use

Use iter to obtain an iterator and next to advance it.

### Requirements

The iterator must implement the iterator protocol.

### Representation

```python
it = iter([10, 20])
print(next(it))
|Iteration is a protocol, not a requirement that the data structure be a list.
```
