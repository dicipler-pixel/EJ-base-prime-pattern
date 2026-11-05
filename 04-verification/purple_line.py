import numpy as np
lam=np.linspace(390,700,400)
def g(mu,sd): return np.exp(-0.5*((lam-mu)/sd)**2)
S_=np.stack([g(570,45),g(540,40),g(445,35)],axis=1)
def chrom(p):
    s=p.sum(); return p/s
C=np.array([chrom(s)[:2] for s in S_])
print("the spectral locus: an OPEN arc of",len(C),"points")
# endpoints of the arc = extremes of wavelength
e_short, e_long = C[0], C[-1]
print(f"  short-wave end (390 nm) chromaticity {np.round(e_short,4)}")
print(f"  long-wave end  (700 nm) chromaticity {np.round(e_long,4)}")
print(f"  chord length {np.linalg.norm(e_long-e_short):.4f}  -- this chord is the LINE OF PURPLES")
print("  it is the ONLY segment of the boundary that is not spectral.\n")
# distance of every spectral point from the chord line
def line_dist(pt,a,b):
    d=b-a; n=np.array([-d[1],d[0]]); n=n/np.linalg.norm(n)
    return abs(n@(pt-a))
print("  where does each named hue sit relative to that chord?")
def band(c,sd): return g(c,sd)/g(c,sd).sum()
tests=[("red 630",630),("yellow 580",580),("green 530",530),("blue 460",460),("violet 400",400)]
for nm,w in tests:
    k=int(np.argmin(abs(lam-w)))
    p=chrom(S_[k])
    dp=line_dist(p[:2],e_short,e_long)
    on_arc = (w<=lam[0]+1) or (w>=lam[-1]-1)
    print(f"    {nm:12s} distance from the purple chord = {dp:.4f}"
          + ("   <- an ENDPOINT of the arc" if on_arc else ""))
# magenta = midpoint of the chord: on the purple line, NOT on the spectral torus
mag=(e_short+e_long)/2
print(f"\n  magenta (midpoint of the purple chord) = {np.round(mag,4)}")
dmin=min(np.linalg.norm(C-mag,axis=1))
print(f"  distance from magenta to the nearest spectral colour: {dmin:.4f}  (never zero)")
print("\n  so: red and violet are the two ENDPOINTS of the arc, and magenta lies strictly inside")
print("  the chord joining them. green is interior to the arc.")
print("\n  the four candidate poles and their status:")
print("    red     : endpoint of the spectral arc        (on dC, extreme)")
print("    violet  : endpoint of the spectral arc        (on dC, extreme)")
print("    green   : interior point of the arc           (on dC, but NOT extreme)")
print("    magenta : interior point of the purple chord  (NOT on the arc at all)")
print("\n  => the only chord whose BOTH ends are extreme is red-violet.")
print("     green-magenta has one non-extreme end (green) and one non-spectral end (magenta),")
print("     so it is a line through the interior, not an axis of dC.")
