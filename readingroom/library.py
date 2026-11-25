"""Reading-room library: load, search, and check the 577-post corpus.

The library is the full public scrape of "jessrsd's Blog" (577
published posts, 2023-12-22 to 2026-11-25), one markdown file per
post under ``library/<year>/<month>/<post-id>-<slug>.md``, indexed
by ``index.json`` at the repo root. Every entry carries provenance:
``source_id``, ``source_locator`` (the post URL), and
``retrieval_timestamp``.

Standard library only. No network access; everything is local.
"""

from __future__ import annotations

import json
import os
from pathlib import Path

__all__ = [
    "find_index",
    "load_index",
    "search",
    "load_post",
    "provenance_check",
    "parse_front_matter",
]

INDEX_KEYS = ("title", "date", "url", "source_id", "source_locator", "path", "retrieval_timestamp")
FRONT_MATTER_KEYS = ("title", "date", "url", "source_id", "source_locator", "retrieval_timestamp")


def find_index(start=None):
    """Locate index.json.

    Order: the READINGROOM_INDEX environment variable, then walking
    up from this package (the repo root holds index.json), then the
    workspace default. Raises FileNotFoundError when not found.
    """
    env = os.environ.get("READINGROOM_INDEX")
    if env:
        path = Path(env)
        if path.exists():
            return path
    here = Path(start or __file__).resolve()
    for parent in [here.parent] + list(here.parents):
        candidate = parent / "index.json"
        if candidate.exists():
            return candidate
    fallback = (
        Path.home() / "workspace" / "notes" / "museintelligence-library" / "index.json"
    )
    if fallback.exists():
        return fallback
    raise FileNotFoundError("index.json not found (set READINGROOM_INDEX)")


def load_index(path=None):
    """Load index.json; validate every entry has all INDEX_KEYS."""
    index_path = Path(path) if path else find_index()
    with open(index_path, "r", encoding="utf-8") as handle:
        entries = json.load(handle)
    if not isinstance(entries, list):
        raise ValueError(f"{index_path}: index is not a list")
    for pos, entry in enumerate(entries):
        missing = [key for key in INDEX_KEYS if not entry.get(key)]
        if missing:
            raise ValueError(f"{index_path}: entry {pos} missing {missing}")
    return entries


def _date_day(value):
    """First 10 characters of an ISO timestamp (the YYYY-MM-DD day)."""
    return str(value)[:10]


def search(entries, query=None, date_from=None, date_to=None):
    """Filter index entries.

    ``query`` matches a case-insensitive substring of the title, or
    an exact source_id. ``date_from`` / ``date_to`` are YYYY-MM-DD
    days, inclusive, compared against the entry date. Entries keep
    index order (newest first).
    """
    results = []
    wanted = query.lower() if query else None
    for entry in entries:
        if wanted and wanted not in entry["title"].lower():
            if wanted != entry["source_id"].lower():
                continue
        day = _date_day(entry["date"])
        if date_from and day < date_from:
            continue
        if date_to and day > date_to:
            continue
        results.append(entry)
    return results


def parse_front_matter(text):
    """Parse a file's YAML front-matter block.

    Returns (metadata dict, body string). The front-matter is the
    ``---`` block at the top of the file; values are double-quoted
    (JSON quoting) or plain. Raises ValueError on a missing or
    malformed block.
    """
    lines = text.splitlines()
    if not lines or lines[0].strip() != "---":
        raise ValueError("missing opening --- front-matter fence")
    close = None
    for i in range(1, len(lines)):
        if lines[i].strip() == "---":
            close = i
            break
    if close is None:
        raise ValueError("missing closing --- front-matter fence")
    meta = {}
    for line in lines[1:close]:
        if not line.strip():
            continue
        if ":" not in line:
            raise ValueError(f"bad front-matter line: {line!r}")
        key, value = line.split(":", 1)
        key = key.strip()
        value = value.strip()
        if value.startswith('"'):
            try:
                value = json.loads(value)
            except json.JSONDecodeError as exc:
                raise ValueError(f"bad quoted front-matter value: {line!r}") from exc
        meta[key] = value
    body = "\n".join(lines[close + 1:])
    if body.startswith("\n"):
        body = body[1:]
    return meta, body


def _repo_root(index_path):
    return Path(index_path).resolve().parent


def load_post(source_id, entries=None, root=None):
    """Load one post by source_id (e.g. SRC-WP-18250).

    Returns a dict with the front-matter fields plus ``path`` and
    ``content``. Raises KeyError when the source_id is not in the
    index, FileNotFoundError when its file is missing.
    """
    if entries is None:
        entries = load_index()
    entry = None
    for candidate in entries:
        if candidate["source_id"] == source_id:
            entry = candidate
            break
    if entry is None:
        raise KeyError(f"no post with source_id {source_id}")
    base = Path(root) if root else _repo_root(find_index())
    path = base / entry["path"]
    with open(path, "r", encoding="utf-8") as handle:
        meta, content = parse_front_matter(handle.read())
    result = dict(meta)
    result["path"] = entry["path"]
    result["content"] = content
    return result


def provenance_check(entries=None, root=None):
    """Check provenance across the index and the files on disk.

    Every index entry must carry source_id, source_locator (its URL),
    and retrieval_timestamp; every file must exist and its
    front-matter must carry title, date, url, source_id,
    source_locator, and retrieval_timestamp, matching the index entry.
    Returns a report dict: {"ok": bool, "checked": int, "problems":
    [str, ...]}.
    """
    if entries is None:
        entries = load_index()
    base = Path(root) if root else _repo_root(find_index())
    problems = []
    for entry in entries:
        source_id = entry.get("source_id", "?")
        for key in ("source_id", "source_locator", "retrieval_timestamp"):
            if not entry.get(key):
                problems.append(f"{source_id}: index entry missing {key}")
        if entry.get("source_locator") and entry.get("url") and entry["source_locator"] != entry["url"]:
            problems.append(f"{source_id}: index source_locator does not match url")
        path = base / entry.get("path", "")
        if not path.exists():
            problems.append(f"{source_id}: file missing on disk: {entry.get('path')}")
            continue
        try:
            with open(path, "r", encoding="utf-8") as handle:
                meta, _ = parse_front_matter(handle.read())
        except (ValueError, OSError) as exc:
            problems.append(f"{source_id}: unreadable front-matter: {exc}")
            continue
        for key in FRONT_MATTER_KEYS:
            if not meta.get(key):
                problems.append(f"{source_id}: front-matter missing {key}")
        if meta.get("source_id") and meta["source_id"] != entry["source_id"]:
            problems.append(
                f"{source_id}: front-matter source_id {meta['source_id']} "
                f"does not match index"
            )
        if meta.get("url") and meta["url"] != entry["url"]:
            problems.append(f"{source_id}: front-matter url does not match index")
        if meta.get("source_locator") and meta["source_locator"] != entry.get("source_locator"):
            problems.append(f"{source_id}: front-matter source_locator does not match index")
    return {"ok": not problems, "checked": len(entries), "problems": problems}
