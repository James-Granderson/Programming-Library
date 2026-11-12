# `Page`

**Concept:** Memory
**Action:** Store
**Object:** `Page`
**Classification:** Memory
**Environment:** Computer
**Path Type:** N/A
**Tags:** page, memory, hardware

---

### What It Is

A memory page is a fixed-size unit of virtual memory managed by an operating system and memory-management hardware. The corresponding physical-memory unit is often called a frame; page size may vary and large pages are supported on many systems.

### What It Does

Pages let the OS map virtual address ranges to physical frames, apply permissions, and move or reclaim memory in page-sized units. A page is not the same as a cache line or a disk sector.

### How to Use

1. Determine the page size and virtual address's page number and offset.
2. Look up the mapping and permissions through the page table/TLB.
3. Keep the offset when translating to the mapped physical frame.

### Requirements

An OS and MMU supporting paging, page tables, and physical frames are required. Page sizes and mapping rules are architecture-specific.

### Representation

```text
virtual address = page number | offset
page-table mapping: page number → frame number; offset unchanged
```
