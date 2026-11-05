#!/usr/bin/env python3
"""Gate 1a: every file matches manifest.json, and no withdrawn false statement survives.

Run from anywhere:  python3 05-handoff/check_pack.py
Last line is PACK OK on success; exit code 1 otherwise.
"""
import hashlib, json, pathlib, sys

root = pathlib.Path(__file__).resolve().parent.parent
m = json.loads((root / "05-handoff" / "manifest.json").read_text())
bad = 0

listed = set()
for f in m["files"]:
    p = root / f["path"]
    listed.add(f["path"])
    if not p.is_file():
        print("MISSING ", f["path"]); bad += 1; continue
    h = hashlib.sha256(p.read_bytes()).hexdigest()
    if h != f["sha256"]:
        print("MISMATCH", f["path"], "expected", f["sha256"][:12], "actual", h[:12]); bad += 1
print(f"checked {len(m['files'])} files against revision {m['revision']}")

# files present but not listed in the manifest
skip = {"05-handoff/manifest.json", ".gitignore"}
for p in sorted(root.rglob("*")):
    rel = p.relative_to(root).as_posix()
    if p.is_file() and rel not in listed and rel not in skip and not rel.startswith((".git/", "ejcheck/", "results/")) and "__pycache__" not in rel:
        print("UNLISTED", rel); bad += 1

for rel in m["scan_for_forbidden"]:
    for p in sorted(root.glob(rel)):
        text = p.read_text(errors="replace").lower()
        for phrase in m["forbidden_phrases"]:
            if phrase.lower() in text:
                print("FORBIDDEN", repr(phrase), "in", p.relative_to(root).as_posix()); bad += 1

print("PACK OK" if not bad else f"PACK FAILED: {bad} problem(s)")
sys.exit(1 if bad else 0)
