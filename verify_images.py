import os, glob, re

base = r'C:\Users\HP\Downloads\awtar-united\awtar-united'
html_files = glob.glob(os.path.join(base, '*.html'))

missing_images = set()
total_images = 0

for h in html_files:
    if 'live_site' in h: continue
    txt = open(h, encoding='utf-8').read()
    srcs = re.findall(r'<img[^>]+src=[\'"]([^\'"]+)[\'"]', txt)
    for s in srcs:
        if s.startswith('http') or s.startswith('data:'):
            continue
        total_images += 1
        full_path = os.path.normpath(os.path.join(base, s))
        if not os.path.exists(full_path):
            missing_images.add(s)

print(f"Total image tags checked across all pages: {total_images}")
if missing_images:
    print(f"Missing images locally ({len(missing_images)}):")
    for m in sorted(missing_images):
        print("  -", m)
else:
    print("ALL images referenced in HTML exist 100% locally!")
