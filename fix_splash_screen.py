import os, re, glob, shutil

BASE = r"C:\Users\HP\Downloads\awtar-united\awtar-united"
PUBLIC = os.path.join(BASE, "public")

# 1. Update CSS to include failsafe auto-dissolve animation
css_file = os.path.join(BASE, "assets", "style.css")
with open(css_file, "r", encoding="utf-8") as f:
    css = f.read()

# Replace #splash-screen rule with foolproof auto-fadeout
old_splash_css = r'#splash-screen\s*\{[^}]*\}'
new_splash_css = '''#splash-screen, #site-splash-loader {
  position: fixed;
  inset: 0;
  background-color: #FAF8F5;
  z-index: 99999;
  display: flex;
  flex-direction: column;
  align-items: center;
  justify-content: center;
  gap: 1.5rem;
  pointer-events: none;
  animation: splashAutoDismiss 0.7s ease 0.6s forwards;
  transition: opacity 0.5s ease, visibility 0.5s ease;
}

#splash-screen.fade-out, #site-splash-loader.hidden {
  opacity: 0;
  visibility: hidden;
  display: none !important;
}

@keyframes splashAutoDismiss {
  0% { opacity: 1; visibility: visible; }
  90% { opacity: 0; visibility: visible; }
  100% { opacity: 0; visibility: hidden; display: none !important; }
}'''

if '#splash-screen' in css:
    css = re.sub(old_splash_css, new_splash_css, css)
else:
    css = new_splash_css + "\n" + css

with open(css_file, "w", encoding="utf-8") as f:
    f.write(css)

# Also update site.js
js_file = os.path.join(BASE, "assets", "site.js")
with open(js_file, "r", encoding="utf-8") as f:
    js = f.read()

# Replace hideSplash function to check both IDs
old_hide = r'function hideSplash\(\)\s*\{[^}]*\}'
new_hide = '''function hideSplash() {
  const ids = ['splash-screen', 'site-splash-loader'];
  ids.forEach(id => {
    const el = document.getElementById(id);
    if (el) {
      el.classList.add('fade-out', 'hidden');
      el.style.opacity = '0';
      el.style.pointerEvents = 'none';
      setTimeout(() => {
        el.style.display = 'none';
      }, 500);
    }
  });
}'''

if 'function hideSplash' in js:
    js = re.sub(old_hide, new_hide, js)
else:
    js = new_hide + "\n" + js

with open(js_file, "w", encoding="utf-8") as f:
    f.write(js)

# 2. Update all HTML files
html_files = glob.glob(os.path.join(BASE, "*.html"))
for h in html_files:
    if "live_site" in h: continue
    with open(h, "r", encoding="utf-8") as f:
        content = f.read()
    
    # Update inline styles
    content = re.sub(old_splash_css, new_splash_css, content)
    
    # Update hideSplash in inline scripts
    content = re.sub(r'const splash = document\.getElementById\([\'"]site-splash-loader[\'"]\);',
                     r'const splash = document.getElementById("splash-screen") || document.getElementById("site-splash-loader");',
                     content)
    
    # Ensure dismiss runs on DOMContentLoaded, load, and timeout
    content = content.replace("window.addEventListener('load', hideSplash);",
                              "window.addEventListener('DOMContentLoaded', hideSplash);\nwindow.addEventListener('load', hideSplash);\nsetTimeout(hideSplash, 600);")

    with open(h, "w", encoding="utf-8") as f:
        f.write(content)
    
    # Mirror to public
    shutil.copy2(h, os.path.join(PUBLIC, os.path.basename(h)))

shutil.copy2(css_file, os.path.join(PUBLIC, "assets", "style.css"))
shutil.copy2(js_file, os.path.join(PUBLIC, "assets", "site.js"))
shutil.copy2(css_file, os.path.join(BASE, "style.css"))
shutil.copy2(js_file, os.path.join(BASE, "site.js"))

print("Splash screen dismiss logic fixed across all files with pure CSS + JS failsafe!")
