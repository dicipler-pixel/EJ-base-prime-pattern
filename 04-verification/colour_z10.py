print("her new sheet: base = 10, primaries 1,3,7,9, secondaries 2,4,6,8, grey 5, base 10")
print("reading: arithmetic is Z/10, 10 == 0.\n")
Z=list(range(10))
units=[x for x in Z if __import__('math').gcd(x,10)==1]
print("the four units of Z/10 :",units,"  <- her PRIMARIES  (and the prime end digits)")
dbl=sorted({(2*x)%10 for x in units})
print("doubles of the units    :",dbl,"  <- her SECONDARIES")
print("   2*1 =",2*1%10,"  2*3 =",2*3%10,"  2*7 =",2*7%10,"  2*9 =",2*9%10)
print("her labels 2=M(magenta) 4=C(cyan) 6=Y(yellow) 8=G(green):")
lab={2:'M',4:'C',6:'Y',8:'G'}
for x in units:
    print(f"   2 * {x} = {(2*x)%10} = {lab[(2*x)%10]}")
print("\nthe unique element of order 2 (2x = 0 mod 10):",
      [x for x in Z if (2*x)%10==0 and x!=0])
print("   -> 5 is the KERNEL of doubling. it is half the base.")
print("\nthe partition of Z/10:")
print("   base      {0}          (= 10, the roll-over)")
print("   primaries",sorted(units))
print("   secondaries",dbl)
print("   neutral   {5}")
print("   counts:",1+len(units)+len(dbl)+1,"= 10  -> exact, nothing left out")
print("\ncomplementation = negation x -> (10-x) % 10 ; orbits:")
seen=set(); orbs=[]
for x in Z:
    if x in seen: continue
    o=frozenset({x,(10-x)%10}); orbs.append(o); seen|=o
for o in sorted(orbs,key=lambda t:min(t)):
    print("   ",sorted(o),"  fixed point" if len(o)==1 else "")
print("\n   her four pairs are exactly the four 2-element orbits;")
print("   the two FIXED points are 0 (the base) and 5 (grey), the only self-complementary colours.")
print("\nso: grey at 5 is not a placement, it is forced -- 5 is the only colour equal to its own")
print("complement other than the base itself, because 2*5 = 10 = the base.")
