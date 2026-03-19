# Recursive Geometric Framework for Fundamental Physical Constants

Reproducibility code for the paper *Geometric Conjecture for the Origin of Fundamental Physical Constants from a Discrete Recursive Geometric Framework*.

## Environment Compatibility
- **Python 3.8+**: V1, V2, V3, V4, V6 (requires numpy)
- **SageMath 9.0+**: All scripts (V1–V6), recommended for V5 (polytope combinatorics)

> V5_edge_count.py depends on SageMath native polytope modules; run V5 in SageMath for full validation.

## Script List (Appendix G)
- V1_spectral_recursion.py: Thermal kernel self-similarity & spectral recursion
- V2_entropy_convergence.py: Information loss rate & critical depth Nc=7
- V3_mass_ratio.py: Proton-electron mass ratio
- V4_fine_structure.py: Inverse fine-structure constant α⁻¹
- V5_edge_count.py: 120-cell / 600-cell Poincaré duality & edge ratio 5/3
- V6_neutrino_hierarchy.py: Neutrino normal hierarchy, φ-scaling, Planck 2024 constraint

## Usage
### Python
```bash
pip install numpy
python script_name.py
