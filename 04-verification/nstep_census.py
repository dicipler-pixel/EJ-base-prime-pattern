import numpy as np, itertools
N=86_100_000
sieve=np.ones(N+1,bool); sieve[:2]=False
for i in range(2,int(N**0.5)+1):
    if sieve[i]: sieve[i*i::i]=False
P=np.nonzero(sieve)[0]; P4=P[P>=3]; a=P4[sieve[P4+2]].astype(np.int64)
d=np.diff(a)[2:]                       # skip the seed gap d_1=2
U=[0,2,4,6,8]; RES30={0:0,2:12,4:24,6:6,8:18}
print("RESIDUE-LEVEL ADMISSIBILITY TEST")
print("  a word of residues r_1..r_n (mod 10) fixes each d_i mod 30, because d_i = 0 mod 6:")
for r in U: print(f"    r={r} -> d = {RES30[r]} mod 30")
def admissible(w):
    D=0; S={0,2}
    for r in w:
        D+=RES30[r]; S|={D%30,(D+2)%30}
    for q in (2,3,5):
        if len({s%q for s in S})==q: return False
    return True
print("\n n | reachable | predicted admissible | agree | reachable-but-predicted-no | predicted-yes-but-never-seen")
for n in range(1,6):
    if n>len(d): break
    word=[tuple(int(x) for x in d[i:i+n]%10) for i in range(len(d)-n+1)]
    seen=set(word); allw=set(itertools.product(U,repeat=n))
    adm={w for w in allw if admissible(w)}
    extra=seen-adm; missing=adm-seen
    print(f" {n} | {len(seen):9d} | {len(adm):20d} | {str(seen==adm):5s} | {len(extra):26d} | {len(missing):27d}")
    if extra and n<=3: print("      reachable but predicted inadmissible:",sorted(extra)[:6])
    if missing and n<=3: print("      predicted but never seen:",sorted(missing)[:6])
print("\n total possible words: 5^n ; the admissible count is the exact prediction")
for n in range(1,6):
    print(f"   n={n}: possible {5**n:5d}, admissible {sum(1 for w in itertools.product(U,repeat=n) if admissible(w)):5d}"
          f"  ({100*sum(1 for w in itertools.product(U,repeat=n) if admissible(w))/5**n:.1f}%)")
