# `Multicore`

**Concept:** Cpu
**Action:** Execute
**Object:** `Multicore`
**Classification:** Cpu
**Environment:** Computer
**Path Type:** N/A
**Tags:** multicore, cpu, hardware

---

### What It Is

A multicore processor contains two or more CPU cores in one package or integrated system. Each core can execute an instruction stream, while caches, memory controllers, and other resources may be private or shared.

### What It Does

Multiple cores allow parallel threads to make progress concurrently when software and workload permit. They do not automatically speed up a serial task; synchronization and shared-resource contention also affect performance.

### How to Use

1. Determine how many cores are available to the operating system.
2. Identify independent work that can run concurrently and coordinate shared data safely.
3. Measure the workload, since scaling depends on parallelism and shared bottlenecks.

### Requirements

A multicore processor, suitable power/cooling, and software capable of using parallel execution are needed. Cache and interconnect topology vary.

### Representation

```text
Thread A → Core 0 ┐
Thread B → Core 1 ├→ shared / private cache and memory system
Thread C → Core 2 ┘
```
