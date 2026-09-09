# `Strings`

**Concept:** Text
**Action:** Represent
**Object:** `Characters`
**Classification:** Immutable Sequence
**Environment:** Python Runtime
**Path Type:** Direct
**Tags:** str, strings, text, unicode, encoding

---

### What It Is

A string is an immutable sequence of Unicode code points.

### What It Does

It represents text and supports searching, slicing, formatting, splitting, and joining.

### How to Use

Use string methods and f-strings; distinguish text from encoded bytes.

### Requirements

Encoding matters at external I/O boundaries.

### Representation

```python
name = "James"
print(f"Hello, {name}")
|Text and bytes are different domains even when they meet at an encoding boundary.
```
