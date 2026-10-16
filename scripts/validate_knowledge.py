from pathlib import Path
import json, hashlib, csv, re
root=Path(__file__).resolve().parents[1]
m=json.loads((root/'catalog/source-manifest.json').read_text())
for s in m['sources']:
 p=root/s['path']; assert p.is_file(), s['path']
 assert hashlib.sha256(p.read_bytes()).hexdigest()==s['sha256'], s['path']
rows=list(csv.DictReader((root/'catalog/mandala-actions.csv').open()))
assert len(rows)==64 and len({r['id'] for r in rows})==64
assert all(r['venture']=='Regulars' for r in rows)
for p in [root/'README.md',root/'INDEX.md',*list((root/'knowledge').glob('*.md')),*list((root/'specs').glob('*.md'))]:
 for link in re.findall(r'\]\(([^)]+)\)',p.read_text()):
  if not re.match(r'[a-z]+:',link) and not link.startswith('#'):
   assert (p.parent/link.split('#')[0]).exists(), (str(p),link)
for e in json.loads((root/'catalog/text-extractions.json').read_text()):
 assert (root/e['source']).is_file() and (root/e['path']).is_file()
print(f"Verified {len(m['sources'])} original files, 64 actions, extracts and maintained-document links.")
