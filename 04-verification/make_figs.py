import matplotlib; matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np, itertools, math
import os
O="results/figs/pdf/"; os.makedirs(O, exist_ok=True)
plt.rcParams.update({"font.size":9,"axes.titlesize":10,"axes.labelsize":9,
                     "figure.dpi":110,"savefig.bbox":"tight"})

# ---------- Fig 1: the census
A=[3**(n+1)-2**(n+1) for n in range(1,11)]
obs={1:5,2:19,3:65,4:211,5:665}
fig,ax=plt.subplots(1,2,figsize=(9,3.4))
n=np.arange(1,11)
ax[0].bar(n,A,color="#9ecae1",label="$3^{n+1}-2^{n+1}$")
ax[0].plot(list(obs),list(obs.values()),"o",color="#d62728",ms=7,zorder=5,
           label="realised in $5\\cdot10^6$ primes")
ax[0].set_yscale("log"); ax[0].set_xlabel("word length $n$")
ax[0].set_ylabel("admissible words")
ax[0].set_title("the census: $A(n)=3^{n+1}-2^{n+1}$")
ax[0].legend(fontsize=7)
ax[1].plot(n,[a/5**k for a,k in zip(A,n)],"o-",color="#2ca02c")
ax[1].plot(n,[(3/5)**(k+1) for k in n],"k--",lw=1,label="$(3/5)^{n+1}$")
ax[1].set_yscale("log"); ax[1].set_xlabel("$n$"); ax[1].set_ylabel("$A(n)/5^n$")
ax[1].set_title("realised share decays like $(3/5)^n$")
ax[1].legend(fontsize=7)
fig.tight_layout(); fig.savefig(O+"fig1_census.pdf"); plt.close(fig)

# ---------- Fig 2: the seven word classes at n=5
# w ranges over beam sequences (b_1..b_n), b_i = D_i mod 10; these are in bijection with words.
U=[0,2,4,6,8]; t0={0,2,4}; t1={0,2,8}; t2={0,6,8}
cls={"A":0,"B":0,"C":0,"AB":0,"BC":0,"AC":0,"ABC":0}
for w in itertools.product(U,repeat=5):
    img=set(w)|{0}
    a=img<=t0; b=img<=t1; c=img<=t2
    if a and b and c: cls["ABC"]+=1
    elif a and b: cls["AB"]+=1
    elif b and c: cls["BC"]+=1
    elif a and c: cls["AC"]+=1
    elif a: cls["A"]+=1
    elif b: cls["B"]+=1
    elif c: cls["C"]+=1
fig,ax=plt.subplots(figsize=(6.4,3.2))
keys=list(cls); vals=[cls[k] for k in keys]
cols=["#2ca02c","#9467bd","#2ca02c","#8c564b","#8c564b","#7f7f7f","#d62728"]
ax.bar(keys,vals,color=cols)
for i,(k,v) in enumerate(zip(keys,vals)):
    ax.text(i,v+3,str(v),ha="center",fontsize=8)
ax.set_ylabel("words of length 5"); ax.set_ylim(0,240)
ax.set_title("the seven word classes at $n=5$ (sum $=665$)")
ax.set_xlabel("class (beams: A$=\\{0,2,4\\}$, B$=\\{0,2,8\\}$, C$=\\{0,6,8\\}$)")
fig.tight_layout(); fig.savefig(O+"fig2_classes.pdf"); plt.close(fig)

# ---------- Fig 3: the five-rung ladder
fig,ax=plt.subplots(1,2,figsize=(9,3.2))
g=np.arange(0,32,2); D=[x%10//2+1 for x in g]
ax[0].step(g,D,where="mid",color="#1f77b4",lw=2)
ax[0].plot(g,D,"o",ms=4,color="#1f77b4")
ax[0].set_xlabel("gap $g$"); ax[0].set_ylabel("rung $D$")
ax[0].set_yticks([1,2,3,4,5]); ax[0].set_title("the five-rung cycle: $D=(g \\mathrm{mod}\\, 10)/2+1$")
ax[0].annotate("gap 10 returns to 1D",(10,1),xytext=(12,2.4),fontsize=7,
               arrowprops=dict(arrowstyle="->",lw=.8))
pos=np.arange(5)
mg=np.arange(12); mt=4+6*np.arange(12)
ax[1].plot(mg,[x%10//2+1 for x in mg],"o-",color="#1f77b4",label="prime gaps (step 2)")
ax[1].plot(mt,[x%10//2+1 for x in mt],"s--",color="#d62728",label="twin gaps (step 6)")
ax[1].set_xlabel("gap value"); ax[1].set_ylabel("rung")
ax[1].set_yticks([1,2,3,4,5]); ax[1].legend(fontsize=7)
ax[1].set_title("same five rungs, two step sizes")
fig.tight_layout(); fig.savefig(O+"fig3_ladder.pdf"); plt.close(fig)

# ---------- Fig 4: the colour wheel Z/10
fig,ax=plt.subplots(figsize=(4.4,4.4))
names={1:"W",3:"R",7:"B",9:"K",0:"0",5:"grey",2:"M",4:"C",6:"Y",8:"G"}
units=[1,3,7,9]; dbl=[2,4,6,8]
col={}
for u in units: col[u]="#2ca02c"
for d in dbl: col[d]="#9467bd"
col[5]="#7f7f7f"; col[0]="#d62728"
for r in range(10):
    th=np.pi/2-2*np.pi*r/10
    x,y=np.cos(th),np.sin(th)
    ax.plot([0,x],[0,y],color=col[r],lw=.6,alpha=.5)
    ax.plot(x,y,"o",ms=17,color=col[r])
    ax.text(x,y,names[r],ha="center",va="center",fontsize=8,color="white",weight="bold")
for a,b in [(1,9),(3,7),(2,8),(4,6)]:
    th1=np.pi/2-2*np.pi*a/10; th2=np.pi/2-2*np.pi*b/10
    ax.plot([np.cos(th1),np.cos(th2)],[np.sin(th1),np.sin(th2)],"k:",lw=1)
ax.set_aspect("equal"); ax.axis("off")
ax.set_title("$\\mathbb{Z}/10$: orbits of $\\mathrm{Aut}$\n"
             "green = units (primaries), purple = doubles,\n"
             "grey = $5$ (neutral), red = $0$ (base); dotted = complement",
             fontsize=8)
fig.tight_layout(); fig.savefig(O+"fig4_wheel.pdf"); plt.close(fig)

# ---------- Fig 5: which modulus obstructs
fig,ax=plt.subplots(figsize=(6.2,3.2))
ns=np.arange(1,9); sizes={2:[],3:[],5:[]}
RES={0:0,2:12,4:24,6:6,8:18}
for n in ns:
    best={2:0,3:0,5:0}
    for w in itertools.product(U,repeat=n):
        D=0; S={0,2}
        for r in w:
            D+=RES[r]; S|={D%30,(D+2)%30}
        for q in (2,3,5): best[q]=max(best[q],len({s%q for s in S}))
    for q in (2,3,5): sizes[q].append(best[q])
for q,c,lab in [(2,"#1f77b4","mod 2 (needs 2)"),(3,"#2ca02c","mod 3 (needs 3)"),(5,"#d62728","mod 5 (needs 5)")]:
    ax.plot(ns,sizes[q],"o-",color=c,label=lab)
for q in (2,3,5): ax.axhline(q,color="k",ls=":",lw=.7)
ax.set_xlabel("word length $n$"); ax.set_ylabel("max distinct residues reached")
ax.set_title("only mod 5 can ever be complete: mod 2 and mod 3 are inert")
ax.legend(fontsize=7); ax.set_ylim(0,5.6)
fig.tight_layout(); fig.savefig(O+"fig5_obstruction.pdf"); plt.close(fig)
print("figures written")
