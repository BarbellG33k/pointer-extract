# Pointer.io Article Index

A self-contained, offline index of every article linked from the
[Pointer.io](https://pointer.io) engineering newsletter — one record per
article, with hierarchical categories, full-text search, filtering, sorting,
and CSV export. Everything renders from a single generated HTML file
(`pointer-extract.html`) with no server and no runtime dependencies.

![Intent](#) *Open `pointer-extract.html` in any browser. That's the whole app.*

## Intent

Pointer.io arrives as an email digest several times a week, and its links are
effectively lost once read. This repo preserves them as a queryable archive:

- **One JSON data file per month** (`YYYY-MM.json`), holding one record per
  article link that appeared in that month's issues.
- **One generated HTML page** (`pointer-extract.html`) that embeds all records
  and provides: search across title/summary/author/category/URL/issue/date,
  hierarchical category filtering (top level → subcategory → sub-subcategory,
  e.g. `Leadership › Management › AI`), sponsored/editorial filtering, issue
  and month filters, column sorting, and CSV export of the current view.

## Repository layout

```
2025-01.json … 2026-10.json   Data: one file per month (see schema below)
pointer-extract.html          Generated output — open in a browser
_build/
  build.py                    Generates pointer-extract.html from data + template
  template.html               Current UI template (styled, "reading ledger" theme)
  template-plain.html         Previous plain template — kept for easy revert
  check.js                    Script portion with data inlined, for `node --check`
```

`.amp/` is local agent scratch space and is not part of the project.

## Data schema

Each record in `YYYY-MM.json`:

| Field | Type | Notes |
|---|---|---|
| `url` | string | Article URL, tracking parameters (`utm_*`, `aid`, etc.) removed |
| `title` | string | Article title |
| `issue` | number | Pointer.io issue number (e.g. `761`) |
| `date` | string | ISO `YYYY-MM-DD` — the issue's send date |
| `date_display` | string | Human format, e.g. `20 October 2026` |
| `category` | string | Space-separated category tokens, e.g. `Leadership Management AI` |
| `categories` | string[] | The same tokens as an ordered array: `[level-0, level-1, …]`. Position encodes hierarchy depth |
| `author` | string \| null | Article author; `null` when unknown (common for sponsored links) |
| `summary` | string | First ~300 characters of the article/description, trimmed at a word boundary |
| `sponsored` | boolean | `true` for paid/sponsored placements |
| `source_thread_id` | string | Gmail thread id of the newsletter email the link came from |

Category conventions:

- `categories` is split on spaces from `category`; keep original casing
  (CamelCase compounds like `ThoughtPiece`, `CareerGrowth`).
- Spellings are canonicalized — one concept, one token. The canonical list
  lives implicitly in the data; before adding a new token, check whether a
  near-duplicate already exists (`Thoughtpiece` vs `ThoughtPiece`,
  `Events` vs `Event`, `Mangement` vs `Management` have all been merged).
- `Tools+Setup` and `Staff+` are single tokens (the `+` is part of the name).

Files are pretty-printed JSON (`indent=1`, UTF-8, trailing newline); record
order within a file does not matter — the build sorts by `(date, issue)`.

## Where the data comes from

The extracts are produced by Claude reading your Gmail directly, so they
require email access:

- **Claude Desktop** — this is how the original months were created. Enable
  the Gmail connector (Settings → Connectors, or the workspace equivalent) so
  Claude can search and read mail.
- **Claude Code CLI** — works the same way once Claude Code has Gmail access,
  e.g. via a Gmail MCP server configured in `~/.claude.json` or
  `.mcp.json` (`claude mcp add …`). Any connector that can search and read
  the mailbox is sufficient.

The mail lives under the label **`Newsletters/Technical/Pointer.io`**. One
email (thread) per issue; each issue contains one link per article.

## Updating the data

One file per calendar month. When a month is over it is frozen; while a month
is in progress, re-running the extraction for that month should **replace**
the month's file with the fuller version (e.g. run in November and replace
`2026-10.json` in its entirety rather than appending).

### Standard prompt

Run this in Claude Desktop (with the Gmail connector enabled) or Claude Code
(with Gmail access), from inside this repository directory. Replace `October
2026` / `2026-10` with the month you are updating.

```text
Update the Pointer.io article extract for October 2026 in this repository.

1. Using Gmail, find every email under the label
   "Newsletters/Technical/Pointer.io" with a send date in October 2026.
2. From each email, extract one record per article link (deduplicate links
   that appear in multiple issues; keep the most recent occurrence).
   Skip images, unsubscribe links, and pointer.io's own housekeeping links.
3. For each article produce a JSON object with exactly these fields:
   - "url": the article URL with all tracking parameters removed
     (utm_*, aid, and similar query parameters; keep the rest of the URL as-is)
   - "title": the article's title in title case
   - "issue": the Pointer.io issue number as a number
   - "date": the issue send date as YYYY-MM-DD
   - "date_display": the send date as e.g. "20 October 2026"
   - "category": space-separated category tokens, e.g. "Leadership Management AI"
   - "categories": the same tokens as an array, first token = top level,
     each following token a sublevel of the previous one
   - "author": the article author, or null if not stated
   - "summary": the first ~300 characters of the article's description or
     opening text, trimmed at a word boundary
   - "sponsored": true for paid/sponsored placements, otherwise false
   - "source_thread_id": the Gmail thread id of the newsletter email
4. Choose categories from the tokens already used in the existing
   YYYY-MM.json files in this repository (read a few to get the vocabulary).
   One concept, one spelling: match the existing CamelCase forms exactly
   (e.g. "ThoughtPiece", "CareerGrowth", "Tools+Setup", "Staff+"). If a
   genuinely new concept is needed, invent one token in the same CamelCase
   style rather than respelling an existing one.
5. Replace the file "2026-10.json" in the repository root with the complete
   result: a JSON array of all records for the month, pretty-printed with
   1-space indent, UTF-8, sorted by (date, issue), including the records
   already present. Do not drop existing records unless their articles no
   longer match the criteria above.
6. After writing the file, report how many records the month now has and
   which issues it covers.
```

For a brand-new month the same prompt works — there will be no existing file
to merge with.

## Building / updating the HTML

Requires only Python 3 (standard library). From the repository root:

```sh
# Rebuild pointer-extract.html from all YYYY-MM.json files + _build/template.html
python3 _build/build.py

# Build using the previous plain template instead
python3 _build/build.py template-plain.html

# Syntax-check the generated script (optional; needs Node)
node --check _build/check.js
```

Note that `check.js` is a snapshot of the template script with data inlined;
regenerate it from the template after template or data changes if you rely on
it.

Full update flow, month to month:

```sh
# 1. Update the month's data via the prompt above (writes/replace YYYY-MM.json)
# 2. Rebuild the page
python3 _build/build.py
# 3. Open pointer-extract.html in a browser
```
