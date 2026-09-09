# `Assertions`

**Concept:** Invariant Checking
**Action:** Assert
**Object:** `Conditions`
**Classification:** Runtime Check
**Environment:** Python Runtime
**Path Type:** Direct
**Tags:** assert, invariants, debugging

---

### What It Is

An assertion states that a programmer assumption should be true at a point in execution.

### What It Does

It documents and checks internal invariants.

### How to Use

Use assertions for programmer assumptions, not validation that must always execute.

### Requirements

Assertions may be disabled with optimization.

### Representation

```python
assert total >= 0, "total cannot be negative"
|Assertions are strongest when they expose an invariant, not when they duplicate ordinary branching.
```
