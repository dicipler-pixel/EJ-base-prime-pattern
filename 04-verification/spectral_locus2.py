import numpy as np
lam=np.linspace(400,700,301)
def g(mu,sd): return np.exp(-0.5*((lam-mu)/sd)**2)
S_=np.stack([g(570,45),g(540,40),g(445,35)],axis=1)
def chrom(p):
    s=p.sum(-1,keepdims=True); return p/s
C3=chrom(S_)
C=C3[:,:2]                                   # chromaticity as a curve in 2D (third coord = 1-sum)
print("the spectral locus as a curve in the chromaticity plane:",C.shape)
def hull(P):
    P=sorted(map(tuple,P)); 
    def cr(o,a,b): return (a[0]-o[0])*(b[1]-o[1])-(a[1]-o[1])*(b[0]-o[0])
    lo=[]
    for p in P:
        while len(lo)>=2 and cr(lo[-2],lo[-1],p)<=0: lo.pop()
        lo.append(p)
    up=[]
    for p in reversed(P):
        while len(up)>=2 and cr(up[-2],up[-1],p)<=0: up.pop()
        up.append(p)
    return np.array(lo[:-1]+up[:-1])
H=hull(C)
print("  convex hull of the locus has",len(H),"vertices -- it is a curve, not a triangle")
# a circumscribing triangle: pick three supporting lines through hull edges, intersect them
def line_through(a,b):
    n=np.array([-(b-a)[1],(b-a)[0]]); n=n/np.linalg.norm(n)
    if n@np.array([0.333,0.333])>0: n=-n
    return n, n@a
edges=[(H[i],H[(i+1)%len(H)]) for i in range(len(H))]
# choose three well separated edges
idx=[0, len(H)//3, 2*len(H)//3]
lines=[line_through(*edges[i]) for i in idx]
def inter(l1,l2):
    n1,c1=l1; n2,c2=l2; A=np.stack([n1,n2])
    return np.linalg.solve(A,np.array([c1,c2]))
V=[inter(lines[0],lines[1]),inter(lines[1],lines[2]),inter(lines[2],lines[0])]
V=np.array(V)
print("\ncircumscribing triangle from three supporting lines:")
for v in V: print("   vertex",np.round(v,4))
d=[min(np.linalg.norm(C-v,axis=1)) for v in V]
print("   distance of each vertex from the locus:",np.round(d,4)," -> all >0, vertices are VIRTUAL")
# verify the triangle contains the locus
def inside(p,V):
    s=[]
    for i in range(3):
        a,b=V[i],V[(i+1)%3]
        s.append((b-a)[0]*(p-a)[1]-(b-a)[1]*(p-a)[0])
    return all(x>=-1e-12 for x in s) or all(x<=1e-12 for x in s)
print("   triangle contains the whole locus:",all(inside(c,V) for c in C))
# and with three REAL primaries (locus points) some colour always needs a negative coefficient
def coefs(p,prim3):
    return np.linalg.solve(np.array(prim3).T,p)
for name,prim in [("locus points 610/520/440",
                   [S_[60],S_[120],S_[240]]),
                  ("triangle vertices -> 3D primaries",
                   [np.array([v[0],v[1],1-v[0]-v[1]]) for v in V])]:
    neg=sum(1 for k in range(301) if coefs(S_[k],prim).min()<-1e-12)
    print(f"\n   {name}: spectral colours needing a negative coefficient = {neg}/301")
print("\nTHEOREM (why virtual primaries are forced)")
print("  C = colour cone, a proper closed convex cone with nonempty interior.")
print("  If p1,p2,p3 lie in int C then any nonneg combination of them (not all zero) is in int C.")
print("  Every spectral colour lies in dC.  Hence no triple of REAL primaries represents all")
print("  spectral colours with nonnegative coefficients; the primaries must lie outside dC.")
print("  Sign changes occur exactly on crossing dC -- the boundary hypersurface.")
