# `Namespaces`

**Concept:** Name Organization
**Action:** Map
**Object:** `Names to Objects`
**Classification:** Mapping
**Environment:** Python Runtime
**Path Type:** Direct
**Tags:** namespaces, globals, locals, attributes

---

### What It Is

A namespace is a mapping from names to objects. Modules, functions, classes, and instances expose different namespaces.

### What It Does

Namespaces organize names and make lookup possible.

### How to Use

Inspect globals, locals, and attributes when debugging or learning.

### Requirements

Namespace behavior depends on context.

### Representation

```python
globals()["answer"] = 42
print(answer)
|The namespace model is one of the cleanest ways to reason about Python names.
```
