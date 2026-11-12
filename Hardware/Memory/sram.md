# `Sram`

**Concept:** Memory
**Action:** Store
**Object:** `Sram`
**Classification:** Memory
**Environment:** Computer
**Path Type:** N/A
**Tags:** sram, memory, hardware

---

### What It Is

Static random-access memory (SRAM) stores each bit in a bistable circuit, commonly a multi-transistor cell, and retains its state while powered without periodic refresh. SRAM is typically faster and denser than registers but less dense and more costly per bit than DRAM.

### What It Does

SRAM is used where low latency is valuable, especially CPU caches and buffers. It is volatile, and its speed, capacity, and power characteristics depend on the implementation.

### How to Use

1. Identify SRAM by its role in a cache or embedded memory block.
2. Check access interface, capacity, and timing for the device.
3. Do not confuse its no-refresh cell operation with nonvolatile storage.

### Requirements

A powered SRAM device and compatible interface are required. It loses data without power and is not the same cell technology as DRAM.

### Representation

```text
powered bistable cell → retains 0/1 without refresh
SRAM cache ⇄ CPU core
```
