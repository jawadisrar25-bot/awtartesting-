import os
import shutil
import urllib.parse

ROOT_DIR = r"C:\Users\HP\Downloads\awtar-united\awtar-united"
PUBLIC_DIR = os.path.join(ROOT_DIR, "public")
IMAGES_DIR = os.path.join(ROOT_DIR, "images")
PUBLIC_IMAGES_DIR = os.path.join(PUBLIC_DIR, "images")
PUBLIC_ASSETS_DIR = os.path.join(PUBLIC_DIR, "assets")
ROOT_ASSETS_DIR = os.path.join(ROOT_DIR, "assets")

# Ensure assets and images exist in both root and public
if not os.path.exists(ROOT_ASSETS_DIR):
    shutil.copytree(PUBLIC_ASSETS_DIR, ROOT_ASSETS_DIR)
if not os.path.exists(PUBLIC_IMAGES_DIR):
    shutil.copytree(IMAGES_DIR, PUBLIC_IMAGES_DIR)

settings = {
    'company': 'Awtar United Catering Services',
    'location': 'Riyadh, Saudi Arabia',
    'whatsapp': '966545264145',
    'phone': '+966564692511',
    'email': 'info@awtarksa.com',
    'instagram': 'https://www.instagram.com/awtarunited/',
    'hours': 'Saturday–Thursday, 9:00 AM–9:00 PM. Friday closed.',
    'headline': 'Refined Taste, Unforgettable Moments',
    'intro': 'Catering and hospitality for corporate gatherings, private celebrations and large-scale projects in Riyadh.',
    'story': 'Awtar United was founded to bring more care to event catering. Our team coordinates food preparation, presentation and guest service around the needs of each event.',
    'mission': 'Serve food and hospitality with care, from the first planning conversation to the final guest.',
    'vision': 'Build lasting relationships in Riyadh through dependable catering and attentive hospitality.',
    'values': 'Care in preparation, attention to presentation and respect for every guest.',
    'quality': 'We plan menus, presentation and service around your event format and guest requirements.',
    'team': 'Our catering and hospitality teams coordinate preparation, service and guest reception.',
    'map_url': 'https://www.google.com/maps/embed?origin=mfe&pb=!1m2!2m1!1sRiyadh+Saudi+Arabia',
    'hero_image': 'images/1.jpeg',
    'logo_url': 'images/logo1.png',
    'confirmation_copy': 'Our team will review your inquiry and follow up using the contact details you provided.',
}

pages = {
    'index': ('Home', 'Catering & Hospitality in Riyadh', 'Premium catering and hospitality for corporate events, celebrations and large-scale projects across Riyadh.'),
    'about': ('About', 'About Awtar United', 'Meet the Riyadh team behind Awtar United’s catering and hospitality services.'),
    'services': ('Services', 'Catering & Hospitality Services', 'Explore corporate catering, mega project catering, buffets, coffee breaks and hospitality services in Riyadh.'),
    'menus': ('Menus', 'Catering Menus', 'Explore Awtar United’s coffee break, buffet and event menu options.'),
    'gallery': ('Gallery', 'Catering Gallery', 'See food presentation, event photography and catering arrangements from Awtar United.'),
    'events': ('Events', 'Events & Projects', 'Discover events and projects featured in Awtar United’s public catering portfolio.'),
    'contact': ('Contact', 'Contact Awtar United', 'Contact Awtar United for catering and hospitality in Riyadh.'),
    'get-quote': ('Get a Quote', 'Request a Catering Quote', 'Request a personalized catering quote for your event in Riyadh.')
}

services_data = [
    {
        'title': 'Mega Project Catering',
        'description': 'Catering for large-scale projects, festivals, public events and staff meal programs, including food stations and coordinated meal service.',
        'image': 'images/1.jpeg'
    },
    {
        'title': 'Corporate Catering',
        'description': 'Food and guest service for conferences, executive meetings, business gatherings and company events.',
        'image': 'images/2.jpeg'
    },
    {
        'title': 'Private Event Catering',
        'description': 'Catering and service planned around your family gathering, VIP reception or private celebration.',
        'image': 'images/3.jpeg'
    },
    {
        'title': 'Buffet Catering',
        'description': 'Standard, premium and VIP buffet arrangements with international options.',
        'image': 'images/12.jpeg'
    },
    {
        'title': 'Coffee Break',
        'description': 'Coffee breaks for meetings and events with pastries, savory bites, desserts and hot or cold beverages.',
        'image': ''
    },
    {
        'title': 'Finger Food',
        'description': 'Canapés, mini sandwiches, appetizers and desserts for receptions and gatherings.',
        'image': ''
    },
    {
        'title': 'Hospitality Services',
        'description': 'Guest reception, professional waitstaff and hospitality team coordination.',
        'image': 'images/13.jpeg'
    }
]

events_data = [
    {
        'title': 'Ministry of Defence',
        'description': 'Awtar United features daily and monthly catering operations in its public project portfolio.',
        'image': 'images/5.jpeg'
    },
    {
        'title': 'MDLBEAST',
        'description': 'Awtar United features event catering and food service logistics in its public project portfolio.',
        'image': 'images/6.jpeg'
    },
    {
        'title': 'Balad Beast',
        'description': 'Awtar United features event hospitality in its public project portfolio.',
        'image': 'images/7.jpeg'
    }
]

clients_data = [
    {
        'title': 'stc',
        'description': '',
        'image': 'images/stc.png'
    }
]

menu_categories = [
    'Coffee Break VIP 1',
    'Coffee Break VIP 2',
    'Buffet 1',
    'Buffet 2',
    'VIP Buffet',
    'Finger Food',
    'Plated Menus',
    'Set Menus',
    'Desserts',
    'Beverages'
]

gallery_categories = [
    (1, 'Corporate Events'),
    (2, 'Government Events'),
    (3, 'Coffee Break'),
    (4, 'Buffet Arrangements'),
    (5, 'VIP Hospitality'),
    (6, 'Food Presentation'),
    (7, 'Private Events'),
    (8, 'Our Team')
]

gallery_images = [
    {
        'title': 'Awtar catering',
        'description': 'Catering photography from Awtar United.',
        'image': 'images/1.jpeg',
        'category_id': ''
    },
    {
        'title': 'Awtar hospitality',
        'description': 'Hospitality photography from Awtar United.',
        'image': 'images/2.jpeg',
        'category_id': '5'
    },
    {
        'title': 'Event presentation',
        'description': 'Event photography from Awtar United.',
        'image': 'images/3.jpeg',
        'category_id': ''
    },
    {
        'title': 'Food service',
        'description': 'Food and service photography from Awtar United.',
        'image': 'images/12.jpeg',
        'category_id': '6'
    }
]

event_types = [
    'Corporate Event',
    'Government Event',
    'Private Event',
    'Conference',
    'Wedding or Celebration',
    'Festival',
    'Mega Project',
    'Other'
]

def render_cards(items, is_service_quote=False):
    html = ['<div class="cards">']
    for item in items:
        html.append('<article class="card">')
        if item.get('image'):
            html.append(f'<img loading="lazy" src="{item["image"]}" alt="{item["title"]}">')
        html.append(f'<div><h3>{item["title"]}</h3><p>{item["description"]}</p>')
        if is_service_quote:
            encoded_title = urllib.parse.quote(item["title"])
            html.append(f'<a class="text-link" href="get-quote.html?service={encoded_title}">Get a Quote</a>')
        html.append('</div></article>')
    html.append('</div>')
    return '\n'.join(html)

def generate_page(slug):
    label, default_title, default_desc = pages[slug]
    title = f"{default_title} | Awtar United"
    desc = default_desc
    hero = settings['hero_image']
    logo = settings['logo_url']

    nav_links = []
    for s, (name, _, _) in pages.items():
        curr = ' aria-current="page"' if s == slug else ''
        btn_class = ' class="button"' if s == 'get-quote' else ''
        filename = f"{s}.html"
        nav_links.append(f'<a{curr}{btn_class} href="{filename}">{name}</a>')
    nav_html = '\n'.join(nav_links)

    # Content generation
    content_html = ""
    if slug == 'index':
        content_html = f"""<section class="hero"><img src="{hero}" alt="Awtar United catering arrangement" fetchpriority="high"><div class="wrap hero-copy"><p class="eyebrow">Catering &amp; hospitality in Riyadh</p><h1>{settings['headline']}</h1><p>{settings['intro']}</p><div class="actions"><a class="button" href="get-quote.html">Request a Quote</a><a class="button outline" href="services.html">Our Services</a></div></div></section>
<section class="wrap section"><p class="eyebrow">Catering services</p><h2>Hospitality for every occasion</h2>{render_cards(services_data[:3], True)}<a class="text-link" href="services.html">Explore all services</a></section>
<section class="feature"><div class="wrap split"><img loading="lazy" src="images/12.jpeg" alt="Awtar food presentation"><div><p class="eyebrow">Menus &amp; presentation</p><h2>Plan your menu around the occasion</h2><p>{settings['quality']}</p><a class="button" href="menus.html">Explore menus</a> <a class="text-link" href="gallery.html">View gallery</a></div></div></section>
<section class="wrap section"><h2>Events and projects</h2>{render_cards(events_data[:3])}<a class="text-link" href="events.html">View projects</a></section>
<section class="wrap section"><h2>Clients and partners</h2>{render_cards(clients_data)}</section>
<section class="feature"><div class="wrap section"><h2>Why clients choose Awtar United</h2><p>{settings['team']}</p><a class="button" href="get-quote.html">Plan your event</a></div></section>"""
    elif slug == 'about':
        about_cards_html = """<div class="cards about-cards">
<article><h3>Our mission</h3><p>""" + settings['mission'] + """</p></article>
<article><h3>Our vision</h3><p>""" + settings['vision'] + """</p></article>
<article><h3>Our values</h3><p>""" + settings['values'] + """</p></article>
<article><h3>Our commitment to quality</h3><p>""" + settings['quality'] + """</p></article>
<article><h3>Our team and approach to hospitality</h3><p>""" + settings['team'] + """</p></article>
</div>"""
        content_html = f"""<section class="page-head"><div class="wrap"><p class="eyebrow">Awtar United · Riyadh</p><h1>{default_title}</h1><p>{desc}</p></div></section>
<div class="wrap section">
<div class="split"><img src="images/13.jpeg" alt="Awtar United catering and event service"><div><h2>Who we are</h2><p>{settings['intro']}</p><h2>Our story</h2><p>{settings['story']}</p></div></div>
{about_cards_html}
</div>"""
    elif slug == 'services':
        content_html = f"""<section class="page-head"><div class="wrap"><p class="eyebrow">Awtar United · Riyadh</p><h1>{default_title}</h1><p>{desc}</p></div></section>
<div class="wrap section">
{render_cards(services_data, True)}
</div>"""
    elif slug == 'events':
        content_html = f"""<section class="page-head"><div class="wrap"><p class="eyebrow">Awtar United · Riyadh</p><h1>{default_title}</h1><p>{desc}</p></div></section>
<div class="wrap section">
{render_cards(events_data)}
</div>"""
    elif slug == 'menus':
        menus_categories_html = []
        for cat in menu_categories:
            encoded_cat = urllib.parse.quote(cat)
            menus_categories_html.append(f"""<section class="menu-category"><h2>{cat}</h2><a class="text-link" href="get-quote.html?menu={encoded_cat}">Request this menu</a></section>""")
        content_html = f"""<section class="page-head"><div class="wrap"><p class="eyebrow">Awtar United · Riyadh</p><h1>{default_title}</h1><p>{desc}</p></div></section>
<div class="wrap section">
<div class="cards">
{''.join(menus_categories_html)}
</div>
</div>"""
    elif slug == 'gallery':
        cat_options = ['<option value="">All photographs</option>']
        for cat_id, cat_title in gallery_categories:
            cat_options.append(f'<option value="{cat_id}">{cat_title}</option>')
        options_html = '\n'.join(cat_options)

        fig_items = []
        for g in gallery_images:
            cat_attr = f' data-category="{g["category_id"]}"' if g["category_id"] else ' data-category=""'
            fig_items.append(f"""<figure{cat_attr}><a data-gallery href="{g['image']}"><img loading="lazy" src="{g['image']}" alt="{g['title']}"></a><figcaption><strong>{g['title']}</strong><br>{g['description']}</figcaption></figure>""")
        figures_html = '\n'.join(fig_items)

        content_html = f"""<section class="page-head"><div class="wrap"><p class="eyebrow">Awtar United · Riyadh</p><h1>{default_title}</h1><p>{desc}</p></div></section>
<div class="wrap section">
<label class="filter">Gallery category<select id="gallery-filter">{options_html}</select></label>
<div class="cards gallery">
{figures_html}
</div>
<dialog id="lightbox"><form method="dialog"><button aria-label="Close image">Close</button></form><img alt=""></dialog>
</div>"""
    elif slug == 'contact':
        content_html = f"""<section class="page-head"><div class="wrap"><p class="eyebrow">Awtar United · Riyadh</p><h1>{default_title}</h1><p>{desc}</p></div></section>
<div class="wrap section">
<div class="split contact-layout">
<aside><h2>Contact details</h2><p>{settings['company']}<br><span itemprop="areaServed">{settings['location']}</span></p><p><a href="tel:{settings['phone']}">{settings['phone']}</a><br><a href="mailto:{settings['email']}">{settings['email']}</a><br><a href="{settings['instagram']}" target="_blank" rel="noopener">Instagram</a><br><a href="https://awtarksa.com">awtarksa.com</a></p><a class="button" href="https://wa.me/{settings['whatsapp']}" target="_blank" rel="noopener">WhatsApp</a><h3>Business hours</h3><p>{settings['hours']}</p><iframe title="Company service area in Riyadh" loading="lazy" src="{settings['map_url']}"></iframe></aside>
<section class="form-panel"><h2>Send a message</h2>
<div id="contact-success" class="notice" style="display:none;" role="status">Thank you! Your message was received. {settings['confirmation_copy']}</div>
<form id="contact-form" class="form-grid">
<label>Full name<input name="name" type="text" maxlength="150" required></label>
<label>Email address<input name="email" type="email" maxlength="254" required></label>
<label>Phone number<input name="phone" type="tel" maxlength="35" required></label>
<label class="full">Message<textarea name="message" maxlength="5000" required></textarea></label>
<div class="full actions"><button class="button" type="submit">Send message</button><a class="button outline" style="color:var(--ink);border-color:var(--muted)" href="https://wa.me/{settings['whatsapp']}" target="_blank" rel="noopener">Chat on WhatsApp</a></div>
</form></section></div>
</div>"""
    elif slug == 'get-quote':
        service_checks = []
        for s in services_data:
            service_checks.append(f"""<label class="check"><input type="checkbox" name="services" value="{s['title']}"> {s['title']}</label>""")
        services_checks_html = '\n'.join(service_checks)

        event_options = ['<option value="">Select an event type</option>']
        for et in event_types:
            event_options.append(f'<option value="{et}">{et}</option>')
        event_options_html = '\n'.join(event_options)

        content_html = f"""<section class="page-head"><div class="wrap"><p class="eyebrow">Awtar United · Riyadh</p><h1>{default_title}</h1><p>{desc}</p></div></section>
<div class="wrap section">
<div class="quote-layout">
<section class="form-panel"><h2>Your event details</h2>
<div id="quote-success" class="notice" style="display:none;" role="status">Thank you! Your quotation request has been received. <span id="quote-ref-container"></span> {settings['confirmation_copy']}</div>
<form id="quote-form" class="form-grid">
<label>Full name<input name="name" type="text" maxlength="150" required></label>
<label>Company name (optional)<input name="company" type="text" maxlength="150"></label>
<label>Email address<input name="email" type="email" maxlength="254" required></label>
<label>Phone number<input name="phone" type="tel" maxlength="35" required></label>
<label>Event type<select name="event_type" required>{event_options_html}</select></label>
<label>Event date<input name="event_date" type="date" required></label>
<label>Event location<input name="location" type="text" maxlength="255" required></label>
<label>Number of guests<input type="number" name="guests" min="1" max="1000000" required></label>
<label>Budget range (optional)<input name="budget" type="text" maxlength="150"></label>
<fieldset class="full"><legend>Required services</legend>
{services_checks_html}
</fieldset>
<label class="full">Menu preferences<textarea id="menu-pref" name="menu" maxlength="3000"></textarea></label>
<label class="full">Additional requirements<textarea name="requirements" maxlength="5000"></textarea></label>
<div class="full actions"><button class="button" type="submit">Request a quotation</button><a id="quote-wa-link" class="text-link" href="https://wa.me/{settings['whatsapp']}" target="_blank" rel="noopener">Contact us on WhatsApp</a></div>
</form></section></div>
</div>"""

    full_html = f"""<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{title}</title>
<meta name="description" content="{desc}">
<meta property="og:title" content="{title}">
<meta property="og:description" content="{desc}">
<meta property="og:type" content="website">
<meta property="og:image" content="{hero}">
<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700&family=Playfair+Display:wght@500;600;700&display=swap">
<link rel="stylesheet" href="assets/style.css">
<script defer src="assets/site.js"></script>
</head>
<body itemscope itemtype="https://schema.org/Caterer">
<meta itemprop="name" content="{settings['company']}">
<meta itemprop="areaServed" content="{settings['location']}">
<meta itemprop="telephone" content="{settings['phone']}">
<meta itemprop="email" content="{settings['email']}">
<header class="top">
  <div class="wrap nav">
    <a class="brand" href="index.html"><img src="{logo}" alt="Awtar United"></a>
    <button class="nav-toggle" type="button" aria-expanded="false" aria-controls="main-nav">Menu</button>
    <nav id="main-nav" aria-label="Main navigation">
{nav_html}
    </nav>
  </div>
</header>
<main>
{content_html}
</main>
<footer class="footer">
  <div class="wrap footer-grid">
    <div>
      <a class="brand" href="index.html"><img src="{logo}" loading="lazy" alt="Awtar United"></a>
      <p>{settings['location']}</p>
    </div>
    <div>
      <h3>Explore</h3>
      <a href="services.html">Services</a>
      <a href="menus.html">Menus</a>
      <a href="events.html">Events</a>
    </div>
    <div>
      <h3>Get in touch</h3>
      <a href="mailto:{settings['email']}">{settings['email']}</a>
      <a href="{settings['instagram']}" target="_blank" rel="noopener">Instagram</a>
      <a href="contact.html">Contact</a>
    </div>
  </div>
  <div class="wrap copyright">© 2026 Awtar United</div>
</footer>
<a class="whatsapp" href="https://wa.me/{settings['whatsapp']}" target="_blank" rel="noopener" aria-label="Contact Awtar United on WhatsApp">WhatsApp</a>
</body>
</html>"""
    return full_html

# Generate each page in both root and public
for slug in pages.keys():
    html = generate_page(slug)
    
    root_path = os.path.join(ROOT_DIR, f"{slug}.html")
    with open(root_path, "w", encoding="utf-8") as f:
        f.write(html)
        
    pub_path = os.path.join(PUBLIC_DIR, f"{slug}.html")
    with open(pub_path, "w", encoding="utf-8") as f:
        f.write(html)

print("Generated all pages successfully!")
