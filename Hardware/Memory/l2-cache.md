# `L2 Cache`

**Concept:** Memory
**Action:** Store
**Object:** `L2 Cache`
**Classification:** Memory
**Environment:** Computer
**Path Type:** N/A
**Tags:** l2-cache, memory, hardware

---

### What It Is

An L2 cache is a cache level between a core's L1 cache and a last-level cache or main memory. It is often larger and slower than L1; it may be private to a core or shared by a group of cores.

### What It Does

It can serve accesses missed by L1 and reduce traffic to more distant levels. L2 organization, inclusivity, and access path are processor-specific, not guaranteed by the label alone.

### How to Use

1. Follow an L1 miss into L2.
2. Determine whether L2 hits or sends the request farther down the hierarchy.
3. Consult the processor's topology to see which cores share this level.

### Requirements

A cache hierarchy containing an L2 level and a next-level service path are required. Size and sharing depend on the CPU.

### Representation

```text
Core → L1 miss → L2 lookup → hit: data / miss: next level
```
