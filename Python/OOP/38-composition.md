# `Composition`

**Concept:** Object Collaboration
**Action:** Contain
**Object:** `Objects`
**Classification:** Has-A Relationship
**Environment:** Python Object Model
**Path Type:** Direct
**Tags:** composition, delegation, has-a, dependency

---

### What It Is

Composition builds an object from collaborating objects instead of deriving every capability through inheritance.

### What It Does

It separates responsibilities and makes implementations replaceable.

### How to Use

Store collaborators as attributes and delegate work.

### Requirements

Collaborators must satisfy the expected behavior.

### Representation

```python
class Service:
    def __init__(self, repository):
        self.repository = repository
|Composition is often the cleanest answer when the relationship is has-a rather than is-a.
```
