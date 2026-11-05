# Proposed addition to the manuscript
## § Verifying the pattern: a certified primality test

*Text to insert after the Mod 9 Counterflow section.*

The two modular theorems of this paper are stated there as filters on gaps. They are also, jointly,
a correct primality test, and the purpose of this section is to state that test, prove it, and report
its verification.

### Theorem A (the test)

For an integer $n>5$, $n$ is prime if and only if

1. $n\bmod 10\in\{1,3,7,9\}$ *(the end-digit key)*;
2. $3\nmid n$ and $5\nmid n$ *(the mod-3 and mod-5 keys)*;
3. no $m$ with $7\le m\le\lfloor\sqrt n\rfloor$ and $\gcd(m,30)=1$ divides $n$.

*Proof.* A prime $n>5$ is coprime to $30$ and has no divisor in $[7,\sqrt n]$. Conversely, if $n$ is
composite write $n=ab$ with $1<a\le b<n$; then $a\le\sqrt n$. Conditions 1–3 give $\gcd(n,30)=1$,
hence $\gcd(a,30)=1$; if $a\le5$ then $2,3$ or $5$ divides $n$, contrary to 2. Hence $a\ge7$ is one
of the integers tested in 3, and 3 fails. $\square$

Conditions 1–2 are precisely the key of Theorem 3 and its mod-3 refinement; condition 3 is the
iteration of the key over successive wheels.

### Corollary B (how far the key alone reaches)

Conditions 1–2 alone decide primality for every $n<49$. The least composite coprime to $30$ is
$7^2=49$, since every composite coprime to $30$ has all prime factors $\ge7$.

More generally, with the wheel $P=p_1\cdots p_k$ and $p=p_{k+1}$, the key $\gcd(n,P)=1$ is exact for
$n<p^2$:

| wheel $P$ | density $\varphi(P)/P$ | first counterexample | exact for |
|---:|---:|---:|---:|
| 30 | 0.2667 | 49 | $n<49$ |
| 210 | 0.2286 | 121 | $n<121$ |
| 2310 | 0.2078 | 169 | $n<169$ |
| 30030 | 0.1918 | 289 | $n<289$ |

This is the precise sense in which the pattern decides primality: **it refutes always, and confirms
exactly up to $p_{k+1}^2$.**

### Corollary C (the twin form)

For $n>3$, the pair $(n,n+2)$ is a twin-prime pair if and only if

$$n\equiv5\pmod6,\qquad 5\nmid n(n+2),\qquad
\forall m\in[7,\sqrt{n+2}],\ \gcd(m,30)=1:\ m\nmid n(n+2).$$

The first condition is the twin-start congruence of Theorem 4; it reduces the search for twin pairs
to one residue class mod 6, against four classes mod 10 for a single prime.

### Verification

The test was run against a complete sieve:

| scope | size | disagreements |
|---|---:|---:|
| exhaustive, $7\le n\le200\,000$ | 199 994 | **0** |
| random, $n\in[2\cdot10^5,10^8]$ | 3 000 | **0** |
| twin test, $n\le200\,000$ | 26 666 starts | **0** |
| key alone, $n<49$ | 42 | exact, first failure $49=7^2$ |

Cost over the exhaustive range: 1 829 848 division tests for 199 994 integers, against 59 328 924
for full trial division.

### Remark on the limits

No finite key decides primality, because $p_{k+1}^2$ always passes the key of $p_1\cdots p_k$ and is
composite. The deductive content of the pattern is therefore exactly the wheel; the remainder of the
construction — the gap distribution, the counterflow, the shafts — is a description of the sequence
of primes rather than a test of an individual one. This distinction is worth preserving in any
exposition, since it is the line between what the pattern proves and what it organises.

### Corollary D (the beams of the candidate stream)

On the wheel of $30$ the integers coprime to $30$ have consecutive gaps
$(4,2,4,2,4,6,2,6)$ of period $30$, so **only the beams $\delta\in\{2,4,6\}$ occur**. Beams $0$
(gap $10$) and $8$ (gap $8$) first appear on the wheel of $210$, where the gaps are
$\{2,4,6,8,10\}$.

Condition 3 may therefore be executed by stepping along the beam cycle rather than by testing each
integer for coprimality to $30$; the two procedures generate the same candidate set and agree on all
$199\,994$ integers tested, the beam-stepped form running $1.5\times$ faster. The beam description
adds no exclusion beyond the wheel — it states why the wheel's steps are what they are.

---

## § The residue language of the twin gaps: an exact census

*Proposed as its own section. All figures from 5 000 000 primes; the seed gap $d_1=2$ is excluded.*

### 1. The reduction

A twin-start gap satisfies $d_k\equiv0\pmod 6$, so its last digit
$r_k=d_k\bmod 10\in\{0,2,4,6,8\}$ determines $d_k\bmod 30$ uniquely:

| $r$ | 0 | 2 | 4 | 6 | 8 |
|---|---:|---:|---:|---:|---:|
| $d \bmod 30$ | 0 | 12 | 24 | 6 | 18 |

Hence a **word** $w=r_1r_2\cdots r_n$ fixes the entire difference set of the forced prime tuple
$$a,\ a+2,\ a+d_1,\ a+d_1+2,\ \dots,\ a+\textstyle\sum_{i\le n}d_i,\ +2$$
modulo $2$, $3$ and $5$ — that is, the word determines admissibility exactly at the three smallest primes.

### 2. Statement

> **Theorem.** If a word $w\in\{0,2,4,6,8\}^n$ is realised by the primes, then its difference set is
> not a complete residue system modulo $2$, $3$ or $5$ (the word is *admissible*). The number of
> admissible words is
> $$A(n)=3^{\,n+1}-2^{\,n+1}.$$
>
> The converse (every admissible word is realised) is a prime-tuples statement and is not proved;
> it is observed for $n\le5$ in the first $5\cdot10^6$ primes.

### 3. Proof

**Step 1 — the modulus 3 condition is vacuous.** Every $d_i\equiv0\pmod{6}$, so every partial sum
$D_i=d_1+\cdots+d_i\equiv0\pmod 3$. The difference set reduces to $\{0,2\}\pmod 3$, two residues,
never three. The modulus $3$ obstruction can never fire.

**Step 2 — modulus 5 is a walk on $C_5$.** Modulo 5 the map $r\mapsto d\bmod5$ is the bijection
$0,2,4,6,8\mapsto 0,2,4,1,3$. Change coordinates by $c\mapsto 2c$ in $\mathbb Z/5$: the domino
$\{D_i,D_i+2\}$ becomes the edge $\{c_i,c_i+1\}$ of the cycle $C_5$ on $0,1,2,3,4$. The partial sums
become a walk $c_0=0$, $c_i=c_{i-1}+s_i$ with $s_i$ ranging over all of $\mathbb Z/5$, one word per
step sequence.

Admissibility is exactly
$$U:=\bigcup_{i=0}^{n}\{c_i,c_i+1\}\ \subsetneq\ \mathbb Z/5 .$$

**Step 3 — a three-state count.** For an admissible word put $k=|U_n|\in\{2,3,4\}$ and let
$N_k(n)$ be the number of words of length $n$ with $|U_n|=k$. Two facts about reachable states.

*(a) Which sets occur.* $U=V\cup(V+1)$ with $0\in V$. If $|U|=2$ then $U=\{0,1\}$ and $V=\{0\}$. If
$|U|=3$ then $U$ must be a **consecutive** triple $\{s,s+1,s+2\}$: a non-consecutive triple such as
$\{0,1,3\}$ would need $3\in V$ (forcing $4\in U$) or $2\in V$ (forcing $2\in U$), so it never
arises. The reachable triples are therefore exactly the five translates of $\{0,1,2\}$, and each
carries its current position $c\in\{s,s+1\}$.

*(b) The transition profile depends only on $k$.* From a state with position $c$, the five choices of
the next position $c'$ give the five edges $\{c',c'+1\}$; count how many add $0$, $1$ or $2$ new
vertices:

| from $|U|$ | to $2$ | to $3$ | to $4$ | to $5$ |
|---:|---:|---:|---:|---:|
| 2 ($U=\{0,1\}$, $c=0$) | 1 | 2 | 2 | 0 |
| 3 (consecutive, $c\in\{s,s{+}1\}$) | 0 | 2 | 2 | 1 |
| 4 ($U$ missing $x$) | 0 | 0 | 3 | 2 |

For $|U|=4$ the two steps $c'=x$ and $c'=x-1$ add $x$ and exceed the bound, the other three add
nothing. For $|U|=3=\{s,s+1,s+2\}$ the steps $c'\in\{s,s+1\}$ add nothing, $c'\in\{s-1,s+2\}$ add one
and $c'=s+3$ adds two. For $|U|=2$ the steps are $c'=0$ (nothing), $c'\in\{1,4\}$ (one), $c'\in\{2,3\}$
(one each, reaching size $4$). The table does not depend on which translate or which of the two
positions is current, so the lumping by $k$ is exact.

**Step 4 — the recursions and the closed form.** Reading the table:

$$N_2(n)=1,\qquad N_3(n)=2\,(2^{\,n}-1)=2^{\,n+1}-2,$$
$$N_4(n)=3\,N_4(n-1)+2\,N_3(n-1)+2\,N_2(n-1).$$

The first is immediate: $|U|=2$ forces every $c_i=0$. The second counts the two families
$V\subseteq\{0,1\}$ and $V\subseteq\{0,4\}$, each contributing $2^n-1$ words (all words over the two
positions except the constant one), disjoint because their only common word is the constant one which
is excluded. The third is the table applied to the preceding level, the only level that can reach
size $4$ from below.

Summing, with $A(n)=N_2(n)+N_3(n)+N_4(n)$ and $A(0)=1$:

\begin{aligned}
A(n)-3A(n-1)
&=\bigl(N_2(n)-3N_2(n-1)\bigr)+\bigl(N_3(n)-3N_3(n-1)\bigr)+\bigl(N_4(n)-3N_4(n-1)\bigr)\\
&=(1-3)+\bigl(N_3(n)-3N_3(n-1)\bigr)+\bigl(2N_3(n-1)+2N_2(n-1)\bigr)\\
&=N_3(n)-N_3(n-1)\;=\;\bigl(2^{\,n+1}-2\bigr)-\bigl(2^{\,n}-2\bigr)\;=\;2^{\,n}.
\end{aligned}

Solving the first-order recurrence $A(n)=3A(n-1)+2^{n}$ with $A(0)=1$ gives

$$\boxed{A(n)=3^{\,n+1}-2^{\,n+1}}.\qquad\square$$

**Remark.** The transfer matrix on the $40$ reachable states $(c,U)$ has spectrum
$\{3,2,1,0\}$; the $3$ and $2$ are exactly the eigenvalues of the companion matrix
$\begin{pmatrix}3&1\\0&2\end{pmatrix}$ which the count above exhibits directly, so the closed form is
a consequence of the table rather than of a numerical diagonalisation.

### 4. Verification

Predicted against the primes:

| $n$ | realised in $5\cdot10^6$ primes | $3^{n+1}-2^{n+1}$ | $5^n$ | realised share |
|---:|---:|---:|---:|---:|
| 1 | 5 | 5 | 5 | 100 % |
| 2 | 19 | 19 | 25 | 76.0 % |
| 3 | 65 | 65 | 125 | 52.0 % |
| 4 | 211 | 211 | 625 | 33.8 % |
| 5 | 665 | 665 | 3125 | 21.3 % |

and the closed form continues exactly by transfer matrix to $n=10$:
$2\,059$, $6\,305$, $19\,171$, $58\,025$, $175\,099$.

Three consequences follow without further computation: the five forbidden two-step cells
$(2,4),(4,2),(4,4),(6,8),(8,6)$ are $25-19$; the $58$ holes among $125$ three-step words are
$125-65$; and the realised share decays like $(3/5)^n$, so long residue words are almost all
impossible.

### 5. Scope

$A(n)$ counts residue **words**, not constellations. That every admissible word occurs infinitely
often is the $k$-tuple conjecture and is not proved here. The theorem characterises the language the
digits admit; it makes no claim about how often the primes speak it.

---

## § Which moduli actually obstruct, and the seven word classes

*Companion to the census section: the obstruction table and the classification of admissible words
in the beam/rung coordinates.*

### 1. The obstruction table

Every $d_i\equiv0\pmod{6}$, so every partial sum $D_i$ is $\equiv0$ modulo $2$ and $3$ (modulo $5$ it is not fixed at $0$; it walks, see below). The
difference set $\{0,2\}\cup\{D_i,D_i+2\}$ therefore reduces as follows:

| modulus | the difference set reduces to | size | can it ever be a complete residue system? |
|---:|---|---:|---|
| $2$ | $\{0\}$ | $1$ of $2$ | **no** — the obstruction is vacuous |
| $3$ | $\{0,2\}$ | $2$ of $3$ | **no** — the obstruction is vacuous |
| $5$ | $\{0,2\}\cup\{D_i,D_i+2\}$ | up to $5$ of $5$ | **yes** — the only live constraint |

So of the three small primes, only $5$ ever acts. Mod 2 and mod 3 are structurally inert: the twin
condition $d_i\equiv0\pmod6$ has already spent them.

### 2. The three triples in her coordinates

The admissible words are those whose image lies in one of three consecutive triples. Writing
$\delta=2c$ for the beam digit (rung $D=\delta/2+1$):

| triple | cycle positions | **beam digits** | **rungs** |
|---|---|---|---|
| $t_0$ | $\{0,1,2\}$ | $\{0,2,4\}$ | $\{1,2,3\}$ |
| $t_1$ | $\{0,1,4\}$ | $\{0,2,8\}$ | $\{1,2,5\}$ |
| $t_2$ | $\{0,3,4\}$ | $\{0,6,8\}$ | $\{1,4,5\}$ |

### 3. The seven classes

Partition the admissible words by which triples contain them. The sizes are exact:

| class | beam digits used | rungs used | closed form | $n=1$ | $2$ | $3$ | $4$ | $5$ |
|---|---|---|---:|---:|---:|---:|---:|---:|
| **A** | $\{0,2,4\}$ | $\{1,2,3\}$ | $3^n-2^n$ | 1 | 5 | 19 | 65 | **211** |
| **B** | $\{0,2,8\}$ | $\{1,2,5\}$ | $3^n-2^{n+1}+1$ | 0 | 2 | 12 | 50 | **180** |
| **C** | $\{0,6,8\}$ | $\{1,4,5\}$ | $3^n-2^n$ | 1 | 5 | 19 | 65 | **211** |
| **AB** | $\{0,2\}$ | $\{1,2\}$ | $2^n-1$ | 1 | 3 | 7 | 15 | 31 |
| **BC** | $\{0,8\}$ | $\{1,5\}$ | $2^n-1$ | 1 | 3 | 7 | 15 | 31 |
| **AC** | $\{0\}$ | $\{1\}$ | $0$ | 0 | 0 | 0 | 0 | 0 |
| **ABC** | constant word | $\{1\}$ | $1$ | 1 | 1 | 1 | 1 | 1 |
| | | | $\mathbf{3^{n+1}-2^{n+1}}$ | 5 | 19 | 65 | 211 | **665** |

Verified by exhaustive enumeration for $n\le6$.

### 4. What the classification says

1. **A and C have identical counts, B differs.** $t_0$ and $t_2$ each meet one neighbour in $2$
   elements and the other in $1$; $t_1$ meets both in $2$. Hence
   $A=C=3^n-2^n$ while $B=3^n-2^{n+1}+1$.
2. **Beams $4$ and $6$ never co-occur.** Rung $3$ and rung $4$ appear in no common class: a word
   using beam $4$ lies in A, one using beam $6$ lies in C, and only $BC$ and $AB$ bridge $\{0,8\}$
   and $\{0,2\}$ respectively — neither contains $4$ or $6$. So **an admissible word can never use
   rungs 3 and 4 together.**
3. **Class AC is empty.** A word whose image lies in $\{0\}$ is the constant word, which also lies in
   $B$ — so it is counted in ABC, not in AC. The zero is structural, not accidental.
4. **The class boundary is where the constraint lives.** Inadmissible words are exactly those whose
   image meets neither $\{0,2,4\}$, nor $\{0,2,8\}$, nor $\{0,6,8\}$ — i.e. those using some beam
   from each of $\{4\}$ and $\{6\}$ together with one of $\{2,8\}$ in a pattern that escapes all
   three.
