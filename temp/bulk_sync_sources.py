from pathlib import Path
import re

root = Path('/Users/zlatomirvangelov/Documents/GitHub/Vangelov')
my_lines = (root / 'my.md').read_text(encoding='utf-8', errors='ignore').splitlines()
pattern = re.compile(r'^\s*-\s*(case-study-[^\s]+\.html).*?https?://127\.0\.0\.1:\d+/Projects/([^\s)]+\.html)', re.I)

pairs = []
for line in my_lines:
    m = pattern.search(line)
    if m:
        pairs.append((m.group(1).strip(), m.group(2).strip()))

updated = []
missing = []
for source_name, target_name in pairs:
    src = root / 'Resources' / 'New folder' / source_name
    if not src.exists():
        hits = sorted(root.rglob(source_name), key=lambda p: len(str(p)))
        src = hits[0] if hits else None

    tgt = root / 'Projects' / target_name

    if not src or not src.exists() or not tgt.exists():
        missing.append((source_name, target_name, bool(src and src.exists()), tgt.exists()))
        continue

    tgt.write_text(src.read_text(encoding='utf-8', errors='ignore'), encoding='utf-8')
    updated.append((source_name, target_name))

print(f'UPDATED={len(updated)}')
for s, t in updated:
    print(f'OK|{s}|{t}')
print(f'MISSING={len(missing)}')
for s, t, se, te in missing:
    print(f'MISS|{s}|{t}|src={se}|tgt={te}')
