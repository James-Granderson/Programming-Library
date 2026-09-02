# `Scope and LEGB`

**Concept:** Name Resolution
**Action:** Resolve
**Object:** `Names`
**Classification:** Scope
**Environment:** Python Runtime
**Path Type:** Direct
**Tags:** scope, LEGB, local, enclosing, global, builtins

---

### What It Is

Python resolves bare names through Local, Enclosing, Global, and Built-in namespaces.

### What It Does

It determines which object a name refers to at a point in execution.

### How to Use

Use local bindings by default; use global and nonlocal only for deliberate rebinding.

### Requirements

The name must resolve somewhere in the search chain.

### Representation

```python
x = "global"
def f():
    x = "local"
    return x
|Scope is a rule about where a binding is found, not a physical place in memory.
```
