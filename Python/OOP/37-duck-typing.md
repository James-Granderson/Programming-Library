# `Duck Typing`

**Concept:** Behavioral Interface
**Action:** Use
**Object:** `Behavior`
**Classification:** Structural Polymorphism
**Environment:** Python Runtime
**Path Type:** Direct
**Tags:** duck typing, behavior, polymorphism

---

### What It Is

Duck typing asks whether an object supports the operation needed by the consumer rather than whether it belongs to a particular hierarchy.

### What It Does

It reduces coupling and makes compatible objects usable without registration.

### How to Use

Write code against required behavior and allow compatible objects to work.

### Requirements

The object must actually provide compatible behavior at runtime.

### Representation

```python
def save(writer):
    writer.write("hello")
|The phrase comes from the idea that if it walks and quacks like a duck, the relevant question is behavior.
```
