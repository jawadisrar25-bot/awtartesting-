import os
import re

ROOT = r"C:\Users\HP\Downloads\awtar-united\awtar-united"
pages = ['index.html', 'about.html', 'services.html', 'menus.html', 'gallery.html', 'events.html', 'contact.html', 'get-quote.html']

all_clean = True
for p in pages:
    path = os.path.join(ROOT, p)
    with open(path, 'r', encoding='utf-8') as f:
        content = f.read()
    imgs = re.findall(r'src=["\']([^"\']+\.(?:jpeg|jpg|png|svg|mp4))["\']', content)
    missing = [img for img in imgs if not img.startswith('http') and not os.path.exists(os.path.join(ROOT, img))]
    print(f"{p}: {len(content)} bytes, {len(imgs)} media refs, missing: {len(missing)}")
    if missing:
        all_clean = False
        print("  Missing:", missing[:5])

if all_clean:
    print("\nALL PAGES & MEDIA REFERENCES ARE 100% VALID AND LOCAL!")
