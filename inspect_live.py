import re

with open(r"C:\Users\HP\Downloads\awtar-united\awtar-united\live_site.html", "r", encoding="utf-8") as f:
    text = f.read()

partners_match = re.search(r'class=["\']partners-section["\'].*?</section>', text, re.DOTALL)
if partners_match:
    print(partners_match.group(0))

# Also extract the translation dictionaries in script tags
translations_match = re.search(r'const translations\s*=\s*(\{.*?\});\s*(?:let|const|var)', text, re.DOTALL)
if translations_match:
    print("\n--- TRANSLATIONS FOUND ---\n")
    print(translations_match.group(1)[:1500])
