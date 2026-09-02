# `JSON, CSV, and Serialization`

**Concept:** External Data
**Action:** Serialize
**Object:** `Structured Data`
**Classification:** Data Representation
**Environment:** Python Standard Library
**Path Type:** Direct
**Tags:** json, csv, serialization, pickle

---

### What It Is

Serialization converts runtime data into a representation that can be stored or transmitted. JSON and CSV are interoperable; pickle is Python-specific and unsafe with untrusted input.

### What It Does

It creates a boundary between in-memory objects and external representations.

### How to Use

Use json for JSON, csv for tables, and trusted pickle only where appropriate.

### Requirements

Validate external data and never load untrusted pickle data.

### Representation

```python
import json
data = json.loads("{\\"x\\": 1}")
|Serialization is a representation boundary, not a magic preservation of arbitrary runtime meaning.
```
