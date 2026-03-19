# Recursive Geometric Framework for Fundamental Physical Constants

Reproducibility code for the paper *Geometric Conjecture for the Origin of Fundamental Physical Constants from a Discrete Recursive Geometric Framework*.

## Environment Compatibility
- **Python 3.8+**: V1, V2, V3, V4, V6 (requires numpy/scipy)
- **SageMath 9.0+**: All scripts (V1–V6), **required for V5** (polytope combinatorics)

&gt; **Note**: V5 uses SageMath native `polytopes` module; run in SageMath only.

## Script List (Appendix G)

| Script | Description | Key Output |
|--------|-------------|------------|
| `V1_spectral_recursion.py` | Heat kernel self-similarity & spectral recursion | $\text{Spec}(\Delta_{N+1}) = \phi^2\text{Spec}(\Delta_N) \sqcup \phi^{-2}\text{Spec}(\Delta_N)$ |
| `V2_entropy_convergence.py` | Information loss rate $\delta_N$ & critical depth | $N_c = 7$, $\delta_7 &lt; 10^{-6}$ |
| `V3_mass_ratio.py` | Proton-electron mass ratio geometric factors | $m_p/m_e \approx 1835.95$ |
| `V4_fine_structure.py` | Inverse fine-structure constant $\alpha^{-1}$ series | $\alpha^{-1} = 137.0359991(7)$ |
| `V5_edge_count.sage` | 120-cell/600-cell Poincaré duality & edge ratio | $E_{120}/E_{600} = 5/3$ |
| `V6_neutrino_hierarchy.py` | **Normal hierarchy prediction** (rigid) vs **mass scale** (phenomenological) | Mass ratio $1:\phi:\phi^2$; Example values $0.01, 0.0162, 0.0262$ eV |

## Important Note on V6 (Neutrino Hierarchy)

**Critical distinction**: V6 outputs must be interpreted carefully:

1. **Geometrically Rigid Predictions** (independent of any free parameters):
   - Normal hierarchy: $m_1 &lt; m_2 &lt; m_3$
   - Mass ratio: $1 : \phi : \phi^2$ (where $\phi = (1+\sqrt{5})/2$)

2. **Phenomenological Input** (example only, not from first principles):
   - Absolute mass scale ($0.01$ eV in the example) is chosen to satisfy cosmological bound $\sum m_i &lt; 0.12$ eV
   - Changing this scale does **not** affect the mass ratio prediction

3. **Current Limitation**:
   - Mass-squared differences differ from experimental values by factors of 2-6 (see output)
   - Precise matching requires PMNS matrix implementation (future work)

4. **Falsifiability**:
   - If JUNO (2028) or DUNE confirms **inverted hierarchy** ($m_3 &lt; m_1 &lt; m_2$), the framework is invalidated regardless of absolute mass values

## Usage

### Python (V1–V4, V6)
```bash
pip install numpy scipy
python V1_spectral_recursion.py
python V6_neutrino_hierarchy.py  # Note: Check output distinction between rigid ratio vs example scale
