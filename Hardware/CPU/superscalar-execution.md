# `Superscalar Execution`

**Concept:** Cpu
**Action:** Use
**Object:** `Superscalar Execution`
**Classification:** Cpu
**Environment:** Computer
**Path Type:** N/A
**Tags:** superscalar-execution, cpu, hardware

---

### What It Is

Superscalar execution allows a CPU to issue or execute multiple instructions in one clock cycle using multiple execution resources. The achievable issue rate depends on instruction independence and the processor's width and resources.

### What It Does

It increases potential instruction throughput for parallel instruction streams. Dependencies, branches, limited ports, and execution-unit availability can reduce actual work per cycle; it is not the same as multicore execution.

### How to Use

1. Find independent instructions available at the same time.
2. Map them to available issue slots and execution units.
3. Compare within-core parallel issue with running threads on separate cores.

### Requirements

Multiple execution resources, issue logic, and dependency handling are required. Width and supported operation combinations are implementation-specific.

### Representation

```text
one core, one cycle:  I1 → ALU 0
                     I2 → ALU 1
                     I3 waits if dependent
```
