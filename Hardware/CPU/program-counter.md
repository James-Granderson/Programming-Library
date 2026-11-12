# `Program Counter`

**Concept:** Cpu
**Action:** Store
**Object:** `Program Counter`
**Classification:** Cpu
**Environment:** Computer
**Path Type:** N/A
**Tags:** program-counter, cpu, hardware

---

### What It Is

The program counter (PC) is CPU state containing an instruction address used to guide instruction fetch. Some architectures describe a current instruction pointer; implementation details and the exact visible value can differ.

### What It Does

Normally fetch advances to a subsequent instruction; branches, calls, exceptions, and returns select another address. Predicted PCs may be used speculatively before control flow is resolved.

### How to Use

1. Read the current fetch address in the relevant architecture model.
2. Determine whether sequential progression or a control-flow operation supplies the next address.
3. For debugging, account for ISA instruction length and any pipeline or exception conventions.

### Requirements

Instruction-address state and a fetch mechanism are required. Address format, update rules, and visibility are ISA-specific.

### Representation

```text
PC → instruction fetch → sequential next PC
             └─ branch/exception → target PC
```
