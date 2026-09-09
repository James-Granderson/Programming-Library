# `Closures`

**Concept:** Lexical State
**Action:** Capture
**Object:** `Enclosing Names`
**Classification:** Function Object
**Environment:** Python Runtime
**Path Type:** Direct
**Tags:** closures, free variables, nonlocal

---

### What It Is

A closure is a function that retains access to names from an enclosing scope after that scope returns.

### What It Does

It lets behavior carry state without necessarily using a class.

### How to Use

Create an inner function that references an enclosing binding; use nonlocal for deliberate rebinding.

### Requirements

The captured binding must remain in the closure environment.

### Representation

```python
def make_adder(n):
    def add(x):
        return x + n
    return add
|Closures are a direct consequence of functions being objects plus lexical scope.
```
