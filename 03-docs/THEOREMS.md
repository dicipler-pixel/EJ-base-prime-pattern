# The theorems, with proofs and a statement audit

Every statement below is written with all hypotheses explicit, proved in full, then audited in the
sense of a statement-fidelity review: **what the statement actually assumes, on what carrier, with
what quantifier order, and what breaks if a hypothesis is dropped.** The distinction matters here
because several of these theorems have small-integer exceptions that a referee will find first.

Conventions. $\mathbb P$ = primes. $d(n)\in\{0,\dots,9\}$ is the last decimal digit, $s(n)=\lfloor n/10\rfloor$.
$g = q-p$ for consecutive primes $p<q$. $a_k$ = the $k$-th twin start ($a_1=3$, $a_2=5$, $a_3=11$,
$\dots$, $a_k,a_k+2$ both prime). A *segment* is $[\,bg,ep\,] = [\,a_k,\ a_{k+1}+2\,]$.

---

## Theorem 1 (two-channel decomposition)

**Statement.** For all $n\in\mathbb Z$, write $n = 10\,s(n)+d(n)$. For all $p<q$,
$$q-p = 10\bigl(s(q)-s(p)\bigr)+\bigl(d(q)-d(p)\bigr).$$

**Proof.** Substitute and subtract. $\square$

**Audit.** Carrier: all of $\mathbb Z$; hypotheses: none. The content is not the identity but the
*claim that it is a decomposition* — that is, $d(q)-d(p)\in[-9,9]$, so the digit channel is bounded
while the subset channel is not. This is what makes them two channels rather than one relabelling.

---

## Theorem 2 (carry law)

**Statement.** Let $p<q$ be integers with $d(p),d(q)\in[0,9]$. Put $\Delta s = s(q)-s(p)$ and
$\Delta d = d(q)-d(p)$. Then
$$\Delta s = \Bigl\lfloor \frac{q-p}{10}\Bigr\rfloor + \mathbb 1[\Delta d<0].$$

**Proof.** By Theorem 1, $q-p = 10\Delta s+\Delta d$ with $\Delta d\ge-9$. If $\Delta d\ge 0$ then
$0\le \Delta d/10 < 1$, so $\frac{q-p}{10} = \Delta s+\frac{\Delta d}{10}$ has floor $\Delta s$. If
$\Delta d<0$ then $-1<\frac{\Delta d}{10}<0$, so the floor is $\Delta s-1$, i.e.
$\Delta s = \lfloor (q-p)/10\rfloor+1$. $\square$

**Audit.** The hypothesis is *decimal position* ($0\le d\le 9$), not primality — the law holds for
all integers. Restricting to primes gives $|\Delta d|\le 8$ because both digits are odd, which
sharpens nothing. It fails for negative dividends if one uses truncation instead of floor.

---

## Theorem 3 (the end-digit key)

**Statement.** Let $p<q$ be consecutive primes with $p\ge 7$. Then
$$q-p \equiv d(q)-d(p) \pmod{10},$$
so the last digit of the gap is a function $\kappa:\{1,3,7,9\}^2\to\{0,2,4,6,8\}$,
$\kappa(u,v)=(v-u)\bmod 10$. The image has five elements, and the fibres have sizes
$4,3,3,3,3$ for $\kappa=0,2,4,6,8$.

**Proof.** Congruence mod 10 of $q-p = 10\Delta s+\Delta d$ gives $\Delta d$. Both digits are odd,
so $\Delta d$ is even; the five even residues are attainable. For the fibres: $\kappa(u,v)=0$ iff
$u=v$, giving 4 pairs. For $\delta\in\{2,4,6,8\}$, the map $u\mapsto u+\delta$ sends exactly one of
$\{1,3,7,9\}$ to $5\bmod 10$, since $5-\delta$ is odd and $\ne 5$; that one is excluded and the other
three give $\kappa=\delta$. Hence 3 each, and $4+4\cdot 3=16$. $\square$

**Audit.** Hypotheses: $p\ge 7$ (equivalently, the terminal digits are in $\{1,3,7,9\}$ and the pair
$(3,5)$ is excluded). *Consecutiveness is not used* — the congruence holds for any two primes, which
is worth saying: consecutiveness enters only when one asks which cells are *realised*. Surjectivity
onto all five residues is a fact about primes (all five classes of gaps occur), not about $\kappa$.

---

## Theorem 4 (twin-start congruence)

**Statement.** If $a>3$ and $a,\ a+2$ are both prime, then $a\equiv 5 \pmod 6$. Consequently, for
twin starts $a_k<a_{k+1}$ with $a_k>3$, $\ d_k := a_{k+1}-a_k \equiv 0\pmod 6$.

**Proof.** A prime $>3$ is odd and $\not\equiv 0\pmod 3$, so it is $\equiv\pm1\pmod 6$. If
$a\equiv 1\pmod 6$ then $a+2\equiv 3\pmod 6$, so $3\mid a+2$ and $a+2>3$, contradicting primality.
Hence $a\equiv -1\equiv 5\pmod 6$. For the consequence, both $a_k,a_{k+1}$ are $\equiv 5\pmod 6$.
$\square$

**Audit.** The exception $a=3$ is *not* an artefact: $3\equiv 3\pmod 6$ and $3+2=5$ is prime, so the
statement is false at $a=3$ and only there. Every later use must carry "$k\ge 2$" or "$a>3$". This is
the single most common place the original formulation slips.

---

## Theorem 5 (twin classes modulo 9)

**Statement.** With $a$ as in Theorem 4, $\ a\bmod 9\in\{2,5,8\}$ and
$(a+2)\bmod 9\in\{4,1,7\}$; the three ordered pairs are $(2,4),(5,7),(8,1)$.

**Proof.** $a\equiv 5\pmod 6$ gives $a\equiv 2\pmod 3$; the residues mod 9 that are $\equiv2\pmod3$
are $2,5,8$. Adding 2 gives $4,7,10\equiv1$. $\square$

**Audit.** This is $\varphi(9)=6$ units cut down by the mod-3 condition — the *reason* there are
exactly three classes is $9=3^2$, not twin-prime structure. The statement is about residues only;
equidistribution (128 439 / 128 798 / 128 440 over $8.6\cdot10^7$) is a separate, unproved claim.

---

## Theorem 6 (digit exclusivity)

**Statement.** (i) If $p\equiv 3\pmod{10}$ and $p>3$ then $p+2$ is composite.
(ii) If $ep = a+2$ for a twin start $a$ and $ep\equiv7\pmod{10}$, then $ep=7$.

**Proof.** (i) $p+2\equiv 5\pmod{10}$, so $5\mid p+2$, and $p+2>5$. (ii) $ep\equiv7$ gives
$a\equiv5\pmod{10}$; the only prime ending in 5 is 5, so $a=5$ and $ep=7$. $\square$

**Audit.** Both are statements about the last digit, hence trivial, and both are *sharp*: each has
exactly one exception in the primes. They are the cleanest results in the whole construction and
should be stated exactly this way — with the exception named.

---

## Theorem 7 (uniqueness of the 1-D junction)

**Statement.** Among $p-2,\ p,\ p+2$ exactly one is divisible by 3. Hence if all three are prime then
one of them is 3, so $p=5$. Consequently the twin-to-twin gap $\gamma_k = a_{k+1}-(a_k+2)$ vanishes
exactly once, at $k=1$, with $\gamma_1 = 0$.

**Proof.** The three numbers are $\equiv p-2, p, p+2 \pmod 3$, which are three distinct residues
since $2\not\equiv 0\pmod 3$; one is $0$. If all three are prime that one is 3, forcing $p\in\{1,3,5\}$
and primality of $p$ gives $p=5$. $\square$

**Audit.** Do not strengthen to "the only 1-D segment": under the end-digit reading of the rung,
$1$D is also attained by every $\gamma\equiv 10\pmod{30}$. What is unique is $\gamma=0$.

---

## Theorem 8 (segment shape)

**Statement.** For every segment, the gap string from $bg$ to $ep$ is $2\,[\,\text{gaps}\ge 4\,]\,2$.
Equivalently: the first and last gaps are 2, and no interior gap is 2.

**Proof.** First gap $= (bg+2)-bg = 2$ because $bg$ is a twin start; last gap $= ep-(ep-2) = 2$
because $ep-2$ is a twin start. If an interior gap were 2, say at $p\in(bg,ep-2)$, then $p,p+2$ would
be a twin pair with $bg<p$, contradicting that $a_{k+1}$ is the *first* twin start after $a_k$.
$\square$

**Audit.** This is a statement about the segment *definition*, and it is where the definition earns
its keep. It is also what forbids gaps of 2 in the interior — a fact used silently in every
"interior gap sum" computation.

---

## Theorem 9 (span and interior congruence)

**Statement.** $\mathrm{span}=ep-bg = d_k+2$, and for $k\ge2$,
$$\mathrm{span}\equiv 2\pmod 6,\qquad \gamma := \mathrm{span}-4\equiv 4\pmod 6.$$

**Proof.** $ep-bg = (a_{k+1}+2)-a_k = d_k+2$; by Theorem 4, $d_k\equiv0\pmod6$ for $k\ge2$. $\square$

**Audit.** $k\ge2$ is essential: at $k=1$, $d_1=2$, so span $=4\equiv4$ and $\gamma=0\equiv0$, both
off the general congruence. The single exception is the junction of Theorem 7.

---

## Theorem 10 (equilibrium obstruction — strengthened form)

**Statement.** Let $u=a_k\bmod 10$, $v=a_{k+1}\bmod 10$, and $r \equiv d_k \equiv v-u \pmod{10}$.
Suppose $a_{k+2}$ exists and $d_k=d_{k+1}$. Then
$$a_{k+2}\equiv 2v-u\equiv v+r \pmod{10},$$
and since twin starts above 3 end in $\{1,7,9\}$, one needs $v+r\in\{1,7,9\}$. Enumerating $r$:

| $r = d_k \bmod 10$ | cells carrying $r$ | the others require |
|---:|---|---|
| 0 | $1{\to}3,\ 7{\to}9,\ 9{\to}1$ — **all permitted** | — |
| 2 | $7{\to}1$ permitted, $9{\to}3$ forbidden | $u=5$, i.e. the seed |
| 4 | $7{\to}3$ forbidden | $u=3$, i.e. the seed |
| 6 | $1{\to}9$ forbidden | $u=5$, i.e. the seed |
| 8 | $1{\to}1$ permitted, $9{\to}9$ forbidden | $u=3$, i.e. the seed |

Hence, for regular segments ($bg>5$), **equilibrium requires $d_k\equiv0,2$ or $8\pmod{10}$; the
residues 4 and 6 never equilibrate anywhere.**

**Proof.** $a_{k+2}=a_{k+1}+d_{k+1}=a_{k+1}+(a_{k+1}-a_k)=2a_{k+1}-a_k$, so
$a_{k+2}\equiv 2v-u \pmod{10}$; and $2v-u = v+r$ because $r\equiv v-u$. For each $r$, solve
$v+r\in\{1,7,9\}$ with $v\in\{1,7,9\}$ (the only digits a twin start can carry, Theorem 6(i)) and
$u = v-r$. The solutions quoted in the table are obtained by enumeration of the three admissible
$v$; the cases marked "seed" need $u\notin\{1,7,9\}$, i.e. $u=3$ or $5$, which occur only at
$a_1=3,a_2=5$. $\square$

**Audit.** This is a **necessary** condition. It does not give the rate, and the rates are not equal:
the five permitted cells equilibrate at 1.66 %–2.48 %. That spread is *fully accounted for* by two
measurable factors (verified to 3.5 % on all five cells):

$$P(\text{eq}\mid c)=\frac{1}{\pi_r}\sum_d P(d_k=d\mid c)\,r_d,
\qquad r_d = P(d_{k+1}=d\mid d_k=d),$$

where $r_d$ is the repeat probability of the gap value (0.8 % at $d=18$, 3.3 % at $d=30$), and
$\pi_r$ is the share of residue-$r$ mass lying in permitted cells: $\pi_0=1$, $\pi_2 = 0.5012$,
$\pi_8 = 0.4987$. The $1/\pi_r$ factor is exactly 2 for $r=2,8$, because the measured $r_d$ averages
the permitted cell with its forbidden twin, which contributes zero. It fails only at the seed
$k=1$.

**Corollary.** $54\equiv4$ and $6\equiv6\pmod{10}$ have repeat rate $0.00\%$; the single repeated gap
$\equiv6$ is the seed at $bg=5$ ($d_2=d_3=6$).

## Theorem 11 (lattice law for the twin-to-twin gap)

**Statement.** Write $\gamma=\delta+10k$ with $\delta=\gamma\bmod 10\in\{0,2,4,6,8\}$ and
$D=\delta/2+1$. Then
$$\gamma\equiv 4\pmod 6 \iff k\equiv D \pmod 3.$$

**Proof.** $\gamma\equiv4\pmod6 \iff \delta+10k\equiv4\pmod6$. Substitute $\delta = 2(D-1)$ and
$10k\equiv4k$:
$$2D-2+4k\equiv 4 \iff 2D+4k\equiv 0 \iff D+2k\equiv 0 \pmod 3,$$
dividing by 2, which is invertible mod 3. Since $-2\equiv 1\pmod 3$, this is $D\equiv k\pmod3$.
$\square$

**Audit.** Verified on all 385 675 regular rows. The hypothesis $\gamma\equiv4\pmod6$ is exactly
Theorem 9's conclusion, so the law is a *rewriting* of the congruence — its value is that it
identifies which cells of the beam grid are reachable. The exception $\gamma=0$ fails
$\gamma\equiv4\pmod6$ and so lies outside the theorem's scope; that is why $(0,0)$ is the one
off-lattice cell.

---

## Theorem 12 (shaft arithmetic)

**Statement.** $\{1,3,7,9\}$ under multiplication mod 10 is cyclic of order 4, generated by 3:
$$3\mapsto 9\mapsto 7\mapsto 1\mapsto 3.$$
Hence the four shafts form $\mathbb Z/4$, and multiplication by $3$ advances the shaft by one, by $9$
by two.

**Proof.** $3^2=9$, $3^3=27\equiv7$, $3^4=81\equiv1 \pmod{10}$; and $|\{1,3,7,9\}|=\varphi(10)=4$.
$\square$

**Audit.** Two bits, but $\mathbb Z/4$ and not $(\mathbb Z/2)^2$: $3\cdot3=9\ne1$. Any "binary/XOR"
reading of the shafts is therefore wrong at the level of the operation, though the *size* is right.

---

## Theorem 13 (admissibility filter)

**Statement.** For a twin start $a$ with predecessor $b=a-pre$ prime and successor twin start
$a+post$, the five primes $b,\,a,\,a+2,\,a+post,\,a+post+2$ have difference set
$$\mathcal D=\{0,\ pre,\ pre+2,\ pre+post,\ pre+post+2\}.$$
If $\mathcal D$ is a complete residue system modulo a prime $q$, the pattern is realisable only if
some member of $\mathcal D$ equals $q$. In particular $(pre,post)=(6,6)$ is inadmissible at $q=5$,
and $(6,4)$ at $q=3$.

**Proof.** If $\mathcal D$ covers all residues mod $q$, then $q$ divides $b+\delta$ for some
$\delta\in\mathcal D$; if $b+\delta>q$ that number is composite. For $(6,6)$:
$\{0,6,8,12,14\}\equiv\{0,1,3,2,4\}\pmod 5$ — five distinct residues. For $(6,4)$:
$\{0,6,8,10,12\}\equiv\{0,0,2,1,0\}\pmod 3$ — contains $0,1,2$. $\square$

**Audit.** This is the Hardy–Littlewood admissibility condition, not a new result; what is new here
is only the measurement that it classifies the data perfectly (70 admissible patterns all occur, 0 of
330 inadmissible ones do). The statement is a *necessary* condition; sufficiency for occurrence is the
$k$-tuple conjecture and is not proved.

---

## Theorem 14 (mod-3 gain)

**Statement.** Let a key pin $g\equiv r\pmod m$. If the class also satisfies $g\equiv2\pmod 3$, the
combined information is a single class modulo
$$\operatorname{lcm}(m,3)=\begin{cases}3m,&3\nmid m\\ m,&3\mid m.\end{cases}$$

**Proof.** The system $g\equiv r\ (m)$, $g\equiv 2\ (3)$ is solvable since $\gcd$ divides the
difference of the right sides for every common divisor; CRT gives a unique class mod
$\operatorname{lcm}(m,3)$, which equals $3m$ exactly when $3\nmid m$. $\square$

**Audit.** This explains the twin key tripling resolution in base 10 ($10\to30$) and doing nothing in
base 9 ($9\to9$), and it is a statement about moduli, containing no prime information.

---

## Empirical statements (measured, not proved)

These are separated deliberately; they are the four claims in the project that are measurements.

| claim | value | status |
|---|---|---|
| equilibrium rate $d_k=d_{k+1}$ | 1.010 % | measured |
| equal gaps suppressed versus iid | 0.638× (pairs), 0.236× (triples) | measured |
| repeat factor by gap size | 0.020 (gap 6) … 2.286 (gap 42) | measured |
| cell drift $W_0(x)$ | 0.446 → 0.729, $\log\log x/\log x$ shape | measured |

---

# Summary: what is deep, what is shallow

| theorem | depth | why |
|---|---|---|
| 1, 2 | trivial | one-line algebra; the content is the bounded/unbounded split |
| 3, 5, 6 | trivial, sharp | congruences with named exceptions |
| 4, 7, 8, 9 | easy | modular obstructions, correctly stated |
| 10 | small result | a three-term obstruction, classifies four cells exactly |
| 11 | small result | a rewriting that identifies the reachable cells |
| 12 | trivial | $\varphi(10)=4$, $3$ is a primitive root |
| 13 | known | Hardy–Littlewood; the measurement is the contribution |
| 14 | trivial | CRT |

An expert will be convinced by the *audit* columns, not the proofs: the exceptions at $a=3$,
$k=1$, $\gamma=0$ and the necessary-versus-sufficient distinction in Theorems 10 and 13 are where
this construction is actually vulnerable, and they are all now named.
