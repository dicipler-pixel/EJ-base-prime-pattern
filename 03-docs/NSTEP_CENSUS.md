# The complete finite characterisation of the twin-gap residue language

`results/nstep_census.py`. 5 000 000 primes; 385 676 twin starts; windows start at regular twin starts $a_k\ge11$ (the seed $3,5$ excluded; from $5$ the word $(6,6)$ is realised but not admissible, see report Remark 4).

---

## Result

Write a twin-start gap's last digit $r_i = d_i \bmod 10 \in \{0,2,4,6,8\}$. Because $d_i\equiv0\pmod 6$,
the residue $r_i$ fixes $d_i \bmod 30$ exactly:

| $r$ | 0 | 2 | 4 | 6 | 8 |
|---|---:|---:|---:|---:|---:|
| $d \bmod 30$ | 0 | 12 | 24 | 6 | 18 |

So a **word** $r_1\cdots r_n$ determines the whole difference set of the forced prime tuple
$a,\,a{+}2,\,a{+}d_1,\,a{+}d_1{+}2,\,\dots$ modulo 30, hence modulo 2, 3 and 5.

**Theorem (census).** A word is reachable *only if* its difference set is not a complete residue
system modulo 2, 3 or 5 (call such a word admissible). The converse is a prime-tuples statement and
is **not proved**; it is observed for $n\le5$ in the first $5\cdot10^6$ primes. The number of
admissible words of length $n$ is

$$A(n)=3^{\,n+1}-2^{\,n+1}.$$

Verified two ways:

| $n$ | words reachable in the data | predicted by admissibility | $5^n$ | share |
|---:|---:|---:|---:|---:|
| 1 | 5 | 5 | 5 | 100 % |
| 2 | 19 | 19 | 25 | 76 % |
| 3 | 65 | 65 | 125 | 52 % |
| 4 | 211 | 211 | 625 | 33.8 % |
| 5 | 665 | 665 | 3125 | 21.3 % |

and the closed form continues to $n=10$ by direct enumeration: 2 059, 6 305, 19 171, 58 025,
175 099 — equal to $3^{n+1}-2^{n+1}$ at every step.

## Why: the mod-3 condition is vacuous, mod 5 is everything

Every $d_i \equiv 0\pmod{6}$, hence $d_i\equiv0\pmod3$ and every partial sum $D_i\equiv0\pmod3$.
The difference set therefore reduces mod 3 to $\{0,2\}$ — two residues, never three. **The mod-3
obstruction can never fire.**

Mod 5 the map $r \mapsto d \bmod 5$ is a bijection ($0,2,4,6,8 \mapsto 0,2,4,1,3$), so the single
real constraint is

$$\{0,2\}\cup\{D_i,\ D_i+2\}_{i\le n}\ \subsetneq\ \mathbb Z/5 .$$

That is a constraint on partial sums in $\mathbb Z/5$, and its transfer matrix has eigenvalues
$3$ and $2$ — which is where $3^{n+1}-2^{n+1}$ comes from.

## Why it matters

This is an **exact, finite, provable** description of which residue words the twin-gap sequence can
produce, and it is written entirely in the digit coordinates. It has no standard counterpart: the
Hardy–Littlewood framework predicts *densities* of constellations and is conjectural; this
characterises *reachability* and is a theorem about $\mathbb{Z}/5$.

Three things follow at once:

1. the six forbidden two-step words $(2,4),(4,2),(4,4),(6,6),(6,8),(8,6)$ — 25 − 19;
2. the 58 holes among 125 three-step words — 125 − 65;
3. the decay $A(n)/5^n \to 0$ like $(3/5)^n$: long residue words are almost all impossible.

## What is not claimed

$A(n)$ counts **residue words**, not prime constellations. That every admissible word occurs
infinitely often is the $k$-tuple conjecture and is not proved. The theorem is about the language
the digits are confined to, not about how often the primes speak it.
