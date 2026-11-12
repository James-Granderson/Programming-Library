# `L1 Cache`

**Concept:** Memory
**Action:** Store
**Object:** `L1 Cache`
**Classification:** Memory
**Environment:** Computer
**Path Type:** N/A
**Tags:** l1-cache, memory, hardware

---

### What It Is

An L1 cache is the first cache level close to a CPU core, commonly split into instruction and data caches. It is generally designed for very low access latency and is smaller than lower cache levels.

### What It Does

It supplies frequently used instructions or data to the core. On an L1 miss, the request proceeds to another cache or memory; an L1 may be private to a core, but designs differ.

### How to Use

1. Identify whether the access targets instruction or data L1.
2. Check for a hit and follow misses to the next level.
3. Use processor documentation for size, associativity, and sharing.

### Requirements

A processor core with an L1 cache and a defined next-level path is required. Organization and inclusion policy vary.

### Representation

```text
Core ↔ L1 instruction/data cache → L2 → lower hierarchy
```
