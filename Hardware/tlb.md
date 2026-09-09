
TLB

Concept: TLB
Action: Cache
Object: Address Translation
Classification: Memory Management Hardware
Environment: CPU
Path Type: N/A
Tags: tlb, virtual-memory, cache, cpu

What It Is

The Translation Lookaside Buffer (TLB) is a small cache of recent virtual-to-physical address translations.

What It Does

It avoids repeatedly walking page tables for translations that are already known.

How to Use

The CPU checks the TLB during virtual address translation.

Requirements

Virtual memory hardware.

Representation
Virtual Address → TLB → Physical Address

