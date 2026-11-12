# `Block`

**Concept:** Architecture
**Action:** Integrate
**Object:** `Block`
**Classification:** Architecture
**Environment:** Computer
**Path Type:** N/A
**Tags:** block, architecture, hardware

---

### What It Is

A block is a functional unit or a bounded group of components in a hardware design. The term is contextual: a block diagram may use it for a subsystem, while a memory system uses it for a fixed-size transfer or allocation unit.

### What It Does

A block groups circuitry and interfaces so a larger design can be reasoned about in parts. Its inputs, outputs, and contract define how it interacts with neighboring blocks; the name alone does not specify a particular circuit.

### How to Use

1. Read the design context to determine whether ‘block’ means a subsystem or a fixed-size data unit.
2. Identify its documented inputs, outputs, and neighboring interfaces.
3. Trace an example transaction across the boundary and consult the detailed specification for implementation behavior.

### Requirements

A defined scope and interface are needed to make the word ‘block’ unambiguous. A block diagram is a documentation view, not a component.

### Representation

```text
Producer ── interface/data ──► [ Functional block ] ──► Consumer
```
