# `Virtual Environments and pip`

**Concept:** Environment Management
**Action:** Isolate
**Object:** `Python Installation`
**Classification:** Environment
**Environment:** Python Tooling
**Path Type:** Direct
**Tags:** venv, pip, packages, dependencies

---

### What It Is

A virtual environment isolates a project's Python environment; pip installs packages into an environment.

### What It Does

They prevent unrelated projects from fighting over dependencies and versions.

### How to Use

Create with python -m venv .venv and install with python -m pip install package.

### Requirements

Python and pip must be available.

### Representation

```python
python -m venv .venv
python -m pip install requests
|Environment management is part of programming because the program depends on more than its source code.
```
