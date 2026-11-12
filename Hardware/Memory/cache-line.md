# `Cache Line`

**Concept:** Memory
**Action:** Store
**Object:** `Cache Line`
**Classification:** Memory
**Environment:** Computer
**Path Type:** N/A
**Tags:** cache-line, memory, hardware

---

### What It Is

A cache line (or cache block) is the unit of data transferred between adjacent levels of a cache hierarchy. A line contains a contiguous address range plus metadata such as tag, valid, and coherence state.

### What It Does

Fetching one requested byte or word usually brings in its entire line, exploiting spatial locality. Line size also affects bandwidth, miss penalty, and coherence granularity.

### How to Use

1. Determine the line size and align the requested address to its line boundary.
2. Use the offset within the line to select the requested data.
3. When analyzing writes or coherence, track metadata for the whole line.

### Requirements

A cache implementation defines line size, metadata, and replacement/coherence policy; these are architecture-specific.

### Representation

```text
tag | state/valid metadata | data bytes [offset 0 … line size−1]
```
