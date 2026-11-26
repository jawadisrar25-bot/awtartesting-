import os, re

BASE = r"C:\Users\HP\Downloads\awtar-united\awtar-united"
pages = ['about.html', 'services.html', 'menus.html', 'events.html', 'contact.html']

total_size = 0
for p in pages:
    txt = open(os.path.join(BASE, p), encoding='utf-8').read()
    imgs = re.findall(r'<img[^>]+src=[\'"]([^\'"]+)[\'"]', txt)
    non_data = [i for i in imgs if not i.startswith('data:')]
    p_size = sum(os.path.getsize(os.path.join(BASE, i)) for i in set(non_data) if os.path.exists(os.path.join(BASE, i)))
    total_size += p_size
    print(f"{p:15} -> {len(non_data)} images, {p_size/1024:.1f} KB")

print(f"Total size across all these pages: {total_size/(1024*1024):.2f} MB")
