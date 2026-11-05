# Review brief

For a reviewer, human or automated, reading this pack. Read this first: it lists what is already
known, so you don't spend time flagging it.

Revision 7. Section, theorem and remark numbers below are as they appear in the compiled
`01-report/report.pdf`.

## What is being claimed

All numerical checks use a sieve of the first 5 000 000 primes above 5 (up to 86 028 223). The
Lean files were compiled for this revision. Their output is in `05-handoff/manifest.json`.

1. **Realised words are admissible** (Theorem 3). Take the word of gap residues read from a regular
   twin start, $a_k \ge 11$. Its offset set is not a complete residue system modulo 2, 3 or 5.
   *Lean:* `realised_admissible`, proved at 5 for any $a>5$. The seed counterexample
   $5, 11, 17$ is checked in the same file.
2. **Only 5 obstructs** (Theorem 5). Modulo 2 and modulo 3 the offset set is always $\{0\}$ and
   $\{0,2\}$ respectively.
3. **The census** (Theorem 6). Admissible words of length $n$ number $3^{n+1}-2^{n+1}$.
   *Lean:* `census_words`, on words, for all $n$, including the bridge to walk positions.
4. **Digit exclusivity** (Theorem 8; classical, proof included). A twin start $a>5$ ends in 1, 7 or 9, and $a+2$ ends in 3, 9 or
   1. This is about twin pairs, *not* all primes: 13 and 17 are primes ending in 3 and 7.
   *Lean:* `twin_start_digit`, `not_prime_add_two`, `seven_of_ends_seven`.
5. **Junction uniqueness** (Theorem 10). If $p-2$, $p$ and $p+2$ are all prime, then $p=5$.
   *Lean:* `junction_unique`.
6. **Equilibrium obstruction** (Theorem 11). For regular twin starts, $d_k = d_{k+1}$ is impossible
   in the cells $u\to v$ = $1\to7$, $7\to1$, $9\to1$, $9\to7$. *Lean:* `equilibrium_obstruction`,
   stated on primes.
7. **Range of the coprimality test** (Theorem 12). Exact hypotheses are in the theorem; at the
   30-wheel the first failure is $49$.
8. **The wheel in coordinates** (Section 5). The orbits of $(\mathbb Z/W)^\times$ are the divisor
   classes (Theorem 13). The orbit sizes are $1,1,m,m$ exactly when $W=2p$ (Proposition 14). At
   $W=2p$ the wheel is $\mathbb Z/2\times\mathbb Z/p$, giving layers, hues, rotation by units,
   complement as the half turn, and the layer swap (Theorem 15). Twin pairs avoid the grey hue
   (Proposition 17; necessary, not sufficient). The hue order depends on a generator (Remark 16).
   *Lean:* `Wheel.lean`, at $W=10$ only.
9. **Colour at scale** (Section 5.4). These are proved:
   * the classes refine, and the primaries never split (Proposition 19);
   * zooming keeps the oriented coarse order (Proposition 21);
   * each zoom offers 4, and then 5, refinements, and the circle of 2 is coherent at every scale
     (Proposition 22).

   The magnitude bullets are *measurements* with cited theory. *Lean:* the scale-100 and
   scale-125 facts in `Wheel.lean`.
10. **Delays** (Section 6). Free hues ω₅(h) = 3, 1, 2, 2, 1 is proved (Proposition 23; *Lean:*
    `free_hues`). That twin delays follow these weights is a Hardy–Littlewood *prediction*, checked
    on the data. Return-delay shapes and memory by lag are *measurements*, and two null checks are
    recorded as null.

## What is *not* claimed: please do not read these as claims

* The converse of claim 1 (that every admissible word occurs). It is a statement of prime-tuples
  type and is only *observed* for $n\le5$.
* That any finite test decides primality. Claim 7 gives its exact range.
* That the wheel symmetries say anything about prime gaps. Only $1$ preserves the cyclic order of
  wheel survivors, and only $-1$ reverses it (Remark 18).
* Any physical or colorimetric claim. "Layer", "hue" and "grey" are names for coordinates.
* That any cell count or rate is a constant. They drift with $x$.
* That the 3+7 lead is permanent. It is a bias, and it is persistent but not permanent (Section 5.4).
* That "colour at scale" is a statement about light. It concerns residues only.
* The empirical decomposition of equilibrium rates in `03-docs/THEOREMS.md` is not a theorem of the
  report.

## Known exceptions: these are correct, not errors

* $3$ and $5$ are the seed. $d_1=2$ is not $\equiv0 \pmod 6$.
* The census and claim 1 use windows from $a_k\ge11$. From $5$, the word $(6,6)$ is realised but not
  admissible (Remark 4). Counting from 5 would give 20, 66, 212, 666.
* The segment $[3,7]$ has span 4.

Each Lean statement carries the matching hypothesis.

## Already corrected: do not re-raise

* Revision 3: the false "no prime above 7 ends in 7", the unproved "iff" in the census, "mod 30"
  for "mod 6", "iff" in the equilibrium theorem, the missing $n>1$, and the formalisation count.
* Revision 4: stale copies of the above in the docs and in this brief, and the handoff/manifest.
* Revision 5: the full list is in `CHANGES.md`. The main items are:
  * the seed hypothesis in claim 1;
  * the false "rungs 3 and 4 never co-occur";
  * the Figure 2 sum;
  * the Theorem 11 table notation;
  * the coprimality-test wording;
  * the orbit-theorem proof, and the "only if" of the $2p$ family;
  * the false symmetry remark (it missed the reflection), "exactly avoid grey", and "forced by the ring" (second review);
  * the Lean bridge for the census.

`03-docs/CORRECTIONS.md` lists eight earlier working-draft statements that the formal check does not support, each with its replacement. If one
of them appears asserted anywhere in `03-docs/`, that file is stale, not making a current claim.

## How to check it

```bash
# inside a Lake project that depends on Mathlib v4.33.0
lake env lean 02-lean/Census.lean
lake env lean 02-lean/EJPrime.lean
lake env lean 02-lean/Wheel.lean
```

The expected output is in `05-handoff/manifest.json` → `verification.expected_stdout`. No line may
contain `sorryAx`.

## What a useful review would attack

1. **Lean fidelity.** Do `offsets`, `admissible`, `wordOf` and `Dn` in `Census.lean` match the
   paper's Definition 2? Does `realised_admissible` say what Theorem 3 says?
2. **The wheel section's framing.** The claim is that the framework's labels are recovered from the
   ring structure. The choice of generator and orientation of the hue angle are conventions. Is
   anything presented as forced that is really chosen?
3. **The open items** at the end of Section 5. Are they stated precisely enough to work on?
