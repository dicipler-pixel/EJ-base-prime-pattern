# The verified fact base

Rebuilt from scratch. Every statement below is re-derived and checked by
`results/verify_all.py` — **24 / 24 PASS** over 5 000 000 primes above 5 (to 86 028 223) and
385 678 twin starts. Nothing unverified is included; the retracted list is at the end.

---

## 1. Encoding

| # | fact | proof / verification |
|---|---|---|
| A1 | every $p>5$ ends in 1, 3, 7 or 9 | all 5 000 000 |
| A2 | all 16 ordered pairs of end digits occur | 16 cells |
| A3 | $g = 10\,\Delta s + \Delta d$ | $q-p=(10s_q+d_q)-(10s_p+d_p)$; 4 999 999 pairs |
| A4 | $\Delta s = \lfloor g/10\rfloor + \mathbb 1[\Delta d<0]$ | since $\lvert\Delta d\rvert\le 8$, $\Delta d\ge0 \Rightarrow \lfloor g/10\rfloor=\Delta s$ and $\Delta d<0\Rightarrow \lfloor g/10\rfloor=\Delta s-1$ |

The subset step is the gap's tens part **plus a carry for every downward digit wrap**. Verified
exactly; the carries are exactly the 39.73 % of gaps with $\Delta d<0$.

## 2. The base end-digit key

| # | fact | verification |
|---|---|---|
| B1 | $g \equiv d_2-d_1 \pmod{10}$ for every consecutive pair | 4 999 999 |
| B2 | 16 cells, one gap residue each | 16 / 16 |
| B3 | residue multiplicities $0{:}4,\ 2{:}3,\ 4{:}3,\ 6{:}3,\ 8{:}3$ | exact |

## 3. Twin structure

| # | fact | proof / verification |
|---|---|---|
| C1 | twin starts $>3$ satisfy $a\equiv 5 \pmod 6$ | $3\nmid a$ and $3\nmid a+2$ force $a\equiv2 \pmod 3$ |
| C2 | $d_k = a_{k+1}-a_k \equiv 0 \pmod 6$ above the first | same congruence |
| C3 | $(a,a+2)\bmod 9 \in \{(2,4),(5,7),(8,1)\}$ | units mod 9 are $\{1,2,4,5,7,8\}$; $a\equiv2\pmod3\Rightarrow a\in\{2,5,8\}$ |

Counts: (2,4) 128 439 · (5,7) 128 798 · (8,1) 128 440.

## 4. Segments

| # | fact | proof / verification |
|---|---|---|
| D1 | $ep_k = a_{k+1}+2$, span $=d_k+2$ | exact |
| D2 | span $\equiv 2 \pmod 6$ on all regular segments | $d_k\equiv0$ |
| D3 | no regular $bg$ ends in 3 | $a\equiv3\pmod{10},\ a>3 \Rightarrow a+2\equiv5$, $5\mid a+2$ |
| D4 | no regular $ep$ ends in 7 | $ep\equiv7\Rightarrow a\equiv5\Rightarrow a=5\Rightarrow ep=7$ |
| D5 | exactly one 1-D segment in 5 000 000 primes: `3bg 5 7ep` | one of $p-2,p,p+2$ is divisible by 3 |

## 5. Counterflow

| # | fact | verification |
|---|---|---|
| E1 | $ep_i-ep_{i-1}=bg_{i+1}-bg_i$ **identically** | 385 674 / 385 674, since $ep_i=bg_{i+1}+2$ |
| E2 | equilibrium $d_k=d_{k+1}$ is **rare** | 3 895 / 385 674 = **1.010 %**, and *suppressed*: 0.64× chance |
| E3 | equilibrium possible exactly when $2v-u\in\{1,7,9\}$, $v=(ep-2)\bmod10$, $u=bg\bmod10$ | 9 / 9 cells agree |

E3 proof: if $d_k=d_{k+1}$ then $a_{k+2}=2a_{k+1}-a_k\equiv2v-u \pmod{10}$; twin starts end in
1, 7 or 9, so $2v-u\in\{1,7,9\}$ is required. Measured:

| cell | possible | equilibria | cell | possible | equilibria |
|---|---|---:|---|---|---:|
| 1→3 | yes | 661 | 7→3 | **no** | 0 |
| 1→1 | yes | 709 | 7→1 | yes | **1 154** |
| 1→9 | **no** | 0 | 7→9 | yes | 681 |
| 9→1 | yes | 690 | 9→3 | **no** | 0 |
| 9→9 | **no** | 0 | | | |

## 6. Keys

| # | fact | verification |
|---|---|---|
| F1 | twin key mod 10 has 9 real cells, residues $\{0,2,4,6,8\}$ | exact |
| F2 | twin key mod 9 has 9 real cells, $bg\in\{2,5,8\}$, $ep\in\{1,4,7\}$ | exact |
| F3 | $\mathrm{lcm}(10,9)=\mathrm{lcm}(30,9)=90$; 99.76 % of gaps are $<90$ | exact |

## 7. Runs and admissibility

| # | fact | verification |
|---|---|---|
| G1 | equal consecutive twin gaps are **rarer than chance** | obs 3 895 vs iid 6 104 (0.64×) |
| G2 | three in a row still rarer | obs 33 vs iid 140 (0.24×) |
| G3 | $P(\text{post gap}=6 \mid \text{pre gap}=6)=0$ | 0 of 44 393 |

G3 proof: the five primes would be $a-6,a,a+2,a+6,a+8$; differences $0,6,8,12,14\equiv0,1,3,2,4
\pmod 5$ — a complete residue system, so one member is divisible by 5 and exceeds 5.

---

# Enhancements — three statements that generalise the above

## H1. The mod-3 gain theorem

*If a key pins $g\bmod m$ and the class also satisfies $g\equiv2\pmod 6$, the combined resolution is
$3m$ when $3\nmid m$, and $m$ when $3\mid m$.*

Proof: the constraints $g\equiv r \pmod m$ and $g\equiv 2\pmod 3$ have a unique solution mod
$\mathrm{lcm}(m,3)$ exactly when they are compatible; compatibility is automatic because
$g\equiv2\pmod6$ already forces $g\bmod 3=2$.

This is why the twin key triples resolution in base 10 (10 → 30) and does nothing in base 9
(9 → 9). It is a property of the modulus, not of the primes.

## H2. The admissibility filter

*A pattern of twin starts is realised only if its difference set is not a complete residue system
modulo any prime $p$.*

The (6,6) pattern is the first non-trivial case and it is measured at exactly zero. This replaces
"balance" as the binding constraint: the counterflow's real content is where the tuple fails
admissibility, not where two differences happen to agree.

## H3. The carry theorem

$\Delta s=\lfloor g/10\rfloor+\mathbb 1[\Delta d<0]$.

Together with A3 this makes the subset sequence a *derived* object: it is the integral of the gaps'
tens parts plus a counter for digit wraps. It is not an independent coordinate, and the +0.973
correlation between inner-node count and decade span (measured earlier) is consistent with that.

---

# Not claimed — removed

- the counterflow balance as a universal law (1.010 %, suppressed);
- the back-trace column as a prediction (a two-row shift);
- Conjecture 6 as stated (needs the digit channel: use $g=10\Delta s+\Delta d$);
- the period-4–6 wave (lag-1 autocorrelation $-0.5047$, nothing after lag 1);
- Snell-type refraction at the joints (residual = shuffled null);
- the chromatic addition rules as arithmetic ($R+W=4\neq6$);
- any cell count quoted as a constant (all drift; $W_0$: 0.446 → 0.729 → 4/3).

# The programme that remains

1. **Admissibility (H2).** Enumerate every $(pre,post)$ pattern, compute the admissible set from
   difference sets mod 5, 7, 11, and check counts against the Hardy–Littlewood singular series.
2. **The 0.64× suppression (G1).** Fit the suppression factor as a function of gap size and $x$.
3. **H1 across bases.** Verify the $3m$ / $m$ rule for $m\in\{8,12,16,30,210\}$.
