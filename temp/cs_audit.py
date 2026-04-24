import re
import html
import difflib
from pathlib import Path

ROOT = Path('/Users/zlatomirvangelov/Documents/GitHub/Vangelov')


def find_source(name: str):
    primary = ROOT / 'Resources' / 'New folder' / name
    if primary.exists():
        return primary
    matches = list(ROOT.rglob(name))
    return matches[0] if matches else None


def normalize(html_text: str) -> str:
    s = re.sub(r'(?is)<script.*?>.*?</script>', ' ', html_text)
    s = re.sub(r'(?is)<style.*?>.*?</style>', ' ', s)
    s = re.sub(r'(?is)<!--.*?-->', ' ', s)
    s = re.sub(r'(?s)<[^>]+>', ' ', s)
    s = html.unescape(s)
    s = re.sub(r'\s+', ' ', s).strip().lower()
    return s


def load_entries():
    lines = (ROOT / 'my.md').read_text(encoding='utf-8', errors='ignore').splitlines()
    result = []
    for line in lines:
        line = line.strip()
        if line.startswith('- case-study-') and 'http://127.0.0.1:5500/Projects/' in line:
            source_name = line.split()[1]
            m = re.search(r'/Projects/([^\)\s]+)', line)
            if m:
                result.append((source_name, m.group(1)))
    return result


def main():
    entries = load_entries()
    print(f'TOTAL_MAPPED={len(entries)}')

    exact_count = 0
    for source_name, project_name in entries:
        src_path = find_source(source_name)
        dst_path = ROOT / 'Projects' / project_name

        if not src_path or not dst_path.exists():
            print(f'MISSING|{source_name}|{project_name}|src={bool(src_path)}|dst={dst_path.exists()}')
            continue

        src_text = normalize(src_path.read_text(encoding='utf-8', errors='ignore'))
        dst_text = normalize(dst_path.read_text(encoding='utf-8', errors='ignore'))

        exact = src_text == dst_text
        similarity = difflib.SequenceMatcher(None, src_text, dst_text).ratio() * 100

        if exact:
            exact_count += 1

        print(f'ROW|{source_name}|{project_name}|exact={exact}|sim={similarity:.2f}')

    print(f'EXACT_MATCHES={exact_count}')


if __name__ == '__main__':
    main()
