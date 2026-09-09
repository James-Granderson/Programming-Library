
Cache Coherence

Concept: Cache Coherence
Action: Synchronize
Object: Cached Data
Classification: Multicore Memory Mechanism
Environment: CPU
Path Type: N/A
Tags: cache, coherence, multicore, cpu, memory

What It Is

Cache coherence is the mechanism that keeps cached copies of shared memory consistent across CPU cores.

What It Does

It prevents different cores from indefinitely using conflicting values for the same shared memory location.

How to Use

The processor's coherence protocol coordinates cache state between cores.

Requirements

MulticU and cache-coherence hardware.

Representation
Core 1 Cache ↔ Coherence Mechanism ↔ Core 2 Cache

