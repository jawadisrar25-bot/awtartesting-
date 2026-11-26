import os
import shutil

SRC_DIR = r"D:\Awtar photos"
DEST_DIR = r"C:\Users\HP\Downloads\awtar-united\awtar-united\images\awtar_photos"
PUBLIC_DEST = r"C:\Users\HP\Downloads\awtar-united\awtar-united\public\images\awtar_photos"

os.makedirs(DEST_DIR, exist_ok=True)
os.makedirs(PUBLIC_DEST, exist_ok=True)

files = os.listdir(SRC_DIR)
jpegs = [f for f in files if f.lower().endswith(('.jpeg', '.jpg'))]
mp4s = [f for f in files if f.lower().endswith('.mp4')]

print(f"Found in D:\\Awtar photos: {len(jpegs)} jpegs and {len(mp4s)} videos.")

copied = []
for i, f in enumerate(jpegs, 1):
    dest_name = f"awtar_{i:03d}.jpg"
    dest_path = os.path.join(DEST_DIR, dest_name)
    pub_path = os.path.join(PUBLIC_DEST, dest_name)
    shutil.copy2(os.path.join(SRC_DIR, f), dest_path)
    shutil.copy2(dest_path, pub_path)
    copied.append(dest_name)

print(f"Successfully copied {len(copied)} photos to {DEST_DIR}")
