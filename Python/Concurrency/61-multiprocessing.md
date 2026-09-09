# `Multiprocessing`

**Concept:** Process Parallelism
**Action:** Parallelize
**Object:** `Processes`
**Classification:** Concurrency
**Environment:** Python Runtime
**Path Type:** Direct
**Tags:** multiprocessing, processes, CPU-bound, parallelism

---

### What It Is

Multiprocessing runs work in separate processes with separate interpreter state.

### What It Does

It can provide process-level CPU parallelism and isolation.

### How to Use

Use multiprocessing or ProcessPoolExecutor for suitable CPU-bound work.

### Requirements

Values crossing process boundaries must be transferable.

### Representation

```python
from concurrent.futures import ProcessPoolExecutor
|Separate processes change the state-sharing model as well as the execution model.
```
