#!/usr/bin/env python3
"""Validate local page links, assets, document headings, and navigation."""
from html.parser import HTMLParser
from pathlib import Path
from urllib.parse import urlsplit, unquote

ROOT = Path(__file__).resolve().parents[1]
errors = []


class Page(HTMLParser):
    def __init__(self, path):
        super().__init__()
        self.path, self.headings, self.current = path, 0, 0

    def handle_starttag(self, tag, attrs):
        a = dict(attrs)
        if tag == 'h1':
            self.headings += 1
        if a.get('aria-current') == 'page':
            self.current += 1
        for key in ['src', 'href']:
            url = a.get(key)
            if not url:
                continue
            part = urlsplit(url)
            if part.scheme or part.netloc or not part.path:
                continue
            target = self.path.parent / unquote(part.path)
            if not target.is_file():
                errors.append(f'{self.path.name}: missing {url}')
        if tag == 'a' and a.get('target') == '_blank' and 'noopener' not in a.get('rel', ''):
            errors.append(f'{self.path.name}: missing noopener')
        if tag == 'img' and 'alt' not in a:
            errors.append(f'{self.path.name}: image missing alt')


for path in ROOT.glob('*.html'):
    parser = Page(path)
    parser.feed(path.read_text())
    if parser.headings != 1 or parser.current != 1:
        errors.append(f'{path.name}: expected one h1 and one current navigation item')
if errors:
    raise SystemExit('\n'.join(errors))
print('All five pages have valid local links, assets, headings, and current navigation.')
