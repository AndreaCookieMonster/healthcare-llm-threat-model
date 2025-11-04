# Detect near-duplicate headings/paragraphs across Markdown files.
import glob, os, re, itertools, difflib, sys
def chunks(md):
    # return (file, lineno, kind, text)
    lines = md.splitlines()
    out = []
    in_list = False
    for i, line in enumerate(lines, 1):
        if re.match(r'^\s*#{1,6}\s+\S', line):
            in_list = False
            out.append(("h", i, line.strip()))
        elif line.strip() and line.lstrip().startswith(("-", "*")):
            in_list = True
            continue
        elif line.strip() and in_list and line.startswith(" "):
            continue
        elif line.strip() and not line.lstrip().startswith((">", "```", "|", "[")):
            in_list = False
            out.append(("p", i, re.sub(r'\s+', ' ', line.strip())))
    return out
files = sorted([p for p in glob.glob("**/*.md", recursive=True) if "/node_modules/" not in p and "/_site/" not in p])
blobs = []
for f in files:
    with open(f, "r", encoding="utf-8", errors="ignore") as fh:
        raw = fh.read()
    if raw.startswith("---"):
        parts = raw.split("---", 2)
        if len(parts) == 3:
            raw = parts[2]
    for kind, ln, txt in chunks(raw):
            if len(txt) >= 40:
                blobs.append((f, ln, kind, txt[:400]))
pairs = []
for (i, a), (j, b) in itertools.combinations(enumerate(blobs), 2):
    r = difflib.SequenceMatcher(None, a[3].lower(), b[3].lower()).ratio()
    if r >= 0.90:
        pairs.append((r, a, b))
pairs.sort(reverse=True)
bad = []
for r, a, b in pairs[:300]:
    bad.append(f"{r:.2f} | {a[0]}:{a[1]} ({a[2]}) == {b[0]}:{b[1]} ({b[2]})")
if bad:
    print("NEAR_DUPLICATES_DETECTED")
    for line in bad: print(line)
    sys.exit(2)
else:
    print("NO_DUPLICATES")
