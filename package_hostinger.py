"""Package only the company website, never the live subdomain applications."""
from pathlib import Path
from zipfile import ZipFile, ZIP_DEFLATED
import sys

root=Path(__file__).resolve().parent
output=Path(sys.argv[1]) if len(sys.argv)>1 else root.parent/'ali-othman-professional-v2.zip'
allowed=['ar','en','assets','index.html','ao-website.css','site.js']
with ZipFile(output,'w',ZIP_DEFLATED) as archive:
    for name in allowed:
        entry=root/'dist'/name
        files=entry.rglob('*') if entry.is_dir() else [entry]
        for file in files:
            if file.is_file(): archive.write(file,file.relative_to(root/'dist').as_posix())
with ZipFile(output) as archive:
    names=archive.namelist()
    assert 'index.html' in names and 'ao-website.css' in names
    assert all(name.split('/')[0] in allowed for name in names)
    assert not any(name.startswith(('cmapp/','cms/','cmsys/','test/')) or '.htaccess' in name for name in names)
print(f'Packaged and verified {len(names)} website files: {output}')
