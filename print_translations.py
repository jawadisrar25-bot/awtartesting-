import re

with open(r"C:\Users\HP\Downloads\awtar-united\awtar-united\live_site.html", "r", encoding="utf-8") as f:
    text = f.read()

m = re.search(r'const translations\s*=\s*(\{.*?\});\s*(?:let|const|var)', text, re.DOTALL)
if m:
    print(m.group(1))
