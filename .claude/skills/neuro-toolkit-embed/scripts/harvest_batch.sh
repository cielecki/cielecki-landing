#!/usr/bin/env bash
# Bulk-harvest timestamped transcripts for the Neuro Toolkit corpus.
# Free (yt-dlp only). Portable to macOS /bin/bash 3.2 (NO associative arrays).
# Dedicated channels harvested broadly; general channels title-filtered to on-topic.
# --no-overwrites makes re-runs skip transcripts already on disk.
export PATH="/opt/homebrew/bin:$PATH"
ROOT="/Users/maciel/Documents/Projects/personal/AuDHD/zrodla/transcripts"
CAP="${CAP:-150}"
TOPIC='(?i)(adhd|autis|audhd|dopamine|focus|executive|rsd|reject|meltdown|burnout|sensor|stimulant|neurodiver|procrastinat|emotional regulation)'

subs () {  # subs <outdir> <yt-dlp source args...>   (source = a URL or --batch-file FILE)
  out="$1"; shift
  mkdir -p "$out"
  yt-dlp --skip-download --ignore-errors --no-warnings --no-progress --no-overwrites \
    --write-subs --write-auto-subs --sub-langs "en.*" --sub-format vtt \
    --sleep-requests 1 --playlist-end "$CAP" \
    --download-archive "$out/.archive" \
    -o "$out/%(id)s__%(title).80B.%(ext)s" "$@"
}

echo "=== seed: hand-picked corpus videos ==="
subs "$ROOT/_corpus-seed" --batch-file /tmp/yt_urls.txt

# name|url|mode   (mode FILTER = on-topic title filter; empty = take all)
CHANNELS="
ADHDChatterPodcast|https://www.youtube.com/channel/UCCKrIhEGR5yoCBWsCkzGEaA/videos|
howtoadhd|https://www.youtube.com/@howtoadhd/videos|
YoSamdySam|https://www.youtube.com/@YoSamdySam/videos|
autismfromtheInside|https://www.youtube.com/@autismfromtheInside/videos|
RussellBarkley|https://www.youtube.com/channel/UC0tLWu7ljYVFPiZQfHjTMsA/videos|
ADDitudeMagazine|https://www.youtube.com/channel/UC_3d1NVczqxa-cQzFt2iVSw/videos|
EdwardHallowell|https://www.youtube.com/channel/UCUxHRVjLIEIS0eeQR6MXONA/videos|
UnconventionalOrganisation|https://www.youtube.com/channel/UCn5JGUn-oADCmPhaoN2_7Dg/videos|
ADHDWomensWellbeing|https://www.youtube.com/channel/UCJR2_itDkuWhDjreZtosV6Q/videos|
Auticate|https://www.youtube.com/channel/UCXQ7acR7O0RUI3NSZIVWbNA/videos|
HealthyGamerGG|https://www.youtube.com/channel/UClHVl2N3jPEbkNJVx-ItQIQ/videos|FILTER
TherapyInANutshell|https://www.youtube.com/channel/UCpuqYFKLkcEryEieomiAv3Q/videos|FILTER
AndrewHuberman|https://www.youtube.com/channel/UC2D2CMWXMOVWx7giW1n3LIg/videos|FILTER
DiaryOfACEO|https://www.youtube.com/channel/UCGq-a57w-aPwyi3pW7XLiHw/videos|FILTER
"

printf '%s\n' "$CHANNELS" | while IFS='|' read -r name url mode; do
  [ -z "$name" ] && continue
  echo "=== ${mode:-full}: $name ==="
  if [ "$mode" = "FILTER" ]; then
    subs "$ROOT/$name" "$url" --match-filter "title ~= '$TOPIC'"
  else
    subs "$ROOT/$name" "$url"
  fi
done

echo "=== DONE. transcript counts: ==="
for d in "$ROOT"/*/; do
  n=$(ls "$d" 2>/dev/null | grep -c '\.vtt$')
  printf "%6s  %s\n" "$n" "$(basename "$d")"
done
