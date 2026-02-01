## Overview

This project explores a data-centric strategy for improving Machine Learning Interatomic Potentials (MLIPs) by systematically incorporating transition-state information into the training dataset. 
Conventional MLIPs are typically trained on near-equilibrium structures obtained from relaxation and molecular dynamics (MD), which limits their reliability when simulations probe activated processes. 
To address this, we investigate whether adding minimum energy path (MEP) configurations obtained from Nudged Elastic Band (NEB) calculations can enhance model transferability and stability. 
The study focuses on Au adsorption and diffusion on Al(100) and AlPd(100) surfaces, where saddle-point configurations play a critical role in surface mobility.

## Key Methods and Approaches

Two datasets were constructed using ASE-based simulations: one containing only relaxed and MD-sampled structures (near-equilibrium), and another augmented with NEB images that capture saddle points along diffusion pathways. 
Using the Atomistic Machine-learning Package (AMP), we trained two neural network potentials with identical architectures but different training data compositions. 
This controlled setup ensures that performance differences can be attributed directly to dataset quality rather than model complexity. 
The models were evaluated through force error analysis and ANN-driven molecular dynamics simulations, with particular attention to energy conservation and structural stability under finite-temperature conditions.

## Key Results and Contribution

Including NEB-derived transition-state data significantly improved MLIP performance in off-equilibrium regions. 
The NEB-enhanced model showed lower force prediction errors and maintained stable, energy-conserving MD trajectories, 
while the MD-only model frequently exhibited energy drift and instability. 
These results demonstrate that strategically enriching training data with physically important but underrepresented configurations can be more effective than simply increasing model size. 
The project highlights a practical pathway toward more robust and transferable MLIPs for simulating activated processes.
