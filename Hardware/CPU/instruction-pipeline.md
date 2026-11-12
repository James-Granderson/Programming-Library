# `Instruction Pipeline`

**Concept:** Cpu
**Action:** Execute
**Object:** `Instruction Pipeline`
**Classification:** Cpu
**Environment:** Computer
**Path Type:** N/A
**Tags:** instruction-pipeline, cpu, hardware

---

### What It Is

An instruction pipeline divides instruction execution into stages so different instructions can occupy different stages at once. Typical stages include fetch, decode, execute, memory access, and writeback, but actual pipelines vary.

### What It Does

Overlapping independent instructions can increase throughput; pipelining does not necessarily reduce the latency of one instruction. Dependencies, branches, and resource conflicts can stall or flush work.

### How to Use

1. Follow several instructions across stages rather than treating one instruction as the entire pipeline.
2. Mark dependencies and branch decisions that can delay progress.
3. Distinguish instruction pipeline stages from a broader CPU/system data pipeline.

### Requirements

Stage registers, control logic, and hazard handling are required. Stage count, names, issue width, and timing are implementation-specific.

### Representation

```text
Cycle →     1       2       3       4
I1          Fetch   Decode  Execute Writeback
I2                  Fetch   Decode  Execute
I3                          Fetch   Decode
```
