# `Memory Address`

**Concept:** Memory
**Action:** Store
**Object:** `Memory Address`
**Classification:** Memory
**Environment:** Computer
**Path Type:** N/A
**Tags:** memory-address, memory, hardware

---

### What It Is

A memory address is a value used to identify a location or range in an address space. A CPU program typically uses virtual addresses; translation hardware maps them to physical memory addresses, and devices may use I/O or DMA address spaces.

### What It Does

The address selects the bytes or data being read or written. Address interpretation depends on width, address space, access size, translation, and permissions; it is not itself the stored data.

### How to Use

1. Identify the address space and whether the value is virtual, physical, or device-visible.
2. Determine access size and alignment.
3. Follow translation and permission checks before locating the memory hierarchy entry.

### Requirements

A defined address space, addressing rules, and access mechanism are required. Translation and protection depend on the processor and operating system.

### Representation

```text
virtual address → translation/protection → physical address → cache / RAM
```
