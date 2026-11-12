# `Page Table`

**Concept:** Memory
**Action:** Store
**Object:** `Page Table`
**Classification:** Memory
**Environment:** Computer
**Path Type:** N/A
**Tags:** page-table, memory, hardware

---

### What It Is

A page table is an operating-system-managed data structure used by a memory-management unit to translate virtual page numbers to physical frames and record attributes such as permissions and presence.

### What It Does

A page-table walk looks up the translation when it is not available in a TLB. Entries can also encode access rights, caching attributes, and status; a missing or invalid mapping can trigger a page fault.

### How to Use

1. Take the virtual address's page number and offset.
2. Use the architecture-defined page-table walk to find a valid entry and check permissions.
3. Combine the physical frame number with the unchanged page offset, or handle a fault.

### Requirements

Virtual memory, page tables in memory, and an MMU with a defined translation format are required. Levels, entry bits, and page sizes vary by architecture.

### Representation

```text
virtual page number → page-table entries → physical frame number
page offset ────────────────────────────┘ → physical address
```
