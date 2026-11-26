import os
import json
import re

ROOT_DIR = r"C:\Users\HP\Downloads\awtar-united\awtar-united"
PUBLIC_DIR = os.path.join(ROOT_DIR, "public")
ASSETS_DIR = os.path.join(ROOT_DIR, "assets")
PUBLIC_ASSETS = os.path.join(PUBLIC_DIR, "assets")

os.makedirs(ASSETS_DIR, exist_ok=True)
os.makedirs(PUBLIC_ASSETS, exist_ok=True)

# Load partners
with open(os.path.join(ROOT_DIR, "partners_data.json"), "r", encoding="utf-8") as f:
    partners_list = json.load(f)

# Fix MOMRAH if needed
for p in partners_list:
    if "stage.maaal.com" in p["image"]:
        p["image"] = "images/partners/16_ministry_of_defence.svg"

# Arabic names map for partners
ar_partners = {
    'stc': 'إس تي سي (stc)',
    'Ministry of Economy & Planning': 'وزارة الاقتصاد والتخطيط',
    'Ministry of Industry': 'وزارة الصناعة والثروة المعدنية',
    'BSF': 'البنك السعودي الفرنسي (BSF)',
    'ZATCA': 'هيئة الزكاة والضريبة والجمارك',
    'World Defence Show': 'معرض الدفاع العالمي',
    'Ministry of Education': 'وزارة التعليم',
    'TMG': 'مجموعة TMG',
    'Rekab': 'ركاب (Rekab)',
    'SMASCO': 'سماسكو (SMASCO)',
    'ESNAD': 'إسناد (ESNAD)',
    'Mobily': 'موبايلي (Mobily)',
    'Ministry of Justice': 'وزارة العدل',
    'NOFA Riyadh': 'منتجع نوفا الرياض',
    'Ministry of Municipalities & Housing': 'وزارة البلديات والإسكان',
    'Ministry of Defence': 'وزارة الدفاع',
    'Hwadi': 'هوادي (Hwadi)',
    'Albawani': 'البواني للمقاولات',
    'NCEC': 'المركز الوطني للالتزام البيئي',
    'Social Development Bank': 'بنك التنمية الاجتماعية',
    'Al Rajhi Bank': 'مصرف الراجحي',
    'Saudi Tadawul Group': 'مجموعة تداول السعودية',
    'Al Jazirah': 'بنك الجزيرة',
    'MEWA': 'وزارة البيئة والمياه والزراعة',
    'Green Riyadh': 'مشروع الرياض الخضراء',
    'Judicial Training Center': 'مركز التدريب العدلي',
    'Al Basha Group': 'مجموعة الباشا',
    'SEA Ventures': 'سي فينشرز (SEA Ventures)',
    'Yelow': 'شركة يلو لتأجير السيارات'
}

for p in partners_list:
    p['name_ar'] = ar_partners.get(p['name_en'], p['name_en'])

print("Prepared partners data with bilingual names.")
