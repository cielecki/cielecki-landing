#!/usr/bin/env python3
"""Build the input for the grade-verification workflow (gradecheck-workflow.js).

Emits a JSON array of method items to literature-check, each:
  { slug, title, summary, body, conditions,
    targets: [ {target, kind, name, evidence} ],   # current A-D grade per edge
    sources: int }                                  # independent voices already attached

Target slugs are resolved to human names (symptom/mechanism titles) so the agent
can phrase real literature queries ("body doubling for task initiation in ADHD").

Usage:
  prep_grades.py <outfile.json> [--slugs a,b,c] [--cap N] [--lang pl]
  # no filter -> all methods; --slugs for a pilot; --cap to take the first N.
"""
from __future__ import annotations
import argparse, json, pathlib

BASE = pathlib.Path(__file__).resolve().parents[4] / "src" / "content"


def name_map(coll: str, lang: str) -> dict[str, str]:
    out: dict[str, str] = {}
    d = BASE / coll / lang
    if d.exists():
        for f in d.glob("*.md"):
            try:
                fm = json.loads(f.read_text(encoding="utf-8").split("---", 2)[1])
                out[f.stem] = fm.get("title", f.stem)
            except Exception:
                pass
    return out


def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument("outfile")
    ap.add_argument("--slugs", default="", help="comma-separated method slugs (pilot)")
    ap.add_argument("--cap", type=int, default=0, help="take only the first N methods")
    ap.add_argument("--lang", default="pl")
    args = ap.parse_args()

    only = {s.strip() for s in args.slugs.split(",") if s.strip()}
    sym = name_map("symptoms", args.lang)
    mech = name_map("mechanisms", args.lang)

    items = []
    for f in sorted((BASE / "protocols" / args.lang).glob("*.md")):
        if only and f.stem not in only:
            continue
        parts = f.read_text(encoding="utf-8").split("---", 2)
        try:
            fm = json.loads(parts[1])
        except Exception:
            continue
        body = parts[2].strip() if len(parts) > 2 else ""
        targets = []
        for e in fm.get("addresses", []):
            nm = (mech if e.get("kind") == "mechanism" else sym).get(e["target"], e["target"])
            targets.append({"target": e["target"], "kind": e["kind"], "name": nm, "evidence": e.get("evidence")})
        srcs = {(r.get("author") or r.get("title") or r.get("url") or "").strip().lower()
                for r in fm.get("resources", [])}
        srcs.discard("")
        items.append({
            "slug": f.stem,
            "title": fm.get("title"),
            "summary": fm.get("summary"),
            "body": body,
            "conditions": fm.get("conditions", []),
            "targets": targets,
            "sources": len(srcs),
        })

    if args.cap:
        items = items[: args.cap]
    pathlib.Path(args.outfile).write_text(json.dumps(items, ensure_ascii=False, indent=2), encoding="utf-8")
    print(f"wrote {len(items)} methods -> {args.outfile}")


if __name__ == "__main__":
    main()
