# `Instances and Attributes`

**Concept:** Object State
**Action:** Store
**Object:** `Instance Data`
**Classification:** Instance
**Environment:** Python Object Model
**Path Type:** Direct
**Tags:** instances, attributes, self, state

---

### What It Is

An instance is an object created from a class. Instance attributes normally hold state specific to that object.

### What It Does

It allows many objects to share behavior while carrying different state.

### How to Use

Use self.attribute inside instance methods and instance.attribute outside.

### Requirements

Attribute lookup determines where the value is found.

### Representation

```python
a = User("Alice")
b = User("Bob")
|Attribute access is a protocol with precedence rules, not simply a dictionary lookup.
```
