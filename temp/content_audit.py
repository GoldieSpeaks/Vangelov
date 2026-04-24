import re
import html
from pathlib import Path
from difflib import SequenceMatcher
from datetime import date

ROOT = Path('/Users/zlatomirvangelov/Documents/GitHub/Vangelov')
MY_MD = ROOT / 'my.md'

PAIR_RE = re.compile(r'^\s*-\s*(case-study-[^\s]+\.html).*?https?://127\.0\.0\.1:\d+/Projects/([^\s)]+\.html)', re.I)
HEADING_RE = re.compile(r'(?is)<h[1-4][^>]*>(.*?)</h[1-4]>')
TEXT_RE = re.compile(r'(?is)<(p|li|td|th|figcaption|blockquote)[^>]*>(.*?)</\1>')


def find_source(name: str):
    p = ROOT / 'Resources' / 'New folder' / name
    if p.exists():
        return p
    hits = sorted(ROOT.rglob(name), key=lambda x: (0 if 'Resources/New folder' in x.as_posix() else 1, len(x.as_posix())))
    return hits[0] if hits else None


def clean_inline_html(s: str) -> str:
    s = re.sub(r'(?is)<[^>]+>', ' ', s)
    s = html.unescape(s)
    s = re.sub(r'\s+', ' ', s).strip()
    return s


def preprocess_doc(raw: str) -> str:
    raw = re.sub(r'(?is)<!--.*?-->', ' ', raw)
    raw = re.sub(r'(?is)<script\b[^>]*>.*?</script\s*>', ' ', raw)
    raw = re.sub(r'(?is)<style\b[^>]*>.*?</style\s*>', ' ', raw)
    return raw


def extract_headings(raw: str):
    out = []
    for m in HEADING_RE.findall(raw):
        t = clean_inline_html(m)
        if t and len(t) >= 4:
            out.append(t)
    return out


def extract_content_snippets(raw: str):
    out = []
    for _, m in TEXT_RE.findall(raw):
        t = clean_inline_html(m)
        # ignore tiny/nav-like snippets
        if len(t.split()) >= 5:
            out.append(t)
    return out


def normalize_text(raw: str) -> str:
    raw = preprocess_doc(raw)
    raw = re.sub(r'(?is)<[^>]+>', ' ', raw)
    raw = html.unescape(raw).lower()
    return re.sub(r'\s+', ' ', raw).strip()


def fuzzy_contains(target_items, source_item, threshold=0.72):
    s = source_item.lower()
    best = 0.0
    for t in target_items:
        score = SequenceMatcher(None, s, t.lower()).ratio()
        if score > best:
            best = score
        if best >= threshold:
            return True, best
    return False, best


def find_missing_headings(src_h, tgt_h):
    missing = []
    for h in src_h:
        ok, best = fuzzy_contains(tgt_h, h, threshold=0.70)
        if not ok:
            missing.append((h, best))
    return missing


def find_missing_snippets(src_s, tgt_text_norm):
    # Match by phrase-presence of first 10-14 words from snippet
    missing = []
    for sn in src_s:
        words = re.findall(r"[a-zA-Z0-9']+", sn.lower())
        if len(words) < 7:
            continue
        probe = ' '.join(words[:12])
        if probe not in tgt_text_norm:
            # fallback fuzzy against whole target text chunk sample
            sample = ' '.join(words[:18])
            if SequenceMatcher(None, sample, tgt_text_norm[: min(len(tgt_text_norm), 12000)]).ratio() < 0.2:
                missing.append(sn)
    return missing


def visual_content_flags(raw: str):
    text = normalize_text(raw)
    lower_raw = raw.lower()

    flags = {
        'table': ('<table' in lower_raw) or (' table ' in f' {text} '),
        'chart_or_graph': any(k in text for k in ['chart', 'graph', 'kpi', 'metric', 'dashboard']),
        'timeline': 'timeline' in text,
        'architecture': any(k in text for k in ['architecture', 'diagram', 'flow']),
        'stakeholders': any(k in text for k in ['stakeholder', 'team', 'roles']),
        'testing_qa': any(k in text for k in ['testing', 'qa', 'quality assurance', 'test coverage']),
        'list_content': ('<ul' in lower_raw) or ('<ol' in lower_raw) or ('<li' in lower_raw),
    }
    return flags


def read_pairs():
    pairs = []
    for line in MY_MD.read_text(encoding='utf-8', errors='ignore').splitlines():
        m = PAIR_RE.search(line)
        if m:
            pairs.append((m.group(1).strip(), m.group(2).strip()))
    return pairs


def main():
    pairs = read_pairs()
    report_lines = []
    report_lines.append('# Case Study Content Coverage Report')
    report_lines.append('')
    report_lines.append(f'Date: {date.today().isoformat()}')
    report_lines.append('')
    report_lines.append('Definition used: content-wise presence of sections, narrative blocks, and visual/analytical elements (charts/graphs/tables/timeline/etc).')
    report_lines.append('')

    full_content_ok = 0
    results = []

    for src_name, tgt_name in pairs:
        src_path = find_source(src_name)
        tgt_path = ROOT / 'Projects' / tgt_name

        if not src_path or not tgt_path.exists():
            results.append({
                'source': src_name,
                'target': tgt_name,
                'status': 'MISSING_FILE',
                'missing_headings': ['file missing'],
                'missing_snippets_count': None,
                'missing_visual_flags': ['file missing'],
            })
            continue

        src_raw = preprocess_doc(src_path.read_text(encoding='utf-8', errors='ignore'))
        tgt_raw = preprocess_doc(tgt_path.read_text(encoding='utf-8', errors='ignore'))

        src_headings = extract_headings(src_raw)
        tgt_headings = extract_headings(tgt_raw)
        missing_headings = find_missing_headings(src_headings, tgt_headings)

        src_snippets = extract_content_snippets(src_raw)
        tgt_norm = normalize_text(tgt_raw)
        missing_snippets = find_missing_snippets(src_snippets, tgt_norm)

        src_flags = visual_content_flags(src_raw)
        tgt_flags = visual_content_flags(tgt_raw)
        missing_visual = [k for k, v in src_flags.items() if v and not tgt_flags.get(k, False)]

        # Conservative pass condition
        status = 'OK'
        if len(missing_headings) > 1 or len(missing_snippets) > max(3, int(0.35 * max(1, len(src_snippets)))) or missing_visual:
            status = 'PARTIAL_OR_MISSING_CONTENT'
        if status == 'OK':
            full_content_ok += 1

        results.append({
            'source': src_name,
            'target': tgt_name,
            'status': status,
            'missing_headings': missing_headings,
            'missing_snippets_count': len(missing_snippets),
            'source_snippets_count': len(src_snippets),
            'missing_visual_flags': missing_visual,
        })

    report_lines.append(f'- Total mapped pairs: **{len(pairs)}**')
    report_lines.append(f'- Full content coverage: **{full_content_ok}**')
    report_lines.append(f'- Partial/Missing content indicators: **{len(pairs) - full_content_ok}**')
    report_lines.append('')
    report_lines.append('## Results')
    report_lines.append('')

    for i, r in enumerate(results, 1):
        report_lines.append(f"### {i}. {r['source']} → {r['target']}")
        report_lines.append(f"- Status: **{r['status']}**")
        if isinstance(r['missing_snippets_count'], int):
            report_lines.append(f"- Missing narrative snippets: **{r['missing_snippets_count']} / {r['source_snippets_count']}**")
        if r['missing_headings']:
            report_lines.append('- Missing/renamed section headings (best fuzzy score):')
            for h, score in r['missing_headings'][:8]:
                report_lines.append(f"  - {h} (best match score: {score:.2f})")
            if len(r['missing_headings']) > 8:
                report_lines.append(f"  - ... and {len(r['missing_headings']) - 8} more")
        if r['missing_visual_flags']:
            report_lines.append('- Missing content element types:')
            for f in r['missing_visual_flags']:
                report_lines.append(f'  - {f}')
        report_lines.append('')

    out = ROOT / 'report-content.md'
    out.write_text('\n'.join(report_lines), encoding='utf-8')
    print(f'WROTE {out}')
    print(f'TOTAL={len(pairs)} OK={full_content_ok} PARTIAL={len(pairs)-full_content_ok}')


if __name__ == '__main__':
    main()
