# `Decoder`

**Concept:** Cpu
**Action:** Execute
**Object:** `Decoder`
**Classification:** Cpu
**Environment:** Computer
**Path Type:** N/A
**Tags:** decoder, cpu, hardware

---

### What It Is

A CPU instruction decoder interprets an instruction's encoded bits according to the instruction set. It identifies the operation, operands, addressing details, and required execution resources.

### What It Does

It translates machine-code fields into internal control or micro-operation information for later stages. Complex instructions may decode into multiple internal operations; this is implementation-dependent.

### How to Use

1. Start with the instruction bytes and the correct ISA mode.
2. Separate opcode and operand fields using the architecture's encoding rules.
3. Trace the decoded operation and operands into execution.

### Requirements

A defined instruction encoding and decoder for that ISA and mode are required. Internal micro-operation formats are processor-specific.

### Representation

```text
instruction bits → [ decoder ] → operation + operand/control information
```
