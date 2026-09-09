# `Logging`

**Concept:** Observability
**Action:** Record
**Object:** `Program Events`
**Classification:** Diagnostics
**Environment:** Python Standard Library
**Path Type:** Direct
**Tags:** logging, levels, handlers, formatters

---

### What It Is

Logging records program events with severity and metadata rather than relying only on print.

### What It Does

It makes runtime behavior observable in a controlled way.

### How to Use

Create loggers, choose levels, and route records through handlers.

### Requirements

Configuration should match the environment.

### Representation

```python
import logging
log = logging.getLogger(__name__)
log.info("started")
|Observability turns hidden runtime behavior into evidence.
```
