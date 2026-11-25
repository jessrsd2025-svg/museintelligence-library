"""Parse the WordPress scrape file (docs/wordpress-posts.md).

The scrape has three parts: a header, an index table (577 rows), and
577 post sections, followed by an appendix ("## Notes on 40-hex
strings in quoted content" plus a linter note) which is not post
content.

A post section starts with a heading ``## <n>. <title>`` followed by
a metadata block::

    - **Post ID:** <id>
    - **Date:** <date>
    - **URL:** <url>
    - **Slug:** <slug>
    - **source_id:** SRC-WP-<id>

Post content may itself contain ``## <n>. ...`` headings, so a heading
is only a section start when the metadata block follows it. Sections
are separated by a bare ``---`` line, which is not post content.
"""

from __future__ import annotations

import re

RETRIEVAL_TIMESTAMP = "2026-11-25T18:01:10Z"

_META_RE = re.compile(r"^- \*\*([A-Za-z_ ]+):\*\* (.*)$")
_HEADING_RE = re.compile(r"^## (\d+)\. (.*)$")
_SOURCE_ID_RE = re.compile(r"^SRC-WP-(\d+)$")
_APPENDIX_HEADING = "## Notes on 40-hex strings in quoted content"
_META_KEYS = ["Post ID", "Date", "URL", "Slug", "source_id"]


def split_table_row(line):
    """Split a markdown table row on unescaped pipes.

    ``\\|`` inside a cell is an escaped pipe and stays part of the
    cell; the leading and trailing empty cells of a ``| ... |`` row
    are dropped.
    """
    parts = []
    current = []
    i = 0
    while i < len(line):
        ch = line[i]
        if ch == "\\" and i + 1 < len(line) and line[i + 1] == "|":
            current.append("|")
            i += 2
            continue
        if ch == "|":
            parts.append("".join(current))
            current = []
            i += 1
            continue
        current.append(ch)
        i += 1
    parts.append("".join(current))
    cells = [p.strip() for p in parts]
    if cells and cells[0] == "":
        cells = cells[1:]
    if cells and cells[-1] == "":
        cells = cells[:-1]
    return cells


def parse_index_table(text):
    """Parse the scrape's index table into a list of entries.

    Each entry is a dict with keys: n (int), title, date, url,
    source_id. The table sits between the ``## Index`` and
    ``## Posts`` headings. Entries keep the table's order (newest
    first).
    """
    lines = text.splitlines()
    start = None
    end = None
    for i, line in enumerate(lines):
        if line == "## Index":
            start = i
        elif line == "## Posts" and start is not None:
            end = i
            break
    if start is None or end is None:
        raise ValueError("index table boundaries (## Index / ## Posts) not found")
    entries = []
    for line in lines[start + 1:end]:
        if not line.startswith("|"):
            continue
        cells = split_table_row(line)
        if len(cells) != 5:
            continue
        if cells[0] == "#" or set(cells[1]) <= {"-", " "}:
            continue
        try:
            n = int(cells[0])
        except ValueError:
            continue
        match = _SOURCE_ID_RE.match(cells[4])
        if not match:
            raise ValueError(f"bad source_id in index row {n}: {cells[4]!r}")
        entries.append(
            {
                "n": n,
                "title": cells[1],
                "date": cells[2],
                "url": cells[3],
                "source_id": cells[4],
            }
        )
    entries.sort(key=lambda e: e["n"])
    if [e["n"] for e in entries] != list(range(1, len(entries) + 1)):
        raise ValueError("index rows are not numbered 1..N in order")
    return entries


def _read_metadata(lines, i):
    """Read the 5-line metadata block after a section heading.

    ``i`` is the heading's line index. Returns (meta_dict, content
    start index) or None when the block is not a post section.
    """
    j = i + 1
    while j < len(lines) and lines[j].strip() == "":
        j += 1
    meta = {}
    for k in range(5):
        if j + k >= len(lines):
            return None
        match = _META_RE.match(lines[j + k])
        if not match:
            return None
        meta[match.group(1)] = match.group(2).strip()
    if list(meta.keys()) != _META_KEYS:
        return None
    try:
        post_id = int(meta["Post ID"])
    except ValueError:
        return None
    if meta["source_id"] != f"SRC-WP-{post_id}":
        return None
    meta["post_id"] = post_id
    return meta, j + 5


def parse_sections(text):
    """Parse the scrape's post sections into a list of dicts.

    Each dict has keys: n, section_title, post_id, date, url, slug,
    source_id, content. Content is the post body with leading and
    trailing blank lines removed and the section-separator ``---``
    removed; it is otherwise reproduced exactly as scraped.
    """
    lines = text.splitlines()
    starts = []
    for i, line in enumerate(lines):
        match = _HEADING_RE.match(line)
        if not match:
            continue
        parsed = _read_metadata(lines, i)
        if parsed is None:
            continue
        meta, content_start = parsed
        starts.append(
            {
                "n": int(match.group(1)),
                "section_title": match.group(2).strip(),
                "post_id": meta["post_id"],
                "date": meta["Date"],
                "url": meta["URL"],
                "slug": meta["Slug"],
                "source_id": meta["source_id"],
                "heading_line": i,
                "content_start": content_start,
            }
        )
    starts.sort(key=lambda s: s["n"])
    if [s["n"] for s in starts] != list(range(1, len(starts) + 1)):
        raise ValueError("post sections are not numbered 1..N in order")
    sections = []
    for pos, sec in enumerate(starts):
        if pos + 1 < len(starts):
            # Content ends at the next section's heading line.
            end = starts[pos + 1]["heading_line"]
        else:
            # Last section: content ends at the appendix heading, if
            # present, else at end of file.
            end = len(lines)
            for k in range(sec["content_start"], len(lines)):
                if lines[k] == _APPENDIX_HEADING:
                    end = k
                    break
        body = lines[sec["content_start"]:end]
        # Strip leading blank lines.
        while body and body[0].strip() == "":
            body = body[1:]
        # Strip trailing blank lines and the section separator.
        while body and body[-1].strip() == "":
            body = body[:-1]
        if body and body[-1].strip() == "---":
            body = body[:-1]
            while body and body[-1].strip() == "":
                body = body[:-1]
        sec = dict(sec)
        del sec["content_start"]
        del sec["heading_line"]
        sec["content"] = "\n".join(body)
        sections.append(sec)
    return sections


def parse_scrape(path):
    """Parse a scrape file; return (index_entries, sections).

    Cross-checks that the index and the sections agree: same count,
    same numbering, and matching source_id, date, and URL per post.
    Raises ValueError on any mismatch.
    """
    with open(path, "r", encoding="utf-8") as handle:
        text = handle.read()
    index = parse_index_table(text)
    sections = parse_sections(text)
    if len(index) != len(sections):
        raise ValueError(
            f"index has {len(index)} rows but {len(sections)} sections"
        )
    for entry, sec in zip(index, sections):
        if entry["n"] != sec["n"]:
            raise ValueError(f"index row {entry['n']} vs section {sec['n']}")
        if entry["source_id"] != sec["source_id"]:
            raise ValueError(
                f"post {entry['n']}: index {entry['source_id']} vs "
                f"section {sec['source_id']}"
            )
        if entry["date"] != sec["date"]:
            raise ValueError(
                f"post {entry['n']}: index date {entry['date']} vs "
                f"section date {sec['date']}"
            )
        if entry["url"] != sec["url"]:
            raise ValueError(
                f"post {entry['n']}: index URL {entry['url']} vs "
                f"section URL {sec['url']}"
            )
        if not sec["content"]:
            raise ValueError(f"post {entry['n']} has empty content")
    return index, sections
