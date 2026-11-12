# `L3 Cache`

**Concept:** Memory
**Action:** Store
**Object:** `L3 Cache`
**Classification:** Memory
**Environment:** Computer
**Path Type:** N/A
**Tags:** l3-cache, memory, hardware

---

### What It Is

An L3 cache is commonly a large last-level cache shared by several CPU cores, though not every design has an L3 and the term does not guarantee a particular topology. Some processors use different names or additional levels.

### What It Does

It can satisfy requests missed by private nearer caches before they reach DRAM, reducing off-chip traffic. Sharing can aid communication but also introduce contention.

### How to Use

1. Trace misses from nearer caches to the last-level cache.
2. Check whether the target processor's L3 is shared and how it is partitioned.
3. Distinguish an L3 hit from a DRAM access.

### Requirements

A processor implementing an L3 cache and a memory path beyond it are required. Capacity, topology, and policy are model-specific.

### Representation

```text
Core 0 L1/L2 ─┐
Core 1 L1/L2 ─┼→ shared L3 → memory controller → DRAM
Core 2 L1/L2 ─┘
```
