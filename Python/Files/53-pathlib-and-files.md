# `Pathlib and Files`

**Concept:** Filesystem I/O
**Action:** Access
**Object:** `Paths and Files`
**Classification:** I/O Interface
**Environment:** Python Standard Library
**Path Type:** Direct
**Tags:** pathlib, Path, files, filesystem

---

### What It Is

pathlib provides object-oriented filesystem paths, while file objects provide streams for reading and writing.

### What It Does

It makes filesystem operations explicit and composable.

### How to Use

Use Path for paths and open or Path.open for file access.

### Requirements

Paths and permissions must permit the operation.

### Representation

```python
from pathlib import Path
text = Path("notes.txt").read_text(encoding="utf-8")
|Treat filesystem paths as data with operations, not just arbitrary strings.
```
