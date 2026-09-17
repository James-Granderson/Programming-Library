# `TLB`

**Concept:** Memory
**Action:** Cache
**Object:** `Virtual Memory Address Translation`
**Classification:** CPU Cache
**Environment:** Computer
**Path Type:** N/A
**Tags:** tlb, cpu, memory, virtual-memory, hardware

---

### What It Is

A Translation Lookaside Buffer (TLB) is a small, fast cache inside the memory management hardware that stores recent mappings from virtual page numbers to physical page numbers.

### What It Does

When a program accesses memory, the CPU first checks the TLB to see whether the virtual address it needs is already mapped. If the translation is found in the TLB, the CPU can resolve the address quickly without walking the full page table. If the mapping is missing, the system performs a page-table lookup and then stores the result back into the TLB for later reuse.

This speeds up memory access by reducing the overhead of repeated virtual-to-physical address translation, especially in systems that use paging and virtual memory.

### How to Use

1. The CPU receives a virtual address from a running program.
2. The TLB checks whether that virtual page has a recent translation cached.
3. On a TLB hit, the physical address is used immediately.
4. On a TLB miss, the memory management unit fetches the mapping from the page table.
5. The new mapping is inserted into the TLB so future accesses are faster.

### Requirements

Virtual memory enabled.  // Allows addresses to be translated from virtual to physical space.
Page tables.  // Store the full mapping information for memory pages.
MMU or memory-management hardware.  // Performs address translation and TLB management.

### Representation

```text
Virtual Address
      ↓
   TLB Check
   /       \
Hit        Miss
 |           ↓
 |      Page Table Walk
 |           ↓
 |      Update TLB
  └────────► Physical Address
```
