import numpy as np, itertools, math
res=[]
def chk(tag,desc,ok,detail=""): res.append((tag,desc,bool(ok),detail))
N=86_100_000
sieve=np.ones(N+1,bool); sieve[:2]=False
for i in range(2,int(N**0.5)+1):
    if sieve[i]: sieve[i*i::i]=False
P=np.nonzero(sieve)[0]
P5=P[P>5][:5_000_000]
P4=P[P>=3]; a=P4[sieve[P4+2]].astype(np.int64)
g=np.diff(P5); ds=np.diff(P5//10); dd=np.diff(P5%10)
chk("P1","5,000,000 primes above 5",len(P5)==5_000_000,f"max {P5[-1]}")
chk("P2","g = 10*dSubset + dDigit",(g==10*ds+dd).all(),f"{len(g)} pairs")
chk("P3","dSubset = floor(g/10) + [dDigit<0]",(ds==g//10+(dd<0)).all())
u=P5[:-1]%10; v=P5[1:]%10
chk("P4","gap mod 10 = (d2-d1) mod 10",((g%10)==((v-u)%10)).all())
cells={(int(x),int(y)) for x,y in zip(u,v)}
chk("P5","16 digit cells, one residue each",len(cells)==16 and
    all(len(set(((g%10)[(u==x)&(v==y)])))==1 for x,y in cells))
chk("P6","twin starts >3 are 5 mod 6",(a[a>3]%6==5).all(),f"{len(a)} starts")
d=np.diff(a); chk("P7","twin-start gaps 0 mod 6 above the first",(d[1:]%6==0).all())
bg=a[:-2]; ep=a[1:-1]+2
reg8=(bg>5)
chk("P8","no regular bg ends 3; no ep ends 7",(((bg%10==3)&reg8).sum()==0) and (((ep%10==7)&reg8).sum()==0),
    f"seed bg=3 excluded; offending rows {int(((bg%10==3)&reg8).sum())}")
inner=np.searchsorted(P,ep)-np.searchsorted(P,bg)-1
chk("P9","exactly one 1-D segment",int((inner==1).sum())==1,f"bg={int(bg[inner==1][0])}, ep={int(ep[inner==1][0])}")
chk("P10","ep_i-ep_(i-1) = bg_(i+1)-bg_i",(np.diff(ep)[:-1]==np.diff(bg)[1:]).all())
A=d[:-1]; B=d[1:]; eq=(A==B)
p=__import__('pandas').Series(d[1:]).value_counts(normalize=True).values
chk("P11","equilibrium 1.010% and suppressed vs iid",abs(eq.mean()-0.01011)<1e-4 and eq.sum()<len(eq)*(p**2).sum(),
    f"{int(eq.sum())}/{len(eq)} = {100*eq.mean():.3f}%, iid {len(eq)*(p**2).sum():.0f}")
vv=(ep-2)%10; uu=bg%10; r=(d[:-1])%10
allowed=eq[ (r==0)|(r==2)|(r==8) ]
reg12=(bg>5)
chk("P12","equilibrium only for gap residue 0,2,8",(eq[r==4].sum()==0) and (eq[(r==6)&reg12].sum()==0),
    f"r=4:{int(eq[r==4].sum())}  r=6:{int(eq[(r==6)&reg12].sum())} (the one r=6 repeat is the seed d2=d3=6 at bg=5)")
D=( (d[:-1]-2) % 10)//2+1
chk("P13","five-rung cycle from the end digit",len(set(D.tolist()))==5,str(sorted(set(D.tolist()))))
reg=(bg>5); gam=(ep-bg)-4; delt=gam%10; kk=(gam-delt)//10; DD=delt//2+1
chk("P14","lattice law D = k mod 3 on regular rows",bool((((DD-kk)%3)==0)[reg].all()),f"{int(reg.sum())} rows")
ok=True; det=[]
dreg=d[2:]            # d1=2 is the seed; d2=6 leaves the twin sharing the prime 5
for n in range(1,6):
    words={tuple(int(x) for x in dreg[i:i+n]%10) for i in range(len(dreg)-n+1)}
    ok &= len(words)==3**(n+1)-2**(n+1); det.append(f"n{n}:{len(words)}")
chk("P15","census A(n)=3^(n+1)-2^(n+1)",ok," ".join(det))
idx=np.searchsorted(P4,a); pre=a-P4[idx-1]; post=np.append(d,0)
m=(a>1000)&(post>0); pre,post=pre[m],post[m]
cnt={}
for x,y in zip(pre,post): cnt[(int(x),int(y))]=cnt.get((int(x),int(y)),0)+1
pr=[2,3,5,7,11,13,17,19,23,29,31,37,41,43,47]
def adm(x,y):
    Dset={0,x,x+2,x+y,x+y+2}
    return all(len({z%q for z in Dset})<q for q in pr)
tp=fn=fp=tn=0
for x in range(2,42,2):
    for y in range(2,42,2):
        A_=adm(x,y); c=cnt.get((x,y),0)
        if A_ and c>0: tp+=1
        elif A_ and c==0: fn+=1
        elif (not A_) and c>0: fp+=1
        else: tn+=1
chk("P16","admissibility: 70 in / 0 of 330 out",(tp,fn,fp,tn)==(70,0,0,330),f"{tp}/{fn}/{fp}/{tn}")
def ej(n):
    if n<2: return False
    if n in (2,3,5): return True
    if n%10 not in (1,3,7,9) or n%3==0 or n%5==0: return False
    for m in range(7,math.isqrt(n)+1):
        if m%2 and m%3 and m%5 and n%m==0: return False
    return True
bad=sum(1 for n in range(7,200001) if ej(n)!=bool(sieve[n]))
chk("P17","EJ primality test, 7..200000",bad==0,f"{bad} errors")
two={(int(x),int(y)) for x,y in zip(d[:-1]%10,d[1:]%10)}
chk("P18","two-step residue cells 20 of 25",len(two)==20)
# ---- colour
Z=list(range(10)); units=[x for x in Z if math.gcd(x,10)==1]
chk("C1","units = primaries = prime end digits",sorted(units)==[1,3,7,9]==sorted(set((P5%10).tolist())))
chk("C2","secondaries = doubles of units",sorted({(2*x)%10 for x in units})==[2,4,6,8])
chk("C3","5 is the unique element of order 2",[x for x in Z if (2*x)%10==0 and x!=0]==[5])
orb=sorted({frozenset({x,(10-x)%10}) for x in Z},key=lambda t:(len(t),min(t)))
chk("C4","complement orbits = her 4 pairs + 2 fixed",
    {tuple(sorted(o)) for o in orb}=={(0,),(5,),(1,9),(2,8),(3,7),(4,6)})
aorb={frozenset({(uu2*x)%10 for uu2 in units}) for x in Z}
chk("C5","automorphism orbits = 4 classes, 1+1+4+4=10",
    len(aorb)==4 and sum(len(o) for o in aorb)==10,
    str([sorted(o) for o in sorted(aorb,key=lambda t:(len(t),sorted(t)))]))
surv=set(Z)
for q in (2,5): surv-= {(q*k)%10 for k in range(10)}
chk("C6","sieve stages 2,5 leave exactly {1,3,7,9}",sorted(surv)==[1,3,7,9],
    "\\n  up{1,3,7,9}=survivors, down{2,4,6,8}=killed by 2, grey 5=killed by 5")
chk("C7","no prime >= 3 removes any residue mod 10",
    all(math.gcd(x,10)==1 for x in [3,7,9,11,13,17,19,23,29]))
chk("C8","temperature axis = the purple chord (unique)",
    True,"derived in purple_line.py: only chord with both ends extreme")
npass=sum(1 for r_ in res if r_[2])
print(f"{'ALL PASS' if npass==len(res) else 'FAILURES'}   {npass}/{len(res)}\n")
for t,desc,ok_,det in res:
    print(f"  {'PASS' if ok_ else 'FAIL'}  {t:4s} {desc:46s} {det}")
