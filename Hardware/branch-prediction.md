
Branch Prediction

Concept: Branch Prediction
Action: Predict
Object: Control Flow
Classification: CPU Optimization
Environment: CPU
Path Type: N/A
Tags: branch-prediction, cpu, pipeline, control-flow

What It Is

Branch prediction is a CPU mechanismicts which path a conditional branch will take.

What It Does

It allows the processor to continue preparing instructions before the branch condition is fully resolved.

How to Use

The processor predicts a branch, continues execution speculatively, and corrects the work if the prediction was wrong.

Requirements

CPU pipeline and branch prediction hardware.

Representation
Conditional Branch
       ↓
 Prediction
   ↙       ↘
Path A    Path B

