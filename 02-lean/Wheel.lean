import Mathlib.Data.Fintype.BigOperators
import Mathlib.Data.Fintype.Powerset
import Mathlib.Data.ZMod.Basic
import Mathlib.Data.Nat.Prime.Basic
import Mathlib.Tactic.NormNum.Prime
import Mathlib.Tactic.Ring
import Mathlib.Tactic.Tauto

/-!
# The base-10 wheel in coordinates

`Z/10 ≅ Z/2 × Z/5` (Chinese remainder theorem). We call `x % 2` the *layer* and `x % 5` the *hue*.
These are names for coordinates, not colorimetric claims.
-/

namespace EJWheel

abbrev W := Fin 10

/-- The four units of `Z/10`. -/
def units10 : Finset W := {1, 3, 7, 9}

/-- **Coordinates.** A digit is determined by its layer and its hue. -/
theorem layer_hue_determine : ∀ x y : W, x.val % 2 = y.val % 2 → x.val % 5 = y.val % 5 → x = y := by
  decide

/-- **Orbits.** Under multiplication by units, two digits lie in the same orbit iff they have the
same gcd with 10. The orbits are `{0}`, `{5}`, `{2,4,6,8}`, `{1,3,7,9}`. -/
theorem orbit_iff_gcd : ∀ x y : W,
    (∃ u ∈ units10, y = u * x) ↔ Nat.gcd x.val 10 = Nat.gcd y.val 10 := by
  decide

/-- **Units fix the layer.** -/
theorem units_fix_layer : ∀ u ∈ units10, ∀ x : W, (u * x).val % 2 = x.val % 2 := by
  decide

/-- **A quarter turn.** Multiplication by `7` cycles each layer through four hues:
`1 → 7 → 9 → 3 → 1` and `6 → 2 → 4 → 8 → 6`; it fixes `0` and `5`. -/
theorem quarter_turn :
    (7 : W) * 1 = 7 ∧ (7 : W) * 7 = 9 ∧ (7 : W) * 9 = 3 ∧ (7 : W) * 3 = 1 ∧
    (7 : W) * 6 = 2 ∧ (7 : W) * 2 = 4 ∧ (7 : W) * 4 = 8 ∧ (7 : W) * 8 = 6 ∧
    (7 : W) * 0 = 0 ∧ (7 : W) * 5 = 5 := by
  decide

/-- **Complement is the half turn.** Multiplication by `9` is negation. -/
theorem complement_is_neg : ∀ x : W, 9 * x = -x := by decide

/-- **Adding the grey point swaps layers and keeps hue.** -/
theorem add_five : ∀ x : W, (x + 5).val % 5 = x.val % 5 ∧ (x + 5).val % 2 ≠ x.val % 2 := by
  decide

/-- **Twin pairs avoid the grey hue.** If `a` and `a + 2` are both prime and `a > 5`, then neither
has hue `0`; equivalently `a % 5 ∈ {1, 2, 4}`. -/
theorem twin_hue {a : ℕ} (ha : Nat.Prime a) (ha2 : Nat.Prime (a + 2)) (h5 : 5 < a) :
    a % 5 = 1 ∨ a % 5 = 2 ∨ a % 5 = 4 := by
  have n0 : a % 5 ≠ 0 := by
    intro h
    rcases (Nat.dvd_prime ha).mp (Nat.dvd_of_mod_eq_zero h) with h' | h' <;> omega
  have n3 : a % 5 ≠ 3 := by
    intro h
    have : 5 ∣ a + 2 := Nat.dvd_of_mod_eq_zero (by omega)
    rcases (Nat.dvd_prime ha2).mp this with h' | h' <;> omega
  omega

/-- **Twin-start digits.** If `a` and `a + 2` are both prime and `a > 5`, then `a` ends in 1, 7 or 9. -/
theorem twin_start_digit {a : ℕ} (ha : Nat.Prime a) (ha2 : Nat.Prime (a + 2)) (h5 : 5 < a) :
    a % 10 = 1 ∨ a % 10 = 7 ∨ a % 10 = 9 := by
  have hodd : a % 2 = 1 := by
    by_contra h
    have : 2 ∣ a := Nat.dvd_of_mod_eq_zero (by omega)
    rcases (Nat.dvd_prime ha).mp this with h' | h' <;> omega
  rcases twin_hue ha ha2 h5 with h | h | h <;> omega

/-! ## Colour at scale: the 100-wheel over the 10-wheel -/

/-- **Classes project to classes.** The coarse class of `x` (its gcd with 10) is a function of its
fine class (its gcd with 100): `gcd(x mod 10, 10) = gcd(gcd(x, 100), 10)`. -/
theorem coarse_of_fine : ∀ x : Fin 100, Nat.gcd (x.val % 10) 10 = Nat.gcd (Nat.gcd x.val 100) 10 := by
  decide

/-- **Nine classes at scale 100.** Every `x` in `Z/100` has gcd with 100 among the nine divisors
`1, 2, 4, 5, 10, 20, 25, 50, 100`, and each of the nine occurs. -/
theorem nine_classes :
    (∀ x : Fin 100, Nat.gcd x.val 100 ∈ [1, 2, 4, 5, 10, 20, 25, 50, 100]) ∧
    (∀ g ∈ [1, 2, 4, 5, 10, 20, 25, 50, 100], ∃ x : Fin 100, Nat.gcd x.val 100 = g) := by
  constructor
  · decide
  · intro g hg
    simp only [List.mem_cons, List.not_mem_nil, or_false] at hg
    rcases hg with rfl | rfl | rfl | rfl | rfl | rfl | rfl | rfl | rfl
    · exact ⟨1, by decide⟩
    · exact ⟨2, by decide⟩
    · exact ⟨4, by decide⟩
    · exact ⟨5, by decide⟩
    · exact ⟨10, by decide⟩
    · exact ⟨20, by decide⟩
    · exact ⟨25, by decide⟩
    · exact ⟨50, by decide⟩
    · exact ⟨0, by decide⟩

/-- **The fine hue circle.** `2` generates the twenty units of `Z/25`: its first twenty powers are
distinct and the twentieth is `1`. -/
theorem two_generates_mod25 :
    ((List.range 20).map (fun k => 2 ^ k % 25)).Nodup ∧ 2 ^ 20 % 25 = 1 := by
  decide

/-- **Zooming keeps the coarse order.** Along the fine circle, the coarse hue of step `θ` is the
coarse hue of step `θ mod 4`: the fine circle wraps the coarse one five times in one direction. -/
theorem fine_projects_to_coarse : ∀ θ : Fin 20, (2 ^ θ.val % 25) % 5 = 2 ^ (θ.val % 4) % 5 := by
  decide

/-- **The fine generators.** The generators of the units of `Z/25` are exactly
`2, 3, 8, 12, 13, 17, 22, 23` — eight of them. (That these give `8 / 2 = 4` circles up to
reflection is argued in the paper, Proposition 22(a), not here.) -/
theorem generators_mod25 : ∀ g : Fin 25,
    (((List.range 20).map (fun k => g.val ^ k % 25)).Nodup ∧ g.val ^ 20 % 25 = 1) ↔
      g.val ∈ [2, 3, 8, 12, 13, 17, 22, 23] := by
  decide

/-- **Every fine generator reduces to a coarse generator** (`2` or `3` mod 5), so every fine circle
projects onto the coarse circle, forwards or backwards. -/
theorem generators_reduce : ∀ g ∈ [2, 3, 8, 12, 13, 17, 22, 23], g % 5 = 2 ∨ g % 5 = 3 := by
  decide

/-- **The second zoom.** All five lifts of `2` from `Z/25` to `Z/125` (`2, 27, 52, 77, 102`)
generate the hundred units of `Z/125`: at this step every refinement of the order is allowed. -/
theorem lifts_mod125 : ∀ g ∈ [2, 27, 52, 77, 102],
    ((List.range 100).map (fun k => g ^ k % 125)).Nodup ∧ g ^ 100 % 125 = 1 := by
  decide

/-! ## Delays on the wheel -/

/-- **Free hues of a twin delay.** For a delay `h` between two twin pairs, the number of hues `a`
(mod 5) at which all four members `a, a+2, a+h, a+h+2` avoid the grey hue `0` is `3, 1, 2, 2, 1`
for `h ≡ 0, 1, 2, 3, 4 (mod 5)`. -/
theorem free_hues : ∀ h : Fin 5,
    (Finset.univ.filter (fun a : Fin 5 => a ≠ 0 ∧ a + 2 ≠ 0 ∧ a + h ≠ 0 ∧ a + h + 2 ≠ 0)).card =
      [3, 1, 2, 2, 1].getD h.val 0 := by
  decide

/-- **Free hues = translations off grey.** The count above is `5` minus the number of distinct hues
in the offset pattern `{0, 2, h, h+2}`. -/
theorem free_hues_eq : ∀ h : Fin 5,
    (Finset.univ.filter (fun a : Fin 5 => a ≠ 0 ∧ a + 2 ≠ 0 ∧ a + h ≠ 0 ∧ a + h + 2 ≠ 0)).card =
      5 - ({0, 2, h, h + 2} : Finset (Fin 5)).card := by
  decide

end EJWheel

#print axioms EJWheel.layer_hue_determine
#print axioms EJWheel.orbit_iff_gcd
#print axioms EJWheel.units_fix_layer
#print axioms EJWheel.quarter_turn
#print axioms EJWheel.complement_is_neg
#print axioms EJWheel.add_five
#print axioms EJWheel.twin_hue
#print axioms EJWheel.twin_start_digit
#print axioms EJWheel.coarse_of_fine
#print axioms EJWheel.nine_classes
#print axioms EJWheel.two_generates_mod25
#print axioms EJWheel.fine_projects_to_coarse
#print axioms EJWheel.generators_mod25
#print axioms EJWheel.generators_reduce
#print axioms EJWheel.lifts_mod125
#print axioms EJWheel.free_hues
#print axioms EJWheel.free_hues_eq
