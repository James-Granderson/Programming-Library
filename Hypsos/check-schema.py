#!/usr/bin/env python3

from pathlib import Path


# ============================================================
# HYPSOS
# Check → Store → Compare → Append → Report
# ============================================================

LIBRARY = Path("/Users/badbwoyasapyvxx/Programming Library")
SCHEMA = LIBRARY / "Schema"
HYPSOS = LIBRARY / "Hypsos"


SCHEMA_FILES = {
    "Concept": SCHEMA / "CONCEPTS.md",
    "Action": SCHEMA / "ACTIONS.md",
    "Classification": SCHEMA / "CLASSIFICATIONS.md",
    "Environment": SCHEMA / "ENVIRONMENTS.md",
    "Path Type": SCHEMA / "PATH_TYPES.md",
    "Tag": SCHEMA / "TAGS.md",
}


# ============================================================
# STORE
# ============================================================

seen = {
    "Concept": {},
    "Action": {},
    "Classification": {},
    "Environment": {},
    "Path Type": {},
    "Tag": {},
}


# ====================================================
# CHECK
# ============================================================

def store(field, value, source):
    if not value:
        return

    if value not in seen[field]:
        seen[field][value] = source


def read_metadata(file):
    metadata = {}

    fields = [
        "Concept",
        "Action",
        "Classification",
        "Environment",
        "Path Type",
        "Tags",
    ]

    for line in file.read_text().splitlines():
        for field in fields:
            prefix = f"**{field}:**"

            if line.startswith(prefix):
                metadata[field] = line[len(prefix):].strip()

    return metadata


def scan_library():
    files_checked = 0
    entries_recognized = 0

    for file in LIBRARY.rglob("*.md"):

        if SCHEMA in file.parents:
            continue

        if HYPSOS in file.parents:
            continue

        files_checked += 1

        metadata = read_metadata(file)

        if not metadata:
            continue

        entries_recognized += 1

        source = file.relative_to(LIBRARY)

        if "Concept" in metadata:
            store("Concept", metadata["Concept"], source)

        if "Action" in metadata:
            store("Action", metadata["Action"], source)

        if "Classification" in metadata:
            store("Classification", metadata["Classification"], source)

        if "Environment" in metadata:
            store("Environment", metadata["Environment"], source)

        if "Path Type" in metadata:
            store("Path Type", metadata["Path Type"], source)

        if "Tags" in metadata:
            for tag in metadata["Tags"].split(","):
                tag = tag.strip()

                if tag:
                    store("Tag", tag, source)

    return files_checked, entries_recognized


# ============================================================
# COMPARE
# ============================================================

def read_schema(schema_file):
    values = set()

    if not schema_file.exists():
        return values

    for line in schema_file.read_text().splitlines():
        line = line.strip()

        if line.startswith("- "):
            values.add(line[2:].strip())

    return values


def find_missing():
    missing = {}

    for field, values in seen.items():
        schema_values = read_schema(SCHEMA_FILES[field])

        missing[field] = {
            value: source
            for value, source in values.items()
            if value not in schema_values
        }

    return missing


# ============================================================
# APPEND
# ============================================================
def append_missing(missing):
    total = 0

    for field, values in missing.items():

        if not values:
            continue

        schema_file = SCHEMA_FILES[field]
        schema_target = schema_file.relative_to(LIBRARY)

        with schema_file.open("a") as file:
            for value in sorted(values):
                source = values[value]

                file.write(f"- {value}\n")

                print(f"  + {field}: {value}")
                print(f"    Source: {source}")
                print(f"    Missing from: {schema_target}")
                print(f"    Appended to: {schema_target}")
                print()

                total += 1

    return total


# ============================================================
# REPORT
# ============================================================

def report(missing, files_checked, entries_recognized, total_added):
    print()
    print("Files checked:", files_checked)
    print("Entries recognized:", entries_recognized)

    print()
    print("Schema comparison:")

    for field in SCHEMA_FILES:
        if missing[field]:
            print(f"  {field}: {len(missing[field])} missing")
        else:
            print(f"  {field}: PASS")

    print()
    print("Changes:")

    if total_added == 0:
        print("  None")
        print()
        print("Hypsos: schema already synchronized")
    else:
        print()
        print(f"Hypsos: {total_added} schema entries appended")

    print()
    print("Hypsos: scan complete")


# ============================================================
# MAIN
# ============================================================

def main():
    print("Hypsos: scan started")
    print()

    files_checked, entries_recognized = scan_library()

    print("Hypsos: comparing against schema...")
    
    missing = find_missing()

    print()
    print("Hypsos: changes detected:")

    total_added = append_missing(missing)

    report(
        missing,
        files_checked,
        entries_recognized,
        total_added,
    )


if __name__ == "__main__":
    main()
