
Flags

Concept: Flags
Action: Record
Object: CPU Status
Classification: Register State
Environment: CPU
Path Type: N/A
Tags: flags, status, register, cpu

What It Is

CPU flags are status bits that record information about operations.

What It Does

Common flags include:

Zero
Carry
Negative / Sign
Overflow
How to Use

Comparisons and arithmetic operations can update flags. Conditional branches can examine them.

Example:

CMP R1, R2
JZ target
Requirements

A CPU architecture that defines status flags.

Representation
Operation → Flags → Conditional Branch

