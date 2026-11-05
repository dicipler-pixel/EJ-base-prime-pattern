import numpy as np, sympy as sp
a=np.array([1.0,0.0]); b=np.array([0.0,1.0])
v={3:a, 6:a+b, 1:b, 2:-a+b, 7:-a, 4:-a-b, 9:-b, 8:a-b}
order=[3,6,1,2,7,4,9,8]
J=np.array([[0.0,-1.0],[1.0,0.0]])            # rotation by +90 in the (R-axis, W-axis) plane
print("J = rotation by +90 deg in the temperature/value plane")
print("  J^2 == -I :", np.allclose(J@J, -np.eye(2)))
print("\n  action on her primaries:")
for r in (3,7,9,1):
    x=v[r]; y=J@x
    tgt=[k for k,z in v.items() if np.allclose(z,y) or np.allclose(z,-y)]
    print(f"    J . v({r}) = {tuple(np.round(y,3))} = v({tgt[0]})   so {r} -> {tgt[0]}")
print("  the 4-cycle is R -> W -> B -> Bl -> R :", [3,1,7,9] )
print("\n  J^2 is the complement map; check all four stated pairs:")
for p in [(3,7),(1,9),(6,4),(8,2)]:
    print(f"    J^2 v({p[0]}) == v({p[1]}) :",
          np.allclose(J@J@v[p[0]], v[p[1]]), " (and the ratio is", 
          round(np.linalg.norm(v[p[1]])/np.linalg.norm(v[p[0]]),3),")")
print("\n  complex coordinates: v(r) = m * exp(i*pi*k/4)")
for r in order:
    z=complex(v[r][0], v[r][1]); import cmath
    print(f"    {r}: z = {z.real:+.1f}{z.imag:+.1f}i   |z| = {abs(z):.3f}   "
          f"arg/45 = {np.degrees(cmath.phase(z))/45:.1f}")
print("\nwhich axis does each residue sit on?")
for r in order:
    z=complex(v[r][0],v[r][1])
    kind = "REAL axis (temperature)" if abs(z.imag)<1e-9 else \
           "pure IMAGINARY axis (value)" if abs(z.real)<1e-9 else "45 deg (maximally virtual)"
    print(f"  {r}: {kind}")
print("\nnow the decisive test: which metrics make J orthogonal (h = g + i*omega Hermitian)?")
aa,bb,cc=sp.symbols('a b c',real=True,positive=True)
G=sp.Matrix([[aa,bb],[bb,cc]]); Jm=sp.Matrix([[0,-1],[1,0]])
print("  J^T G J =", (Jm.T*G*Jm).tolist())
print("  set equal to G:")
sol=sp.solve([sp.Eq((Jm.T*G*Jm)[0,0],G[0,0]),sp.Eq((Jm.T*G*Jm)[0,1],G[0,1]),
              sp.Eq((Jm.T*G*Jm)[1,1],G[1,1])],[aa,bb,cc],dict=True)
print("   ->",sol)
print("\n  so J-invariance forces G = a*I: the metric collapses from 3 parameters to 1 (a scale).")
print("  equal norms on the two channels is a CONSEQUENCE of admitting J, not an assumption.")
