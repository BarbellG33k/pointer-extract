#!/usr/bin/env python3
"""Convert YouTube VTT captions to clean per-episode Markdown transcripts.

Reads episodes.tsv (playlist_index, video_id, title) and subs/*.vtt,
writes one .md per episode into transcripts/.
"""

import html
import re
import sys
from pathlib import Path

BASE = Path(__file__).resolve().parent.parent / "engineering-alpha"
SUBS_DIR = BASE / "subs"
OUT_DIR = BASE / "transcripts"
EPISODES_TSV = BASE / "episodes.tsv"

SENTENCES_PER_PARAGRAPH = 5

TAG_RE = re.compile(r"<[^>]+>")
TS_LINE_RE = re.compile(
    r"^\s*\d{2}:\d{2}:\d{2}\.\d{3}\s*-->\s*\d{2}:\d{2}:\d{2}\.\d{3}"
)


def parse_vtt(path: Path) -> list[str]:
    """Return cue text lines from a VTT file, tags stripped."""
    lines_out = []
    for raw in path.read_text(encoding="utf-8").splitlines():
        line = raw.strip()
        if not line:
            continue
        if line.startswith(("WEBVTT", "Kind:", "Language:", "NOTE")):
            continue
        if TS_LINE_RE.match(line):
            continue
        # drop standalone cue identifiers (digits or ids without spaces)
        if re.fullmatch(r"[\w-]+", line) and ">" not in line and " " not in line:
            # could be a cue id; caption words are usually not this shape,
            # but keep short lowercase words like "a" or "i"
            if not re.fullmatch(r"[a-z]", line):
                continue
        text = html.unescape(TAG_RE.sub("", line))
        # "&gt;&gt;" is a speaker-change marker in YouTube auto captions
        text = re.sub(r"\s*>>\s*", " ", text)
        text = re.sub(r"\s+", " ", text).strip()
        if text:
            lines_out.append(text)
    return lines_out


def dedupe_rolling(lines: list[str]) -> list[str]:
    """Remove overlap duplication from rolling auto-generated captions."""
    out: list[str] = []
    for line in lines:
        if out and line == out[-1]:
            continue
        if out and line.startswith(out[-1]):
            # line extends previous line (rolling window): keep only the tail
            tail = line[len(out[-1]):].strip()
            if tail:
                out.append(tail)
            continue
        if out and out[-1].startswith(line):
            continue
        out.append(line)
    # second pass: fix word-level overlap at joins ("word word")
    fixed: list[str] = []
    for line in out:
        if fixed:
            prev_words = fixed[-1].split()
            words = line.split()
            max_k = min(6, len(prev_words), len(words))
            for k in range(max_k, 0, -1):
                if prev_words[-k:] == words[:k]:
                    words = words[k:]
                    break
            line = " ".join(words)
        if line:
            fixed.append(line)
    return fixed


def to_paragraphs(text: str) -> str:
    """Group sentences into paragraphs of SENTENCES_PER_PARAGRAPH."""
    sentences = re.split(r"(?<=[.!?])\s+", text)
    paras = []
    for i in range(0, len(sentences), SENTENCES_PER_PARAGRAPH):
        chunk = " ".join(sentences[i : i + SENTENCES_PER_PARAGRAPH]).strip()
        if chunk:
            paras.append(chunk)
    return "\n\n".join(paras)


def safe_filename(title: str) -> str:
    name = title.replace(":", " -")
    name = re.sub(r'[<>:"/\\|?*\x00-\x1f]', "", name)
    name = re.sub(r"\s+", " ", name).strip(" .")
    return name + ".md"


def caption_source(sub_path: Path) -> str:
    if sub_path.name.endswith(".en-orig.vtt"):
        return "auto-generated (original)"
    return "auto-generated"


def main() -> int:
    OUT_DIR.mkdir(parents=True, exist_ok=True)
    written = 0
    missing = []
    for raw in EPISODES_TSV.read_text(encoding="utf-8").splitlines():
        if not raw.strip():
            continue
        parts = raw.split("\\t")
        if len(parts) != 3:
            parts = raw.split("\t")
        index, vid, title = parts[0].strip(), parts[1].strip(), parts[2].strip()

        sub = SUBS_DIR / f"{vid}.en.vtt"
        if not sub.exists():
            sub = SUBS_DIR / f"{vid}.en-orig.vtt"
        if not sub.exists():
            missing.append((index, vid, title))
            continue

        lines = dedupe_rolling(parse_vtt(sub))
        body = to_paragraphs(" ".join(lines))
        url = f"https://www.youtube.com/watch?v={vid}"
        doc = (
            f"# {title}\n\n"
            f"- **Playlist position:** {index}\n"
            f"- **URL:** {url}\n"
            f"- **Caption source:** {caption_source(sub)}\n\n"
            f"---\n\n{body}\n"
        )
        out_path = OUT_DIR / safe_filename(title)
        out_path.write_text(doc, encoding="utf-8")
        written += 1
        print(f"written\t{index}\t{out_path.name}")

    print(f"\nTOTAL written: {written}")
    if missing:
        print("MISSING captions:")
        for index, vid, title in missing:
            print(f"  {index}\t{vid}\t{title}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
