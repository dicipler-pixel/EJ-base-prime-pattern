# The intrinsic colour wheel: $\mathbb{Z}/W$, its automorphism group, and the $2p$ family

Everything below is computed from the ring alone — no coordinates, no metric chosen.

---

## 1. The object and the general theorem

The wheel at base $W$ is the ring $\mathbb{Z}/W$. Its symmetry group is the unit group
$(\mathbb{Z}/W)^\times$, acting by multiplication.

> **Theorem.** The orbits of $(\mathbb{Z}/W)^\times$ on $\mathbb{Z}/W$ are the **divisor classes**:
> the orbit of $x$ is $\{y:\gcd(y,W)=\gcd(x,W)\}$, one class per divisor $d\mid W$, of size
> $\varphi(d)$ — the primitive $d$-th roots of unity. Hence there are exactly $\tau(W)$ classes.

Verified for $W=6,8,10,12,14,18,22,26,30$.

At $W=10$ this reproduces the colour scheme exactly:

| divisor $d$ | class | size | EJ's name |
|---:|---|---:|---|
| 1 | $\{0\}$ | 1 | base (10) |
| 2 | $\{5\}$ | 1 | grey |
| 5 | $\{2,4,6,8\}$ | 4 | secondaries (primitive 5th roots) |
| 10 | $\{1,3,7,9\}$ | 4 | primaries (primitive 10th roots) |

And $\Phi_{10}(x)=\Phi_5(-x)$, which is *why* the primaries are the negatives of the secondaries.

## 2. The colour-viability test — five conditions, all necessary

| | condition | why |
|---|---|---|
| (a) | $\tau(W)=4$ | four classes: base, neutral, primaries, secondaries |
| (b) | sizes $1,1,p{-}1,p{-}1$ | exactly two families of equal size |
| (c) | $(\mathbb{Z}/W)^\times$ **cyclic** | one generator for the symmetries |
| (d) | $W$ even | the neutral is the single element $W/2$ |
| (e) | $2\cdot$(units) lies in **one** class | doubling maps primaries onto secondaries |

| $W$ | $2p$? | $\varphi$ | $\tau$ | class sizes | units cyclic | verdict |
|---:|---|---:|---:|---|---|---|
| **6** | yes | 2 | 4 | $1,1,2,2$ | yes | **viable** |
| 8 | — | 4 | 4 | $1,1,2,4$ | **no** (Klein) | fails (b),(c) |
| **10** | yes | 4 | 4 | $1,1,4,4$ | yes | **viable** |
| 12 | — | 4 | **6** | $1,1,2,2,2,4$ | **no** (Klein) | fails (a),(c) |
| **14** | yes | 6 | 4 | $1,1,6,6$ | yes | **viable** |
| 18 | — | 6 | **6** | $1,1,2,2,6,6$ | yes | fails (a) |
| **22** | yes | 10 | 4 | $1,1,10,10$ | yes | **viable** |
| **26** | yes | 12 | 4 | $1,1,12,12$ | yes | **viable** |
| 30 | — | 8 | **8** | $1,1,2,2,4,4,8,8$ | **no** | fails (a),(c) |

$$\boxed{\text{viable} \iff W = 2p \text{ with } p \text{ an odd prime}}$$

**$W=14$ is the third member, confirmed.** The analytic reason: divisors $1,2,p,2p$ give class
sizes $\varphi=1,1,p{-}1,p{-}1$; and $(\mathbb{Z}/2p)^\times\cong(\mathbb{Z}/p)^\times$ is cyclic of
order $p-1$.

## 3. The richness scale — the colour-system ladder

The number of primaries equals $p-1$, and so does the order of the symmetry group:

| $p$ | $W=2p$ | primaries | secondaries | symmetry group |
|---:|---:|---:|---:|---|
| 3 | 6 | 2 | 2 | $\mathbb{Z}/2$ |
| 5 | 10 | 4 | 4 | $\mathbb{Z}/4$ |
| 7 | 14 | 6 | 6 | $\mathbb{Z}/6$ |
| 11 | 22 | 10 | 10 | $\mathbb{Z}/10$ |
| 13 | 26 | 12 | 12 | $\mathbb{Z}/12$ |

So the family gives colour systems with **2, 4, 6, 10, 12, 16, 18, 22, 28, …** primaries —
exactly $p-1$ for $p$ prime — and *not* 3, 5, 7, 8, 9, 11, 13, 14, 15. Each rung is strictly richer:
more primaries, a bigger symmetry group, a finer class structure.

Base 10's four primaries are the four-ink case; base 6's two are the black/white case.

**Caveat.** This is the ladder *within this family*, under the five conditions. It is not a claim that
no 3-primary or 8-primary colour system can exist — only that no $\mathbb{Z}/W$ wheel satisfies the
five conditions at those sizes.

## 4. What breaks when the method is applied to the sieve — kept deliberately

The sieve's own automorphism group is also $(\mathbb{Z}/W)^\times$, and the divisor-class theorem
applies to it verbatim. What it returns is nothing:

> Every $x\mapsto ux$ permutes the units, so it fixes the survivor set, so **it leaves the gap
> sequence identically unchanged**.

| | colour wheel | sieve |
|---|---|---|
| the classes | **are** the colours | are divisor classes |
| action on the content | relabels colours, meaningfully | **fixes the gaps exactly** |
| information produced | the whole classification | none about primes |

So the intrinsic-wheel derivation is not a general method that happens to work on colour. It
succeeds on the colour wheel because the classes *are* the content, and it fails on the sieve
because the sieve's symmetry is invisible to the only thing that matters there. **Among unit
multiplications, only $u=1$ preserves the cyclic order of the wheel survivors and only $u=-1$
reverses it** (checked at $W=10,30,210,2310$; the 30-wheel gap cycle is a palindrome up to
rotation). So the symmetry group contributes exactly the reflection of the wheel's gap pattern and
nothing about the gaps between actual primes — that is the boundary of this whole line of argument.
*(Corrected in revision 5: an earlier version said the gap sequence has "no non-trivial
symmetry", which missed the reflection.)*

---

## 5. The tuning constraint — and why it is vacuous as a filter on primes

### 5.1 Two readings of "the wheel fits a tuning"

A tuning that divides the octave into $N$ equal steps is the cycle $\mathbb{Z}/N$.

| reading | condition | meaning |
|---|---|---|
| **(P) positions** | $2p \mid N$ | the wheel's $2p$ positions land on distinct pitch classes |
| **(S) symmetry** | $(p-1) \mid N$ | the wheel's symmetry group $\mathbb{Z}/(p{-}1)$ acts on the tuning |

### 5.2 The table

| $N$ | tuning | (P) positions | (S) symmetry |
|---:|---|---|---|
| 12 | Western 12-TET | **6** only | 6, 10, 14, 26 |
| 24 | Turkish notation (24 named pitches) | **6** only | 6, 10, 14, 26 |
| 53 | Turkish AEU comma grid | **none** | **none** |
| 60 | 60-fold | 6, 10 | 6, 10, 14, 22, 26, … |
| 72 | 72-fold | 6 | 6, 10, 14, 26, 38, … |

**53-TET is empty under both readings.** 53 is prime, so $2p\mid 53$ is impossible (53 odd) and
$(p-1)\mid 53$ forces $p-1\in\{1,53\}$, i.e. $p=2$ or $p=54$ — no odd prime.

**24-TET admits base 6 alone under (P).** The only member of the family dividing 24 is 6. So if the
wheel must sit on the named pitches, base 6 is the unique survivor — and base 6's primaries
$\{1,5\}$ are exactly the twin-prime residue classes mod 6.

### 5.3 No comma — just intonation

Just intonation has no modulus: pitches are rationals, and intervals mod octaves form
$\mathbb{Q}^+/\langle 2\rangle$, **free abelian on the primes $3,5,7,\dots$**.

- Under **(P)** there is no modulus to divide, so **every** wheel fits. The condition is vacuous.
- Under **(S)** the group is **torsion-free**, and a finite cyclic group embeds in a torsion-free
  group only when it is trivial. So $(p-1)=1$, i.e. $p=2$: **no odd prime works.**

This is the standard music-theoretic fact in structural form: a just scale is not closed under
transposition. Equal temperament is precisely what makes a finite transposition symmetry possible.

### 5.4 The answer to "can we just pick the tuning to match?"

**Yes, trivially.** For any odd prime $p$, take $N=2p$ — then $2p\mid N$ and $(p-1)\mid 2p$ both hold,
so both readings are satisfied at once. Any multiple of $2p$ works equally.

Therefore the tuning constraint **is not a filter on primes**. It filters which musical systems can
host a given wheel, and it produces two genuine negatives (53-TET and just intonation), but it cannot
single out "real" values of $p$, because the tuning can always be chosen to fit. A constraint that
can be satisfied for every input carries no information about the input.

What survives is narrower and still worth having: **equal temperament is necessary for the symmetry,
and the smallest temperament hosting the base-$2p$ wheel with its full symmetry is $2p$ itself.**

---

## 6. What is derived and what is chosen

| | statement | status |
|---|---|---|
| the colour set is $\mathbb{Z}/W$ | a choice of base $W$ | **chosen** |
| primaries = one orbit of the automorphism group | orbit decomposition | **derived** given $W$ |
| secondaries = the doubling image of the primaries | $2\cdot$units | **derived** given $W$ |
| the neutral is the unique element of order 2, $=W/2$ | $2x\equiv0$ | **derived** given $W$ |
| complement is negation, an element of the automorphism group | $-1\in(\mathbb{Z}/W)^\times$ | **derived** |
| the four classes have sizes $1,1,p{-}1,p{-}1$ | divisor structure of $2p$ | **derived** given $W=2p$ |
| the wheel is viable exactly for $W=2p$ | five conditions | **derived** |
| the symmetry group is cyclic | $(\mathbb{Z}/2p)^\times\cong(\mathbb{Z}/p)^\times$ | **derived** |
| which primary is called "hot" and which "cold" | labelling | **chosen** |
| the temperature axis is red–blue rather than green–magenta | the line of purples is the unique non-spectral chord of $\partial C$ | **derived from the spectrum** |
| the two channels are brightness × chromaticity | de-correlation of overlapping cone fundamentals | **derived, but from conation not the locus** |
| that any of this constrains the primes | — | **false**: the sieve's symmetry fixes the gaps |

## 7. What to claim, and what not to

**Claim.** The colour scheme is the orbit decomposition of the ring $\mathbb{Z}/10$ under its
automorphism group: primaries $=\{1,3,7,9\}$ (the units, which are also the prime end digits),
secondaries $=\{2,4,6,8\}$ (their doubles), grey $=\{5\}$ (the unique element of order 2), base
$=\{0\}$. The scheme generalises to exactly the family $W=2p$, and to nothing else.

**Do not claim.**
1. That the tuning constraint selects real primes — it is satisfiable for every $p$ by taking $N=2p$.
2. That any of this applies to the primes — the sieve's automorphism group fixes the gap sequence
   identically, so the method returns no gap information. That is §4 and it is the boundary of the
   whole line of argument.

The colour result stands on its own as an intrinsic classification. It does not need the primes, and
it is stronger without them.
