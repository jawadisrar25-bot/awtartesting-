import os

ROOT_DIR = r"C:\Users\HP\Downloads\awtar-united\awtar-united"
PUBLIC_DIR = os.path.join(ROOT_DIR, "public")
ASSETS_DIR = os.path.join(ROOT_DIR, "assets")
PUBLIC_ASSETS = os.path.join(PUBLIC_DIR, "assets")

css_content = """/* AWTAR UNITED - LUXURY, MODERN & CLEAN SAUDI CATERING */
:root {
  --gold: #C89A2C;
  --gold-light: #F1D694;
  --gold-dark: #9F7517;
  --gold-gradient: linear-gradient(135deg, #DFB756 0%, #C89A2C 50%, #9F7517 100%);
  --dark-bg: #110F0C;
  --dark-surface: #1A1713;
  --dark-card: #231F1A;
  --dark-border: rgba(200, 154, 44, 0.2);
  --light-bg: #FDFCFA;
  --light-surface: #FFFFFF;
  --light-card: #F8F4EC;
  --cream-line: #ECE4D6;
  --text-dark: #1E1A15;
  --text-muted: #6B6256;
  --text-light: #FAF5EB;
  --text-light-muted: #D1C7B7;
  --whatsapp: #25D366;
  --shadow-sm: 0 4px 14px rgba(0,0,0,0.05);
  --shadow-md: 0 10px 28px rgba(0,0,0,0.08);
  --shadow-lg: 0 20px 50px rgba(0,0,0,0.12);
  --transition: all 0.3s cubic-bezier(0.25, 0.8, 0.25, 1);
}

* { box-sizing: border-box; margin: 0; padding: 0; }
html { scroll-behavior: smooth; }

body {
  font-family: 'Manrope', -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif;
  background-color: var(--light-bg);
  color: var(--text-dark);
  line-height: 1.6;
  overflow-x: hidden;
}

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
  background: rgba(17, 15, 12, 0.94);
  backdrop-filter: blur(12px);
  border-bottom: 1px solid rgba(200, 154, 44, 0.2);
}

.header-inner {
  display: flex;
  align-items: center;
  justify-content: space-between;
  min-height: 84px;
  gap: 1.5rem;
}

.brand-logo img {
  height: 52px;
  width: auto;
  object-fit: contain;
}

.nav-menu {
  display: flex;
  align-items: center;
  gap: 1.8rem;
}

.nav-link {
  color: var(--text-light-muted);
  font-size: 0.88rem;
  font-weight: 600;
  letter-spacing: 0.04em;
  padding: 0.4rem 0;
  position: relative;
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
}

.header-actions {
  display: flex;
  align-items: center;
  gap: 1rem;
}

.lang-btn {
  display: inline-flex;
  align-items: center;
  padding: 0.45rem 1rem;
  border: 1px solid rgba(200, 154, 44, 0.45);
  border-radius: 40px;
  color: var(--text-light);
  font-size: 0.82rem;
  font-weight: 700;
  transition: var(--transition);
}

.lang-btn:hover {
  background: rgba(200, 154, 44, 0.18);
  border-color: var(--gold);
}

.btn {
  display: inline-flex;
  align-items: center;
  justify-content: center;
  gap: 0.5rem;
  padding: 0.7rem 1.5rem;
  font-size: 0.88rem;
  font-weight: 700;
  border-radius: 4px;
  transition: var(--transition);
}

.btn-gold {
  background: var(--gold-gradient);
  color: #110F0C;
  box-shadow: 0 4px 14px rgba(200, 154, 44, 0.3);
}

.btn-gold:hover {
  transform: translateY(-2px);
  box-shadow: 0 6px 20px rgba(200, 154, 44, 0.45);
  filter: brightness(1.06);
}

.btn-outline-white {
  border: 1.5px solid rgba(255, 255, 255, 0.7);
  color: #FFFFFF;
  backdrop-filter: blur(4px);
}

.btn-outline-white:hover {
  background: rgba(255, 255, 255, 0.2);
  color: #FFFFFF;
  border-color: #FFFFFF;
}

.nav-toggle-btn {
  display: none;
  color: var(--gold);
  font-size: 1.7rem;
}

/* HERO SLIDER - LIGHT OVERLAY SO PHOTOS POP */
.hero-slider-section {
  position: relative;
  min-height: 480px;
  background: #110F0C;
  color: #FFFFFF;
  overflow: hidden;
  display: flex;
  align-items: center;
}

.hero-slider-section.home-hero {
  min-height: calc(82vh - 84px);
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
  transition: opacity 1s ease-in-out, transform 6s ease-out;
  transform: scale(1.05);
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

/* SUBTLE, LIGHT OVERLAY - NO HEAVY SHADE! */
.slider-overlay {
  position: absolute;
  inset: 0;
  background: linear-gradient(180deg, rgba(0,0,0,0.28) 0%, rgba(0,0,0,0.1) 45%, rgba(0,0,0,0.45) 100%);
  z-index: 1;
}

html[dir="rtl"] .slider-overlay {
  background: linear-gradient(180deg, rgba(0,0,0,0.28) 0%, rgba(0,0,0,0.1) 45%, rgba(0,0,0,0.45) 100%);
}

.hero-content {
  position: relative;
  z-index: 2;
  padding: 3.5rem 0;
  max-width: 760px;
  text-shadow: 0 2px 16px rgba(0,0,0,0.7);
}

.eyebrow-badge {
  display: inline-flex;
  align-items: center;
  padding: 0.3rem 0.85rem;
  background: rgba(17, 15, 12, 0.6);
  backdrop-filter: blur(8px);
  border: 1px solid var(--gold);
  color: var(--gold-light);
  font-size: 0.78rem;
  font-weight: 700;
  text-transform: uppercase;
  letter-spacing: 0.12em;
  border-radius: 30px;
  margin-bottom: 1rem;
}

.hero-title {
  font-size: clamp(2.3rem, 5vw, 4rem);
  color: #FFFFFF;
  margin-bottom: 0.8rem;
  letter-spacing: -0.01em;
}

.hero-desc {
  font-size: clamp(1.05rem, 1.8vw, 1.22rem);
  color: rgba(255, 255, 255, 0.95);
  margin-bottom: 1.8rem;
  max-width: 580px;
  line-height: 1.5;
  font-weight: 500;
}

.hero-actions {
  display: flex;
  align-items: center;
  gap: 1rem;
  flex-wrap: wrap;
}

.slider-arrow {
  position: absolute;
  top: 50%;
  transform: translateY(-50%);
  z-index: 10;
  width: 44px;
  height: 44px;
  background: rgba(17, 15, 12, 0.55);
  backdrop-filter: blur(4px);
  border: 1px solid rgba(255, 255, 255, 0.35);
  color: #FFFFFF;
  border-radius: 50%;
  display: flex;
  align-items: center;
  justify-content: center;
  font-size: 1.3rem;
  transition: var(--transition);
}

.slider-arrow:hover {
  background: var(--gold);
  color: #110F0C;
  border-color: var(--gold);
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
  gap: 0.5rem;
}

.slider-dot {
  width: 10px;
  height: 10px;
  border-radius: 50%;
  background: rgba(255, 255, 255, 0.5);
  border: 1px solid rgba(0, 0, 0, 0.2);
  transition: var(--transition);
}

.slider-dot.active {
  width: 26px;
  border-radius: 8px;
  background: var(--gold);
}

/* STATS BAR */
.stats-bar {
  background: var(--dark-surface);
  border-bottom: 1px solid var(--dark-border);
  padding: 2rem 0;
  color: #FFFFFF;
}

.stats-grid {
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(200px, 1fr));
  gap: 1.5rem;
  text-align: center;
}

.stat-item h3 {
  font-size: clamp(2.2rem, 3.5vw, 3rem);
  color: var(--gold-light);
  margin-bottom: 0.2rem;
}

.stat-item p {
  color: var(--text-light-muted);
  font-size: 0.88rem;
  font-weight: 600;
  text-transform: uppercase;
  letter-spacing: 0.06em;
}

/* SECTIONS */
.section-py {
  padding: 4.8rem 0;
}

.section-head {
  text-align: center;
  max-width: 680px;
  margin: 0 auto 3rem;
}

.section-kicker {
  color: var(--gold);
  font-size: 0.8rem;
  font-weight: 700;
  text-transform: uppercase;
  letter-spacing: 0.16em;
  margin-bottom: 0.5rem;
}

.section-title {
  font-size: clamp(1.8rem, 3vw, 2.6rem);
  color: var(--text-dark);
  margin-bottom: 0.6rem;
}

.section-subtitle {
  color: var(--text-muted);
  font-size: 1rem;
}

/* CARDS GRID */
.cards-grid {
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(300px, 1fr));
  gap: 1.8rem;
}

.luxury-card {
  background: var(--light-surface);
  border: 1px solid var(--cream-line);
  border-radius: 10px;
  overflow: hidden;
  box-shadow: var(--shadow-sm);
  transition: var(--transition);
  display: flex;
  flex-direction: column;
}

.luxury-card:hover {
  transform: translateY(-5px);
  box-shadow: var(--shadow-md);
  border-color: rgba(200, 154, 44, 0.4);
}

.card-img-wrap {
  aspect-ratio: 16/10;
  overflow: hidden;
}

.card-img-wrap img {
  width: 100%;
  height: 100%;
  object-fit: cover;
  transition: transform 0.5s ease;
}

.luxury-card:hover .card-img-wrap img {
  transform: scale(1.05);
}

.card-body {
  padding: 1.5rem;
  flex: 1;
  display: flex;
  flex-direction: column;
}

.card-title {
  font-size: 1.3rem;
  margin-bottom: 0.6rem;
  color: var(--text-dark);
}

.card-text {
  color: var(--text-muted);
  font-size: 0.92rem;
  line-height: 1.6;
  margin-bottom: 1.2rem;
  flex: 1;
}

.card-footer {
  margin-top: auto;
  display: flex;
  align-items: center;
  justify-content: space-between;
}

/* VIDEO SECTION */
.video-section {
  background: var(--dark-bg);
  color: #FFFFFF;
}

.video-section .section-title { color: #FFFFFF; }
.video-section .section-subtitle { color: var(--text-light-muted); }

.video-grid {
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(320px, 1fr));
  gap: 2rem;
}

.video-card {
  background: var(--dark-card);
  border: 1px solid var(--dark-border);
  border-radius: 10px;
  overflow: hidden;
  box-shadow: var(--shadow-md);
}

.video-player-wrap {
  position: relative;
  width: 100%;
  aspect-ratio: 16/9;
  background: #000;
}

.video-player-wrap video {
  width: 100%;
  height: 100%;
  object-fit: cover;
}

.video-info {
  padding: 1.4rem;
}

.video-info h3 {
  font-size: 1.15rem;
  color: var(--gold-light);
  margin-bottom: 0.4rem;
}

.video-info p {
  color: var(--text-light-muted);
  font-size: 0.88rem;
}

/* PARTNERS & CLIENTS (ONLY ON HOME SCREEN!) */
.partners-section {
  background: #F8F5EE;
  border-top: 1px solid var(--cream-line);
  border-bottom: 1px solid var(--cream-line);
}

.partners-grid {
  display: grid;
  grid-template-columns: repeat(auto-fill, minmax(170px, 1fr));
  gap: 1.2rem;
}

.partner-card {
  background: var(--light-surface);
  border: 1px solid rgba(200, 154, 44, 0.18);
  border-radius: 8px;
  padding: 1.4rem 0.8rem;
  display: flex;
  flex-direction: column;
  align-items: center;
  justify-content: center;
  text-align: center;
  gap: 0.8rem;
  min-height: 130px;
  box-shadow: var(--shadow-sm);
  transition: var(--transition);
}

.partner-card:hover {
  transform: translateY(-4px);
  border-color: var(--gold);
  box-shadow: var(--shadow-md);
}

.partner-card img {
  max-height: 48px;
  max-width: 105px;
  object-fit: contain;
}

.partner-card span {
  font-size: 0.8rem;
  font-weight: 700;
  color: var(--text-dark);
  line-height: 1.25;
}

/* GALLERY WITH FILTER & LIGHTBOX */
.gallery-filters {
  display: flex;
  justify-content: center;
  flex-wrap: wrap;
  gap: 0.6rem;
  margin-bottom: 2.5rem;
}

.filter-btn {
  padding: 0.5rem 1.2rem;
  border-radius: 30px;
  border: 1px solid var(--cream-line);
  background: var(--light-surface);
  color: var(--text-dark);
  font-weight: 600;
  font-size: 0.86rem;
  transition: var(--transition);
}

.filter-btn:hover, .filter-btn.active {
  background: var(--gold);
  color: #110F0C;
  border-color: var(--gold);
}

.gallery-grid {
  display: grid;
  grid-template-columns: repeat(auto-fill, minmax(260px, 1fr));
  gap: 1.2rem;
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
  transition: transform 0.4s ease;
}

.gallery-item:hover img {
  transform: scale(1.06);
}

.gallery-overlay {
  position: absolute;
  inset: 0;
  background: rgba(17, 15, 12, 0.6);
  display: flex;
  flex-direction: column;
  justify-content: flex-end;
  padding: 1rem;
  color: #FFFFFF;
  opacity: 0;
  transition: opacity 0.25s ease;
}

.gallery-item:hover .gallery-overlay {
  opacity: 1;
}

/* Lightbox Dialog */
.lightbox-modal {
  max-width: min(94vw, 950px);
  border: none;
  background: transparent;
  margin: auto;
  outline: none;
}

.lightbox-modal::backdrop {
  background: rgba(14, 12, 10, 0.9);
  backdrop-filter: blur(8px);
}

.lightbox-content {
  position: relative;
  background: var(--dark-surface);
  border: 1px solid var(--dark-border);
  border-radius: 10px;
  overflow: hidden;
  padding: 0.8rem;
}

.lightbox-close-btn {
  position: absolute;
  top: 1rem;
  right: 1rem;
  z-index: 10;
  background: var(--gold);
  color: #110F0C;
  width: 34px;
  height: 34px;
  border-radius: 50%;
  display: flex;
  align-items: center;
  justify-content: center;
  font-weight: bold;
}

.lightbox-modal img {
  width: 100%;
  max-height: 75vh;
  object-fit: contain;
  border-radius: 6px;
}

/* FORMS */
.form-card {
  background: var(--light-surface);
  border: 1px solid var(--cream-line);
  border-radius: 12px;
  padding: clamp(1.6rem, 3.5vw, 2.8rem);
  box-shadow: var(--shadow-md);
}

.form-grid {
  display: grid;
  grid-template-columns: 1fr 1fr;
  gap: 1.2rem;
}

.full-col { grid-column: 1 / -1; }

.form-group label {
  display: block;
  font-size: 0.86rem;
  font-weight: 700;
  margin-bottom: 0.35rem;
  color: var(--text-dark);
}

.form-input, .form-select, .form-textarea {
  width: 100%;
  padding: 0.75rem 0.9rem;
  border: 1px solid var(--cream-line);
  border-radius: 5px;
  background: #FAF7F0;
  color: var(--text-dark);
  font-family: inherit;
  font-size: 0.92rem;
  transition: var(--transition);
}

.form-input:focus, .form-select:focus, .form-textarea:focus {
  outline: none;
  border-color: var(--gold);
  background: #FFFFFF;
  box-shadow: 0 0 0 3px rgba(200, 154, 44, 0.12);
}

.checkbox-cluster {
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(180px, 1fr));
  gap: 0.7rem;
  background: #FAF7F0;
  padding: 1rem;
  border: 1px solid var(--cream-line);
  border-radius: 6px;
}

.checkbox-label {
  display: flex;
  align-items: center;
  gap: 0.5rem;
  font-weight: 600;
  font-size: 0.86rem;
  cursor: pointer;
}

.alert-box {
  padding: 1.1rem;
  border-radius: 6px;
  margin-bottom: 1.2rem;
  display: none;
}

.alert-success {
  background: #E8F5E9;
  border: 1px solid #A5D6A7;
  color: #1B5E20;
}

/* OFFICIAL WHATSAPP FLOATING BUTTON */
.whatsapp-floating {
  position: fixed;
  bottom: 2rem;
  right: 2rem;
  z-index: 9999;
  display: flex;
  align-items: center;
  gap: 0.7rem;
  text-decoration: none;
}

html[dir="rtl"] .whatsapp-floating {
  right: auto;
  left: 2rem;
  flex-direction: row-reverse;
}

.whatsapp-circle {
  width: 58px;
  height: 58px;
  background: #25D366;
  border-radius: 50%;
  display: flex;
  align-items: center;
  justify-content: center;
  color: #FFFFFF;
  box-shadow: 0 6px 20px rgba(37, 211, 102, 0.4);
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
  100% { transform: scale(1.35); opacity: 0; }
}

.whatsapp-circle:hover {
  transform: scale(1.08);
  box-shadow: 0 10px 28px rgba(37, 211, 102, 0.55);
}

.whatsapp-tooltip {
  background: #110F0C;
  color: #FFFFFF;
  padding: 0.45rem 0.95rem;
  border-radius: 30px;
  font-size: 0.82rem;
  font-weight: 700;
  box-shadow: var(--shadow-md);
  border: 1px solid rgba(200, 154, 44, 0.35);
  white-space: nowrap;
}

/* FOOTER */
.site-footer {
  background: var(--dark-bg);
  color: var(--text-light-muted);
  border-top: 1px solid var(--dark-border);
  padding: 4.5rem 0 1.8rem;
}

.footer-grid {
  display: grid;
  grid-template-columns: 2fr 1fr 1fr 1.5fr;
  gap: 2.5rem;
  margin-bottom: 3.5rem;
}

.footer-brand img {
  height: 54px;
  margin-bottom: 1rem;
}

.footer-brand p {
  line-height: 1.6;
  max-width: 320px;
  color: var(--text-light-muted);
  font-size: 0.92rem;
}

.footer-col h4 {
  color: var(--gold-light);
  font-size: 1.05rem;
  margin-bottom: 1.2rem;
}

.footer-links {
  list-style: none;
  display: flex;
  flex-direction: column;
  gap: 0.7rem;
  font-size: 0.92rem;
}

.footer-links a:hover {
  color: var(--gold);
}

.copyright-bar {
  border-top: 1px solid rgba(255, 255, 255, 0.08);
  padding-top: 1.8rem;
  text-align: center;
  font-size: 0.82rem;
  color: #8A8172;
}

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

print("Updated style.css with clean, light-overlay styles!")
