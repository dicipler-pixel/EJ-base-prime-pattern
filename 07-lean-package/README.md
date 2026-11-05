# EJ: the Lean proofs, ready to build yourself

**Machine-checked fragments of a base-10 prime pattern**, by Elizabeth Johnson (@Ellyrox110) and
Jeromie Beasley. This folder is a complete Lean 4 project for the proofs in the report
(revision 7). Building it makes your own computer re-check every proof from scratch.

The framework (base-10 encoding, end-digit key, twin segmentation, colour scheme) is Elizabeth Johnson's,
DOI [10.5281/zenodo.23378596](https://doi.org/10.5281/zenodo.23378596). The results checked here
are joint.

**Attribution note.** A related document, *Advanced Color Theory in Relations to Primes* (Elizabeth Johnson and Shaun Neer, October 2026), lists a second author. The attribution of the colour scheme and its mixing rules, credited here to Elizabeth Johnson, is still being verified with the authors, and will be corrected in a later revision if needed.

---

## What you need

* About **10 GB of free disk space**. Most of it is Mathlib, the shared maths library the proofs
  use.
* An internet connection for the first build.
* **20–40 minutes** the first time, almost all of it downloading. Later builds take seconds.

## Step 1: install Lean (once)

**Easiest, on any computer:** install [VS Code](https://code.visualstudio.com/), open the
Extensions panel, and install **"Lean 4"**. It offers to install Lean (the `elan` installer) for
you. Say yes.

Or install it from a terminal instead:

* **Mac / Linux**

  ```bash
  curl https://elan.lean-lang.org/elan-init.sh -sSf | sh
  ```

* **Windows (PowerShell)**

  ```powershell
  curl -O --location https://elan.lean-lang.org/elan-init.ps1
  powershell -ExecutionPolicy Bypass -f elan-init.ps1
  ```

Close the terminal and open a new one afterwards, so it can find `lake`.

## Step 2: get the pre-built Mathlib

Open a terminal **inside this folder** (the one with `lakefile.toml`), then run:

```bash
lake exe cache get
```

The first time, this downloads the right version of Lean (4.33.0) and Mathlib, then fetches
Mathlib already compiled. You'll see a lot of download lines. That's normal.

## Step 3: build the proofs

```bash
lake build
```

## What you should see

Near the end, 29 `info:` lines, then:

```
Build completed successfully
```

The 29 lines should match `EXPECTED_OUTPUT.txt` in this folder. That file has the same lines, just
without the file paths in front. Two things to check:

1. The line `[1, 5, 19, 65, 211, 665]` appears. That is the census counter being run.
2. **No line contains `sorryAx`.** `sorry` is Lean's word for "proof skipped". If it appeared in an
   axiom list, a proof would be missing. It doesn't.

`propext`, `Classical.choice` and `Quot.sound` are the standard axioms that ordinary mathematics
uses. One line says "does not depend on any axioms", which is fine.

If anything else happens, copy the last 30 lines of the output and send them over.

---

## What is proved, in plain words

**`EJ/Census.lean`**

* `census_words`: the residue words of length *n* that are admissible number exactly
  3ⁿ⁺¹ − 2ⁿ⁺¹, for every *n*.
* `realised_admissible`: every word actually produced by twin primes starting above 5 is
  admissible. Starting at 5 it can fail (5, 11, 17), and that case is checked too.
* `cover_iff`, `census`: the steps of the counting proof.

**`EJ/EJPrime.lean`**

* `twin_start_digit`: a twin prime start above 5 ends in 1, 7 or 9.
* `not_prime_add_two`, `seven_of_ends_seven`: the start of a twin pair never ends in 3 (except 3
  itself), and the end never ends in 7 (except 7 itself).
* `junction_unique`: if *p* − 2, *p* and *p* + 2 are all prime, then *p* = 5.
* `equilibrium_obstruction`: two equal gaps in a row between twin pairs are impossible in four
  digit cells.

**`EJ/Wheel.lean`** (the colour wheel)

* At scale 10:
  * a digit is fixed by its layer and hue (`layer_hue_determine`);
  * the colour classes are the gcd classes (`orbit_iff_gcd`);
  * multiplying by 7 is a quarter turn (`quarter_turn`);
  * complement is negation (`complement_is_neg`);
  * adding 5 swaps layers and keeps the hue (`add_five`);
  * twin pairs avoid the grey hue (`twin_hue`).
* At scales 100 and 125: classes project to classes and the circle of 2 keeps the coarse order
  (`coarse_of_fine`, `nine_classes`, `two_generates_mod25`, `fine_projects_to_coarse`,
  `generators_mod25`, `generators_reduce`, `lifts_mod125`).
* Delays: a twin delay leaves 3, 1, 2, 2, 1 hues free for the pair to avoid grey (`free_hues`,
  `free_hues_eq`).

What Lean does *not* check is listed in the report's Formalisation section. That includes the
general-scale statements beyond 100 and 125, and every measured rate.

## Files

| file | what it is |
|---|---|
| `lakefile.toml` | the project: library `EJ`, depending on Mathlib `v4.33.0` |
| `lean-toolchain` | pins Lean 4.33.0 |
| `EJ.lean` | imports the three files, so building it builds everything |
| `EJ/Census.lean`, `EJ/EJPrime.lean`, `EJ/Wheel.lean` | the proofs, identical to `02-lean/` in the review pack |
| `EXPECTED_OUTPUT.txt` | the 29 lines a successful build prints |
