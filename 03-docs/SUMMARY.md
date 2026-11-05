# What is here, what it is worth, and where it could go

All figures: first 5 000 000 primes (2 … 86 028 121), 385 375 twin pairs, 385 374 segments.

---

# Part I — the models

## 1. Base Prime Model

| element | statement |
|---|---|
| encoding | $p = 10s+d$, $d\in\{1,3,7,9\}$ = end digit, $s$ = inner node |
| gap identity | $g = 10\Delta s + \Delta d$ — exact, 4 999 999 / 4 999 999 |
| **carry law** | $\Delta s = \lfloor g/10 \rfloor + \mathbb{1}[\Delta d<0]$ — exact |
| segment | $bg = a_k$ (twin start) to $ep = a_{k+1}+2$; interior primes = inner nodes |
| subset sequence | inner-node values, normalised to start at 0; non-decreasing, always |
| dimension | $D=\pi(ep-2)-\pi(bg+1)$ = number of inner nodes |

The pattern is a **two-channel code**: the end digit is the fine channel, the subset sequence the
coarse one.

| information | bits |
|---|---:|
| $H(g)$ | 4.378 |
| removed by the subset step | 1.649 |
| removed by the digit step | **2.310** |
| left with both | **0** |

## 2. Twin Prime Counterflow

| element | statement | status |
|---|---|---|
| boundary | $ep_i = bg_{i+1}+2$ | definition |
| **exchange** | $B_k=A_{k+1}$ (offset column of row $k$ = difference column of row $k+1$) | identity, 100 % |
| **balance** | $ep_{i+1}-ep_i = bg_{i+1}-bg_i$, i.e. $d_k=d_{k+1}$ | 1.011 % |
| **equilibrium law** | impossible iff $2v-u\equiv3,5 \pmod{10}$, $v=(ep-2)\bmod 10$ | 4 of 9 cells, exact |
| back-trace column | $F=-d_{k+2}$ | exact, but a shift |

The counterflow is a **three-term relation in two-row clothing**: whether a row can equilibrate is
decided by the end digit of the *third* twin start.

## 3. The keys (cipher ladder)

| level | input | base 10 | base 9 |
|---|---|---|---|
| 1 | (end digit of $p$, of $q$) | 16 cells → gap mod 10 | 36 cells → gap mod 9 |
| 2 | $(bg, ep)$ | 9 cells → span **mod 30** | 9 cells → span mod 9 |
| 3 | $(bg, ep_{k+1})$ merged | 9 cells → gap **mod 30** | 9 cells → gap mod 9 |

Multiplicities: 4-3-3-3-3 (L1 base 10), 3-2-2-2-1 (L2/L3 base 10), 3-3-3 (base 9).
Cell-count spread: 2.00, 1.19, 1.03 (base 10) and 2.66, 1.15, 1.05 (base 9).

$$\operatorname{lcm}(10,9)=90=\operatorname{lcm}(30,9)$$

**Both routes hit mod 90, which resolves 99.76 % of prime gaps outright.** The twin structure's
factor of 3 is exactly the factor that base 9 supplies anyway, because the twin condition is a
constraint mod 3.

---

# Part II — what each piece is worth

## Exact and worth keeping

1. $g = 10\Delta s+\Delta d$ and $\Delta s=\lfloor g/10\rfloor+\mathbb{1}[\Delta d<0]$.
2. Theorem 3: the end-digit cipher key (16 cells, one residue each).
3. Theorem 15: three mod-9 twin classes, 128 328 / 128 709 / 128 338.
4. Twin starts $\equiv 5 \pmod 6$; $d_k\equiv 0 \pmod 6$.
5. Digit exclusivity: 3 never in $bg$, 7 never in $ep$ (0 in 385 375). Both one-line proofs.
6. Exactly one 1D segment in five million primes: $[3,7]$.
7. The equilibrium-forbidden theorem (4 of 9 cells).
8. Merged key pins mod 30; base key pins mod 10; together with base 9, mod 90.
9. Cell-count flattening 2.00 → 1.19 → 1.03 under aggregation.

## Identities — true, but carry no information

- the counterflow exchange (100 % because $ep$ is defined from $bg$);
- the mass identities ($\sum D_k=(a_{m+1}-a_1)/2-m$, $\bar D\rho=1/2-m/x$);
- the back-trace column (a two-row shift, not a prediction);
- the 4/3 "rule" (it is the asymptote, not the observation);
- the diamond counts (hold for any odd sequence).

## Known — measured here, published elsewhere

- the last-digit transition bias (Lemke Oliver–Soundararajan 2016), and its transience (Holt 2024);
- mod-9 equidistribution of twin classes (special case of the same framework);
- the gap populations per residue class under Eratosthenes sieve.

## False, and measured so

- Conjecture 6 (subscripts alone determine gaps): 11 898 of 243 008 tuples conflict;
- Conjecture 11 as universal (1.011 %);
- the period-4–6 wave (lag-1 autocorrelation $-0.5047$, nothing after);
- the Snell-type law at the joints (residual = shuffled null);
- the chromatic addition rules as a homomorphism ($R+W=4\neq6$).

---

# Part III — avenues, ranked

## 1. Runs of equal gaps = twin pairs in arithmetic progression ← best

The equilibrium $d_k=d_{k+1}$ is the length-2 case of a general object: $r+1$ twin starts in
arithmetic progression. Measured:

| run of equal gaps | count | note |
|---|---:|---|
| 2 | 3 830 (1.00 %) | fewer than the iid expectation (1.64 %) |
| 3 | 33 | e.g. gap 210 at twin start 906 119 |
| 4 or more | **0** | none below 8.6·10⁷ |

So $g_k=g_{k+1}=\cdots=g_{k+r-1}$ defines a cluster of twin pairs in AP, and the sequence stops at
$r=3$ in this range. This is a **prime-constellation question with a literature** (constellations,
CPAP, Hardy–Littlewood $k$-tuples): the singular series predicts the density of each run length, and
the run-4 case is a specific, computable prediction. This is the only place where the counterflow
touches open mathematics rather than bookkeeping, and it is one long-running computation to test.

## 2. Base-general key theory

The gain from the twin condition is $3/\gcd(3,b)$: real in base 10, absent in base 9, expected to be
real in 8, 16 (not divisible by 3) and absent in 12, 30, 210 except through their own 3. The level
structure and the mod-$\mathrm{lcm}$ closure generalise. A note's worth of arithmetic, low risk,
fully checkable — build the same three keys for $b\in\{8,12,16,30,210\}$ and tabulate resolution and
spread.

## 3. The flattening law

Cell-count spread goes 2.00 → 1.19 → 1.03 (base 10) and 2.66 → 1.15 → 1.05 (base 9) as levels
aggregate. Is the rate a function of the modulus, of the number of cells, or of the number of summed
gaps? Five levels of data would answer it. Cheap, and it is the quantitative form of Holt's
transience.

## 4. Mod 90 as a filter

99.76 % of consecutive-prime gaps are pinned by the pair (end-digit key, mod-9 key). That is a clean
structural statement about gaps; it is not a sieve improvement (the residues are already forced by
the two numbers) and should not be sold as one.

## Closed — do not spend time here

- **Merging further.** Level 4+ leaves resolution at mod 30 / mod 9. Nothing new appears; only cell
  counts tighten (1.03 → 1.01).
- **Dimension as an independent coordinate.** Inner-node count correlates +0.973 with the segment's
  decade span. It is a restatement of window size, not a new axis.
- **Any dynamical/physical reading.** The sequence of twin-start gaps is white (lags 1–24 inside
  ±0.0032); no propagation, no wave, no refraction.
- **Any claim resting on the last-digit bias as a constant.** It is transient and reverses.

## The one honest sentence to put at the top of the paper

*The keys are exact and the ladder is real; the counts in the cells carry the known last-digit bias
and nothing more; the only place the model touches open mathematics is runs of equal twin-start
gaps, i.e. twin pairs in arithmetic progression.*
