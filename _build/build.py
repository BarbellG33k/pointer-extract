import glob, json, os, re, sys
here = os.path.dirname(os.path.abspath(__file__))
parent = os.path.dirname(here)
records = []
for f in sorted(glob.glob(os.path.join(parent, '20[0-9][0-9]-[0-1][0-9].json'))):
    with open(f, encoding='utf-8') as fh:
        records.extend(json.load(fh))
records.sort(key=lambda r: (r['date'], r['issue']))
data = json.dumps(records, ensure_ascii=False).replace('</', '<\\/')
tpl_name = sys.argv[1] if len(sys.argv) > 1 else 'template.html'
with open(os.path.join(here, tpl_name), encoding='utf-8') as fh:
    tpl = fh.read()
assert '/*__DATA__*/[]' in tpl
out = tpl.replace('/*__DATA__*/[]', data, 1)
with open(os.path.join(parent, 'pointer-extract.html'), 'w', encoding='utf-8') as fh:
    fh.write(out)
print('template', tpl_name, '| records', len(records), 'issues', len(set(r['issue'] for r in records)))
