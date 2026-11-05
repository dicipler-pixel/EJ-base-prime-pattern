#!/usr/bin/env bash
# Push the whole pack to a repository (private or public - the URL decides).
#   usage: ./05-handoff/push.sh git@github.com:USERNAME/REPO.git [branch]
#   optional: LEAN_PROJECT=/path/to/lake/project-with-mathlib  -> also runs the Lean gate
set -euo pipefail
REPO_URL="${1:?usage: ./05-handoff/push.sh git@github.com:USERNAME/REPO.git [branch]}"
BRANCH="${2:-main}"
ROOT="$(cd "$(dirname "$0")/.." && pwd)"
cd "$ROOT"

NAME="${GIT_AUTHOR_NAME:-$(git config user.name || true)}"
EMAIL="${GIT_AUTHOR_EMAIL:-$(git config user.email || true)}"
if [ -z "$NAME" ] || [ -z "$EMAIL" ]; then
  echo "Set an identity first:"
  echo "  git config --global user.name 'Jeromie Beasley'"
  echo "  git config --global user.email 'you@example.com'"
  exit 1
fi

echo "== integrity and wording gate"
python3 05-handoff/check_pack.py        # exits non-zero on any mismatch -> push aborted

if [ -n "${LEAN_PROJECT:-}" ]; then
  echo "== Lean gate (project: $LEAN_PROJECT)"
  for f in 02-lean/Census.lean 02-lean/EJPrime.lean; do
    out="$(cd "$LEAN_PROJECT" && lake env lean "$ROOT/$f" 2>&1)" || { echo "$out"; echo "!! $f failed"; exit 1; }
    echo "$out"
    if echo "$out" | grep -q sorryAx; then echo "!! sorryAx in $f"; exit 1; fi
  done
else
  echo "!! LEAN_PROJECT not set - Lean gate skipped; record the build as NOT VERIFIED"
fi

[ -d .git ] || git init -q
cat > .gitignore <<'EOF'
ejcheck/
__pycache__/
results/
EOF
git add -A
git -c user.name="$NAME" -c user.email="$EMAIL" commit -q -m "Review pack: census theorem and digit-exclusivity proofs (rev 7)

Framework by Elizabeth Johnson (DOI 10.5281/zenodo.23378596); new results joint.
See 05-handoff/REVIEW.md for what is claimed and what is not." || echo "nothing new to commit"
git branch -M "$BRANCH"
git remote remove origin 2>/dev/null || true
git remote add origin "$REPO_URL"
# If the repository already has commits (for example a README made on GitHub), keep them in the
# history and merge the pack on top. Where a file exists on both sides, the pack's version is used;
# nothing is force-pushed and no existing commit is rewritten.
if git ls-remote --exit-code --heads origin "$BRANCH" >/dev/null 2>&1; then
  echo "== $BRANCH already exists on the remote: merging it in (pack files win on conflicts)"
  git fetch -q origin "$BRANCH"
  if ! git merge-base --is-ancestor "origin/$BRANCH" HEAD 2>/dev/null; then
    git -c user.name="$NAME" -c user.email="$EMAIL" merge -q --allow-unrelated-histories -X ours \
      -m "Merge existing repository content into the review pack" "origin/$BRANCH"
  fi
fi
git push -u origin "$BRANCH"
echo; echo "pushed to ${REPO_URL%.git} ($(git rev-parse HEAD))"
