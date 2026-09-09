# `Hashability`

**Concept:** Hash Contract
**Action:** Hash
**Object:** `Values`
**Classification:** Hashable Object
**Environment:** Python Runtime
**Path Type:** Direct
**Tags:** hash, hashability, dict keys, set members

---

### What It Is

A hashable object has a stable hash value and equality semantics compatible with hash-based collections.

### What It Does

It lets objects serve as dictionary keys and set members.

### How to Use

Use hashable values as keys and preserve their hash/equality contract.

### Requirements

The hash/equality relationship must remain consistent.

### Representation

```python
lookup = {"user_id": 42}
print(hash("user_id"))
|Hashing is part of the contract between an object and a hash table.
```
