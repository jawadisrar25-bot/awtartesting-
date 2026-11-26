import os, re, shutil

BASE_DIR = r"C:\Users\HP\Downloads\awtar-united\awtar-united"
PUBLIC_DIR = os.path.join(BASE_DIR, "public")
index_path = os.path.join(BASE_DIR, "index.html")

with open(index_path, "r", encoding="utf-8") as f:
    txt = f.read()

# Fix corrupted partner images markup
# Pattern: <img loading="lazy" src="images/partners/...> followed by junk
# Let's replace the whole partners section cleanly

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

# Build clean partners HTML
cards_html = []
for file_name, en_name, ar_name in partners_list:
    card = f'''    <div class="partner-card" data-name-en="{en_name}" data-name-ar="{ar_name}">
      <img loading="lazy" src="images/partners/{file_name}" alt="{en_name}">
      <span>{en_name}</span>
    </div>'''
    cards_html.append(card)

new_grid_content = '<div class="partners-grid">\n' + '\n'.join(cards_html) + '\n  </div>'

# Replace old partners-grid
txt = re.sub(r'<div class="partners-grid">.*?</div>\s*</div>\s*</section>', new_grid_content + '\n  </div>\n</section>', txt, flags=re.DOTALL)

with open(index_path, "w", encoding="utf-8") as f:
    f.write(txt)

shutil.copy2(index_path, os.path.join(PUBLIC_DIR, "index.html"))
print("index.html partners grid repaired cleanly without any junk text!")
