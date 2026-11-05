> **SUPERSEDED — do not follow.** This runbook was written for a different machine (a project
> GitHub connector). Use `05-handoff/HANDOFF.md`.

# Runbook: pushing once a repository is connected

Two routes. **Route A needs the GitHub connector connected to this project**; without it, and without
credentials in the VM, nothing can be pushed. Route B is what to do if the connector is unavailable.

---

## Route A — GitHub connector (the only route that works from this VM)

The connector's repository is fixed by project settings, so first:

```
github_status
```

If it reports `github_not_connected`, stop: someone must connect the repository in project settings
first. Do not ask for a token or an SSH key; none is needed and none must be stored.

Once connected:

**1. Fetch the default branch**

```
github_fetch
```

Returns `refs/remotes/omm/<default-branch>`.

**2. Create the branch locally**

```bash
git checkout -b ej-census refs/remotes/omm/main
mkdir -p lean
cp results/lean/Census.lean   lean/Census.lean
cp results/lean/EJPrime.lean  lean/EJPrime.lean
cp results/lean/README.md     lean/README.md
git add lean/
git status --short
```

**3. Confirm both files still check before committing**

```bash
lean lean/Census.lean
lean lean/EJPrime.lean
```

Expect: `[1, 5, 19, 65, 211, 665]` then the axiom line for `census`; and three axiom lines for
`EJPrime` showing only `propext` and `Quot.sound`.

**4. Commit**

```bash
git commit -m "Census theorem and digit-exclusivity proofs, machine-checked

Residue-language census: admissible words number 3^(n+1) - 2^(n+1).
Digit exclusivity, junction uniqueness, equilibrium obstruction.
Framework by Elizabeth Johnson (DOI 10.5281/zenodo.23378596); new results joint."
git rev-parse HEAD
```

**5. Push**

```
github_push  branch="ej-census"  commit="<sha from step 4>"
```

**6. Open the pull request**

```
github_create_pull_request
  head="ej-census"
  base="main"
  title="Census theorem and digit-exclusivity proofs (machine-checked)"
  body="See lean/README.md for the split between Elizabeth Johnson's framework and the joint new results."
```

---

## Route B — if the connector cannot be connected

The VM has no git credentials. A shell `git push` will fail on authentication, and that is expected,
not a bug to work around. Two clean options:

1. **Push from the owner's account.** This pack lives on Jeromie Beasley's repository (`dicipler-pixel/EJ-base-prime-pattern`). Hand the three files to whoever has push access and they commit from their own machine.
2. **She invites you as a collaborator**, then connect the repository in project settings and use
   Route A.

Either way the files are unchanged; only who runs the push differs.

---

## If the target repository has a Lake project

The three Lean files are built as a Lake package in `07-lean-package/`. To include them in another `lake build`, add them to the library globs in `lakefile.toml`, e.g.

```toml
[[lean_lib]]
name = "leq"
globs = ["lean", "lean.EJCensus", "lean.EJPrime"]
```

Check with `lake build` afterwards and confirm the warning-free build before opening the pull request.

---

## What to say in the pull request

Three facts, in this order:

1. `lean Census.lean` and `lean EJPrime.lean` both exit 0;
2. the axiom footprints are `propext, Classical.choice, Quot.sound` and `propext, Quot.sound` — no
   `sorryAx`;
3. the README separates her framework (prior work, cited to her alone) from the joint new results.

That is what a reviewer checks first, and all three are already true.
