#!/usr/bin/env python3
"""HANDTONE desktop launcher — wraps index.html as a native window."""
import webview
import os
import sys

HTML_DIR = os.path.dirname(os.path.abspath(__file__))
HTML_FILE = os.path.join(HTML_DIR, 'index.html')

if not os.path.exists(HTML_FILE):
    print(f"ERROR: {HTML_FILE} not found")
    sys.exit(1)

window = webview.create_window(
    title='HANDTONE',
    url=f'file://{HTML_FILE}',
    width=1280,
    height=860,
    resizable=True,
    frameless=False,
    on_top=False,
    background_color='#0a0908',
)

webview.start(debug=False)