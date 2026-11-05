# What is known: EJ's prime pattern, the counterflow, the two shafts

Everything below is verified on the first 5 000 000 primes above 5 (to 86 028 223), 385 678 twin
starts, 385 676 segments. Scripts: `verify_all.py` (24/24), `shaft_beam_cols.py`, `ways_all.py`.

---

# 1. EJ's prime number pattern

## The encoding

$$p=10s+d,\qquad d\in\{1,3,7,9\}\ (\text{shaft}),\quad s\ (\text{level})$$

Every gap splits into two channels, exactly:

$$g=10\,\Delta s+\Delta d\qquad\text{and}\qquad
\Delta s=\Big\lfloor\frac{g}{10}\Big\rfloor+\mathbb 1[\Delta d<0]$$

The subset step is the gap's tens part **plus a carry whenever the end digit wraps downward** —
39.73 % of gaps. Information per gap: 4.378 bits → 2.310 from the digit channel, 1.649 from the
subset channel, 0 left over.

## The base key

$g\equiv d_2-d_1\pmod{10}$. 16 cells, each pinning exactly one residue:

| | →1 | →3 | →7 | →9 |
|---|---:|---:|---:|---:|
| **1** | 0 | 2 | 6 | 8 |
| **3** | 8 | 0 | 4 | 6 |
| **7** | 4 | 6 | 0 | 2 |
| **9** | 2 | 4 | 8 | 0 |

Multiplicities $0{:}4,\ 2{:}3,\ 4{:}3,\ 6{:}3,\ 8{:}3$ — the diagonal has four members, every other
beam three.

## The twin structure

| fact | verification |
|---|---|
| twin starts $>3$ satisfy $a\equiv5\pmod6$ | proof: $3\nmid a$, $3\nmid a+2$ |
| twin-start gaps $d_k\equiv0\pmod6$ | same |
| $(a,a+2)\bmod9\in\{(2,4),(5,7),(8,1)\}$ | 128 439 / 128 798 / 128 440 |
| no twin start $>3$ ends in 3 | $a+2\equiv5$, $5\mid a+2$ — 0 occurrences |
| no segment end ends in 7 | $ep\equiv7\Rightarrow a=5\Rightarrow ep=7$ — 0 occurrences |
| exactly one 1D junction | `3bg 5 7ep`, $\gamma=0$ |

## Segments

$bg=a_k,\ ep=a_{k+1}+2$; span $=d_k+2\equiv2\pmod6$; interior gap sum
$\gamma=ep-bg-4\equiv4\pmod6$.

**Every segment's gap string is $2\cdot[\text{gaps}\ge4]\cdot2$** — bookended by the twin gaps, no 2
inside (385 373 / 385 373).

---

# 2. The twin prime counterflow

## What is exact

$$ep_i-ep_{i-1}=bg_{i+1}-bg_i\qquad\textbf{385 674 / 385 674}$$

The offset column of row $k$ *is* the difference column of row $k+1$. This is an identity — $ep$ is
defined from the next $bg$, so the $+2$ cancels — and it holds for any increasing sequence.

## What is not

The same-rung balance reduces to $d_k=d_{k+1}$: **1.010 %**, and *suppressed* to **0.64× chance**
(3 895 observed, 6 104 expected). Runs of three: 33 against 140 expected. Equal consecutive gaps are
avoided, not balanced.

## The one real constraint

**Equilibrium is impossible in four of the nine key cells.** If $d_k=d_{k+1}$ then
$a_{k+2}\equiv2v-u\pmod{10}$ with $v=(ep-2)\bmod10$, $u=bg\bmod10$; twin starts end in 1, 7, 9.

| cell | possible | equilibria | cell | possible | equilibria |
|---|---|---:|---|---|---:|
| 1→3 | yes | 661 | 7→3 | **no** | 0 |
| 1→1 | yes | 709 | 7→1 | yes | **1 154** |
| 1→9 | **no** | 0 | 7→9 | yes | 681 |
| 9→1 | yes | 690 | 9→3 | **no** | 0 |
| 9→9 | **no** | 0 | | | |

## What binds the pattern: admissibility

The 5-tuple $b,a,a+2,a{+}post,a{+}post{+}2$ occurs *only if* its difference set is not a complete
residue system mod any prime. The converse is the prime-tuples conjecture and is not proved; the
table below is an observation in the tested range. Tested on all $(pre,post)$ patterns with $pre,post\in\{2,\dots,40\}$:

**admissible & seen 70 · admissible & absent 0 · inadmissible & seen 0 · inadmissible & absent 330**

A perfect 2×2. The $(6,6)$ pattern is blocked by $p=5$, $(6,4)$ by $p=3$.

## Repulsion, measured

| gap | 6 | 12 | 18 | 30 | 42 | 60 |
|---|---:|---:|---:|---:|---:|---:|
| repeat vs chance | **0.020** | 1.002 | 0.436 | 1.416 | **2.286** | 2.005 |

Small gaps repel, large gaps attract, crossover between 12 and 18, and the factor is flat in $x$.

---

# 3. The vertical and horizontal shafts

## Vertical — the shafts (2 bits)

$p=10s+d$: four shafts $\{1,3,7,9\}$, level $s$, one level per $+10$.

| shaft | primes below 8.6·10⁷ |
|---:|---:|
| 1 | 1 249 833 |
| 3 | 1 250 195 |
| 7 | 1 250 079 |
| 9 | 1 249 893 |

- within a shaft the gaps are **always multiples of 10** (10, 20, 30, …, 80 and no others)
- a **vertical move** is $g\equiv0\pmod{10}$: **17.12 %** of consecutive pairs
- shaft arithmetic is $\mathbb Z/4$: $\times3$ cycles $3\to9\to7\to1\to3$
- staying in the shaft is the *least* likely move in every row of the transition table (16.6–17.7 %)

## Horizontal — the beams (base 5)

$g=10k+\delta$, $\delta\in\{0,2,4,6,8\}$; rung $D=\delta/2+1$.

| beam | rung | count | share | most common gap |
|---:|---:|---:|---:|---:|
| 0 | 1 | 856 199 | 17.12 % | 10 |
| 2 | 2 | 1 175 259 | 23.51 % | 12 |
| 4 | 3 | 999 177 | 19.98 % | 4 |
| 6 | 4 | 1 118 991 | 22.38 % | 6 |
| 8 | 5 | 850 373 | 17.01 % | 18 |

**16 shaft transitions → 5 beams**, multiplicities $4,3,3,3,3$; the four-member fibre is the
diagonal, and **beam 2 is exactly the three twin transitions** $1{:}3,\ 7{:}9,\ 9{:}1$.

## The two together

| | vertical | horizontal |
|---|---|---|
| coordinate | shaft (4 = 2 bits) | beam (5) |
| counter | level $s$ | level $k$ |
| step | $+10$ in the prime | $+10$ in the gap |
| rung step per gap step | $+1 \bmod 5$ (gap step 2) | $+3 \bmod 5$ (twin step 6) |
| lattice | fully populated | $k\equiv D\!\!\pmod 3$ on the twin counting |

**The lattice law.** On the twin-to-twin gap $\gamma=\delta+10k$:

$$\gamma\equiv4\!\!\pmod6\iff D\equiv k\!\!\pmod3$$

verified on 385 675 rows. Each beam lives on one residue class of $k$: 1D and 4D on $k\equiv1$, 2D and
5D on $k\equiv2$, 3D on $k\equiv0$.

**The one exception.** $\gamma=0$ (the `3 5 7` junction) is not $\equiv4\pmod6$, so it sits at
$(0,0)$ — off its own beam's lattice. It is the origin of the lattice, not a member of it.

---

# 4. What is not true, and should not appear in the write-up

| claim | measured |
|---|---|
| the subset sequence alone determines the gaps | false — 11 898 of 243 008 tuples conflict; carry the digit channel |
| the balance holds universally | 1.010 %, and suppressed |
| the period-4–6 wave | lag-1 autocorrelation −0.5047, nothing after |
| Snell-type refraction at the joints | residual = shuffled null, every index |
| a cell count is a constant | $W_0$ drifts 0.446 → 0.729 → 4/3, with a $\log\log x/\log x$ shape |
| density of light falls with dimension | no — 5D is the commonest rung |
