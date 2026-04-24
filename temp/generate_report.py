import re
import html
from datetime import date
from pathlib import Path
from difflib import SequenceMatcher

root = Path('/Users/zlatomirvangelov/Documents/GitHub/Vangelov')

lines = (root / 'my.md').read_text(encoding='utf-8', errors='ignore').splitlines()
pat = re.compile(r'^\s*-\s*(case-study-[^\s]+\.html).*?https?://127\.0\.0\.1:\d+/Projects/([^\s)]+\.html)', re.I)
pairs = [(m.group(1).strip(), m.group(2).strip()) for ln in lines for m in [pat.search(ln)] if m]


def find_src(name: str):
    p = root / 'Resources' / 'New folder' / name
    if p.exists():
        return p
    hits = sorted(
        root.rglob(name),
        key=lambda x: (0 if 'Resources/New folder' in x.as_posix() else 1, len(x.as_posix())),
    )
    return hits[0] if hits else None


def norm(t: str) -> str:
    t = re.sub(r'<!--.*?-->', ' ', t, flags=re.S)
    t = re.sub(r'<script\b[^>]*>.*?</script\s*>', ' ', t, flags=re.I | re.S)
    t = re.sub(r'<style\b[^>]*>.*?</style\s*>', ' ', t, flags=re.I | re.S)
    t = re.sub(r'<[^>]+>', ' ', t)
    t = html.unescape(t).lower()
    return re.sub(r'\s+', ' ', t).strip()


rows = []
exact = 0
missing = []

for source_name, target_name in pairs:
    src = find_src(source_name)
    tgt = root / 'Projects' / target_name

    src_exists = bool(src and src.exists())
    tgt_exists = tgt.exists()

    if not src_exists or not tgt_exists:
        missing.append((source_name, target_name, src_exists, tgt_exists))
        rows.append((source_name, target_name, None, None, src_exists, tgt_exists))
        continue

    src_text = norm(src.read_text(encoding='utf-8', errors='ignore'))
    tgt_text = norm(tgt.read_text(encoding='utf-8', errors='ignore'))

    is_exact = src_text == tgt_text
    similarity = round(SequenceMatcher(None, src_text, tgt_text).ratio() * 100, 2)

    if is_exact:
        exact += 1

    rows.append((source_name, target_name, is_exact, similarity, src_exists, tgt_exists))

rows_sorted = sorted([r for r in rows if r[3] is not None], key=lambda x: x[3])

report = []
report.append('# Case Study Text Parity Report')
report.append('')
report.append(f'Date: {date.today().isoformat()}')
report.append('')
report.append(f'- Total mapped pairs: **{len(pairs)}**')
report.append(f'- Exact 1:1 matches: **{exact}**')
report.append(f'- Non-exact: **{len(pairs) - exact}**')
report.append(f'- Missing files: **{len(missing)}**')
report.append('')
report.append('## Ranked by mismatch (lowest similarity first)')
report.append('')
report.append('| # | Source | Project | Exact | Similarity % |')
report.append('|---:|---|---|:---:|---:|')

for i, (source_name, target_name, is_exact, similarity, _, _) in enumerate(rows_sorted, 1):
    mark = 'YES' if is_exact else 'NO'
    report.append(f'| {i} | {source_name} | {target_name} | {mark} | {similarity:.2f} |')

if missing:
    report.append('')
    report.append('## Missing files')
    report.append('')
    for source_name, target_name, src_exists, tgt_exists in missing:
        report.append(
            f'- {source_name} -> {target_name} (source_exists={src_exists}, target_exists={tgt_exists})'
        )

(root / 'report.md').write_text('\n'.join(report) + '\n', encoding='utf-8')
print(f'WROTE {root / "report.md"}')
print(f'PAIRS={len(pairs)} EXACT={exact} MISSING={len(missing)}')
