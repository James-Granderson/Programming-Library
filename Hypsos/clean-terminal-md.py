#!/usr/bin/env python3

from pathlib import Path
import re


TERMINAL = Path(
    "/Users/badbwoyasapyvxx/Programming Library/Terminal"
)

METADATA = [
    "Concept",
    "Action",
    "Object",
    "Classification",
    "Environment",
    "Path Type",
    "Tags",
]

SECTIONS = [
    "What It Is",
    "What It Does",
    "How to Use",
    "Requirements",
    "Representation",
]


def clean_metadata(lines):
    """
    Repair only the known collapsed metadata corruption.

    Converts things like:

    ## **Concept:** Shell **Action:** Delete **Object:** rm
    **Classification:** Command **Environment:** Shell
    **Path Type:** N/A **Tags:** command

    into:

    **Concept:** Shell
    **Action:** Delete
    **Object:** rm
    **Classification:** Command
    **Environment:** Shell
    **Path Type:** N/A
    **Tags:** command
    """

    text = "\n".join(lines)

    marker = "**Concept:**"

    if marker not in text:
        return lines

    concept_position = text.find(marker)

    # Find the beginning of the corrupted metadata line.
    line_start = text.rfind("\n", 0, concept_position) + 1

    # Find the first real section after metadata.
    section_positions = []

    for section in SECTIONS:
        position = text.find(f"### {section}")

        if position != -1:
            section_positions.append(position)

    if not section_positions:
        return lines

    content_start = min(section_positions)

    metadata_block = text[line_start:content_start]

    extracted = {}

    for index, field in enumerate(METADATA):

        marker = f"**{field}:**"

        position = metadata_block.find(marker)

        if position == -1:
            continue

        value_start = position + len(marker)

        next_positions = []

        for next_field in METADATA[index + 1:]:
            next_marker = f"**{next_field}:**"

            next_position = metadata_block.find(
                next_marker,
                value_start,
            )

            if next_position != -1:
                next_positions.append(next_position)

        if next_positions:
            value_end = min(next_positions)
            value = metadata_block[
                value_start:value_end
            ].strip()
        else:
            value = metadata_block[value_start:].strip()

        value = value.strip()

        extracted[field] = value

    if not extracted:
        return lines

    metadata_lines = []

    for field in METADATA:

        if field in extracted:

            metadata_lines.append(
                f"**{field}:** {extracted[field]}"
            )

    before = text[:line_start].rstrip()
    after = text[content_start:].lstrip()

    rebuilt = (
        before
        + "\n\n"
        + "\n".join(metadata_lines)
        + "\n\n---\n\n"
        + after
    )

    return rebuilt.splitlines()


def clean_heading_duplicates(lines):
    """
    Remove duplicate Object text beneath the level-1 heading.

    Example:

        # `rm`
        rm

    becomes:

        # `rm`
    """

    if len(lines) < 2:
        return lines

    heading = lines[0].strip()

    if not heading.startswith("# "):
        return lines

    object_text = heading[2:].strip()

    if object_text.startswith("`") and object_text.endswith("`"):
        object_text = object_text[1:-1]

    second = lines[1].strip()

    if second == object_text:
        del lines[1]

    return lines


def clean_section_duplicates(lines):
    """
    Normalize section headings and remove the duplicate label
    immediately beneath them.

    Example:

        ### What It Is

        What It Is
        A definition...

    becomes:

        ### What It Is

        A definition...
    """

    result = []

    i = 0

    while i < len(lines):

        line = lines[i].strip()

        matched = None

        # Existing proper heading.
        for section in SECTIONS:

            if line == f"### {section}":
                matched = section
                break

        # Bare section label accidentally used as heading.
        if matched is None:

            for section in SECTIONS:

                if line == section:
                    matched = section
                    break

        if matched is None:

            result.append(lines[i])
            i += 1
            continue

        # Always normalize to the proper Markdown heading.
        result.append(f"### {matched}")

        i += 1

        # Remove ALL immediately following copies of the section name.
        while (
            i < len(lines)
            and lines[i].strip() == matched
        ):
            i += 1

    return result


def clean_representation_duplicate(lines):
    """
    Remove the duplicate literal 'Representation' if it appears
    immediately inside the Representation section.
    """

    result = []

    in_representation = False
    removed = False

    for line in lines:

        stripped = line.strip()

        if stripped == "### Representation":
            in_representation = True
            removed = False
            result.append(line)
            continue

        if (
            in_representation
            and not removed
            and stripped == "Representation"
        ):
            removed = True
            continue

        # A new section ends the representation heading context.
        if (
            stripped.startswith("### ")
            and stripped != "### Representation"
        ):
            in_representation = False

        result.append(line)

    return result


def clean_duplicate_object_everywhere(lines):
    """
    Specifically remove a bare object name immediately after
    the level-1 heading, including blank-line variants.
    """

    if not lines:
        return lines

    heading = lines[0].strip()

    if not heading.startswith("# "):
        return lines

    object_name = heading[2:].strip().strip("`")

    i = 1

    # Allow blank lines between heading and duplicate.
    while i < len(lines) and not lines[i].strip():
        i += 1

    if (
        i < len(lines)
        and lines[i].strip().strip("`") == object_name
    ):
        del lines[1:i + 1]

    return lines


def clean_extra_separators(lines):
    """
    Keep the metadata separator as one ---.
    Remove only immediately duplicated separators.
    """

    result = []

    previous_separator = False

    for line in lines:

        if line.strip() == "---":

            if previous_separator:
                continue

            previous_separator = True
            result.append("---")
            continue

        previous_separator = False
        result.append(line)

    return result


def clean_blank_lines(lines):
    """
    Prevent structural cleanup from leaving huge blank-line gaps.
    """

    result = []
    previous_blank = False

    for line in lines:

        if not line.strip():

            if previous_blank:
                continue

            result.append("")
            previous_blank = True

        else:

            result.append(line)
            previous_blank = False

    return result


def clean_file(path):

    original = path.read_text()

    lines = original.splitlines()

    # 1. Remove duplicate Object beneath heading.
    lines = clean_heading_duplicates(lines)

    # 2. Remove the same corruption even when separated by blanks.
    lines = clean_duplicate_object_everywhere(lines)

    # 3. Rebuild collapsed metadata.
    lines = clean_metadata(lines)

    # 4. Normalize section headings and remove duplicate labels.
    lines = clean_section_duplicates(lines)

    # 5. Remove duplicate Representation label.
    lines = clean_representation_duplicate(lines)

    # 6. Collapse duplicate --- separators.
    lines = clean_extra_separators(lines)

    # 7. Clean excessive blank lines.
    lines = clean_blank_lines(lines)

    cleaned = "\n".join(lines).rstrip() + "\n"

    if cleaned != original:
        path.write_text(cleaned)
        print(f"FIXED: {path.name}")
    else:
        print(f"UNCHANGED: {path.name}")


def main():

    if not TERMINAL.exists():
        raise SystemExit(
            f"Terminal directory not found: {TERMINAL}"
        )

    for path in sorted(TERMINAL.glob("*.md")):
        clean_file(path)

    print()
    print("Terminal duplicate cleanup complete.")


if __name__ == "__main__":
    main()
