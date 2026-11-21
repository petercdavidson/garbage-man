"""Bake the original TI-BASIC source into the web port.

    python3 web/build.py

Reads web/template.html + the original .txt listing and writes docs/index.html,
which GitHub Pages serves.
"""
from pathlib import Path
here = Path(__file__).resolve().parent
repo = here.parent
src = (repo / "TI-BASIC Original" / "GARBAGE (plaintext TI-Basic).txt").read_text(encoding="utf-8")
assert "</script" not in src
html = (here / "template.html").read_text(encoding="utf-8").replace("__SOURCE__", src)
out = repo / "docs" / "index.html"
out.parent.mkdir(exist_ok=True)
out.write_text(html, encoding="utf-8")
(out.parent / ".nojekyll").touch()
print("wrote", out)
