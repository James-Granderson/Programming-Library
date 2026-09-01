#!/usr/bin/env python3
"""
Hypsos — Markdown structure enforcer for the Programming Library corpus.

STRICT RULE: this script normalizes STRUCTURE only. It never invents,
rewrites, expands, summarizes, or deletes legitimate knowledge. It only
reorganizes text that already exists in a file into the canonical
template.

Design: every file is parsed into a structured model (heading, metadata
dict, five section blocks) and then deterministically re-serialized from
that model. Because the output is always rebuilt from the same
canonical serializer, running the script on its own output re-parses
into an identical model and produces byte-identical text — that's what
makes it idempotent, not a special-cased check for "already clean."

Usage:
    python3 enforce-md.py --dry-run     # report only, write nothing
    python3 enforce-md.py               # apply changes
    python3 enforce-md.py --root PATH   # override library root

Run it twice. The second run must report "Files changed: 0".
"""

import argparse
import re
import sys
from pathlib import Path

META_ORDER = [
    "Concept", "Action", "Object", "Classification",
    "Environment", "Path Type", "Tags",
]

SECTION_ORDER = [
    "What It Is", "What It Does", "How to Use",
    "Requirements", "Representation",
]

# Used only to pick a fence language for previously-unfenced Representation
# content. This is a structural/formatting choice (which code-fence tag to
# use), not new knowledge — the underlying text is never altered.
LANG_MAP = {
    "sql": "sql",
    "shell": "sh",
    "c": "c",
    "c++": "cpp",
    "python": "python",
    "powershell": "powershell",
    "git": "bash",
    "html": "html",
}

EXCLUDE_DIRS = {"Hypsos", "Schema", ".git"}


class ParseError(Exception):
    pass


def find_markdown_files(root: Path):
    files = []
    for p in root.rglob("*.md"):
        if any(part in EXCLUDE_DIRS for part in p.relative_to(root).parts):
            continue
        files.append(p)
    return sorted(files)


def extract_heading(text: str):
    """Return (heading_text, remainder). Drops a stray duplicate line that
    just repeats the bare object name right after the heading — a known
    corruption pattern (`# `rm`` followed by a bare `rm` line)."""
    lines = text.splitlines()
    if not lines or not lines[0].strip().startswith("#"):
        raise ParseError("No leading '#' heading found")

    heading_line = lines[0].strip()
    heading = heading_line.lstrip("#").strip()
    heading_bare = heading.strip("`").strip()

    idx = 1
    while idx < len(lines) and lines[idx].strip() == "":
        idx += 1
    if idx < len(lines) and lines[idx].strip().strip("`").strip() == heading_bare:
        idx += 1

    return heading, "\n".join(lines[idx:])


_META_KEY_RE = re.compile(
    r"\*\*(" + "|".join(re.escape(k) for k in META_ORDER) + r"):\*\*\s*"
)


def extract_metadata(text: str):
    """Pull **Key:** Value pairs regardless of whether they were written
    one-per-line (correct) or collapsed onto a single line (corruption).
    Returns (meta_dict, remainder_text_after_the_metadata_block)."""
    matches = list(_META_KEY_RE.finditer(text))
    if not matches:
        raise ParseError("No metadata block found")

    meta = {}
    for i, m in enumerate(matches):
        key = m.group(1)
        start = m.end()
        end = matches[i + 1].start() if i + 1 < len(matches) else None
        value_block = text[start:end] if end is not None else text[start:]
        value_block = value_block.strip()
        value = value_block.splitlines()[0].strip() if value_block else ""
        meta[key] = value

    # Remainder starts right after the last key's marker; its first line
    # is the tail of that key's own value (already captured above), so
    # drop it before returning what comes after.
    tail = text[matches[-1].end():]
    tail_lines = tail.splitlines()
    remainder = "\n".join(tail_lines[1:]) if tail_lines else ""
    return meta, remainder


def strip_leading_separators(text: str):
    """Drop any number of leading blank lines / '---' lines, however many
    duplicates accumulated. The canonical serializer re-adds exactly one."""
    lines = text.splitlines()
    i = 0
    while i < len(lines) and (lines[i].strip() == "" or lines[i].strip() == "---"):
        i += 1
    return "\n".join(lines[i:])


_SECTION_ALTS = "|".join(re.escape(s) for s in SECTION_ORDER)
_SECTION_HEADING_RE = re.compile(
    r"^\s{0,3}#{1,3}\s*(" + _SECTION_ALTS + r")\s*$", re.IGNORECASE
)
_SECTION_PLAIN_RE = re.compile(
    r"^\s{0,3}(" + _SECTION_ALTS + r")\s*$", re.IGNORECASE
)


def extract_sections(text: str):
    """Locate each of the five canonical sections wherever they appear —
    properly headed with '###', or degraded to a bare plain-text line
    (a known corruption pattern). Content is never dropped: if a section
    name recurs (duplicate heading corruption), its content blocks are
    concatenated rather than overwritten."""
    lines = text.splitlines()
    markers = []

    for idx, line in enumerate(lines):
        m = _SECTION_HEADING_RE.match(line) or _SECTION_PLAIN_RE.match(line)
        if m:
            name = m.group(1)
            canonical = next(s for s in SECTION_ORDER if s.lower() == name.lower())
            markers.append((idx, canonical))

    if not markers:
        raise ParseError("No recognizable section headings found")

    sections = {}
    for i, (idx, name) in enumerate(markers):
        start = idx + 1
        end = markers[i + 1][0] if i + 1 < len(markers) else len(lines)
        block_lines = lines[start:end]

        while block_lines and block_lines[0].strip() == "":
            block_lines.pop(0)
        # Drop a duplicated plain-text repeat of the heading itself,
        # e.g. "### What It Is\n\nWhat It Is\n\nActual content".
        if block_lines and block_lines[0].strip().lower() == name.lower():
            block_lines.pop(0)
            while block_lines and block_lines[0].strip() == "":
                block_lines.pop(0)

        block = "\n".join(block_lines).strip()

        if sections.get(name):
            if block:
                sections[name] = sections[name].rstrip() + "\n\n" + block
        else:
            sections[name] = block

    return sections


_FENCE_RE = re.compile(r"```[^\n]*\n.*?```", re.DOTALL)


def normalize_representation(content: str, concept: str):
    """Ensure Representation content sits inside a fenced code block.
    If a fence already exists anywhere in the block, the block is left
    untouched (including any legacy trailing prose like an old Flags
    list after the fence — that's existing knowledge, not touched).
    If no fence exists at all, wrap the leading contiguous block of
    lines in a fence and leave anything after the first blank line
    exactly as it was."""
    if _FENCE_RE.search(content):
        return content.strip()

    lines = content.splitlines()
    code_lines, rest_lines = [], []
    in_rest = False
    for ln in lines:
        if not in_rest and ln.strip() == "" and code_lines:
            in_rest = True
            continue
        (rest_lines if in_rest else code_lines).append(ln)

    lang = LANG_MAP.get(concept.strip().lower(), "")
    fence = f"```{lang}\n" + "\n".join(code_lines).strip("\n") + "\n```"
    rest = "\n".join(rest_lines).strip()
    return f"{fence}\n\n{rest}" if rest else fence


def build_canonical(heading: str, meta: dict, sections: dict) -> str:
    lines = [f"# {heading}", ""]
    for key in META_ORDER:
        lines.append(f"**{key}:** {meta.get(key, '')}")
    lines += ["", "---", ""]

    for i, sec in enumerate(SECTION_ORDER):
        lines.append(f"### {sec}")
        lines.append("")
        lines.append(sections.get(sec, "").strip())
        if i != len(SECTION_ORDER) - 1:
            lines.append("")

    return "\n".join(lines).rstrip() + "\n"


def process_file(path: Path):
    original = path.read_text(encoding="utf-8")

    try:
        heading, rest = extract_heading(original)
        meta, rest = extract_metadata(rest)
        rest = strip_leading_separators(rest)
        sections = extract_sections(rest)
    except ParseError as e:
        return None, f"SKIPPED ({e})"

    concept = meta.get("Concept", "")
    if "Representation" in sections:
        sections["Representation"] = normalize_representation(
            sections["Representation"], concept
        )

    missing_meta = [k for k in META_ORDER if not meta.get(k)]
    missing_sections = [s for s in SECTION_ORDER if s not in sections]

    canonical = build_canonical(heading, meta, sections)

    notes = []
    if missing_meta:
        notes.append(f"missing metadata: {', '.join(missing_meta)}")
    if missing_sections:
        notes.append(f"missing sections: {', '.join(missing_sections)}")

    return canonical, ("; ".join(notes) if notes else None)


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument(
        "--root",
        default="/Users/badbwoyasapyvxx/Programming Library",
        help="Library root to scan",
    )
    ap.add_argument("--dry-run", action="store_true", help="Report only, write nothing")
    args = ap.parse_args()

    root = Path(args.root)
    if not root.is_dir():
        print(f"ERROR: root not found: {root}")
        sys.exit(1)

    files = find_markdown_files(root)
    checked = changed = skipped = 0
    warnings = []

    for f in files:
        checked += 1
        try:
            canonical, note = process_file(f)
        except Exception as e:
            skipped += 1
            print(f"ERROR processing {f}: {e}")
            continue

        if canonical is None:
            skipped += 1
            print(f"SKIP: {f} — {note}")
            continue

        if note:
            warnings.append(f"{f}: {note}")

        original = f.read_text(encoding="utf-8")
        if canonical != original:
            changed += 1
            if args.dry_run:
                print(f"WOULD CHANGE: {f}")
            else:
                f.write_text(canonical, encoding="utf-8")
                print(f"CHANGED: {f}")

    print()
    print(f"Files checked:      {checked}")
    print(f"Files changed:      {changed}")
    print(f"Files skipped:      {skipped}")
    if warnings:
        print()
        print(f"Warnings ({len(warnings)}):")
        for w in warnings:
            print(f"  - {w}")


if __name__ == "__main__":
    main()