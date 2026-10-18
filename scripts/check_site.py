"""Check the actual Jekyll output before previewing or deploying it.

This intentionally uses only Python's standard library so the same checks can
run locally and in GitHub Actions. It checks local assets and document links,
unrendered template syntax, and the private-content exclusions for this site.
"""

from html.parser import HTMLParser
import argparse
from pathlib import Path
import re
from urllib.parse import unquote, urlsplit


class PageLinks(HTMLParser):
    """Collect references and text without treating markup as visible copy."""

    def __init__(self):
        super().__init__()
        self.links = []
        self.text = []
        self.private_sections = []
        self.private_links = []

    def handle_starttag(self, tag, attrs):
        attributes = dict(attrs)
        if tag == "div":
            self.private_sections.append(attributes.get("data-visibility") == "private")
        if tag == "a" and any(self.private_sections):
            self.private_links.append(attributes.get("href", ""))
        self.links.extend(value for key, value in attrs if key in {"href", "src"} and value)

    def handle_endtag(self, tag):
        if tag == "div" and self.private_sections:
            self.private_sections.pop()

    def handle_data(self, data):
        self.text.append(data)


def check_site(root, baseurl=""):
    """Validate a finished site, failing with actionable file-specific errors.

    Absolute internal paths are resolved relative to the build root; relative
    paths are resolved against their containing page. External URLs and mailto
    links are intentionally left to the publisher, avoiding network-dependent
    or privacy-sensitive checks in CI.
    """
    root = root.resolve()
    pages = sorted(root.rglob("*.html"))
    errors = []
    required = ["index.html", "publications/index.html", "software/index.html", "cv/index.html", "contact/index.html", "404.html"]
    errors.extend(f"Missing page: {name}" for name in required if not (root / name).is_file())
    for page in pages:
        raw = page.read_text(encoding="utf-8-sig")
        if "{%" in raw or "{{" in raw:
            errors.append(f"Unrendered Liquid in {page.relative_to(root)}")
        parsed = PageLinks()
        parsed.feed(raw)
        if parsed.private_links:
            errors.append(f"Private software entry contains a link: {page.relative_to(root)}")
        text = " ".join(parsed.text).casefold()
        forbidden = ["super-memory", "tilt-invariant", "research statement", "phd project", "ph.d. project", "158 8969", "1588969", "wechat", "none@example.org", "your sidebar name", "red brick university"]
        errors.extend(f"Excluded content {term!r}: {page.relative_to(root)}" for term in forbidden if term in text)
        for link in parsed.links:
            parts = urlsplit(link)
            if parts.scheme or parts.netloc or not parts.path:
                continue
            path = unquote(parts.path)
            if baseurl and path.startswith(baseurl.rstrip("/") + "/"):
                path = path[len(baseurl.rstrip("/")):]
            target = root / path.lstrip("/") if path.startswith("/") else page.parent / path
            if target.is_dir():
                target /= "index.html"
            if not target.is_file():
                errors.append(f"Broken local reference in {page.relative_to(root)}: {link}")
    for path in root.rglob("*"):
        if path.is_file() and (path.suffix.lower() in {".docx", ".pptx", ".pdf", ".7z"} or any(part in {".build-tools", ".qa", "Application", "scripts"} for part in path.parts)):
            errors.append(f"Non-public file in build: {path.relative_to(root)}")
    publications = root / "publications/index.html"
    if publications.is_file() and len(re.findall(r'class="publication-entry"', publications.read_text(encoding="utf-8"))) != 3:
        errors.append("The publications page must contain exactly the three supplied published papers.")
    for name in ["publications/index.html", "cv/index.html"]:
        page = root / name
        if page.is_file() and "CN 116165187 B" not in page.read_text(encoding="utf-8"):
            errors.append(f"Verified patent missing from {name}")
    if errors:
        raise SystemExit("\n".join(errors))
    print(f"PASS: {len(pages)} HTML pages; local references, publication count, template rendering, and content exclusions.")


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--baseurl", default="", help="GitHub project-site prefix, if applicable")
    args = parser.parse_args()
    check_site(Path(__file__).resolve().parents[1] / "_site", args.baseurl)
