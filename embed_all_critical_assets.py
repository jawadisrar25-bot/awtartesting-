import os
import base64
import re
import glob

BASE_DIR = r"C:\Users\HP\Downloads\awtar-united\awtar-united"
PUBLIC_DIR = os.path.join(BASE_DIR, "public")

def get_b64(rel_path, mime_type="image/jpeg"):
    full_path = os.path.join(BASE_DIR, rel_path)
    if not os.path.exists(full_path):
        print(f"Warning: {full_path} not found")
        return ""
    with open(full_path, "rb") as f:
        data = base64.b64encode(f.read()).decode("utf-8")
    return f"data:{mime_type};base64,{data}"

# Get base64 for logo and 3 home slider images
b64_logo = get_b64("images/logo1.png", "image/png")
b64_slide1 = get_b64("images/home_slide_1_brownies.jpg", "image/jpeg")
b64_slide2 = get_b64("images/home_slide_2_cheesecake.jpg", "image/jpeg")
b64_slide3 = get_b64("images/home_slide_3_canapes.jpg", "image/jpeg")

# Also for desserts and canapes
b64_brownie = get_b64("images/dessert_brownie.jpg", "image/jpeg")
b64_cheesecake = get_b64("images/dessert_cheesecake.jpg", "image/jpeg")
b64_canapes = get_b64("images/canapes_luxury.jpg", "image/jpeg")

# Also get service images
b64_srv1 = get_b64("images/awtar_photos/awtar_001.jpg", "image/jpeg")
b64_srv2 = get_b64("images/awtar_photos/awtar_002.jpg", "image/jpeg")
b64_srv3 = get_b64("images/awtar_photos/awtar_003.jpg", "image/jpeg")

print("Base64 generated successfully!")

# Copy these key images to root as well
import shutil
for img_name in ["logo1.png", "home_slide_1_brownies.jpg", "home_slide_2_cheesecake.jpg", "home_slide_3_canapes.jpg", "dessert_brownie.jpg", "dessert_cheesecake.jpg", "canapes_luxury.jpg"]:
    s = os.path.join(BASE_DIR, "images", img_name)
    if os.path.exists(s):
        shutil.copy2(s, os.path.join(BASE_DIR, img_name))
        shutil.copy2(s, os.path.join(PUBLIC_DIR, img_name))

# 1. Update index.html
index_path = os.path.join(BASE_DIR, "index.html")
with open(index_path, "r", encoding="utf-8") as f:
    content = f.read()

# Replace all occurrences of logo1.png
content = re.sub(r'src=["\'](?:images/)?logo1\.png["\']', f'src="{b64_logo}"', content)

# Replace home slider images
content = re.sub(r'src=["\'](?:images/)?home_slide_1_brownies\.jpg["\']', f'src="{b64_slide1}"', content)
content = re.sub(r'src=["\'](?:images/)?home_slide_2_cheesecake\.jpg["\']', f'src="{b64_slide2}"', content)
content = re.sub(r'src=["\'](?:images/)?home_slide_3_canapes\.jpg["\']', f'src="{b64_slide3}"', content)

# Replace services highlight images
content = re.sub(r'src=["\']images/awtar_photos/awtar_001\.jpg["\']', f'src="{b64_srv1}"', content)
content = re.sub(r'src=["\']images/awtar_photos/awtar_002\.jpg["\']', f'src="{b64_srv2}"', content)
content = re.sub(r'src=["\']images/awtar_photos/awtar_003\.jpg["\']', f'src="{b64_srv3}"', content)

# Add graceful partner logo fallback in CSS if image fails
partner_css_fallback = """
.partner-card img {
  max-width: 120px;
  max-height: 48px;
  object-fit: contain;
  filter: grayscale(100%) opacity(0.8);
  transition: var(--transition);
}
.partner-card:hover img {
  filter: grayscale(0%) opacity(1);
}
.partner-card .partner-fallback-text {
  display: none;
  font-size: 0.82rem;
  font-weight: 700;
  color: #1A1A1A;
  text-align: center;
  padding: 0.5rem;
}
"""
if '.partner-fallback-text' not in content:
    content = content.replace('</style>', partner_css_fallback + '\n</style>')

# Replace partner card img tags to have fallback text
def replace_partner_img(match):
    full = match.group(0)
    alt = match.group(1)
    return f'{full}\n        <span class="partner-fallback-text">{alt}</span>'

content = re.sub(r'<img loading="lazy" src="images/partners/[^"]+" alt="([^"]+)">',
                 r'<img loading="lazy" src="images/partners/\g<0>" alt="\1" onerror="this.style.display=\'none\'; this.nextElementSibling.style.display=\'block\';">',
                 content)
# Fix any double nested src
content = content.replace('src="images/partners/<img loading="lazy" src="images/partners/', 'src="images/partners/')

with open(index_path, "w", encoding="utf-8") as f:
    f.write(content)
shutil.copy2(index_path, os.path.join(PUBLIC_DIR, "index.html"))
print("index.html updated with embedded Logo, 3 Slider photos, and Service images!")

# 2. Update all other HTML files to embed logo and key images
other_pages = ["about.html", "services.html", "menus.html", "gallery.html", "events.html", "contact.html", "get-quote.html"]
for p in other_pages:
    ppath = os.path.join(BASE_DIR, p)
    if not os.path.exists(ppath): continue
    with open(ppath, "r", encoding="utf-8") as f:
        c = f.read()
    
    # Replace logo with embedded base64
    c = re.sub(r'src=["\'](?:images/)?logo1\.png["\']', f'src="{b64_logo}"', c)
    
    if p == "menus.html":
        c = re.sub(r'src=["\']images/canapes_luxury\.jpg["\']', f'src="{b64_canapes}"', c)
        c = re.sub(r'src=["\']images/dessert_cheesecake\.jpg["\']', f'src="{b64_cheesecake}"', c)
        c = re.sub(r'src=["\']images/dessert_brownie\.jpg["\']', f'src="{b64_brownie}"', c)
    
    if p == "gallery.html":
        c = re.sub(r'src=["\']images/dessert_brownie\.jpg["\']', f'src="{b64_brownie}"', c)
        c = re.sub(r'src=["\']images/dessert_cheesecake\.jpg["\']', f'src="{b64_cheesecake}"', c)
        c = re.sub(r'src=["\']images/canapes_luxury\.jpg["\']', f'src="{b64_canapes}"', c)

    with open(ppath, "w", encoding="utf-8") as f:
        f.write(c)
    shutil.copy2(ppath, os.path.join(PUBLIC_DIR, p))

print("All other HTML files updated with embedded logo and key images!")
