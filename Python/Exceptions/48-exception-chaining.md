# `Exception Chaining`

**Concept:** Failure Context
**Action:** Preserve
**Object:** `Exceptions`
**Classification:** Error Context
**Environment:** Python Runtime
**Path Type:** Direct
**Tags:** raise from, exception chaining, causality

---

### What It Is

Exception chaining preserves the relationship between a higher-level failure and its lower-level cause.

### What It Does

It retains causal information when translating implementation errors into domain errors.

### How to Use

Use raise NewError(...) from original when changing abstraction levels.

### Requirements

The original exception must be available.

### Representation

```python
try:
    load()
except OSError as exc:
    raise ConfigError("cannot load config") from exc
|Causality is information. Do not throw it away unnecessarily.
```
