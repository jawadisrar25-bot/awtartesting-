import os

ROOT_DIR = r"C:\Users\HP\Downloads\awtar-united\awtar-united"
PUBLIC_DIR = os.path.join(ROOT_DIR, "public")
ASSETS_DIR = os.path.join(ROOT_DIR, "assets")
PUBLIC_ASSETS = os.path.join(PUBLIC_DIR, "assets")

# Modern, Simple, Clean, Light Color Palette (No heavy dark colors!)
css_content = """/* AWTAR UNITED - CLEAN, MODERN & LIGHT SAUDI CATERING */
:root {
  --gold: #C89A2C;
  --gold-light: #E0B855;
  --gold-dark: #A0781D;
  --gold-gradient: linear-gradient(135deg, #DFB756 0%, #C89A2C 100%);
  --white: #FFFFFF;
  --light-bg: #FFFFFF;
  --cream-soft: #F9F7F2;
  --cream-card: #F4EFE6;
  --cream-line: #E8E1D5;
  --text-dark: #221E19;
  --text-muted: #665D52;
  --whatsapp: #25D366;
  --shadow-sm: 0 2px 10px rgba(0,0,0,0.04);
  --shadow-md: 0 8px 24px rgba(0,0,0,0.06);
  --shadow-lg: 0 16px 40px rgba(0,0,0,0.08);
  --transition: all 0.25s ease;
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
  color: var(--text-dark);
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
  width: min(1240px, calc(100% - 3rem));
  margin-inline: auto;
}

/* CLEAN, LIGHT SPLASH LOADER */
.splash-loader {
  position: fixed;
  inset: 0;
  z-index: 99999;
  background: #FFFFFF;
  display: flex;
  align-items: center;
  justify-content: center;
  transition: opacity 0.5s ease, visibility 0.5s ease;
}

.splash-loader.hidden {
  opacity: 0;
  visibility: hidden;
  pointer-events: none;
}

.splash-inner {
  text-align: center;
  display: flex;
  flex-direction: column;
  align-items: center;
  gap: 1.2rem;
}

.splash-logo-wrap {
  width: 120px;
  height: 85px;
  display: flex;
  align-items: center;
  justify-content: center;
}

.splash-logo {
  max-width: 100%;
  max-height: 100%;
  object-fit: contain;
  animation: logo-float 2s infinite ease-in-out;
}

@keyframes logo-float {
  0%, 100% { transform: translateY(0); }
  50% { transform: translateY(-4px); }
}

.splash-spinner {
  width: 28px;
  height: 28px;
  border: 2px solid #EAE3D5;
  border-top-color: var(--gold);
  border-radius: 50%;
  animation: spin 0.8s linear infinite;
}

@keyframes spin {
  to { transform: rotate(360deg); }
}

.splash-text {
  color: var(--gold-dark);
  font-size: 0.82rem;
  letter-spacing: 0.14em;
  text-transform: uppercase;
  font-weight: 700;
}

/* CLEAN, LIGHT HEADER */
.site-header {
  position: sticky;
  top: 0;
  z-index: 1000;
  background: rgba(255, 255, 255, 0.96);
  backdrop-filter: blur(10px);
  border-bottom: 1px solid var(--cream-line);
  box-shadow: 0 1px 10px rgba(0,0,0,0.03);
}

.header-inner {
  display: flex;
  align-items: center;
  justify-content: space-between;
  min-height: 80px;
  gap: 1.5rem;
}

.brand-logo img {
  height: 50px;
  width: auto;
  object-fit: contain;
}

.nav-menu {
  display: flex;
  align-items: center;
  gap: 1.8rem;
}

.nav-link {
  color: var(--text-dark);
  font-size: 0.88rem;
  font-weight: 600;
  letter-spacing: 0.02em;
  padding: 0.4rem 0;
  position: relative;
}

.nav-link:hover, .nav-link.active {
  color: var(--gold-dark);
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
  padding: 0.4rem 0.9rem;
  border: 1px solid var(--cream-line);
  border-radius: 30px;
  color: var(--text-dark);
  font-size: 0.82rem;
  font-weight: 700;
  background: var(--cream-soft);
  transition: var(--transition);
}

.lang-btn:hover {
  background: #FFFFFF;
  border-color: var(--gold);
  color: var(--gold-dark);
}

.btn {
  display: inline-flex;
  align-items: center;
  justify-content: center;
  gap: 0.5rem;
  padding: 0.65rem 1.4rem;
  font-size: 0.88rem;
  font-weight: 700;
  border-radius: 4px;
  transition: var(--transition);
}

.btn-gold {
  background: var(--gold-gradient);
  color: #FFFFFF;
  box-shadow: 0 3px 12px rgba(200, 154, 44, 0.25);
}

.btn-gold:hover {
  transform: translateY(-2px);
  box-shadow: 0 6px 18px rgba(200, 154, 44, 0.4);
  filter: brightness(1.05);
}

.btn-outline-gold {
  border: 1.5px solid var(--gold);
  color: var(--gold-dark);
  background: #FFFFFF;
}

.btn-outline-gold:hover {
  background: var(--cream-soft);
}

.nav-toggle-btn {
  display: none;
  color: var(--text-dark);
  font-size: 1.6rem;
}

/* HERO SLIDER - AIRY, LIGHT, ZERO HEAVY SHADE */
.hero-slider-section {
  position: relative;
  min-height: 480px;
  background: var(--cream-soft);
  overflow: hidden;
  display: flex;
  align-items: center;
}

.hero-slider-section.home-hero {
  min-height: calc(80vh - 80px);
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
  transform: scale(1.04);
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

/* VERY SOFT, SUBTLE LIGHT OVERLAY - PHOTOS ARE BRIGHT AND VIVID */
.slider-overlay {
  position: absolute;
  inset: 0;
  background: linear-gradient(180deg, rgba(255,255,255,0.15) 0%, rgba(255,255,255,0.05) 50%, rgba(0,0,0,0.35) 100%);
  z-index: 1;
}

.hero-content {
  position: relative;
  z-index: 2;
  padding: 3rem 0;
  max-width: 680px;
  color: #FFFFFF;
  text-shadow: 0 2px 14px rgba(0,0,0,0.7);
}

.hero-title {
  font-size: clamp(2.3rem, 5vw, 3.8rem);
  color: #FFFFFF;
  margin-bottom: 0.8rem;
  letter-spacing: -0.01em;
  line-height: 1.2;
}

.hero-desc {
  font-size: clamp(1rem, 1.6vw, 1.2rem);
  color: #FFFFFF;
  margin-bottom: 1.8rem;
  max-width: 540px;
  line-height: 1.5;
  font-weight: 500;
}

.hero-actions {
  display: flex;
  align-items: center;
  gap: 1rem;
}

.slider-arrow {
  position: absolute;
  top: 50%;
  transform: translateY(-50%);
  z-index: 10;
  width: 44px;
  height: 44px;
  background: rgba(255, 255, 255, 0.85);
  border: 1px solid var(--cream-line);
  color: var(--text-dark);
  border-radius: 50%;
  display: flex;
  align-items: center;
  justify-content: center;
  font-size: 1.3rem;
  box-shadow: var(--shadow-sm);
  transition: var(--transition);
}

.slider-arrow:hover {
  background: var(--gold);
  color: #FFFFFF;
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
  background: rgba(255, 255, 255, 0.6);
  border: 1px solid rgba(0, 0, 0, 0.2);
  transition: var(--transition);
}

.slider-dot.active {
  width: 26px;
  border-radius: 8px;
  background: var(--gold);
}

/* STATS BAR - LIGHT & CLEAN */
.stats-bar {
  background: #FFFFFF;
  border-bottom: 1px solid var(--cream-line);
  padding: 2.2rem 0;
}

.stats-grid {
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(180px, 1fr));
  gap: 1.5rem;
  text-align: center;
}

.stat-item h3 {
  font-size: clamp(2.2rem, 3.5vw, 3rem);
  color: var(--gold-dark);
  margin-bottom: 0.2rem;
}

.stat-item p {
  color: var(--text-muted);
  font-size: 0.88rem;
  font-weight: 600;
  text-transform: uppercase;
  letter-spacing: 0.05em;
}

/* SECTIONS */
.section-py {
  padding: 4.5rem 0;
}

.section-head {
  text-align: center;
  max-width: 650px;
  margin: 0 auto 2.8rem;
}

.section-kicker {
  color: var(--gold-dark);
  font-size: 0.8rem;
  font-weight: 700;
  text-transform: uppercase;
  letter-spacing: 0.16em;
  margin-bottom: 0.5rem;
}

.section-title {
  font-size: clamp(1.8rem, 3vw, 2.5rem);
  color: var(--text-dark);
  margin-bottom: 0.5rem;
}

.section-subtitle {
  color: var(--text-muted);
  font-size: 0.98rem;
}

/* CLEAN, SIMPLE CARDS GRID - NO CROWDED TEXT */
.cards-grid {
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(280px, 1fr));
  gap: 1.6rem;
}

.luxury-card {
  background: #FFFFFF;
  border: 1px solid var(--cream-line);
  border-radius: 10px;
  overflow: hidden;
  box-shadow: var(--shadow-sm);
  transition: var(--transition);
  display: flex;
  flex-direction: column;
}

.luxury-card:hover {
  transform: translateY(-4px);
  box-shadow: var(--shadow-md);
  border-color: var(--gold);
}

.card-img-wrap {
  aspect-ratio: 16/10;
  overflow: hidden;
  background: var(--cream-soft);
}

.card-img-wrap img {
  width: 100%;
  height: 100%;
  object-fit: cover;
  transition: transform 0.4s ease;
}

.luxury-card:hover .card-img-wrap img {
  transform: scale(1.05);
}

.card-body {
  padding: 1.3rem;
  flex: 1;
  display: flex;
  flex-direction: column;
  justify-content: space-between;
}

.card-title {
  font-size: 1.25rem;
  color: var(--text-dark);
  margin-bottom: 0.8rem;
}

.card-footer {
  margin-top: auto;
  padding-top: 0.5rem;
}

/* VIDEO SECTION - LIGHT & ELEGANT */
.video-section {
  background: var(--cream-soft);
  border-top: 1px solid var(--cream-line);
  border-bottom: 1px solid var(--cream-line);
}

.video-grid {
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(320px, 1fr));
  gap: 2rem;
}

.video-card {
  background: #FFFFFF;
  border: 1px solid var(--cream-line);
  border-radius: 10px;
  overflow: hidden;
  box-shadow: var(--shadow-sm);
}

.video-player-wrap {
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
  padding: 1.3rem;
}

.video-info h3 {
  font-size: 1.15rem;
  color: var(--text-dark);
  margin-bottom: 0.3rem;
}

.video-info p {
  color: var(--text-muted);
  font-size: 0.88rem;
}

/* PARTNERS & CLIENTS (ONLY ON HOME SCREEN) */
.partners-section {
  background: #FFFFFF;
  border-top: 1px solid var(--cream-line);
}

.partners-grid {
  display: grid;
  grid-template-columns: repeat(auto-fill, minmax(160px, 1fr));
  gap: 1.2rem;
}

.partner-card {
  background: #FFFFFF;
  border: 1px solid var(--cream-line);
  border-radius: 8px;
  padding: 1.4rem 0.8rem;
  display: flex;
  flex-direction: column;
  align-items: center;
  justify-content: center;
  text-align: center;
  gap: 0.8rem;
  min-height: 125px;
  box-shadow: var(--shadow-sm);
  transition: var(--transition);
}

.partner-card:hover {
  transform: translateY(-3px);
  border-color: var(--gold);
  box-shadow: var(--shadow-md);
}

.partner-card img {
  max-height: 46px;
  max-width: 100px;
  object-fit: contain;
}

.partner-card span {
  font-size: 0.8rem;
  font-weight: 700;
  color: var(--text-dark);
  line-height: 1.2;
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
  background: #FFFFFF;
  color: var(--text-dark);
  font-weight: 600;
  font-size: 0.86rem;
  transition: var(--transition);
}

.filter-btn:hover, .filter-btn.active {
  background: var(--gold);
  color: #FFFFFF;
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
  transform: scale(1.05);
}

.gallery-overlay {
  position: absolute;
  inset: 0;
  background: rgba(0, 0, 0, 0.45);
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
  background: rgba(0, 0, 0, 0.8);
  backdrop-filter: blur(6px);
}

.lightbox-content {
  position: relative;
  background: #FFFFFF;
  border-radius: 10px;
  overflow: hidden;
  padding: 0.8rem;
  box-shadow: var(--shadow-lg);
}

.lightbox-close-btn {
  position: absolute;
  top: 1rem;
  right: 1rem;
  z-index: 10;
  background: var(--gold);
  color: #FFFFFF;
  width: 32px;
  height: 32px;
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
  background: #FFFFFF;
  border: 1px solid var(--cream-line);
  border-radius: 12px;
  padding: clamp(1.6rem, 3.5vw, 2.5rem);
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
  background: #FFFFFF;
  color: var(--text-dark);
  font-family: inherit;
  font-size: 0.92rem;
  transition: var(--transition);
}

.form-input:focus, .form-select:focus, .form-textarea:focus {
  outline: none;
  border-color: var(--gold);
  box-shadow: 0 0 0 3px rgba(200, 154, 44, 0.12);
}

.checkbox-cluster {
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(180px, 1fr));
  gap: 0.7rem;
  background: var(--cream-soft);
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

/* WHATSAPP BUTTON */
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
  width: 56px;
  height: 56px;
  background: #25D366;
  border-radius: 50%;
  display: flex;
  align-items: center;
  justify-content: center;
  color: #FFFFFF;
  box-shadow: 0 4px 16px rgba(37, 211, 102, 0.35);
  position: relative;
  transition: var(--transition);
}

.whatsapp-circle:hover {
  transform: scale(1.08);
  box-shadow: 0 8px 24px rgba(37, 211, 102, 0.5);
}

.whatsapp-tooltip {
  background: #FFFFFF;
  color: var(--text-dark);
  padding: 0.45rem 0.9rem;
  border-radius: 30px;
  font-size: 0.82rem;
  font-weight: 700;
  box-shadow: var(--shadow-md);
  border: 1px solid var(--cream-line);
  white-space: nowrap;
}

/* CLEAN, LIGHT FOOTER (NO HEAVY BLACK!) */
.site-footer {
  background: #FAF8F5;
  color: var(--text-dark);
  border-top: 1px solid var(--cream-line);
  padding: 4rem 0 1.6rem;
}

.footer-grid {
  display: grid;
  grid-template-columns: 2fr 1fr 1fr 1.5fr;
  gap: 2.5rem;
  margin-bottom: 3rem;
}

.footer-brand img {
  height: 50px;
  margin-bottom: 1rem;
}

.footer-brand p {
  line-height: 1.6;
  max-width: 320px;
  color: var(--text-muted);
  font-size: 0.9rem;
}

.footer-col h4 {
  color: var(--gold-dark);
  font-size: 1.05rem;
  margin-bottom: 1rem;
}

.footer-links {
  list-style: none;
  display: flex;
  flex-direction: column;
  gap: 0.65rem;
  font-size: 0.9rem;
}

.footer-links a {
  color: var(--text-muted);
}

.footer-links a:hover {
  color: var(--gold-dark);
}

.copyright-bar {
  border-top: 1px solid var(--cream-line);
  padding-top: 1.6rem;
  text-align: center;
  font-size: 0.82rem;
  color: var(--text-muted);
}

/* DISTINCT PAGE LAYOUT ELEMENTS */
.page-hero-banner {
  position: relative;
  min-height: 340px;
  background: var(--cream-soft);
  color: #FFFFFF;
  display: flex;
  align-items: center;
  overflow: hidden;
}

.page-hero-bg {
  position: absolute;
  inset: 0;
  width: 100%;
  height: 100%;
  object-fit: cover;
}

.page-hero-overlay {
  position: absolute;
  inset: 0;
  background: linear-gradient(180deg, rgba(0,0,0,0.2) 0%, rgba(0,0,0,0.1) 50%, rgba(0,0,0,0.45) 100%);
  z-index: 1;
}

.page-hero-content {
  position: relative;
  z-index: 2;
  padding: 3.5rem 0 2.5rem;
  max-width: 680px;
  text-shadow: 0 2px 14px rgba(0,0,0,0.7);
}

.timeline-grid {
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(220px, 1fr));
  gap: 1.4rem;
  margin-top: 2.5rem;
}

.timeline-card {
  background: #FFFFFF;
  border: 1px solid var(--cream-line);
  border-top: 3px solid var(--gold);
  border-radius: 8px;
  padding: 1.5rem;
  box-shadow: var(--shadow-sm);
  transition: var(--transition);
}

.timeline-card:hover {
  transform: translateY(-3px);
  box-shadow: var(--shadow-md);
}

.timeline-year {
  color: var(--gold-dark);
  font-family: 'Playfair Display', serif;
  font-size: 1.5rem;
  font-weight: 700;
  margin-bottom: 0.3rem;
}

.workflow-grid {
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(220px, 1fr));
  gap: 1.4rem;
  margin-top: 2.5rem;
}

.workflow-card {
  background: #FFFFFF;
  border: 1px solid var(--cream-line);
  border-radius: 8px;
  padding: 1.6rem;
  box-shadow: var(--shadow-sm);
  transition: var(--transition);
}

.workflow-card:hover {
  border-color: var(--gold);
}

.workflow-step {
  display: inline-block;
  width: 32px;
  height: 32px;
  line-height: 32px;
  background: var(--gold);
  color: #FFFFFF;
  font-weight: 800;
  border-radius: 50%;
  text-align: center;
  margin-bottom: 0.8rem;
  font-size: 0.9rem;
}

.menu-tag {
  display: inline-block;
  padding: 0.2rem 0.55rem;
  background: var(--cream-soft);
  color: var(--gold-dark);
  border: 1px solid var(--cream-line);
  border-radius: 4px;
  font-size: 0.74rem;
  font-weight: 700;
  margin-right: 0.4rem;
  margin-bottom: 0.4rem;
}

html[dir="rtl"] .menu-tag {
  margin-right: 0;
  margin-left: 0.4rem;
}

.project-metrics {
  display: flex;
  gap: 0.8rem;
  flex-wrap: wrap;
  margin: 0.8rem 0;
}

.metric-pill {
  display: inline-flex;
  align-items: center;
  gap: 0.35rem;
  background: var(--cream-soft);
  border: 1px solid var(--cream-line);
  padding: 0.3rem 0.75rem;
  border-radius: 20px;
  font-size: 0.8rem;
  font-weight: 700;
  color: var(--text-dark);
}

@media (max-width: 992px) {
  .nav-menu {
    display: none;
    position: absolute;
    top: 100%;
    left: 0;
    right: 0;
    background: #FFFFFF;
    flex-direction: column;
    padding: 1.5rem;
    border-bottom: 1px solid var(--cream-line);
    box-shadow: var(--shadow-md);
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

print("Updated style.css with clean, light aesthetic without heavy dark colors!")
