#!/usr/bin/env python3
"""Apply an extraction-workflow result to the Neuro Toolkit graph.

Reads a workflow output JSON (the file named in the <task-notification>, shape
{summary,logs,result:{synth:{new_mechanisms,new_methods,enrichments}}}) and:
  - creates new mechanism / method .md files (pl+en) that don't already exist,
  - appends enrichment resources to existing method files (dedup by url).

Never clobbers an existing slug (so re-runs are safe); orders are auto-assigned
after the current max in each collection.

Usage:  apply_synth.py <workflow-output.json> [--symptom <slug>]
The --symptom is the default symptom a new mechanism hangs under if the synth
didn't set `symptoms` on it.
"""
from __future__ import annotations
import argparse, json, pathlib, sys

BASE = pathlib.Path(__file__).resolve().parents[4] / "src" / "content"

def load_result(path):
    d = json.load(open(path, encoding="utf-8"))
    r = d.get("result", d)
    if isinstance(r, str):
        r = json.loads(r)
    return r["synth"]

def next_order(coll):
    mx = 0
    d = BASE / coll / "pl"
    if d.exists():
        for f in d.glob("*.md"):
            try:
                fm = json.loads(f.read_text(encoding="utf-8").split("---", 2)[1])
                mx = max(mx, int(fm.get("order", 0)))
            except Exception:
                pass
    return mx + 1

def write(coll, lang, slug, fm, body):
    dd = BASE / coll / lang; dd.mkdir(parents=True, exist_ok=True)
    fm = dict(fm); fm["lang"] = lang
    (dd / f"{slug}.md").write_text("---\n" + json.dumps(fm, ensure_ascii=False, indent=2) + "\n---\n\n" + (body or "").strip() + "\n", encoding="utf-8")

def res_for(r, lang):
    out = {"title": r.get(f"title_{lang}") or r.get("title_pl") or r.get("title_en"), "type": r.get("type", "video")}
    if r.get("url"): out["url"] = r["url"].replace("&amp;", "&").strip()
    if r.get("author"): out["author"] = r["author"]
    note = r.get(f"note_{lang}") or r.get("note_pl") or r.get("note_en")
    if note: out["note"] = note
    return out

def edges_for(addresses, lang):
    out = []
    for e in addresses or []:
        a = {"target": e["target"], "kind": e["kind"], "evidence": e["evidence"], "community": e["community"]}
        note = e.get(f"note_{lang}") or e.get("note_pl") or e.get("note_en")
        if note: a["note"] = note
        out.append(a)
    return out

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("output")
    ap.add_argument("--symptom", default="sen")
    args = ap.parse_args()
    synth = load_result(args.output)
    created_m, created_p, enriched, skipped = [], [], [], []

    order = next_order("mechanisms")
    for m in synth.get("new_mechanisms", []):
        slug = m["slug"]
        if (BASE / "mechanisms" / "pl" / f"{slug}.md").exists():
            skipped.append(f"mechanism:{slug}"); continue
        for lang in ("pl", "en"):
            write("mechanisms", lang, slug, {
                "title": m[f"title_{lang}"], "summary": m[f"summary_{lang}"], "icon": "mdi:cog-outline",
                "order": order, "conditions": m.get("conditions") or ["adhd", "autism", "audhd"],
                "symptoms": m.get("symptoms") or [args.symptom]}, m[f"body_{lang}"])
        created_m.append(slug); order += 1

    order = next_order("protocols")
    for m in synth.get("new_methods", []):
        slug = m["slug"]
        if (BASE / "protocols" / "pl" / f"{slug}.md").exists():
            skipped.append(f"method:{slug}"); continue
        for lang in ("pl", "en"):
            write("protocols", lang, slug, {
                "title": m[f"title_{lang}"], "summary": m[f"summary_{lang}"], "icon": "mdi:tools",
                "order": order, "conditions": m.get("conditions") or ["adhd", "autism", "audhd"],
                "addresses": edges_for(m.get("addresses"), lang),
                "resources": [res_for(r, lang) for r in m.get("resources", [])]}, m[f"body_{lang}"])
        created_p.append(slug); order += 1

    for e in synth.get("enrichments", []):
        slug = e["method_slug"]; r = e["resource"]
        for lang in ("pl", "en"):
            p = BASE / "protocols" / lang / f"{slug}.md"
            if not p.exists(): continue
            _, fm_s, body = p.read_text(encoding="utf-8").split("---", 2)
            fm = json.loads(fm_s)
            urls = {x.get("url") for x in fm.get("resources", [])}
            res = res_for(r, lang)
            if res.get("url") and res["url"] in urls: continue
            fm.setdefault("resources", []).append(res)
            p.write_text("---\n" + json.dumps(fm, ensure_ascii=False, indent=2) + "\n---" + body, encoding="utf-8")
        enriched.append(slug)

    print("new mechanisms:", created_m)
    print("new methods:", created_p)
    print("enriched:", enriched)
    if skipped: print("skipped (already exist):", skipped)

if __name__ == "__main__":
    main()
