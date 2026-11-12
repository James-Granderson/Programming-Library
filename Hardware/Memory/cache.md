# `Cache`

**Concept:** Memory
**Action:** Store
**Object:** `Cache`
**Classification:** Memory
**Environment:** Computer
**Path Type:** N/A
**Tags:** cache, memory, hardware

---

### What It Is

A cache is a small, fast storage structure holding copies of data from a slower or more distant source. CPU caches usually keep recently or predictively useful memory lines; caches also appear in other systems and software layers.

### What It Does

It reduces average access time when requests reuse cached data. A hit is served locally; a miss consults another level. Capacity, associativity, replacement, write policy, and workload locality influence results.

### How to Use

1. Identify the cached data, line granularity, and hierarchy level.
2. Follow a request through tag lookup and hit or miss handling.
3. Evaluate locality and miss behavior rather than assuming every access is faster.

### Requirements

A source of authoritative data, storage for cached copies, lookup/management logic, and a policy for misses and writes are required.

### Representation

```text
CPU request → L1 → (miss) L2 → (miss) last-level cache → RAM
```
