#!/usr/bin/env python3
"""Convert a YouTube auto-caption .vtt into a clean, de-duplicated, timestamped
transcript that an analyst (human or LLM) can mine for nuggets.

Auto-captions repeat each line as a rolling window; we collapse that to one line
per phrase, each prefixed with [H:MM:SS | <seconds>] so a nugget can be turned
into a precise fragment link:  https://www.youtube.com/watch?v=<id>&t=<seconds>s

Usage:
  vtt_to_text.py path/to/file.en.vtt            # prints clean transcript
  vtt_to_text.py file.vtt --link VIDEOID         # also prints a fragment link per line
  vtt_to_text.py file.vtt --grep 'sleep|bed'     # only matching lines
"""
from __future__ import annotations
import argparse, html, re
from pathlib import Path

TS = re.compile(r"(\d{2}):(\d{2}):(\d{2})\.(\d{3})\s+-->\s+")
TAG = re.compile(r"<[^>]+>")
WORDTAG = re.compile(r"<\d{2}:\d{2}:\d{2}\.\d{3}>")
WS = re.compile(r"[ ​‎‏]")  # nbsp / zero-width / bidi marks


def detag(s: str) -> str:
    s = html.unescape(TAG.sub("", s))
    s = WS.sub(" ", s)
    return re.sub(r"\s+", " ", s).strip()


def to_seconds(h: str, m: str, s: str) -> int:
    return int(h) * 3600 + int(m) * 60 + int(s)


def clean(vtt_text: str) -> list[tuple[int, str]]:
    """YouTube auto-captions roll each phrase across two cues; the canonical
    de-dup is to keep only the 'live' line (the one carrying word-level <ts> tags)
    and use its cue start time. Falls back to plain de-dup for manual subs."""
    lines = vtt_text.splitlines()
    out: list[tuple[int, str]] = []
    last_text = ""
    cue_start = 0
    had_wordtags = False
    for ln in lines:
        m = TS.match(ln.strip())
        if m:
            cue_start = to_seconds(m.group(1), m.group(2), m.group(3))
            continue
        if WORDTAG.search(ln):
            had_wordtags = True
            text = detag(ln)
            if text and text != last_text:
                out.append((cue_start, text))
                last_text = text
    if had_wordtags:
        return out
    # manual subs (no word tags): de-dup plain cue text
    out, last_text, cue_start = [], "", 0
    pending: list[str] = []
    for ln in lines + ["@@END"]:
        m = TS.match(ln.strip())
        if m or ln == "@@END":
            text = detag(" ".join(pending))
            if text and text != last_text:
                out.append((cue_start, text))
                last_text = text
            pending = []
            if m:
                cue_start = to_seconds(m.group(1), m.group(2), m.group(3))
        elif ln.strip() and not ln.startswith(("WEBVTT", "Kind:", "Language:")):
            pending.append(ln)
    return out


def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument("vtt", type=Path)
    ap.add_argument("--link", help="video id; print a fragment link per line")
    ap.add_argument("--grep", help="only lines matching this regex (case-insensitive)")
    args = ap.parse_args()

    rows = clean(args.vtt.read_text(encoding="utf-8", errors="ignore"))
    pat = re.compile(args.grep, re.I) if args.grep else None
    for sec, text in rows:
        if pat and not pat.search(text):
            continue
        h, m, s = sec // 3600, (sec % 3600) // 60, sec % 60
        stamp = f"{h}:{m:02d}:{s:02d}"
        if args.link:
            print(f"[{stamp} | https://www.youtube.com/watch?v={args.link}&t={sec}s] {text}")
        else:
            print(f"[{stamp}] {text}")


if __name__ == "__main__":
    main()
