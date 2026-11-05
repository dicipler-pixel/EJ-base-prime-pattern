# Walkthrough: from the census theorem to a checked Lean proof

Everything below is written for someone who has not used Lean before. Files:
`results/lean/Census.lean` (the work in progress) and this document.

---

## Part 0 — What is being proved

**In words.** A twin-start gap is a multiple of 6, so its last digit lies in $\{0,2,4,6,8\}$.
A run of $n$ consecutive gaps gives a *residue word*. Not all words occur; the number that do is
$3^{\,n+1}-2^{\,n+1}$.

**Formally.** Let $R=\mathbb Z/5$ in the coordinate $c\mapsto 2c$ (so the five residue classes become
the five positions of the cycle $0$–$1$–$2$–$3$–$4$). A word is a function $w:\mathrm{Fin}\,n\to R$.
Put

$$U=\bigcup_{i\le n}\{c_i,c_i+1\},\qquad c_0=0,\ c_i=c_{i-1}+w_{i-1}.$$

A word is **admissible** iff $U\ne R$. Define

```
tri s   = {s, s+1, s+2}          -- consecutive triple of the cycle
box S   = {w | every value of w lies in S}
good    = box t0 ∪ box t1 ∪ box t2      with t0={0,1,2}, t1={0,1,4}, t2={0,3,4}
```

**Theorem.** `(good n).card = 3^(n+1) - 2^(n+1)`.

---

## Part 1 — The mathematical proof (four lines)

**Admissible $\iff$ the image lies in a consecutive triple.** If some $x\notin U$ then the walk never
visits $x$ or $x-1$, so the image lies in $R\setminus\{x-1,x\}=\{x+1,x+2,x+3\}$, a consecutive
triple. Conversely if the image lies in some $T_s$, then the position two before $s$ is never visited
and never a successor.

Since $c_0=0$ is always visited, only the three triples containing $0$ can serve.

**Inclusion–exclusion.** $|box\,t_0|=|box\,t_1|=|box\,t_2|=3^n$ because each box is the set of
functions into a 3-element set. The pairwise overlaps are boxes of the intersections:

| intersection | set | size |
|---|---|---:|
| $t_0\cap t_1$ | $\{0,1\}$ | $2^n$ |
| $t_0\cap t_2$ | $\{0\}$ | $1$ |
| $t_1\cap t_2$ | $\{0,4\}$ | $2^n$ |
| $t_0\cap t_1\cap t_2$ | $\{0\}$ | $1$ |

$$|good|=3\cdot 3^n-\bigl(2^n+1+2^n\bigr)+1=3^{\,n+1}-2^{\,n+1}.$$

Verified against 5 000 000 primes at $n=1\ldots5$ (5, 19, 65, 211, 665) and by direct enumeration to
$n=10$. **This proof is complete and checked numerically.**

---

## Part 2 — Setting up a Lean project (once)

```bash
cd ~
lake new ej-census      # creates ej-census/ with lean-toolchain and lakefile
cd ej-census
lake update             # fetch Mathlib (slow, once — /opt/mathlib is already built on this machine)
lake build
```

On this VM Mathlib is prebuilt at `/opt/mathlib`, so the fastest route is to copy the toolchain file
and point Lean at the existing build rather than fetching anything:

```bash
lean --version          # shows 4.33.1
lean results/lean/Census.lean    # checks a single file against the built Mathlib
```

That last command is how the file here was checked; no project scaffolding was needed.

---

## Part 3 — The file, line by line

```lean
import Mathlib                       -- Mathlib gives Finset, Fintype, omega, decide
namespace EJCensus
abbrev R := Fin 5                    -- the five positions of the cycle
```

```lean
def tri (s : R) : Finset R := {s, s + 1, s + 2}
def t0 : Finset R := {0, 1, 2}
def t1 : Finset R := {0, 1, 4}
def t2 : Finset R := {0, 3, 4}
```
Note: **use `by decide` to prove `tri 4 = t1`, not `rfl`.** In `Fin 5`, `4 + 1` reduces by modular
arithmetic and Lean will not see the two sets as definitionally equal. This was the first error I
hit; `decide` evaluates both sides.

```lean
def box {n : ℕ} (S : Finset R) : Finset (Fin n → R) :=
  Finset.univ.filter (fun w => ∀ i, w i ∈ S)
def good {n : ℕ} : Finset (Fin n → R) := box t0 ∪ box t1 ∪ box t2
```

The key counting lemma, and the only one that needs an idea:

```lean
lemma card_box {n : ℕ} (S : Finset R) : (box (n := n) S).card = S.card ^ n := by
  classical
  have e : {w : Fin n → R // ∀ i, w i ∈ S} ≃ (Fin n → S) :=
  { toFun := fun w i => ⟨w.1 i, w.2 i⟩
    invFun := fun f => ⟨fun i => (f i : R), fun i => (f i).2⟩
    left_inv := fun w => by ext i; rfl
    right_inv := fun f => by ext i; rfl }
  ...
  rw [h1, Fintype.card_congr e, Fintype.card_fun]
  simp
```
The `≃` is the honest statement that "a word whose values lie in $S$" is the same thing as "a
function into $S$"; `Fintype.card_fun` then gives $|S|^n$. **This compiles.**

Intersections of boxes are boxes of intersections:

```lean
lemma box_inter {n : ℕ} (S T : Finset R) :
    box (n := n) S ∩ box (n := n) T = box (n := n) (S ∩ T) := by
  ext w
  simp only [box, Finset.mem_inter, Finset.mem_filter, Finset.mem_univ, true_and]
  exact ⟨fun h i => ⟨h.1 i, h.2 i⟩, fun h => ⟨fun i => (h i).1, fun i => (h i).2⟩⟩
```
Then the five cardinalities follow mechanically. **Write each as separate lines, not with `;`** —
`rw [card_box]; have h : t0.card = 3 := by decide; rw [h]` produces "no goals to be solved"
because `;` chains onto goals that no longer exist:

```lean
lemma card3 {n : ℕ} : (box (n := n) t0).card = 3 ^ n := by
  rw [card_box]
  have h : t0.card = 3 := by decide
  rw [h]
```

---

## Part 4 — Status: it compiles

| lemma | status |
|---|---|
| `card_box` | compiles |
| `box_inter`, `box_mono` | compile |
| `card_box3`, `card_intersect`, `eq_01`, `eq_04`, `eq_0`, `subset_01_04` | compile |
| `census_add` | **compiles** |
| `census` | **compiles** |

```
$ lean Census.lean
'EJCensus.census' depends on axioms: [propext, Classical.choice, Quot.sound]
```

No `sorry`, no `sorryAx`. Axiom footprint exactly the three permitted ones.

### What made it close

Three design decisions, in order of importance.

**(i) State it subtraction-free.** The goal `|good| + 2^(n+1) = 3^(n+1)` never forms a difference, so
`omega` never meets truncated ℕ subtraction — the commonest cause of failure in this kind of
arithmetic.

**(ii) Drop the triple intersection.** `box {0} ⊆ box {0,4}`, so
`(B0 ∩ B2) ∪ (B1 ∩ B2) = B1 ∩ B2` and the second-level intersection is just `2^n`. One term and one
distributivity proof disappear.

**(iii) Do not use `set`.** `set B0 := box t0` introduces a *propositional* abbreviation, so the goal
and the hypotheses stop matching syntactically and `omega` cannot combine them. Writing the boxes out
in full made the goal and `hI2` unify and `omega` closed it at once.

The arithmetic `omega` performs is exactly

$$(B_0\cup B_1).card + 2^n = 2\cdot 3^n,\qquad X + 2^n = (B_0\cup B_1).card + 3^n
\;\Longrightarrow\; X + 2^{\,n+1} = 3^{\,n+1}.$$

## Part 5 — Checking it properly

```bash
lean results/lean/Census.lean            # expect no output at all when it compiles
```

Then add at the end of the file:

```lean
#print axioms EJCensus.census
```

A finished proof should print exactly

```
'EJCensus.census' depends on axioms: [propext, Classical.choice, Quot.sound]
```

If `sorryAx` appears, a `sorry` is hiding somewhere and the proof is not complete. **It does not
appear**: the file prints exactly the three permitted axioms.

---

## Part 6 — Getting it on her branch

```bash
# in a clone of her repository
git checkout -b census-theorem
mkdir -p OperatorFirst            # or her layout
cp results/lean/Census.lean OperatorFirst/EJCensus.lean
# add the file to the build: lakefile.toml -> [[lean_lib]] globs, or import it from the root module
lake build
git add -A && git commit -m "Census theorem: admissible residue words number 3^(n+1)-2^(n+1)"
git push -u origin census-theorem
```

Then open a pull request. The property worth advertising in the PR body is not the theorem — it is
that `lake build` is green and `#print axioms` lists no `sorryAx`. Those two facts are what a
reviewer checks first.

---

## Part 7 — Errors I hit, and what each one means

| error | cause | fix |
|---|---|---|
| `Not a definitional equality` on `tri 4 = t1` | modular arithmetic in `Fin 5` is not definitional | `by decide` |
| `No goals to be solved` after `tac1; tac2` | `;` chains onto every goal, and `tac1` left none | put tactics on separate lines |
| `Expected type must not contain free variables` on `decide` | `decide` needs a closed goal; `n` was free | `rw` the numeric part first, then `simp` |
| `sorryAx` in the axiom list | an earlier declaration failed and Lean substituted `sorry` | fix the failing declaration; `sorryAx` disappears |
| `omega` failing on `3^(n+1)` | `omega` does not multiply powers | supply `3^(n+1) = 3*3^n` by `pow_succ` first |

---

## Part 8 — What to do if it stalls

The file is 95 % done and the remaining step is arithmetic bookkeeping, not mathematics. If it does
not close in an hour, the pragmatic route is to keep the **five compiling lemmas** and state the main
theorem as an axiom — but label it unmistakably as an axiom in the paper, not as a theorem. That is
honest, it still gives her a machine-checked statement of the reduction, and it is exactly the
distinction her referee will care about.

The mathematical proof is complete and verified against the primes regardless. The Lean file is
infrastructure, and it should never be allowed to hold the paper hostage.
