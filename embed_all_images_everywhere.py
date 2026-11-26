import os
import base64
import re
import shutil

BASE = r"C:\Users\HP\Downloads\awtar-united\awtar-united"
PUBLIC = os.path.join(BASE, "public")

def to_base64_uri(file_path):
    if not os.path.exists(file_path):
        return None
    ext = os.path.splitext(file_path)[1].lower()
    mime = "image/jpeg"
    if ext == ".png": mime = "image/png"
    elif ext == ".svg": mime = "image/svg+xml"
    elif ext == ".webp": mime = "image/webp"
    with open(file_path, "rb") as f:
        data = base64.b64encode(f.read()).decode("utf-8")
    return f"data:{mime};base64,{data}"

# 1. Partner Logos in index.html
partners_dir = os.path.join(BASE, "images", "partners")
partner_b64 = {}
if os.path.exists(partners_dir):
    for f in os.listdir(partners_dir):
        b64 = to_base64_uri(os.path.join(partners_dir, f))
        if b64:
            partner_b64[f] = b64

index_file = os.path.join(BASE, "index.html")
with open(index_file, "r", encoding="utf-8") as f:
    txt = f.read()

partners_list = [
    ("01_stc.png", "stc", "إس تي سي (stc)"),
    ("02_ministry_of_economy___planning.png", "Ministry of Economy & Planning", "وزارة الاقتصاد والتخطيط"),
    ("03_ministry_of_industry.png", "Ministry of Industry", "وزارة الصناعة والثروة المعدنية"),
    ("04_bsf.png", "BSF", "البنك السعودي الفرنسي (BSF)"),
    ("05_zatca.png", "ZATCA", "هيئة الزكاة والضريبة والجمارك (ZATCA)"),
    ("06_world_defence_show.png", "World Defence Show", "معرض الدفاع العالمي"),
    ("07_ministry_of_education.png", "Ministry of Education", "وزارة التعليم"),
    ("08_tmg.png", "TMG", "مجموعة طلعت مصطفى (TMG)"),
    ("09_rekab.png", "Rekab", "ركاب (Rekab)"),
    ("10_smasco.png", "SMASCO", "سماسكو (SMASCO)"),
    ("11_esnad.jpg", "ESNAD", "إسناد (ESNAD)"),
    ("12_mobily.png", "Mobily", "موبايلي (Mobily)"),
    ("13_ministry_of_justice.jpg", "Ministry of Justice", "وزارة العدل"),
    ("14_nofa_riyadh.png", "NOFA Riyadh", "منتجع نوفا الرياض"),
    ("16_ministry_of_defence.svg", "Ministry of Municipalities & Housing", "وزارة البلديات والإسكان"),
    ("16_ministry_of_defence.svg", "Ministry of Defence", "وزارة الدفاع"),
    ("17_hwadi.png", "Hwadi", "حوادي (Hwadi)"),
    ("18_albawani.png", "Albawani", "البواني (Albawani)"),
    ("19_ncec.png", "NCEC", "المركز الوطني للرقابة على الالتزام البيئي"),
    ("20_social_development_bank.png", "Social Development Bank", "بنك التنمية الاجتماعية"),
    ("21_al_rajhi_bank.png", "Al Rajhi Bank", "مصرف الراجحي"),
    ("22_saudi_tadawul.png", "Saudi Tadawul Group", "مجموعة تداول السعودية"),
    ("23_al_jazirah.png", "Al Jazirah", "بنك الجزيرة"),
    ("24_mewa.png", "MEWA", "وزارة البيئة والمياه والزراعة"),
    ("25_green_riyadh.png", "Green Riyadh", "الرياض الخضراء"),
    ("26_judicial_training_center.png", "Judicial Training Center", "مركز التدريب العدلي"),
    ("27_al_basha_group.png", "Al Basha Group", "مجموعة الباشا"),
    ("28_sea_ventures.png", "SEA Ventures", "سي فينتشرز"),
    ("29_yelow.png", "Yelow", "يلو لتأجير السيارات (Yelow)")
]

cards_html = []
for file_name, en_name, ar_name in partners_list:
    src_val = partner_b64.get(file_name, f"images/partners/{file_name}")
    # Note: alt is empty to prevent broken-image double text, span carries the accessible name
    card = f'''    <div class="partner-card" data-name-en="{en_name}" data-name-ar="{ar_name}">
      <img loading="lazy" src="{src_val}" alt="" class="partner-logo">
      <span class="partner-label">{en_name}</span>
    </div>'''
    cards_html.append(card)

new_grid_content = '<div class="partners-grid">\n' + '\n'.join(cards_html) + '\n  </div>'
txt = re.sub(r'<div class="partners-grid">.*?</div>\s*</div>\s*</section>', new_grid_content + '\n  </div>\n</section>', txt, flags=re.DOTALL)

with open(index_file, "w", encoding="utf-8") as f:
    f.write(txt)
shutil.copy2(index_file, os.path.join(PUBLIC, "index.html"))
print(f"index.html embedded with {len(partner_b64)} partner logos!")

# 2. Embed images in other pages
other_pages = ["about.html", "services.html", "menus.html", "events.html", "contact.html", "gallery.html"]

for p in other_pages:
    fpath = os.path.join(BASE, p)
    if not os.path.exists(fpath): continue
    with open(fpath, "r", encoding="utf-8") as f:
        html = f.read()

    # Find all external image srcs
    imgs = re.findall(r'<img[^>]+src=[\'"]([^\'"]+)[\'"]', html)
    embedded_count = 0
    for img_rel in set(imgs):
        if img_rel.startswith("data:") or img_rel.startswith("http"):
            continue
        local_path = os.path.join(BASE, img_rel)
        if os.path.exists(local_path):
            # Check size, if under 1.5MB embed
            if os.path.getsize(local_path) < 1500000:
                b64 = to_base64_uri(local_path)
                if b64:
                    html = html.replace(f'src="{img_rel}"', f'src="{b64}"')
                    html = html.replace(f"src='{img_rel}'", f'src="{b64}"')
                    embedded_count += 1
    
    with open(fpath, "w", encoding="utf-8") as f:
        f.write(html)
    shutil.copy2(fpath, os.path.join(PUBLIC, p))
    print(f"{p}: embedded {embedded_count} images as base64 data URIs!")

print("All pages have their images embedded directly!")
