import re

txt = open(r'C:\Users\HP\Downloads\awtar-united\awtar-united\index.html', encoding='utf-8').read()

# Find whatsapp markup
for m in re.finditer(r'<a[^>]+whatsapp-floating[^>]*>.*?</a>', txt, re.DOTALL):
    print("WhatsApp markup:\n", m.group(0))

# Find partners section
p_match = re.search(r'<section[^>]+class="[^"]*partners[^"]*"[^>]*>.*?</section>', txt, re.DOTALL)
if p_match:
    print("\nPartners section length:", len(p_match.group(0)))
    # print first 500 chars
    print(p_match.group(0)[:500])
