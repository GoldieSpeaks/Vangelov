import re
from pathlib import Path
from datetime import date

ROOT = Path('/Users/zlatomirvangelov/Documents/GitHub/Vangelov')
MY_MD = ROOT / 'my.md'

PAIR_RE = re.compile(r'^\s*-\s*(case-study-[^\s]+\.html).*?https?://127\.0\.0\.1:\d+/Projects/([^\s)]+\.html)', re.I)

CRITICAL_TAGS = [
    'section', 'h1', 'h2', 'h3', 'h4', 'table', 'thead', 'tbody', 'tr',
    'svg', 'img', 'ul', 'ol', 'li', 'blockquote'
]


def find_source(name: str):
    p = ROOT / 'Resources' / 'New folder' / name
    if p.exists():
        return p
    hits = sorted(
        ROOT.rglob(name),
        key=lambda x: (0 if 'Resources/New folder' in x.as_posix() else 1, len(x.as_posix()))
    )
    return hits[0] if hits else None


def read_pairs():
    pairs = []
    for line in MY_MD.read_text(encoding='utf-8', errors='ignore').splitlines():
        m = PAIR_RE.search(line)
        if m:
            pairs.append((m.group(1).strip(), m.group(2).strip()))
    return pairs


def strip_non_content(html: str) -> str:
    html = re.sub(r'(?is)<!--.*?-->', ' ', html)
    html = re.sub(r'(?is)<script\b[^>]*>.*?</script\s*>', ' ', html)
    html = re.sub(r'(?is)<style\b[^>]*>.*?</style\s*>', ' ', html)
    return html


def tag_count(html: str, tag: str) -> int:
    return len(re.findall(rf'(?is)<{tag}\b', html))


def get_counts(html: str):
    html = strip_non_content(html)
    return {t: tag_count(html, t) for t in CRITICAL_TAGS}


def evaluate(src_counts, tgt_counts):
    missing = []
    for tag in CRITICAL_TAGS:
        if tgt_counts.get(tag, 0) < src_counts.get(tag, 0):
            missing.append((tag, src_counts[tag], tgt_counts[tag]))
    return missing


def main():
    pairs = read_pairs()
    rows = []
    ok_count = 0

    for src_name, tgt_name in pairs:
        src_path = find_source(src_name)
        tgt_path = ROOT / 'Projects' / tgt_name

        if not src_path or not tgt_path.exists():
            rows.append({
                'source': src_name,
                'target': tgt_name,
                'status': 'MISSING_FILE',
                'missing_tags': []
            })
            continue

        src_html = src_path.read_text(encoding='utf-8', errors='ignore')
        tgt_html = tgt_path.read_text(encoding='utf-8', errors='ignore')
        src_counts = get_counts(src_html)
        tgt_counts = get_counts(tgt_html)

        missing_tags = evaluate(src_counts, tgt_counts)
        status = 'OK' if not missing_tags else 'MISSING_ELEMENTS'
        if status == 'OK':
            ok_count += 1

        rows.append({
            'source': src_name,
            'target': tgt_name,
            'status': status,
            'missing_tags': missing_tags,
        })

    report = []
    report.append('# Case Study Structure & Element Coverage Report')
    report.append('')
    report.append(f'Date: {date.today().isoformat()}')
    report.append('')
    report.append(f'- Total mapped pairs: **{len(pairs)}**')
    report.append(f'- Full structural coverage (critical tags): **{ok_count}**')
    report.append(f'- With missing structural elements: **{len(pairs) - ok_count}**')
    report.append('')
    report.append('Validation rule: target must contain at least the same count as source for critical tags.')
    report.append('Critical tags: ' + ', '.join(CRITICAL_TAGS))
    report.append('')
    report.append('## Results')
    report.append('')

    for i, r in enumerate(rows, 1):
        report.append(f"### {i}. {r['source']} → {r['target']}")
        report.append(f"- Status: **{r['status']}**")
        if r['missing_tags']:
            report.append('- Missing/lower-count tags:')
            for tag, src_n, tgt_n in r['missing_tags']:
                report.append(f'  - `{tag}`: source={src_n}, target={tgt_n}')
        report.append('')

    out = ROOT / 'report-structure.md'
    out.write_text('\n'.join(report), encoding='utf-8')
    print(f'WROTE {out}')
    print(f'TOTAL={len(pairs)} OK={ok_count} FAIL={len(pairs)-ok_count}')


if __name__ == '__main__':
    main()
