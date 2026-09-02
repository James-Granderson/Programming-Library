# `Type Hints`

**Concept:** Static Description
**Action:** Describe
**Object:** `Expected Types`
**Classification:** Annotation
**Environment:** Python Typing System
**Path Type:** Direct
**Tags:** type hints, annotations, static analysis

---

### What It Is

Type hints describe intended types without making Python statically enforced at runtime.

### What It Does

They improve documentation, editor support, refactoring, and static analysis.

### How to Use

Annotate parameters, returns, attributes, and variables where useful.

### Requirements

A type checker is required for static enforcement.

### Representation

```python
def square(x: int) -> int:
    return x * x
|Typing adds a second layer of reasoning on top of Python's dynamic runtime.
```
