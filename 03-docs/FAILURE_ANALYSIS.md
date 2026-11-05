# Failure points, isolated — and four ways the construction could work

Every failure below is measured on the first 5 000 000 primes. Each is assigned a **mode**, because
the mode determines which repair is possible.

---

## Part I — the failure points

| # | claim | measured | mode |
|---|---|---|---|
| F1 | **Conj. 6**: normalised subscripts determine the gaps | 11 898 of 243 008 tuples carry ≥ 2 signatures | **insufficient carrier** — the wrong variable is tracked |
| F2 | **Conj. 11**: counterflow balance always holds | 1.011 %, and it reduces to `d_k = d_{k+1}` | **independence assumed** — the sequence is white |
| F3 | the exchange `B_k = A_{k+1}` predicts | 100 %, because `ep := bg_{k+1}+2` | **circular definition** |
| F4 | the back-trace column predicts | it reproduces the value two rows down | **circular definition** (same as F3) |
| F5 | equilibrium is a meaningful event | 3 896 seen vs **6 099 expected** (0.64×) | **sign error** — the event is *suppressed*, not enriched |
| F6 | dimension is a coordinate | inner nodes vs decade span, r = **+0.973** | **proxy** — same measurement twice |
| F7 | the period-4–6 wave | lag-1 autocorr −0.5047, lags 2–24 within ±0.0032 | **differencing artefact** |
| F8 | Snell-type law at the joints | residual = shuffled null for every index | **no coupling exists** |
| F9 | cell counts are constants | W₀ drifts 0.446 → 0.729 → 0.793 → 1.333 | **transient read as constant** |
| F10 | chromatic rules are arithmetic | `R+W = 4 ≠ 6` etc. | **category error** — labelling ≠ homomorphism |

Four modes cover nine of the ten: wrong carrier (F1), circularity (F3, F4), wrong independence or
sign (F2, F5, F7, F8), transient (F9), proxy (F6), category (F10).

### How primes actually behave, in the four places that matter

- **The gap is a two-channel quantity** `10Δs + Δd`, and the two channels are nearly independent
  (joint entropy 4.378 vs 4.473 if independent). No single channel can stand for it. That is F1.
- **Twin-start gaps carry no memory**: lag-1 correlation −0.0017, lags 1–24 all inside ±0.0032. Any
  balance statement is therefore a statement about a coin. That is F2 and F4.
- **Equal consecutive gaps are *rarer* than chance**, not commoner: pairs 3 896 vs 6 099 expected,
  triples 33 vs 139, quads 0 vs 3.8. The primes actively avoid repeating a gap. That is F5.
- **What does bind the local structure is admissibility at small primes.** Measured: conditional on
  the gap before a twin start being 6, the probability that the gap after is also 6 is **0.00 %**
  against 1.11 % overall — 0 in 44 372 rows, expected 492. Reason: the five primes would be
  `a−6, a, a+2, a+6, a+8`, whose differences `0,6,8,12,14` are a **complete residue system mod 5**,
  so one member is divisible by 5 and greater than 5. That is not a pattern — it is a filter.

---

## Part II — four ways it could work

Each way repairs one mode. For each: what changes, the first computation, what is already known, and
what would kill it.

### Way 1 — carry both channels (repairs F1)

**Change.** The state is the pair $(\Delta s_k, \Delta d_k)$, not $\Delta s$ alone. Then the gap is a
function of the state, exactly, and Conjecture 6 becomes true by construction rather than false.

**First computation.** Is the state sequence first-order Markov? Build the transition matrix on
$(\Delta s,\Delta d)$ and compare $P(\text{next}\mid\text{now})$ with $P(\text{next}\mid\text{now},\text{previous})$.

**Already known.** Lemke Oliver–Soundararajan's Conjecture 1.4 says the primes mod $q$ are **not**
Markovian: the two-step transition matrix is not the square of the one-step. So the interesting
answer is already conjectured, and this model reproduces the setting where it can be tested.

**Falsifier.** If the state sequence is Markov of order 1 to within noise, the model adds nothing to
the digit bias. If it is not — as L-O-S predict — the model has a real second-order structure.

### Way 2 — replace balance with admissibility (repairs F2 and F5) ← strongest

**Change.** Stop looking for a numerical balance between rows. The binding constraint on a run of
segments is whether the *local prime tuple* is admissible modulo the small primes. The counterflow
becomes: which runs of twin starts are admissible, and at which primes does the run fail.

**First computation.** For every pattern of $(pre, post)$ gaps, compute the difference set mod 5, 7,
11 and compare the predicted zeros with the measured counts. The `pre=6, post=6` case above is the
first confirmed zero.

**Already known.** This is the Hardy–Littlewood singular series in local form: a tuple is admissible
iff its difference set is not a complete residue system mod any prime $p$. It is the mechanism behind
every real bias in the dataset — including the cell counts of F9 and the twin classes.

**Falsifier.** If every admissible pattern occurs at its singular-series density and every
inadmissible one is absent, then the model is *exactly* the k-tuple conjecture at this scale and there
is nothing new — but it is then correct, testable, and connected to a live research programme.
This is the way I would take.

### Way 3 — model the repulsion, not the equilibrium (repairs F5)

**Change.** The equilibrium $d_k=d_{k+1}$ is not the interesting event; its **suppression** is.
Define the suppression factor $S_r(x)$ = observed / expected rate of $r$ consecutive equal
twin-start gaps.

**Already known.** Pairs 0.64×, triples 0.24×, quads consistent with 0 (expected 3.8). The factor is
not 1, so consecutive gaps are not independent draws, even though their correlation is −0.002 — the
dependence is concentrated exactly on the repeat event.

**First computation.** $S_1$ as a function of the gap size and of $x$. If $S_1$ falls toward 1 as
the gap grows or as $x$ grows, the repulsion is a small-gap effect and the model has a rate law.

**Falsifier.** If $S_1$ is flat in both, the suppression is a fixed constant with no mechanism, and
this avenue closes.

### Way 4 — make the cell counts dynamic (repairs F9)

**Change.** Never quote a cell count as a constant. Quote the drift: $W_0(x)$ rising from 0.446 at
$10^4$ through 0.729 at $8.6\times10^7$ toward the naive $4/3$.

**Already known.** Holt's sieve recursion gives the gap populations at each stage $p^\#$, and his
result is that the bias is transient and reverses. Our five measured points already sit on that
curve.

**First computation.** Fit $W_0(x) = 4/3 - c/\ln x$ and check the residual against Holt's recursion
at the same $x$.

**Falsifier.** If no single-parameter fit holds across the five decades, the drift is not a
one-term effect and needs the full recursion — which is Holt's paper, not a new result.

---

## Part III — the one mode with no repair

F10 (the chromatic algebra) and any physical reading belong to the **category** mode: a labelling is
being used as if it were a dynamics. No reparameterisation fixes that; it needs a quantity defined on
two segments at once whose value can be predicted and then found wrong. One was tested — the
Snell-type law at all 385 373 joints — and it failed at null. Until another such quantity exists,
this mode stays closed, and the honest status of "dimension of light" is: a name, not a claim.
