# Machine-checked fragments of a base-10 prime pattern

**This repository holds two distinct things, and they must never be cited as one:**

1. **A framework, which is Elizabeth Johnson's alone.** Prior work, already published. Cited to her.
2. **New results, which are hers and Jeromie Beasley's jointly.** Derived on top of the framework.
   Cited to both.

---

# Part 1 — The framework (hers)

**Elizabeth Johnson** (*Ellyrox110*). Prior work, published as
*EJ's Alternate Base Prime Number Pattern and the Twin Prime Counterflow Model*,
DOI [10.5281/zenodo.23378596](https://doi.org/10.5281/zenodo.23378596).

She is credited with:

* the base-10 encoding $p = 10s + d$, with $d$ the end digit and $s$ the inner node;
* the end-digit key $g \equiv d_2 - d_1 \pmod{10}$ (her Theorem 3);
* the mod-9 twin classes $(2,4),(5,7),(8,1)$ (her Theorem 15);
* the twin segmentation: segments cut at every twin gap, from $bg$ to $ep$;
* the counterflow framing of the ladder;
* the colour scheme (attribution under verification; see note) — primaries $1,3,7,9$, secondaries $2,4,6,8$, grey $5$, base $10$, and the
  complementary pairs $(1,9),(3,7),(2,4\text{-pair}),\dots$;
* the rung ladder $D = (g \bmod 10)/2 + 1$.

Cite her manuscript.

**Attribution note.** A related document, *Advanced Color Theory in Relations to Primes* (Elizabeth Johnson and Shaun Neer, October 2026), lists a second author. The attribution of the colour scheme and its mixing rules, credited here to Elizabeth Johnson, is still being verified with the authors, and will be corrected in a later revision if needed.

---

# Part 2 — The new results (jointly hers and Jeromie's)

Derived in collaboration, **not present in her manuscript**, and not implied by it:

* **the residue-language census.** Admissible residue words of length $n$ over $\{0,2,4,6,8\}$
  number $A(n) = 3^{\,n+1} - 2^{\,n+1}$, and every word realised from a regular twin start
  ($a_k\ge11$) is admissible. With a combinatorial proof, the seven word classes, and the
  mod-2/3/5 obstruction table (only mod 5 is ever live). The converse is not claimed.
* **the carry law.** $\Delta s = \lfloor g/10 \rfloor + \mathbb{1}[\Delta d < 0]$ — the subset step
  is the tens part of the gap plus a digit-wrap carry.
* **the equilibrium obstruction (Theorem 10′).** Equilibrium $d_k = d_{k+1}$ is impossible in exactly
  the four cells where $2v-u \equiv 3$ or $5 \pmod{10}$. (The spread among the other five cells is
  studied empirically in `03-docs/THEOREMS.md`; that is not a theorem.)
* **the digit-exclusivity proofs.** In a twin pair, if the start ends in 3 then it is 3, and if the
  end ends in 7 then it is 7. The statements were observed; the proofs are new.
* **the junction uniqueness.** Among $p-2,p,p+2$ one is divisible by 3, so all three prime forces
  $p=5$ — the `3bg 5 7ep` segment is unique.
* **the admissibility filter.** 70 of 70 admissible $(pre,post)$ patterns occur; 0 of 330
  inadmissible ones do.
* **the exact range of the coprimality test.** For $n>1$ not itself a factor of $P$: a common factor
  with $P$ refutes, and coprimality confirms only for $n < p^2$, $p$ the least prime not dividing $P$;
  at the 30-wheel the first failure is $49 = 7^2$.
* **the $2p$ family** for the colour wheel, via the divisor classes of $(\mathbb{Z}/W)^\times$, and
  **the wheel in coordinates**: $\mathbb{Z}/2p \cong \mathbb{Z}/2\times\mathbb{Z}/p$ (layer, hue), units
  as rotations, complement as the half turn, twin pairs avoiding the grey hue.
* **these Lean formalizations.**

**Authorship of Part 2: Elizabeth Johnson and Jeromie Beasley, jointly.**

**Methodological contribution:** Jeromie Beasley — the three-tier separation of written proof /
independent certificate / formalization, the negative-control discipline, and the direction that
produced the results above.

---

# Files

Lean 4 v4.33.0, Mathlib v4.33.0. Each file imports only the Mathlib modules it needs. All three were
compiled for revision 7, with no `sorry`; the verbatim output is in `05-handoff/manifest.json`.

| file | main statements |
|---|---|
| `Census.lean` | `census_words` (the census on words, all $n$), `realised_admissible` (realised ⇒ admissible, $a>5$; seed counterexample checked), `cover_iff`, `admissible_iff`, `census` |
| `EJPrime.lean` | `twin_start_digit`, `not_prime_add_two`, `seven_of_ends_seven`, `junction_unique`, `equilibrium_obstruction`, cell identities |
| `Wheel.lean` | at $W=10$: `layer_hue_determine`, `orbit_iff_gcd`, `units_fix_layer`, `quarter_turn`, `complement_is_neg`, `add_five`, `twin_hue`, `twin_start_digit` |

# Build

Inside a Lake project that depends on Mathlib v4.33.0:

```bash
lake env lean Census.lean
lake env lean EJPrime.lean
lake env lean Wheel.lean
```

Each file ends with `#print axioms` lines; no line may contain `sorryAx`.

---

# Citation

**For the framework (§ Part 1), cite her alone:**

> Elizabeth Johnson, *EJ's Alternate Base Prime Number Pattern and the Twin Prime Counterflow Model*,
> Zenodo, DOI 10.5281/zenodo.23378596.

**For the census, the obstruction, the digit-exclusivity proofs or the formalization (§ Part 2),
cite both:**

> Elizabeth Johnson and Jeromie Beasley, *Machine-checked fragments of a base-10 prime pattern*, with
> Lean 4 formalizations; built on DOI 10.5281/zenodo.23378596.

---

# Scope — what is not claimed here

* **No finite coprimality test decides primality in general.** It confirms only below $p^2$.
* **The sieve's symmetry gives nothing.** The automorphism group of $\mathbb{Z}/W$ fixes the gap
  sequence identically, so the divisor-class method returns no information about gaps.
* **No physical or colourimetric claim.** The colour structure is a classification of the label
  system, not a statement about light.
* **The seed exceptions are explicit hypotheses.** $a = 3$, and the pair $(5,7)$ sharing the prime 5.
  Lean forced them to be named; they are not artefacts of the formalization.

---

## Posting

Posted by Jeromie Beasley with Elizabeth Johnson's knowledge; she may fork it or request changes (2026-11-04). The authorship split above cites her framework to her alone and the new results to both.

Prepared with AI assistance (Grok Bot and Claude); all Lean proofs are checked by GitHub Actions. As with any tool-assisted work, the responsibility for correctness rests with the named authors.
