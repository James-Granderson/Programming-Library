# hash-table

**Concept:** Data Structures
**Action:** Store
**Object:** Hash Table
**Classification:** Data Structure
**Environment:** Language-independent
**Path Type:** N/A
**Tags:** data-structure

---

### What It Is

A data structure that stores key-value pairs by using a hash function to map each key to a location.

### What It Does

Provides fast average-case insertion, lookup, and removal by locating a key through its hash value.

### How to Use

Choose a hash function, use it to locate a bucket for each key, and define a collision strategy for keys that map to the same bucket.

### Requirements

Keys  // Identify stored values.
Hash function  // Maps each key to a bucket.
Collision strategy  // Handles keys that map to the same bucket.

### Representation

```text
hash(key) → bucket
bucket → key-value pair
```
