import re, pathlib
MD = list(pathlib.Path(".").rglob("*.md")) + list(pathlib.Path(".").rglob("*.html"))
LINK = re.compile(r"\]\(((/(?!/)[^)#]+)(#[^)]+)?\))")
def to_liquid(path, frag):
    liquid = '{{ "' + path + '" | relative_url }}'
    return f"]({liquid}{frag or ''})"
for p in MD:
    if any(part.startswith("_site") for part in p.parts):
        continue
    txt = p.read_text(encoding="utf-8", errors="ignore")
    new = LINK.sub(lambda m: to_liquid(m.group(1), m.group(2) or ""), txt)
    if new != txt:
        p.write_text(new, encoding="utf-8")
        print("updated", p)
print("done")
