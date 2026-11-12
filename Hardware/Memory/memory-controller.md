# `Memory Controller`

**Concept:** Memory
**Action:** Store
**Object:** `Memory Controller`
**Classification:** Memory
**Environment:** Computer
**Path Type:** N/A
**Tags:** memory-controller, memory, hardware

---

### What It Is

A memory controller manages access between processors or other requesters and system memory. It may be integrated into a CPU or chipset and commonly handles DRAM initialization, scheduling, timing, and error features where supported.

### What It Does

It converts requests into memory-device commands, arbitrates among requesters, and returns read data. It improves utilization through scheduling but does not make DRAM nonvolatile or eliminate its latency.

### How to Use

1. Trace a CPU or device request to the controller.
2. Follow how the controller selects a channel, bank, and row and schedules commands.
3. Check platform support for capacity, timings, ECC, and channel modes.

### Requirements

A controller compatible with the processor/platform and attached memory technology is required. Supported memory and features are platform-specific.

### Representation

```text
CPU/device requests → memory controller → channel commands → DRAM → returned data
```
