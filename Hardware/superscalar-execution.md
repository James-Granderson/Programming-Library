
superscalar-execution

Concept: CPU
Action: Execute
Object: superscalar-execution
Classification: Execution Mechanism
Environment: CPU
Path Type: N/A
Tags: cpu, pipeline, execution, performance

What It Is

Superscalar execution allows a CPU core to begin or execute multiple instructions during the same clock cycle when the instructions can be processed independently.

What It Does

Uses multiple execution units so several instructions can progress in parallel.

How to Use

The processor determines which instructions can execute simultaneously and dispatches them to available execution units.

Requirements

Superscalar CPU architecture

Representation
            ┌→ Execute Unit 1
Decode ─────┼→ Execute Unit 2
            └→ Execute Unit 3

