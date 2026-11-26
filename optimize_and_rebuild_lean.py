import os
import base64
import re
import shutil
from PIL import Image

BASE = r"C:\Users\HP\Downloads\awtar-united\awtar-united"
PUBLIC = os.path.join(BASE, "public")

# 1. Optimize all HD images to lean, high-fidelity web JPEGs (target ~100-200 KB each)
hd_imgs = [
    'hero_banquet_luxury.jpg',
    'hero_canapes_gourmet.jpg',
    'hero_desserts_artisan.jpg',
    'service_corporate_summit.jpg',
    'service_coffee_break.jpg',
    'service_mega_projects.jpg'
]

opt_b64 = {}

for name in hd_imgs:
    src_p = os.path.join(BASE, 'images', name)
    if os.path.exists(src_p):
        im = Image.open(src_p)
        orig_w, orig_h = im.size
        # Scale to max 1280px for crisp HD display while keeping size tiny
        if orig_w > 1280:
            new_h = int(orig_h * (1280 / orig_w))
            im = im.resize((1280, new_h), Image.Resampling.LANCZOS)
        opt_p = os.path.join(BASE, 'images', 'lean_' + name)
        im.save(opt_p, 'JPEG', quality=78, optimize=True)
        print(f"Optimized {name}: {os.path.getsize(src_p)//1024} KB -> {os.path.getsize(opt_p)//1024} KB")
        
        with open(opt_p, 'rb') as f:
            data = base64.b64encode(f.read()).decode('utf-8')
            opt_b64[name] = f"data:image/jpeg;base64,{data}"

# Optimize Logo
logo_p = os.path.join(BASE, 'images', 'logo1.png')
with open(logo_p, 'rb') as f:
    b64_logo = f"data:image/png;base64,{base64.b64encode(f.read()).decode('utf-8')}"

# Optimize Partner Logos (scale to max 180px width)
partners_dir = os.path.join(BASE, "images", "partners")
partner_b64 = {}
for f in os.listdir(partners_dir):
    if f.startswith('opt_') or f.startswith('lean_'): continue
    full = os.path.join(partners_dir, f)
    if not os.path.isfile(full): continue
    try:
        im = Image.open(full)
        if im.size[0] > 180:
            h = int(im.size[1] * (180 / im.size[0]))
            im = im.resize((180, h), Image.Resampling.LANCZOS)
        tmp_p = os.path.join(partners_dir, 'lean_' + f)
        if f.endswith('.png'):
            im.save(tmp_p, 'PNG', optimize=True)
            mime = "image/png"
        elif f.endswith('.svg'):
            shutil.copy2(full, tmp_p)
            mime = "image/svg+xml"
        else:
            im.save(tmp_p, 'JPEG', quality=75, optimize=True)
            mime = "image/jpeg"
        
        with open(tmp_p, 'rb') as pf:
            partner_b64[f] = f"data:{mime};base64,{base64.b64encode(pf.read()).decode('utf-8')}"
    except Exception as e:
        with open(full, 'rb') as pf:
            ext = os.path.splitext(f)[1].lower()
            mime = "image/png" if ext == ".png" else "image/jpeg"
            partner_b64[f] = f"data:{mime};base64,{base64.b64encode(pf.read()).decode('utf-8')}"

print(f"Encoded {len(partner_b64)} partner logos.")

# Build Partner Cards
partners_data = [
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

partner_cards_html = []
for file_name, en_name, ar_name in partners_data:
    src_val = partner_b64.get(file_name, f"images/partners/{file_name}")
    card = f'''        <div class="partner-card" data-name-en="{en_name}" data-name-ar="{ar_name}">
          <img loading="lazy" src="{src_val}" alt="" class="partner-logo">
          <span class="partner-label">{en_name}</span>
        </div>'''
    partner_cards_html.append(card)
partners_grid_html = '\n'.join(partner_cards_html)

# Read CSS
css_content = open(os.path.join(BASE, "assets", "style.css"), encoding="utf-8").read()

# Common Header & Footer
def get_header(active_page="home"):
    links = [
        ("index.html", "nav_home", "Home"),
        ("about.html", "nav_about", "About Us"),
        ("services.html", "nav_services", "Services"),
        ("menus.html", "nav_menus", "Menus"),
        ("gallery.html", "nav_gallery", "Gallery"),
        ("events.html", "nav_events", "Events & Projects"),
        ("contact.html", "nav_contact", "Contact")
    ]
    links_html = []
    for href, i18n_key, label in links:
        is_act = " active" if (active_page in href or (active_page == "home" and href == "index.html")) else ""
        links_html.append(f'<li><a href="{href}" class="nav-link{is_act}" data-i18n="{i18n_key}">{label}</a></li>')
    
    return f'''  <div id="splash-screen">
    <img src="{b64_logo}" alt="Awtar United" class="splash-logo">
    <div class="splash-spinner"></div>
  </div>

  <header class="site-header" id="siteHeader">
    <div class="nav-container">
      <a href="index.html" class="logo-link">
        <img src="{b64_logo}" alt="Awtar United - أوتار المتحدة">
      </a>
      <ul class="nav-menu">
        {chr(10).join(links_html)}
      </ul>
      <div class="nav-actions">
        <button class="lang-btn" id="langToggleBtn" type="button" aria-label="Toggle Language">
          <span id="langCurrent">العربية</span>
        </button>
        <a href="get-quote.html" class="btn-gold" data-i18n="cta_quote">Request Quote</a>
        <button class="mobile-nav-toggle" id="mobileMenuBtn" aria-label="Toggle menu">
          <svg width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M3 12h18M3 6h18M3 18h18"/></svg>
        </button>
      </div>
    </div>
  </header>'''

def get_footer():
    return f'''  <footer class="site-footer">
    <div class="container">
      <div class="footer-grid">
        <div class="footer-brand">
          <img src="{b64_logo}" alt="Awtar United">
          <p data-i18n="footer_about">Premier Saudi hospitality and culinary excellence in Riyadh. Orchestrating royal receptions, sovereign summits, and mega-event catering with distinction.</p>
        </div>
        <div class="footer-col">
          <h4 data-i18n="footer_nav">Quick Links</h4>
          <ul class="footer-links">
            <li><a href="index.html" data-i18n="nav_home">Home</a></li>
            <li><a href="about.html" data-i18n="nav_about">About Us</a></li>
            <li><a href="services.html" data-i18n="nav_services">Services</a></li>
            <li><a href="menus.html" data-i18n="nav_menus">Menus</a></li>
            <li><a href="gallery.html" data-i18n="nav_gallery">Gallery</a></li>
            <li><a href="events.html" data-i18n="nav_events">Events & Projects</a></li>
          </ul>
        </div>
        <div class="footer-col">
          <h4 data-i18n="footer_services">Services</h4>
          <ul class="footer-links">
            <li><a href="services.html" data-i18n="srv_mega_title">Mega-Project Operations</a></li>
            <li><a href="services.html" data-i18n="srv_summit_title">Corporate & Sovereign Summits</a></li>
            <li><a href="services.html" data-i18n="srv_banquet_title">Royal Banquets & Receptions</a></li>
            <li><a href="services.html" data-i18n="srv_coffee_title">Executive Coffee Breaks</a></li>
          </ul>
        </div>
        <div class="footer-col">
          <h4 data-i18n="footer_contact">Get in Touch</h4>
          <ul class="footer-contact">
            <li><span>📍</span> Riyadh, Kingdom of Saudi Arabia</li>
            <li><span>📞</span> +966 56 469 2511</li>
            <li><span>✉️</span> info@awtarksa.com</li>
            <li><span>📸</span> <a href="https://www.instagram.com/awtarunited/" target="_blank" rel="noopener">@awtarunited</a></li>
          </ul>
        </div>
      </div>
      <div class="footer-bottom">
        <p>© 2026 Awtar United Catering Services. All Rights Reserved. Riyadh, Saudi Arabia.</p>
        <p>Bespoke Saudi Hospitality & Haute Cuisine</p>
      </div>
    </div>
  </footer>

  <a class="whatsapp-floating" href="https://wa.me/966545264145" target="_blank" rel="noopener" aria-label="Chat on WhatsApp">
    <div class="whatsapp-circle">
      <svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 448 512" width="28" height="28" fill="currentColor">
        <path d="M380.9 97.1C339 55.1 283.2 32 223.9 32c-122.4 0-222 99.6-222 222 0 39.1 10.2 77.3 29.6 111L0 480l117.7-30.9c32.4 17.7 68.9 27 106.1 27h.1c122.3 0 224.1-99.6 224.1-222 0-59.3-25.2-115-67.1-157zm-157 341.6c-33.2 0-65.7-8.9-94-25.7l-6.7-4-69.8 18.3L72 359.2l-4.4-7c-18.5-29.4-28.2-63.3-28.2-98.2 0-101.7 82.8-184.5 184.6-184.5 49.3 0 95.6 19.2 130.4 54.1 34.8 34.9 56.2 81.2 56.1 130.5 0 101.8-84.9 184.6-186.6 184.6zm101.2-138.2c-5.5-2.8-32.8-16.2-37.9-18-5.1-1.9-8.8-2.8-12.5 2.8-3.7 5.6-14.3 18-17.6 21.8-3.2 3.7-6.5 4.2-12 1.4-32.6-16.3-54-29.1-75.5-66-5.7-9.8 5.7-9.1 16.3-30.3 1.8-3.7.9-6.9-.5-9.7-1.4-2.8-12.5-30.1-17.1-41.2-4.5-10.8-9.1-9.3-12.5-9.5-3.2-.2-6.9-.2-10.6-.2-3.7 0-9.7 1.4-14.8 6.9-5.1 5.6-19.4 19-19.4 46.3 0 27.3 19.9 53.7 22.6 57.4 2.8 3.7 39.1 59.7 94.8 83.8 35.2 15.2 49 16.5 66.6 13.9 10.7-1.6 32.8-13.4 37.4-26.4 4.6-13 4.6-24.1 3.2-26.4-1.3-2.5-5-3.9-10.5-6.6z"/>
      </svg>
    </div>
    <span class="whatsapp-tooltip" data-i18n="whatsapp_tooltip">Chat on WhatsApp</span>
  </a>'''

js_engine = open(os.path.join(BASE, "assets", "site.js"), encoding="utf-8").read()

# 1. LEAN index.html
b64_s1 = opt_b64['hero_banquet_luxury.jpg']
b64_s2 = opt_b64['hero_canapes_gourmet.jpg']
b64_s3 = opt_b64['hero_desserts_artisan.jpg']
b64_srv_mega = opt_b64['service_mega_projects.jpg']
b64_srv_summit = opt_b64['service_corporate_summit.jpg']
b64_srv_coffee = opt_b64['service_coffee_break.jpg']

index_html = f'''<!doctype html>
<html lang="en" dir="ltr">
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <title>Awtar United | Luxury Catering & Hospitality in Riyadh</title>
  <meta name="description" content="Premier Saudi royal catering, executive summits, and mega-project dining operations in Riyadh.">
  <link rel="icon" href="{b64_logo}" type="image/png">
  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
  <link href="https://fonts.googleapis.com/css2?family=Manrope:wght@400;500;600;700;800&family=Noto+Sans+Arabic:wght@400;500;600;700;800&family=Playfair+Display:ital,wght@0,600;0,700;0,800;1,600&family=Plus+Jakarta+Sans:wght@400;500;600;700;800&display=swap" rel="stylesheet">
  <style id="awtar-inline-styles">
{css_content}
  </style>
</head>
<body>
{get_header("home")}

  <section class="hero-slider-section">
    <div class="slider-wrapper">
      <div class="slide active">
        <img class="slide-img" src="{b64_s1}" alt="Awtar United Royal Banquet Spread">
        <div class="slide-overlay">
          <div class="slide-content">
            <span class="slide-kicker" data-i18n="hero_kicker_1">ROYAL CATERING & GASTRONOMY</span>
            <h1 class="slide-title" data-i18n="hero_title_1">Crafting Culinary Art for Saudi Arabia's Finest Moments</h1>
            <p class="slide-desc" data-i18n="hero_desc_1">Bespoke royal banquets, sovereign summits, and lavish celebrations orchestrated with culinary excellence.</p>
            <div class="slide-cta-row">
              <a href="get-quote.html" class="btn-gold" data-i18n="cta_quote">Request Quote</a>
              <a href="menus.html" class="btn-outline" style="color: #FFF !important; border-color: rgba(255,255,255,0.4);" data-i18n="cta_explore_menus">Explore Menus</a>
            </div>
          </div>
        </div>
      </div>

      <div class="slide">
        <img class="slide-img" src="{b64_s2}" alt="Awtar United Gourmet Finger Food and Canapés">
        <div class="slide-overlay">
          <div class="slide-content">
            <span class="slide-kicker" data-i18n="hero_kicker_2">GOURMET CANAPÉS & RECEPTIONS</span>
            <h2 class="slide-title" data-i18n="hero_title_2">Exquisite Flavors, Flawless Presentation</h2>
            <p class="slide-desc" data-i18n="hero_desc_2">Artisanal cocktail bites, gourmet finger food, and Michelin-inspired culinary stations for VIP guests.</p>
            <div class="slide-cta-row">
              <a href="get-quote.html" class="btn-gold" data-i18n="cta_quote">Request Quote</a>
              <a href="menus.html" class="btn-outline" style="color: #FFF !important; border-color: rgba(255,255,255,0.4);" data-i18n="cta_explore_menus">Explore Menus</a>
            </div>
          </div>
        </div>
      </div>

      <div class="slide">
        <img class="slide-img" src="{b64_s3}" alt="Awtar United Luxury Desserts and Patisserie">
        <div class="slide-overlay">
          <div class="slide-content">
            <span class="slide-kicker" data-i18n="hero_kicker_3">ARTISANAL PATISSERIE & SWEETS</span>
            <h2 class="slide-title" data-i18n="hero_title_3">A Symphony of Handcrafted Delicacies</h2>
            <p class="slide-desc" data-i18n="hero_desc_3">Saffron cardamom delicacies, pistachio tarts, and luxury French patisserie created by master chefs.</p>
            <div class="slide-cta-row">
              <a href="get-quote.html" class="btn-gold" data-i18n="cta_quote">Request Quote</a>
              <a href="gallery.html" class="btn-outline" style="color: #FFF !important; border-color: rgba(255,255,255,0.4);" data-i18n="nav_gallery">View Gallery</a>
            </div>
          </div>
        </div>
      </div>
    </div>

    <button class="slider-btn slider-prev" aria-label="Previous slide">&#10094;</button>
    <button class="slider-btn slider-next" aria-label="Next slide">&#10095;</button>

    <div class="slider-indicators">
      <button class="indicator active" aria-label="Go to slide 1"></button>
      <button class="indicator" aria-label="Go to slide 2"></button>
      <button class="indicator" aria-label="Go to slide 3"></button>
    </div>
  </section>

  <section class="section-py">
    <div class="container">
      <div class="section-head">
        <div class="section-kicker" data-i18n="services_kicker">WHAT WE ORCHESTRATE</div>
        <h2 class="section-title" data-i18n="services_title">Prestige Catering Services in Riyadh</h2>
        <p class="section-subtitle" data-i18n="services_subtitle">From high-stakes government summits to magnificent royal banquets, our standards define Saudi luxury.</p>
      </div>

      <div class="services-grid">
        <div class="service-card">
          <div class="service-card-media">
            <img loading="lazy" src="{b64_srv_mega}" alt="Mega-Project Logistics">
          </div>
          <div class="service-card-body">
            <h3 class="service-card-title" data-i18n="srv_mega_title">Mega-Project & National Logistics</h3>
            <p class="service-card-desc" data-i18n="srv_mega_desc">End-to-end full scale catering operations, festival villages, and corporate dining logistics across the Kingdom.</p>
            <a href="services.html" class="service-link"><span data-i18n="cta_explore_menus">Learn More</span> &rarr;</a>
          </div>
        </div>

        <div class="service-card">
          <div class="service-card-media">
            <img loading="lazy" src="{b64_srv_summit}" alt="Corporate and Sovereign Summits">
          </div>
          <div class="service-card-body">
            <h3 class="service-card-title" data-i18n="srv_summit_title">Corporate & Sovereign Summits</h3>
            <p class="service-card-desc" data-i18n="srv_summit_desc">Impeccable executive dining for state assemblies, board retreats, ministerial conferences, and VIP receptions.</p>
            <a href="services.html" class="service-link"><span data-i18n="cta_explore_menus">Learn More</span> &rarr;</a>
          </div>
        </div>

        <div class="service-card">
          <div class="service-card-media">
            <img loading="lazy" src="{b64_srv_coffee}" alt="Executive Coffee Breaks & Protocol">
          </div>
          <div class="service-card-body">
            <h3 class="service-card-title" data-i18n="srv_coffee_title">Executive Coffee Breaks & Protocol</h3>
            <p class="service-card-desc" data-i18n="srv_coffee_desc">Signature Saudi Arabic coffee, fine crystal refreshments, artisanal pastries, and bespoke VIP protocol service.</p>
            <a href="services.html" class="service-link"><span data-i18n="cta_explore_menus">Learn More</span> &rarr;</a>
          </div>
        </div>
      </div>
    </div>
  </section>

  <section class="section-py" style="padding-top: 0;">
    <div class="container">
      <div class="showcase-banner">
        <div class="showcase-grid">
          <div>
            <div class="section-kicker" style="color: #E8D5B5;" data-i18n="showcase_kicker">OUR GASTRONOMY PHILOSOPHY</div>
            <h2 class="showcase-title" data-i18n="showcase_title">Culinary Artistry Driven by Authentic Hospitality</h2>
            <p class="showcase-desc" data-i18n="showcase_desc">At Awtar United, every banquet is a bespoke masterpiece. We combine the rich heritage of Saudi warmth with cutting-edge international haute cuisine standards, delivering memorable sensory experiences to over 500,000 guests annually.</p>
            <a href="get-quote.html" class="btn-gold" data-i18n="cta_quote">Request Quote</a>
          </div>
          <div class="stats-row">
            <div class="stat-item">
              <h3 data-i18n="stat_1_num">500K+</h3>
              <p data-i18n="stat_1_lbl">VIP Guests Hosted</p>
            </div>
            <div class="stat-item">
              <h3 data-i18n="stat_2_num">100%</h3>
              <p data-i18n="stat_2_lbl">Sovereign Safety Compliance</p>
            </div>
            <div class="stat-item">
              <h3 data-i18n="stat_3_num">15+</h3>
              <p data-i18n="stat_3_lbl">Years of Culinary Prestige</p>
            </div>
          </div>
        </div>
      </div>
    </div>
  </section>

  <section class="section-py partners-section">
    <div class="container">
      <div class="section-head">
        <div class="section-kicker" data-i18n="partners_kicker">HONORED COLLABORATIONS</div>
        <h2 class="section-title" data-i18n="partners_title">Our Prestigious Partners & Clients</h2>
        <p class="section-subtitle" data-i18n="partners_subtitle">Trusted by Saudi Arabia's leading ministries, sovereign authorities, and corporate giants.</p>
      </div>

      <div class="partners-grid">
{partners_grid_html}
      </div>
    </div>
  </section>

{get_footer()}

  <script id="awtar-inline-script">
{js_engine}
  </script>
</body>
</html>'''

with open(os.path.join(BASE, "index.html"), "w", encoding="utf-8") as f:
    f.write(index_html)
shutil.copy2(os.path.join(BASE, "index.html"), os.path.join(PUBLIC, "index.html"))

# 2. Rebuild other pages with lean images
# about.html
about_html = f'''<!doctype html>
<html lang="en" dir="ltr">
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <title>About Us | Awtar United Catering & Hospitality</title>
  <meta name="description" content="Discover Awtar United - Riyadh's leading culinary and hospitality company.">
  <link rel="icon" href="{b64_logo}" type="image/png">
  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
  <link href="https://fonts.googleapis.com/css2?family=Manrope:wght@400;500;600;700;800&family=Noto+Sans+Arabic:wght@400;500;600;700;800&family=Playfair+Display:ital,wght@0,600;0,700;0,800;1,600&family=Plus+Jakarta+Sans:wght@400;500;600;700;800&display=swap" rel="stylesheet">
  <style id="awtar-inline-styles">
{css_content}
  </style>
</head>
<body>
{get_header("about")}

  <section style="background: linear-gradient(rgba(18,18,18,0.5), rgba(18,18,18,0.7)), url('{b64_s1}') center/cover; padding: 10rem 0 5rem 0; color: #FFF; text-align: center;">
    <div class="container">
      <span class="slide-kicker" data-i18n="nav_about">ABOUT AWTAR UNITED</span>
      <h1 style="font-size: 3.2rem; color: #FFF; margin-bottom: 1rem;">Culinary Excellence & Authentic Saudi Hospitality</h1>
      <p style="max-width: 680px; margin: 0 auto; font-size: 1.15rem; color: rgba(255,255,255,0.85);">Delivering state banquets, high-profile summits, and signature culinary experiences across Riyadh and the Kingdom.</p>
    </div>
  </section>

  <section class="section-py">
    <div class="container">
      <div style="display: grid; grid-template-columns: 1fr 1fr; gap: 4rem; align-items: center;">
        <div>
          <div class="section-kicker">HERITAGE & VISION</div>
          <h2 class="section-title">Setting the Standard for Fine Saudi Gastronomy</h2>
          <p style="font-size: 1.05rem; margin-bottom: 1.5rem; color: var(--text-body);">Founded in Riyadh, Awtar United has emerged as the premier partner of choice for royal receptions, sovereign ministries, and Fortune 500 corporate assemblies.</p>
          <p style="font-size: 1.05rem; margin-bottom: 2rem; color: var(--text-body);">Our master chefs blend age-old Saudi hospitality traditions with world-class French culinary techniques, operating out of HACCP and ISO 22000 certified central production kitchens in Riyadh.</p>
          <a href="get-quote.html" class="btn-gold" data-i18n="cta_quote">Plan Your Event With Us</a>
        </div>
        <div>
          <img style="border-radius: var(--radius-lg); box-shadow: var(--shadow-hover);" src="{b64_srv_mega}" alt="Awtar United Kitchen Operations">
        </div>
      </div>
    </div>
  </section>

{get_footer()}

  <script id="awtar-inline-script">
{js_engine}
  </script>
</body>
</html>'''

with open(os.path.join(BASE, "about.html"), "w", encoding="utf-8") as f:
    f.write(about_html)
shutil.copy2(os.path.join(BASE, "about.html"), os.path.join(PUBLIC, "about.html"))

# services.html
services_html = f'''<!doctype html>
<html lang="en" dir="ltr">
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <title>Catering Services | Awtar United Riyadh</title>
  <meta name="description" content="Explore our bespoke royal catering and event services in Riyadh.">
  <link rel="icon" href="{b64_logo}" type="image/png">
  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
  <link href="https://fonts.googleapis.com/css2?family=Manrope:wght@400;500;600;700;800&family=Noto+Sans+Arabic:wght@400;500;600;700;800&family=Playfair+Display:ital,wght@0,600;0,700;0,800;1,600&family=Plus+Jakarta+Sans:wght@400;500;600;700;800&display=swap" rel="stylesheet">
  <style id="awtar-inline-styles">
{css_content}
  </style>
</head>
<body>
{get_header("services")}

  <section style="background: linear-gradient(rgba(18,18,18,0.5), rgba(18,18,18,0.7)), url('{b64_srv_summit}') center/cover; padding: 10rem 0 5rem 0; color: #FFF; text-align: center;">
    <div class="container">
      <span class="slide-kicker" data-i18n="nav_services">OUR CAPABILITIES</span>
      <h1 style="font-size: 3.2rem; color: #FFF; margin-bottom: 1rem;" data-i18n="services_title">Prestige Catering Services in Riyadh</h1>
      <p style="max-width: 680px; margin: 0 auto; font-size: 1.15rem; color: rgba(255,255,255,0.85);" data-i18n="services_subtitle">From high-stakes government summits to magnificent royal banquets, our standards define Saudi luxury.</p>
    </div>
  </section>

  <section class="section-py">
    <div class="container">
      <div class="services-grid">
        <div class="service-card">
          <div class="service-card-media"><img src="{b64_srv_mega}" alt="Mega-Project Logistics"></div>
          <div class="service-card-body">
            <h3 class="service-card-title" data-i18n="srv_mega_title">Mega-Project & National Logistics</h3>
            <p class="service-card-desc" data-i18n="srv_mega_desc">End-to-end full scale catering operations, festival villages, and corporate dining logistics across the Kingdom.</p>
            <a href="get-quote.html" class="btn-gold" data-i18n="cta_quote">Inquire Now</a>
          </div>
        </div>

        <div class="service-card">
          <div class="service-card-media"><img src="{b64_srv_summit}" alt="Corporate and Sovereign Summits"></div>
          <div class="service-card-body">
            <h3 class="service-card-title" data-i18n="srv_summit_title">Corporate & Sovereign Summits</h3>
            <p class="service-card-desc" data-i18n="srv_summit_desc">Impeccable executive dining for state assemblies, board retreats, ministerial conferences, and VIP receptions.</p>
            <a href="get-quote.html" class="btn-gold" data-i18n="cta_quote">Inquire Now</a>
          </div>
        </div>

        <div class="service-card">
          <div class="service-card-media"><img src="{b64_srv_coffee}" alt="Executive Coffee Breaks & Protocol"></div>
          <div class="service-card-body">
            <h3 class="service-card-title" data-i18n="srv_coffee_title">Executive Coffee Breaks & Protocol</h3>
            <p class="service-card-desc" data-i18n="srv_coffee_desc">Signature Saudi Arabic coffee, fine crystal refreshments, artisanal pastries, and bespoke VIP protocol service.</p>
            <a href="get-quote.html" class="btn-gold" data-i18n="cta_quote">Inquire Now</a>
          </div>
        </div>
      </div>
    </div>
  </section>

{get_footer()}

  <script id="awtar-inline-script">
{js_engine}
  </script>
</body>
</html>'''

with open(os.path.join(BASE, "services.html"), "w", encoding="utf-8") as f:
    f.write(services_html)
shutil.copy2(os.path.join(BASE, "services.html"), os.path.join(PUBLIC, "services.html"))

# menus.html
menus_html = f'''<!doctype html>
<html lang="en" dir="ltr">
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <title>Gourmet Menus | Awtar United Riyadh</title>
  <meta name="description" content="Explore handcrafted catering menus by Awtar United.">
  <link rel="icon" href="{b64_logo}" type="image/png">
  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
  <link href="https://fonts.googleapis.com/css2?family=Manrope:wght@400;500;600;700;800&family=Noto+Sans+Arabic:wght@400;500;600;700;800&family=Playfair+Display:ital,wght@0,600;0,700;0,800;1,600&family=Plus+Jakarta+Sans:wght@400;500;600;700;800&display=swap" rel="stylesheet">
  <style id="awtar-inline-styles">
{css_content}
  </style>
</head>
<body>
{get_header("menus")}

  <section style="background: linear-gradient(rgba(18,18,18,0.5), rgba(18,18,18,0.7)), url('{b64_s3}') center/cover; padding: 10rem 0 5rem 0; color: #FFF; text-align: center;">
    <div class="container">
      <span class="slide-kicker" data-i18n="nav_menus">OUR CULINARY REPERTOIRE</span>
      <h1 style="font-size: 3.2rem; color: #FFF; margin-bottom: 1rem;">Gourmet Menus Crafted for Royalty</h1>
      <p style="max-width: 680px; margin: 0 auto; font-size: 1.15rem; color: rgba(255,255,255,0.85);">Explore our bespoke selections from traditional Saudi feasts to contemporary international gastronomy.</p>
    </div>
  </section>

  <section class="section-py">
    <div class="container">
      <div class="services-grid">
        <div class="service-card">
          <div class="service-card-media"><img src="{b64_s1}" alt="Royal Saudi Feast Menu"></div>
          <div class="service-card-body">
            <h3 class="service-card-title">Royal Saudi Feast Menu</h3>
            <p class="service-card-desc">Tender Najdi lamb with spiced saffron rice, jareesh, qursan, smoked meat platters, and heritage Saudi delicacies.</p>
            <a href="get-quote.html" class="btn-gold">Request Menu PDF</a>
          </div>
        </div>

        <div class="service-card">
          <div class="service-card-media"><img src="{b64_s2}" alt="VIP Canapés & Finger Food"></div>
          <div class="service-card-body">
            <h3 class="service-card-title">Gourmet Cocktail Canapés</h3>
            <p class="service-card-desc">Truffle arancini, smoked salmon blinis, Angus beef sliders, and micro-herbed savory cones.</p>
            <a href="get-quote.html" class="btn-gold">Request Menu PDF</a>
          </div>
        </div>

        <div class="service-card">
          <div class="service-card-media"><img src="{b64_s3}" alt="Artisanal Desserts & Sweets"></div>
          <div class="service-card-body">
            <h3 class="service-card-title">Artisanal Desserts & Patisserie</h3>
            <p class="service-card-desc">Raspberry dark chocolate mousse, saffron cardamom tartlets, pistachio baklava towers, and artisanal macarons.</p>
            <a href="get-quote.html" class="btn-gold">Request Menu PDF</a>
          </div>
        </div>
      </div>
    </div>
  </section>

{get_footer()}

  <script id="awtar-inline-script">
{js_engine}
  </script>
</body>
</html>'''

with open(os.path.join(BASE, "menus.html"), "w", encoding="utf-8") as f:
    f.write(menus_html)
shutil.copy2(os.path.join(BASE, "menus.html"), os.path.join(PUBLIC, "menus.html"))

# events.html
events_html = f'''<!doctype html>
<html lang="en" dir="ltr">
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <title>Events & Mega Projects | Awtar United Riyadh</title>
  <meta name="description" content="View premier events and national summits catered by Awtar United.">
  <link rel="icon" href="{b64_logo}" type="image/png">
  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
  <link href="https://fonts.googleapis.com/css2?family=Manrope:wght@400;500;600;700;800&family=Noto+Sans+Arabic:wght@400;500;600;700;800&family=Playfair+Display:ital,wght@0,600;0,700;0,800;1,600&family=Plus+Jakarta+Sans:wght@400;500;600;700;800&display=swap" rel="stylesheet">
  <style id="awtar-inline-styles">
{css_content}
  </style>
</head>
<body>
{get_header("events")}

  <section style="background: linear-gradient(rgba(18,18,18,0.5), rgba(18,18,18,0.7)), url('{b64_srv_mega}') center/cover; padding: 10rem 0 5rem 0; color: #FFF; text-align: center;">
    <div class="container">
      <span class="slide-kicker" data-i18n="nav_events">PRESTIGE PORTFOLIO</span>
      <h1 style="font-size: 3.2rem; color: #FFF; margin-bottom: 1rem;">Events & Mega-Project Operations</h1>
      <p style="max-width: 680px; margin: 0 auto; font-size: 1.15rem; color: rgba(255,255,255,0.85);">Delivering high-capacity catering logistics for Saudi Arabia's most prestigious gatherings.</p>
    </div>
  </section>

  <section class="section-py">
    <div class="container">
      <div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(350px, 1fr)); gap: 2.5rem;">
        <div style="background: #FFF; border-radius: var(--radius-lg); overflow: hidden; box-shadow: var(--shadow-card);">
          <img style="width: 100%; height: 260px; object-fit: cover;" src="{b64_s1}" alt="World Defence Show Catering">
          <div style="padding: 2rem;">
            <span style="color: var(--gold-dark); font-weight: 700; font-size: 0.85rem;">DEFENCE & SOVEREIGN</span>
            <h3 style="font-size: 1.4rem; margin: 0.5rem 0 1rem 0;">World Defence Show VIP Hospitality</h3>
            <p style="font-size: 0.95rem; color: var(--text-body);">Full-scale protocol hospitality and VIP chalets catering for international dignitaries and military leaders.</p>
          </div>
        </div>

        <div style="background: #FFF; border-radius: var(--radius-lg); overflow: hidden; box-shadow: var(--shadow-card);">
          <img style="width: 100%; height: 260px; object-fit: cover;" src="{b64_srv_summit}" alt="Ministry Summits">
          <div style="padding: 2rem;">
            <span style="color: var(--gold-dark); font-weight: 700; font-size: 0.85rem;">GOVERNMENT FORUMS</span>
            <h3 style="font-size: 1.4rem; margin: 0.5rem 0 1rem 0;">Ministerial & Sovereign Conclaves</h3>
            <p style="font-size: 0.95rem; color: var(--text-body);">High-level diplomatic dining for the Ministry of Economy, Ministry of Industry, and sovereign partners.</p>
          </div>
        </div>

        <div style="background: #FFF; border-radius: var(--radius-lg); overflow: hidden; box-shadow: var(--shadow-card);">
          <img style="width: 100%; height: 260px; object-fit: cover;" src="{b64_s2}" alt="National Festival Villages">
          <div style="padding: 2rem;">
            <span style="color: var(--gold-dark); font-weight: 700; font-size: 0.85rem;">FESTIVALS & PUBLIC SCALE</span>
            <h3 style="font-size: 1.4rem; margin: 0.5rem 0 1rem 0;">Mega-Project Dining Villages</h3>
            <p style="font-size: 0.95rem; color: var(--text-body);">Multi-kitchen operations feeding thousands of guests with continuous gourmet quality and strict safety protocols.</p>
          </div>
        </div>
      </div>
    </div>
  </section>

{get_footer()}

  <script id="awtar-inline-script">
{js_engine}
  </script>
</body>
</html>'''

with open(os.path.join(BASE, "events.html"), "w", encoding="utf-8") as f:
    f.write(events_html)
shutil.copy2(os.path.join(BASE, "events.html"), os.path.join(PUBLIC, "events.html"))

# gallery.html
gallery_html = f'''<!doctype html>
<html lang="en" dir="ltr">
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <title>Gallery | Awtar United Riyadh</title>
  <meta name="description" content="View our visual gallery of royal catering and event presentations.">
  <link rel="icon" href="{b64_logo}" type="image/png">
  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
  <link href="https://fonts.googleapis.com/css2?family=Manrope:wght@400;500;600;700;800&family=Noto+Sans+Arabic:wght@400;500;600;700;800&family=Playfair+Display:ital,wght@0,600;0,700;0,800;1,600&family=Plus+Jakarta+Sans:wght@400;500;600;700;800&display=swap" rel="stylesheet">
  <style id="awtar-inline-styles">
{css_content}
  </style>
</head>
<body>
{get_header("gallery")}

  <section style="background: linear-gradient(rgba(18,18,18,0.5), rgba(18,18,18,0.7)), url('{b64_s2}') center/cover; padding: 10rem 0 5rem 0; color: #FFF; text-align: center;">
    <div class="container">
      <span class="slide-kicker" data-i18n="nav_gallery">VISUAL SHOWCASE</span>
      <h1 style="font-size: 3.2rem; color: #FFF; margin-bottom: 1rem;">The Art of Culinary Presentation</h1>
      <p style="max-width: 680px; margin: 0 auto; font-size: 1.15rem; color: rgba(255,255,255,0.85);">A glimpse into our royal spreads, gourmet bites, and artisanal sweets.</p>
    </div>
  </section>

  <section class="section-py">
    <div class="container">
      <div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(360px, 1fr)); gap: 1.5rem;">
        <div style="border-radius: var(--radius-md); overflow: hidden; box-shadow: var(--shadow-card);">
          <img style="width: 100%; height: 320px; object-fit: cover;" src="{b64_s1}" alt="Royal Banquet Spread">
        </div>
        <div style="border-radius: var(--radius-md); overflow: hidden; box-shadow: var(--shadow-card);">
          <img style="width: 100%; height: 320px; object-fit: cover;" src="{b64_s2}" alt="Gourmet Canapes">
        </div>
        <div style="border-radius: var(--radius-md); overflow: hidden; box-shadow: var(--shadow-card);">
          <img style="width: 100%; height: 320px; object-fit: cover;" src="{b64_s3}" alt="Artisan Desserts">
        </div>
        <div style="border-radius: var(--radius-md); overflow: hidden; box-shadow: var(--shadow-card);">
          <img style="width: 100%; height: 320px; object-fit: cover;" src="{b64_srv_coffee}" alt="VIP Coffee Break">
        </div>
        <div style="border-radius: var(--radius-md); overflow: hidden; box-shadow: var(--shadow-card);">
          <img style="width: 100%; height: 320px; object-fit: cover;" src="{b64_srv_summit}" alt="Corporate Summit">
        </div>
        <div style="border-radius: var(--radius-md); overflow: hidden; box-shadow: var(--shadow-card);">
          <img style="width: 100%; height: 320px; object-fit: cover;" src="{b64_srv_mega}" alt="Mega Project Setup">
        </div>
      </div>
    </div>
  </section>

{get_footer()}

  <script id="awtar-inline-script">
{js_engine}
  </script>
</body>
</html>'''

with open(os.path.join(BASE, "gallery.html"), "w", encoding="utf-8") as f:
    f.write(gallery_html)
shutil.copy2(os.path.join(BASE, "gallery.html"), os.path.join(PUBLIC, "gallery.html"))

# contact.html & get-quote.html
contact_html = f'''<!doctype html>
<html lang="en" dir="ltr">
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <title>Contact Us | Awtar United Riyadh</title>
  <meta name="description" content="Get in touch with Awtar United catering team in Riyadh.">
  <link rel="icon" href="{b64_logo}" type="image/png">
  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
  <link href="https://fonts.googleapis.com/css2?family=Manrope:wght@400;500;600;700;800&family=Noto+Sans+Arabic:wght@400;500;600;700;800&family=Playfair+Display:ital,wght@0,600;0,700;0,800;1,600&family=Plus+Jakarta+Sans:wght@400;500;600;700;800&display=swap" rel="stylesheet">
  <style id="awtar-inline-styles">
{css_content}
  </style>
</head>
<body>
{get_header("contact")}

  <section style="background: linear-gradient(rgba(18,18,18,0.5), rgba(18,18,18,0.7)), url('{b64_srv_summit}') center/cover; padding: 10rem 0 5rem 0; color: #FFF; text-align: center;">
    <div class="container">
      <span class="slide-kicker" data-i18n="nav_contact">CONNECT WITH US</span>
      <h1 style="font-size: 3.2rem; color: #FFF; margin-bottom: 1rem;">Let Us Elevate Your Next Event</h1>
      <p style="max-width: 680px; margin: 0 auto; font-size: 1.15rem; color: rgba(255,255,255,0.85);">Our team of event planners and executive chefs is at your service across Riyadh.</p>
    </div>
  </section>

  <section class="section-py">
    <div class="container">
      <div style="display: grid; grid-template-columns: 1fr 1fr; gap: 4rem;">
        <div>
          <div class="section-kicker">DIRECT CONTACT</div>
          <h2 class="section-title">Headquarters in Riyadh</h2>
          <div style="margin-top: 2rem; display: flex; flex-direction: column; gap: 1.5rem; font-size: 1.05rem;">
            <div><strong>Location:</strong> Riyadh, Kingdom of Saudi Arabia</div>
            <div><strong>Phone / Call:</strong> +966 56 469 2511</div>
            <div><strong>WhatsApp Direct:</strong> +966 54 526 4145</div>
            <div><strong>Email:</strong> info@awtarksa.com</div>
            <div><strong>Instagram:</strong> <a href="https://www.instagram.com/awtarunited/" target="_blank" style="color: var(--gold-dark); font-weight: 700;">@awtarunited</a></div>
          </div>
          <div style="margin-top: 2.5rem;">
            <a href="https://wa.me/966545264145" target="_blank" class="btn-gold">Chat with Us on WhatsApp</a>
          </div>
        </div>
        <div style="background: #FFF; padding: 3rem; border-radius: var(--radius-lg); box-shadow: var(--shadow-card); border: 1px solid var(--cream-line);">
          <h3 style="font-size: 1.5rem; margin-bottom: 1.5rem;">Send a Message</h3>
          <form onsubmit="alert('Thank you! Your message has been received.'); return false;" style="display: flex; flex-direction: column; gap: 1.2rem;">
            <input type="text" placeholder="Your Name" required style="padding: 0.85rem 1.2rem; border-radius: var(--radius-sm); border: 1px solid var(--cream-line); font-family: inherit;">
            <input type="email" placeholder="Email Address" required style="padding: 0.85rem 1.2rem; border-radius: var(--radius-sm); border: 1px solid var(--cream-line); font-family: inherit;">
            <input type="tel" placeholder="Phone / WhatsApp Number" required style="padding: 0.85rem 1.2rem; border-radius: var(--radius-sm); border: 1px solid var(--cream-line); font-family: inherit;">
            <textarea placeholder="Event Details, Date & Guest Count" rows="4" required style="padding: 0.85rem 1.2rem; border-radius: var(--radius-sm); border: 1px solid var(--cream-line); font-family: inherit;"></textarea>
            <button type="submit" class="btn-gold" style="align-self: flex-start;">Send Inquiry</button>
          </form>
        </div>
      </div>
    </div>
  </section>

{get_footer()}

  <script id="awtar-inline-script">
{js_engine}
  </script>
</body>
</html>'''

with open(os.path.join(BASE, "contact.html"), "w", encoding="utf-8") as f:
    f.write(contact_html)
shutil.copy2(os.path.join(BASE, "contact.html"), os.path.join(PUBLIC, "contact.html"))

quote_html = contact_html.replace("Contact Us", "Request a Quote").replace("CONNECT WITH US", "VIP QUOTATION")
with open(os.path.join(BASE, "get-quote.html"), "w", encoding="utf-8") as f:
    f.write(quote_html)
shutil.copy2(os.path.join(BASE, "get-quote.html"), os.path.join(PUBLIC, "get-quote.html"))

print("All pages successfully rebuilt with lean, ultra-crisp web assets!")
