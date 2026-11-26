import os
import re
import urllib.request
import urllib.error

ROOT_DIR = r"C:\Users\HP\Downloads\awtar-united\awtar-united"
PARTNERS_DIR = os.path.join(ROOT_DIR, "images", "partners")
PUBLIC_PARTNERS_DIR = os.path.join(ROOT_DIR, "public", "images", "partners")

os.makedirs(PARTNERS_DIR, exist_ok=True)
os.makedirs(PUBLIC_PARTNERS_DIR, exist_ok=True)

with open(os.path.join(ROOT_DIR, "live_site.html"), "r", encoding="utf-8") as f:
    text = f.read()

# Extract all partner cards
matches = re.findall(r'<div class="partner-card"><img src="([^"]+)" alt="([^"]+)"><span>([^<]+)</span></div>', text)
print(f"Found {len(matches)} partner cards.")

headers = {'User-Agent': 'Mozilla/5.0'}

downloaded_partners = []
for i, (url, alt, name) in enumerate(matches, 1):
    safe_name = re.sub(r'[^a-zA-Z0-9]', '_', alt.lower()).strip('_')
    ext = os.path.splitext(url.split('?')[0])[1]
    if not ext or len(ext) > 5:
        ext = '.png'
    dest_filename = f"{i:02d}_{safe_name}{ext}"
    dest_path = os.path.join(PARTNERS_DIR, dest_filename)
    public_path = os.path.join(PUBLIC_PARTNERS_DIR, dest_filename)
    
    local_url = f"images/partners/{dest_filename}"
    
    if not os.path.exists(dest_path):
        try:
            req = urllib.request.Request(url, headers=headers)
            with urllib.request.urlopen(req, timeout=8) as response, open(dest_path, 'wb') as out_file:
                out_file.write(response.read())
            with open(dest_path, 'rb') as src, open(public_path, 'wb') as dst:
                dst.write(src.read())
            print(f"Downloaded: {name} -> {dest_filename}")
        except Exception as e:
            print(f"Failed to download {name} ({url}): {e}")
            # Keep original URL as fallback
            local_url = url
    else:
        with open(dest_path, 'rb') as src, open(public_path, 'wb') as dst:
            dst.write(src.read())
        print(f"Already exists: {dest_filename}")
        
    downloaded_partners.append({
        'name_en': name,
        'alt': alt,
        'image': local_url if os.path.exists(dest_path) else url
    })

import json
with open(os.path.join(ROOT_DIR, "partners_data.json"), "w", encoding="utf-8") as f:
    json.dump(downloaded_partners, f, indent=2, ensure_ascii=False)
print("Saved partners_data.json")
