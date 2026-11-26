import os, shutil, re

BASE = r"C:\Users\HP\Downloads\awtar-united\awtar-united"
PUBLIC = os.path.join(BASE, "public")

# Copy videos to root
for v in ["video_1.mp4", "video_2.mp4"]:
    src = os.path.join(BASE, "media", v)
    if os.path.exists(src):
        shutil.copy2(src, os.path.join(BASE, v))
        shutil.copy2(src, os.path.join(PUBLIC, v))

# Update video tags across pages
for p in ["index.html", "about.html", "events.html"]:
    fpath = os.path.join(BASE, p)
    if not os.path.exists(fpath): continue
    txt = open(fpath, encoding="utf-8").read()
    
    # Replace video sources to include root fallback
    txt = txt.replace(
        '<source src="media/video_1.mp4" type="video/mp4">',
        '<source src="media/video_1.mp4" type="video/mp4">\n            <source src="video_1.mp4" type="video/mp4">'
    )
    txt = txt.replace(
        '<source src="media/video_2.mp4" type="video/mp4">',
        '<source src="media/video_2.mp4" type="video/mp4">\n            <source src="video_2.mp4" type="video/mp4">'
    )
    
    with open(fpath, "w", encoding="utf-8") as f:
        f.write(txt)
    shutil.copy2(fpath, os.path.join(PUBLIC, p))

print("Videos copied to root and fallback source tags added!")
