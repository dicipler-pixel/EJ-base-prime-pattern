# Revision history

## Revision 7 — 2026-11-05 (current)

New Section 6, **Delays on the wheel**, written at the authors' prompting on delay times.

* **Return delays.** The mean return delay of each digit is 4, which is forced by its rate of 1/4.
  The shape is not forced: an immediate return is 16.6–17.7 % against 25 %. The memory lasts about
  two primes (36.5, 2.0, 0.11 millibits at lags 1, 2, 3).
* **Free hues (Proposition 23, proved; Lean `free_hues`, `free_hues_eq` at q = 5).** A twin delay h
  leaves ω₅(h) = 3, 1, 2, 2, 1 hues free for h ≡ 0..4 mod 5. This is the Hardy–Littlewood local
  factor. Its prediction fits all pairs of twin starts within 0.2 points (5.27 M pairs, h ≤ 3000).
  Consecutive pairs deviate by up to 2.6 points, which is the consecutiveness effect.
* **Null checks, recorded.** Hue-walk drift: z = 0.99. Clustering of equilibria: z = −1.79, not
  significant.
* **Code.** New `04-verification/delay_check.py`.
* **HTML edition.** `01-report/report.html` is the same paper as the PDF: the theorem and section
  numbers match, the maths is MathML and the figures are embedded, with no network needed. It is
  built by `04-verification/html_build/make_html.py` (pandoc).
* **push.sh.** If the target repository already has commits (for example a README made on
  GitHub), the script now merges them in. Their history is kept, pack files win on conflicts, and
  nothing is force-pushed.
* **`07-lean-package/`.** The three Lean files as a ready-to-build Lake project (Mathlib `v4.33.0`,
  commit db584cd), with step-by-step instructions and `EXPECTED_OUTPUT.txt` (29 lines). It builds as
  one library with every axiom line as recorded and no `sorry`.
* **README.md** now opens with the title, both authors and the framework DOI.
* **`.github/workflows/lean-proofs.yml`.** On every push, GitHub's own servers check the pack against
  the manifest, build the Lean proofs, and compare all 29 result lines with `EXPECTED_OUTPUT.txt`,
  failing on any `sorry`. No one's computer is needed.
* **Name and attribution note.** Short form of her name → **Elizabeth Johnson** everywhere (at her request). An
  attribution note is added to the paper, README, CITATION and handoff: a related document lists a
  second author (Shaun Neer), and attribution of the colour scheme is still being verified.
* **`CITATION.cff`.** Gives the repository a "Cite this repository" button with both authors. Her
  framework DOI is given as a reference cited to her alone.

## Revision 6 — 2026-11-05

New subsection 5.4, **Colour at scale**, written with the authors' direction that colour should
change with scale. It was refereed independently and the findings were addressed.

* **Resolution (proved).** At scale $10^k$ there are $(k+1)^2$ classes. The primaries never split;
  grey and the secondaries get $k$ shades each and the base gets $k^2$ (Prop. 19). Hue circles and
  refinement are defined precisely (Def. 20). Zooming preserves the coarse cyclic order once an
  orientation is fixed (Prop. 21). Each zoom adds a finite, counted freedom: 4 refinements at the
  first zoom and 5 at every later one, and the circle of 2 is coherent at every scale (Prop. 22).
  The layer side is not cyclic from scale 1000 on.
* **Magnitude (measured).** 3+7 is never strictly behind 1+9 (ties at 11, 31, 41, 3581); this is
  Chebyshev's bias, persistent but not permanent by Rubinstein–Sarnak (conditional). The tie-free
  ranking changes 36 times across 49 checkpoints. The same-digit share is 11.84 / 15.35 / 17.12 %
  against 25 % (Lemke Oliver–Soundararajan, conjectural theory). The new
  `04-verification/scale_check.py` computes all of these on the exact 5,000,000-prime set.
* **Lean.** `Wheel.lean` adds the scale-100 and scale-125 facts: `coarse_of_fine`, `nine_classes`,
  `two_generates_mod25`, `fine_projects_to_coarse`, `generators_mod25`, `generators_reduce` and
  `lifts_mod125`.
* **References.** A bibliography was added: Ireland–Rosen, Rubinstein–Sarnak and Lemke
  Oliver–Soundararajan.

## Revision 5 — 2026-11-05

A strengthened paper and Lean development, after two rounds of independent review.

**Corrections to the mathematics**
1. Theorem 3 (realised ⇒ admissible) was false at the seed: from 5, the twin starts 5, 11, 17
   realise the inadmissible word (6, 6). It now requires a regular start ($a_k\ge11$), and the
   counterexample is Remark 4. Counting from 5 would give 20, 66, 212, 666.
2. The proof of Theorem 2(i) cited an argument that did not cover mod 5. There is now a complete
   proof.
3. The census proof treated letters as walk positions. It now has four explicit steps: the
   bijection to positions, the reduction, the cover lemma (with its proof), and
   inclusion–exclusion.
4. "No admissible word uses rungs 3 and 4 together" was false: (4, 6) is admissible and the adjacent
   pair occurs 30 124 times. Only the beam statement is true.
5. Figure 2's title said the classes sum to 211. They sum to 665; the figure was redrawn.
6. Theorem 11's table used an undefined "u → e" and wrong "reason" entries. It now lists the cells
   as u → v with 2v − u; the old bg → ep notation is noted.
7. The coprimality test conflated the end-digit key with the gcd test, and "refutes always" was
   false for $n\mid P$. Hypotheses are now exact.
8. The orbit theorem's converse is now proved (the CRT lift), and the "only if" of the $2p$ family
   is proved.
9. "The gap structure has no non-trivial symmetry" was false. It is now: only u = 1 preserves the
   cyclic order of wheel survivors and only u = −1 reverses it (checked at W = 10, 30, 210, 2310).
10. "Twin primes are exactly the configurations that avoid grey" was false (119, 121 avoid grey).
    Avoiding grey is necessary, not sufficient.
11. "Forced by the ring" overclaimed the hue circle. The cyclic order depends on the generator:
    there are φ(p−1)/2 orders up to rotation and reflection. That is unique at 5 and 7, two at 11
    and 13 (Remark 16).
12. The open converse is now stated precisely: a prime-tuples statement plus consecutiveness.
13. Novelty is labelled. Digit exclusivity and the uniqueness of 3, 5, 7 are classical, and the
    carry identity is elementary.
14. The abstract no longer said "five" results while the body said "four", and the figure path in
    report.tex now points at `figures/`.

**New**
* A wheel section in coordinates: Z/2p ≅ Z/2 × Z/p (layer, hue), units as rotations, complement as
  the half turn, the layer swap, twins avoiding grey, a precise list of what is open, and a TikZ
  figure of the wheel.
* `02-lean/Census.lean`:
  * `census_words` (the census stated on words, for all n) via `cover_iff` and `admissible_iff`;
  * `realised_admissible` (realised ⇒ admissible at 5, a > 5);
  * the seed counterexample.
* `02-lean/EJPrime.lean`: `twin_start_digit`, and `equilibrium_obstruction` stated on primes.
* `02-lean/Wheel.lean`: the W = 10 wheel identities and `twin_hue`.
* All three Lean files compiled by the preparer (Lean 4.33.0, Mathlib db584cd) with no
  `sorry`. Imports were narrowed from `import Mathlib` to the modules used.

**Docs**
* `03-docs/NSTEP_CENSUS.md`: the list of forbidden two-letter words now includes (6, 6) (six words,
  25 − 19), and the seed rule is stated.
* `05-handoff/REVIEW.md` and `02-lean/README.md` were rewritten for revision 5.
* `05-handoff/HANDOFF.md` was updated: the Lean gate covers three files.

## Revision 4 — 2026-11-05

The paper (`01-report/`) and the Lean files are byte-identical to revision 3. Supporting files fixed:

1. `05-handoff/REVIEW.md` still listed the false "no prime above 3 ends in 3; no prime above 7 ends
   in 7" as claim 3. Now restricted to twin pairs, as in the paper. Its Lean commands now use
   `lake env lean` and expect five axiom lines; its Lean-coverage sentence now names the results
   actually checked.
2. `03-docs/NSTEP_CENSUS.md`, `03-docs/PAPER_UPDATE.md` and `03-docs/FINAL_STATEMENT.md` still stated
   the unproved converse ("iff"). Now "only if", with the converse marked as observed, not proved.
3. `NSTEP_CENSUS.md` and `PAPER_UPDATE.md` still said $d_i\equiv0\pmod{30}$ (three places). Now
   mod 6. One place also claimed the partial sums are $\equiv0$ mod 5, which is false; now removed.
4. `05-handoff/HANDOFF.md` rewritten so it runs against this layout: paths, a Lake-based Lean gate,
   a Zenodo sandbox dry run, the description corrected from "five" to "four" formalised results, and
   a description sentence that depends on whether the Lean gate ran.
5. `05-handoff/manifest.json` was missing from the archive; regenerated for revision 4, with
   `05-handoff/check_pack.py` to check it.
6. `05-handoff/push.sh` used to commit only the `05-handoff/` folder and called `lean` without Mathlib;
   it now commits the pack root and runs Lean through a Lake project.
7. `04-verification/verify_all.py` crashed at the end when `results/data/` was missing; it now
   creates the folder. All 24 checks pass.
8. `05-handoff/PUBLISH.md` marked superseded; it described a different machine.

## Revision 3 — 2026-11-05

Six defects found in external review, all fixed:

1. **Theorem 2** claimed a word is realised **iff** admissible. The "only if" is proved; the "if" is
   a prime-tuples statement. Now split: (i) realised implies admissible — proved; (ii) the count
   $3^{n+1}-2^{n+1}$ — proved. The observation that all admissible words occur for $n\le5$ is stated
   as an observation.
2. **Theorem 4** was false as written: "no prime above 7 ends in 7" — 17, 37, 47 are primes ending
   in 7. Now stated for twin pairs, with the counterexamples named in a remark.
3. **"$d_i\equiv0\pmod{30}$"** was wrong in two proofs; the correct hypothesis is
   $d_i\equiv0\pmod 6$. Both proofs only needed mod 6, so the conclusions are unchanged.
4. **Theorem 6** said "iff $r\in\{0,2,8\}$". Since $r=2$ and $r=8$ each have one forbidden cell, this
   is "only if", now stated with the insufficiency explicit.
5. **Theorem 7** omitted $n>1$: 1 is coprime to $P$ and is not prime.
6. **The formalisation count** was wrong — four results, not five — and the Theorem 6 cell lemmas
   were claimed but not audited. They now print axioms, so the claim matches the check.

## Revision 2 — 2026-11-05

Corrected the digit-exclusivity statement in `report.tex` and `lean/README.md`. The Lean theorem was
already correct; the prose was not. Checksums refreshed.

## Revision 1 — 2026-11-05

First issue. Superseded: contains the false Theorem 4 and the "iff" in Theorem 2.
