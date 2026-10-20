# Transcript Extraction Plan — Engineering Alpha in Private Equity

**Date:** 2026-10-20
**Source playlist:** https://youtube.com/playlist?list=PLfNwtl3QHiMQ
**Playlist title:** Engineering Alpha in Private Equity (podcast hosted by Dave Mangot & Paul Karner)
**Output location:** `podcasts/engineering-alpha/transcripts/`

## Goal

Extract the transcript of every episode in the playlist, one Markdown (`.md`)
file per episode.

## Findings (reconnaissance)

- The playlist is public and accessible.
- YouTube no longer returns episode lists in the initial page HTML; they load
  via internal API continuations, and direct API probes returned empty
  responses (anti-scraping). **yt-dlp** is the reliable tool for enumeration
  and caption download.
- yt-dlp can fetch subtitles (manual English preferred, auto-generated as
  fallback) without downloading any video or audio.

## Steps

1. **Install yt-dlp** via Homebrew (`brew install yt-dlp`).
2. **Enumerate episodes** in playlist order:
   `yt-dlp --flat-playlist -J <playlist-url>` → video IDs + titles.
3. **Fetch captions** per episode:
   `--skip-download --write-subs --write-auto-subs --sub-langs "en.*" --sub-format vtt`
   (falls back to auto-captions when no manual subs exist).
4. **Convert each VTT to a clean Markdown file** — strip timestamps, dedupe
   rolling auto-caption lines, join into paragraphs; add a small header with
   episode title, number, and URL.
   - Filenames: `NN - <episode title>.md`.
5. **Verify** — one file per episode, spot-check content against the YouTube
   transcript for a couple of episodes; report any episodes with no available
   captions.

## Contingencies

- Episodes with no English captions (manual or auto): create a stub `.md`
  noting that, and list them in the final report.
- Auto-caption fetches occasionally hit YouTube's "PO token" requirement;
  retry strategies exist (e.g. browser cookies via `--cookies-from-browser`)
  and will be flagged if needed.

## Results

Executed 2026-10-20 with yt-dlp 2026.08.19 (installed via Homebrew).

- Playlist contains **20 videos: 19 episodes + 1 trailer** — all extracted,
  none missing captions (English auto-generated for all).
- **20 Markdown transcripts** written to
  `podcasts/engineering-alpha/transcripts/` (~90k words total), named
  `Episode NN - <title>.md` in playlist order, each with a header
  (title, playlist position, URL, caption source).
- Post-processing: stripped VTT timestamps/tags, removed `>>`
  speaker-change markers, deduplicated rolling auto-caption overlap,
  grouped into paragraphs.
- Known limitations (inherent to YouTube auto-captions): occasional
  mis-transcriptions (e.g. host names rendered as "Carner"/"Mango"),
  `[music]`/`[laught` markers, and rare word repetitions present in the
  source captions. Left faithful to source.

### Intermediate artifacts

- `engineering-alpha/episodes.tsv` — playlist order, video IDs, titles
- `engineering-alpha/subs/` — raw VTT captions (`.en.vtt` + `.en-orig.vtt`)
- `engineering-alpha/*.log` — enumeration and download logs
- `../scripts/vtt_to_md.py` — re-runnable VTT → Markdown converter
