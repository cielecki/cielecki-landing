#!/usr/bin/env python3
"""Bulk-harvest timestamped YouTube transcripts for the Neuro Toolkit knowledge base.

Pulls, for a whole channel (or a --limit slice):
  - a manifest.json of videos (id, title, url, duration, upload_date)
  - English subtitles as timestamped .vtt (manual subs preferred, auto-subs fallback)

Free — uses yt-dlp only, no paid API. Resumable: yt-dlp's download-archive skips
videos already fetched, so re-running only grabs new uploads.

Usage:
  harvest_channel.py @howtoadhd [--limit N] [--out DIR]
  harvest_channel.py https://www.youtube.com/@autismfromtheInside [--limit 5]
"""
from __future__ import annotations
import argparse, json, subprocess, sys, re
from pathlib import Path

DEFAULT_OUT = Path.home() / "Documents/Projects/personal/AuDHD/zrodla/transcripts"


def handle_of(channel: str) -> str:
    m = re.search(r"@([A-Za-z0-9_.-]+)", channel)
    if m:
        return m.group(1)
    return re.sub(r"[^A-Za-z0-9_.-]", "_", channel.strip("/").split("/")[-1])


def channel_url(channel: str) -> str:
    if channel.startswith("http"):
        base = channel.rstrip("/")
    else:
        base = f"https://www.youtube.com/@{channel.lstrip('@')}"
    if not base.endswith(("/videos", "/streams", "/shorts")):
        base += "/videos"
    return base


def run(cmd: list[str]) -> subprocess.CompletedProcess:
    return subprocess.run(cmd, capture_output=True, text=True)


def build_manifest(url: str, limit: int | None) -> list[dict]:
    cmd = ["yt-dlp", "--flat-playlist", "--ignore-errors",
           "--print", "%(id)s\t%(title)s\t%(duration)s"]
    if limit:
        cmd += ["--playlist-end", str(limit)]
    cmd.append(url)
    cp = run(cmd)
    rows = []
    for line in cp.stdout.splitlines():
        parts = line.split("\t")
        if len(parts) < 2 or not parts[0]:
            continue
        vid = parts[0]
        rows.append({
            "id": vid,
            "title": parts[1],
            "duration": parts[2] if len(parts) > 2 else None,
            "url": f"https://www.youtube.com/watch?v={vid}",
        })
    if cp.returncode != 0 and not rows:
        sys.stderr.write(cp.stderr[-800:])
    return rows


def fetch_subs(url: str, outdir: Path, limit: int | None) -> None:
    cmd = [
        "yt-dlp", "--skip-download", "--ignore-errors",
        "--write-subs", "--write-auto-subs",
        "--sub-langs", "en.*", "--sub-format", "vtt",
        "--sleep-requests", "1",
        "--download-archive", str(outdir / ".archive"),
        "-o", str(outdir / "%(id)s__%(title).80B.%(ext)s"),
    ]
    if limit:
        cmd += ["--playlist-end", str(limit)]
    cmd.append(url)
    # stream progress to stderr so a long run shows life
    subprocess.run(cmd)


def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument("channel")
    ap.add_argument("--limit", type=int, default=None)
    ap.add_argument("--out", type=Path, default=None)
    ap.add_argument("--manifest-only", action="store_true")
    args = ap.parse_args()

    handle = handle_of(args.channel)
    url = channel_url(args.channel)
    outdir = (args.out or DEFAULT_OUT) / handle
    outdir.mkdir(parents=True, exist_ok=True)

    print(f"▶ {handle}  ({url})\n  → {outdir}")
    manifest = build_manifest(url, args.limit)
    (outdir / "manifest.json").write_text(
        json.dumps({"handle": handle, "url": url, "count": len(manifest), "videos": manifest},
                   ensure_ascii=False, indent=2), encoding="utf-8")
    print(f"  manifest: {len(manifest)} videos")

    if not args.manifest_only:
        fetch_subs(url, outdir, args.limit)
        vtts = list(outdir.glob("*.vtt"))
        print(f"  transcripts on disk: {len(vtts)} .vtt files")


if __name__ == "__main__":
    main()
