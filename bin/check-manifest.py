#!/usr/bin/env python3
"""Check manifest.json and chapter footnotes before they reach wordpress.org/book.

wordpress.org/book imports every chapter listed in manifest.json, so a
broken entry or footnote shows up on the live site. Run from the repo root:

    python3 bin/check-manifest.py
"""

import glob
import json
import re
import sys
import urllib.parse

errors = []

with open("manifest.json", encoding="utf-8") as f:
    manifest = json.load(f)

for key, doc in manifest.items():
    if doc.get("slug") != key:
        errors.append(f"{key}: slug must match the key")
    if not doc.get("title"):
        errors.append(f"{key}: missing title")
    source = doc.get("markdown_source", "")
    if "://" in source or source.startswith("/") or ".." in source:
        errors.append(f"{key}: markdown_source must be a path relative to manifest.json")
        continue
    path = urllib.parse.unquote(source)
    try:
        open(path, encoding="utf-8").close()
    except OSError:
        errors.append(f"{key}: {path} does not exist")

for path in sorted(glob.glob("milestones-vol-*/Content/**/*.md", recursive=True)):
    with open(path, encoding="utf-8") as f:
        text = f.read()
    refs = set(re.findall(r"\[\^([^\]]+)\](?!:)", text))
    note_list = re.findall(r"(?m)^\[\^([^\]]+)\]:", text)
    notes = set(note_list)
    for note in sorted({n for n in note_list if note_list.count(n) > 1}):
        errors.append(f"{path}: note [^{note}]: is defined more than once")
    for ref in sorted(refs - notes):
        errors.append(f"{path}: footnote [^{ref}] has no note")
    for note in sorted(notes - refs):
        errors.append(f"{path}: note [^{note}]: is never referenced")
    if re.search(r"\[(?:\^[A-Za-z]+-|[A-Za-z]+\^)\d+\]", text):
        errors.append(f"{path}: old footnote style, use [^1] and [^1]:")

if errors:
    print("\n".join(errors))
    sys.exit(1)

print(f"manifest.json: {len(manifest)} chapters OK, footnotes OK")
