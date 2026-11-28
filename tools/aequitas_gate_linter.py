#!/usr/bin/env python3
"""AEQUITAS gate linter — validate a repository against the 18-gate
AGENTS.md acceptance checklist (ICD203, pp. 33-35).

Every pull request, SKILL.md module, tool schema, and rendering artifact
must pass all 18 gates before merging or leaving DRY_RUN status.

Usage:
    python3 aequitas_gate_linter.py [PATH] [--json] [--strict] [--exclude DIR ...]

    PATH defaults to the current directory.

Exit status:
    0  no gate failed (MANUAL gates do not fail unless --strict is given)
    1  at least one gate failed (or a MANUAL gate failed under --strict)
    2  usage / unreadable-path error

Gate statuses:
    PASS    the checkable form of the gate holds for every file scanned
    FAIL    a concrete violation was found (file:line is reported)
    MANUAL  the gate cannot be decided from files alone — a human must
            confirm it. MANUAL never fails a run unless --strict is used.

Honest scope notes (see also each gate's docstring):
  * Gates A4, B4, C4, D1 and D3 are heuristics: they catch the
    checkable shape of the violation, not every instance. A PASS there
    means "no violation of the checkable shape was found", not "the
    gate is proven".
  * Gate A2 checks duplicate keys and canonical-serialization stability
    (sorted keys, RFC 8785-style separators). It is not a full
    RFC 8785 JCS implementation (e.g. it does not re-encode IEEE-754
    numbers); run a dedicated JCS validator before hashing envelopes
    for production use.
  * Gate B2 validates market envelopes found in JSON files. If the
    `jsonschema` package is installed and a
    templates/06_market_sentiment_envelope.json schema is present in
    the scanned tree, envelopes are also validated against that schema.
  * Gate D2 (context vs. authorization) and E3 (human sign-off) are
    MANUAL by design: no static scan can prove that a loaded skill was
    not treated as an authorization token, or that a promotion was
    really signed by a human.

Source: "MuseIntelligence ICD203 — Unmanned_News ReadingRoom"
(AGENTS.md roles & 18-gate acceptance checklist, pp. 33-35; follow-up
item listed on p. 35: "A Python linter script to automatically
validate repositories against the 18-point AGENTS.md acceptance
checklist"). Companion artifact: templates/06_market_sentiment_envelope.json
(TOOL-MKT-01 output contract).
"""

from __future__ import annotations

import argparse
import json
import re
import sys
from dataclasses import dataclass, field
from datetime import datetime
from pathlib import Path

# ---------------------------------------------------------------------------
# Data model
# ---------------------------------------------------------------------------

PASS, FAIL, MANUAL = "PASS", "FAIL", "MANUAL"


@dataclass
class Finding:
    path: str
    line: int | None
    message: str

    def render(self) -> str:
        loc = f"{self.path}:{self.line}" if self.line else self.path
        return f"{loc}: {self.message}"


@dataclass
class GateResult:
    gate_id: str
    name: str
    status: str = PASS
    findings: list[Finding] = field(default_factory=list)
    note: str = ""

    def fail(self, path: str, line: int | None, message: str) -> None:
        self.status = FAIL
        self.findings.append(Finding(path, line, message))

    def to_dict(self) -> dict:
        return {
            "gate": self.gate_id,
            "name": self.name,
            "status": self.status,
            "note": self.note,
            "findings": [f.render() for f in self.findings],
        }


# ---------------------------------------------------------------------------
# File walking helpers
# ---------------------------------------------------------------------------

SKIP_DIRS = {
    ".git", "__pycache__", "node_modules", ".venv", "venv",
    ".tox", ".mypy_cache", ".pytest_cache", "dist", "build",
}
TEXT_EXTS = {
    ".md", ".py", ".json", ".jsonl", ".yaml", ".yml", ".txt",
    ".html", ".cypher", ".cql", ".toml", ".cfg", ".ini", ".js",
    ".ts", ".sh", ".geojson",
}
# Extensions that hold JSON data (GeoJSON is JSON too).
JSON_EXTS = {".json", ".jsonl", ".geojson"}


def iter_files(root: Path, exclude: set[str]) -> list[Path]:
    out: list[Path] = []
    for path in sorted(root.rglob("*")):
        if not path.is_file():
            continue
        if any(part in SKIP_DIRS or part in exclude for part in path.parts):
            continue
        if path.suffix.lower() in TEXT_EXTS or path.name in {
            "SKILL.md", "quarantine.md", "pending_review.md",
            "AGENTS.md", "Dockerfile",
        }:
            out.append(path)
    return out


def read_text(path: Path) -> str | None:
    try:
        return path.read_text(encoding="utf-8", errors="strict")
    except (UnicodeDecodeError, OSError):
        return None


def line_no(text: str, pos: int) -> int:
    return text.count("\n", 0, pos) + 1


def rel(root: Path, path: Path) -> str:
    try:
        return str(path.relative_to(root))
    except ValueError:
        return str(path)


# Duplicate-key detection for A2.
class _DupKeyError(ValueError):
    def __init__(self, key: str):
        super().__init__(key)
        self.key = key


def _no_dup_object(pairs):
    obj = {}
    for key, value in pairs:
        if key in obj:
            raise _DupKeyError(key)
        obj[key] = value
    return obj


def load_json_strict(text: str):
    return json.loads(text, object_pairs_hook=_no_dup_object)


# ---------------------------------------------------------------------------
# Shared JSON-object walk (A1, B2)
# ---------------------------------------------------------------------------

SOURCE_ID_KEYS = ("source_id", "sourceId")
SOURCE_LOCATOR_KEYS = ("source_locator", "sourceLocator")
RETRIEVAL_KEYS = ("retrieval_timestamp", "retrievalTimestamp")


def walk_json_objects(node, path: str = ""):
    """Yield (json_path, dict) for every dict in a parsed JSON value."""
    if isinstance(node, dict):
        yield path or "$", node
        for key, value in node.items():
            yield from walk_json_objects(value, f"{path}.{key}")
    elif isinstance(node, list):
        for i, value in enumerate(node):
            yield from walk_json_objects(value, f"{path}[{i}]")


def is_source_object(obj: dict) -> bool:
    """A dict counts as a source object only when one of the provenance
    keys maps to an actual (string) value — a JSON Schema's "properties"
    object merely *names* those fields, with dicts as values, and is not
    a source object."""
    for key in SOURCE_ID_KEYS + SOURCE_LOCATOR_KEYS + RETRIEVAL_KEYS:
        if isinstance(obj.get(key), str):
            return True
    return False


def parse_timestamp(value) -> datetime | None:
    if not isinstance(value, str):
        return None
    try:
        return datetime.fromisoformat(value.replace("Z", "+00:00"))
    except ValueError:
        return None


# ---------------------------------------------------------------------------
# Gate A — Provenance & Cryptographic Integrity
# ---------------------------------------------------------------------------

def gate_a1(root: Path, files: list[Path], json_docs: dict) -> GateResult:
    """A1 Immutable Identifiers: every source object carries a unique
    source_id, stable source_locator, and UTC retrieval_timestamp.
    A payload lacking sourceId/sourceLocator triggers INCOMPLETE_PROVENANCE
    and routes to quarantine.md (see E1)."""
    result = GateResult("A1", "Immutable Identifiers")
    seen_ids: dict[str, str] = {}
    checked = 0
    for path in files:
        if path.suffix.lower() not in JSON_EXTS:
            continue
        doc = json_docs.get(path)
        if doc is None:
            continue
        for jpath, obj in walk_json_objects(doc):
            if not is_source_object(obj):
                continue
            checked += 1
            label = f"{rel(root, path)} {jpath}"
            sid = next((obj.get(k) for k in SOURCE_ID_KEYS if obj.get(k)), None)
            sloc = next((obj.get(k) for k in SOURCE_LOCATOR_KEYS if obj.get(k)), None)
            rts = next((obj.get(k) for k in RETRIEVAL_KEYS if obj.get(k)), None)
            if not sid:
                result.fail(rel(root, path), None,
                            f"{label}: source object missing source_id/sourceId")
            elif not isinstance(sid, str) or not sid.strip():
                result.fail(rel(root, path), None,
                            f"{label}: source_id is empty")
            elif sid in seen_ids:
                result.fail(rel(root, path), None,
                            f"{label}: duplicate source_id {sid!r} "
                            f"(also in {seen_ids[sid]})")
            else:
                seen_ids[sid] = label
            if not sloc:
                result.fail(rel(root, path), None,
                            f"{label}: source object missing "
                            "source_locator/sourceLocator (INCOMPLETE_PROVENANCE)")
            if not rts:
                result.fail(rel(root, path), None,
                            f"{label}: source object missing retrieval_timestamp")
            else:
                ts = parse_timestamp(rts)
                if ts is None:
                    result.fail(rel(root, path), None,
                                f"{label}: retrieval_timestamp {rts!r} is not "
                                "a valid ISO-8601 timestamp")
                elif ts.utcoffset() is None or ts.utcoffset().total_seconds() != 0:
                    result.fail(rel(root, path), None,
                                f"{label}: retrieval_timestamp {rts!r} is not UTC")
    result.note = f"{checked} source object(s) checked; {len(seen_ids)} unique source_id(s)"
    return result


def _check_canonical_doc(result: GateResult, root: Path, path: Path,
                         text: str, lineno: int | None) -> None:
    """Check one JSON document string for duplicate keys and canonical
    serialization stability, recording any failure on ``result``."""
    try:
        load_json_strict(text)
    except _DupKeyError as exc:
        result.fail(rel(root, path), lineno,
                    f"duplicate key {exc.key!r} — canonicalization is "
                    "not deterministic")
        return
    except json.JSONDecodeError as exc:
        result.fail(rel(root, path),
                    lineno if lineno is not None else exc.lineno,
                    f"invalid JSON, cannot canonicalize: {exc.msg}")
        return
    try:
        doc = json.loads(text)
        canonical = json.dumps(doc, sort_keys=True, separators=(",", ":"),
                               ensure_ascii=False)
        again = json.dumps(json.loads(canonical), sort_keys=True,
                           separators=(",", ":"), ensure_ascii=False)
        if canonical != again:
            result.fail(rel(root, path), lineno,
                        "canonical serialization is not stable")
    except (TypeError, ValueError) as exc:
        result.fail(rel(root, path), lineno,
                    f"cannot canonicalize: {exc}")


def gate_a2(root: Path, files: list[Path], json_docs: dict) -> GateResult:
    """A2 Deterministic Canonicalization: all JSON envelopes conform to
    RFC 8785 canonical sorting prior to SHA-256 hashing. Checked here as:
    no duplicate keys, and re-serializing with sorted keys / canonical
    separators is stable. Not a full JCS number-encoding check.
    JSON Lines (.jsonl) files are checked one document per line."""
    result = GateResult("A2", "Deterministic Canonicalization (RFC 8785)")
    checked = 0
    for path in files:
        if path.suffix.lower() not in JSON_EXTS:
            continue
        text = read_text(path)
        if text is None:
            continue
        checked += 1
        if path.suffix.lower() == ".jsonl":
            for lineno, line in enumerate(text.splitlines(), start=1):
                if not line.strip():
                    continue
                _check_canonical_doc(result, root, path, line, lineno)
            continue
        _check_canonical_doc(result, root, path, text, None)
    result.note = f"{checked} JSON file(s) checked for duplicate keys and canonical stability"
    return result


FLOATING_REF = re.compile(
    r"(?:github\.com/[\w.-]+/[\w.-]+/(?:tree|archive|blob)/"
    r"(?:main|master|HEAD)\b"
    r"|github\.com/[\w.-]+/[\w.-]+(?:\.git)?@(?:main|master|HEAD)\b"
    r"|huggingface\.co/[\w.-]+/[\w.-]+/(?:resolve|blob)/(?:main|master|HEAD)\b"
    r"|huggingface\.co/[\w.-]+/[\w.-]+@(?:main|master|HEAD)\b)",
    re.IGNORECASE,
)


def gate_a3(root: Path, files: list[Path]) -> GateResult:
    """A3 Pinned Dependencies: external GitHub / Hugging Face references
    are pinned to immutable commit SHAs (TOOL-GH-01), never floating
    branch names like main or HEAD. Plain paper links (e.g.
    huggingface.co/papers/…) carry no branch and are not flagged."""
    result = GateResult("A3", "Pinned Dependencies")
    checked = 0
    for path in files:
        text = read_text(path)
        if text is None:
            continue
        checked += 1
        for match in FLOATING_REF.finditer(text):
            result.fail(rel(root, path), line_no(text, match.start()),
                        f"floating reference {match.group(0)!r} — pin to a "
                        "commit SHA")
    result.note = f"{checked} text file(s) scanned for floating GitHub/Hugging Face refs"
    return result


# Decomposition classes: a single node must not merge claims from two classes.
_DECOMP_CLASSES = {
    "primary legal text": ("legal_text", "primary_text", "statute_text"),
    "secondary analysis": ("secondary_analysis", "analysis_text", "commentary_text"),
    "on-chain oracle hash": ("oracle_hash", "por_hash", "attestation_hash"),
    "forum post": ("forum_post", "post_text", "forum_text"),
}


def gate_a4(root: Path, files: list[Path], json_docs: dict) -> GateResult:
    """A4 Source Decomposition (heuristic): primary legal texts, secondary
    analyses, on-chain oracle hashes, and forum posts are stored as
    separate nodes rather than merged claims. Flags any single JSON
    object carrying fields from two or more of those classes."""
    result = GateResult("A4", "Source Decomposition")
    checked = 0
    for path in files:
        if path.suffix.lower() not in JSON_EXTS:
            continue
        doc = json_docs.get(path)
        if doc is None:
            continue
        for jpath, obj in walk_json_objects(doc):
            if not isinstance(obj, dict):
                continue
            checked += 1
            present = [name for name, keys in _DECOMP_CLASSES.items()
                       if any(k in obj for k in keys)]
            if len(present) > 1:
                result.fail(rel(root, path), None,
                            f"{jpath}: merged claim — single node carries "
                            f"{' + '.join(present)}")
    result.note = (f"{checked} JSON object(s) checked; heuristic only — "
                   "a PASS means no merged node of the checkable shape was found")
    return result


# ---------------------------------------------------------------------------
# Gate B — Epistemic Firewall & AEQUITAS Compliance
# ---------------------------------------------------------------------------

# Lines that talk *about* a promotion (prohibiting or describing it) rather
# than performing one — never treated as a silent upgrade.
_NEGATION = re.compile(
    r"\b(cannot|can't|never|blocked|prohibit\w*|without human|no unverified|"
    r"must not|not permitted|forbidden|halt|silent|descriptive)\b",
    re.IGNORECASE)
_PROMOTION = re.compile(
    r"(?:promot\w*\s+(?:\w+\s+){0,4}?to\s+[`\"']?VERIFIED_FACT[`\"']?"
    r"|upgrade\w*\s+(?:\w+\s+){0,4}?to\s+[`\"']?VERIFIED_FACT[`\"']?"
    r"|epistemic_tag[`\"']?\s*[:=]\s*[`\"']VERIFIED_FACT[`\"']"
    r"|->\s*[`\"']?VERIFIED_FACT[`\"']?"
    r"|\bVERIFIED_FACT\s*=\s*True\b"
    r"|\"VERIFIED_FACT\"\s*:\s*true)",
    re.IGNORECASE,
)


def gate_b1(root: Path, files: list[Path]) -> GateResult:
    """B1 No Silent Upgrades: automated transitions from SOURCE_ASSERTION
    or CONTEXT_SIGNAL to VERIFIED_FACT are programmatically blocked.
    Flags code/text that performs such a promotion (descriptive or
    prohibiting mentions are not flagged)."""
    result = GateResult("B1", "No Silent Upgrades")
    for path in files:
        text = read_text(path)
        if text is None:
            continue
        for match in _PROMOTION.finditer(text):
            line_start = text.rfind("\n", 0, match.start()) + 1
            line_end = text.find("\n", match.end())
            line = text[line_start:line_end if line_end != -1 else len(text)]
            if _NEGATION.search(line):
                continue
            result.fail(rel(root, path), line_no(text, match.start()),
                        "unauthorized epistemic promotion detected: "
                        f"{line.strip()[:120]}")
    if result.status == PASS:
        result.note = "no unauthorized promotion found outside prohibiting/descriptive text"
    return result


def gate_b2(root: Path, files: list[Path], json_docs: dict,
            schema: dict | None) -> GateResult:
    """B2 Market & Oracle Containment: prediction-market odds (TOOL-MKT-01)
    are explicitly tagged SENTIMENT_ONLY, and Chainlink PoR hashes
    (TOOL-CHAIN-01) are bounded as integrity anchors. The market half is
    checked strictly on every envelope found in JSON; the oracle half is
    checked only where a PoR hash is presented as event evidence."""
    result = GateResult("B2", "Market & Oracle Containment")
    envelopes = 0
    for path in files:
        if path.suffix.lower() not in JSON_EXTS:
            continue
        doc = json_docs.get(path)
        if doc is None:
            continue
        for jpath, obj in walk_json_objects(doc):
            if not isinstance(obj, dict):
                continue
            # An envelope has scalar values for its identifying fields.
            # A JSON Schema's "properties" object merely names those
            # fields (dict values) and is not an envelope.
            if not (isinstance(obj.get("market_id"), str)
                    or isinstance(obj.get("implied_probability_float"),
                                  (int, float))):
                continue
            envelopes += 1
            label = f"{rel(root, path)} {jpath}"
            if obj.get("epistemic_tag") != "SENTIMENT_ONLY":
                result.fail(rel(root, path), None,
                            f"{label}: market envelope epistemic_tag is "
                            f"{obj.get('epistemic_tag')!r}, must be SENTIMENT_ONLY")
            if obj.get("graph_mutation_authorized") is not False:
                result.fail(rel(root, path), None,
                            f"{label}: graph_mutation_authorized must be false")
            if obj.get("human_review_required") is not True:
                result.fail(rel(root, path), None,
                            f"{label}: human_review_required must be true")
            if "confidence_weight" in obj and obj["confidence_weight"] != 0.0:
                result.fail(rel(root, path), None,
                            f"{label}: confidence_weight must be 0.0 for "
                            "market signals")
            prob = obj.get("implied_probability_float")
            if prob is not None and not (isinstance(prob, (int, float))
                                         and not isinstance(prob, bool)
                                         and 0 <= prob <= 1):
                result.fail(rel(root, path), None,
                            f"{label}: implied_probability_float {prob!r} "
                            "outside 0-1")
    if schema is not None and envelopes:
        try:
            import jsonschema  # type: ignore
            validator = jsonschema.Draft202012Validator(schema)
            for path in files:
                if path.suffix.lower() not in JSON_EXTS:
                    continue
                doc = json_docs.get(path)
                if doc is None:
                    continue
                for jpath, obj in walk_json_objects(doc):
                    if isinstance(obj, dict) and (
                            isinstance(obj.get("market_id"), str)
                            or isinstance(obj.get("implied_probability_float"),
                                          (int, float))):
                        for error in validator.iter_errors(obj):
                            result.fail(rel(root, path), None,
                                        f"{jpath}: schema violation: "
                                        f"{error.message}")
            result.note = (f"{envelopes} market envelope(s) checked, "
                           "including validation against "
                           "templates/06_market_sentiment_envelope.json")
        except ImportError:
            result.note = (f"{envelopes} market envelope(s) checked; "
                           "jsonschema not installed, schema validation skipped")
    else:
        result.note = (f"{envelopes} market envelope(s) checked"
                       + ("; no envelope schema found in tree" if not schema else ""))
    return result


# Corrupted OCR variants of SOURCE_ASSERTION (and neighbours) named in the
# ICD203 spec. Assembled from fragments so this file does not itself
# contain the corrupted tokens it scans for.
_CORRUPT_FRAGMENTS = (
    "SOURCE_ASSER" + "ATION", "SOURCE_ASSER" + "TOIN",
    "SOURCE_ASER" + "TION", "SOURCE_ASSERT" + "ON",
    "SOURCE_ASSEP" + "TION", "SOURCE_ASSEN" + "TION",
    "SOURCE_ASSER" + "CTION",
    "VERIF" + "ED_FACT", "VERIFIED_" + "FATC",
    "SENTIMENT_" + "ONLYY", "CONTEX_" + "SIGNAL",
)
CORRUPTED_TOKENS = _CORRUPT_FRAGMENTS

# A corrupted token mentioned in prose that is *about* the corruption
# (the spec listing variants to normalize, a sanitation rule, an example)
# is not a corrupted payload. Skip matches whose surrounding lines
# describe the corruption rather than contain it.
_DESCRIPTIVE_CONTEXT = re.compile(
    r"corrupt|sanit|e\.g\.|normali[sz]e|example", re.IGNORECASE)


def gate_b3(root: Path, files: list[Path]) -> GateResult:
    """B3 OCR & Schema Hygiene: zero corrupted tokens (e.g.
    SOURCE_ASSERATION, SOURCE_ASSERTOIN) in Markdown or Cypher payloads."""
    result = GateResult("B3", "OCR & Schema Hygiene")
    for path in files:
        text = read_text(path)
        if text is None:
            continue
        lines = text.split("\n")
        for token in CORRUPTED_TOKENS:
            for match in re.finditer(re.escape(token), text):
                lineno = line_no(text, match.start())
                window = "\n".join(lines[max(0, lineno - 3):lineno + 2])
                if _DESCRIPTIVE_CONTEXT.search(window):
                    continue
                result.fail(rel(root, path), lineno,
                            f"corrupted token {token!r}")
    return result


_GENERATED_SUMMARY = re.compile(
    r"(LLM[- ]generated summary|generated summary|AI[- ]generated summary"
    r"|Gemini summary|ChatGPT summary)", re.IGNORECASE)


def gate_b4(root: Path, files: list[Path]) -> GateResult:
    """B4 Summary Isolation (heuristic): LLM-generated summaries are
    labeled GENERATED_ANALYSIS and never substituted for verbatim source
    passages. Flags generated summaries with no GENERATED_ANALYSIS label
    nearby."""
    result = GateResult("B4", "Summary Isolation")
    for path in files:
        if path.suffix.lower() != ".md":
            continue
        text = read_text(path)
        if text is None:
            continue
        for match in _GENERATED_SUMMARY.finditer(text):
            window = text[max(0, match.start() - 500):match.end() + 500]
            if "GENERATED_ANALYSIS" not in window:
                result.fail(rel(root, path), line_no(text, match.start()),
                            "generated summary without GENERATED_ANALYSIS label")
    if result.status == PASS:
        result.note = "heuristic only — no unlabeled generated summary found"
    return result


# ---------------------------------------------------------------------------
# Gate C — Graph & Spatial Governance (Neo4j / GeoJSON)
# ---------------------------------------------------------------------------

_MUTATION_TRUE = re.compile(
    r"(?:graph_mutation_authorized|c2_mutation_authorized)[\"']?\s*"
    r"(?:[:=]\s*(?:true|True)\b|:\s*\{\s*[\"']?const[\"']?\s*:\s*true\b)",
    re.IGNORECASE,
)


def gate_c1(root: Path, files: list[Path]) -> GateResult:
    """C1 Zero Autonomous Mutations: graph_mutation_authorized and
    c2_mutation_authorized default to false across all automated scripts."""
    result = GateResult("C1", "Zero Autonomous Mutations")
    for path in files:
        text = read_text(path)
        if text is None:
            continue
        for match in _MUTATION_TRUE.finditer(text):
            result.fail(rel(root, path), line_no(text, match.start()),
                        f"mutation authorized: {match.group(0).strip()[:100]}")
    return result


CAUSAL = ("CONTROLS", "OWNS", "FINANCES", "EXECUTES_C2")
_CAUSAL_REL = re.compile(
    r"(?:\[:\s*(?:CONTROLS|OWNS|FINANCES|EXECUTES_C2)\b"
    r"|-\[\s*:?\s*(?:CONTROLS|OWNS|FINANCES|EXECUTES_C2)\b"
    r"|\"(?:relationship|relationship_type|edge_type)\"\s*:\s*\"(?:CONTROLS|OWNS|FINANCES|EXECUTES_C2)\""
    r"|'(?:CONTROLS|OWNS|FINANCES|EXECUTES_C2)'\s*\])")


def gate_c2(root: Path, files: list[Path]) -> GateResult:
    """C2 Non-Causal Edges Only: unverified relationships are restricted
    to RELATED_TO, MENTIONED_WITH, SUPPORTED_BY, QUARANTINED_AS. Causal
    predicates (CONTROLS, OWNS, FINANCES, EXECUTES_C2) are absent — as
    relationship types in Cypher/JSON, not as words in prose."""
    result = GateResult("C2", "Non-Causal Edges Only")
    for path in files:
        text = read_text(path)
        if text is None:
            continue
        for match in _CAUSAL_REL.finditer(text):
            result.fail(rel(root, path), line_no(text, match.start()),
                        f"causal predicate used as a relationship: "
                        f"{match.group(0).strip()[:100]}")
    if result.status == PASS:
        result.note = "no causal predicate found in Cypher/JSON relationship position"
    return result


def _coord_pairs(node, pairs: list):
    if isinstance(node, list) and len(node) == 2 and all(
            isinstance(v, (int, float)) and not isinstance(v, bool)
            for v in node):
        pairs.append(tuple(node))
    elif isinstance(node, list):
        for item in node:
            _coord_pairs(item, pairs)


def gate_c3(root: Path, files: list[Path], json_docs: dict) -> GateResult:
    """C3 Spatial Non-Navigability: all GeoJSON layers enforce
    [longitude, latitude] coordinate order, navigation_suitability: 0,
    and live_tracking: false."""
    result = GateResult("C3", "Spatial Non-Navigability")
    geojson_files = 0
    for path in files:
        if path.suffix.lower() not in {".json", ".geojson"}:
            continue
        doc = json_docs.get(path)
        if not isinstance(doc, dict):
            continue
        if doc.get("type") not in {"Feature", "FeatureCollection", "GeometryCollection"} \
                and "features" not in doc and "geometry" not in doc:
            continue
        geojson_files += 1
        label = rel(root, path)
        # Collect (properties, geometry) pairs to check. A FeatureCollection
        # with "features": null has no features (treat as empty, do not
        # crash). A GeometryCollection carries "geometries", not features:
        # check the coordinates in each geometry, but there are no
        # per-geometry properties to check for navigation flags.
        checks: list[tuple[dict | None, object]] = []
        if "features" in doc:
            for feature in (doc.get("features") or []):
                if isinstance(feature, dict):
                    checks.append((feature.get("properties"),
                                   feature.get("geometry")))
        elif doc.get("type") == "GeometryCollection":
            for geometry in (doc.get("geometries") or []):
                checks.append((None, geometry))
        else:
            # A single Feature (or a bare geometry-bearing doc).
            checks.append((doc.get("properties"), doc.get("geometry")))
        for props, geometry in checks:
            if props is not None:
                props = props or {}
                if props.get("navigation_suitability") != 0:
                    result.fail(label, None,
                                "GeoJSON feature missing navigation_suitability: 0")
                if props.get("live_tracking") is not False:
                    result.fail(label, None,
                                "GeoJSON feature missing live_tracking: false")
            pairs: list = []
            _coord_pairs(geometry, pairs)
            for lon, lat in pairs:
                if not (-180 <= lon <= 180 and -90 <= lat <= 90):
                    result.fail(label, None,
                                f"coordinate [{lon}, {lat}] outside "
                                "[longitude, latitude] ranges — check order")
    result.note = f"{geojson_files} GeoJSON file(s) checked"
    return result


def gate_c4(root: Path, files: list[Path]) -> GateResult:
    """C4 Visual Grammar Alignment (heuristic): unverified claims render
    strictly as RED_HOLLOW nodes; SOLID_MARKERS appear only where
    human-reviewed provenance exists. Flags SOLID_MARKERS in a file
    with no human-review marker."""
    result = GateResult("C4", "Visual Grammar Alignment")
    review_mark = re.compile(r"human[-_ ]review", re.IGNORECASE)
    for path in files:
        text = read_text(path)
        if text is None or "SOLID_MARKERS" not in text:
            continue
        if not review_mark.search(text):
            for match in re.finditer(r"SOLID_MARKERS", text):
                result.fail(rel(root, path), line_no(text, match.start()),
                            "SOLID_MARKERS used with no human-reviewed "
                            "provenance marker in the same file")
    if result.status == PASS:
        result.note = "heuristic only — SOLID_MARKERS occurrences co-occur with a human-review marker"
    return result


# ---------------------------------------------------------------------------
# Gate D — Agent & Skill Hygiene (SKILL.md Linting)
# ---------------------------------------------------------------------------

SKILL_SMELL = re.compile(
    r"(skip (?:the )?verification|bypass\w*\s+(?:the )?verification"
    r"|proceed without (?:human )?review|if unsure,?\s+proceed"
    r"|do not (?:verify|check))", re.IGNORECASE)
_FALLBACK = re.compile(r"\b(fallback|on error|if .* fails|retry|escalate)\b",
                       re.IGNORECASE)
_NUMBERED_STEP = re.compile(r"^\s*\d+[.)]\s+\S", re.MULTILINE)


def gate_d1(root: Path, files: list[Path]) -> GateResult:
    """D1 No 'Skill Smells' (heuristic): SKILL.md files avoid rigid Series
    of Commands scripts without fallback handling and close
    Rationalization Loopholes that allow agents to skip verification."""
    result = GateResult("D1", "No Skill Smells")
    skill_files = 0
    for path in files:
        if path.name != "SKILL.md":
            continue
        skill_files += 1
        text = read_text(path)
        if text is None:
            continue
        for match in SKILL_SMELL.finditer(text):
            result.fail(rel(root, path), line_no(text, match.start()),
                        f"rationalization loophole: {match.group(0)!r}")
        steps = _NUMBERED_STEP.findall(text)
        if len(steps) >= 5 and not _FALLBACK.search(text):
            result.fail(rel(root, path), None,
                        f"rigid Series of Commands: {len(steps)} numbered "
                        "steps with no fallback / on-error handling")
    result.note = f"{skill_files} SKILL.md file(s) checked; heuristic only"
    return result


def gate_d2(root: Path, files: list[Path]) -> GateResult:
    """D2 Context vs. Authorization Separation: loaded skills and MCP
    contexts are treated strictly as contextual input, never as
    authorization tokens. Not decidable by static scan — MANUAL."""
    return GateResult(
        "D2", "Context vs. Authorization Separation", MANUAL,
        note="MANUAL: confirm no skill/MCP context is used as an "
             "authorization token (e.g. a token, credential, or approval "
             "read from loaded context).")


_NETWORK_CALL = re.compile(
    r"\b(requests\.(?:get|post|put|patch|delete|request)"
    r"|urllib\.request\.urlopen|httpx\.(?:get|post|request|Client)"
    r"|http\.client\.HTTPConnection|socket\.create_connection"
    r"|openai\.|anthropic\.|boto3\.client)\b")
_ALLOW_NETWORK = "aequitas: allow-network"


def gate_d3(root: Path, files: list[Path]) -> GateResult:
    """D3 Air-Gap & Telemetry Safety (heuristic): local execution pipelines
    make zero unauthorized outbound API calls during DRY_RUN execution.
    Flags network calls in Python files; annotate an intentional,
    authorized call with a trailing '# aequitas: allow-network' comment."""
    result = GateResult("D3", "Air-Gap & Telemetry Safety")
    py_files = 0
    for path in files:
        if path.suffix.lower() != ".py":
            continue
        py_files += 1
        text = read_text(path)
        if text is None:
            continue
        for match in _NETWORK_CALL.finditer(text):
            line_start = text.rfind("\n", 0, match.start()) + 1
            line_end = text.find("\n", match.end())
            line = text[line_start:line_end if line_end != -1 else len(text)]
            if _ALLOW_NETWORK in line:
                continue
            result.fail(rel(root, path), line_no(text, match.start()),
                        f"outbound call in Python file: {line.strip()[:120]}")
    result.note = (f"{py_files} Python file(s) scanned; heuristic only — "
                   "a PASS means no outbound call site of the checkable shape")
    return result


# ---------------------------------------------------------------------------
# Gate E — Quarantine & Human Adjudication
# ---------------------------------------------------------------------------

def gate_e1(root: Path, files: list[Path], a1: GateResult) -> GateResult:
    """E1 Deterministic Routing: incomplete provenance or cross-domain
    conflations route automatically to quarantine.md or pending_review.md.
    Checked as: if A1 found incomplete provenance, a quarantine /
    pending-review file must exist in the tree."""
    result = GateResult("E1", "Deterministic Routing")
    incomplete = [f for f in a1.findings if "INCOMPLETE_PROVENANCE" in f.message
                  or "missing source" in f.message]
    if not incomplete:
        result.note = "no incomplete-provenance payload found, so routing was not exercised"
        return result
    names = {p.name for p in files}
    if "quarantine.md" in names or "pending_review.md" in names:
        result.note = (f"{len(incomplete)} incomplete-provenance finding(s) "
                       "and a quarantine/pending-review file exists")
    else:
        result.fail(str(root), None,
                    f"{len(incomplete)} payload(s) with incomplete provenance "
                    "but no quarantine.md or pending_review.md in the tree")
    return result


def gate_e2(root: Path, files: list[Path]) -> GateResult:
    """E2 Audit Trail Completeness: every quarantined item includes an
    explicit decision_rationale placeholder and human_review_required: true.
    If there is no quarantine file, there is nothing to audit."""
    result = GateResult("E2", "Audit Trail Completeness")
    quarantine_files = [p for p in files
                        if p.name in {"quarantine.md", "pending_review.md"}]
    if not quarantine_files:
        result.note = "no quarantine.md / pending_review.md — nothing quarantined to audit"
        return result
    for path in quarantine_files:
        text = read_text(path) or ""
        if "decision_rationale" not in text:
            result.fail(rel(root, path), None,
                        "quarantined items lack a decision_rationale placeholder")
        if "human_review_required" not in text:
            result.fail(rel(root, path), None,
                        "quarantined items lack human_review_required")
        elif re.search(r"human_review_required\s*[:=]\s*(false|False)", text):
            result.fail(rel(root, path), None,
                        "quarantined item has human_review_required: false")
    return result


def gate_e3(root: Path, files: list[Path]) -> GateResult:
    """E3 Human Sign-Off: final promotion to reviewed publication status
    contains a verifiable human reviewer signature and timestamp. A
    static scan can find a signature, not verify the human behind it —
    MANUAL unless a signed record is present, in which case PASS with
    the caveat recorded."""
    result = GateResult("E3", "Human Sign-Off")
    signed = re.compile(
        r"(human_reviewer|reviewed_by|approved_by)\s*[:=]\s*\S+.{0,120}?"
        r"\d{4}-\d{2}-\d{2}", re.IGNORECASE | re.DOTALL)
    for path in files:
        text = read_text(path)
        if text and signed.search(text):
            result.note = (f"signed review record found in {rel(root, path)} — "
                           "signature presence only; verifying the human is out "
                           "of scope for a static linter")
            return result
    result.status = MANUAL
    result.note = ("MANUAL: no signed human-review record found in the tree — "
                   "confirm a human reviewer signed off with a timestamp "
                   "before any promotion to reviewed publication status")
    return result


# ---------------------------------------------------------------------------
# Runner
# ---------------------------------------------------------------------------

def find_envelope_schema(root: Path, files: list[Path]) -> dict | None:
    for path in files:
        if path.name == "06_market_sentiment_envelope.json":
            try:
                return json.loads(path.read_text(encoding="utf-8"))
            except (OSError, json.JSONDecodeError):
                return None
    return None


def load_json_docs(files: list[Path]) -> dict[Path, object | None]:
    docs: dict[Path, object | None] = {}
    for path in files:
        if path.suffix.lower() not in JSON_EXTS:
            continue
        text = read_text(path)
        if text is None:
            docs[path] = None
            continue
        if path.suffix.lower() == ".jsonl":
            # JSON Lines: one JSON document per non-empty line. Parse
            # each line; a single malformed line makes the whole file
            # unparseable (same as a malformed single-document JSON).
            # The parsed lines are stored as a list, which
            # walk_json_objects traverses line by line.
            objs: list[object] = []
            bad = False
            for line in text.splitlines():
                if not line.strip():
                    continue
                try:
                    objs.append(json.loads(line))
                except json.JSONDecodeError:
                    bad = True
                    break
            docs[path] = None if bad else objs
            continue
        try:
            docs[path] = json.loads(text)
        except json.JSONDecodeError:
            docs[path] = None
    return docs


def run(root: Path, exclude: set[str]) -> list[GateResult]:
    files = iter_files(root, exclude)
    json_docs = load_json_docs(files)
    schema = find_envelope_schema(root, files)

    a1 = gate_a1(root, files, json_docs)
    results = [
        a1,
        gate_a2(root, files, json_docs),
        gate_a3(root, files),
        gate_a4(root, files, json_docs),
        gate_b1(root, files),
        gate_b2(root, files, json_docs, schema),
        gate_b3(root, files),
        gate_b4(root, files),
        gate_c1(root, files),
        gate_c2(root, files),
        gate_c3(root, files, json_docs),
        gate_c4(root, files),
        gate_d1(root, files),
        GateResult("D2", "Context vs. Authorization Separation", MANUAL,
                   note="MANUAL: confirm no skill/MCP context is used as an "
                        "authorization token (e.g. a token, credential, or "
                        "approval read from loaded context)."),
        gate_d3(root, files),
        gate_e1(root, files, a1),
        gate_e2(root, files),
        gate_e3(root, files),
    ]
    return results


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(
        description="Validate a repository against the 18-gate AGENTS.md "
                    "acceptance checklist (ICD203, pp. 33-35).")
    parser.add_argument("path", nargs="?", default=".",
                        help="repository root to scan (default: .)")
    parser.add_argument("--json", action="store_true",
                        help="emit machine-readable JSON instead of text")
    parser.add_argument("--strict", action="store_true",
                        help="treat MANUAL gates as failures")
    parser.add_argument("--exclude", nargs="*", default=[],
                        help="extra directory names to skip")
    args = parser.parse_args(argv)

    root = Path(args.path).resolve()
    if not root.is_dir():
        print(f"error: {root} is not a directory", file=sys.stderr)
        return 2

    results = run(root, set(args.exclude))
    failed = [r for r in results if r.status == FAIL]
    manual = [r for r in results if r.status == MANUAL]
    passed = [r for r in results if r.status == PASS]

    if args.json:
        print(json.dumps({
            "root": str(root),
            "summary": {"pass": len(passed), "fail": len(failed),
                        "manual": len(manual), "total": len(results)},
            "gates": [r.to_dict() for r in results],
        }, indent=2))
    else:
        for r in results:
            mark = {"PASS": "✓", "FAIL": "✗", "MANUAL": "?"}[r.status]
            print(f"[{mark}] {r.gate_id} {r.name}: {r.status}")
            if r.note:
                print(f"      {r.note}")
            for finding in r.findings:
                print(f"      {finding.render()}")
        print(f"\n{len(passed)} passed, {len(failed)} failed, "
              f"{len(manual)} manual — {len(results)} gates total")
        if failed:
            print("Result: FAIL — do not merge or leave DRY_RUN.")
        elif manual and args.strict:
            print("Result: FAIL under --strict — manual gates unresolved.")
        elif manual:
            print("Result: PASS with manual gates to confirm by a human.")
        else:
            print("Result: PASS — all 18 gates clear.")

    if failed:
        return 1
    if args.strict and manual:
        return 1
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
