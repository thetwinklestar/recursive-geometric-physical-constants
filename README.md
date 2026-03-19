# Recursive Geometric Framework for Fundamental Physical Constants

[![Python 3.8+](https://img.shields.io/badge/python-3.8+-blue.svg)](https://www.python.org/downloads/)
[![SageMath 9.0+](https://img.shields.io/badge/SageMath-9.0+-green.svg)](https://www.sagemath.org/)

Reproducibility code for the paper:  
**"Geometric Conjecture for the Origin of Fundamental Physical Constants from Recursive Discrete Spacetime"**  
*Jingbo Zhang (2026)*

&gt; **Abstract**: This repository contains the numerical verification scripts for a geometric framework where fundamental constants (α⁻¹ ≈ 137.036, mₚ/mₑ ≈ 1836, neutrino hierarchy) emerge from the recursive topology of discrete spacetime, rooted in the binary icosahedral group 2I and the 120-cell/600-cell duality.

---

## 📋 Script Overview (Appendix G)

| Script | Environment | Core Verification | Key Output |
|--------|-------------|-------------------|------------|
| **V1_spectral_recursion.py** | Python 3.8+ | Heat kernel self-similarity | Spec(Δₙ₊₁) = φ²Spec(Δₙ) ⊔ φ⁻²Spec(Δₙ) |
| **V2_entropy_convergence.py** | Python 3.8+ | Information loss rate δₙ | Critical depth **N_c = 7** |
| **V3_mass_ratio.py** | Python 3.8+ | Geometric factor decomposition | mₚ/mₑ ≈ 1835.95 (deviation 10⁻⁴) |
| **V4_fine_structure.py** | Python 3.8+ | α⁻¹ series expansion | **137.0359991(7)** (deviation 10⁻⁸) |
| **V5_edge_count.py** | Python / Sage | 120-cell/600-cell duality | Edge ratio **5/3** → Complexity **10/7** |
| **V6_neutrino_hierarchy.py** | Python 3.8+ | Neutrino hierarchy from 2I | Normal hierarchy (rigid) vs mass scale (phenomenological) |

---

## ⚠️ Critical Note on V6 (Neutrino Masses)

**V6 requires careful interpretation.** Two distinct levels of predictions:

### 1. Geometrically Rigid (Parameter-Free)
- **Normal hierarchy**: m₁ &lt; m₂ &lt; m₃
- **Mass ratio**: 1 : φ : φ² (φ = (1+√5)/2)
- **Falsifiability**: If JUNO/DUNE observes **inverted hierarchy** (m₃ &lt; m₁ &lt; m₂), framework is invalidated

### 2. Phenomenological Example (Illustrative)
- **Absolute scale** (0.01 eV) is *ad hoc* (satisfies Σmᵢ &lt; 0.12 eV)
- **Mass-squared differences** differ from experiment by factors of 2–6 (expected, lacks PMNS mixing)
- These demonstrate cosmological compatibility but are **not first-principles predictions**

---

## 🚀 Quick Start

### Pure Python (V1–V4, V6)
```bash
pip install numpy scipy
python V1_spectral_recursion.py
python V6_neutrino_hierarchy.py  # Check: mass ratio 1:1.618:2.618
