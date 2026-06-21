#!/usr/bin/env python3
"""Apply gradecheck-workflow.js results to the Neuro Toolkit graph.

For each method result it:
  - updates edge `evidence` grades, CONSERVATIVELY:
      * downgrades (literature is weaker than the current grade)  -> applied automatically
      * upgrades   (literature is stronger)                       -> only with --apply-upgrades,
                                                                     otherwise reported for review
  - writes the real citations into the protocol's `studies[]` field (pl uses finding_pl,
    en uses finding_en), replacing any previous studies so re-runs are idempotent.

Never invents data — only writes what the workflow returned. Run a build after.

Usage:
  apply_grades.py <workflow-output.json> [--apply-upgrades] [--dry-run]
"""
from __future__ import annotations
import argparse, json, pathlib

BASE = pathlib.Path(__file__).resolve().parents[4] / "src" / "content"
RANK = {"A": 4, "B": 3, "C": 2, "D": 1}


def load_results(path):
    d = json.load(open(path, encoding="utf-8"))
    if isinstance(d, list):
        return d
    r = d.get("result", d)
    if isinstance(r, str):
        r = json.loads(r)
    if isinstance(r, list):
        return r
    return r.get("results", [])


def clean_url(u):
    return (u or "").replace("&amp;", "&").strip() or None


def studies_for(raw, lang):
    out = []
    for s in raw or []:
        item = {"title": s.get("title"), "type": s.get("type", "other")}
        u = clean_url(s.get("url"))
        if u:
            item["url"] = u
        if s.get("year"):
            item["year"] = s["year"]
        finding = s.get(f"finding_{lang}") or s.get("finding_en") or s.get("finding_pl")
        if finding:
            item["finding"] = finding
        out.append(item)
    return out


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("output")
    ap.add_argument("--apply-upgrades", action="store_true", help="also raise grades when literature is stronger (ALL methods)")
    ap.add_argument("--upgrade-slugs", default="", help="comma-separated method slugs whose upgrades to accept (reviewed)")
    ap.add_argument("--dry-run", action="store_true")
    args = ap.parse_args()
    upgrade_ok = {s.strip() for s in args.upgrade_slugs.split(",") if s.strip()}

    report = []
    pending_upgrades = []
    for r in load_results(args.output):
        slug = r["slug"]
        rec = r["recommended_grade"]
        per = {p["target"]: p["grade"] for p in r.get("per_target", [])}
        changes = []
        for lang in ("pl", "en"):
            p = BASE / "protocols" / lang / f"{slug}.md"
            if not p.exists():
                continue
            _, fm_s, body = p.read_text(encoding="utf-8").split("---", 2)
            fm = json.loads(fm_s)
            for e in fm.get("addresses", []):
                new = per.get(e["target"], rec)
                old = e.get("evidence")
                if RANK.get(new, 0) < RANK.get(old, 0):
                    if lang == "pl":
                        changes.append(f"{e['target']}: {old}->{new}")
                    e["evidence"] = new
                elif RANK.get(new, 0) > RANK.get(old, 0):
                    accept = args.apply_upgrades or slug in upgrade_ok
                    if lang == "pl":
                        pending_upgrades.append(f"{slug}/{e['target']}: {old}->{new}" + ("  [APPLIED]" if accept else "  [held]"))
                    if accept:
                        e["evidence"] = new
            fm["studies"] = studies_for(r.get("studies"), lang)
            if not args.dry_run:
                p.write_text("---\n" + json.dumps(fm, ensure_ascii=False, indent=2) + "\n---" + body, encoding="utf-8")
        report.append((slug, rec, r.get("confidence"), r.get("no_direct_evidence"),
                       len(r.get("studies") or []), changes))

    print(f"{'DRY-RUN ' if args.dry_run else ''}applied {len(report)} methods\n")
    for slug, rec, conf, noev, nstud, changes in report:
        flags = []
        if noev:
            flags.append("NO-DIRECT-EVIDENCE")
        tag = (" [" + ", ".join(flags) + "]") if flags else ""
        ch = ("  downgrades: " + "; ".join(changes)) if changes else ""
        print(f"  {slug}: grade={rec} conf={conf} studies={nstud}{tag}{ch}")
    if pending_upgrades:
        print("\nUPGRADES suggested by literature (NOT applied — review, then --apply-upgrades):")
        for u in pending_upgrades:
            print("  " + u)


if __name__ == "__main__":
    main()
