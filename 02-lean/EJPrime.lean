import Mathlib.Data.Fintype.BigOperators
import Mathlib.Data.Fintype.Powerset
import Mathlib.Data.ZMod.Basic
import Mathlib.Data.Nat.Prime.Basic
import Mathlib.Tactic.NormNum.Prime
import Mathlib.Tactic.Ring
import Mathlib.Tactic.Tauto

/-!
# The kept results: EJ's base prime pattern and twin structure

Kept after review: the digit-exclusivity theorems, the uniqueness of the 3-5-7 junction,
the arithmetic of the equilibrium obstruction, and the obstruction itself stated on primes. The census theorem is in `Census.lean`.
-/

namespace EJPrime

/-! ## 1. Digit exclusivity -/

/-- If `p` ends in 3 then `5 ∣ p + 2`. -/
theorem five_dvd_of_ends_three {p : ℕ} (h : p % 10 = 3) : 5 ∣ p + 2 := by
  apply Nat.dvd_of_mod_eq_zero
  omega

/-- **No twin start above 3 ends in 3.** If `p` ends in 3 then `p + 2` ends in 5, hence is a
multiple of 5 and greater than 5, so it cannot be prime: `p` is not the start of a twin pair.
(Primes ending in 3 above 3 exist -- 13, 23, 43 -- they are simply not twin starts.) -/
theorem not_prime_add_two {p : ℕ} (hp : p % 10 = 3) (h3 : 3 < p) :
    ¬ Nat.Prime (p + 2) := by
  intro hpr
  have h5 : 5 ∣ p + 2 := five_dvd_of_ends_three hp
  rcases (Nat.dvd_prime hpr).mp h5 with h | h <;> omega

/-- **No twin end prime above 7 ends in 7.** If `q` ends in 7 and its twin predecessor `q - 2` is
prime, then `q - 2` ends in 5 and is divisible by 5, so `q - 2 = 5` and `q = 7`.
(Primes ending in 7 above 7 exist -- 17, 37, 47 -- they are simply not end primes of twin pairs.) -/
theorem seven_of_ends_seven {q : ℕ} (hq : q % 10 = 7)
    (hp : Nat.Prime (q - 2)) : q = 7 := by
  have h5 : 5 ∣ q - 2 := by
    apply Nat.dvd_of_mod_eq_zero
    omega
  rcases (Nat.dvd_prime hp).mp h5 with h | h
  · omega
  · omega

/-! ## 2. Uniqueness of the 3-5-7 junction -/

/-- Among `p-2, p, p+2` exactly one is divisible by 3; if all three are prime then `p = 5`. -/
theorem junction_unique {p : ℕ} (hp : 2 < p) (h1 : Nat.Prime (p - 2))
    (h2 : Nat.Prime p) (h3 : Nat.Prime (p + 2)) : p = 5 := by
  have hcases : p % 3 = 0 ∨ p % 3 = 1 ∨ p % 3 = 2 := by omega
  rcases hcases with h | h | h
  · have h3dvd : 3 ∣ p := Nat.dvd_of_mod_eq_zero h
    rcases (Nat.dvd_prime h2).mp h3dvd with h' | h'
    · exact absurd h' (by norm_num)
    · have hpp : p - 2 = 1 := by omega
      rw [hpp] at h1
      exact absurd h1 (by norm_num)
  · have h3dvd : 3 ∣ p + 2 := by
      apply Nat.dvd_of_mod_eq_zero; omega
    rcases (Nat.dvd_prime h3).mp h3dvd with h' | h'
    · exact absurd h' (by norm_num)
    · omega
  · have h3dvd : 3 ∣ p - 2 := by
      apply Nat.dvd_of_mod_eq_zero; omega
    rcases (Nat.dvd_prime h1).mp h3dvd with h' | h'
    · exact absurd h' (by norm_num)
    · omega

/-! ## 3. The equilibrium obstruction: `2v - u mod 10`, computed in ℕ as `2v + 10 - u` -/

/-- The four forbidden cells, written `u → v` for the end digits of consecutive twin starts
(`1→7, 7→1, 9→1, 9→7`), give `2v - u ≡ 3` or `5 (mod 10)` — digits no twin start above 5 carries. -/
theorem forbidden_cells :
    (2 * 7 + 10 - 1) % 10 = 3 ∧ (2 * 1 + 10 - 7) % 10 = 5 ∧
    (2 * 1 + 10 - 9) % 10 = 3 ∧ (2 * 7 + 10 - 9) % 10 = 5 := by
  refine ⟨?_, ?_, ?_, ?_⟩ <;> norm_num

/-- The five permitted cells `1→9, 1→1, 7→9, 7→7, 9→9` give `2v - u ≡ 1, 7` or `9 (mod 10)`. -/
theorem permitted_cells :
    (2 * 9 + 10 - 1) % 10 = 7 ∧ (2 * 1 + 10 - 1) % 10 = 1 ∧
    (2 * 9 + 10 - 7) % 10 = 1 ∧ (2 * 7 + 10 - 7) % 10 = 7 ∧
    (2 * 9 + 10 - 9) % 10 = 9 := by
  refine ⟨?_, ?_, ?_, ?_, ?_⟩ <;> norm_num

/-! ## 4. The equilibrium obstruction, stated on primes -/

/-- If `a` and `a + 2` are both prime and `a > 5`, then `a` ends in 1, 7 or 9. -/
theorem twin_start_digit {a : ℕ} (ha : Nat.Prime a) (ha2 : Nat.Prime (a + 2)) (h5 : 5 < a) :
    a % 10 = 1 ∨ a % 10 = 7 ∨ a % 10 = 9 := by
  have hodd : a % 2 = 1 := by
    by_contra h
    have : 2 ∣ a := Nat.dvd_of_mod_eq_zero (by omega)
    rcases (Nat.dvd_prime ha).mp this with h' | h' <;> omega
  have n0 : a % 5 ≠ 0 := by
    intro h
    rcases (Nat.dvd_prime ha).mp (Nat.dvd_of_mod_eq_zero h) with h' | h' <;> omega
  have n3 : a % 5 ≠ 3 := by
    intro h
    have : 5 ∣ a + 2 := Nat.dvd_of_mod_eq_zero (by omega)
    rcases (Nat.dvd_prime ha2).mp this with h' | h' <;> omega
  have h5' : a % 5 = 1 ∨ a % 5 = 2 ∨ a % 5 = 4 := by omega
  rcases h5' with h | h | h <;> omega

/-- **Equilibrium obstruction.** Let `a < b` be twin starts above 5 such that `2b - a` is also a
twin start (two equal consecutive gaps, `b - a = (2b - a) - b`). Then the end digits `u → v` of
`a, b` are not one of the four forbidden cells `1→7, 7→1, 9→1, 9→7`. -/
theorem equilibrium_obstruction {a b : ℕ} (hab : a < b) (h5 : 5 < a)
    (hc : Nat.Prime (2 * b - a)) (hc2 : Nat.Prime (2 * b - a + 2)) :
    ¬ ((a % 10 = 1 ∧ b % 10 = 7) ∨ (a % 10 = 7 ∧ b % 10 = 1) ∨
       (a % 10 = 9 ∧ b % 10 = 1) ∨ (a % 10 = 9 ∧ b % 10 = 7)) := by
  have := twin_start_digit hc hc2 (by omega)
  omega

end EJPrime

#print axioms EJPrime.not_prime_add_two
#print axioms EJPrime.seven_of_ends_seven
#print axioms EJPrime.junction_unique
#print axioms EJPrime.forbidden_cells
#print axioms EJPrime.permitted_cells
#print axioms EJPrime.twin_start_digit
#print axioms EJPrime.equilibrium_obstruction
