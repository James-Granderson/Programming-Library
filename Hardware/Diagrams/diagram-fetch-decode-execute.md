# `Diagram Fetch Decode Execute`

**Concept:** Diagrams
**Action:** Store
**Object:** `Diagram Fetch Decode Execute`
**Classification:** Concept
**Environment:** CPU
**Path Type:** N/A
**Tags:** diagram-fetch-decode-execute, diagrams, hardware

---

### What It Is

A fetch–decode–execute diagram is a visual aid for a simplified model of instruction processing. It represents conceptual stages rather than three required physical components or the complete organization of a modern CPU.

### What It Does

It shows that an instruction is fetched from an address, interpreted, and executed, with the next instruction address selected afterward. Real processors overlap stages, handle memory and writeback separately, and may speculate or execute out of order.

### How to Use

1. Follow the arrows from the program counter to instruction fetch.
2. Track the instruction through decode and execution, then note result and next-address updates.
3. Treat the sequence as a teaching model; consult a microarchitecture diagram for pipelines and parallel stages.

### Requirements

The diagram should label the model's scope and distinguish instruction flow from data flow. Stage names and implementation vary by architecture.

### Representation

```text
PC → Fetch instruction → Decode operation → Execute
 ↑                                         │
 └──────────── next PC / branch target ────┘
```
