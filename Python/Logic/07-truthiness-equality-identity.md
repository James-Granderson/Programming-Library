# `Truthiness, Equality, and Identity`

**Concept:** Boolean Semantics
**Action:** Compare
**Object:** `Objects`
**Classification:** Comparison Semantics
**Environment:** Python Runtime
**Path Type:** Direct
**Tags:** truthiness, equality, identity, comparisons

---

### What It Is

Truthiness determines boolean-context behavior. Equality compares values while identity asks whether references point to the same object.

### What It Does

It supports branching, comparison, and precise object reasoning.

### How to Use

Use == for equality and is for identity, especially x is None.

### Requirements

The object types determine comparison and truth behavior.

### Representation

```python
if value:
    print("truthy")
if value is None:
    print("missing")
|Never use is as a general replacement for ==.
```
