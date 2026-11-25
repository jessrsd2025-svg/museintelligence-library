"""Reading-room library: the 577-post corpus of "jessrsd's Blog".

Public API: load_index, search, load_post, provenance_check,
parse_front_matter, find_index.
"""

from .library import (
    find_index,
    load_index,
    load_post,
    parse_front_matter,
    provenance_check,
    search,
)

__version__ = "0.1.0"

__all__ = [
    "find_index",
    "load_index",
    "load_post",
    "parse_front_matter",
    "provenance_check",
    "search",
    "__version__",
]
