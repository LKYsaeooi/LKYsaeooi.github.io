"""Package the editable source and a double-clickable offline preview.

The preview is derived from Jekyll's actual output. Only internal href/src paths
are rewritten for file-based navigation; content and styles stay unchanged.
Build tools, original application documents and QA files never enter archives.
"""

import os
from pathlib import Path
import re
import shutil
from urllib.parse import urlsplit
from zipfile import ZIP_DEFLATED, ZipFile


def make_preview(source, destination):
    """Copy built pages and convert root-relative references to portable paths."""
    shutil.copytree(source, destination, dirs_exist_ok=True)
    for page in destination.rglob("*.html"):
        def relative_reference(match):
            attribute, url = match.groups()
            parts = urlsplit(url)
            path = destination / parts.path.lstrip("/")
            if path.is_dir():
                path /= "index.html"
            relative = Path(os.path.relpath(path, page.parent)).as_posix()
            suffix = ("?" + parts.query if parts.query else "") + ("#" + parts.fragment if parts.fragment else "")
            return f'{attribute}="{relative}{suffix}"'
        raw = page.read_text(encoding="utf-8-sig")
        raw = re.sub(r'(href|src)="(/(?!/)[^"]*)"', relative_reference, raw)
        page.write_text(raw, encoding="utf-8")


def archive_tree(root, output, excluded=()):
    """Write a bounded archive, preserving hidden deployment configuration."""
    count = 0
    with ZipFile(output, "w", ZIP_DEFLATED) as archive:
        for directory, folders, files in os.walk(root):
            # Exclude build/dependency directories only at the project root;
            # preserve the upstream theme's nested _sass/vendor source files.
            folders[:] = sorted(folder for folder in folders if not (
                (Path(directory) == root and folder in excluded)
                or folder in {"__pycache__", ".git"}
            ))
            for name in sorted(files):
                if name in excluded:
                    continue
                path = Path(directory) / name
                archive.write(path, path.relative_to(root).as_posix())
                count += 1
    print(f"Packaged {output.name}: {count} files")


if __name__ == "__main__":
    site = Path(__file__).resolve().parents[1]
    built = site / "_site"
    if not (built / "index.html").is_file():
        raise SystemExit("Build Jekyll before packaging.")
    preview = site / ".preview"
    make_preview(built, preview)
    archive_tree(preview, site.parent / "Kaiyuan-Li-website-preview.zip")
    archive_tree(site, site.parent / "Kaiyuan-Li-website-source.zip", {"_site", ".preview", ".build-tools", ".qa", ".bundle", ".git", ".jekyll-cache", ".jekyll-metadata", ".sass-cache", "vendor", "__pycache__", "Gemfile.lock"})
