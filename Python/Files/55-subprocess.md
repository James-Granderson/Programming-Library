# `Subprocesses`

**Concept:** Process Execution
**Action:** Invoke
**Object:** `External Programs`
**Classification:** Operating System Interface
**Environment:** Python Standard Library
**Path Type:** Direct
**Tags:** subprocess, commands, processes, pipes

---

### What It Is

The subprocess module starts and communicates with external programs.

### What It Does

It connects Python programs to the operating system process model.

### How to Use

Prefer subprocess.run for ordinary commands and explicitly manage output and errors.

### Requirements

The executable and arguments must be valid for the environment.

### Representation

```python
import subprocess
result = subprocess.run(["echo", "hello"], capture_output=True, text=True)
|This is where Python meets the terminal and operating system directly.
```
