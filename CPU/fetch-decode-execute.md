
Fetch-Decode-Execute

Concept: Fetch-Decode-Execute
Action: Process
Object: Instn
Classification: Execution Cycle
Environment: CPU
Path Type: N/A
Tags: fetch, decode, execute, instruction-cycle, cpu

What It Is

Fetch-decode-execute is a basic model for describing how a CPU processes instructions.

What It Does

The cycle consists of three basic stages:

Fetch

The CPU obtains an instruction from memory using the program counter.

Decode

The CPU determines what the instruction means and what resources are required.

Execute

The CPU performs the operation specified by the instruction.

The cycle then repeats for the next instruction.

How to Use

The model can be used to understand the basic flow of instruction execution.

Modern processors may overlap, reorder, or execute multiple instructions simultaneously, so the simple cycle is a conceptual model rather than a complete description of modern CPU internals.

Requirements

A processor capable of executing machine instructions.

Representation
Fetch
  ↓
Decode
  ↓
Execute
  ↓
Fetch
  ↓
Decode
  ↓
Execute
  ↺

