import os
import shutil
import glob

SRC_DIR = r"C:\Users\HP\Downloads\photos"
DEST_MEDIA = r"C:\Users\HP\Downloads\awtar-united\awtar-united\media"
PUBLIC_MEDIA = r"C:\Users\HP\Downloads\awtar-united\awtar-united\public\media"

os.makedirs(DEST_MEDIA, exist_ok=True)
os.makedirs(PUBLIC_MEDIA, exist_ok=True)

# List all files in SRC_DIR
files = os.listdir(SRC_DIR)
jpegs = [f for f in files if f.lower().endswith(('.jpeg', '.jpg'))]
mp4s = [f for f in files if f.lower().endswith('.mp4')]

print(f"Found {len(jpegs)} jpegs and {len(mp4s)} videos.")

# Copy videos
video_names = []
for i, v in enumerate(mp4s, 1):
    dest_name = f"video_{i}.mp4"
    dest_path = os.path.join(DEST_MEDIA, dest_name)
    shutil.copy2(os.path.join(SRC_DIR, v), dest_path)
    shutil.copy2(dest_path, os.path.join(PUBLIC_MEDIA, dest_name))
    video_names.append(dest_name)
    print(f"Copied video: {dest_name} ({os.path.getsize(dest_path)} bytes)")

# Sort jpegs by name or time
jpegs.sort()
copied_images = []
for i, img in enumerate(jpegs, 1):
    dest_name = f"photo_{i:03d}.jpeg"
    dest_path = os.path.join(DEST_MEDIA, dest_name)
    shutil.copy2(os.path.join(SRC_DIR, img), dest_path)
    shutil.copy2(dest_path, os.path.join(PUBLIC_MEDIA, dest_name))
    copied_images.append(dest_name)

print(f"Successfully copied {len(copied_images)} photos to {DEST_MEDIA}")
