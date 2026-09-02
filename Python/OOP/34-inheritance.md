# `Inheritance`

**Concept:** Subtype Relationship
**Action:** Extend
**Object:** `Base Type`
**Classification:** Inheritance
**Environment:** Python Object Model
**Path Type:** Direct
**Tags:** inheritance, subclass, overriding

---

### What It Is

Inheritance lets a class derive behavior from one or more base classes.

### What It Does

It enables reuse and specialization but introduces coupling and method-resolution complexity.

### How to Use

Use subclassing when the subtype genuinely preserves the base contract.

### Requirements

The base classes must form a valid MRO.

### Representation

```python
class Dog(Animal):
    def speak(self):
        return "woof"
|Inheritance is one tool for reuse, not the definition of reuse itself.
```
