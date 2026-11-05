import math, sympy as sp
from sympy import totient, divisors, cyclotomic_poly
def classes(W):
    units=[u for u in range(W) if math.gcd(u,W)==1]
    orbs={}
    for x in range(W):
        o=frozenset({(u*x)%W for u in units})
        orbs.setdefault(o,[]).append(x)
    return units, orbs
print("THE GENERAL THEOREM: orbits of (Z/W)* acting on Z/W  =  the divisor classes")
print("  orbit of x  =  {y : gcd(y,W) = gcd(x,W)},  i.e. one class per divisor d of W\n")
for W in (6,8,10,12,14,30):
    units,orbs=classes(W)
    ds=sorted(set(W//math.gcd(x,W) for x in range(W)))
    print(f"W = {W:3d}:  phi={len(units):2d}   tau(W)={len(sp.divisors(W)):2d}   orbits={len(orbs):2d}"
          f"   match: {len(orbs)==len(sp.divisors(W))}")
    for o in sorted(orbs,key=lambda t:(len(t),sorted(t)[0])):
        d=W//math.gcd(sorted(o)[0],W)
        cp=sp.cyclotomic_poly(d,sp.Symbol('x'))
        print(f"     d={d:3d}  size {len(o):2d}  {str(sorted(o)):34s} primitive {d}th roots,  Phi_{d} = {cp}")
    print()
print("="*74)
print("WHAT BREAKS FOR THE SIEVE'S OWN AUTOMORPHISM GROUP")
print("="*74)
for W in (6,10,30):
    units,orbs=classes(W)
    K=sorted(set(u for u in units))
    print(f"W={W}: the action x -> ux permutes the units, so the SET of survivors is fixed.")
    print(f"      survivors {K[:8]}{'...' if len(K)>8 else ''}  -> the gap sequence is UNCHANGED.")
print("\n  so the automorphism group classifies RESIDUES but is invisible to GAPS.")
print("  for the colour wheel the classes ARE the colours, so the derivation produces content.")
print("  for the sieve the classes are divisor classes and the gaps are invariant -> nothing new.")
print("\n  the clean 1+1+4+4 colour split needs tau(W)=4, i.e. W = p*q or p^3:")
print("   ", [W for W in range(6,60) if len(sp.divisors(W))==4])
