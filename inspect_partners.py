txt = open(r'C:\Users\HP\Downloads\awtar-united\awtar-united\index.html', encoding='utf-8').read()
idx = txt.find('class="partners-grid"')
print(txt[idx:idx+1000])
