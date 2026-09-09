# `functools and itertools`

**Concept:** Functional Utilities
**Action:** Compose
**Object:** `Callables and Iterators`
**Classification:** Standard Library
**Environment:** Python Standard Library
**Path Type:** Direct
**Tags:** functools, itertools, partial, reduce, chain, product

---

### What It Is

functools provides callable tools; itertools provides iterator-building blocks.

### What It Does

They allow programs to compose behavior and traversal without rebuilding mechanisms manually.

### How to Use

Use partial, wraps, caching, chain, product, and related tools when they clarify the design.

### Requirements

The callable and iterator contracts must match the utility.

### Representation

```python
from functools import partial
from itertools import chain
|The standard library often packages general patterns that you could implement yourself but should not have to.
```
