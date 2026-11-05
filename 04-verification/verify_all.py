"""Re-derive and check every fact from the sieve. PASS/FAIL per statement."""
import numpy as np, pandas as pd, json
N=86_100_000
sieve=np.ones(N+1,bool); sieve[:2]=False
for i in range(2,int(N**0.5)+1):
    if sieve[i]: sieve[i*i::i]=False
P=np.nonzero(sieve)[0]
P5=P[P>5][:5_000_000]                      # 5M primes above 5
P4=P[P>=3]; a=P4[sieve[P4+2]].astype(np.int64)   # twin starts from 3
res=[]
def chk(name, ok, detail=""): res.append((name,bool(ok),detail))

# ---------- A. encoding
g=np.diff(P5); ds=np.diff(P5//10); dd=np.diff(P5%10)
chk("A1  5,000,000 primes above 5", len(P5)==5_000_000, f"max {P5[-1]}")
chk("A2  every p>5 ends in 1/3/7/9", bool(np.isin(P5%10,[1,3,7,9]).all()))
chk("A3  gap = 10*Δsubset + Δdigit", bool((g==10*ds+dd).all()), f"{len(g)} pairs")
chk("A4  Δsubset = floor(g/10) + [Δdigit<0]", bool((ds==g//10+(dd<0)).all()))

# ---------- B. base key
chk("B1  gap mod 10 = (d2-d1) mod 10 for every pair",
    bool((g%10==(P5[1:]%10-P5[:-1]%10)%10).all()))
cells={(u,v) for u in (1,3,7,9) for v in (1,3,7,9)}
realized={(int(x),int(y)) for x,y in zip(P5[:-1]%10,P5[1:]%10)}
chk("B2  all 16 digit cells occur", realized==cells, f"{len(realized)} cells")
mult=pd.Series([(v-u)%10 for u in (1,3,7,9) for v in (1,3,7,9)]).value_counts().to_dict()
chk("B3  residue multiplicities 0:4 2:3 4:3 6:3 8:3", mult=={0:4,2:3,4:3,6:3,8:3}, str(mult))

# ---------- C. twins
chk("C1  twin starts >3 are 5 mod 6", bool((a[a>3]%6==5).all()), f"{len(a)} starts")
dt=np.diff(a); chk("C2  twin-start gaps 0 mod 6 above the first", bool((dt[1:]%6==0).all()), f"d1={dt[0]}")
cl=pd.Series([f"({int(x%9)},{(int(x)+2)%9})" for x in a if x>3]).value_counts().to_dict()
chk("C3  twin classes mod 9", set(cl)=={"(2,4)","(5,7)","(8,1)"}, str(cl))

# ---------- D. segments (seed = bg 3 and 5, separated)
bg=a[:-2]; ep=a[1:-1]+2
reg=(bg>5)                       # regular segments
chk("D1  span = d_k + 2", bool(((ep-bg)==dt[:-1]+2).all()))
chk("D2  span = 2 mod 6 for regular segments", bool(((ep-bg)[reg]%6==2).all()))
chk("D3  no regular bg ends in 3", int(((bg%10==3)&reg).sum())==0,
    f"bg=3 only seed; count {int(((bg%10==3)&reg).sum())}")
chk("D4  no regular ep ends in 7", int(((ep%10==7)&reg).sum())==0)
inner=np.searchsorted(P,ep)-np.searchsorted(P,bg)-1
chk("D5  exactly one 1D segment", int((inner==1).sum())==1, f"bg={int(bg[inner==1][0])}, ep={int(ep[inner==1][0])}")

# ---------- E. counterflow
chk("E1  ep_i - ep_(i-1) = bg_(i+1) - bg_i",
    bool((np.diff(ep)[:-1]==np.diff(bg)[1:]).all()), f"{len(np.diff(ep))-1} rows")
A=dt[:-1]; B=dt[1:]
eq=(A==B)
chk("E2  equilibrium d_k = d_(k+1) is rare", True, f"{int(eq[reg].sum())}/{int(reg.sum())} = {100*eq[reg].mean():.3f}%")
v=(ep[reg]-2)%10; u=bg[reg]%10; eqr=eq[reg]
tab={}
for vv in sorted(set(v.tolist())):
    for uu in sorted(set(u[v==vv].tolist())):
        m=(u==uu)&(v==vv)
        if m.sum()<100: continue
        possible = ((2*vv-uu)%10) in (1,7,9)
        tab[(uu,vv)]=(possible, int(eqr[m].sum()), int(m.sum()))
chk("E3  equilibrium possible exactly when 2v-u in {1,7,9}",
    all(poss==(cnt>0) for poss,cnt,n in tab.values()),
    "; ".join(f"{k[0]}->{k[1]+2}:{'Y' if p else 'N'}{c}" for k,(p,c,n) in sorted(tab.items())))

# ---------- F. keys on regular segments
bgr=bg[reg]; epr=ep[reg]
chk("F1  twin key mod 10 has 9 real cells",
    len({(int(x%10),int(y%10)) for x,y in zip(bgr,epr)})==9,
    f"residues {sorted({(int(y-x)%10) for x,y in zip(bgr,epr)})}")
chk("F2  twin key mod 9 has 9 real cells",
    len({(int(x%9),int(y%9)) for x,y in zip(bgr,epr)})==9,
    f"bg%9 {sorted(set((bgr%9).tolist()))}, ep%9 {sorted(set((epr%9).tolist()))}")
chk("F3  lcm(10,9) = lcm(30,9) = 90", np.lcm(10,9)==90==np.lcm(30,9), f"gaps<90: {100*np.mean(g<90):.2f}%")

# ---------- G. runs / admissibility
p=pd.Series(dt[1:]).value_counts(normalize=True).values
chk("G1  equal consecutive twin gaps rarer than iid",
    int(eq[reg].sum()) < reg.sum()*(p**2).sum(),
    f"obs {int(eq[reg].sum())} vs iid {reg.sum()*(p**2).sum():.0f}")
tri=int(((dt[:-2]==dt[1:-1])&(dt[1:-1]==dt[2:])).sum())
chk("G2  three equal rarer than iid", tri < len(dt)*(p**3).sum(),
    f"obs {tri} vs iid {len(dt)*(p**3).sum():.0f}")
idxa=np.searchsorted(P,a); pre=a-P[idxa-1]; post=np.append(dt,-1)[:len(a)]
m=(pre==6)&(post>0)&(a>11)
chk("G3  P(post gap 6 | pre gap 6) = 0", int((post[m]==6).sum())==0, f"n={int(m.sum())}")

npass=sum(r[1] for r in res)
print(f"{'ALL PASS' if npass==len(res) else 'FAILURES'}  {npass}/{len(res)}\n")
for n,ok,dtl in res: print(f"  {'PASS' if ok else 'FAIL'}  {n:52s} {dtl}")
import os; os.makedirs("results/data", exist_ok=True)
json.dump([{"fact":n,"pass":bool(o),"detail":d} for n,o,d in res],
          open("results/data/verified_facts.json","w"), indent=1)
