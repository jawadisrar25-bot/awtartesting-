import os
import glob
import re
import shutil

BASE_DIR = r"C:\Users\HP\Downloads\awtar-united\awtar-united"
PUBLIC_DIR = os.path.join(BASE_DIR, "public")

css_path = os.path.join(BASE_DIR, "assets", "style.css")
js_path = os.path.join(BASE_DIR, "assets", "site.js")

with open(css_path, "r", encoding="utf-8") as f:
    css_content = f.read()

with open(js_path, "r", encoding="utf-8") as f:
    js_content = f.read()

# Copy style.css and site.js to root directory as well
shutil.copy2(css_path, os.path.join(BASE_DIR, "style.css"))
shutil.copy2(js_path, os.path.join(BASE_DIR, "site.js"))
shutil.copy2(css_path, os.path.join(PUBLIC_DIR, "style.css"))
shutil.copy2(js_path, os.path.join(PUBLIC_DIR, "site.js"))

# Create vercel.json
vercel_json = '''{
  "version": 2,
  "cleanUrls": true,
  "trailingSlash": false
}'''

with open(os.path.join(BASE_DIR, "vercel.json"), "w", encoding="utf-8") as f:
    f.write(vercel_json)

with open(os.path.join(PUBLIC_DIR, "vercel.json"), "w", encoding="utf-8") as f:
    f.write(vercel_json)

# Create .vercelignore
vercel_ignore = '''app/
bin/
database/
tests/
*.py
*.bak
composer.json
.env.example
'''

with open(os.path.join(BASE_DIR, ".vercelignore"), "w", encoding="utf-8") as f:
    f.write(vercel_ignore)

# Rename composer.json so Vercel does not mistake project for a PHP backend
composer_path = os.path.join(BASE_DIR, "composer.json")
if os.path.exists(composer_path):
    shutil.copy2(composer_path, os.path.join(BASE_DIR, "composer.json.bak"))
    os.remove(composer_path)
    print("Renamed composer.json to composer.json.bak to prevent PHP detection on Vercel.")

pub_composer = os.path.join(PUBLIC_DIR, "composer.json")
if os.path.exists(pub_composer):
    os.remove(pub_composer)

# Process all HTML files
html_files = [
    "index.html",
    "about.html",
    "services.html",
    "menus.html",
    "gallery.html",
    "events.html",
    "contact.html",
    "get-quote.html"
]

# Update menus.html specifically with dessert and canapé photos
menus_file = os.path.join(BASE_DIR, "menus.html")
with open(menus_file, "r", encoding="utf-8") as f:
    m_html = f.read()

# Replace images in menus
m_html = m_html.replace('images/awtar_photos/awtar_037.jpg', 'images/canapes_luxury.jpg')
m_html = m_html.replace('images/awtar_photos/awtar_043.jpg', 'images/dessert_cheesecake.jpg')
m_html = m_html.replace('images/awtar_photos/awtar_024.jpg', 'images/dessert_brownie.jpg')

with open(menus_file, "w", encoding="utf-8") as f:
    f.write(m_html)

# Update gallery.html with new dessert & canapé cards
gallery_file = os.path.join(BASE_DIR, "gallery.html")
with open(gallery_file, "r", encoding="utf-8") as f:
    g_html = f.read()

# Check if new photos already in gallery
if 'dessert_cheesecake.jpg' not in g_html:
    new_gallery_items = '''
      <!-- New Featured Food & Dessert Items -->
      <div class="gallery-card" data-category="coffee">
        <img loading="lazy" src="images/dessert_brownie.jpg" alt="Artisanal Chocolate Brownies">
        <div class="gallery-overlay">
          <span class="gallery-cat" data-i18n="filter_coffee">Coffee Break & Sweets</span>
          <h4 data-i18n="gallery_item_brownie">Artisanal Chocolate Raspberry Brownies</h4>
        </div>
      </div>

      <div class="gallery-card" data-category="coffee">
        <img loading="lazy" src="images/dessert_cheesecake.jpg" alt="Mini Strawberry Cheesecakes">
        <div class="gallery-overlay">
          <span class="gallery-cat" data-i18n="filter_coffee">Coffee Break & Sweets</span>
          <h4 data-i18n="gallery_item_cheesecake">Mini Fresh Strawberry Cheesecakes</h4>
        </div>
      </div>

      <div class="gallery-card" data-category="buffets">
        <img loading="lazy" src="images/canapes_luxury.jpg" alt="Luxury Cocktail Canapés">
        <div class="gallery-overlay">
          <span class="gallery-cat" data-i18n="filter_buffets">Buffets & Banquets</span>
          <h4 data-i18n="gallery_item_canapes">Royal Reception Finger Foods & Canapés</h4>
        </div>
      </div>
'''
    g_html = g_html.replace('<div class="gallery-grid" id="galleryGrid">', '<div class="gallery-grid" id="galleryGrid">' + new_gallery_items)
    with open(gallery_file, "w", encoding="utf-8") as f:
        f.write(g_html)

# Now inject inline CSS and fallback JS in ALL HTML files (both in BASE_DIR and PUBLIC_DIR)
for h_name in html_files:
    fpath = os.path.join(BASE_DIR, h_name)
    if not os.path.exists(fpath):
        continue
    
    with open(fpath, "r", encoding="utf-8") as f:
        content = f.read()

    # Ensure link rel has both fallback and proper paths
    # Inject full CSS into <head> right before </head> if not already inlined
    style_tag = f'<style id="awtar-inline-styles">\n{css_content}\n</style>'
    
    if 'id="awtar-inline-styles"' in content:
        content = re.sub(r'<style id="awtar-inline-styles">.*?</style>', style_tag, content, flags=re.DOTALL)
    else:
        content = content.replace('</head>', f'{style_tag}\n</head>')

    # Inject full JS fallback right before </body> if not already inlined
    js_tag = f'<script id="awtar-inline-script">\n{js_content}\n</script>'
    if 'id="awtar-inline-script"' in content:
        content = re.sub(r'<script id="awtar-inline-script">.*?</script>', js_tag, content, flags=re.DOTALL)
    else:
        content = content.replace('</body>', f'{js_tag}\n</body>')

    with open(fpath, "w", encoding="utf-8") as f:
        f.write(content)

    # Copy identical updated file to public/
    shutil.copy2(fpath, os.path.join(PUBLIC_DIR, h_name))

print("All 8 HTML files updated with inline luxury CSS & interactive JS fallback!")
print("Copied files to public/ as well.")
