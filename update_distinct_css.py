import os
import json
import urllib.parse

ROOT_DIR = r"C:\Users\HP\Downloads\awtar-united\awtar-united"
PUBLIC_DIR = os.path.join(ROOT_DIR, "public")
ASSETS_DIR = os.path.join(ROOT_DIR, "assets")
PUBLIC_ASSETS = os.path.join(PUBLIC_DIR, "assets")

# 1. Update style.css with Splash screen & unique page styling
css_additions = """
/* LUXURY SPLASH LOADING SCREEN WITH GOLD LOGO */
.splash-loader {
  position: fixed;
  inset: 0;
  z-index: 99999;
  background: #110F0C;
  display: flex;
  align-items: center;
  justify-content: center;
  transition: opacity 0.6s cubic-bezier(0.25, 1, 0.5, 1), visibility 0.6s ease;
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
  position: relative;
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
  animation: logo-breathe 2s infinite ease-in-out;
}

@keyframes logo-breathe {
  0%, 100% { transform: scale(1); filter: brightness(1); }
  50% { transform: scale(1.06); filter: brightness(1.2) drop-shadow(0 0 20px rgba(200, 154, 44, 0.6)); }
}

.splash-spinner {
  width: 32px;
  height: 32px;
  border: 2px solid rgba(200, 154, 44, 0.2);
  border-top-color: var(--gold);
  border-radius: 50%;
  animation: spin 0.8s linear infinite;
}

@keyframes spin {
  to { transform: rotate(360deg); }
}

.splash-text {
  color: var(--gold-light);
  font-size: 0.82rem;
  letter-spacing: 0.18em;
  text-transform: uppercase;
  font-weight: 700;
}

/* DISTINCT PAGE LAYOUT ELEMENTS */
.page-hero-banner {
  position: relative;
  min-height: 380px;
  background: #110F0C;
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
  background: linear-gradient(180deg, rgba(17,15,12,0.3) 0%, rgba(17,15,12,0.15) 50%, rgba(17,15,12,0.65) 100%);
  z-index: 1;
}

.page-hero-content {
  position: relative;
  z-index: 2;
  padding: 4rem 0 3rem;
  max-width: 720px;
  text-shadow: 0 2px 14px rgba(0,0,0,0.7);
}

/* Timeline on About Page */
.timeline-grid {
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(240px, 1fr));
  gap: 1.5rem;
  margin-top: 3rem;
}

.timeline-card {
  background: var(--light-surface);
  border: 1px solid var(--cream-line);
  border-top: 3px solid var(--gold);
  border-radius: 8px;
  padding: 1.6rem;
  box-shadow: var(--shadow-sm);
  transition: var(--transition);
}

.timeline-card:hover {
  transform: translateY(-4px);
  box-shadow: var(--shadow-md);
}

.timeline-year {
  color: var(--gold-dark);
  font-family: 'Playfair Display', serif;
  font-size: 1.6rem;
  font-weight: 700;
  margin-bottom: 0.4rem;
}

/* Process Workflow on Services Page */
.workflow-grid {
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(220px, 1fr));
  gap: 1.5rem;
  margin-top: 3rem;
}

.workflow-card {
  background: #F8F4EC;
  border: 1px solid var(--cream-line);
  border-radius: 10px;
  padding: 1.8rem;
  position: relative;
  transition: var(--transition);
}

.workflow-card:hover {
  background: var(--light-surface);
  border-color: var(--gold);
}

.workflow-step {
  display: inline-block;
  width: 36px;
  height: 36px;
  line-height: 36px;
  background: var(--gold);
  color: #110F0C;
  font-weight: 800;
  border-radius: 50%;
  text-align: center;
  margin-bottom: 1rem;
}

/* Menu Course Tags */
.menu-tag {
  display: inline-block;
  padding: 0.2rem 0.6rem;
  background: rgba(200, 154, 44, 0.12);
  color: var(--gold-dark);
  border-radius: 4px;
  font-size: 0.75rem;
  font-weight: 700;
  margin-right: 0.4rem;
  margin-bottom: 0.4rem;
}

html[dir="rtl"] .menu-tag {
  margin-right: 0;
  margin-left: 0.4rem;
}

/* Event Metrics on Events Page */
.project-metrics {
  display: flex;
  gap: 1.2rem;
  flex-wrap: wrap;
  margin: 1rem 0;
}

.metric-pill {
  display: inline-flex;
  align-items: center;
  gap: 0.4rem;
  background: #FAF6ED;
  border: 1px solid var(--cream-line);
  padding: 0.35rem 0.8rem;
  border-radius: 20px;
  font-size: 0.82rem;
  font-weight: 700;
  color: var(--text-dark);
}
"""

with open(os.path.join(ASSETS_DIR, "style.css"), "r", encoding="utf-8") as f:
    orig_css = f.read()

# Only append if not already present
if "splash-loader" not in orig_css:
    full_css = orig_css + css_additions
    with open(os.path.join(ASSETS_DIR, "style.css"), "w", encoding="utf-8") as f:
        f.write(full_css)
    with open(os.path.join(PUBLIC_ASSETS, "style.css"), "w", encoding="utf-8") as f:
        f.write(full_css)
    print("Appended splash and distinct layout styles to style.css!")

print("CSS verified.")
