import math, sympy as sp
from collections import Counter
def structure(W):
    units=[u for u in range(W) if math.gcd(u,W)==1]
    U=set(units)
    orbs={}
    for x in range(W):
        orbs.setdefault(frozenset({(u*x)%W for u in units}),set()).add(x)
    sizes=sorted(len(o) for o in orbs)
    # complement
    comp=[frozenset({x,(W-x)%W}) for x in range(W)]
    comp=sorted(set(comp),key=lambda t:(len(t),min(t)))
    fixed=[sorted(o)[0] for o in comp if len(o)==1]
    # doubling: does 2*units land in ONE orbit?
    img={(2*u)%W for u in units}
    img_orbs={o for o in orbs if o<=set(img) or set(img)<=o}
    dbl_single=(len(img_orbs)==1)
    # group structure
    cyc = sp.nsimplify(0)==0 and bool(sp.number_theory.orders.n_order(2,W)>0) if False else None
    from sympy.combinatorics.named_groups import CyclicGroup
    import sympy.ntheory.residue_ntheory as rn
    return dict(W=W, phi=len(units), tau=len(orbs), sizes=sizes,
                ngroups=len(comp), fixed=fixed, dbl_single=dbl_single,
                dbl_img=sorted(img)[:8], units=units[:12])
def is_cyclic_units(W):
    units=[u for u in range(W) if math.gcd(u,W)==1]
    if len(units)<=1: return True
    # cyclic iff there is an element of order phi(W)
    return any(pow(u,len(units),W)==1 and len({pow(u,k,W) for k in range(len(units))})==len(units)
               for u in units)
print("FULL STRUCTURE TABLE  (not just the partition)")
print(f"{'W':>4} {'2p?':>4} {'phi':>4} {'tau':>4} {'class sizes':>18} {'units cyclic?':>13} {'#comp orbits':>13} {'fixed':>10} {'2*units one class?':>19}")
rows=[]
for W in (6,8,10,12,14,18,22,26,30):
    s=structure(W); cyc=is_cyclic_units(W)
    is2p = (W%2==0) and sp.isprime(W//2)
    s['cyc']=cyc; s['is2p']=is2p; rows.append(s)
    print(f"{W:>4} {str(is2p):>4} {s['phi']:>4} {s['tau']:>4} {str(s['sizes']):>18} "
          f"{str(cyc):>13} {s['ngroups']:>13} {str(s['fixed']):>10} {str(s['dbl_single']):>19}")
print("\nTHE TEST: a wheel is COLOUR-VIABLE when all five hold")
print("  (a) tau(W)=4          four classes: base, neutral, primaries, secondaries")
print("  (b) class sizes 1,1,p-1,p-1   exactly two families of equal size")
print("  (c) (Z/W)* cyclic     one generator for the symmetries")
print("  (d) W even            the neutral is a single element W/2")
print("  (e) 2*units in ONE class   doubling maps primaries onto secondaries")
print()
for s in rows:
    W=s['W']; sizes=s['sizes']
    ok = (s['tau']==4) and (len(sizes)==4 and sizes[0]==1 and sizes[1]==1 and sizes[2]==sizes[3]) \
         and s['cyc'] and (W%2==0) and s['dbl_single']
    fails=[]
    if s['tau']!=4: fails.append(f"tau={s['tau']}")
    if not(len(sizes)==4 and sizes[0]==1 and sizes[1]==1 and sizes[2]==sizes[3]): fails.append(f"sizes {sizes}")
    if not s['cyc']: fails.append("units not cyclic")
    if not s['dbl_single']: fails.append("2*units splits")
    print(f"  W={W:3d}: {'VIABLE' if ok else 'fails'}   {'none' if not fails else ', '.join(fails)}")
print("\nVIABLE SET:", [s['W'] for s in rows if (s['tau']==4 and s['sizes'][0]==1 and s['sizes'][1]==1
      and s['sizes'][2]==s['sizes'][3] and s['cyc'] and s['W']%2==0 and s['dbl_single'])])
print("\nanalytic reason: W = 2p (p odd prime) gives")
print("  divisors 1,2,p,2p -> class sizes phi = 1,1,p-1,p-1")
print("  (Z/2p)* = (Z/p)* is CYCLIC of order p-1")
print("  -1 is in (Z/2p)*, so complement is a symmetry")
print("  2*units = the (Z/2p)-class of the p-th roots, bijectively")
