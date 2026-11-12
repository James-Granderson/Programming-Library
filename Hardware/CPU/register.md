# `Register`

**Concept:** Cpu
**Action:** Execute
**Object:** `Register`
**Classification:** Cpu
**Environment:** Computer
**Path Type:** N/A
**Tags:** register, cpu, hardware

---

### What It Is

A CPU register is a small, fast storage location within a processor. Architectural registers are named by the instruction set; physical registers, pipeline registers, and control registers are implementation or system concepts with different roles.

### What It Does

Registers hold operands, addresses, intermediate values, or processor state close to execution units. Register files provide read/write ports whose count and timing constrain the design.

### How to Use

1. Identify whether the register is architectural, control, or an internal pipeline element.
2. Trace which instruction reads or writes it.
3. Use the ISA or processor documentation for width, privilege, and side effects.

### Requirements

A processor design with storage elements and access logic is required. Register names, widths, and semantics are architecture-specific.

### Representation

```text
instruction → register-file read → execution → register-file write
```
