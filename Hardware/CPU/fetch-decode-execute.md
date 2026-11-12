# `Fetch Decode Execute`

**Concept:** Cpu
**Action:** Execute
**Object:** `Fetch Decode Execute`
**Classification:** Cpu
**Environment:** Computer
**Path Type:** N/A
**Tags:** fetch-decode-execute, cpu, hardware

---

### What It Is

Fetch–decode–execute is a simplified model of instruction processing: obtain an instruction, interpret it, and perform its operation. Real CPUs overlap stages, add memory and retirement steps, and may use different names or organizations.

### What It Does

The model explains how a program counter selects an instruction, how its encoding becomes an operation, and how results are produced. It is a teaching abstraction, not a fixed three-box implementation.

### How to Use

1. Fetch the instruction at the current or predicted program counter.
2. Decode its operation and operands.
3. Execute it and determine the next PC; account for memory access and writeback where relevant.

### Requirements

An instruction stream, program counter, decoder, execution resources, and memory interface are needed in an actual CPU. Stage boundaries vary.

### Representation

```text
Fetch → Decode → Execute → (Memory / Writeback) → next instruction
```
