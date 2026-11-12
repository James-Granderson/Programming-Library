# `Data Movement Instructions`

**Concept:** Cpu
**Action:** Execute
**Object:** `Data Movement Instructions`
**Classification:** Cpu
**Environment:** Computer
**Path Type:** N/A
**Tags:** data-movement-instructions, cpu, hardware

---

### What It Is

Data-movement instructions transfer or copy values among registers, memory, and sometimes special registers. Loads and stores are common examples; moves between registers may be implemented as renaming or aliases in some CPUs.

### What It Does

They place data where later operations need it. A load typically reads through the memory hierarchy into a register; a store sends register data toward memory. These operations are distinct from persistent file storage.

### How to Use

1. Identify source and destination locations and the operand size.
2. For a load/store, compute the effective address and check alignment/permissions as defined by the ISA.
3. Follow the data through registers, cache, and memory as appropriate.

### Requirements

A CPU ISA with the relevant transfer operation, accessible addresses, and valid permissions are required. Ordering and alignment rules are architecture-specific.

### Representation

```text
register ──store──► cache / RAM
register ◄──load──── cache / RAM
```
