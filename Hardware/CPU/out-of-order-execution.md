# `Out of Order Execution`

**Concept:** Cpu
**Action:** Use
**Object:** `Out of Order Execution`
**Classification:** Cpu
**Environment:** Computer
**Path Type:** N/A
**Tags:** out-of-order-execution, cpu, hardware

---

### What It Is

Out-of-order execution lets a CPU issue ready operations before older stalled operations when their dependencies permit. The processor tracks dependencies and typically retires completed instructions in architectural order to preserve program behavior.

### What It Does

It can use otherwise idle execution units while waiting for a cache miss or other delay. It does not mean the program's visible results are committed in arbitrary order; recovery handles exceptions and mispredictions.

### How to Use

1. Trace instruction dependencies and identify which operations are ready.
2. Observe a later independent operation executing while an earlier one waits.
3. Distinguish execution completion from in-order retirement.

### Requirements

A scheduling window, dependency tracking, execution resources, and a mechanism to preserve architectural state are required. Details vary by microarchitecture.

### Representation

```text
Program order: I1(wait) → I2(ready) → I3(ready)
Execution: I2, I3 may run first; retirement remains ordered
```
