import sympy as sp
print("TWO DIFFERENT CONSTRAINTS — they give different answers, and both matter")
print("  (P) POSITIONS  : the wheel's 2p positions embed in the tuning  <=>  2p | N")
print("  (S) SYMMETRY   : the wheel's group Z/(p-1) acts on the tuning  <=>  (p-1) | N")
print()
ps=[p for p in sp.primerange(3,120)]
def usable(N,cond):
    return [p for p in ps if cond(p,N)]
tunings=[(12,"Western 12-TET"),(24,"Turkish notation (24 named pitches)"),
         (53,"Turkish AEU comma grid"),(60,"60-fold"),(72,"72-fold"),(120,"120-fold")]
print(f"{'N':>5}  {'tuning':32s} {'(P) positions  2p|N':>28s} {'(S) symmetry  (p-1)|N':>30s}")
for N,name in tunings:
    up=usable(N,lambda p,N: N%(2*p)==0)
    us=usable(N,lambda p,N: N%(p-1)==0)
    print(f"{N:>5}  {name:32s} {str([2*p for p in up]):>28s} {str([2*p for p in us]):>30s}")
print()
print("NO COMMA — just intonation (exact ratios, no equal temperament)")
print("  the interval group is Q^+ / 2^Z, a FREE ABELIAN group on the primes 3,5,7,... ")
print("  a finite cyclic group Z/n embeds in a free abelian group only when n = 1")
print("  so under (S) the condition is p-1 = 1, i.e. p = 2 — NO odd prime works")
print("  but under (P) there is no modulus at all: infinitely many rationals, so EVERY wheel fits")
print()
print("  => just intonation: (P) admits every base, (S) admits none.")
print("  => equal temperament is what makes a finite symmetry possible at all.")
print()
print("BASE 6 UNDER 24 PITCHES: is it the only one?")
for N in (12,24):
    up=[2*p for p in ps if N%(2*p)==0]
    print(f"  N={N}: (P) usable bases = {up}   -> base 6 {'is the ONLY one' if up==[6] else 'is not alone'}")
print()
print("the full position table for the first members of the 2p family:")
print(f"{'base 2p':>8}", "".join(f"{N:>7}" for N in (6,10,12,14,22,24,26,30,34,38,60,72)))
for W in (6,10,14,22,26,34,38,46,58):
    row=""
    for N in (6,10,12,14,22,24,26,30,34,38,60,72):
        row+=f"{'2p|N':>7}" if N%W==0 else f"{'-':>7}"
    print(f"{W:>8}",row)
