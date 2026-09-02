# `__name__ and __main__`

**Concept:** Execution Context
**Action:** Select
**Object:** `Module State`
**Classification:** Entry Point
**Environment:** Python Runtime
**Path Type:** Direct
**Tags:** __name__, __main__, scripts, entry point

---

### What It Is

A module has a __name__ value. A file executed as the program entry point normally has __name__ equal to __main__.

### What It Does

It lets reusable definitions and script behavior coexist.

### How to Use

Put entry-point behavior behind if __name__ == "__main__".

### Requirements

Execution mode determines the module name.

### Representation

```python
if __name__ == "__main__":
    main()
|This is one of the simplest examples of a program behaving differently based on execution context.
```
