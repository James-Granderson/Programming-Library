# `Cache Hit`

**Concept:** Memory
**Action:** Store
**Object:** `Cache Hit`
**Classification:** Memory
**Environment:** Computer
**Path Type:** N/A
**Tags:** cache-hit, memory, hardware

---

### What It Is

A cache hit occurs when a requested address is present in the relevant cache at a usable state. The hit test normally compares the address's tag with a selected cache entry and checks its valid/status bits.

### What It Does

On a hit, the cache supplies the requested data without fetching that block from the next memory level. Latency and behavior depend on cache level and access type.

### How to Use

1. Split the address into index, tag, and offset as the cache design specifies.
2. Check whether the selected entry is valid and its tag matches.
3. On a hit, select the requested bytes or word using the offset.

### Requirements

A cache containing a valid matching line and a request that the cache can service are required.

### Representation

```text
request address → index/tag lookup → valid tag match? yes → return cached data
```
