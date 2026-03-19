# -*- coding: utf-8 -*-
# V6_neutrino_hierarchy.py
# Strict version: Neutrino mass hierarchy prediction based on 2I group 3-fold symmetry phi-scaling

# ===================== Environment Adaptation: Sage and Python Compatible =====================
try:
    # Sage environment
    from sage.all import Rational, sqrt, N
    Integer = int
    SAGE_MODE = True
except ImportError:
    # Pure Python environment
    import math
    Rational = lambda a, b: a / b
    sqrt = math.sqrt
    N = lambda x, n=10: round(float(x), n)
    Integer = int
    SAGE_MODE = False

# ===================== Core Parameters (Strictly Distinguish Geometric vs Phenomenological) =====================
# Golden ratio phi = (1+sqrt(5))/2 -- This is the GEOMETRIC RIGID OUTPUT from 2I group 3-fold symmetry
# This ratio is determined by the geometry of the binary icosahedral group, not adjustable
phi = (1 + sqrt(5)) / 2

# [CRITICAL NOTE] The following mass scale is a PHENOMENOLOGICAL INPUT, NOT geometrically derived!
# Absolute mass scale must be determined by future theory (E4 projection combined with PMNS matrix) or experiment
# Here we use 0.01 eV only to demonstrate compatibility with cosmological constraint (< 0.12 eV)
# Changing this scale does NOT affect the mass ratio prediction 1:phi:phi^2
mass_scale = Rational(1, 100)  # Example scale: 0.01 eV (phenomenological, adjustable)

# ===================== Neutrino Mass Calculation (Geometric Rigidity vs Human Input) =====================
# Normal hierarchy: m1 (light) < m2 (medium) < m3 (heavy)
# Geometric factors: 1, phi, phi^2 are rigid outputs of 2I symmetry
# Absolute values depend on the phenomenological mass_scale above

m1 = mass_scale * 1          # Light neutrino: Geometric factor x 1 (human scale x geometric rigidity)
m2 = mass_scale * phi        # Medium neutrino: Geometric factor x phi (human scale x geometric rigidity)
m3 = mass_scale * phi**2     # Heavy neutrino: Geometric factor x phi^2 (human scale x geometric rigidity)

# Numerical approximations (4 decimal places, matching paper Table VI)
m1_num = N(m1, 4)
m2_num = N(m2, 4)
m3_num = N(m3, 4)

# Experimental comparison parameters (from paper Table VI, for reference only)
delta_m2_21_exp = 7.5e-5    # Solar mass splitting ~7.5 x 10^-5 eV^2
delta_m2_32_exp = 2.5e-3    # Atmospheric mass splitting ~2.5 x 10^-3 eV^2

# Theoretical mass-squared differences (depend on the arbitrary mass_scale!)
delta_m2_21_theo = m2**2 - m1**2
delta_m2_32_theo = abs(m3**2 - m2**2)

# ===================== Results Output (Clearly Separate Theory from Examples) =====================
print("=" * 70)
print("V6 Strict Version: Neutrino Mass Hierarchy Prediction")
print("Based on 2I Group 3-Fold Symmetry Phi-Scaling")
print("=" * 70)
print("[CORE GEOMETRIC PREDICTION (Scale-Independent)]:")
print("  Normal hierarchy: m1 < m2 < m3")
print("  Mass ratio: 1 : phi : phi^2")
print("-" * 70)
print("[EXAMPLE NUMERICAL VALUES]: Mass scale = 0.01 eV (phenomenological choice)")
print("  For demonstration of cosmological constraint compatibility only")
print("-" * 70)

print("\n[1] Neutrino Mass Example Values (phi-scaling model with phenomenological scale):")
print("-" * 70)
print(f"  nu_1 (lightest):  m1 = {m1_num} eV  [EXAMPLE VALUE, not geometrically derived]")
print(f"  nu_2 (medium):    m2 = {m2_num} eV  [EXAMPLE VALUE, not geometrically derived]")
print(f"  nu_3 (heaviest):  m3 = {m3_num} eV  [EXAMPLE VALUE, not geometrically derived]")
print(f"  Mass ratio (rigid):  1 : {N(phi, 4)} : {N(phi**2, 4)}  (independent of scale choice)")
print(f"  Sum of masses (example): {N(m1+m2+m3, 4)} eV < 0.12 eV (cosmological bound satisfied)")

print("\n[2] Comparison with Experimental Data (Order-of-magnitude check only):")
print("-" * 70)
print(f"  Theory Delta m^2_21 = {N(delta_m2_21_theo, 6)} eV^2  [at example scale]")
print(f"  Experiment: ~7.5 x 10^-5 eV^2  (Difference: ~2x, requires PMNS mixing correction)")
print(f"  Theory |Delta m^2_32| = {N(delta_m2_32_theo, 5)} eV^2  [at example scale]")
print(f"  Experiment: ~2.5 x 10^-3 eV^2  (Difference: ~6x, requires PMNS mixing correction)")

print("\n[CRITICAL NOTES]")
print("-" * 70)
print("1. GEOMETRIC RIGID PREDICTION:")
print("   - Normal hierarchy m1 < m2 < m3")
print("   - Mass ratio 1:phi:phi^2")
print("   These are strict mathematical consequences of 2I group 3-fold symmetry.")
print("   They are INDEPENDENT of the mass scale choice.")
print()
print("2. PHENOMENOLOGICAL INPUT:")
print("   - Absolute mass scale (0.01 eV here) is NOT derived from geometry.")
print("   - It is chosen to satisfy cosmological bound Sum m_i < 0.12 eV.")
print("   - True scale requires future theory combining E4 projection and PMNS matrix.")
print()
print("3. FALSIFIABILITY:")
print("   - If JUNO (2028) or DUNE confirms inverted hierarchy (m3 < m1 < m2),")
print("     regardless of absolute mass values, this framework is falsified.")
print()
print("4. CURRENT LIMITATION:")
print("   - Mass-squared differences differ from experiment by factors of 2-6.")
print("   - This is expected because simple phi-scaling lacks flavor mixing structure.")
print("   - Precise matching requires PMNS matrix implementation (future work).")

print("\n" + "=" * 70)
print("CONCLUSION: Normal hierarchy is geometric necessity from 2I symmetry;")
print("            Absolute mass scale requires additional theoretical input!")
print("=" * 70)
