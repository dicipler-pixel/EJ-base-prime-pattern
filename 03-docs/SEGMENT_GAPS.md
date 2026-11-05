# The gaps inside every twin-prime segment, and the total gap number

`results/segment_gaps.py` · 5 000 000 primes · 385 373 segments

Files: `data/segments_gaps_5M.csv` (one row per segment, gaps included) ·
`data/total_gaps_5M.csv` (one row per distinct total)

---

## The matching-up check

For every segment the internal gaps sum to `ep − bg`:

$$\sum \text{(gaps from } bg \text{ to } ep\text{)} = ep-bg \qquad \textbf{385 373 / 385 373}$$

That is the telescoping identity, so it cannot fail — every segment's gaps add up to its total by
construction. The table below makes it checkable row by row (`check_total_equals_span` column).

What is *not* automatic, and is real prime content:

| fact | verification |
|---|---|
| every segment's gap string **starts with 2** (the opening twin gap) | 385 373 / 385 373 |
| every segment's gap string **ends with 2** (the closing twin gap) | 385 373 / 385 373 |
| **no 2 anywhere in the middle** | 0 occurrences |
| smallest middle gap is 4 | exact |
| middle sum $=$ total $-4\equiv 4 \pmod 6$ | all but the single `[3,7]` |

So every segment is `2 · [gaps ≥ 4] · 2`. A 2 inside the middle would be a twin pair, and a segment
by definition ends at the first twin after its start.

## Total gap numbers

$ \text{total} = d_k + 2$, and the total is $2 \pmod 6$ for every segment except the first.

| | |
|---|---|
| distinct total gap numbers | **355** |
| range | 4 → 2 834 |
| mean / median | 225.24 / 164 |
| gaps per segment | mean 13.97, median 11, max 152 |
| 50 % / 90 % / 99 % of segments | ≤ 164 / ≤ 500 / ≤ 992 |
| most common total | **32** (15 620 segments, 4.05 %) |

| total | count | share | cum. | distinct internal sequences | most common |
|---:|---:|---:|---:|---:|---|
| 4 | 1 | 0.00 % | 0.00 % | 1 | `2-2` |
| 8 | 4 263 | 1.11 % | 1.11 % | 1 | `2-4-2` |
| 14 | 11 209 | 2.91 % | 4.01 % | 3 | `2-10-2` (9 362) |
| 20 | 8 120 | 2.11 % | 6.12 % | 8 | `2-16-2` (4 689) |
| 26 | 5 098 | 1.32 % | 7.44 % | 12 | `2-22-2` (2 376) |
| 32 | **15 620** | 4.05 % | 11.49 % | 69 | `2-28-2` (4 637) |
| 44 | 14 227 | 3.69 % | 16.36 % | 343 | `2-40-2` (1 955) |
| 62 | 11 174 | 2.90 % | 22.52 % | 2 302 | `2-58-2` (505) |
| 92 | 10 864 | 2.82 % | 32.63 % | 8 294 | `2-88-2` (54) |

## What the totals say

**1. The total gap number is not new information.** Since total $= d_k+2$, knowing the total is
knowing the twin-start gap exactly. It is a relabelling of the counterflow's `d_k`, not a second
measurement.

**2. But it is a very incomplete description of the interior.** A single total (92) is realised by
**8 294 distinct internal gap sequences**; total 62 by 2 302; total 32 by 69. The number of
compositions explodes, and the frequencies are far from uniform inside a total.

**3. Inside every total, one shape dominates: a single gap flanked by the twins.**
`2-(T−4)-2` is the most common sequence for *every* total in the table — 83.5 % of total-14
segments, 54 % of total-32, but only 0.6 % of total-92 as the alternatives multiply.

**4. The uniform case is the smallest.** Total 8 admits exactly one sequence (`2-4-2`), and it
occurs 4 263 times. Total 14 admits three. Diversity grows with the total, as it must.

## Reading the dataset

```
segments_gaps_5M.csv : seg, bg, ep, n_gaps, gaps, total_gap, check_total_equals_span
                       e.g.  2, 5, 13, 3, "2-4-2", 8, True
total_gaps_5M.csv    : total_gap, count, share_%, cum_%, n_distinct_sequences,
                       most_common_sequence, its_count
```

`gaps` is the full string from `bg` to `ep`, so `sum(gaps.split('-')) == total_gap == ep - bg` is
checkable in the spreadsheet with one formula per row.
