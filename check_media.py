import glob, re

h_files = glob.glob(r'C:\Users\HP\Downloads\awtar-united\awtar-united\*.html')
refs = []
for h in h_files:
    if 'live_site' in h: continue
    txt = open(h, encoding='utf-8').read()
    refs.extend(re.findall(r'media/[^\s"\'<>]+', txt))

print('Total media/ references in our redesigned pages:', len(refs))
if refs:
    print('Sample refs:', refs[:5])
