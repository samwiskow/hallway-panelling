"""Check local page links, preview controls and required public assets."""
from html.parser import HTMLParser
from pathlib import Path
from urllib.parse import unquote, urlsplit

ROOT = Path(__file__).resolve().parent


class Page(HTMLParser):
    def __init__(self, path):
        super().__init__()
        self.path = path
        self.ids = set()
        self.links = []
        self.images = []
        self.previews = set()
        self.feed(path.read_text())

    def handle_starttag(self, tag, attrs):
        attrs = dict(attrs)
        if 'id' in attrs:
            assert attrs['id'] not in self.ids, f'Duplicate ID: {self.path}: {attrs["id"]}'
            self.ids.add(attrs['id'])
            if tag == 'figure':
                self.previews.add(attrs['id'])
        for name in ('href', 'src'):
            if name in attrs:
                self.links.append(attrs[name])
        if tag == 'img':
            assert attrs.get('alt'), f'Missing image text: {self.path}'
            self.images.append(attrs['src'])


pages = {path.resolve(): Page(path) for path in ROOT.rglob('*.html')}
for path, page in pages.items():
    for link in page.links:
        parsed = urlsplit(link)
        if parsed.scheme or parsed.netloc:
            continue
        target = (path.parent / unquote(parsed.path)).resolve() if parsed.path else path
        if target.is_dir():
            target /= 'index.html'
        assert target.is_file(), f'Broken asset or link: {path}: {link}'
        if parsed.fragment and target.suffix == '.html':
            assert parsed.fragment in pages[target].ids, f'Broken anchor: {path}: {link}'
    if path.parent.name in ('shaker', 'frames', 'grooved'):
        assert len(page.previews) == 10, f'Missing room or door views: {path}'
        assert {'view-barn-closed', 'view-barn-part-open', 'view-barn-open'} <= page.previews
        for preview in page.previews:
            assert '#'+preview in page.links, f'Preview cannot be selected: {path}: {preview}'
assert len(pages) == 4
assert (ROOT/'assets/hallway-panelling-materials-and-cuts.pdf').read_bytes().startswith(b'%PDF-')
print(f'PASS: {len(pages)} pages; all local links, assets, anchors and 30 previews')
