"""Colour at scale, magnitude side: the measurements quoted in report Section 5.4.

Prime set: the first 5,000,000 primes above 5 (to 86,028,223), as everywhere in the report.
Rankings are by strict order only: a checkpoint with any tie among the four digit counts is skipped.
"""
import numpy as np
N = 86_100_000
s = np.ones(N + 1, bool); s[:2] = False
for i in range(2, int(N ** 0.5) + 1):
    if s[i]: s[i * i::i] = False
P = np.nonzero(s)[0]; P = P[P > 5][:5_000_000]
assert P[-1] == 86_028_223
d = P % 10
cs = {k: np.cumsum(d == k) for k in (1, 3, 7, 9)}

race = (cs[3] + cs[7]) - (cs[1] + cs[9])
print("race (3+7)-(1+9): strictly behind at", int((race < 0).sum()), "primes; tied at p =",
      [int(x) for x in P[race == 0]])

pts = np.unique(np.logspace(2, np.log10(len(P) - 1), 60).astype(int))
ranks = []
for i in pts:
    c = [(int(cs[k][i]), k) for k in (1, 3, 7, 9)]
    if len({v for v, _ in c}) < 4: continue
    ranks.append("".join(str(k) for _, k in sorted(c, reverse=True)))
changes = sum(a != b for a, b in zip(ranks, ranks[1:]))
print(f"tie-free checkpoints: {len(ranks)} of {len(pts)}; ranking changes between them: {changes}")
print("rankings seen:", sorted(set(ranks)))

others = np.minimum(np.minimum(cs[1], cs[7]), cs[9])
last3 = cs[3] < others
starts = [int(P[i]) for i in np.nonzero(last3 & ~np.r_[False, last3[:-1]])[0]]
print("stretches where 3 is strictly last (checked at every prime): start at p =", starts)

for x in (10 ** 4, 10 ** 6, None):
    q = d if x is None else d[P < x]
    print(f"repeat share {'all' if x is None else '<'+str(x)}: {100 * (q[1:] == q[:-1]).mean():.2f}%")
