"""Build the museintelligence-library content from the blog scrape.

Reads the WordPress scrape (default: the sibling
``museintelligence-app`` repo's ``docs/wordpress-posts.md``), writes
one markdown file per post under ``library/<year>/<month>/<post-id>-<slug>.md``
with YAML front-matter, and writes ``index.json`` at the repo root.

Re-run to rebuild from a fresh scrape. The script verifies the parse
(counts, index-vs-section match, unique output paths) before writing
anything, and prints a verification summary.

Usage::

    python3 tools/build_library.py [--scrape PATH] [--root DIR]

The scrape is a snapshot: posts published after the scrape date are
not included until the scrape is re-run.
"""

from __future__ import annotations

import argparse
import json
import re
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

from readingroom.scrape import RETRIEVAL_TIMESTAMP, parse_scrape

DEFAULT_SCRAPE = (
    Path(__file__).resolve().parent.parent.parent
    / "museintelligence-app"
    / "docs"
    / "wordpress-posts.md"
)


def sanitize_slug(slug):
    """Make a slug safe for a filename; the API slugs are already
    URL-safe, so this is mostly a guard."""
    slug = re.sub(r"[^A-Za-z0-9._-]+", "-", slug)
    slug = re.sub(r"-+", "-", slug)
    slug = slug.strip("-.")
    if not slug:
        slug = "untitled"
    return slug[:120].rstrip("-.")


def yaml_quote(value):
    """Quote a string as a YAML double-quoted scalar (JSON quoting
    is valid YAML for the characters used here)."""
    return json.dumps(value, ensure_ascii=False)


def build(scrape_path, root):
    """Build library/ and index.json under ``root`` from the scrape."""
    index, sections = parse_scrape(str(scrape_path))
    entries = []
    seen_paths = set()
    for entry, sec in zip(index, sections):
        slug = sanitize_slug(sec["slug"])
        year, month = sec["date"][:4], sec["date"][5:7]
        rel_path = f"library/{year}/{month}/{sec['post_id']}-{slug}.md"
        if rel_path in seen_paths:
            raise ValueError(f"duplicate output path: {rel_path}")
        seen_paths.add(rel_path)
        out_path = root / rel_path
        out_path.parent.mkdir(parents=True, exist_ok=True)
        front_matter = (
            "---\n"
            f"title: {yaml_quote(sec['section_title'])}\n"
            f"date: {sec['date']}\n"
            f"url: {yaml_quote(sec['url'])}\n"
            f"source_id: {sec['source_id']}\n"
            f"source_locator: {yaml_quote(sec['url'])}\n"
            f"retrieval_timestamp: {RETRIEVAL_TIMESTAMP}\n"
            "---\n"
        )
        with open(out_path, "w", encoding="utf-8") as handle:
            handle.write(front_matter)
            handle.write("\n")
            handle.write(sec["content"])
            handle.write("\n")
        entries.append(
            {
                "title": entry["title"],
                "date": entry["date"],
                "url": entry["url"],
                "source_id": entry["source_id"],
                "source_locator": entry["url"],
                "path": rel_path,
                "retrieval_timestamp": RETRIEVAL_TIMESTAMP,
            }
        )
    index_path = root / "index.json"
    with open(index_path, "w", encoding="utf-8") as handle:
        json.dump(entries, handle, indent=2, ensure_ascii=False)
        handle.write("\n")
    return entries


def main(argv=None):
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "--scrape",
        type=Path,
        default=DEFAULT_SCRAPE,
        help="path to the WordPress scrape markdown file",
    )
    parser.add_argument(
        "--root",
        type=Path,
        default=Path(__file__).resolve().parent.parent,
        help="library repo root (library/ and index.json go here)",
    )
    args = parser.parse_args(argv)
    if not args.scrape.exists():
        print(f"scrape not found: {args.scrape}", file=sys.stderr)
        return 1
    entries = build(args.scrape, args.root)
    years = sorted({e["date"][:4] for e in entries})
    months = sorted({e["date"][:7] for e in entries})
    print(f"scrape: {args.scrape}")
    print(f"posts written: {len(entries)}")
    print(f"index.json entries: {len(entries)}")
    print(f"years covered: {years[0]}-{years[-1]} ({len(years)} years, "
          f"{len(months)} year-months)")
    print(f"first: {entries[0]['date']} {entries[0]['source_id']}")
    print(f"last: {entries[-1]['date']} {entries[-1]['source_id']}")
    print(f"untitled: {sum(1 for e in entries if e['title'] == '(untitled)')}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
