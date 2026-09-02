# `Copying and Deep Copying`

**Concept:** Copy Semantics
**Action:** Duplicate
**Object:** `Objects`
**Classification:** Copy Operation
**Environment:** Python Standard Library
**Path Type:** Direct
**Tags:** copy, shallow copy, deep copy, nested state

---

### What It Is

A shallow copy creates a new outer object while retaining nested references; deep copy recursively copies supported nested objects.

### What It Does

It controls whether structures share nested state.

### How to Use

Use copy.copy for shallow copying and copy.deepcopy only when recursive independence is required.

### Requirements

Deep copying can be expensive or inappropriate.

### Representation

```python
import copy
b = copy.copy(a)
c = copy.deepcopy(a)
|Copying is a semantic decision about independence and shared state.
```
