# Three keys, same 5 000 000 primes, compared cell by cell

`results/three_keys.py` · data in `data/key1_base_enddigit.csv`, `data/key2_twin_segment.csv`,
`data/key3_smashed.csv`

---

## Key 1 — EJ's base prime end-digit key

$(d_1 \to d_2) \mapsto g \bmod 10$. Each cell gives **exactly one** gap last digit (Theorem 3).

| from | →1 | →3 | →7 | →9 |
|---|---:|---:|---:|---:|
| **1** | 0 · 220 539 | 2 · 380 424 | 6 · 388 660 | 8 · 260 209 |
| **3** | 8 · 295 354 | 0 · 207 458 | 4 · 358 921 | 6 · 388 461 |
| **7** | 4 · 319 814 | 6 · 341 870 | 0 · 207 687 | 2 · 380 708 |
| **9** | 2 · 414 126 | 4 · 320 442 | 8 · 294 810 | 0 · 220 515 |

*(plus the seed `5→7 = 2`, count 1)*

Residue multiplicities: `0` in 4 cells, `2, 4, 6, 8` in 3 cells each — 16 cells, 5 residues.
Cell counts span a factor **2.00** (207 458 → 414 126).

## Key 2 — twin prime segment key

$(bg \to ep) \mapsto (ep - bg) \bmod 10$. This is the twin key set from the last round.

| cell | span last digit | count |
|---|---:|---:|
| 1→1 | 0 | 42 406 |
| 1→3 | 2 | 39 745 |
| 1→9 | 8 | 46 562 |
| 7→1 | 4 | 46 462 |
| 7→3 | 6 | 42 718 |
| 7→9 | 2 | 39 340 |
| 9→1 | 2 | 39 272 |
| 9→3 | 4 | 46 249 |
| 9→9 | 0 | 42 618 |

*(plus seed `5→3 = 8`, count 1)*

9 cells, 5 residues with multiplicities `2`→3, `0`→2, `4`→2, `8`→2, `6`→1.
Cell counts span a factor **1.19** (39 272 → 46 562).

## Key 3 — two segments smashed: inner bg and ep become inner nodes

Take segments $k$ and $k+1$, keep the outer endpoints $bg_k$ and $ep_{k+1}$; the inner nodes are the
twin pair $(a_{k+1},\ a_{k+1}+2) = (bg_{k+1},\ ep_k)$.

$$\text{smashed gap} = ep_{k+1} - bg_k = d_k + d_{k+1} + 2 \;\equiv\; 2 \pmod 6$$

| cell | gap last digit | gap mod 30 | count | most common gaps |
|---|---:|---:|---:|---|
| 1→1 | 0 | **20** | 43 196 | 200 (2 798), 170 (2 791), 380, 350 |
| 1→3 | 2 | **2** | 42 165 | 212 (3 153), 242 (2 584), 422, 182 |
| 1→9 | 8 | **8** | 43 352 | 308 (2 834), 158 (2 729), 338, 368 |
| 7→1 | 4 | **14** | 43 026 | 254, 464, 224, 284 |
| 7→3 | 6 | **26** | 43 336 | 266 (2 914), 296 (2 747), 326 |
| 7→9 | 2 | **2** | 42 158 | 212 (3 025), 242, 422, 182 |
| 9→1 | 2 | **2** | 41 918 | 212 (3 028), 242, 422, 392 |
| 9→3 | 4 | **14** | 43 212 | 464, 254, 224, 284 |
| 9→9 | 0 | **20** | 43 009 | 170 (2 733), 200 (2 712), 380, 410 |

*(plus seed `5→9 = 4`, count 1)*

Cell counts span a factor **1.03** (41 918 → 43 352).

---

## What the three keys together say

**1. The new key is stronger than the base key.** Because every twin-anchored span satisfies
`span ≡ 2 (mod 6)`, the last digit no longer leaves the residue mod 30 undetermined:

| last digit | 0 | 2 | 4 | 6 | 8 |
|---|---|---|---|---|---|
| base key: gap mod 30 | {0,10,20} | {2,12,22} | {4,14,24} | {6,16,26} | {8,18,28} |
| **new key: gap mod 30** | **20** | **2** | **14** | **26** | **8** |

Three possibilities collapse to one. That is the "natural and normal" arithmetic of the smashed
segments: `g = 6m + 2` and `g mod 10` are compatible in exactly one class mod 30. Verified: every
gap in every cell lies in the single class listed.

**2. The keys get more uniform as you aggregate.** Cell counts span a factor of 2.00 (Key 1),
1.19 (Key 2), 1.03 (Key 3). The last-digit bias is a first-order effect that averages out as more
primes are folded into each cell — the same drift measured before, seen from the key side.

**3. The multiplicity pattern is the signature of each key.** 4-3-3-3-3 for the base key,
3-2-2-2-1 for the twin key. Those numbers are the count of cells feeding each residue, and they set
what the keys can and cannot distinguish.

**4. The gap values inside a cell are not arbitrary.** Cell `1→3` prefers 212, `1→1` prefers 200 and
170, `7→3` prefers 266 — different preferred values per cell, even though all are ≡ 2 mod 30 within
their class. That is the leftover with content: the key fixes the class, not the member.
