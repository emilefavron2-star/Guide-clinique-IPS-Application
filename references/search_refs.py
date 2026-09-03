#!/usr/bin/env python3
"""
Recherche dans les ouvrages de référence du guide clinique IPS.

Usage :
    python3 search_refs.py "goutte"                  # cherche partout
    python3 search_refs.py "gout" -b goldman         # un seul ouvrage
    python3 search_refs.py "osteoporosis" -n 5       # nb de résultats
    python3 search_refs.py --chapters goldman gout   # chapitres correspondants
    python3 search_refs.py --page goldman 1850       # affiche une page
    python3 search_refs.py --list                    # liste les ouvrages
"""
import re, json, sys, argparse, os

BASE = os.path.dirname(os.path.abspath(__file__))
TXT = {
    'copstead':       '/tmp/copstead.txt',
    'goldman':        '/tmp/goldman.txt',
    'gphc_entrevue':  '/tmp/gphc_entrevue.txt',
    'gphc_habiletes': '/tmp/gphc_habiletes.txt',
    'lilly':          '/tmp/lilly.txt',
    'demarche':       '/tmp/demarche.txt',
    'beaulieu':       '/tmp/beaulieu.txt',
    'querin':         '/tmp/querin.txt',
    'cardiomedik':    '/tmp/cardiomedik.txt',
    'rej':            '/tmp/rej.txt',
}

def load_index():
    with open(os.path.join(BASE, 'index.json'), encoding='utf-8') as f:
        return json.load(f)

def load_pages(book):
    path = TXT.get(book)
    if not path or not os.path.exists(path):
        sys.exit(f"Texte absent pour '{book}'. Relancer extract_refs.sh")
    with open(path, encoding='utf-8', errors='ignore') as f:
        return f.read().split('\f')

def chapter_for(idx, book, pdf_page):
    for num, d in idx[book]['chapters'].items():
        if d['pdf_start'] <= pdf_page <= d['pdf_end']:
            return f"Ch.{num} — {d['title']}"
    return ""

def search(idx, term, books, limit, ctx):
    pat = re.compile(re.escape(term), re.IGNORECASE)
    for book in books:
        pages = load_pages(book)
        hits = []
        for i, pg in enumerate(pages):
            n = len(pat.findall(pg))
            if n:
                hits.append((n, i + 1, pg))
        if not hits:
            continue
        hits.sort(key=lambda x: -x[0])
        print(f"\n{'='*74}\n{idx[book]['title']}  —  {len(hits)} page(s)\n{'='*74}")
        for n, pdfpg, pg in hits[:limit]:
            print(f"\n  ▸ PDF p.{pdfpg}  ({n} occurrence{'s' if n>1 else ''})  {chapter_for(idx, book, pdfpg)}")
            for m in list(pat.finditer(pg))[:2]:
                s = max(0, m.start() - ctx); e = min(len(pg), m.end() + ctx)
                frag = re.sub(r'\s+', ' ', pg[s:e]).strip()
                print(f"      …{frag}…")

def main():
    ap = argparse.ArgumentParser(add_help=False)
    ap.add_argument('term', nargs='*')
    ap.add_argument('-b', '--book', action='append')
    ap.add_argument('-n', '--limit', type=int, default=6)
    ap.add_argument('-c', '--context', type=int, default=220)
    ap.add_argument('--chapters', nargs=2, metavar=('BOOK', 'TERM'))
    ap.add_argument('--page', nargs=2, metavar=('BOOK', 'N'))
    ap.add_argument('--list', action='store_true')
    ap.add_argument('-h', '--help', action='store_true')
    a = ap.parse_args()
    idx = load_index()

    if a.help or (not a.term and not a.chapters and not a.page and not a.list):
        print(__doc__); return

    if a.list:
        for k, b in idx.items():
            print(f"  {k:16} {b['pages']:>5} p.  {len(b['chapters']):>3} ch.  {b['title']}")
        return

    if a.page:
        book, n = a.page[0], int(a.page[1])
        pages = load_pages(book)
        print(f"── {idx[book]['title']} — PDF p.{n} — {chapter_for(idx, book, n)} ──\n")
        print(pages[n-1])
        return

    if a.chapters:
        book, term = a.chapters
        pat = re.compile(re.escape(term), re.IGNORECASE)
        for num in sorted(idx[book]['chapters'], key=lambda x: int(x)):
            d = idx[book]['chapters'][num]
            if pat.search(d['title']):
                print(f"  Ch.{num:>3}  PDF p.{d['pdf_start']}-{d['pdf_end']}  {d['title']}")
        return

    books = a.book or list(idx.keys())
    search(idx, ' '.join(a.term), books, a.limit, a.context)

if __name__ == '__main__':
    main()
