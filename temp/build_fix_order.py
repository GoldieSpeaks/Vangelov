import re
from pathlib import Path

root = Path('/Users/zlatomirvangelov/Documents/GitHub/Vangelov')
content_report = (root / 'report-content.md').read_text(encoding='utf-8', errors='ignore')

blocks = re.split(r'\n###\s+\d+\.\s+', content_report)
items = []
for b in blocks[1:]:
    header, *rest = b.split('\n')
    m = re.match(r'(case-study-[^\s]+\.html)\s+→\s+([^\s]+\.html)', header.strip())
    if not m:
        continue
    source, target = m.group(1), m.group(2)

    ms = re.search(r'Missing narrative snippets:\s+\*\*(\d+)\s*/\s*(\d+)\*\*', b)
    missing = int(ms.group(1)) if ms else 0
    total = int(ms.group(2)) if ms else 1
    ratio = missing / total if total else 0

    mv_count = len(re.findall(r'^\s*-\s+[a-z_]+\s*$', b, flags=re.M))
    # In this file bullet lines under "Missing content element types" are simple tokens like chart_or_graph

    score = ratio * 100 + mv_count * 10

    if score >= 95:
        priority = 'P0'
    elif score >= 80:
        priority = 'P1'
    elif score >= 65:
        priority = 'P2'
    else:
        priority = 'P3'

    items.append({
        'source': source,
        'target': target,
        'missing': missing,
        'total': total,
        'ratio_pct': ratio * 100,
        'visual_gaps': mv_count,
        'score': score,
        'priority': priority,
    })

items.sort(key=lambda x: x['score'], reverse=True)

lines = []
lines.append('## Content Fix Order (highest risk first)')
lines.append('')
lines.append('Basis: missing narrative ratio + penalty for missing visual/analytical elements.')
lines.append('')
lines.append('| Priority | Source | Project | Missing snippets | Missing visual types | Risk score |')
lines.append('|---|---|---|---:|---:|---:|')
for it in items:
    lines.append(
        f"| {it['priority']} | {it['source']} | {it['target']} | {it['missing']}/{it['total']} ({it['ratio_pct']:.1f}%) | {it['visual_gaps']} | {it['score']:.1f} |"
    )

(root / 'temp' / 'fix_order_section.md').write_text('\n'.join(lines) + '\n', encoding='utf-8')
print(f"WROTE {root / 'temp' / 'fix_order_section.md'}")
