# Current-art check on what we "discovered"

Checked 2026 against primary sources. **Verdict: our central new "result" is already in the
literature, published twice, and one of my claims has to be demoted.**

## The literature

| source | what it establishes | how it hits us |
|---|---|---|
| Lemke Oliver & Soundararajan, *Unexpected biases in the distribution of consecutive primes*, PNAS 2016, [arXiv:1603.03720](https://arxiv.org/abs/1603.03720) | The 4×4 last-digit transition matrix is biased; a Main Conjecture from Hardy–Littlewood gives `π(x;q,a) = li(x)/φ(q)^r (1 + c₁ loglog x/log x + c₂/log x + …)` with `c₁ = φ(q)/2·(r−1)/φ(q) − #{i : a_i ≡ a_{i+1}}`. Also: the primes mod q are **not Markovian** (Conjecture 1.4), and the reverse patterns are symmetric (1.5). | Our 4×4 matrix and the "1.24 pp residual" are their `c₂` term. |
| Holt, *Expected biases in the distribution of consecutive primes*, [arXiv:2405.03540](https://arxiv.org/abs/2405.03540) (2024) and *On the last digits of consecutive primes*, [arXiv:1604.02443](https://arxiv.org/abs/1604.02443) | Gaps grouped into **"teams" by `g mod 10`**; and, verbatim: *"the class `r=0` has four ordered pairs `(a,b)` assigned to it and the other classes each have three, so we would expect the class `r=0` to occur 4/3 times as often as any other class."* Plus an exact Eratosthenes-sieve dynamical model for the gap populations `w_{g,1}(p#)`, showing the biases are **transient** and reverse at enormous `x`. | **This is our digit-count rule.** The "teams" are our routes, at class level. |
| Kühn / jumping champions line, [arXiv:0910.2960](https://arxiv.org/abs/0910.2960) | Gap frequencies `∝ 𝔖(g) = 2C₂ ∏_{q|g, q>2}(q−1)/(q−2)`. | The class ratios we measured have this shape. |
| MathWorld, *Consecutive Prime Bias* | Textbook summary of the above. | — |

## What this means, claim by claim

| our claim | status after the check |
|---|---|
| "the gap has two routes, split by counting end digits" | **Known at class level** (Holt's 4/3 rule). Our per-gap, per-decade-crossing refinement is the only part I could not find stated. Call it a refinement of Holt, not a discovery. |
| "the residual is the real target" | **Already a research programme** (Holt's sieve dynamics; L-O-S's Main Conjecture). Not new; and it has a published mechanism. |
| "the bias is the one genuine correlation in the data" | True, but it is the best-studied correlation in the primes' last digits. |
| Conjecture 16 (mod-9 twin types each 1/3) | Follows from the same Hardy–Littlewood framework; the limit is equidistribution, with L-O-S-type secondary terms. Not novel. |
| the diamond / dimension construction | Not in the literature, because there is nothing to publish: `g = 10k + δ` is arithmetic, and `dim = g/2` holds for any odd sequence. As a **notation** it is hers and is fine. |

## The consequence she needs to hear

Holt proves the bias is **transient**: it fades and reverses far beyond the computational range.
So any "key" that rests on the observed last-digit bias — including any light/dimension reading
built on it — is reading a finite-range artefact that is *known to go away*. That is not my
opinion; it is a published result. It is the strongest single argument for keeping the
construction as notation and not as physics.

## Divide and conquer

**Queue A — her path: the construction.** Deliverable: one exact rule sheet.
- `g = 10k + δ`; diamonds `⌊g/4⌋`; dimensions `g/2`; 1D ⟺ `g = 2`.
- The segment ladder: `inner_nodes = π(ep−2) − π(bg+1)`; the 1/2/5/8 gap-sum ladder with its
  single `(3,5)` exception.
- Success criterion: **20 hand-checked rows**, no computers. If those hold, the notation is sound.
- Stop rule: no physical word enters the sheet.

**Queue B — my path: the statistics.** Deliverable: test the residual against a published model.
- Implement Holt's recursion for `w_{g,1}(p#)` and ask whether it reproduces the 1.24 pp residual
  and its concentration at `g = 22, 44, 76, 82`. If it does, our residual is *explained*, and the
  "new target" closes.
- Extend the route split to base 30 and 210. Holt says "a few other bases"; check where he stops,
  and whether the two-route refinement survives at base 30.
- Test whether the route residuals organise by `𝔖(g)`. First pass: they do not organise by any
  small factor (all gaps are even, and the top gaps 22, 44, 76, 82 share no prime factor beyond 2).

**The key between the two paths — and it is a real one.** Her pictures are drawn along the
**decade** axis; his statistics live on the **digit** axis. They are the two coordinates of the
same table, `(k, δ)`, and `data/key_table_5M.csv` is that table with counts. So:

> every claim from Queue A must be expressible as a statement about `(k, δ)` counts before it
> counts as a result — and every Queue B result that cannot be drawn on her grid is probably not
> about her objects.

That is the comparison protocol. Nothing crosses between the paths except through that table.

## Ranked new angles

1. **Holt's recursion vs our residual.** Highest value: it either explains the 1.24 pp or shows
   Holt's model is incomplete at second order. Both are publishable-quality outcomes, and neither
   requires new theory.
2. **Route split at base 30/210.** The refinement may be genuinely new there; the 4/3 rule becomes
   a product over the base's primes, and the route count grows. Check against Holt's "few other bases".
3. **Two-digit conditioning** (`(d_k, d_{k+1})` → route). The 4×4 matrix is first order; L-O-S's
   Conjecture 1.4 says the primes mod q are not Markovian, which predicts exactly the kind of
   second-order structure our residual shows. That is a *prediction* to test, not a coincidence to
   hunt.

## Honest limits of this check

I read the abstracts and the quoted passages of the three papers, not their full texts, and I
searched four phrasings. A per-gap two-route split could exist in Holt's Section 2 or in the
Eratosthenes-sieve literature under a different name ("teams", "gap populations per class stage").
Before claiming the refinement, read Holt §2–3 in full. Everything else above is quoted directly.
