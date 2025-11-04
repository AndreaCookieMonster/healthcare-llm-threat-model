import re
import sys
import pathlib
import requests

FILE_GLOBS = ["**/*.md", "**/*.html"]
URL_RE = re.compile(r'(?P<url>https?://[^\s)>"\'`]+)')


def iter_files(root):
    for glob in FILE_GLOBS:
        for path in pathlib.Path(root).glob(glob):
            if path.is_file() and ".git" not in path.parts and "_site" not in path.parts:
                yield path


def try_https(url):
    if url.startswith("http://"):
        https_url = "https://" + url[len("http://"):]
        try:
            response = requests.get(https_url, timeout=10, allow_redirects=True)
            if response.ok:
                return response.url
        except Exception:
            pass
    return None


def final_url(url):
    try:
        response = requests.get(url, timeout=12, allow_redirects=True)
        if response.ok:
            return response.url
    except Exception:
        pass
    return None


def rewrite_file(path):
    text = path.read_text(encoding="utf-8", errors="ignore")
    changed = False

    def replace(match):
        nonlocal changed
        url = match.group("url")
        https_url = try_https(url)
        if https_url and https_url != url:
            changed = True
            return https_url
        destination = final_url(url)
        if destination and destination != url:
            changed = True
            return destination
        return url

    new_text = URL_RE.sub(replace, text)
    if changed:
        path.write_text(new_text, encoding="utf-8")
    return changed


def main():
    root = pathlib.Path(".")
    touched = []
    for path in iter_files(root):
        if rewrite_file(path):
            touched.append(str(path))
    if touched:
        print("Updated links in:", *touched, sep="\n - ")
    else:
        print("No auto-fixable links found.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
