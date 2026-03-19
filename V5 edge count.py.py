# -*- coding: utf-8 -*-
# V5_edge_count.py
# 120-cell / 600-cell combinatorial verification
# Compatible with Python 3.6+ and SageMath 9.0+

# ===================== Environment Detection =====================
try:
    from sage.all import Rational
    HAS_SAGE = True
except ImportError:
    from fractions import Fraction
    Rational = Fraction
    HAS_SAGE = False

# ===================== Mathematical Data (Hardcoded) =====================
# From Coxeter's "Regular Polytopes" - established facts

C120_DATA = {
    'V': 600,      # vertices
    'E': 1200,     # edges (factor 10 = 2×5 for proton)
    'F': 720,      # faces (pentagons)
    'C': 120       # cells (dodecahedra)
}

C600_DATA = {
    'V': 120,      # vertices
    'E': 720,      # edges (factor 7 = 2+5 = N_c for electron)
    'F': 1200,     # faces (triangles)
    'C': 600       # cells (tetrahedra)
}

# ===================== Main Verification =====================
def main():
    print("=" * 70)
    print("V5: 120-cell / 600-cell Combinatorial Verification")
    print(f"Running in: {'SageMath' if HAS_SAGE else 'Pure Python'} mode")
    print("=" * 70)
    
    # Unpack data
    V120, E120, F120, C120 = C120_DATA['V'], C120_DATA['E'], C120_DATA['F'], C120_DATA['C']
    V600, E600, F600, C600 = C600_DATA['V'], C600_DATA['E'], C600_DATA['F'], C600_DATA['C']
    
    print(f"\n[1] Combinatorial Data:")
    print(f"    120-cell {{5,3,3}}: V={V120}, E={E120}, F={F120} (pent), C={C120}")
    print(f"    600-cell {{3,3,5}}: V={V600}, E={E600}, F={F600} (tri), C={C600}")
    
    # Poincaré Duality: V(120)↔C(600), C(120)↔V(600)
    print(f"\n[2] Poincaré Duality Verification (V ↔ C):")
    check1 = (V120 == C600)
    check2 = (C120 == V600)
    print(f"    V(120)={V120} = C(600)={C600}? {'✓ PASS' if check1 else '✗ FAIL'}")
    print(f"    C(120)={C120} = V(600)={V600}? {'✓ PASS' if check2 else '✗ FAIL'}")
    
    # Edge ratio 5/3
    print(f"\n[3] CRITICAL: Edge Count Ratio:")
    ratio = Rational(E120, E600)  # 1200/720 = 5/3
    target = Rational(5, 3)
    print(f"    E(120)/E(600) = {E120}/{E600} = {ratio}")
    print(f"    As decimal: {float(ratio):.10f}")
    print(f"    Target 5/3:  {float(target):.10f}")
    match = (ratio == target)
    print(f"    Exact match: {'✓ PASS (Exact 5/3)' if match else '✗ FAIL'}")
    print(f"    Physics: 5-fold (pentagon) vs 3-fold (triangle) symmetry!")
    
    # Euler Characteristic
    print(f"\n[4] Euler Characteristic (χ = V - E + F - C):")
    chi_120 = V120 - E120 + F120 - C120
    chi_600 = V600 - E600 + F600 - C600
    print(f"    χ(120-cell) = {V120}-{E120}+{F120}-{C120} = {chi_120}")
    print(f"    χ(600-cell) = {V600}-{E600}+{F600}-{C600} = {chi_600}")
    euler_ok = (chi_120 == 0) and (chi_600 == 0)
    print(f"    Both zero (S^4 topology): {'✓ PASS' if euler_ok else '✗ FAIL'}")
    
    # Symmetry
    print(f"\n[5] Symmetry Group:")
    print(f"    Binary icosahedral |2I| = 120 = 2³ × 3 × 5")
    
    # Sage optional check
    if HAS_SAGE:
        try:
            from sage.geometry.polyhedron.library import polytopes
            print(f"\n[6] SageMath Polytope Verification:")
            P120 = polytopes.one_hundred_twenty_cell()
            f120 = list(P120.f_vector())
            print(f"    Sage f-vector: {f120}")
            sage_match = (f120 == [V120, E120, F120, C120])
            print(f"    Matches data: {'✓ PASS' if sage_match else '✗ FAIL'}")
        except Exception as e:
            print(f"\n[6] Sage check skipped: {e}")
    
    # Summary
    print("\n" + "=" * 70)
    print("SUMMARY for Mass Ratio Formula:")
    print(f"    C_p (proton)  = 2 × 5 = 10  [non-Abelian, 120-cell]")
    print(f"    C_e (electron)= 2 + 5 = 7   [Abelian, 600-cell, N_c]")
    print(f"    Ratio 10/7 from: product vs sum of (2,5) symmetries")
    print("=" * 70)

if __name__ == "__main__":
    main()
