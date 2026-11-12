# `Virtual Memory`

**Concept:** Memory
**Action:** Store
**Object:** `Virtual Memory`
**Classification:** Memory
**Environment:** Computer
**Path Type:** N/A
**Tags:** virtual-memory, memory, hardware

---

### What It Is

Virtual memory is an address-space abstraction in which software uses virtual addresses that hardware translates to physical memory. The operating system manages mappings and protections; paging can also support moving inactive contents to backing storage.

### What It Does

It isolates processes, provides a flexible address space, and lets the OS map shared or private pages. It does not mean every address resides in RAM: a nonresident page may require storage I/O and cause a costly fault.

### How to Use

1. A process issues a virtual address.
2. The MMU checks a TLB or walks page tables and verifies permissions.
3. Use the mapped physical address, or handle a page fault if the mapping is absent.

### Requirements

An MMU, OS-managed address spaces and page tables, and physical memory are required. Backing storage is used only when OS policy and configuration require it.

### Representation

```text
process virtual address → TLB/page table → physical RAM
                             └→ page fault → OS may fetch backing page
```
