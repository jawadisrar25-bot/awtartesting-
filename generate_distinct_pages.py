import os
import json
import urllib.parse

ROOT_DIR = r"C:\Users\HP\Downloads\awtar-united\awtar-united"
PUBLIC_DIR = os.path.join(ROOT_DIR, "public")

# Load partners
with open(os.path.join(ROOT_DIR, "partners_data.json"), "r", encoding="utf-8") as f:
    partners_list = json.load(f)

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
    if "stage.maaal.com" in p["image"]:
        p["image"] = "images/partners/16_ministry_of_defence.svg"
    p['name_ar'] = ar_partners.get(p['name_en'], p['name_en'])

WHATSAPP_ICON_SVG = """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 448 512" width="28" height="28" fill="currentColor">
  <path d="M380.9 97.1C339 55.1 283.2 32 223.9 32c-122.4 0-222 99.6-222 222 0 39.1 10.2 77.3 29.6 111L0 480l117.7-30.9c32.4 17.7 68.9 27 106.1 27h.1c122.3 0 224.1-99.6 224.1-222 0-59.3-25.2-115-67.1-157zm-157 341.6c-33.2 0-65.7-8.9-94-25.7l-6.7-4-69.8 18.3L72 359.2l-4.4-7c-18.5-29.4-28.2-63.3-28.2-98.2 0-101.7 82.8-184.5 184.6-184.5 49.3 0 95.6 19.2 130.4 54.1 34.8 34.9 56.2 81.2 56.1 130.5 0 101.8-84.9 184.6-186.6 184.6zm101.2-138.2c-5.5-2.8-32.8-16.2-37.9-18-5.1-1.9-8.8-2.8-12.5 2.8-3.7 5.6-14.3 18-17.6 21.8-3.2 3.7-6.5 4.2-12 1.4-32.6-16.3-54-29.1-75.5-66-5.7-9.8 5.7-9.1 16.3-30.3 1.8-3.7.9-6.9-.5-9.7-1.4-2.8-12.5-30.1-17.1-41.2-4.5-10.8-9.1-9.3-12.5-9.5-3.2-.2-6.9-.2-10.6-.2-3.7 0-9.7 1.4-14.8 6.9-5.1 5.6-19.4 19-19.4 46.3 0 27.3 19.9 53.7 22.6 57.4 2.8 3.7 39.1 59.7 94.8 83.8 35.2 15.2 49 16.5 66.6 13.9 10.7-1.6 32.8-13.4 37.4-26.4 4.6-13 4.6-24.1 3.2-26.4-1.3-2.5-5-3.9-10.5-6.6z"/>
</svg>"""

def render_splash():
    return """<!-- CLEAN, LIGHT SPLASH SCREEN -->
<div id="site-splash-loader" class="splash-loader">
  <div class="splash-inner">
    <div class="splash-logo-wrap">
      <img src="images/logo1.png" alt="Awtar United" class="splash-logo">
    </div>
    <div class="splash-spinner"></div>
    <p class="splash-text" data-i18n="splash_text">Awtar United Catering & Hospitality</p>
  </div>
</div>"""

def render_header(active_slug):
    nav_items = [
        ('index', 'nav_home', 'Home'),
        ('about', 'nav_about', 'About Us'),
        ('services', 'nav_services', 'Services'),
        ('menus', 'nav_menus', 'Menus'),
        ('gallery', 'nav_gallery', 'Gallery'),
        ('events', 'nav_events', 'Events & Projects'),
        ('contact', 'nav_contact', 'Contact')
    ]
    links_html = []
    for slug, i18n_key, fallback in nav_items:
        act = ' active' if slug == active_slug else ''
        fname = f"{slug}.html"
        links_html.append(f'<a class="nav-link{act}" href="{fname}" data-i18n="{i18n_key}">{fallback}</a>')
    links_str = '\n        '.join(links_html)

    # For header actions: on home page, keep navigation clean.
    return f"""<header class="site-header">
  <div class="container header-inner">
    <a class="brand-logo" href="index.html">
      <img src="images/logo1.png" alt="Awtar United - أوتار المتحدة">
    </a>

    <nav id="nav-menu" class="nav-menu">
        {links_str}
    </nav>

    <div class="header-actions">
      <button id="lang-toggle-btn" class="lang-btn" aria-label="Toggle language">
        <span class="lang-label" data-i18n="lang_btn">العربية</span>
      </button>
      <a class="btn btn-gold" href="get-quote.html" data-i18n="nav_quote">Get a Quote</a>
      <button id="nav-toggle-btn" class="nav-toggle-btn" aria-label="Toggle navigation">☰</button>
    </div>
  </div>
</header>"""

def render_footer():
    return f"""<footer class="site-footer">
  <div class="container footer-grid">
    <div class="footer-brand">
      <a href="index.html"><img src="images/logo1.png" alt="Awtar United"></a>
      <p data-i18n="footer_about">Awtar United brings together culinary excellence and authentic Saudi hospitality for corporate events, private celebrations, and mega projects in Riyadh.</p>
    </div>

    <div class="footer-col">
      <h4 data-i18n="footer_quick_links">Quick Navigation</h4>
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
      <h4 data-i18n="footer_services_title">Services</h4>
      <ul class="footer-links">
        <li><a href="services.html" data-i18n="service_1_title">Mega Project Catering</a></li>
        <li><a href="services.html" data-i18n="service_2_title">Corporate Catering</a></li>
        <li><a href="services.html" data-i18n="service_3_title">Royal Buffets</a></li>
        <li><a href="services.html" data-i18n="service_4_title">Coffee Break</a></li>
        <li><a href="services.html" data-i18n="service_6_title">VIP Hospitality</a></li>
      </ul>
    </div>

    <div class="footer-col">
      <h4 data-i18n="footer_contact_title">Get in Touch</h4>
      <ul class="footer-links">
        <li><a href="tel:+966564692511">+966 56 469 2511</a></li>
        <li><a href="mailto:info@awtarksa.com">info@awtarksa.com</a></li>
        <li><span data-i18n="contact_address_val">Riyadh, Kingdom of Saudi Arabia</span></li>
        <li><a href="https://www.instagram.com/awtarunited/" target="_blank" rel="noopener">@awtarunited</a></li>
      </ul>
    </div>
  </div>

  <div class="container copyright-bar">
    <p data-i18n="footer_copyright">© 2026 Awtar United Catering Services. All Rights Reserved. Riyadh, Saudi Arabia.</p>
  </div>
</footer>

<!-- Proper WhatsApp Floating Button -->
<a class="whatsapp-floating" href="https://wa.me/966545264145" target="_blank" rel="noopener" aria-label="Contact on WhatsApp">
  <div class="whatsapp-circle">
    {WHATSAPP_ICON_SVG}
  </div>
  <span class="whatsapp-tooltip" data-i18n="whatsapp_tooltip">Chat on WhatsApp</span>
</a>"""

def render_partners_section():
    cards_html = []
    for p in partners_list:
        cards_html.append(f"""<div class="partner-card" data-name-en="{p['name_en']}" data-name-ar="{p['name_ar']}">
  <img loading="lazy" src="{p['image']}" alt="{p['name_en']}">
  <span>{p['name_en']}</span>
</div>""")
    cards_str = '\n    '.join(cards_html)

    return f"""<section class="section-py partners-section">
  <div class="container">
    <div class="section-head">
      <div class="section-kicker" data-i18n="partners_kicker">Honored Collaborations</div>
      <h2 class="section-title" data-i18n="partners_title">Our Prestigious Partners & Clients</h2>
      <p class="section-subtitle" data-i18n="partners_subtitle">Proud to collaborate with Saudi Arabia's most esteemed ministries, sovereign institutions, and corporate giants.</p>
    </div>
    <div class="partners-grid">
    {cards_str}
    </div>
  </div>
</section>"""

def render_stats_bar():
    return """<section class="stats-bar">
  <div class="container stats-grid">
    <div class="stat-item">
      <h3 data-i18n="stat_years_num">5+</h3>
      <p data-i18n="stat_years_label">Years of Excellence</p>
    </div>
    <div class="stat-item">
      <h3 data-i18n="stat_clients_num">500+</h3>
      <p data-i18n="stat_clients_label">Prestigious Clients</p>
    </div>
    <div class="stat-item">
      <h3 data-i18n="stat_events_num">5,000+</h3>
      <p data-i18n="stat_events_label">Flawlessly Catered Events</p>
    </div>
    <div class="stat-item">
      <h3 data-i18n="stat_team_num">100%</h3>
      <p data-i18n="stat_team_label">Saudi & International Standards</p>
    </div>
  </div>
</section>"""

def render_video_section():
    return """<section class="section-py video-section">
  <div class="container">
    <div class="section-head">
      <div class="section-kicker" data-i18n="video_kicker">In Action</div>
      <h2 class="section-title" data-i18n="video_title">Witness Our Craft & Precision</h2>
      <p class="section-subtitle" data-i18n="video_subtitle">Experience the preparation and grandeur of Awtar United.</p>
    </div>
    <div class="video-grid">
      <div class="video-card">
        <div class="video-player-wrap">
          <video controls preload="metadata" poster="images/awtar_photos/awtar_001.jpg">
            <source src="media/video_1.mp4" type="video/mp4">
            Your browser does not support the video tag.
          </video>
        </div>
        <div class="video-info">
          <h3 data-i18n="video_1_title">Culinary Excellence & Preparation</h3>
          <p data-i18n="video_1_desc">Watch our expert culinary team prepare lavish spreads using fresh ingredients.</p>
        </div>
      </div>

      <div class="video-card">
        <div class="video-player-wrap">
          <video controls preload="metadata" poster="images/awtar_photos/awtar_002.jpg">
            <source src="media/video_2.mp4" type="video/mp4">
            Your browser does not support the video tag.
          </video>
        </div>
        <div class="video-info">
          <h3 data-i18n="video_2_title">Live Event & Banquet Hospitality</h3>
          <p data-i18n="video_2_desc">Live banquet setups, welcoming guests, and delivering service.</p>
        </div>
      </div>
    </div>
  </div>
</section>"""

def wrap_html(title, desc, body_content, active_slug):
    splash = render_splash()
    header = render_header(active_slug)
    footer = render_footer()
    return f"""<!doctype html>
<html lang="en" dir="ltr">
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <title>{title}</title>
  <meta name="description" content="{desc}">
  <meta property="og:title" content="{title}">
  <meta property="og:description" content="{desc}">
  <meta property="og:image" content="images/home_slide_2_cheesecake.jpg">
  <link rel="icon" href="images/logo1.png" type="image/png">
  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
  <link href="https://fonts.googleapis.com/css2?family=Manrope:wght@400;500;600;700;800&family=Noto+Sans+Arabic:wght@400;500;600;700;800&family=Playfair+Display:ital,wght@0,600;0,700;0,800;1,600&display=swap" rel="stylesheet">
  <link rel="stylesheet" href="assets/style.css">
  <script defer src="assets/site.js"></script>
</head>
<body>
{splash}
{header}
<main>
{body_content}
</main>
{footer}
</body>
</html>"""

# 1. INDEX.HTML (HOME)
# - Removed "Premier Hospitality in Riyadh"
# - Removed "Explore Menus" / "View Menus"
# - Banner has exactly 1 clean CTA button: "Request a Quote"
# - Removed crowded text paragraphs from the 3 cards
# - Partners section ONLY on Home screen
def build_index():
    slider_html = """<section class="hero-slider-section home-hero">
  <div class="slider-container">
    <div class="slide active"><img class="slide-img" src="images/home_slide_1_brownies.jpg" alt="Awtar United Gourmet Desserts"></div>
    <div class="slide"><img class="slide-img" src="images/home_slide_2_cheesecake.jpg" alt="Awtar United Mini Cheesecakes"></div>
    <div class="slide"><img class="slide-img" src="images/home_slide_3_canapes.jpg" alt="Awtar United Canapés & Banquets"></div>
  </div>
  <div class="slider-overlay"></div>
  <div class="container hero-content">
    <h1 class="hero-title" data-i18n="hero_title_1">Refined Taste, Unforgettable Moments</h1>
    <p class="hero-desc" data-i18n="hero_desc_1">Luxury catering and royal hospitality for corporate summits, VIP celebrations and mega projects across the Kingdom.</p>
    <div class="hero-actions">
      <a class="btn btn-gold" href="get-quote.html" data-i18n="btn_quote">Request a Quote</a>
    </div>
  </div>
  <button class="slider-arrow slider-prev" aria-label="Previous Slide">‹</button>
  <button class="slider-arrow slider-next" aria-label="Next Slide">›</button>
  <div class="slider-dots"></div>
</section>"""

    # Uncrowded clean cards: NO long paragraphs!
    services_preview = """<section class="section-py">
  <div class="container">
    <div class="section-head">
      <div class="section-kicker" data-i18n="services_kicker">Culinary & Hospitality Solutions</div>
      <h2 class="section-title" data-i18n="services_title">Exceptional Services Tailored for You</h2>
    </div>
    <div class="cards-grid">
      <article class="luxury-card">
        <div class="card-img-wrap"><img loading="lazy" src="images/awtar_photos/awtar_001.jpg" alt="Mega Project Catering"></div>
        <div class="card-body">
          <h3 class="card-title" data-i18n="service_1_title">Mega Project Catering</h3>
          <div class="card-footer"><a class="btn btn-outline-gold" href="get-quote.html?service=Mega%20Project%20Catering" data-i18n="btn_quote">Request a Quote</a></div>
        </div>
      </article>

      <article class="luxury-card">
        <div class="card-img-wrap"><img loading="lazy" src="images/awtar_photos/awtar_002.jpg" alt="Corporate Catering"></div>
        <div class="card-body">
          <h3 class="card-title" data-i18n="service_2_title">Corporate & Summit Catering</h3>
          <div class="card-footer"><a class="btn btn-outline-gold" href="get-quote.html?service=Corporate%20Catering" data-i18n="btn_quote">Request a Quote</a></div>
        </div>
      </article>

      <article class="luxury-card">
        <div class="card-img-wrap"><img loading="lazy" src="images/awtar_photos/awtar_003.jpg" alt="Royal Buffets"></div>
        <div class="card-body">
          <h3 class="card-title" data-i18n="service_3_title">Royal Buffets & VIP Receptions</h3>
          <div class="card-footer"><a class="btn btn-outline-gold" href="get-quote.html?service=Royal%20Buffets" data-i18n="btn_quote">Request a Quote</a></div>
        </div>
      </article>
    </div>
  </div>
</section>"""

    body = f"{slider_html}\n{render_stats_bar()}\n{services_preview}\n{render_video_section()}\n{render_partners_section()}"
    return wrap_html("Awtar United | Luxury Catering & Hospitality in Riyadh", "Premier Saudi catering and hospitality services in Riyadh.", body, "index")

# 2. ABOUT.HTML
def build_about():
    page_hero = """<section class="page-hero-banner">
  <img class="page-hero-bg" src="images/awtar_photos/awtar_008.jpg" alt="About Awtar United">
  <div class="page-hero-overlay"></div>
  <div class="container page-hero-content">
    <h1 class="hero-title" data-i18n="about_hero_title">Hospitality Rooted in Passion & Precision</h1>
    <p class="hero-desc" data-i18n="about_hero_desc">Discover the story, heritage, and culinary leadership behind Riyadh's foremost catering service.</p>
  </div>
</section>"""

    story_split = """<section class="section-py">
  <div class="container" style="display:grid;grid-template-columns:repeat(auto-fit,minmax(320px,1fr));gap:3.5rem;align-items:center;">
    <div>
      <div class="section-kicker" data-i18n="about_story_kicker">Our Heritage</div>
      <h2 class="section-title" data-i18n="about_story_title">5+ Years of Defining Saudi Hospitality</h2>
      <p style="font-size:1.02rem;color:var(--text-muted);margin-bottom:1.2rem;line-height:1.7;" data-i18n="about_story_text1">We started Awtar United because we saw too many events where the food was just there. No soul, no care. So we decided to do things differently. Every plate we send out and every event we handle, we treat it like our own family gathering.</p>
      <p style="font-size:1.02rem;color:var(--text-muted);margin-bottom:1.8rem;line-height:1.7;" data-i18n="about_story_text2">Today, we stand proud as trusted catering partners to the Kingdom's largest ministries, international defense exhibitions, entertainment festivals, and corporate leaders.</p>
      <a class="btn btn-gold" href="get-quote.html" data-i18n="btn_quote">Request a Quote</a>
    </div>
    <div style="border-radius:10px;overflow:hidden;box-shadow:var(--shadow-md);border:1px solid var(--cream-line);">
      <img src="images/awtar_photos/awtar_014.jpg" alt="Awtar Catering Team">
    </div>
  </div>
</section>"""

    timeline_section = """<section class="section-py" style="background:#FAF8F5;">
  <div class="container">
    <div class="section-head">
      <div class="section-kicker" data-i18n="timeline_kicker">Key Milestones</div>
      <h2 class="section-title" data-i18n="timeline_title">Our Journey of Excellence</h2>
    </div>
    <div class="timeline-grid">
      <div class="timeline-card">
        <div class="timeline-year" data-i18n="t_year_1">2019</div>
        <p style="color:var(--text-muted);font-size:0.92rem;" data-i18n="t_desc_1">Founded in Riyadh with a vision to revolutionize event catering through authentic Saudi care.</p>
      </div>
      <div class="timeline-card">
        <div class="timeline-year" data-i18n="t_year_2">2021</div>
        <p style="color:var(--text-muted);font-size:0.92rem;" data-i18n="t_desc_2">Awarded ongoing executive catering operations for prestigious government ministries and defence sectors.</p>
      </div>
      <div class="timeline-card">
        <div class="timeline-year" data-i18n="t_year_3">2023</div>
        <p style="color:var(--text-muted);font-size:0.92rem;" data-i18n="t_desc_3">Expanded to mega-project operations, festival catering, and VIP protocol for Riyadh Season and MDLBEAST.</p>
      </div>
      <div class="timeline-card">
        <div class="timeline-year" data-i18n="t_year_4">2026</div>
        <p style="color:var(--text-muted);font-size:0.92rem;" data-i18n="t_desc_4">Leading full-scale catering and hospitality partner aligned with Saudi Vision 2030 standards.</p>
      </div>
    </div>
  </div>
</section>"""

    pillars_grid = """<section class="section-py">
  <div class="container cards-grid">
    <div class="luxury-card" style="padding:1.8rem;">
      <h3 style="color:var(--gold-dark);margin-bottom:0.6rem;" data-i18n="mission_title">Our Mission</h3>
      <p style="color:var(--text-muted);font-size:0.92rem;" data-i18n="mission_desc">To deliver culinary artistry and genuine hospitality that honors our clients' reputation.</p>
    </div>
    <div class="luxury-card" style="padding:1.8rem;">
      <h3 style="color:var(--gold-dark);margin-bottom:0.6rem;" data-i18n="vision_title">Our Vision</h3>
      <p style="color:var(--text-muted);font-size:0.92rem;" data-i18n="vision_desc">To be the leading Saudi hospitality enterprise recognized across the Gulf.</p>
    </div>
    <div class="luxury-card" style="padding:1.8rem;">
      <h3 style="color:var(--gold-dark);margin-bottom:0.6rem;" data-i18n="values_title">Our Values</h3>
      <p style="color:var(--text-muted);font-size:0.92rem;" data-i18n="values_desc">Authentic Saudi generosity, uncompromising food safety, and immaculate presentation.</p>
    </div>
    <div class="luxury-card" style="padding:1.8rem;">
      <h3 style="color:var(--gold-dark);margin-bottom:0.6rem;" data-i18n="quality_title">Commitment to Quality</h3>
      <p style="color:var(--text-muted);font-size:0.92rem;" data-i18n="quality_desc">Rigorous food safety certifications, daily fresh sourcing, and precision temperature logistics.</p>
    </div>
  </div>
</section>"""

    body = f"{page_hero}\n{story_split}\n{timeline_section}\n{pillars_grid}\n{render_video_section()}"
    return wrap_html("About Us | Awtar United Catering", "Learn about Awtar United, Riyadh's premier catering team.", body, "about")

# 3. SERVICES.HTML
# Uncrowded cards with clean titles & direct quote buttons!
def build_services():
    page_hero = """<section class="page-hero-banner">
  <img class="page-hero-bg" src="images/awtar_photos/awtar_015.jpg" alt="Awtar Catering Services">
  <div class="page-hero-overlay"></div>
  <div class="container page-hero-content">
    <h1 class="hero-title" data-i18n="services_hero_title">Comprehensive Hospitality Solutions</h1>
    <p class="hero-desc" data-i18n="services_hero_desc">Tailored catering solutions engineered for royal summits, corporate banquets, and high-volume operations.</p>
  </div>
</section>"""

    catalog_cards = """<section class="section-py">
  <div class="container cards-grid">
    <article class="luxury-card">
      <div class="card-img-wrap"><img loading="lazy" src="images/awtar_photos/awtar_004.jpg" alt="Mega Project Catering"></div>
      <div class="card-body">
        <h3 class="card-title" data-i18n="service_1_title">Mega Project Catering</h3>
        <div class="card-footer"><a class="btn btn-outline-gold" href="get-quote.html?service=Mega%20Project%20Catering" data-i18n="btn_quote">Request Quote</a></div>
      </div>
    </article>

    <article class="luxury-card">
      <div class="card-img-wrap"><img loading="lazy" src="images/awtar_photos/awtar_006.jpg" alt="Corporate Catering"></div>
      <div class="card-body">
        <h3 class="card-title" data-i18n="service_2_title">Corporate & Summit Catering</h3>
        <div class="card-footer"><a class="btn btn-outline-gold" href="get-quote.html?service=Corporate%20Catering" data-i18n="btn_quote">Request Quote</a></div>
      </div>
    </article>

    <article class="luxury-card">
      <div class="card-img-wrap"><img loading="lazy" src="images/awtar_photos/awtar_009.jpg" alt="Royal Buffets"></div>
      <div class="card-body">
        <h3 class="card-title" data-i18n="service_3_title">Royal Buffets & VIP Receptions</h3>
        <div class="card-footer"><a class="btn btn-outline-gold" href="get-quote.html?service=Royal%20Buffets" data-i18n="btn_quote">Request Quote</a></div>
      </div>
    </article>

    <article class="luxury-card">
      <div class="card-img-wrap"><img loading="lazy" src="images/awtar_photos/awtar_011.jpg" alt="Coffee Break"></div>
      <div class="card-body">
        <h3 class="card-title" data-i18n="service_4_title">Coffee Break & Executive Refreshments</h3>
        <div class="card-footer"><a class="btn btn-outline-gold" href="get-quote.html?service=Coffee%20Break" data-i18n="btn_quote">Request Quote</a></div>
      </div>
    </article>

    <article class="luxury-card">
      <div class="card-img-wrap"><img loading="lazy" src="images/awtar_photos/awtar_016.jpg" alt="Finger Food"></div>
      <div class="card-body">
        <h3 class="card-title" data-i18n="service_5_title">Finger Food & Cocktail Canapés</h3>
        <div class="card-footer"><a class="btn btn-outline-gold" href="get-quote.html?service=Finger%20Food" data-i18n="btn_quote">Request Quote</a></div>
      </div>
    </article>

    <article class="luxury-card">
      <div class="card-img-wrap"><img loading="lazy" src="images/awtar_photos/awtar_020.jpg" alt="VIP Hospitality"></div>
      <div class="card-body">
        <h3 class="card-title" data-i18n="service_6_title">VIP Hospitality & Protocol Staff</h3>
        <div class="card-footer"><a class="btn btn-outline-gold" href="get-quote.html?service=VIP%20Hospitality" data-i18n="btn_quote">Request Quote</a></div>
      </div>
    </article>
  </div>
</section>"""

    workflow_section = """<section class="section-py" style="background:#FAF8F5;">
  <div class="container">
    <div class="section-head">
      <div class="section-kicker" data-i18n="workflow_kicker">Our Process</div>
      <h2 class="section-title" data-i18n="workflow_title">From Consultation to Flawless Service</h2>
    </div>
    <div class="workflow-grid">
      <div class="workflow-card">
        <span class="workflow-step">1</span>
        <h4 style="font-size:1.15rem;margin-bottom:0.4rem;" data-i18n="step_1_title">1. Consultation & Vision</h4>
        <p style="color:var(--text-muted);font-size:0.88rem;" data-i18n="step_1_desc">We analyze your event scale and preferences.</p>
      </div>
      <div class="workflow-card">
        <span class="workflow-step">2</span>
        <h4 style="font-size:1.15rem;margin-bottom:0.4rem;" data-i18n="step_2_title">2. Tasting & Menu Design</h4>
        <p style="color:var(--text-muted);font-size:0.88rem;" data-i18n="step_2_desc">Curated multi-course menus crafted by executive chefs.</p>
      </div>
      <div class="workflow-card">
        <span class="workflow-step">3</span>
        <h4 style="font-size:1.15rem;margin-bottom:0.4rem;" data-i18n="step_3_title">3. Precision Logistics</h4>
        <p style="color:var(--text-muted);font-size:0.88rem;" data-i18n="step_3_desc">Equipped mobile kitchens and seamless setup.</p>
      </div>
      <div class="workflow-card">
        <span class="workflow-step">4</span>
        <h4 style="font-size:1.15rem;margin-bottom:0.4rem;" data-i18n="step_4_title">4. Flawless Execution</h4>
        <p style="color:var(--text-muted);font-size:0.88rem;" data-i18n="step_4_desc">Impeccable table service and attentive guest care.</p>
      </div>
    </div>
  </div>
</section>"""

    body = f"{page_hero}\n{catalog_cards}\n{workflow_section}"
    return wrap_html("Catering Services | Awtar United Riyadh", "Explore corporate catering and hospitality services by Awtar United.", body, "services")

# 4. MENUS.HTML
def build_menus():
    page_hero = """<section class="page-hero-banner">
  <img class="page-hero-bg" src="images/awtar_photos/awtar_022.jpg" alt="Awtar United Menus">
  <div class="page-hero-overlay"></div>
  <div class="container page-hero-content">
    <h1 class="hero-title" data-i18n="menus_hero_title">Curated Culinary Collections</h1>
    <p class="hero-desc" data-i18n="menus_hero_desc">Explore authentic Saudi banquets, international gourmet buffets, artisan coffee breaks, and exquisite desserts.</p>
  </div>
</section>"""

    cats = [
        ("menu_cat_1", "Coffee Break VIP 1", "images/awtar_photos/awtar_024.jpg", ["Specialty Coffee", "Mini Croissants"]),
        ("menu_cat_2", "Coffee Break VIP 2", "images/awtar_photos/awtar_027.jpg", ["Saudi Gahwa", "Artisan Brioche"]),
        ("menu_cat_3", "International Buffet 1", "images/awtar_photos/awtar_029.jpg", ["Live Grill", "Mediterranean Salads"]),
        ("menu_cat_4", "Executive Royal Buffet 2", "images/awtar_photos/awtar_031.jpg", ["Wagyu Beef", "Tiger Prawns"]),
        ("menu_cat_5", "VIP Grand Banquet", "images/awtar_photos/awtar_034.jpg", ["Whole Lamb Najdi", "Spiced Kabsa"]),
        ("menu_cat_6", "Gourmet Finger Food", "images/awtar_photos/awtar_037.jpg", ["Mini Wagyu Sliders", "Truffle Tartlets"]),
        ("menu_cat_7", "Plated VIP Menus", "images/awtar_photos/awtar_039.jpg", ["4-Course Silver Service", "Sorbet Intermezzo"]),
        ("menu_cat_8", "Artisanal Desserts & Sweets", "images/awtar_photos/awtar_043.jpg", ["French Patisserie", "Kunafa Cups"]),
        ("menu_cat_9", "Beverages & Specialty Mocktails", "images/awtar_photos/awtar_046.jpg", ["Infused Mojitos", "Cold Pressed Juices"])
    ]
    menu_cards = []
    for key, title, img, tags in cats:
        enc = urllib.parse.quote(title)
        tags_html = ''.join([f'<span class="menu-tag">{t}</span>' for t in tags])
        menu_cards.append(f"""<article class="luxury-card">
  <div class="card-img-wrap"><img loading="lazy" src="{img}" alt="{title}"></div>
  <div class="card-body">
    <h3 class="card-title" data-i18n="{key}">{title}</h3>
    <div style="margin-bottom:0.8rem;">{tags_html}</div>
    <div class="card-footer"><a class="btn btn-outline-gold" href="get-quote.html?menu={enc}" data-i18n="btn_quote">Request this Menu</a></div>
  </div>
</article>""")
    menu_cards_str = '\n    '.join(menu_cards)

    body = f"""{page_hero}
<section class="section-py">
  <div class="container cards-grid">
    {menu_cards_str}
  </div>
</section>"""
    return wrap_html("Catering Menus | Awtar United", "Discover coffee breaks, buffets, and Saudi banquets from Awtar United.", body, "menus")

# 5. GALLERY.HTML
def build_gallery():
    page_hero = """<section class="page-hero-banner">
  <img class="page-hero-bg" src="images/awtar_photos/awtar_010.jpg" alt="Awtar Catering Gallery">
  <div class="page-hero-overlay"></div>
  <div class="container page-hero-content">
    <h1 class="hero-title" data-i18n="gallery_hero_title">Visual Feast & Portfolio</h1>
    <p class="hero-desc" data-i18n="gallery_hero_desc">A photographic journey through our signature buffets, corporate banquets, VIP hospitality, and exquisite food styling.</p>
  </div>
</section>"""

    gallery_items = []
    cats_cycle = ['buffet', 'projects', 'coffee', 'hospitality']
    for i in range(1, 25):
        img = f"images/awtar_photos/awtar_{i:03d}.jpg"
        cat = cats_cycle[(i - 1) % len(cats_cycle)]
        gallery_items.append(f"""<div class="gallery-item" data-category="{cat}">
  <img loading="lazy" src="{img}" alt="Awtar Catering Presentation #{i}">
  <div class="gallery-overlay">
    <strong>Awtar United #{i}</strong>
  </div>
</div>""")
    gallery_str = '\n    '.join(gallery_items)

    body = f"""{page_hero}
<section class="section-py">
  <div class="container">
    <div class="gallery-filters">
      <button class="filter-btn active" data-filter="all" data-i18n="filter_all">All Photographs</button>
      <button class="filter-btn" data-filter="buffet" data-i18n="filter_buffet">Buffets & Banquets</button>
      <button class="filter-btn" data-filter="projects" data-i18n="filter_projects">Mega Projects & Corporate</button>
      <button class="filter-btn" data-filter="coffee" data-i18n="filter_coffee">Coffee Break & Sweets</button>
      <button class="filter-btn" data-filter="hospitality" data-i18n="filter_hospitality">VIP Hospitality & Protocol</button>
    </div>
    <div class="gallery-grid">
    {gallery_str}
    </div>
  </div>
</section>

<!-- Lightbox Modal -->
<dialog id="gallery-lightbox" class="lightbox-modal">
  <div class="lightbox-content">
    <button class="lightbox-close-btn" onclick="document.getElementById('gallery-lightbox').close()">✕</button>
    <img src="" alt="Enlarged photo">
  </div>
</dialog>"""
    return wrap_html("Catering Gallery | Awtar United", "Photographic showcase of Awtar United's food presentation and events in Riyadh.", body, "gallery")

# 6. EVENTS.HTML
def build_events():
    page_hero = """<section class="page-hero-banner">
  <img class="page-hero-bg" src="images/5.jpeg" alt="Major Events & Projects">
  <div class="page-hero-overlay"></div>
  <div class="container page-hero-content">
    <h1 class="hero-title" data-i18n="events_hero_title">Major Events & Project Portfolio</h1>
    <p class="hero-desc" data-i18n="events_hero_desc">Highlighting memorable operations and mega-scale events managed with supreme professionalism by Awtar United.</p>
  </div>
</section>"""

    events_cards = """<section class="section-py">
  <div class="container cards-grid">
    <article class="luxury-card">
      <div class="card-img-wrap"><img loading="lazy" src="images/5.jpeg" alt="Ministry of Defence"></div>
      <div class="card-body">
        <h3 class="card-title" data-i18n="event_mod_title">Ministry of Defence</h3>
        <div class="project-metrics">
          <span class="metric-pill">🏢 Daily Operations</span>
          <span class="metric-pill">🍽️ 3,000+ Meals Daily</span>
        </div>
        <div class="card-footer"><a class="btn btn-outline-gold" href="get-quote.html?project=Ministry%20of%20Defence" data-i18n="btn_quote">Inquire</a></div>
      </div>
    </article>

    <article class="luxury-card">
      <div class="card-img-wrap"><img loading="lazy" src="images/6.jpeg" alt="MDLBEAST"></div>
      <div class="card-body">
        <h3 class="card-title" data-i18n="event_mdl_title">MDLBEAST Soundstorm</h3>
        <div class="project-metrics">
          <span class="metric-pill">🎵 Global Festival</span>
          <span class="metric-pill">⭐ VIP Lounges</span>
        </div>
        <div class="card-footer"><a class="btn btn-outline-gold" href="get-quote.html?project=MDLBEAST" data-i18n="btn_quote">Inquire</a></div>
      </div>
    </article>

    <article class="luxury-card">
      <div class="card-img-wrap"><img loading="lazy" src="images/7.jpeg" alt="Balad Beast"></div>
      <div class="card-body">
        <h3 class="card-title" data-i18n="event_balad_title">Balad Beast Jeddah</h3>
        <div class="project-metrics">
          <span class="metric-pill">🏛️ Historical Setting</span>
          <span class="metric-pill">☕ Heritage Hospitality</span>
        </div>
        <div class="card-footer"><a class="btn btn-outline-gold" href="get-quote.html?project=Balad%20Beast" data-i18n="btn_quote">Inquire</a></div>
      </div>
    </article>
  </div>
</section>"""

    body = f"{page_hero}\n{events_cards}\n{render_video_section()}"
    return wrap_html("Events & Projects | Awtar United", "Major catering operations and festivals by Awtar United.", body, "events")

# 7. CONTACT.HTML
def build_contact():
    page_hero = """<section class="page-hero-banner">
  <img class="page-hero-bg" src="images/awtar_photos/awtar_042.jpg" alt="Contact Awtar United">
  <div class="page-hero-overlay"></div>
  <div class="container page-hero-content">
    <h1 class="hero-title" data-i18n="contact_hero_title">Let's Plan Your Next Event</h1>
    <p class="hero-desc" data-i18n="contact_hero_desc">Get in touch with our event planners today. We are available to consult, customize, and deliver excellence.</p>
  </div>
</section>"""

    contact_section = """<section class="section-py">
  <div class="container" style="display:grid;grid-template-columns:repeat(auto-fit,minmax(320px,1fr));gap:3.5rem;">
    <!-- Info Card -->
    <div class="luxury-card" style="padding:2rem;">
      <h3 style="font-size:1.4rem;color:var(--text-dark);margin-bottom:1.2rem;" data-i18n="contact_info_title">Direct Inquiries</h3>
      <div style="display:flex;flex-direction:column;gap:1.2rem;">
        <div>
          <strong style="display:block;color:var(--gold-dark);font-size:0.82rem;text-transform:uppercase;" data-i18n="contact_phone">Phone / Support</strong>
          <a href="tel:+966564692511" style="font-size:1.05rem;font-weight:700;">+966 56 469 2511</a>
        </div>
        <div>
          <strong style="display:block;color:var(--gold-dark);font-size:0.82rem;text-transform:uppercase;" data-i18n="contact_email">Email Address</strong>
          <a href="mailto:info@awtarksa.com" style="font-size:1.05rem;font-weight:700;">info@awtarksa.com</a>
        </div>
        <div>
          <strong style="display:block;color:var(--gold-dark);font-size:0.82rem;text-transform:uppercase;" data-i18n="contact_address">Location & Service Area</strong>
          <p style="font-size:0.95rem;" data-i18n="contact_address_val">Riyadh, Kingdom of Saudi Arabia</p>
        </div>
        <div>
          <strong style="display:block;color:var(--gold-dark);font-size:0.82rem;text-transform:uppercase;" data-i18n="contact_hours">Business Hours</strong>
          <p style="color:var(--text-muted);font-size:0.88rem;" data-i18n="contact_hours_val">Saturday – Thursday, 9:00 AM – 9:00 PM. Friday closed.</p>
        </div>
      </div>

      <div style="margin-top:1.6rem;border-radius:6px;overflow:hidden;border:1px solid var(--cream-line);">
        <iframe title="Awtar Riyadh Service Area" src="https://www.google.com/maps/embed?origin=mfe&pb=!1m2!2m1!1sRiyadh+Saudi+Arabia" style="width:100%;height:160px;border:none;"></iframe>
      </div>

      <div style="margin-top:1.6rem;">
        <a class="btn btn-gold" style="width:100%;" href="https://wa.me/966545264145" target="_blank" rel="noopener">
          <span style="font-size:1.1rem;">💬</span> <span data-i18n="form_whatsapp_cta">Chat Directly on WhatsApp</span>
        </a>
      </div>
    </div>

    <!-- Form Card -->
    <div class="form-card">
      <div id="contact-alert" class="alert-box alert-success" role="status">
        <strong>Thank you!</strong> Your message has been received. Our team will review your inquiry and follow up promptly.
      </div>
      <form id="contact-form" class="form-grid">
        <div class="form-group">
          <label data-i18n="form_fullname">Full Name</label>
          <input class="form-input" name="name" type="text" required>
        </div>
        <div class="form-group">
          <label data-i18n="form_phone">Phone Number</label>
          <input class="form-input" name="phone" type="tel" required>
        </div>
        <div class="form-group full-col">
          <label data-i18n="form_email">Email Address</label>
          <input class="form-input" name="email" type="email" required>
        </div>
        <div class="form-group full-col">
          <label data-i18n="form_notes">Message</label>
          <textarea class="form-textarea" name="message" rows="4" required></textarea>
        </div>
        <div class="full-col" style="margin-top:0.6rem;">
          <button class="btn btn-gold" type="submit" style="width:100%;" data-i18n="form_submit_msg">Send Message</button>
        </div>
      </form>
    </div>
  </div>
</section>"""

    body = f"{page_hero}\n{contact_section}"
    return wrap_html("Contact Us | Awtar United Riyadh", "Connect with Awtar United catering team in Riyadh for quotes and consultation.", body, "contact")

# 8. GET-QUOTE.HTML
def build_quote():
    page_hero = """<section class="page-hero-banner">
  <img class="page-hero-bg" src="images/awtar_photos/awtar_055.jpg" alt="Request a Quote">
  <div class="page-hero-overlay"></div>
  <div class="container page-hero-content">
    <h1 class="hero-title" data-i18n="quote_hero_title">Request a Customized Quotation</h1>
    <p class="hero-desc" data-i18n="quote_hero_desc">Provide your event specifications and our banquet managers will formulate a detailed bespoke proposal within hours.</p>
  </div>
</section>"""

    quote_form_section = """<section class="section-py">
  <div class="container" style="max-width:880px;">
    <div class="form-card">
      <div id="quote-alert" class="alert-box alert-success" role="status">
        <strong>Thank you!</strong> Your quotation request was created. Reference: <strong id="quote-ref-code">AWT-000000</strong>.<br>
        Our event team is reviewing your requirements. You can also send your details directly via WhatsApp:
        <div style="margin-top:1rem;">
          <a id="quote-whatsapp-submit" class="btn btn-gold" href="#" target="_blank" rel="noopener" style="display:none;">
            Chat Directly on WhatsApp with this Inquiry
          </a>
        </div>
      </div>

      <form id="quote-form" class="form-grid">
        <div class="form-group">
          <label data-i18n="form_fullname">Full Name</label>
          <input class="form-input" name="name" type="text" required>
        </div>
        <div class="form-group">
          <label data-i18n="form_company">Company / Organization</label>
          <input class="form-input" name="company" type="text">
        </div>
        <div class="form-group">
          <label data-i18n="form_email">Email Address</label>
          <input class="form-input" name="email" type="email" required>
        </div>
        <div class="form-group">
          <label data-i18n="form_phone">Phone Number</label>
          <input class="form-input" name="phone" type="tel" required>
        </div>

        <div class="form-group">
          <label data-i18n="form_event_type">Event Type</label>
          <select class="form-select" name="event_type" required>
            <option value="">Select Event Type</option>
            <option value="Corporate Event">Corporate Summit / Gala</option>
            <option value="Government Event">Government / Diplomatic Gathering</option>
            <option value="Private Event">Private VIP Celebration</option>
            <option value="Conference">Conference / Exhibition</option>
            <option value="Festival">Festival & Entertainment</option>
            <option value="Mega Project">Mega Project Operations</option>
            <option value="Other">Other</option>
          </select>
        </div>

        <div class="form-group">
          <label data-i18n="form_event_date">Event Date</label>
          <input class="form-input" name="event_date" type="date" required>
        </div>

        <div class="form-group">
          <label data-i18n="form_location">Event Location in Riyadh</label>
          <input class="form-input" name="location" type="text" required>
        </div>

        <div class="form-group">
          <label data-i18n="form_guests">Estimated Number of Guests</label>
          <input class="form-input" name="guests" type="number" min="1" max="50000" required>
        </div>

        <div class="form-group full-col">
          <label data-i18n="form_services_needed">Required Services</label>
          <div class="checkbox-cluster">
            <label class="checkbox-label"><input type="checkbox" name="services" value="Mega Project Catering"> <span data-i18n="service_1_title">Mega Project Catering</span></label>
            <label class="checkbox-label"><input type="checkbox" name="services" value="Corporate Catering"> <span data-i18n="service_2_title">Corporate Catering</span></label>
            <label class="checkbox-label"><input type="checkbox" name="services" value="Royal Buffets"> <span data-i18n="service_3_title">Royal Buffets</span></label>
            <label class="checkbox-label"><input type="checkbox" name="services" value="Coffee Break"> <span data-i18n="service_4_title">Coffee Break</span></label>
            <label class="checkbox-label"><input type="checkbox" name="services" value="Finger Food"> <span data-i18n="service_5_title">Finger Food & Canapés</span></label>
            <label class="checkbox-label"><input type="checkbox" name="services" value="VIP Hospitality"> <span data-i18n="service_6_title">VIP Hospitality Staff</span></label>
          </div>
        </div>

        <div class="form-group full-col">
          <label data-i18n="form_menu_pref">Menu & Dietary Preferences</label>
          <textarea class="form-textarea" name="menu" rows="3"></textarea>
        </div>

        <div class="form-group full-col">
          <label data-i18n="form_notes">Additional Notes or Special Requirements</label>
          <textarea class="form-textarea" name="requirements" rows="3"></textarea>
        </div>

        <div class="full-col" style="margin-top:1rem;">
          <button class="btn btn-gold" type="submit" style="width:100%;font-size:1rem;" data-i18n="form_submit_quote">Submit Quotation Request</button>
        </div>
      </form>
    </div>
  </div>
</section>"""

    body = f"{page_hero}\n{quote_form_section}"
    return wrap_html("Request a Quote | Awtar United", "Request custom catering proposals in Riyadh with Awtar United.", body, "get-quote")

# GENERATE ALL 8 PAGES
pages_generators = {
    'index': build_index,
    'about': build_about,
    'services': build_services,
    'menus': build_menus,
    'gallery': build_gallery,
    'events': build_events,
    'contact': build_contact,
    'get-quote': build_quote
}

for slug, gen in pages_generators.items():
    html_content = gen()
    
    root_file = os.path.join(ROOT_DIR, f"{slug}.html")
    with open(root_file, "w", encoding="utf-8") as f:
        f.write(html_content)
        
    pub_file = os.path.join(PUBLIC_DIR, f"{slug}.html")
    with open(pub_file, "w", encoding="utf-8") as f:
        f.write(html_content)

print(f"Generated all {len(pages_generators)} updated pages with light colors, uncrowded cards, and no duplicates!")
