# New perspective: the two models, the harmonic levels, the subset sequence

Everything below is measured on the first 5 000 000 primes (`harmonic_levels.py`).

---

## 1. Base Prime Pattern — what it actually is

Writing every prime as $p = 10s + d$ splits each gap into two channels:

$$g = 10\,\Delta s + \Delta d,\qquad \Delta s = \text{subset step},\quad \Delta d = \text{end-digit step}$$

This is exact for every consecutive pair (4 999 999 / 4 999 999) and needs no prime beyond the
two numbers. The **subset sequence** is the running sum of $\Delta s$, started at 0.

The sharp version, which I had not stated before:

$$\boxed{\Delta s = \left\lfloor \frac{g}{10}\right\rfloor + \mathbb{1}[\Delta d < 0]}$$

The subset step is the gap's tens part **plus a carry whenever the end digit wraps downward**.
Verified exactly: every gap with $\Delta d<0$ (39.73 % of them) is a $+1$ carry, and nothing else is.

So the subset sequence is not mysterious: **it is the integral of the gaps' tens parts, plus a
counter for downward digit wraps.** Every sequence is non-decreasing, every sequence starts at 0
by construction, and the absolute location of the segment is destroyed by the normalisation —
only the shape survives.

### Information split (bits per gap)

| quantity | bits |
|---|---:|
| entropy of a gap $H(g)$ | 4.378 |
| left after knowing $\Delta s$ | 2.729 → the subset channel removes **1.649** |
| left after knowing $\Delta d$ | 2.068 → the digit channel removes **2.310** |
| left after knowing both | **0** |

The end digit is the *richer* channel, which is the opposite of the intuition that the big number
carries the information. $\Delta d$ is nearly uniform over its nine values ($H = 3.067$ of a
possible 3.170), so it behaves like a full 3-bit remainder; $\Delta s$ is concentrated on 0, 1, 2
and carries the *size*, not the identity.

## 2. Twin Prime Counterflow — two parts, only one of which is a law

| part | statement | status |
|---|---|---|
| **the exchange** | $B_k = A_{k+1}$: the offset column of row $k$ *is* the difference column of row $k+1$ | identity, 385 372/385 372 = 100 % |
| **the equilibrium** | $d_k = d_{k+1}$, the row reads $x:x$ | 1.011 %, and **forbidden in 4 of 9 key cells** |

The exchange is a single sequence flowing diagonally down-left; it cannot fail because `ep` is
defined from the next `bg`. The equilibrium is the real content: whether it can occur at all is
decided by the digit of the **third** twin start, $2v-u \bmod 10$, which must be 1, 7 or 9.

So the counterflow is a three-term relation wearing a two-row costume. That is why it looked
patternless when written as a balance between two rows.

## 3. Harmonic levels

A level-$L$ key is the last $L$ digits: $(p \bmod 10^L,\ q \bmod 10^L) \mapsto g \bmod 10^L$.

| level | modulus | gaps determined exactly | note |
|---:|---:|---:|---|
| 1 | 10 | 34.698 % | the base end-digit key, 16 cells |
| 2 | 100 | **99.887 %** | last two digits give the gap outright |
| 3 | 1000 | 100 % | nothing left to determine |

**Two digits of key resolve the gap for 99.9 % of all consecutive pairs.** That is the strongest
statement in the whole construction and it is one line of arithmetic.

The twin keys sit on a different rung. Because a twin-anchored span is $\equiv 2 \pmod 6$,

| key | resolution at level 1 |
|---|---|
| base end-digit key | $g \bmod 10$ — five classes |
| **twin / smashed key** | **$g \bmod 30$** — one class per last digit |

Matched by last digit: `0→20`, `2→2`, `4→14`, `6→26`, `8→8`.

So the twin structure buys exactly a factor of **3** in resolution, and the factor is 3 because 3 is
the prime the twin condition excludes. That, I think, is what "harmonic level" is measuring: the
modulus ladder 10 → 30 → 100 → 300 → 1000, with the twin keys one rung above the base keys at the
same digit count.

## 4. The subset sequence, measured

385 374 sequences, one per segment:

| property | value |
|---|---|
| always starts at 0 | yes, by construction |
| non-decreasing | yes, every one |
| length (= inner nodes, "dimension") | mean 12.97, median 10, max 151 |
| last value (decades spanned) | mean 22.0, max 283 |
| correlation length vs last value | **+0.973** |
| mean step per node | 1.84 decades |

The +0.973 is the important number. **The "dimension" and the segment's span in decades are almost
the same measurement** — the inner-node count is essentially the size of the window, so it cannot be
an independent geometric property. It is a restatement of how many decades the segment covers, which
is why it tracks prime density and nothing else.

What the sequence does genuinely carry: the shape of the carry pattern. Two segments with the same
digits and the same length can differ only in *where* the carries fall, and that is exactly the
information the normalisation was designed to keep.

## Summary in five lines

1. $g = 10\Delta s + \Delta d$: two channels, both needed, neither sufficient.
2. $\Delta s = \lfloor g/10\rfloor + \mathbb{1}[\Delta d<0]$: the subset sequence is a carry counter.
3. The counterflow exchange is an identity; the equilibrium is a three-term key constraint.
4. Level-2 keys determine the gap exactly for 99.887 % of pairs; twin keys are worth a factor of 3.
5. The inner-node "dimension" is the segment's decade span (r = 0.973), not a new coordinate.
