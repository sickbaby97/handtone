#!/usr/bin/env python3
"""Build HANDTONE.app bundle + icon."""
import os, shutil, math
from PIL import Image, ImageDraw

base = "/Users/abie/gesture-sound-tool"
appdir = os.path.join(base, "HANDTONE.app")

if os.path.exists(appdir):
    shutil.rmtree(appdir)

os.makedirs(os.path.join(appdir, "Contents/MacOS"), exist_ok=True)
os.makedirs(os.path.join(appdir, "Contents/Resources"), exist_ok=True)

plist = """<?xml version="1.0" encoding="UTF-8"?>
<!DOCTYPE plist PUBLIC "-//Apple//DTD PLIST 1.0//EN" "http://www.apple.com/DTDs/PropertyList-1.0.dtd">
<plist version="1.0">
<dict>
    <key>CFBundleExecutable</key>
    <string>start</string>
    <key>CFBundleIdentifier</key>
    <string>com.abie.handtone</string>
    <key>CFBundleName</key>
    <string>HANDTONE</string>
    <key>CFBundleDisplayName</key>
    <string>HANDTONE</string>
    <key>CFBundleVersion</key>
    <string>2.0</string>
    <key>CFBundleShortVersionString</key>
    <string>2.0</string>
    <key>CFBundlePackageType</key>
    <string>APPL</string>
    <key>CFBundleSignature</key>
    <string>????</string>
    <key>NSHighResolutionCapable</key>
    <true/>
    <key>NSMicrophoneUsageDescription</key>
    <string>Needs camera + microphone for hand gesture sound control.</string>
    <key>NSCameraUsageDescription</key>
    <string>Needs camera for hand gesture sound control.</string>
</dict>
</plist>
"""

with open(os.path.join(appdir, "Contents/Info.plist"), "w") as f:
    f.write(plist)

start_script = """#!/bin/bash
DIR="$(cd "$(dirname "$0")" && pwd)"
cd "$DIR/.."
exec "$DIR/../venv/bin/python" "$DIR/../desktop.py"
"""
start_path = os.path.join(appdir, "Contents/MacOS/start")
with open(start_path, "w") as f:
    f.write(start_script)
os.chmod(start_path, 0o755)

# Build icon
size = 512
img = Image.new("RGBA", (size, size), (10, 9, 8, 255))
draw = ImageDraw.Draw(img)

for i in range(8):
    r = size/2 - i*30
    alpha = int(30 - i*3)
    draw.ellipse([size/2-r, size/2-r, size/2+r, size/2+r], fill=(195, 242, 78, alpha))

draw.ellipse([size*0.1, size*0.1, size*0.9, size*0.9], outline=(195, 242, 78, 200), width=8)

pts = []
for i in range(120):
    x = size*0.15 + (i/119)*size*0.7
    y = size/2 + math.sin(i/119*math.pi*8 + math.pi/2)*size*0.12
    pts.append((x, y))
draw.line(pts, fill=(233, 225, 210, 255), width=6, joint="curve")

for cx, cy in [(size*0.38, size*0.34), (size*0.44, size*0.28), (size*0.50, size*0.26), (size*0.56, size*0.28), (size*0.62, size*0.34)]:
    r = size*0.045
    draw.ellipse([cx-r, cy-r, cx+r, cy+r], fill=(195, 242, 78, 255))

img.save(os.path.join(appdir, "Contents/Resources/icon.png"))
print("OK: app bundle at", appdir)