"""EJ test: the base key as a primality filter, with wheel-accelerated trial division."""
import numpy as np, random, math
N=1_200_000
sieve=np.ones(N+1,bool); sieve[:2]=False
for i in range(2,int(N**0.5)+1):
    if sieve[i]: sieve[i*i::i]=False
C30=[r for r in range(1,30) if math.gcd(r,30)==1]
C30=[r for r in C30 if r>=7]                       # 7,11,13,17,19,23,29
def ej_test(n):
    """(verdict, certificate, trial divisions) — the EJ test."""
    if n<2: return ("composite","n<2",0)
    if n in (2,3,5): return ("prime",None,0)
    d=n%10
    if d not in (1,3,7,9): return ("composite",f"last digit {d}",0)
    if n%3==0: return ("composite","3 divides",0)
    if n%5==0: return ("composite","5 divides",0)
    lim=int(math.isqrt(n)); div=0
    for m in range(7,lim+1):
        if m%2==0 or m%3==0 or m%5==0: continue      # residues coprime to 30
        div+=1
        if n%m==0: return ("composite",f"{m} divides",div)
    return ("prime",None,div)

# --- exhaustive check
bad=0; tot=0; divs=0; divs_naive=0
for n in range(7,200001):
    v,c,d=ej_test(n); tot+=1; divs+=d
    naive=sum(1 for m in range(2,int(math.isqrt(n))+1) if n%m==0) if n>3 else 0
    divs_naive+= int(math.isqrt(n))-1 if n>3 else 0
    if (v=="prime")!=bool(sieve[n]): bad+=1; print("  FAIL",n,v)
print(f"exhaustive 7..200000: {tot} numbers, {bad} errors")
print(f"  trial divisions: EJ test {divs:,}   naive (all m<=sqrt n) {divs_naive:,}   "
      f"ratio {divs/divs_naive:.4f}  (speed-up x{divs_naive/divs:.2f})")
# --- random large
random.seed(7); bad=0; tested=0
for _ in range(3000):
    n=random.randint(200001,10**8); tested+=1
    v,c,d=ej_test(n)
    ok=(v=="prime")
    if ok!=bool(sieve[n]) if n<=N else False: bad+=1
print(f"random 3000 in [2e5,1e8]: {bad} errors against the sieve (for n<=1.2e6)")
# --- the range theorem check: key alone exact below 49
print("\nthe key alone (steps 1-2 only) is exact for n < 49:")
bad=[]
for n in range(7,49):
    keyonly = (n%10 in (1,3,7,9)) and n%3 and n%5
    if keyonly != bool(sieve[n]): bad.append(n)
print("  disagreements below 49:",bad if bad else "none")
first=[n for n in range(7,2000) if (n%10 in (1,3,7,9)) and n%3 and n%5 and not sieve[n]][0]
print("  first composite passing the key alone:",first,"=",int(math.isqrt(first)),"^2")
# --- twin version
print("\ntwin test on n <= 200000: n and n+2 both prime <-> n=5 mod 6 and no divisor in C30")
bad=0; hits=0
for n in range(7,200000):
    if n%6!=5: continue
    if (n%3==0) or (n%5==0): continue
    if (n+2)%5==0 and (n+2)>5: ok=False
    else:
        lim=int(math.isqrt(n+2))
        ok=all(n%m and (n+2)%m for m in range(7,lim+1) if math.gcd(m,30)==1)
    hits+=1
    if ok!=bool(sieve[n] and sieve[n+2]): bad+=1; print("  FAIL",n)
print(f"  twin starts tested: {hits}, errors: {bad}")
print(f"  twin residue class: 1 of 6 (n = 5 mod 6) vs 4 of 10 for a single prime")
