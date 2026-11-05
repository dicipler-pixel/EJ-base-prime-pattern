"""Build the HTML edition of the report from report.tex (pandoc + small pre/post fixes)."""
import math, re, subprocess, sys, pathlib

src, outdir = pathlib.Path(sys.argv[1]), pathlib.Path(sys.argv[2])
t = src.read_text()

# --- pre-processing -------------------------------------------------------------------------
t = t.replace(r"\qedhere", "")
t = re.sub(r"\\paragraph\{([^}]*)\}", r"\\textbf{\1}", t)
t = t.replace(r"\begin{equation}\label{eq:mod6}", r"\begin{equation}\tag{1}")
t = t.replace(r"\eqref{eq:mod6}", "(1)")
for key, num in (("IR", 1), ("LOS", 2), ("RS", 3)):
    t = t.replace(r"\cite{%s}" % key, "[%d]" % num)

# figures: \includegraphics[...]{\fig{X.pdf}} + \captionof{figure}{...}  ->  figure env, numbered
n = [0]
def figrep(m):
    n[0] += 1
    opts, name, cap = m.group(1) or "", m.group(2), m.group(3)
    width = "100%"
    w = re.search(r"width=([0-9.]*)\\textwidth", opts)
    if w and w.group(1):
        width = f"{float(w.group(1)) * 100:.0f}%"
    return ("\\begin{figure}\n\\includegraphics[width=%s]{figures/%s.svg}\n"
            "\\caption{Figure %d. %s}\n\\end{figure}" % (width.replace("%", "\\%"), name, n[0], cap))
t = re.sub(r"\\begin\{center\}\s*\\includegraphics(\[[^\]]*\])?\{\\fig\{([a-z0-9_]+)\.pdf\}\}\s*"
           r"\\captionof\{figure\}\{((?:[^{}]|\{[^{}]*\})*)\}\s*\\end\{center\}", figrep, t)

# the TikZ wheel -> placeholder paragraph
t = re.sub(r"\\begin\{tikzpicture\}.*?\\end\{tikzpicture\}", "WHEELSVGPLACEHOLDER", t, flags=re.S)

# bibliography -> numbered list
bib = re.search(r"\\begin\{thebibliography\}\{9\}(.*?)\\end\{thebibliography\}", t, re.S).group(1)
items = [i.strip() for i in re.split(r"\\bibitem\{[A-Za-z]+\}", bib) if i.strip()]
t = t.replace(re.search(r"\\begin\{thebibliography\}.*?\\end\{thebibliography\}", t, re.S).group(0),
              "\\section*{References}\n\\begin{enumerate}\n" + "\n".join("\\item " + i for i in items)
              + "\n\\end{enumerate}")

pre = outdir / "pre.tex"
pre.write_text(t)

# --- pandoc -----------------------------------------------------------------------------------
css = (outdir / "style.html")
subprocess.run(["pandoc", str(pre), "-f", "latex", "-t", "html5", "--mathml", "-s", "--number-sections",
                "--embed-resources", "--resource-path", str(outdir), "-H", str(css),
                "--metadata", "pagetitle=Base-10 Prime Pattern",
                "-o", str(outdir / "report.html")], check=True)
h = (outdir / "report.html").read_text()

# --- the wheel as inline SVG (same layout as the PDF: 1 top, 7 right, 9 bottom, 3 left) ----------
C, R1, R2 = 130, 92, 56
def P(r, a): return C + r * math.cos(math.radians(a)), C - r * math.sin(math.radians(a))
svg = [f'<svg class="wheel" viewBox="0 0 260 260" role="img" aria-label="The wheel: two rings of hues and the neutral axis">',
       f'<defs><marker id="wh-ah" viewBox="0 0 10 10" refX="8" refY="5" markerWidth="6" markerHeight="6" orient="auto-start-reverse"><path d="M0,0 L10,5 L0,10 z" class="wh-fill"/></marker></defs>',
       f'<circle cx="{C}" cy="{C}" r="{R1}" class="wh-ring"/><circle cx="{C}" cy="{C}" r="{R2}" class="wh-ring"/>']
for a, o, e in ((90, 1, 6), (0, 7, 2), (270, 9, 4), (180, 3, 8)):
    x, y = P(R1, a); svg.append(f'<circle cx="{x:.1f}" cy="{y:.1f}" r="13" class="wh-node"/><text x="{x:.1f}" y="{y:.1f}" class="wh-t">{o}</text>')
    x, y = P(R2, a); svg.append(f'<circle cx="{x:.1f}" cy="{y:.1f}" r="12" class="wh-node wh-dash"/><text x="{x:.1f}" y="{y:.1f}" class="wh-t">{e}</text>')
svg.append(f'<circle cx="{C}" cy="{C-14}" r="11" class="wh-node wh-grey"/><text x="{C}" y="{C-14}" class="wh-t">5</text>')
svg.append(f'<circle cx="{C}" cy="{C+16}" r="11" class="wh-node wh-base"/><text x="{C}" y="{C+16}" class="wh-t">0</text>')
(x0, y0), (x1, y1) = P(116, 75), P(116, 15)
svg.append(f'<path d="M{x0:.1f},{y0:.1f} A116,116 0 0 1 {x1:.1f},{y1:.1f}" class="wh-arrow" marker-end="url(#wh-ah)"/>')
tx, ty = P(128, 45); svg.append(f'<text x="{tx:.1f}" y="{ty:.1f}" class="wh-small">×7</text>')
svg.append("</svg>")
h = re.sub(r"<p>\s*WHEELSVGPLACEHOLDER\s*</p>|WHEELSVGPLACEHOLDER", "".join(svg), h)
assert "WHEELSVGPLACEHOLDER" not in h
(outdir / "report.html").write_text(h)
print("figures:", n[0], "bytes:", len(h))
