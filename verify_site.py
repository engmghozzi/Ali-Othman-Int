from pathlib import Path
from html.parser import HTMLParser
from urllib.parse import urlsplit, unquote

root=Path('dist')
class Page(HTMLParser):
    def __init__(self):
        super().__init__();self.links=[];self.ids=set();self.headings=0;self.forms=[]
    def handle_starttag(self,tag,attrs):
        d=dict(attrs)
        if 'id' in d:
            assert d['id'] not in self.ids, f'Duplicate ID {d["id"]}'
            self.ids.add(d['id'])
        if tag=='h1':self.headings+=1
        if tag=='form':self.forms.append(d)
        for key in ['href','src']:
            if d.get(key):self.links.append(d[key])

pages={}
for file in root.rglob('*.html'):
    page=Page();page.feed(file.read_text(encoding='utf-8'));pages[file]=page
    if file!=root/'index.html': assert page.headings==1,file
for file,page in pages.items():
    for link in page.links:
        value=urlsplit(link)
        if value.scheme or value.netloc:continue
        dest=root/unquote(value.path).lstrip('/') if value.path.startswith('/') else file.parent/unquote(value.path)
        if not value.path:dest=file
        elif dest.is_dir():dest=dest/'index.html'
        assert dest.is_file(),(file,link)
        if value.fragment and dest in pages:assert value.fragment in pages[dest].ids,(file,link)
for lang in ['ar','en']:
    services=pages[root/lang/'services/index.html']
    assert len([x for x in services.ids if x in ['air-conditioning','duct-installation','duct-cleaning','electrical','plumbing','cctv','interiors']])==7
    form=pages[root/lang/'contact/index.html'].forms[0]
    assert form['action']=='https://formsubmit.co/aliothmanintl@gmail.com'
    assert form['method']=='POST'
print(f'Validated {len(pages)} pages: local assets, links, anchors, heading structure, services and form destination.')
