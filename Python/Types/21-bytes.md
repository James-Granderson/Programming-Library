# `Bytes`

**Concept:** Binary Data
**Action:** Represent
**Object:** `Octets`
**Classification:** Immutable Binary Sequence
**Environment:** Python Runtime
**Path Type:** Direct
**Tags:** bytes, bytearray, binary, encoding

---

### What It Is

bytes represents immutable binary data as integers from 0 through 255.

### What It Does

It provides binary representation for I/O and encoded data.

### How to Use

Encode strings with encode and decode bytes with decode using the correct encoding.

### Requirements

The encoding must match the external representation.

### Representation

```python
data = "hello".encode("utf-8")
|A useful mental model is text <-> encoding <-> bytes.
```
