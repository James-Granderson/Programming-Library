# `Instruction Register`

**Concept:** Cpu
**Action:** Execute
**Object:** `Instruction Register`
**Classification:** Cpu
**Environment:** Computer
**Path Type:** N/A
**Tags:** instruction-register, cpu, hardware

---

### What It Is

An instruction register is a CPU register that holds an instruction or part of one during processing. In a simple processor it may hold the fetched instruction for decoding; modern pipelined CPUs often use stage registers, queues, and decoded forms instead of one visible register.

### What It Does

It preserves instruction bits between fetch and decode or another processing stage so control logic can interpret them. It is distinct from the program counter, which identifies the next instruction address.

### How to Use

1. Locate the instruction-holding state in the design or teaching model.
2. Trace fetched bits into decode while tracking the program counter separately.
3. In a modern core, follow the front-end queue or pipeline register documented by that design.

### Requirements

A fetch path and state element wide enough for the instruction representation are required. Organization varies with fixed- or variable-length ISA designs.

### Representation

```text
instruction memory → fetch register/queue → decoder; PC tracks fetch address
```
