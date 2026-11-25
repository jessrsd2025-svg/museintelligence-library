"""Command line for the reading-room library.

Usage::

    python3 -m readingroom --count
    python3 -m readingroom --search ICD203
    python3 -m readingroom --search ICD203 --from 2026-11-01 --to 2026-11-30
    python3 -m readingroom --show SRC-WP-18250
    python3 -m readingroom --check

``--index`` overrides the index.json location. Standard library
only; everything is local, no network access.
"""

from __future__ import annotations

import argparse
import sys

from .library import find_index, load_index, load_post, provenance_check, search


def main(argv=None):
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--index", help="path to index.json")
    parser.add_argument("--search", metavar="QUERY", help="keyword (title) or source_id")
    parser.add_argument("--from", dest="date_from", help="earliest day, YYYY-MM-DD")
    parser.add_argument("--to", dest="date_to", help="latest day, YYYY-MM-DD")
    parser.add_argument("--show", metavar="SOURCE_ID", help="print one post by source_id")
    parser.add_argument("--check", action="store_true", help="run the provenance check")
    parser.add_argument("--count", action="store_true", help="print the entry count")
    args = parser.parse_args(argv)

    index_path = args.index
    entries = load_index(index_path)

    if args.count:
        print(f"{len(entries)} posts indexed (index: {index_path or find_index()})")
    if args.search is not None:
        results = search(entries, args.search, args.date_from, args.date_to)
        print(f"{len(results)} match(es)")
        for entry in results:
            print(f"{entry['date'][:10]}  {entry['source_id']}  {entry['title']}")
            print(f"    {entry['path']}")
    if args.show:
        try:
            post = load_post(args.show, entries)
        except KeyError as exc:
            print(str(exc), file=sys.stderr)
            return 1
        print(f"{post['title']}")
        print(f"{post['date']}  {post['source_id']}  {post['url']}")
        print()
        print(post["content"])
    if args.check:
        report = provenance_check(entries)
        print(f"checked {report['checked']} entries")
        if report["ok"]:
            print("provenance check: OK")
        else:
            print(f"provenance check: {len(report['problems'])} problem(s)")
            for problem in report["problems"]:
                print(f"  - {problem}")
            return 1
    if not (args.count or args.search is not None or args.show or args.check):
        parser.print_help()
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
