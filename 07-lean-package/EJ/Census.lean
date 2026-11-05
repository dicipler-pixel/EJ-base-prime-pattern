import Mathlib.Data.Fintype.BigOperators
import Mathlib.Data.Fintype.Powerset
import Mathlib.Data.ZMod.Basic
import Mathlib.Data.Nat.Prime.Basic
import Mathlib.Tactic.NormNum.Prime
import Mathlib.Tactic.Ring
import Mathlib.Tactic.Tauto

/-!
# The residue-language census of the twin-gap sequence

Main results:

* `census_words`: residue words of length `n` that are admissible at 5 number `3^(n+1) - 2^(n+1)`;
* `realised_admissible`: the residue word of gaps between twin starts beginning at `a > 5` is
  admissible (the converse is a prime-tuples statement and is not claimed);
* `cover_iff`, `admissible_iff`: the bridge from words to walk positions in one of three triples;
* `census`: the inclusion–exclusion count over those triples.

Admissibility at 2 and 3 is automatic for these words (paper, Theorem 3), so "admissible at 5"
is admissibility.
-/

namespace EJCensus

abbrev R := Fin 5

/-- The three consecutive triples containing `0`. -/
def t0 : Finset R := {0, 1, 2}
def t1 : Finset R := {0, 1, 4}
def t2 : Finset R := {0, 3, 4}

/-- Words of length `n` whose image lies in `S`. -/
def box {n : ℕ} (S : Finset R) : Finset (Fin n → R) :=
  Finset.univ.filter (fun w => ∀ i, w i ∈ S)

/-- Admissible words. -/
def good {n : ℕ} : Finset (Fin n → R) := box t0 ∪ box t1 ∪ box t2

lemma card_box {n : ℕ} (S : Finset R) : (box (n := n) S).card = S.card ^ n := by
  classical
  have e : {w : Fin n → R // ∀ i, w i ∈ S} ≃ (Fin n → S) :=
  { toFun := fun w i => ⟨w.1 i, w.2 i⟩
    invFun := fun f => ⟨fun i => (f i : R), fun i => (f i).2⟩
    left_inv := fun w => by ext i; rfl
    right_inv := fun f => by ext i; rfl }
  have h1 : (box (n := n) S).card = Fintype.card {w : Fin n → R // ∀ i, w i ∈ S} := by
    simp [box, Fintype.card_subtype]
  rw [h1, Fintype.card_congr e, Fintype.card_fun]
  simp

lemma box_inter {n : ℕ} (S T : Finset R) :
    box (n := n) S ∩ box (n := n) T = box (n := n) (S ∩ T) := by
  ext w
  simp only [box, Finset.mem_inter, Finset.mem_filter, Finset.mem_univ, true_and]
  exact ⟨fun h i => ⟨h.1 i, h.2 i⟩, fun h => ⟨fun i => (h i).1, fun i => (h i).2⟩⟩

lemma box_mono {n : ℕ} {S T : Finset R} (h : S ⊆ T) : box (n := n) S ⊆ box (n := n) T := by
  intro w hw
  simp only [box, Finset.mem_filter, Finset.mem_univ, true_and] at hw ⊢
  exact fun i => h (hw i)

lemma card_box3 {n : ℕ} (S : Finset R) (h : S.card = 3) : (box (n := n) S).card = 3 ^ n := by
  rw [card_box, h]

lemma card_box2 {n : ℕ} (S : Finset R) (h : S.card = 2) : (box (n := n) S).card = 2 ^ n := by
  rw [card_box, h]

lemma subset_01_04 : ({0} : Finset R) ⊆ {0, 4} := by decide
lemma eq_01 : t0 ∩ t1 = ({0, 1} : Finset R) := by decide
lemma eq_04 : t1 ∩ t2 = ({0, 4} : Finset R) := by decide
lemma eq_0 : t0 ∩ t2 = ({0} : Finset R) := by decide

lemma card_intersect {n : ℕ} (S T : Finset R) :
    (box (n := n) S ∩ box (n := n) T).card = (S ∩ T).card ^ n := by
  rw [box_inter, card_box]

/-- **(Census, subtraction-free form.)** -/
theorem census_add (n : ℕ) : (good (n := n)).card + 2 ^ (n + 1) = 3 ^ (n + 1) := by
  classical
  have h0 : (box (n := n) t0).card = 3 ^ n := card_box3 t0 (by decide)
  have h1c : (box (n := n) t1).card = 3 ^ n := card_box3 t1 (by decide)
  have h2c : (box (n := n) t2).card = 3 ^ n := card_box3 t2 (by decide)
  have hAB : (box (n := n) t0 ∩ box (n := n) t1).card = 2 ^ n := by
    have c : ({0,1} : Finset R).card = 2 := by decide
    rw [card_intersect, eq_01, c]
  have hBC : (box (n := n) t1 ∩ box (n := n) t2).card = 2 ^ n := by
    have c : ({0,4} : Finset R).card = 2 := by decide
    rw [card_intersect, eq_04, c]
  have hsub : (box (n := n) t0 ∩ box (n := n) t2) ⊆ (box (n := n) t1 ∩ box (n := n) t2) := by
    rw [box_inter, box_inter, eq_0, eq_04]
    exact box_mono subset_01_04
  have hunion : (box (n := n) t0 ∩ box (n := n) t2) ∪ (box (n := n) t1 ∩ box (n := n) t2)
      = (box (n := n) t1 ∩ box (n := n) t2) := Finset.union_eq_right.mpr hsub
  have hd : (box (n := n) t0 ∪ box (n := n) t1) ∩ box (n := n) t2
      = (box (n := n) t0 ∩ box (n := n) t2) ∪ (box (n := n) t1 ∩ box (n := n) t2) := by
    ext w; simp only [Finset.mem_inter, Finset.mem_union]; tauto
  have hI1 := Finset.card_union_add_card_inter (box (n := n) t0) (box (n := n) t1)
  have hI2 := Finset.card_union_add_card_inter
    (box (n := n) t0 ∪ box (n := n) t1) (box (n := n) t2)
  rw [hd, hunion, hBC] at hI2
  have hp2 : 2 ^ (n + 1) = 2 * 2 ^ n := by rw [pow_succ]; ring
  have hp3 : 3 ^ (n + 1) = 3 * 3 ^ n := by rw [pow_succ]; ring
  simp only [good]
  omega

/-- **The census.** -/
theorem census (n : ℕ) : (good (n := n)).card = 3 ^ (n + 1) - 2 ^ (n + 1) := by
  have h := census_add n
  omega


/-! ## Numeric corollaries: the formal count meets the primes

The census theorem gives `3^(n+1) - 2^(n+1)`.  The counts of admissible residue words actually
realised by 5 000 000 primes, measured independently of this file, are

| n | realised in the primes | 3^(n+1) - 2^(n+1) |
|---|---|---|
| 1 | 5   | 5 |
| 2 | 19  | 19 |
| 3 | 65  | 65 |
| 4 | 211 | 211 |
| 5 | 665 | 665 |

For `n = 1,2,3` the count is checked by **direct enumeration** — `decide` filters the words from
scratch and does not invoke the theorem.  For `n = 4,5` the word space (`625` and `3125` functions)
exceeds what the kernel can enumerate in this environment, so those two are read off the theorem and
checked arithmetically; the enumeration for them is performed below by `#eval`, which evaluates rather
than proves, and is labelled accordingly.
-/

set_option maxRecDepth 100000 in
/-- Length 1: five residues, all admissible. Checked by enumeration. -/
example : (good (n := 1)).card = 5 := by decide

set_option maxRecDepth 100000 in
/-- Length 2: 19 of 25. Checked by enumeration. -/
example : (good (n := 2)).card = 19 := by decide

set_option maxRecDepth 100000 in
/-- Length 3: 65 of 125. Checked by enumeration. -/
example : (good (n := 3)).card = 65 := by decide

/-- Length 4: 211 of 625. Read off the census theorem. -/
example : (good (n := 4)).card = 211 := by
  have h := census 4
  norm_num at h
  exact h

/-- Length 5: 665 of 3125. Read off the census theorem. -/
example : (good (n := 5)).card = 665 := by
  have h := census 5
  norm_num at h
  exact h

/-- The closed form reproduces the five measured values. -/
example : (List.range 5).map (fun n => 3 ^ (n + 2) - 2 ^ (n + 2)) = [5, 19, 65, 211, 665] := by
  decide

/-! ### Evaluation (not proof)

These run the counter and print; they corroborate but are not kernel-checked. -/

#eval (List.range 6).map (fun n => (good (n := n)).card)

/-! ## The bridge: from residue words to walk positions

A residue word of length `n` is `w : Fin n → R`, where the letter `w i` encodes the gap residue
`r = 2 * w i ∈ {0,2,4,6,8}` (mod 10).  Since a twin-start gap `d` has `d ≡ r (mod 10)`, it has
`d ≡ 2 * w i (mod 5)`.  The partial sums are `D_k = 2 * S w k` (mod 5), with `S w k` the sum of the
first `k` letters, and the offset set of the forced tuple is `{D_k, D_k + 2 : k ≤ n}`.
A word is admissible at 5 when that offset set is not all of `Z/5`.
-/

/-- The letter extended by `0` beyond the word. -/
def ext {n : ℕ} (w : Fin n → R) (j : ℕ) : R := if h : j < n then w ⟨j, h⟩ else 0

/-- Sum of the first `k` letters. -/
def S {n : ℕ} (w : Fin n → R) (k : ℕ) : R := ∑ j ∈ Finset.range k, ext w j

/-- The walk positions `c_1, …, c_n`. -/
def pos {n : ℕ} (w : Fin n → R) : Fin n → R := fun i => S w (i.val + 1)

/-- The offset set of the forced tuple, reduced mod 5. -/
def offsets {n : ℕ} (w : Fin n → R) : Finset R :=
  ((Finset.range (n + 1)).image (fun k => 2 * S w k)) ∪
  ((Finset.range (n + 1)).image (fun k => 2 * S w k + 2))

/-- **Admissible at 5**: the offsets are not a complete residue system mod 5. -/
def admissible {n : ℕ} (w : Fin n → R) : Prop := offsets w ≠ Finset.univ

instance {n : ℕ} : DecidablePred (admissible (n := n)) := fun w => by
  unfold admissible; infer_instance

lemma S_succ {n : ℕ} (w : Fin n → R) (k : ℕ) : S w (k + 1) = S w k + ext w k := by
  simp [S, Finset.sum_range_succ]

lemma pos_injective (n : ℕ) : Function.Injective (pos (n := n)) := by
  intro w w' h
  have hS : ∀ k, k ≤ n → S w k = S w' k := by
    intro k
    induction k with
    | zero => intro _; simp [S]
    | succ k ih =>
      intro hk
      have := congrFun h ⟨k, by omega⟩
      simpa [pos] using this
  funext i
  have h1 := S_succ w i.val
  have h2 := S_succ w' i.val
  have e1 : S w (i.val + 1) = S w' (i.val + 1) := hS _ (by omega)
  have e0 : S w i.val = S w' i.val := hS _ (by omega)
  have : ext w i.val = ext w' i.val := by
    rw [h1, h2, e0] at e1; exact add_left_cancel e1
  simpa [ext, i.isLt] using this

/-- The set of all walk positions, `c_0 = 0` included. -/
def walkSet {n : ℕ} (w : Fin n → R) : Finset R := (Finset.range (n + 1)).image (S w)

lemma walkSet_eq {n : ℕ} (w : Fin n → R) :
    walkSet w = insert 0 (Finset.univ.image (pos w)) := by
  ext x
  simp only [walkSet, Finset.mem_image, Finset.mem_range, Finset.mem_insert, Finset.mem_univ,
    true_and, pos]
  constructor
  · rintro ⟨k, hk, rfl⟩
    rcases k with _ | k
    · left; simp [S]
    · right; exact ⟨⟨k, by omega⟩, rfl⟩
  · rintro (rfl | ⟨i, rfl⟩)
    · exact ⟨0, by omega, by simp [S]⟩
    · exact ⟨i.val + 1, by omega, rfl⟩

lemma two_mul_bij : Function.Bijective (fun x : R => 2 * x) := by decide

lemma offsets_eq {n : ℕ} (w : Fin n → R) :
    offsets w = (walkSet w ∪ (walkSet w).image (· + 1)).image (fun x => 2 * x) := by
  have h2 : ∀ x : R, 2 * (x + 1) = 2 * x + 2 := by decide
  ext y
  simp only [offsets, walkSet, Finset.mem_union, Finset.mem_image, Finset.mem_range]
  constructor
  · rintro (⟨k, hk, rfl⟩ | ⟨k, hk, rfl⟩)
    · exact ⟨S w k, Or.inl ⟨k, hk, rfl⟩, rfl⟩
    · exact ⟨S w k + 1, Or.inr ⟨S w k, ⟨k, hk, rfl⟩, rfl⟩, h2 _⟩
  · rintro ⟨x, (⟨k, hk, rfl⟩ | ⟨_, ⟨k, hk, rfl⟩, rfl⟩), rfl⟩
    · exact Or.inl ⟨k, hk, rfl⟩
    · exact Or.inr ⟨k, hk, (h2 _).symm⟩

/-- **Bridge lemma** (all subsets of `Z/5` checked): a set of positions containing `0` leaves a
point of `C ∪ (C+1)` uncovered iff it lies in one of the three consecutive triples containing `0`. -/
theorem cover_iff : ∀ C : Finset R, (0 : R) ∈ C →
    ((C ∪ C.image (· + 1)) ≠ Finset.univ ↔ (C ⊆ t0 ∨ C ⊆ t1 ∨ C ⊆ t2)) := by
  decide

lemma image_ne_univ_iff {X : Finset R} :
    X.image (fun x => 2 * x) ≠ Finset.univ ↔ X ≠ Finset.univ := by
  have hinj : Function.Injective (fun x : R => 2 * x) := two_mul_bij.1
  constructor
  · intro h hX; apply h; rw [hX]
    exact Finset.image_univ_of_surjective two_mul_bij.2
  · intro h hX; apply h
    apply Finset.eq_univ_of_card
    rw [← Finset.card_image_of_injective X hinj, hX, Finset.card_univ]

lemma admissible_iff {n : ℕ} (w : Fin n → R) : admissible w ↔ pos w ∈ good := by
  have h0 : (0 : R) ∈ walkSet w := by rw [walkSet_eq]; exact Finset.mem_insert_self _ _
  rw [admissible, offsets_eq, image_ne_univ_iff, cover_iff _ h0, walkSet_eq]
  simp only [good, box, Finset.mem_union, Finset.mem_filter, Finset.mem_univ, true_and,
    Finset.insert_subset_iff, Finset.image_subset_iff]
  have a0 : (0 : R) ∈ t0 := by decide
  have a1 : (0 : R) ∈ t1 := by decide
  have a2 : (0 : R) ∈ t2 := by decide
  simp only [a0, a1, a2, true_and, forall_true_left]
  tauto

/-- **The census, stated on words.** Residue words of length `n` that are admissible at 5 number
`3^(n+1) - 2^(n+1)`. -/
theorem census_words (n : ℕ) :
    (Finset.univ.filter (admissible (n := n))).card = 3 ^ (n + 1) - 2 ^ (n + 1) := by
  rw [← census n]
  have hbij : Function.Bijective (pos (n := n)) :=
    ⟨pos_injective n, Finite.injective_iff_surjective.mp (pos_injective n)⟩
  let e := Equiv.ofBijective _ hbij
  apply Finset.card_bij (fun w _ => e w)
  · intro w hw
    simp only [Finset.mem_filter, Finset.mem_univ, true_and] at hw
    exact (admissible_iff w).mp hw
  · intro a _ b _ h; exact e.injective h
  · intro c hc
    refine ⟨e.symm c, ?_, by simp⟩
    simp only [Finset.mem_filter, Finset.mem_univ, true_and]
    rw [admissible_iff, Equiv.ofBijective_apply_symm_apply pos hbij c]; exact hc

/-! ## Realised words are admissible

Let `a` be a twin start and `d₁, …, dₙ` gaps to later twin starts, with partial sums `Dₖ`, so that
every `a + Dₖ` and `a + Dₖ + 2` is prime. If `a > 5`, the residue word of the gaps is admissible.
The hypothesis `a > 5` is necessary: from `a = 5` the twin starts `5, 11, 17` give the word `(6, 6)`,
which is realised but not admissible. -/

/-- Reduction of a natural number mod 5. -/
def toR (x : ℕ) : R := ⟨x % 5, Nat.mod_lt _ (by norm_num)⟩

lemma toR_add (x y : ℕ) : toR (x + y) = toR x + toR y := by
  apply Fin.ext; simp [toR, Fin.val_add, Nat.add_mod]

lemma toR_eq_iff (x y : ℕ) : toR x = toR y ↔ x % 5 = y % 5 := by
  constructor
  · intro h; exact congrArg Fin.val h
  · intro h; exact Fin.ext h

/-- Partial sums of a gap sequence. -/
def Dn {n : ℕ} (d : Fin n → ℕ) (k : ℕ) : ℕ :=
  ∑ j ∈ Finset.range k, (if h : j < n then d ⟨j, h⟩ else 0)

/-- The residue word of a gap sequence: the letter of `d` is `(d mod 10)/2`. -/
def wordOf {n : ℕ} (d : Fin n → ℕ) : Fin n → R := fun i => toR ((d i % 10) / 2)

lemma two_toR (x : ℕ) : 2 * toR x = toR (2 * x) := by
  apply Fin.ext
  simp only [toR, Fin.val_mul]
  show (2 % 5) * (x % 5) % 5 = 2 * x % 5
  omega

lemma two_S_eq {n : ℕ} (d : Fin n → ℕ) (heven : ∀ i, d i % 2 = 0) :
    ∀ k, 2 * S (wordOf d) k = toR (Dn d k) := by
  intro k
  induction k with
  | zero => simp [S, Dn]; rfl
  | succ k ih =>
    rw [S_succ, mul_add, ih]
    have hD : Dn d (k + 1) = Dn d k + (if h : k < n then d ⟨k, h⟩ else 0) := by
      simp [Dn, Finset.sum_range_succ]
    rw [hD, toR_add]
    congr 1
    by_cases hk : k < n
    · simp only [ext, hk, dite_true, wordOf]
      rw [two_toR, toR_eq_iff]
      have := heven ⟨k, hk⟩
      omega
    · simp only [ext, hk, dite_false]; rfl

/-- **Realised implies admissible.** -/
theorem realised_admissible {n : ℕ} (a : ℕ) (d : Fin n → ℕ) (ha : 5 < a)
    (heven : ∀ i, d i % 2 = 0)
    (hp : ∀ k, k ≤ n → Nat.Prime (a + Dn d k) ∧ Nat.Prime (a + Dn d k + 2)) :
    admissible (wordOf d) := by
  intro huniv
  have hx : (-(toR a)) ∈ offsets (wordOf d) := by rw [huniv]; exact Finset.mem_univ _
  simp only [offsets, Finset.mem_union, Finset.mem_image, Finset.mem_range] at hx
  have key : ∀ m : ℕ, toR m = -(toR a) → Nat.Prime (a + m) → False := by
    intro m hm hpr
    have h0 : toR (a + m) = toR 0 := by rw [toR_add, hm]; simp; rfl
    rw [toR_eq_iff] at h0
    rcases (Nat.dvd_prime hpr).mp (Nat.dvd_of_mod_eq_zero h0) with h | h <;> omega
  have two : (2 : R) = toR 2 := rfl
  rcases hx with ⟨k, hk, hkx⟩ | ⟨k, hk, hkx⟩
  · rw [two_S_eq d heven] at hkx
    exact key _ hkx (hp k (by omega)).1
  · rw [two_S_eq d heven, two, ← toR_add] at hkx
    have hpr := (hp k (by omega)).2
    rw [Nat.add_assoc] at hpr
    exact key _ hkx hpr

/-- The seed counterexample: from `a = 5`, gaps `(6, 6)` are realised (5, 11, 17 are twin starts)
but the word is not admissible. -/
example : ¬ admissible (wordOf (n := 2) (fun _ => 6)) := by decide

/-- …and `5, 7, 11, 13, 17, 19` are all prime, so the word `(6, 6)` really is realised from `a = 5`. -/
example : Nat.Prime 5 ∧ Nat.Prime 7 ∧ Nat.Prime 11 ∧ Nat.Prime 13 ∧ Nat.Prime 17 ∧ Nat.Prime 19 := by
  norm_num

end EJCensus

#print axioms EJCensus.census
#print axioms EJCensus.census_words
#print axioms EJCensus.cover_iff
#print axioms EJCensus.realised_admissible
