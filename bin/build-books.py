#!/usr/bin/env python3
"""Build the EPUB and PDF of each volume from the Markdown chapters.

Chapters are read in the order manifest.json lists them, which is the
reading order. Needs pandoc and, for the PDF, WeasyPrint. Run from the
repo root:

    python3 bin/build-books.py            # writes build/*.epub and build/*.pdf
    python3 bin/build-books.py --epub-only
"""

import json
import os
import re
import shutil
import subprocess
import sys
import tempfile
import urllib.parse

VOLUMES = [
    {
        "dir": "milestones-vol-1",
        "file": "Milestones-The-Story-of-WordPress",
        "title": "Milestones: The Story of WordPress",
        "author": "WordPress contributors",
        "date": "2015",
        "cover": "milestones-vol-1/Resources/illustrations/exports/Cover.png",
        # Chapters already use ## headings, under # Part headings added below.
        "shift": 0,
    },
    {
        "dir": "milestones-vol-2",
        "file": "Building-Blocks-The-Evolution-of-WordPress",
        "title": "Building Blocks: The Evolution of WordPress",
        "author": "Rebecca Haden",
        "date": "2023",
        "cover": "milestones-vol-2/Resources/cover.png",
        # No parts, so ## chapter headings move up to #.
        "shift": -1,
    },
]

PART_NAMES = ["One", "Two", "Three", "Four", "Five", "Six"]
OUT = "build"
CSS = "bin/book.css"


def absolute_paths(text, chapter_dir):
    """Point relative image paths at the files, since chapters move to a temp dir."""

    def fix(path):
        if re.match(r"^([a-z]+:)?//", path, re.I) or path.startswith("/"):
            return path
        return os.path.abspath(os.path.join(chapter_dir, urllib.parse.unquote(path)))

    text = re.sub(r'(<img\s[^>]*src=")([^"]+)"', lambda m: m.group(1) + fix(m.group(2)) + '"', text)
    text = re.sub(r"(!\[[^\]]*\]\()([^)\s]+)", lambda m: m.group(1) + fix(m.group(2)), text)
    # EPUB only accepts whole numbers for image sizes, so "600px" becomes "600".
    return re.sub(r'\b(width|height)="(\d+)px"', r'\1="\2"', text)


def chapter_files(volume, manifest, tmp):
    """Write each chapter, plus Part headings, as its own file in reading order."""
    files = []
    part = None
    for doc in manifest.values():
        path = urllib.parse.unquote(doc["markdown_source"])
        if not path.startswith(volume["dir"] + "/"):
            continue

        with open(path, encoding="utf-8") as f:
            text = f.read().strip()

        # Drop the volume title that opens each Volume 2 chapter.
        text = re.sub(r"\A#\s[^\n]*\n", "", text).lstrip()
        if not text.startswith("#"):
            text = f"## {doc['title']}\n\n{text}"

        match = re.search(r"/Part (\d+)/", path)
        if match:
            # Mark the chapter heading so the PDF starts each chapter on a new page.
            heading, rest = text.split("\n", 1)
            text = heading.rstrip() + " {.chapter}\n" + rest
        if match and match.group(1) != part:
            part = match.group(1)
            files.append(write(tmp, len(files), f"# Part {PART_NAMES[int(part) - 1]}\n"))
        elif not match and volume["shift"] == 0:
            # The Introduction sits outside the parts, at the top level.
            text = re.sub(r"\A##\s", "# ", text)

        # Every chapter numbers its notes from 1, so make the labels unique.
        n = len(files)
        text = re.sub(r"\[\^([^\]]+)\]", lambda m: f"[^{n}-{m.group(1)}]", text)

        files.append(write(tmp, n, absolute_paths(text, os.path.dirname(path)) + "\n"))
    return files


def write(tmp, index, text):
    path = os.path.join(tmp, f"{index:03d}.md")
    with open(path, "w", encoding="utf-8") as f:
        f.write(text)
    return path


def pandoc(volume, files, output, extra):
    args = [
        "pandoc",
        "--from=markdown+raw_html-implicit_figures",
        f"--shift-heading-level-by={volume['shift']}",
        "--toc",
        "--toc-depth=2",
        f"--metadata=title:{volume['title']}",
        f"--metadata=author:{volume['author']}",
        f"--metadata=date:{volume['date']}",
        "--metadata=lang:en",
        "--metadata=rights:Dual-licensed under GPLv2 and CC BY-SA 4.0",
        f"--output={output}",
        *extra,
        *files,
    ]
    subprocess.run(args, check=True)
    print(f"built {output}")


def main():
    epub_only = "--epub-only" in sys.argv
    with open("manifest.json", encoding="utf-8") as f:
        manifest = json.load(f)

    os.makedirs(OUT, exist_ok=True)
    for volume in VOLUMES:
        tmp = tempfile.mkdtemp()
        try:
            files = chapter_files(volume, manifest, tmp)
            base = os.path.join(OUT, volume["file"])
            split = "2" if volume["shift"] == 0 else "1"
            pandoc(volume, files, base + ".epub", [f"--epub-cover-image={volume['cover']}", f"--split-level={split}"])
            if not epub_only:
                cover = os.path.join(tmp, "cover.html")
                with open(cover, "w", encoding="utf-8") as f:
                    f.write(f'<div class="cover"><img src="{os.path.abspath(volume["cover"])}" alt="" /></div>\n')
                pandoc(
                    volume,
                    files,
                    base + ".pdf",
                    [
                        "--to=html5",
                        "--standalone",
                        "--embed-resources",
                        f"--css={CSS}",
                        f"--include-before-body={cover}",
                        # Notes at the end of each part or chapter, not the whole book.
                        "--reference-location=section",
                        "--pdf-engine=weasyprint",
                    ],
                )
        finally:
            shutil.rmtree(tmp)


if __name__ == "__main__":
    main()
