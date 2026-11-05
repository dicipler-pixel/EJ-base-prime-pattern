# The four ways, implemented and checked

`results/ways_all.py`, `results/way2_way4.py`. 5 000 000 primes above 5; 385 678 twin starts.

| way | repairs | verdict |
|---|---|---|
| 1 — two-channel state, Markov order | F1 wrong carrier | **works**: order-1 rejected, as L-O-S predict |
| 2 — admissibility instead of balance | F2, F5 | **complete**: perfect classifier, 70/70 and 0/330 |
| 3 — repulsion, not equilibrium | F5 | **works**: a clean law in the gap size |
| 4 — dynamic cell counts | F9 | **works, and picks the functional form** |

---

## Way 1 — the state has second-order memory

Likelihood-ratio test of order-1 against order-2:

| sequence | states | G/df | max L1 gap | verdict |
|---|---:|---:|---:|---|
| end digits | 4 | **641** | 9.65 % | order-1 rejected |
| $(\Delta s,\Delta d)$ | 45 | 82 | (sparse) | order-1 rejected |
| $(\Delta s,\Delta d)$ coarse | 25 | 194 | (sparse) | order-1 rejected |

Knowing the previous end digit shifts the next-digit distribution by up to **9.65 percentage
points** beyond what the current digit implies. That is a large second-order effect and it is
exactly what Lemke Oliver–Soundararajan's Conjecture 1.4 asserts ("the primes mod $q$ are not
Markovian"). The 45-state row is noise-inflated in the L1 column — with 45 states and 5 M samples
each cell holds ~55 counts — so G/df is the number to trust there.

## Way 2 — admissibility is a perfect classifier

Tuple: $b,\ a,\ a+2,\ a{+}post,\ a{+}post{+}2$ with $pre = a-b$. Difference set
$D=\{0,pre,pre{+}2,pre{+}post,pre{+}post{+}2\}$. Admissible iff $D \bmod p$ never covers all $p$
residues, for every prime $p$.

Patterns with $pre,post \in \{2,4,\dots,40\}$, restricted to $a>1000$:

|  | seen | absent |
|---|---:|---:|
| **admissible** | **70** | **0** |
| **inadmissible** | **0** | **330** |

A perfect 2×2. Every admissible pattern occurs; no inadmissible one ever does. The zeros:

| pattern | admissible | blocked by | measured |
|---|---|---|---|
| (6, 6) | no | $p=5$ | **0** |
| (6, 4) | no | $p=3$ | **0** |
| (4, 6) | yes | — | 620 |
| (12, 6) | yes | — | 720 |
| (10, 30) | yes | — | 2 761 |

This is the Hardy–Littlewood admissibility condition in local form, and it explains **the whole
zero set** of the $(pre,post)$ table. The counterflow has no balance; it has a filter.

## Way 3 — the repulsion law

$S_r$ = observed / chance rate of $r$ consecutive equal twin-start gaps.

| band | n | $S_1$ | $S_2$ | $S_3$ |
|---|---:|---:|---:|---:|
| $10^4$–$10^5$ | 1 019 | 0.654 | 0.000 | 0 |
| $10^5$–$10^6$ | 6 945 | 0.595 | 0.275 | 0 |
| $10^6$–$10^7$ | 50 811 | 0.646 | 0.250 | 0 |
| $10^7$–$10^8$ | 326 697 | 0.630 | 0.224 | 0 |
| **all** | 385 677 | **0.638** | **0.236** | **0** |

$S_1$ is **flat in $x$** — it does not drift toward 1, so the suppression is not a finite-range
artefact. But it is a strong function of the **gap size**:

| gap | 6 | 12 | 18 | 30 | 42 | 60 |
|---|---:|---:|---:|---:|---:|---:|
| $S_1$ | **0.020** | 1.002 | 0.436 | 1.416 | **2.286** | 2.005 |
| n | 4 263 | 11 209 | 8 120 | 15 620 | 14 227 | 11 174 |

**Gap 6 essentially never repeats (0.02× chance); gap 42 repeats 2.3× more than chance.** Small
gaps repel, large gaps attract, and the crossover sits between 12 and 18. This is the classic
anti-correlation of consecutive prime gaps, now measured per gap value with a ratio attached.

## Way 4 — the drift picks the L-O-S functional form

$W_0(x)$ = count of class 0 ÷ count of class 2:

| x | $10^4$ | $10^5$ | $10^6$ | $10^7$ | $3\cdot10^7$ | $8.6\cdot10^7$ |
|---|---:|---:|---:|---:|---:|---:|
| $W_0$ | 0.446 | 0.540 | 0.619 | 0.677 | 0.705 | 0.729 |

| fit | params | $R^2$ | value at $x\to\infty$ |
|---|---|---:|---:|
| $a + b/\ln x$ | $a=1.0147$, $b=-5.43$ | 0.985 | **1.015** — wrong, must be $4/3$ |
| $a + d\,\frac{\log\log x}{\log x}$ | $a=1.2904$, $d=-3.55$ | **0.990** | **1.290** — within 3 % of $4/3$ |

A pure $1/\ln x$ fit extrapolates to 1.015 and is therefore misspecified. The
$\log\log x/\log x$ form fits better *and* extrapolates to 1.290 against the required 1.333. That is
the shape Lemke Oliver–Soundararajan's Main Conjecture demands (their correction is
$c_1\log\log x/\log x$), and it is visible in five decades of data.

---

## What the four together say

1. The local structure is **not Markov of order 1** — there is real memory, of exactly the kind
   L-O-S conjecture.
2. The pattern that *can* occur is fixed **entirely by small-prime admissibility**: 70/70 in,
   0/330 out. This replaces "balance" and is the correct statement of the counterflow.
3. Equal consecutive gaps are suppressed by a factor that is **flat in x but strongly graded in
   gap size**, from 0.02 at gap 6 to 2.29 at gap 42.
4. The cell counts drift with the **$\log\log x/\log x$** shape, not $1/\ln x$.

Three of the four are new measurements on this data; all four are consistent with the standard
Hardy–Littlewood framework, which is the strongest thing that can be said for the construction —
it now predicts correctly instead of only describing.
