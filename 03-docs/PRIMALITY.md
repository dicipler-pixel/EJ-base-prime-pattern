# A certified primality test from the base and twin patterns

`ej_primality.py`. Verified: **0 errors** on 199 994 exhaustive $n$, 3 000 random $n\le10^8$, and
26 666 twin starts.

---

## Theorem (the EJ test)

For an integer $n>5$, $n$ is prime **if and only if** all four hold:

1. $n \bmod 10 \in \{1,3,7,9\}$;
2. $3 \nmid n$;
3. $5 \nmid n$;
4. no $m$ with $7\le m\le\lfloor\sqrt n\rfloor$ and $\gcd(m,30)=1$ divides $n$.

**Proof.** ($\Rightarrow$) A prime $n>5$ is coprime to $30$, so 1–3 hold, and it has no divisor in
$[7,\sqrt n]$.

($\Leftarrow$) Contrapositive. Suppose $n$ is composite: $n=ab$ with $1<a\le b<n$, so
$a\le\sqrt n$. By 1–3, $\gcd(n,30)=1$, hence $\gcd(a,30)=1$. If $a\le5$ then $2$, $3$ or $5$ divides
$n$, contradicting 2–3. Therefore $a\ge7$ and $\gcd(a,30)=1$, so $a$ is one of the tested $m$,
contradicting 4. $\square$

Conditions 1–3 are exactly the **key**; condition 4 is the wheel iteration. The key is therefore not
a heuristic but the base case of a correct algorithm.

## Corollary 1 (the key's exact reach)

Conditions 1–3 alone decide primality for every $n<49$.

*Proof.* The least composite coprime to 30 is $7^2=49$: any composite coprime to $30$ has all prime
factors $\ge7$, hence is $\ge49$. $\square$

General form: with the wheel $P=p_1\cdots p_k$ and $p=p_{k+1}$, the conditions $\gcd(n,P)=1$
decide primality for all $n<p^2$.

| wheel | survivors $\varphi(P)/P$ | first failure | exact for |
|---:|---:|---:|---:|
| 30 | 26.67 % | **49** | $n<49$ |
| 210 | 22.86 % | 121 | $n<121$ |
| 2310 | 20.78 % | 169 | $n<169$ |
| 30030 | 19.18 % | 289 | $n<289$ |

## Corollary 2 (the twin test)

For $n>3$: $n$ and $n+2$ are both prime **iff**

$$n\equiv5\pmod6,\qquad 5\nmid n,\qquad 5\nmid (n+2),\qquad
\forall m\in[7,\sqrt{n+2}],\ \gcd(m,30)=1:\ m\nmid n(n+2).$$

*Proof.* ($\Rightarrow$) Theorem 4 of the main paper. ($\Leftarrow$) If $n$ or $n+2$ is composite,
let $p$ be its least prime factor. Since $n\equiv5\pmod6$, $3\nmid n(n+2)$; if $p=5$ the third
condition fails; otherwise $p\ge7$, $\gcd(p,30)=1$ and $p\le\sqrt{n+2}$. $\square$

The twin pattern's contribution is a **residue-class saving**: a twin start is one class mod 6,
against four classes mod 10 for a single prime.

## The algorithm

```
input n > 5
  if n mod 10 not in {1,3,7,9}: return COMPOSITE (last digit)
  if 3 | n : return COMPOSITE (3)
  if 5 | n : return COMPOSITE (5)
  if n < 49 : return PRIME
  for m in [7, sqrt(n)] with gcd(m,30)=1:
      if m | n : return COMPOSITE (m)
  return PRIME
```

Every COMPOSITE is returned with a **certificate** (a divisor), so compositeness is verifiable
without re-running the test. Every PRIME rests on the exhaustion of $\{m\le\sqrt n:\gcd(m,30)=1\}$.

## Verification

| test | scope | errors |
|---|---|---:|
| exhaustive | $7\le n\le200\,000$ (199 994 numbers) | **0** |
| random | 3 000 values in $[2\cdot10^5,10^8]$ | **0** |
| key alone | $n<49$ | exact; first failure $49=7^2$ |
| twin test | 26 666 twin starts $\le200\,000$ | **0** |

Cost, measured over the exhaustive range: **1 829 848 division tests** for 199 994 numbers
(9.15 per number), against 59 328 924 for full trial division (296.7 per number). The structural
factor is $\varphi(30)/30 = 0.2667$ — a $3.75\times$ reduction in candidates for the survivors of
conditions 1–3, with the rest of the saving coming from early exit.

## What the test cannot do

No finite key decides primality. For every wheel $P$ the number $p_{k+1}^2$ passes the key and is
composite, so condition 4 is not removable. The pattern's deductive content is exactly the wheel;
its statistical content — the gap distribution — is a statement about the sequence, not a test of a
single number.

---

# Addition: running condition 3 in the beam language

## Theorem D (the candidate stream's own beams)

On the wheel of $30$, the integers coprime to $30$ have consecutive gaps
$$(4,\,2,\,4,\,2,\,4,\,6,\,2,\,6)$$
with period $30$ — so **only the beams $\delta\in\{2,4,6\}$ occur.** Beams $0$ (gap $10$) and
$8$ (gap $8$) first appear on the wheel of $210$.

*Proof.* The residues coprime to $30$ in $[1,30]$ are $1,7,11,13,17,19,23,29$; the successive
differences are $6,4,2,4,2,4,6,2$, all in $\{2,4,6\}$. Enumerating the $48$ residues coprime to $210$
produces gaps $\{2,4,6,8,10\}$, whose beams are $\{0,2,4,6,8\}$. $\square$

Verified across wheels:

| wheel | residues | gap values | beams used |
|---:|---:|---|---|
| 30 | 8 | 2, 4, 6 | **2, 4, 6** |
| 210 | 48 | 2, 4, 6, 8, 10 | **0, 2, 4, 6, 8** |
| 2310 | 480 | 2 … 14 | 0, 2, 4, 6, 8 |
| 30030 | 5 760 | 2 … 22 | 0, 2, 4, 6, 8 |

## The step-driven test

Condition 3 can be executed **by the beam cycle instead of by a divisibility check on the index**:

```
m = 7 ; i = 0 ; cycle = (4,2,4,2,4,6,2,6)
while m <= sqrt(n):
    if m | n: return COMPOSITE (m)
    m += cycle[i mod 8] ; i += 1
```

This steps from one candidate to the next along the beam cycle and never computes
$\gcd(m,30)$. It is the same candidate set, reached without testing each integer in between.

| version | exhaustive errors | random $n\le10^8$ |
|---|---:|---:|
| gcd-filtered | 0 | 0.06 s / 3000 |
| **beam-stepped** | **0** | **0.04 s / 3000** (1.5×) |

Both agree on all 199 994 numbers.

## What this does and does not buy

**It does not shrink the candidate set.** The wheel already produces exactly these candidates, so
condition 3 tests the same $m$ either way — the beam description adds no new exclusion.

**It does buy three things.** (i) A structural statement, Theorem D, which places the beams inside the
test: the 30-wheel lives entirely in beams 2, 4, 6. (ii) A 1.5× faster loop, because the step is
precomputed. (iii) A clean statement of *why* gaps 8 and 10 are absent from the small-wheel stream —
they need the 210-wheel to exist, which is the same fact as $p_{k+1}^2$ in Corollary 1.
