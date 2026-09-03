
Data Movement Instructions

Concept: Data Movement Instruction
Action: Move
Object: Data
Classification: CPU Instruction
Environment: CPU
Path Type: N/A
Tags: instruction, load, store, move, cpu

What It Is

A data movement instruction transfers data between locations.

What It Does

Common operations include:

MOV
LOAD
STORE

LOAD generally moves data from memory into a register.

STORE generally moves data from a register into memory.

How to Usmple:

LOAD R1, [0x1000]

Conceptually:

Memory[0x1000] → R1
Requirements

A CPU architecture with data movement instructions.

Representation
Memory → LOAD → Register

