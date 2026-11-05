import math, sympy as sp
def check(W):
    units=[u for u in range(W) if math.gcd(u,W)==1]
    orbs={}
    for x in range(W):
        orbs.setdefault(frozenset({(u*x)%W for u in units}),set()).add(x)
    sizes=sorted(len(o) for o in orbs)
    cyc=any(len({pow(u,k,W) for k in range(len(units))})==len(units) for u in units)
    img={(2*u)%W for u in units}
    one=any(set(img)<=o for o in orbs)
    comp=sorted({frozenset({x,(W-x)%W}) for x in range(W)},key=lambda t:(len(t),min(t)))
    fixed=[sorted(o)[0] for o in comp if len(o)==1]
    return dict(W=W,phi=len(units),tau=len(orbs),sizes=sizes,cyc=cyc,
                one=one,ncomp=len(comp),fixed=fixed)
print("p=17 and p=19: the third and fourth members beyond 14")
print(f"{'W':>4} {'p':>3} {'phi':>4} {'tau':>4} {'sizes':>22} {'cyclic':>7} {'2u one class':>13} {'neutral':>10} {'verdict':>9}")
for W in (6,10,14,22,26,34,38):
    s=check(W); p=W//2
    ok=(s['tau']==4 and s['sizes']==[1,1,p-1,p-1] and s['cyc'] and s['one'])
    print(f"{W:>4} {p:>3} {s['phi']:>4} {s['tau']:>4} {str(s['sizes']):>22} {str(s['cyc']):>7} "
          f"{str(s['one']):>13} {str(s['fixed']):>10} {'VIABLE' if ok else 'FAIL':>9}")
print("\nTHE THREE-LINE PROOF for every odd prime p (no enumeration needed):")
print("  (i)  divisors of 2p are 1,2,p,2p, so phi = 1,1,p-1,p-1 -> tau=4 and two families of size p-1")
print("  (ii) (Z/2p)* = (Z/p)* by CRT, and (Z/p)* is CYCLIC of order p-1 (standard)")
print("  (iii) -1 is a unit, so the complement is an automorphism; the neutral is p = W/2")
print("        and 2*(units) is the class of the p-th roots, bijectively")
print("  => the 2p family is settled for ALL odd primes p.")
print("\n"+"="*74)
print("DOES A TUNING LADDER CONSTRAIN WHICH p ARE USABLE?")
print("  if a music system divides the octave into N equal steps (Z/N), a 2p wheel can sit inside")
print("  it only if its symmetry group Z/(p-1) is a subgroup of Z/N, i.e. (p-1) | N.")
def usable(N,name):
    ps=[p for p in sp.primerange(3,200) if N%(p-1)==0]
    print(f"  N={N:3d} ({name:28s}): p = {ps}  -> bases {[2*p for p in ps]}")
    return ps
usable(12,"Western 12-TET")
usable(24,"Turkish notation, 24 pitches")
usable(53,"Turkish AEU comma system, 53")
usable(60,"60-fold")
usable(72,"72-fold (Hindustani 22 shruti is separate)")
print("\n  key result: under a 53-comma system NO odd prime works (53 is prime, so p-1 in {1,53}).")
print("  under 24 pitches, exactly p = 3,5,7,13 survive -> bases 6, 10, 14, 26.")
print("  base 22 (p=11) needs N divisible by 10: fine for 60-fold, not for 12- or 24-fold.")
