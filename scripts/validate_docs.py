#!/usr/bin/env python3
"""Validate structure, links, and images of the documentation archive."""

from __future__ import annotations

import os
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
DOCS = ROOT / "docs"

EXPECTED = {"triggers": 127, "conditions": 88, "actions": 219}
INDEX_FILES = {"README.md", "glossary.md", "faq.md"}

errors: list[str] = []
warnings: list[str] = []


def rel(path: Path) -> str:
    return path.relative_to(ROOT).as_posix()


def check_front_matter(path: Path) -> None:
    if path.name in INDEX_FILES:
        return
    text = path.read_text(encoding="utf-8")
    if not text.startswith("---\n"):
        errors.append(f"front matter hilang: {rel(path)}")
        return
    end = text.find("\n---\n", 4)
    if end == -1:
        errors.append(f"front matter tidak ditutup: {rel(path)}")
        return
    meta = text[4:end]
    for key in ("title", "source", "archived", "archive_url", "category"):
        if not re.search(rf"^{key}:", meta, re.M):
            errors.append(f"{rel(path)}: field '{key}' tidak ada")


def check_links(path: Path) -> None:
    text = path.read_text(encoding="utf-8")
    if re.search(r"\]\([^)]*_en\.html", text):
        errors.append(f"tautan lama *_en.html: {rel(path)}")
    for m in re.finditer(r"(?<!!)\[[^\]]*\]\(([^)\s]+)\)", text):
        target = m.group(1)
        if target.startswith(("http://", "https://", "mailto:", "#")):
            continue
        clean = target.split("#", 1)[0]
        if not clean:
            continue
        full = (path.parent / clean).resolve()
        if not full.exists():
            errors.append(f"tautan rusak: {rel(path)} -> {target}")
    for m in re.finditer(r"!\[[^\]]*\]\(([^)\s]+)\)", text):
        target = m.group(1)
        if target.startswith(("http://", "https://", "data:")):
            continue
        full = (path.parent / target).resolve()
        if not full.exists():
            errors.append(f"gambar hilang: {rel(path)} -> {target}")


def main() -> int:
    md_files = sorted(ROOT.rglob("*.md"))
    if not md_files:
        print("Tidak ada berkas Markdown.")
        return 1

    for path in md_files:
        if DOCS in path.parents:
            check_front_matter(path)
        check_links(path)

    titles: dict[str, str] = {}
    for folder, expected in EXPECTED.items():
        folder_path = DOCS / "components" / folder
        files = [p for p in folder_path.glob("*.md") if p.name != "README.md"]
        if len(files) != expected:
            errors.append(f"{folder}: {len(files)} berkas, seharusnya {expected}")
        index = folder_path / "README.md"
        if not index.exists():
            errors.append(f"indeks kategori hilang: {rel(index)}")
            continue
        index_text = index.read_text(encoding="utf-8")
        for path in files:
            text = path.read_text(encoding="utf-8")
            meta = text.split("\n---\n", 1)[0]
            match = re.search(r'^title:\s*"?([^"\n]+)"?', meta, re.M)
            title = match.group(1).strip() if match else path.stem
            if title in titles:
                errors.append(f"judul duplikat: '{title}' di {rel(path)} dan {titles[title]}")
            titles[title] = rel(path)
            if path.name not in index_text:
                errors.append(f"{rel(path)} tidak tertaut dari indeks kategori")

    image_files = list((DOCS / "assets").rglob("*.png"))
    if len(image_files) < 50:
        errors.append(f"gambar terlalu sedikit: {len(image_files)}")

    print(f"Berkas Markdown       : {len(md_files)}")
    print(f"Komponen              : {sum(EXPECTED.values())}")
    print(f"Gambar                : {len(image_files)}")
    print(f"Halaman tanpa judul   : {len(titles)}")
    print(f"Error                 : {len(errors)}")
    print(f"Peringatan            : {len(warnings)}")

    for item in errors[:50]:
        print("  ERROR:", item)
    for item in warnings[:20]:
        print("  WARN :", item)

    return 1 if errors else 0


if __name__ == "__main__":
    sys.exit(main())
