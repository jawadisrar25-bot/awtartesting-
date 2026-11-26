import glob, re, os

BASE = r"C:\Users\HP\Downloads\awtar-united\awtar-united"
pages = ['about.html', 'services.html', 'menus.html', 'gallery.html', 'events.html', 'contact.html']

for p in pages:
    fpath = os.path.join(BASE, p)
    txt = open(fpath, encoding='utf-8').read()
    imgs = re.findall(r'<img[^>]+src=[\'"]([^\'"]+)[\'"]', txt)
    non_data = [i for i in imgs if not i.startswith('data:')]
    print(f"{p:15} -> {len(non_data)} external images: {non_data[:4]}")
