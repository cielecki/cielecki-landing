#!/usr/bin/env python3
"""Verify a gradecheck workflow output: for every study URL, resolve PubMed/PMC IDs
via NCBI eutils and confirm the citation's title roughly matches what the agent
returned. Flags hallucination-risk (ID not found, or title mismatch) and lists
non-NCBI URLs that need manual checking. Read-only — does not modify content."""
import json, sys, re, urllib.request, time
from difflib import SequenceMatcher

OUT = sys.argv[1]
d = json.load(open(OUT, encoding="utf-8"))
results = d.get("result", d)
if isinstance(results, dict):
    results = results.get("results", [])

def eutils(db, _id):
    url = f"https://eutils.ncbi.nlm.nih.gov/entrez/eutils/esummary.fcgi?db={db}&id={_id}&retmode=json"
    try:
        with urllib.request.urlopen(url, timeout=20) as r:
            j = json.load(r)
        return j["result"][str(_id)]
    except Exception as e:
        return None

def norm(s):
    return re.sub(r"[^a-z0-9 ]", "", (s or "").lower()).strip()

print(f"# Verifying {len(results)} methods\n")
for r in results:
    print(f"## {r['slug']}  (rec={r['recommended_grade']} conf={r.get('confidence')} no_direct={r.get('no_direct_evidence')})")
    for s in r.get("studies", []):
        u = s.get("url", "") or ""
        claimed = s.get("title", "")
        pm = re.search(r"pubmed\.ncbi\.nlm\.nih\.gov/(\d+)", u)
        pmc = re.search(r"PMC(\d+)", u)
        if pm:
            rec = eutils("pubmed", pm.group(1))
            if not rec:
                print(f"   ✗ NOT FOUND  pubmed {pm.group(1)} | claimed: {claimed[:60]}")
            else:
                sim = SequenceMatcher(None, norm(claimed), norm(rec.get("title"))).ratio()
                tag = "✓" if sim > 0.6 else "⚠ TITLE MISMATCH"
                print(f"   {tag} pubmed {pm.group(1)} sim={sim:.2f} | real: {rec.get('title','?')[:65]}")
            time.sleep(0.34)
        elif pmc:
            rec = eutils("pmc", pmc.group(1))
            if not rec:
                print(f"   ✗ NOT FOUND  PMC{pmc.group(1)} | claimed: {claimed[:60]}")
            else:
                sim = SequenceMatcher(None, norm(claimed), norm(rec.get("title"))).ratio()
                tag = "✓" if sim > 0.6 else "⚠ TITLE MISMATCH"
                print(f"   {tag} PMC{pmc.group(1)} sim={sim:.2f} | real: {rec.get('title','?')[:65]}")
            time.sleep(0.34)
        elif u:
            print(f"   ? MANUAL    {u[:75]} | {claimed[:45]}")
        else:
            print(f"   · (no url)  {claimed[:55]}")
    print()
