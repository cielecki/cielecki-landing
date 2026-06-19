#!/usr/bin/env python3
"""Select + clean corpus transcripts for one symptom fill, into a /tmp work dir.

Picks transcripts whose TITLE matches a topic regex, cleans each to timestamped
text (vtt_to_text), caps the set (default 5 — keep runs SHORT to dodge 529 stalls),
and writes args.json for the extract-workflow.

Usage:
  prep_symptom.py <outdir> "<title-regex>" [--cap N]
Example:
  prep_symptom.py /tmp/nt_maskowanie "mask|unmask|authentic|pretend|fit in|camouflage|identity" --cap 5
"""
from __future__ import annotations
import argparse, json, re, subprocess, pathlib

ROOT = pathlib.Path.home() / "Documents/Projects/personal/AuDHD/zrodla/transcripts"
TOOL = str(pathlib.Path(__file__).with_name("vtt_to_text.py"))

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("outdir"); ap.add_argument("regex"); ap.add_argument("--cap", type=int, default=5)
    a = ap.parse_args()
    OUT = pathlib.Path(a.outdir); OUT.mkdir(parents=True, exist_ok=True)
    TOPIC = re.compile(a.regex, re.I)
    cands = {}
    for vtt in ROOT.glob("*/*.vtt"):
        m = re.match(r"^(.+?)__(.*)\.(en[\w-]*)\.vtt$", vtt.name)
        if not m: continue
        vid, title, lang = m.group(1), m.group(2), m.group(3)
        if not TOPIC.search(title): continue
        pref = 0 if lang == "en-orig" else (1 if lang == "en" else 2)
        if vid not in cands or pref < cands[vid]["pref"]:
            cands[vid] = {"id": vid, "title": title, "path": str(vtt), "pref": pref}
    manifest = []
    for vid, c in cands.items():
        r = subprocess.run(["/usr/bin/python3", TOOL, c["path"], f"--link={vid}"], capture_output=True, text=True)
        lines = r.stdout.strip()
        if lines.count("\n") < 15: continue
        (OUT / f"{vid}.txt").write_text(lines, encoding="utf-8")
        manifest.append({"id": vid, "title": c["title"], "path": str(OUT / f"{vid}.txt"),
                         "url": f"https://www.youtube.com/watch?v={vid}", "lines": lines.count(chr(10)) + 1})
    manifest.sort(key=lambda x: -x["lines"])
    manifest = manifest[:a.cap]
    args = [{k: v for k, v in m.items() if k != "lines"} for m in manifest]
    (OUT / "args.json").write_text(json.dumps(args, ensure_ascii=False), encoding="utf-8")
    print(f"prepared {len(manifest)} transcripts (cap {a.cap}) -> {OUT}/args.json")
    for m in manifest: print(f"  {m['lines']:5}  {m['title'][:72]}")

if __name__ == "__main__":
    main()
