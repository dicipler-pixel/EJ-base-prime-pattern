import itertools
U=[0,1,2,3,4]
t0={0,1,2}; t1={0,1,4}; t2={0,3,4}
R2={0:0,1:2,2:4,3:6,4:8}          # cycle index -> her beam digit
def classes(n):
    c={'A':0,'B':0,'C':0,'AB':0,'BC':0,'AC':0,'ABC':0}
    for w in itertools.product(U,repeat=n):
        img=set(w)|{0}
        a=img<=t0; b=img<=t1; c3=img<=t2
        if a and b and c3: c['ABC']+=1
        elif a and b: c['AB']+=1
        elif b and c3: c['BC']+=1
        elif a and c3: c['AC']+=1
        elif a: c['A']+=1
        elif b: c['B']+=1
        elif c3: c['C']+=1
    return c
print("the three admissible triples in HER beam coordinates (beam = 2 * cycle index):")
for nm,t in [('t0',t0),('t1',t1),('t2',t2)]:
    print(f"  {nm} = cycle {sorted(t)} -> beams {sorted(R2[x] for x in t)}")
print("\nclass sizes (Venn regions of the three triples):")
print(f"{'n':>2} {'A':>6} {'B':>6} {'C':>6} {'AB':>5} {'BC':>5} {'AC':>3} {'ABC':>4} {'total':>7} {'3^(n+1)-2^(n+1)':>18}")
for n in range(1,7):
    c=classes(n); tot=sum(c.values())
    print(f"{n:>2} {c['A']:>6} {c['B']:>6} {c['C']:>6} {c['AB']:>5} {c['BC']:>5} {c['AC']:>3} {c['ABC']:>4} "
          f"{tot:>7} {3**(n+1)-2**(n+1):>18}")
print("\nclosed forms:")
print("  A  = 3^n - 2^n            (beams {0,2,4})")
print("  B  = 3^n - 2^(n+1) + 1    (beams {0,2,8})")
print("  C  = 3^n - 2^n            (beams {0,6,8})")
print("  AB = 2^n - 1              (beams {0,2})")
print("  BC = 2^n - 1              (beams {0,8})")
print("  AC = 0                    (beams {0} alone: impossible)")
print("  ABC= 1                    (the constant word)")
for n in range(1,7):
    f=(3**n-2**n)+(3**n-2**(n+1)+1)+(3**n-2**n)+(2**n-1)+(2**n-1)+0+1
    print(f"  n={n}: sum of forms = {f}  vs 3^(n+1)-2^(n+1) = {3**(n+1)-2**(n+1)}  {'OK' if f==3**(n+1)-2**(n+1) else 'FAIL'}")
