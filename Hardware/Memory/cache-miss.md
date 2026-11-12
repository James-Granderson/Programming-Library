# `Cache Miss`

**Concept:** Memory
**Action:** Store
**Object:** `Cache Miss`
**Classification:** Memory
**Environment:** Computer
**Path Type:** N/A
**Tags:** cache-miss, memory, hardware

---

### What It Is

A cache miss occurs when a cache cannot supply a requested address from a valid matching line. Misses are often described as compulsory, capacity, or conflict, though these categories are analytical rather than hardware events.

### What It Does

The request is serviced by a lower cache or memory and may cause a line fill and replacement. Some misses overlap or are handled differently by prefetching, write policy, or coherence state.

### How to Use

1. Check tag and valid state for the requested set.
2. Follow the request to the next level and identify whether a line fill is needed.
3. Track victim selection, any writeback, and the returned data.

### Requirements

The cache must have no usable matching entry for the request; servicing requires a reachable lower level or defined fault path.

### Representation

```text
lookup → no valid tag match → next level fetch → line fill / victim replacement → data
```
