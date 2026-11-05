import numpy as np, itertools
subsets=[frozenset(s) for k in range(6) for s in itertools.combinations(range(5),k)]
S=[(c,U) for c in range(5) for U in subsets if {c,(c+1)%5}<=U]
idx={s:i for i,s in enumerate(S)}
T=np.zeros((len(S),len(S)))
for (c,U) in S:
    for step in range(5):
        c2=(c+step)%5; U2=frozenset(U|{c2,(c2+1)%5})
        if len(U2)<=4: T[idx[(c,U)],idx[(c2,U2)]]+=1
v=np.zeros(len(S)); v[idx[(0,frozenset({0,1}))]]=1
print("admissible words by transfer matrix")
print(" n |   a_n | 3^(n+1)-2^(n+1) | match")
a=[]
for n in range(1,11):
    v=v@T; c=int(round(v.sum())); a.append(c)
    print(f"{n:2d} | {c:5d} | {3**(n+1)-2**(n+1):15d} | {c==3**(n+1)-2**(n+1)}")
print("recurrence a_n = 3a_(n-1) + 2^n :")
for n in range(2,11):
    print(f"  n={n}: {3*a[n-2]}+{2**n}={3*a[n-2]+2**n} vs {a[n-1]} {'OK' if 3*a[n-2]+2**n==a[n-1] else 'FAIL'}")
print("real eigenvalues of the restricted matrix:",
      sorted({round(x.real,6) for x in np.linalg.eigvals(T) if abs(x.imag)<1e-8},reverse=True)[:6])
