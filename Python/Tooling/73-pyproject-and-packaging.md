# `pyproject.toml and Packaging`

**Concept:** Project Packaging
**Action:** Declare
**Object:** `Project Metadata`
**Classification:** Packaging
**Environment:** Python Ecosystem
**Path Type:** Direct
**Tags:** pyproject.toml, packaging, dependencies, build systems

---

### What It Is

pyproject.toml is a standard project configuration location for Python metadata and tool configuration.

### What It Does

It gives packaging and development tools a common project configuration boundary.

### How to Use

Use it to declare project metadata, dependencies, and tool configuration according to the chosen build backend.

### Requirements

Exact fields depend on the build backend and tools.

### Representation

```python
[project]
name = "example"
version = "0.1.0"
|Packaging is the act of defining how code becomes a distributable dependency or application.
```
