# `Cache Line`

**Concept:** Cache Line
**Action:** Transfer
**Object:** `Block of Data`
**Classification:** Cache Unit
**Environment:** CPU
**Path Type:** N/A
**Tags:** cache, cache-line, memory, cpu

---

### What It Is

A cache line is the fixed-size unit of data transferred between a cache and a lower level of the memory hierarchy.

### What It Does

It allows caches to store and retrieve data in blocks.

### How to Use

The processor typically transfers an entire cache line when bringing data into a cache.

### Requirements

Cache hardware and a memory hierarchy.

### Representation

```text
RAM Block → Cache Line → Cache

