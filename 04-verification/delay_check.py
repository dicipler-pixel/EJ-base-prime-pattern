"""Delays on the wheel: the measurements quoted in report Section 6.

Prime set: the first 5,000,000 primes above 5 (to 86,028,223).
"""
import numpy as np
from math import sqrt
N = 86_100_000
s = np.ones(N + 3, bool); s[:2] = False
for i in range(2, int(N ** 0.5) + 1):
    if s[i]: s[i * i::i] = False
P = np.nonzero(s)[0]; P = P[P > 5][:5_000_000]
assert P[-1] == 86_028_223
d = P % 10

print("1) return delay of each end digit (in primes)")
geo = [0.25 * 0.75 ** (j - 1) for j in range(1, 6)]
for k in (1, 3, 7, 9):
    w = np.diff(np.nonzero(d == k)[0])
    print(f"   digit {k}: mean {w.mean():.3f}; P(delay=1..5) = " + " ".join(f"{100*np.mean(w==j):.2f}" for j in range(1, 6)))
print("   independent digits: mean 4.000; P(delay=1..5) = " + " ".join(f"{100*x:.2f}" for x in geo))

print("2) memory by lag: mutual information between the digit and the digit k primes later")
x = np.searchsorted([1, 3, 7, 9], d)
def H(p): p = p[p > 0]; return -(p * np.log2(p)).sum()
print("   entropy of one digit: %.5f bits" % H(np.bincount(x, minlength=4) / len(x)))
for k in (1, 2, 3, 5, 10):
    J = np.zeros((4, 4)); np.add.at(J, (x[:-k], x[k:]), 1); J /= J.sum()
    print(f"   lag {k:2}: {1000*(H(J.sum(1)) + H(J.sum(0)) - H(J.ravel())):.3f} millibits")

t = P[s[P + 2]]                       # twin starts among the 5M primes
w5 = np.array([5 - len({0, 2, r, (r + 2) % 5}) for r in range(5)])
pred = w5 / w5.sum()
print("3) twin delays mod 5: free hues", list(w5), "-> predicted shares", [f"{100*x:.1f}" for x in pred])
g = np.diff(t)
print("   consecutive twin pairs:", [f"{100*np.mean(g % 5 == r):.1f}" for r in range(5)], f"(n={len(g)})")
H_MAX = 3000
cnt = np.zeros(5)
for j in range(1, 400):
    dd = t[j:] - t[:-j]; dd = dd[dd <= H_MAX]
    if len(dd) == 0: break
    np.add.at(cnt, dd % 5, 1)
print(f"   all pairs of twin starts with delay <= {H_MAX}:", [f"{100*x:.1f}" for x in cnt / cnt.sum()], f"(n={int(cnt.sum())})")

print("4) checks that came out null or not significant")
ang = np.searchsorted([1, 7, 9, 3], d, sorter=np.argsort([1, 7, 9, 3]))
a = np.array([{1: 0, 7: 1, 9: 2, 3: 3}[v] for v in (1, 3, 7, 9)])[x]
st = np.diff(a) % 4
steps = np.where(st == 1, 1, np.where(st == 3, -1, 0))
var = np.mean(steps ** 2) * len(steps)
print(f"   hue walk: net quarter turns {int(steps.sum())}, chance-size {sqrt(var):.0f} -> z = {steps.sum()/sqrt(var):.2f}")
eq = np.nonzero(g[:-1] == g[1:])[0]; ge = np.diff(eq); rate = len(eq) / len(g)
e5 = (1 - (1 - rate) ** 5) * len(ge); o5 = int((ge <= 5).sum())
print(f"   equilibria: {len(eq)}; delays <= 5 between consecutive equilibria: observed {o5}, "
      f"independent {e5:.1f}, z = {(o5 - e5)/sqrt(e5):.2f}")
