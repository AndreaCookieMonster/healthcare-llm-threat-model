#!/usr/bin/env python3
"""Update internal links to include the Jekyll baseurl."""
from __future__ import annotations

import re
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
TARGET_SUFFIXES = {".md", ".markdown", ".mdown", ".html"}
EXCLUDED_DIRS = {"_site"}

MARKDOWN_LINK_RE = re.compile(r"(?P<prefix>!?)\[(?P<text>[^\]]+)\]\((?P<link>[^)]+)\)")
HTML_HREF_RE = re.compile(r"href=(?P<quote>['\"])(?P<link>[^'\"]+)(?P=quote)")
YAML_URL_RE = re.compile(r"^(?P<indent>\s*(?:-\s*)?url:\s*)(?P<quote>['\"]?)(?P<link>[^'\"\n]+)(?P=quote)", re.MULTILINE)

EXTERNAL_PREFIXES = ("http://", "https://", "mailto:")
BASEURL_TOKEN = "{{ site.baseurl }}"


def should_skip_path(path: Path) -> bool:
    parts = path.parts
    return any(part in EXCLUDED_DIRS for part in parts)


def needs_baseurl(link: str) -> bool:
    if not link:
        return False
    stripped = link.strip()
    lower = stripped.lower()
    if stripped.startswith(BASEURL_TOKEN) or stripped.startswith("{{") or stripped.startswith("{%"):
        return False
    if lower.startswith(EXTERNAL_PREFIXES) or stripped.startswith("#"):
        return False
    return stripped.startswith("/") or stripped.startswith("threats/")


def transform_link(link: str) -> str:
    stripped = link.strip()
    if stripped.startswith("/"):
        remainder = stripped.lstrip("/")
    elif stripped.startswith("threats/"):
        remainder = stripped
    else:
        return link
    new_link = f"{BASEURL_TOKEN}/{remainder}" if remainder else BASEURL_TOKEN
    # Preserve any leading/trailing whitespace from the original value
    prefix_len = len(link) - len(link.lstrip())
    suffix_len = len(link) - len(link.rstrip())
    prefix = link[:prefix_len]
    suffix = link[len(link) - suffix_len :]
    return f"{prefix}{new_link}{suffix}"


def replace_markdown_links(text: str) -> tuple[str, bool]:
    changed = False

    def _repl(match: re.Match[str]) -> str:
        nonlocal changed
        if match.group("prefix") == "!":
            return match.group(0)
        link = match.group("link")
        if needs_baseurl(link):
            changed = True
            new_link = transform_link(link)
            return f"[{match.group('text')}]({new_link})"
        return match.group(0)

    return MARKDOWN_LINK_RE.sub(_repl, text), changed


def replace_html_links(text: str) -> tuple[str, bool]:
    changed = False

    def _repl(match: re.Match[str]) -> str:
        nonlocal changed
        link = match.group("link")
        if needs_baseurl(link):
            changed = True
            new_link = transform_link(link)
            return f"href={match.group('quote')}{new_link}{match.group('quote')}"
        return match.group(0)

    return HTML_HREF_RE.sub(_repl, text), changed


def replace_yaml_urls(text: str) -> tuple[str, bool]:
    changed = False

    def _repl(match: re.Match[str]) -> str:
        nonlocal changed
        link = match.group("link")
        if needs_baseurl(link):
            changed = True
            new_link = transform_link(link)
            return f"{match.group('indent')}{match.group('quote')}{new_link}{match.group('quote')}"
        return match.group(0)

    return YAML_URL_RE.sub(_repl, text), changed


def process_file(path: Path) -> bool:
    original = path.read_text(encoding="utf-8")
    updated = original
    changed = False
    if path.suffix.lower() in {".md", ".markdown", ".mdown"}:
        updated, yaml_changed = replace_yaml_urls(updated)
        changed = changed or yaml_changed
        updated, md_changed = replace_markdown_links(updated)
        changed = changed or md_changed
    if path.suffix.lower() == ".html":
        updated, html_changed = replace_html_links(updated)
        changed = changed or html_changed
    if changed and updated != original:
        path.write_text(updated, encoding="utf-8")
    return changed


def main() -> None:
    changed_files: list[Path] = []
    for path in ROOT.rglob("*"):
        if path.is_file() and path.suffix.lower() in TARGET_SUFFIXES and not should_skip_path(path.relative_to(ROOT)):
            if process_file(path):
                changed_files.append(path)
    if changed_files:
        print("Updated baseurl links in:")
        for path in changed_files:
            print(f" - {path.relative_to(ROOT)}")
    else:
        print("No files required baseurl updates.")


if __name__ == "__main__":
    main()
