# Geometric Conjecture for the Origin of Fundamental Physical Constants

Python/SageMath code for reproducing numerical results in:

**"Geometric Conjecture for the Origin of Fundamental Physical Constants from Recursive Discrete Spacetime"**  
Jingbo Zhang (2026)

---

## Core Mathematical Identities

The framework is built on two fundamental geometric relations:

1. **Golden ratio**: $\phi = \frac{1+\sqrt{5}}{2}$

2. **Geometric $\pi$ from 120-cell**: 
   $$\pi = 10 \cdot \arcsin\left(\frac{1}{2\phi}\right)$$
   
   This identity derives from the half-central angle of pentagonal faces in the regular 120-cell $\{5,3,3\}$.

---

## Main Results

| Constant | Theoretical Value | CODATA 2022 | Relative Deviation |
|----------|------------------|-------------|-------------------|
| $\alpha^{-1}$ | **137.035999168** | 137.035999084 | $6.11 \times 10^{-10}$ |
| $m_p/m_e$ | **1835.948298** | 1836.152673 | $1.11 \times 10^{-4}$ |

**Key distinction for neutrino masses**:
- **Geometrically rigid predictions**: Mass ratio $m_1:m_2:m_3 = 1:\phi:\phi^2$ and normal hierarchy ($m_1 &lt; m_2 &lt; m_3$)
- **Phenomenological input**: Absolute mass scale $\sim 0.01$ eV (chosen to satisfy cosmological bounds $\sum m_i &lt; 0.12$ eV)

---

## Verification Scripts

All scripts are independent with no cross-dependencies.

| Script | Function | Appendix |
|--------|----------|----------|
| `V1_spectral_recursion.py` | Heat kernel self-similarity; spectral recursion verification | A |
| `V2_entropy_convergence.py` | Information loss rate $\delta_N$; entropy gradient convergence | B |
| `V3_mass_ratio.py` | Proton-electron mass ratio geometric factors | C |
| `V4_fine_structure.py` | $\alpha^{-1}$ series expansion; Minakshisundaram-Pleijel coefficients | D |
| `V5_edge_count.py` | 120-cell/600-cell combinatorics; Poincaré duality | E |
| `V6_neutrino_hierarchy.py` | Neutrino mass scaling; $\phi$-hierarchy prediction | F |

### Usage

```bash
python V4_fine_structure.py    # Reproduces α⁻¹ = 137.035999168
python V3_mass_ratio.py        # Reproduces m_p/m_e = 1835.948298
