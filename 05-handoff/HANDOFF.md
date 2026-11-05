# Handoff: publish this pack

Instructions for an automated agent. Follow the steps in order. Every step has a gate. If a gate
fails, **stop and report**; do not continue.

**Run every command from the pack root**, the folder that holds `README.md`, `01-report/`,
`02-lean/` and the rest. Machine-readable companion: `05-handoff/manifest.json`.

**Revision 7 (2026-11-05).** This revision adds Section 6, Delays on the wheel, with two more
`Wheel.lean` facts and `04-verification/delay_check.py`.

**Revision 6 (2026-11-05).** This revision adds Section 5.4, Colour at scale, with seven more
`Wheel.lean` facts and `04-verification/scale_check.py`.

**Revision 5 (2026-11-05).** This revision adds a strengthened paper and a third Lean file,
`Wheel.lean`, following two rounds of independent review. All three Lean files were compiled by
the preparer, with no `sorry`. See `CHANGES.md`.

**Revision 4 (2026-11-05).** The paper is unchanged from revision 3. Revision 4 corrects the
supporting files: the reviewer brief and three docs still carried the false statements fixed in
revision 3, the handoff pointed at a file layout the pack doesn't use, `manifest.json` was missing,
and the Zenodo description still said "five" formalised results. See `CHANGES.md`. If your copy of
any file does not match its sha256 in the manifest, you don't have the revision named in the manifest: **do not publish it.**

---

## 0. What is being published, and by whose authority

| who | what |
|---|---|
| **Elizabeth Johnson** (`@Ellyrox110`) | the framework: base-10 encoding, end-digit key, twin segmentation, colour scheme. Already published, DOI `10.5281/zenodo.23378596`. |
| **Elizabeth Johnson and Jeromie Beasley** | the new results in this pack, jointly. |

**Posting.** Posted by Jeromie Beasley with Elizabeth Johnson's knowledge; she may fork it or request changes (2026-11-04; recorded in `02-lean/README.md` and on page 1 of the report).

**Attribution note.** A related document, *Advanced Color Theory in Relations to Primes* (Elizabeth Johnson and Shaun Neer, October 2026), lists a second author. The attribution of the colour scheme and its mixing rules, credited here to Elizabeth Johnson, is still being verified with the authors, and will be corrected in a later revision if needed. Keep this note in any description you publish.

**Hard constraint.** Do not modify or re-upload her existing Zenodo record. This pack is a *new*
deposit that cites hers.

---

## 1. Gate: verify before publishing anything

### 1a. Integrity and wording

```bash
python3 05-handoff/check_pack.py
```

This checks every file against `05-handoff/manifest.json` by sha256. It also scans the reviewer
brief, the report source and the docs for the withdrawn false statements listed in
`manifest.json` → `forbidden_phrases`.

**Gate:** the last line must be `PACK OK`.

### 1b. Lean

All three Lean files start with `import Mathlib`, so plain `lean FILE` fails unless Mathlib is installed.
Use a Lake project pinned to the same toolchain (or build `07-lean-package/`):

```bash
lake new ejcheck math
cd ejcheck
echo 'leanprover/lean4:v4.33.0' > lean-toolchain
lake update && lake exe cache get
lake env lean ../02-lean/Census.lean
lake env lean ../02-lean/EJPrime.lean
lake env lean ../02-lean/Wheel.lean
cd ..
```

Expected output, in full, is in `manifest.json` → `verification.expected_stdout`:

* `Census.lean`: `[1, 5, 19, 65, 211, 665]`, then four axiom lines (`census`, `census_words`,
  `cover_iff`, `realised_admissible`);
* `EJPrime.lean`: seven axiom lines;
* `Wheel.lean`: seventeen axiom lines.

Compare the output line by line with the manifest.

**Gates:**

* No line may contain `sorryAx`, and there must be no `error:` lines.
* If Lean or the Mathlib cache can't be obtained, record **"Lean build: not verified"**. You may
  continue, but the deposit description in step 3 must then use the *unverified* sentence given
  there.

### 1c. Numeric checks (optional, about 1 minute, needs numpy and pandas)

```bash
mkdir -p /tmp/ejrun && (cd /tmp/ejrun && python3 "$OLDPWD/04-verification/verify_all.py")
```

**Gate:** the output must say `ALL PASS  24/24`.

---

## 2. Publish to a git repository

Private or public: the URL decides; nothing else changes.

```bash
./05-handoff/push.sh git@github.com:dicipler-pixel/REPO.git
```

The script runs the 1a check, runs Lean if `LEAN_PROJECT` points at the step-1b project
(`LEAN_PROJECT=$PWD/ejcheck ./05-handoff/push.sh ...`), and then commits the **whole pack** and
pushes it to `main`.

**Gate:** `git ls-remote <URL> main` must return a SHA, and `git log -1 --format=%s` must show
`Review pack: census theorem and digit-exclusivity proofs (rev 7)`.

---

## 3. Deposit on Zenodo

**Do not run without Jeromie Beasley's explicit OK — a published Zenodo record cannot be deleted.**

Needs `ZENODO_TOKEN` in the environment. **Never write the token into a file in this pack.**

**Do a dry run on the sandbox first.** A published Zenodo record can't be deleted, only versioned.
The sandbox needs its own account and token (sandbox.zenodo.org):

```bash
export ZENODO=https://sandbox.zenodo.org     # dry run
# export ZENODO=https://zenodo.org           # the real deposit, only after the sandbox run succeeds
```

Bundle the pack once (the archive goes into the deposit next to the PDF):

```bash
zip -qr /tmp/ej-pack-rev7.zip . -x 'ejcheck/*' '.git/*'
```

Create the deposition:

```bash
curl -sS -H "Authorization: Bearer $ZENODO_TOKEN" -H "Content-Type: application/json" -d '{
 "metadata": {
  "title": "Machine-checked fragments of a base-10 prime pattern",
  "upload_type": "publication",
  "publication_type": "preprint",
  "creators": [{"name":"Johnson, Elizabeth"},{"name":"Beasley, Jeromie","orcid":"0009-0006-4645-5643"}],
  "description": "Residue-language census of the twin-gap sequence: admissible residue words of length n over {0,2,4,6,8} number 3^(n+1)-2^(n+1), and every word realised from a twin start above 5 is admissible (the converse is not claimed). Also: digit exclusivity for twin pairs, junction uniqueness, the equilibrium obstruction, the exact range of the coprimality test, and the base-10 colour wheel in intrinsic coordinates Z/10 = Z/2 x Z/5, on which twin primes avoid the neutral hue, and its refinement across scales 10^k. The census, the obstruction theorems and the wheel identities at W=10 are formalised in Lean 4 with Mathlib. LEAN_SENTENCE Built on the framework of Elizabeth Johnson (DOI 10.5281/zenodo.23378596); the framework is hers alone and the new results are joint.",
  "license": "cc-by-4.0",
  "keywords": ["prime gaps","twin primes","Lean 4","formalisation","modular arithmetic"],
  "related_identifiers": [
   {"identifier":"10.5281/zenodo.23378596","relation":"isSupplementTo","scheme":"doi"}
  ]
 }}' "$ZENODO/api/deposit/depositions"
```

Before sending, replace `LEAN_SENTENCE` with exactly one of these:

* if gate 1b passed: `The Lean files compile with no sorry; axiom footprints are in the archive.`
* if 1b was not run: `The Lean build was not re-verified for this deposit.`

If the response is a 400 that complains about `upload_type`, resend with
`"upload_type":"publication","publication_type":"preprint"` replaced by
`"resource_type":{"title":"Preprint","type":"publication","subtype":"preprint"}`.

The response contains `id` and `links.bucket`. Upload the two files, then publish:

```bash
ID=<id from the response>
BUCKET=<links.bucket from the response>
curl -sS -H "Authorization: Bearer $ZENODO_TOKEN" --upload-file 01-report/report.pdf "$BUCKET/report.pdf"
curl -sS -H "Authorization: Bearer $ZENODO_TOKEN" --upload-file /tmp/ej-pack-rev7.zip "$BUCKET/ej-pack-rev7.zip"
curl -sS -X POST -H "Authorization: Bearer $ZENODO_TOKEN" "$ZENODO/api/deposit/depositions/$ID/actions/publish"
```

**Gates:** each upload must return a JSON body with a `checksum`, and the publish response must
contain a `doi`. Record the DOI.

**Caveat.** These calls follow the documented API (<https://developers.zenodo.org>). They were
**not** run during preparation because there was no token. Check every response code; don't
assume success.

---

## 4. Cross-link

1. Add the Zenodo DOI to `README.md` in the repository, then commit and push:
   `git commit -am "add deposit DOI" && git push`. Editing `README.md` after the freeze is expected;
   leave every other file unchanged.
2. If the repository is public, add its URL to the deposit's `related_identifiers` with
   `PUT $ZENODO/api/deposit/depositions/$ID`. If it is private, skip this: a private URL must not be
   published.

---

## 5. Report back

Return exactly these:

* the 1a result (the last line of `check_pack.py`);
* the 1b result, with the axiom lines verbatim, or "not verified" and the reason;
* the repository URL and the pushed commit SHA;
* the sandbox DOI, then the real DOI, or the failing response body;
* any gate that was skipped, and why.

---

## Prohibited

* **Do not** say or imply that every admissible word occurs among the primes. That is a
  prime-tuples statement; it is observed for n ≤ 5, not proved.
* **Do not** say "no prime above 7 ends in 7" or "no prime above 3 ends in 3". Digit exclusivity
  is about twin pairs only.
* **Do not** say or imply that the pattern decides primality in general. It refutes always and
  confirms only for `1 < n < p_{k+1}^2`. First failure: `49 = 7^2`.
* **Do not** say or imply a result about the sieve of Eratosthenes. The automorphism group of `Z/W`
  fixes the gap sequence identically; the method gives no gap information.
* **Do not** describe the colour section as a colorimetric or physical claim.
* **Do not** quote any cell count as a constant; the counts drift with `x`.
* **Do not** reuse the withdrawn claims: closure on `S`; `R+B=0` in `Z/9`; the counterflow balance as
  universal (it is 1.010 %, and suppressed); Conjecture 6 as stated; the "0.53 conservation"; the
  period-4–6 wave. See `03-docs/CORRECTIONS.md`.
* **Do not** call the Lean files "proved" in any description unless gate 1b passed in this run.
* **Do not** relicense her framework. It is cited, not relicensed.
