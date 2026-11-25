"""Tests for the reading-room library.

Verifies the built corpus: 577 entries in the index, every file
present on disk, every file's front-matter complete, and the index
matching the scrape (count, titles, dates, URLs, source_ids).
The scrape comparison needs the scrape file; it is skipped with a
clear message when the scrape is not at any known location.
"""

from __future__ import annotations

import json
import os
import unittest
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parent.parent
INDEX_PATH = REPO_ROOT / "index.json"

from readingroom.library import parse_front_matter

SCRAPE_CANDIDATES = [
    Path(p) for p in [os.environ.get("READINGROOM_SCRAPE")] if p
] + [
    REPO_ROOT.parent / "museintelligence-app" / "docs" / "wordpress-posts.md",
    Path.home() / "workspace" / "notes" / "museintelligence-app"
    / "docs" / "wordpress-posts.md",
]


def find_scrape():
    for candidate in SCRAPE_CANDIDATES:
        if candidate.exists():
            return candidate
    return None


class LibraryTestCase(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        from readingroom import load_index

        cls.entries = load_index(str(INDEX_PATH))
        cls.by_id = {e["source_id"]: e for e in cls.entries}
        cls.scrape_path = find_scrape()

    def test_index_has_577_entries(self):
        self.assertEqual(len(self.entries), 577)

    def test_no_duplicate_source_ids(self):
        self.assertEqual(len(self.by_id), len(self.entries))

    def test_paths_are_unique_and_under_library(self):
        paths = [e["path"] for e in self.entries]
        self.assertEqual(len(set(paths)), len(paths))
        for path in paths:
            self.assertTrue(path.startswith("library/"), path)
            self.assertTrue(path.endswith(".md"), path)

    def test_every_file_exists_on_disk(self):
        missing = [
            e["path"] for e in self.entries if not (REPO_ROOT / e["path"]).exists()
        ]
        self.assertEqual(missing, [])

    def test_front_matter_complete_and_matching(self):
        required = ("title", "date", "url", "source_id", "source_locator", "retrieval_timestamp")
        for entry in self.entries:
            path = REPO_ROOT / entry["path"]
            meta, content = parse_front_matter(
                path.read_text(encoding="utf-8")
            )
            for key in required:
                self.assertTrue(meta.get(key), f"{entry['source_id']}: missing {key}")
            self.assertEqual(meta["source_id"], entry["source_id"])
            self.assertEqual(meta["url"], entry["url"])
            self.assertEqual(meta["source_locator"], entry["url"])
            self.assertEqual(meta["date"], entry["date"])
            self.assertEqual(
                meta["retrieval_timestamp"], entry["retrieval_timestamp"]
            )
            self.assertTrue(content.strip(), f"{entry['source_id']}: empty content")
            # Filename carries the post id and slug.
            post_id = entry["source_id"].removeprefix("SRC-WP-")
            self.assertTrue(
                Path(entry["path"]).name.startswith(f"{post_id}-"),
                entry["path"],
            )

    def test_provenance_check_clean(self):
        from readingroom import provenance_check

        report = provenance_check(self.entries, root=str(REPO_ROOT))
        self.assertTrue(report["ok"], report["problems"][:5])
        self.assertEqual(report["checked"], 577)

    def test_search_by_keyword(self):
        from readingroom import search

        results = search(self.entries, "ICD203")
        self.assertTrue(len(results) >= 1)
        self.assertIn("SRC-WP-18250", {r["source_id"] for r in results})
        # Case-insensitive, and an unknown keyword finds nothing.
        self.assertEqual(
            {r["source_id"] for r in search(self.entries, "icd203")},
            {r["source_id"] for r in results},
        )
        self.assertEqual(search(self.entries, "zzz-no-such-title-zzz"), [])

    def test_search_by_date_range(self):
        from readingroom import search

        day = search(self.entries, date_from="2026-11-25", date_to="2026-11-25")
        self.assertEqual([r["source_id"] for r in day], ["SRC-WP-18250"])
        old = search(self.entries, date_from="2023-12-22", date_to="2023-12-22")
        self.assertEqual([r["source_id"] for r in old], ["SRC-WP-20"])

    def test_load_post_by_source_id(self):
        from readingroom import load_post

        post = load_post("SRC-WP-18250", self.entries, root=str(REPO_ROOT))
        self.assertEqual(post["source_id"], "SRC-WP-18250")
        self.assertIn("Renderings.md", post["content"])
        self.assertTrue(post["title"].startswith("Unmanned_News ReadingRoonm"))
        with self.assertRaises(KeyError):
            load_post("SRC-WP-99999999", self.entries, root=str(REPO_ROOT))

    def test_index_matches_scrape(self):
        if self.scrape_path is None:
            self.skipTest("scrape file not found at any known location")
        from readingroom.scrape import parse_scrape

        index_rows, sections = parse_scrape(str(self.scrape_path))
        self.assertEqual(len(index_rows), 577)
        self.assertEqual(len(sections), 577)
        for row, entry in zip(index_rows, self.entries):
            self.assertEqual(row["source_id"], entry["source_id"])
            self.assertEqual(row["title"], entry["title"])
            self.assertEqual(row["date"], entry["date"])
            self.assertEqual(row["url"], entry["url"])
        # Front-matter titles match the section headings.
        for sec in sections:
            entry = self.by_id[sec["source_id"]]
            path = REPO_ROOT / entry["path"]
            meta, _ = parse_front_matter(path.read_text(encoding="utf-8"))
            self.assertEqual(meta["title"], sec["section_title"])
            self.assertEqual(meta["date"], sec["date"])

    def test_index_is_valid_json_with_required_keys(self):
        raw = json.loads(INDEX_PATH.read_text(encoding="utf-8"))
        self.assertIsInstance(raw, list)
        for entry in raw:
            for key in (
                "title",
                "date",
                "url",
                "source_id",
                "path",
                "retrieval_timestamp",
            ):
                self.assertIn(key, entry)


if __name__ == "__main__":
    unittest.main()
