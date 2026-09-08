#!/usr/bin/env python3
"""Embed the verified course dataset into a single self contained page."""
import json, sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
course = json.loads((ROOT / "data" / "course.json").read_text(encoding="utf-8"))
tpl = (ROOT / "src" / "index.template.html").read_text(encoding="utf-8")

# Every topic must carry pedagogical guidance in both languages, or the Arabic
# page is a shell of the English one.
faults = [t["id"] for d in course["domains"] for t in d["topics"]
          if not t.get("trapAr") or not t.get("titleAr")]
if faults:
    print("topics missing Arabic:", *faults, sep="\n  ", file=sys.stderr)
    sys.exit(1)

html = tpl.replace("/*__COURSE__*/null",
                   json.dumps(course, ensure_ascii=False, separators=(",", ":")))
if "__COURSE__" in html:
    print("payload placeholder not replaced", file=sys.stderr); sys.exit(1)

out = ROOT / "index.html"
out.write_text(html, encoding="utf-8")
c = course["counts"]
print(f"index.html {out.stat().st_size // 1024} KB, {c['topics']} topics, "
      f"{c['resources']} verified links")
