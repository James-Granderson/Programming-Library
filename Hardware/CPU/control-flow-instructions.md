# `Control Flow Instructions`

**Concept:** Cpu
**Action:** Execute
**Object:** `Control Flow Instructions`
**Classification:** Cpu
**Environment:** Computer
**Path Type:** N/A
**Tags:** control-flow-instructions, cpu, hardware

---

### What It Is

Control-flow instructions change which instruction address is executed next. They include branches, jumps, calls, returns, and sometimes traps or system transitions; exact categories depend on the ISA.

### What It Does

A control-flow operation selects a target address instead of simply continuing to the sequential instruction. Calls and returns may also save or restore return state, while conditional branches depend on a condition.

### How to Use

1. Decode the operation and determine whether it is conditional.
2. Compute or obtain the target and evaluate any condition.
3. Follow the selected next PC; account for prediction and pipeline redirection separately.

### Requirements

A CPU implementing the control-flow operation and a valid target/condition are required. Target formation and privilege effects are ISA-specific.

### Representation

```text
current PC → condition / target selection → next PC
```
