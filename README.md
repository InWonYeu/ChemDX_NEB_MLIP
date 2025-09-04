# ChemDX_NEB_MLIP

Machine Learning Interatomic Potential (MLIP) project using the ChemDX database  
🏆 Developed as part of the **KRICT ChemDX Hackathon 2025**

---

## 🧠 Motivation

> **Can we systematically supply missing data that greatly improves MLIPs?**

- Many MLIPs suffer from poor transferability due to insufficient or biased training data, which is often limited to equilibrium configurations. 
- In this project, we explore whether supplementing *minimum energy path (MEP)* data (from NEB calculations) can improve the **accuracy and stability** of MLIP models.

<p align="center">
  <img src="docs/images/motivation.gif" width="600">
</p>

---

## 🔬 Approach Overview

1. **Data Generation**
    - Sampled atomic structures using Relaxation, MD, and NEB (via ASE)
    - Focus: Adsorption systems (Au on Al(100), Au on AlPd(100))

2. **ANN Model Training**
    - Trained two separate neural network potentials:
        - **Set #1**: Relax + MD
        - **Set #2**: Relax + MD + NEB

3. **Model Evaluation**
    - Tested models through ANN-MD simulations
    - Compared energy conservation and force accuracy

<p align="center">
  <img src="docs/images/overview.png" width="600">
</p>

---

## ⚙️ Systems Studied

| System            | Type         | Stable Site |
|------------------|--------------|-------------|
| Au on Al(100)     | Single metal | Hollow      |
| Au on AlPd(100)   | Alloy metal  | Hollow      |

<p align="center">
  <img src="docs/images/system_PES.png" width="700">
</p>

---

## 📈 Key Results

---

### 📚 Dataset Comparison

| Dataset | Sampling Methods       | Config Space Coverage       |
|---------|------------------------|------------------------------|
| Set #1  | Relaxation + MD        | Near-equilibrium only        |
| Set #2  | Relax + MD + **NEB**   | Near-equilibrium + saddle pts ✅ |

<p align="center">
  <img src="docs/images/dataset_comparison.gif" width="700">
</p>

---

### ⚛️ MD Stability: NEB Makes a Difference

| Model Type         | Force Error | Energy Conservation |
|--------------------|-------------|----------------------|
| MD-only            | High        | ❌                    |
| MD + **NEB**       | Low         | ✅                    |

<p align="center">
  <img src="docs/images/md_results.gif" width="750">
</p>

---

---

## 🛠 Tools Used

- **ASE**: Structure generation, Relaxation, MD, NEB
- **AMP** (ASE's ML package): ANN model training
- **ChemDX Database**: Initial structure and metadata source
- Python (Jupyter), Matplotlib, NumPy

---

## 🔍 Conclusion

Adding NEB-based data significantly improves:
- Sampling of off-equilibrium regions
- Force prediction accuracy
- Energy conservation during MD

This strategy enables **more reliable and transferable MLIPs**, especially for surface and catalytic systems.

---

## 📌 Acknowledgments

This project was developed during the **KRICT ChemDX Hackathon 2025**.  
We thank the ChemDX team for providing access to the database and computational resources.

---

## 📬 Contact

For questions or contributions, please contact:  
**In Won Yeu** (GitHub: [@InWonYeu](https://github.com/InWonYeu))
