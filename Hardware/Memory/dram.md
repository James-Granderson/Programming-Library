# `Dram`

**Concept:** Memory
**Action:** Store
**Object:** `Dram`
**Classification:** Memory
**Environment:** Computer
**Path Type:** N/A
**Tags:** dram, memory, hardware

---

### What It Is

Dynamic random-access memory (DRAM) stores each bit as charge in a capacitor controlled by a transistor. The charge leaks, so DRAM requires periodic refresh; typical system RAM uses synchronous DRAM such as DDR generations.

### What It Does

DRAM provides dense, relatively inexpensive volatile main memory. Reads and writes operate through rows, banks, and bursts, with more latency and refresh management than on-chip SRAM caches.

### How to Use

1. Check the supported DRAM type, speed, capacity, and module configuration.
2. Let the memory controller initialize and schedule DRAM accesses.
3. Remember that contents are lost without power and require refresh while powered.

### Requirements

DRAM chips or modules, a compatible memory controller, supported signaling, and refresh are required. Timings and features vary by generation and platform.

### Representation

```text
Memory controller → DRAM bank/row → capacitor cells (refresh required)
```
