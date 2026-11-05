import numpy as np, math, time
# ---- Theorem D: the candidate stream's own gap structure
def wheel_gaps(W):
    C=[r for r in range(1,W) if math.gcd(r,W)==1]
    g=[(C[(i+1)%len(C)]-C[i])%W for i in range(len(C))]
    return C,g
print("the candidate stream on each wheel: which gap values occur, and their beams")
for W in (30,210,2310,30030):
    C,g=wheel_gaps(W)
    gs=sorted(set(g)); beams=sorted({x%10 for x in gs})
    print(f"  W={W:6d}: {len(C):5d} residues, {len(gs)} gap values {gs[:12]}"
          f"{'...' if len(gs)>12 else ''}")
    print(f"           beams used: {beams}")
print("\nso on the 30-wheel only beams 2,4,6 occur; beams 0 and 8 first appear at the 210-wheel.")
C,g=wheel_gaps(30)
print("30-wheel gap cycle in order:",g)
print("  = beams",[x%10 for x in g])

# ---- beam-stepping test (no gcd calls): step by the beam cycle
CYC0=wheel_gaps(30)[1]
CYC=np.array(CYC0[1:]+CYC0[:1],dtype=np.int64)   # rotate to start at 7
print('cycle starting at 7:',CYC.tolist())
def ej_test_beam(n):
    if n<2: return ("composite","n<2",0)
    if n in (2,3,5): return ("prime",None,0)
    if n%10 not in (1,3,7,9): return ("composite","digit",0)
    if n%3==0: return ("composite","3",0)
    if n%5==0: return ("composite","5",0)
    lim=math.isqrt(n); m=7; i=0; div=0
    while m<=lim:
        div+=1
        if n%m==0: return ("composite",m,div)
        m+=int(CYC[i%8]); i+=1
    return ("prime",None,div)
def ej_test_gcd(n):
    if n<2: return ("composite","n<2",0)
    if n in (2,3,5): return ("prime",None,0)
    if n%10 not in (1,3,7,9): return ("composite","digit",0)
    if n%3==0: return ("composite","3",0)
    if n%5==0: return ("composite","5",0)
    lim=math.isqrt(n); div=0
    for m in range(7,lim+1):
        if m%2==0 or m%3==0 or m%5==0: continue
        div+=1
        if n%m==0: return ("composite",m,div)
    return ("prime",None,div)
N=1_200_000
sieve=np.ones(N+1,bool); sieve[:2]=False
for i in range(2,int(N**0.5)+1):
    if sieve[i]: sieve[i*i::i]=False
bad=0
t0=time.time()
for n in range(7,200001):
    v,_,_=ej_test_beam(n)
    if (v=="prime")!=bool(sieve[n]): bad+=1
t1=time.time()
print(f"\nbeam-stepping test, exhaustive 7..200000: {bad} errors  ({t1-t0:.2f}s)")
bad2=sum(1 for n in range(7,200001) if (ej_test_beam(n)[0]=="prime")!=bool(sieve[n]))
bad3=sum(1 for n in range(7,200001) if (ej_test_gcd(n)[0]=="prime")!=bool(sieve[n]))
print(f"  gcd version: {bad3} errors")
agree=sum(1 for n in range(7,200001) if ej_test_beam(n)[0]==ej_test_gcd(n)[0])
print(f"  the two versions agree on {agree}/199994 numbers")
# benchmark on tough cases: primes near 1e8 (full loop)
import random; random.seed(1); primes=[p for p in range(10**8-20000,10**8) if sieve[p] ] if False else []
t0=time.time()
for _ in range(3000):
    n=random.randint(10**7,10**8); ej_test_beam(n)
t1=time.time()
for _ in range(3000):
    n=random.randint(10**7,10**8); ej_test_gcd(n)
t2=time.time()
print(f"  3000 random n<=1e8: beam {t1-t0:.2f}s vs gcd {t2-t1:.2f}s "
      f"({(t2-t1)/(t1-t0):.2f}x faster)")
