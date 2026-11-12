# `Cpu Core`

**Concept:** Cpu
**Action:** Execute
**Object:** `Cpu Core`
**Classification:** Cpu
**Environment:** Computer
**Path Type:** N/A
**Tags:** cpu-core, cpu, hardware

---

### What It Is

A CPU core is an execution engine capable of fetching and executing an instruction stream. A core may contain front-end, execution, memory, and control structures; a processor package can contain one or multiple cores.

### What It Does

The core runs instructions using its architecture-specific pipeline and accesses memory through caches and system interfaces. Core count does not equal simultaneous instruction throughput because dependencies and shared resources matter.

### How to Use

1. Identify the core architecture and supported instruction set.
2. Trace instruction flow through fetch, execution, and memory access.
3. Consider per-core resources and shared package resources when evaluating workload performance.

### Requirements

A core design, clock and power delivery, memory access paths, and compatible software are required. Core features vary by implementation.

### Representation

```text
instruction stream → [ core: front end | execution | load/store ] → results
```
