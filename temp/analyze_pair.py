import re, html
from difflib import SequenceMatcher
from pathlib import Path

ROOT = Path('/Users/zlatomirvangelov/Documents/GitHub/Vangelov')
src = ROOT / 'Resources' / 'New folder' / 'case-study-domestic-cc-fee-config.html'
tgt = ROOT / 'Projects' / 'domestic-cc-fee-config.html'

HEADING_RE = re.compile(r'(?is)<h[1-4][^>]*>(.*?)</h[1-4]>')
TEXT_RE = re.compile(r'(?is)<(p|li|td|th|figcaption|blockquote)[^>]*>(.*?)</\1>')

def clean(s):
    s = re.sub(r'(?is)<[^>]+>', ' ', s)
    s = html.unescape(s)
    return re.sub(r'\s+', ' ', s).strip()

def preprocess(raw):
    raw = re.sub(r'(?is)<!--.*?-->', ' ', raw)
    raw = re.sub(r'(?is)<script\b[^>]*>.*?</script\s*>', ' ', raw)
    raw = re.sub(r'(?is)<style\b[^>]*>.*?</style\s*>', ' ', raw)
    return raw

def extract_headings(raw):
    out=[]
    for h in HEADING_RE.findall(raw):
        t=clean(h)
        if len(t)>=4:
            out.append(t)
    return out

def extract_snippets(raw):
    out=[]
    for _,v in TEXT_RE.findall(raw):
        t=clean(v)
        if len(t.split())>=5:
            out.append(t)
    return out

def fuzzy_contains(target_items, source_item, threshold=0.70):
    best=0.0
    for t in target_items:
        s=SequenceMatcher(None, source_item.lower(), t.lower()).ratio()
        if s>best:
            best=s
        if s>=threshold:
            return True,best
    return False,best

src_raw = preprocess(src.read_text(encoding='utf-8', errors='ignore'))
tgt_raw = preprocess(tgt.read_text(encoding='utf-8', errors='ignore'))

src_h = extract_headings(src_raw)
tgt_h = extract_headings(tgt_raw)

print('HEADINGS SOURCE:', len(src_h), 'TARGET:', len(tgt_h))
missing_h=[]
for h in src_h:
    ok,b=fuzzy_contains(tgt_h,h)
    if not ok:
        missing_h.append((h,b))
print('MISSING HEADINGS:', len(missing_h))
for h,b in missing_h[:20]:
    print(f'- {h} :: {b:.2f}')

src_s = extract_snippets(src_raw)
tgt_text = clean(re.sub(r'(?is)<[^>]+>', ' ', tgt_raw)).lower()
missing_s=[]
for s in src_s:
    words=re.findall(r"[a-zA-Z0-9']+", s.lower())
    if len(words)<7:
        continue
    probe=' '.join(words[:12])
    if probe not in tgt_text:
        missing_s.append(s)
print('SNIPPETS SOURCE:', len(src_s))
print('MISSING SNIPPETS (probe check):', len(missing_s))
for s in missing_s[:20]:
    print('-', s[:220])
