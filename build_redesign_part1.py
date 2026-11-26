import os
import json
import shutil
import urllib.parse

ROOT_DIR = r"C:\Users\HP\Downloads\awtar-united\awtar-united"
PUBLIC_DIR = os.path.join(ROOT_DIR, "public")
ASSETS_DIR = os.path.join(ROOT_DIR, "assets")
PUBLIC_ASSETS = os.path.join(PUBLIC_DIR, "assets")
MEDIA_DIR = os.path.join(ROOT_DIR, "media")
PUBLIC_MEDIA = os.path.join(PUBLIC_DIR, "media")

# Make sure media is in both
if not os.path.exists(PUBLIC_MEDIA):
    shutil.copytree(MEDIA_DIR, PUBLIC_MEDIA)

# 1. STYLE.CSS
css_content = """/* AWTAR UNITED - LUXURY SAUDI CATERING & HOSPITALITY STYLES */
:root {
  --gold: #C89A2C;
  --gold-light: #F1D694;
  --gold-dark: #9F7517;
  --gold-gradient: linear-gradient(135deg, #DFB756 0%, #C89A2C 50%, #9F7517 100%);
  --dark-bg: #110F0C;
  --dark-surface: #1A1713;
  --dark-card: #231F1A;
  --dark-border: rgba(200, 154, 44, 0.2);
  --light-bg: #FAF6EE;
  --light-surface: #FFFFFF;
  --light-card: #F3ECE0;
  --cream-line: #E5DCCF;
  --text-dark: #1F1B16;
  --text-muted: #726759;
  --text-light: #FAF5EB;
  --text-light-muted: #BCB19F;
  --whatsapp: #25D366;
  --shadow-sm: 0 4px 14px rgba(0,0,0,0.06);
  --shadow-md: 0 12px 32px rgba(0,0,0,0.1);
  --shadow-lg: 0 24px 64px rgba(0,0,0,0.16);
  --transition: all 0.3s cubic-bezier(0.25, 0.8, 0.25, 1);
}

* { box-sizing: border-box; margin: 0; padding: 0; }
html { scroll-behavior: smooth; }

body {
  font-family: 'Manrope', -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif;
  background-color: var(--light-bg);
  color: var(--text-dark);
  line-height: 1.65;
  overflow-x: hidden;
}

/* RTL & Arabic Support */
html[dir="rtl"] body {
  font-family: 'Noto Sans Arabic', 'Cairo', Tahoma, sans-serif;
  direction: rtl;
  text-align: right;
}

h1, h2, h3, h4 {
  font-family: 'Playfair Display', Georgia, serif;
  font-weight: 700;
  line-height: 1.25;
  color: inherit;
}

html[dir="rtl"] h1, 
html[dir="rtl"] h2, 
html[dir="rtl"] h3, 
html[dir="rtl"] h4 {
  font-family: 'Noto Sans Arabic', 'Cairo', sans-serif;
  font-weight: 800;
  line-height: 1.35;
}

a { color: inherit; text-decoration: none; transition: var(--transition); }
img { display: block; max-width: 100%; height: auto; }
button { font-family: inherit; cursor: pointer; border: none; outline: none; background: none; }

.container {
  width: min(1280px, calc(100% - 3rem));
  margin-inline: auto;
}

/* NAVIGATION */
.site-header {
  position: sticky;
  top: 0;
  z-index: 1000;
  background: rgba(18, 15, 12, 0.95);
  backdrop-filter: blur(12px);
  border-bottom: 1px solid rgba(200, 154, 44, 0.2);
  transition: var(--transition);
}

.header-inner {
  display: flex;
  align-items: center;
  justify-content: space-between;
  min-height: 90px;
  gap: 1.5rem;
}

.brand-logo img {
  height: 58px;
  width: auto;
  object-fit: contain;
  filter: brightness(1.05);
}

.nav-menu {
  display: flex;
  align-items: center;
  gap: 1.6rem;
}

.nav-link {
  color: var(--text-light-muted);
  font-size: 0.88rem;
  font-weight: 600;
  letter-spacing: 0.05em;
  position: relative;
  padding: 0.5rem 0;
}

.nav-link:hover, .nav-link.active {
  color: var(--gold-light);
}

.nav-link.active::after {
  content: '';
  position: absolute;
  bottom: 0;
  left: 0;
  right: 0;
  height: 2px;
  background: var(--gold);
  border-radius: 2px;
}

.header-actions {
  display: flex;
  align-items: center;
  gap: 1rem;
}

/* Language Switcher */
.lang-btn {
  display: inline-flex;
  align-items: center;
  gap: 0.4rem;
  padding: 0.45rem 1rem;
  border: 1px solid rgba(200, 154, 44, 0.4);
  border-radius: 40px;
  color: var(--text-light);
  font-size: 0.8rem;
  font-weight: 700;
  letter-spacing: 0.05em;
  transition: var(--transition);
}

.lang-btn:hover {
  background: rgba(200, 154, 44, 0.15);
  border-color: var(--gold);
}

.lang-btn .active-lang {
  color: var(--gold-light);
}

/* Buttons */
.btn {
  display: inline-flex;
  align-items: center;
  justify-content: center;
  gap: 0.6rem;
  padding: 0.75rem 1.6rem;
  font-size: 0.9rem;
  font-weight: 700;
  border-radius: 4px;
  letter-spacing: 0.03em;
  transition: var(--transition);
}

.btn-gold {
  background: var(--gold-gradient);
  color: #110F0C;
  box-shadow: 0 4px 18px rgba(200, 154, 44, 0.35);
}

.btn-gold:hover {
  transform: translateY(-2px);
  box-shadow: 0 8px 24px rgba(200, 154, 44, 0.5);
  filter: brightness(1.08);
}

.btn-outline-gold {
  border: 1.5px solid var(--gold);
  color: var(--gold-light);
}

.btn-outline-gold:hover {
  background: rgba(200, 154, 44, 0.15);
  color: #FFFFFF;
}

.nav-toggle-btn {
  display: none;
  color: var(--gold);
  font-size: 1.7rem;
}

/* HERO SLIDER (EVERY PAGE) */
.hero-slider-section {
  position: relative;
  min-height: 520px;
  background: var(--dark-bg);
  color: #FFFFFF;
  overflow: hidden;
  display: flex;
  align-items: center;
}

.hero-slider-section.home-hero {
  min-height: calc(88vh - 90px);
}

.slider-container {
  position: absolute;
  inset: 0;
  width: 100%;
  height: 100%;
}

.slide {
  position: absolute;
  inset: 0;
  opacity: 0;
  transition: opacity 1s ease-in-out, transform 8s ease-out;
  transform: scale(1.08);
}

.slide.active {
  opacity: 1;
  transform: scale(1);
}

.slide-img {
  width: 100%;
  height: 100%;
  object-fit: cover;
  object-position: center;
}

.slider-overlay {
  position: absolute;
  inset: 0;
  background: linear-gradient(90deg, rgba(14,12,10,0.92) 0%, rgba(14,12,10,0.65) 60%, rgba(14,12,10,0.4) 100%);
  z-index: 1;
}

html[dir="rtl"] .slider-overlay {
  background: linear-gradient(270deg, rgba(14,12,10,0.92) 0%, rgba(14,12,10,0.65) 60%, rgba(14,12,10,0.4) 100%);
}

.hero-content {
  position: relative;
  z-index: 2;
  padding: 4.5rem 0;
  max-width: 820px;
}

.eyebrow-badge {
  display: inline-flex;
  align-items: center;
  gap: 0.5rem;
  padding: 0.35rem 0.9rem;
  background: rgba(200, 154, 44, 0.15);
  border: 1px solid var(--gold);
  color: var(--gold-light);
  font-size: 0.78rem;
  font-weight: 700;
  text-transform: uppercase;
  letter-spacing: 0.15em;
  border-radius: 30px;
  margin-bottom: 1.2rem;
}

.hero-title {
  font-size: clamp(2.4rem, 5.5vw, 4.4rem);
  color: #FFFFFF;
  margin-bottom: 1.2rem;
  letter-spacing: -0.02em;
}

.hero-desc {
  font-size: clamp(1.05rem, 1.8vw, 1.25rem);
  color: var(--text-light-muted);
  margin-bottom: 2.2rem;
  max-width: 650px;
  line-height: 1.7;
}

.hero-actions {
  display: flex;
  align-items: center;
  gap: 1.2rem;
  flex-wrap: wrap;
}

/* Slider Controls */
.slider-arrow {
  position: absolute;
  top: 50%;
  transform: translateY(-50%);
  z-index: 10;
  width: 48px;
  height: 48px;
  background: rgba(18, 15, 12, 0.7);
  border: 1px solid rgba(200, 154, 44, 0.4);
  color: var(--gold-light);
  border-radius: 50%;
  display: flex;
  align-items: center;
  justify-content: center;
  font-size: 1.4rem;
  transition: var(--transition);
}

.slider-arrow:hover {
  background: var(--gold);
  color: #110F0C;
}

.slider-prev { left: 1.5rem; }
.slider-next { right: 1.5rem; }

html[dir="rtl"] .slider-prev { left: auto; right: 1.5rem; transform: translateY(-50%) rotate(180deg); }
html[dir="rtl"] .slider-next { right: auto; left: 1.5rem; transform: translateY(-50%) rotate(180deg); }

.slider-dots {
  position: absolute;
  bottom: 1.5rem;
  left: 50%;
  transform: translateX(-50%);
  z-index: 10;
  display: flex;
  gap: 0.6rem;
}

.slider-dot {
  width: 12px;
  height: 12px;
  border-radius: 50%;
  background: rgba(255, 255, 255, 0.35);
  border: 1px solid rgba(200, 154, 44, 0.3);
  transition: var(--transition);
}

.slider-dot.active {
  width: 32px;
  border-radius: 10px;
  background: var(--gold);
}

/* STATS BAR */
.stats-bar {
  background: var(--dark-surface);
  border-bottom: 1px solid var(--dark-border);
  padding: 2.2rem 0;
  color: #FFFFFF;
}

.stats-grid {
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(220px, 1fr));
  gap: 2rem;
  text-align: center;
}

.stat-item h3 {
  font-size: clamp(2.4rem, 4vw, 3.2rem);
  color: var(--gold-light);
  font-family: 'Playfair Display', serif;
  margin-bottom: 0.2rem;
}

.stat-item p {
  color: var(--text-light-muted);
  font-size: 0.95rem;
  font-weight: 600;
  text-transform: uppercase;
  letter-spacing: 0.08em;
}

/* SECTION COMMONS */
.section-py {
  padding: 5.5rem 0;
}

.section-head {
  text-align: center;
  max-width: 760px;
  margin: 0 auto 3.5rem;
}

.section-kicker {
  color: var(--gold);
  font-size: 0.82rem;
  font-weight: 700;
  text-transform: uppercase;
  letter-spacing: 0.18em;
  margin-bottom: 0.6rem;
}

.section-title {
  font-size: clamp(2rem, 3.5vw, 2.9rem);
  color: var(--text-dark);
  margin-bottom: 1rem;
}

.section-subtitle {
  color: var(--text-muted);
  font-size: 1.05rem;
}

/* CARDS GRID */
.cards-grid {
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(320px, 1fr));
  gap: 2rem;
}

.luxury-card {
  background: var(--light-surface);
  border: 1px solid var(--cream-line);
  border-radius: 12px;
  overflow: hidden;
  box-shadow: var(--shadow-sm);
  transition: var(--transition);
  display: flex;
  flex-direction: column;
}

.luxury-card:hover {
  transform: translateY(-6px);
  box-shadow: var(--shadow-md);
  border-color: rgba(200, 154, 44, 0.5);
}

.card-img-wrap {
  position: relative;
  aspect-ratio: 16/10;
  overflow: hidden;
}

.card-img-wrap img {
  width: 100%;
  height: 100%;
  object-fit: cover;
  transition: transform 0.6s ease;
}

.luxury-card:hover .card-img-wrap img {
  transform: scale(1.06);
}

.card-body {
  padding: 1.8rem;
  flex: 1;
  display: flex;
  flex-direction: column;
}

.card-title {
  font-size: 1.4rem;
  margin-bottom: 0.8rem;
  color: var(--text-dark);
}

.card-text {
  color: var(--text-muted);
  font-size: 0.95rem;
  line-height: 1.65;
  margin-bottom: 1.5rem;
  flex: 1;
}

.card-footer {
  margin-top: auto;
  display: flex;
  align-items: center;
  justify-content: space-between;
}

.card-link {
  color: var(--gold-dark);
  font-weight: 700;
  font-size: 0.92rem;
  display: inline-flex;
  align-items: center;
  gap: 0.4rem;
}

.card-link:hover {
  color: var(--gold);
}

/* VIDEO SHOWCASE SECTION */
.video-section {
  background: var(--dark-bg);
  color: #FFFFFF;
}

.video-section .section-title {
  color: #FFFFFF;
}

.video-section .section-subtitle {
  color: var(--text-light-muted);
}

.video-grid {
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(340px, 1fr));
  gap: 2.5rem;
}

.video-card {
  background: var(--dark-card);
  border: 1px solid var(--dark-border);
  border-radius: 12px;
  overflow: hidden;
  box-shadow: var(--shadow-md);
}

.video-player-wrap {
  position: relative;
  width: 100%;
  aspect-ratio: 16/9;
  background: #000000;
}

.video-player-wrap video {
  width: 100%;
  height: 100%;
  object-fit: cover;
}

.video-info {
  padding: 1.6rem;
}

.video-info h3 {
  font-size: 1.25rem;
  color: var(--gold-light);
  margin-bottom: 0.5rem;
}

.video-info p {
  color: var(--text-light-muted);
  font-size: 0.92rem;
}

/* PARTNERS & CLIENTS SECTION */
.partners-section {
  background: #F4EFE6;
  border-top: 1px solid var(--cream-line);
  border-bottom: 1px solid var(--cream-line);
}

.partners-grid {
  display: grid;
  grid-template-columns: repeat(auto-fill, minmax(180px, 1fr));
  gap: 1.5rem;
}

.partner-card {
  background: var(--light-surface);
  border: 1px solid rgba(200, 154, 44, 0.2);
  border-radius: 10px;
  padding: 1.6rem 1rem;
  display: flex;
  flex-direction: column;
  align-items: center;
  justify-content: center;
  text-align: center;
  gap: 1rem;
  min-height: 140px;
  box-shadow: var(--shadow-sm);
  transition: var(--transition);
}

.partner-card:hover {
  transform: translateY(-4px);
  border-color: var(--gold);
  box-shadow: var(--shadow-md);
}

.partner-card img {
  max-height: 52px;
  max-width: 110px;
  object-fit: contain;
  transition: var(--transition);
}

.partner-card span {
  font-size: 0.82rem;
  font-weight: 700;
  color: var(--text-dark);
  line-height: 1.3;
}

/* GALLERY WITH FILTER & LIGHTBOX */
.gallery-filters {
  display: flex;
  justify-content: center;
  flex-wrap: wrap;
  gap: 0.8rem;
  margin-bottom: 3rem;
}

.filter-btn {
  padding: 0.6rem 1.4rem;
  border-radius: 30px;
  border: 1px solid var(--cream-line);
  background: var(--light-surface);
  color: var(--text-dark);
  font-weight: 600;
  font-size: 0.9rem;
  transition: var(--transition);
}

.filter-btn:hover, .filter-btn.active {
  background: var(--gold);
  color: #110F0C;
  border-color: var(--gold);
}

.gallery-grid {
  display: grid;
  grid-template-columns: repeat(auto-fill, minmax(280px, 1fr));
  gap: 1.4rem;
}

.gallery-item {
  position: relative;
  aspect-ratio: 4/3;
  border-radius: 8px;
  overflow: hidden;
  box-shadow: var(--shadow-sm);
  cursor: pointer;
}

.gallery-item img {
  width: 100%;
  height: 100%;
  object-fit: cover;
  transition: transform 0.5s ease;
}

.gallery-item:hover img {
  transform: scale(1.08);
}

.gallery-overlay {
  position: absolute;
  inset: 0;
  background: rgba(17, 15, 12, 0.65);
  display: flex;
  flex-direction: column;
  justify-content: flex-end;
  padding: 1.2rem;
  color: #FFFFFF;
  opacity: 0;
  transition: opacity 0.3s ease;
}

.gallery-item:hover .gallery-overlay {
  opacity: 1;
}

/* Lightbox Dialog */
.lightbox-modal {
  max-width: min(94vw, 1000px);
  border: none;
  background: transparent;
  margin: auto;
  outline: none;
}

.lightbox-modal::backdrop {
  background: rgba(14, 12, 10, 0.92);
  backdrop-filter: blur(8px);
}

.lightbox-content {
  position: relative;
  background: var(--dark-surface);
  border: 1px solid var(--dark-border);
  border-radius: 12px;
  overflow: hidden;
  padding: 1rem;
}

.lightbox-close-btn {
  position: absolute;
  top: 1rem;
  right: 1rem;
  z-index: 10;
  background: var(--gold);
  color: #110F0C;
  width: 36px;
  height: 36px;
  border-radius: 50%;
  display: flex;
  align-items: center;
  justify-content: center;
  font-weight: bold;
  font-size: 1.2rem;
}

.lightbox-modal img {
  width: 100%;
  max-height: 75vh;
  object-fit: contain;
  border-radius: 8px;
}

/* FORMS */
.form-card {
  background: var(--light-surface);
  border: 1px solid var(--cream-line);
  border-radius: 16px;
  padding: clamp(1.8rem, 4vw, 3rem);
  box-shadow: var(--shadow-md);
}

.form-grid {
  display: grid;
  grid-template-columns: 1fr 1fr;
  gap: 1.4rem;
}

.full-col { grid-column: 1 / -1; }

.form-group label {
  display: block;
  font-size: 0.9rem;
  font-weight: 700;
  margin-bottom: 0.4rem;
  color: var(--text-dark);
}

.form-input, .form-select, .form-textarea {
  width: 100%;
  padding: 0.8rem 1rem;
  border: 1.5px solid var(--cream-line);
  border-radius: 6px;
  background: #FAF7F0;
  color: var(--text-dark);
  font-family: inherit;
  font-size: 0.95rem;
  transition: var(--transition);
}

.form-input:focus, .form-select:focus, .form-textarea:focus {
  outline: none;
  border-color: var(--gold);
  background: #FFFFFF;
  box-shadow: 0 0 0 4px rgba(200, 154, 44, 0.15);
}

.checkbox-cluster {
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(200px, 1fr));
  gap: 0.8rem;
  background: #FAF7F0;
  padding: 1.2rem;
  border: 1px solid var(--cream-line);
  border-radius: 8px;
}

.checkbox-label {
  display: flex;
  align-items: center;
  gap: 0.6rem;
  font-weight: 600;
  font-size: 0.9rem;
  cursor: pointer;
}

.alert-box {
  padding: 1.2rem;
  border-radius: 8px;
  margin-bottom: 1.5rem;
  display: none;
}

.alert-success {
  background: #E8F5E9;
  border: 1px solid #A5D6A7;
  color: #1B5E20;
}

/* PROPER WHATSAPP FLOATING BUTTON WITH OFFICIAL LOGO */
.whatsapp-floating {
  position: fixed;
  bottom: 2rem;
  right: 2rem;
  z-index: 9999;
  display: flex;
  align-items: center;
  gap: 0.8rem;
  text-decoration: none;
}

html[dir="rtl"] .whatsapp-floating {
  right: auto;
  left: 2rem;
  flex-direction: row-reverse;
}

.whatsapp-circle {
  width: 60px;
  height: 60px;
  background: #25D366;
  border-radius: 50%;
  display: flex;
  align-items: center;
  justify-content: center;
  color: #FFFFFF;
  box-shadow: 0 8px 24px rgba(37, 211, 102, 0.45);
  position: relative;
  transition: var(--transition);
}

.whatsapp-circle::before {
  content: '';
  position: absolute;
  inset: -4px;
  border-radius: 50%;
  border: 2px solid #25D366;
  animation: pulse-ring 2s infinite;
}

@keyframes pulse-ring {
  0% { transform: scale(1); opacity: 0.8; }
  100% { transform: scale(1.4); opacity: 0; }
}

.whatsapp-circle:hover {
  transform: scale(1.1);
  box-shadow: 0 12px 32px rgba(37, 211, 102, 0.6);
}

.whatsapp-tooltip {
  background: #110F0C;
  color: #FFFFFF;
  padding: 0.55rem 1.1rem;
  border-radius: 30px;
  font-size: 0.85rem;
  font-weight: 700;
  box-shadow: var(--shadow-md);
  border: 1px solid rgba(200, 154, 44, 0.4);
  white-space: nowrap;
  pointer-events: none;
}

/* FOOTER */
.site-footer {
  background: var(--dark-bg);
  color: var(--text-light-muted);
  border-top: 1px solid var(--dark-border);
  padding: 5rem 0 2rem;
}

.footer-grid {
  display: grid;
  grid-template-columns: 2fr 1fr 1fr 1.5fr;
  gap: 3rem;
  margin-bottom: 4rem;
}

.footer-brand img {
  height: 60px;
  margin-bottom: 1.2rem;
}

.footer-brand p {
  line-height: 1.7;
  max-width: 320px;
  color: var(--text-light-muted);
}

.footer-col h4 {
  color: var(--gold-light);
  font-size: 1.15rem;
  margin-bottom: 1.4rem;
}

.footer-links {
  list-style: none;
  display: flex;
  flex-direction: column;
  gap: 0.8rem;
}

.footer-links a:hover {
  color: var(--gold);
  padding-inline-start: 4px;
}

.copyright-bar {
  border-top: 1px solid rgba(255, 255, 255, 0.08);
  padding-top: 2rem;
  text-align: center;
  font-size: 0.85rem;
  color: #8A8172;
}

/* RESPONSIVE */
@media (max-width: 992px) {
  .nav-menu {
    display: none;
    position: absolute;
    top: 100%;
    left: 0;
    right: 0;
    background: var(--dark-bg);
    flex-direction: column;
    padding: 1.5rem;
    border-bottom: 1px solid var(--dark-border);
  }
  .nav-menu.active { display: flex; }
  .nav-toggle-btn { display: block; }
  .footer-grid { grid-template-columns: 1fr 1fr; }
}

@media (max-width: 640px) {
  .form-grid { grid-template-columns: 1fr; }
  .footer-grid { grid-template-columns: 1fr; }
  .header-actions .btn { display: none; }
  .whatsapp-tooltip { display: none; }
}
"""

with open(os.path.join(ASSETS_DIR, "style.css"), "w", encoding="utf-8") as f:
    f.write(css_content)
with open(os.path.join(PUBLIC_ASSETS, "style.css"), "w", encoding="utf-8") as f:
    f.write(css_content)

print("Wrote modern luxury style.css successfully!")
