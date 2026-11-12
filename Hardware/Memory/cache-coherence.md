# `Cache Coherence`

**Concept:** Memory
**Action:** Store
**Object:** `Cache Coherence`
**Classification:** Memory
**Environment:** Computer
**Path Type:** N/A
**Tags:** cache-coherence, memory, hardware

---

### What It Is

Cache coherence is the set of mechanisms that keeps multiple cached copies of shared memory from producing inconsistent values across CPU cores or agents. Protocols commonly track line states and coordinate ownership; exact protocols differ.

### What It Does

On a read or write, coherence rules determine whether a line can be used, shared, invalidated, or transferred from another cache. Coherence is distinct from memory consistency, which specifies ordering visible to programs.

### How to Use

1. Identify which agents cache a shared address.
2. Trace line state changes on reads and writes.
3. Distinguish maintaining a single coherent value from ordering separate memory operations.

### Requirements

Multiple cacheable agents and a coherence mechanism in the interconnect or memory system are required. State names and policies are implementation-specific.

### Representation

```text
Core 0 cache ── coherence messages ── Core 1 cache
             └──── shared memory system ────┘
```
