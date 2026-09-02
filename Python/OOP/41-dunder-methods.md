# `Dunder Methods`

**Concept:** Object Protocol
**Action:** Define
**Object:** `Special Operations`
**Classification:** Special Method
**Environment:** Python Object Model
**Path Type:** Direct
**Tags:** dunder, special methods, protocols, operator overloading

---

### What It Is

Special methods such as __len__, __iter__, and __add__ connect objects to Python syntax and built-ins.

### What It Does

They let custom objects participate in language protocols.

### How to Use

Implement the special method corresponding to the protocol you want to support.

### Requirements

The method must obey the protocol's expected semantics.

### Representation

```python
class Box:
    def __len__(self):
        return 3
|Dunder methods are interfaces between your objects and the language itself.
```
