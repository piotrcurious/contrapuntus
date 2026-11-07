#!/usr/bin/env python3
"""
Zero-Dependency Bundler for Contrapunctus Rework2B3-Moves
Inlines all external fonts, styles, and assets into a standalone offline HTML bundle.
Can be executed after every development iteration:
    python3 scripts/bundle.py
"""
import os
import re
import base64
import urllib.request

REPO_ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
SRC_HTML = os.path.join(REPO_ROOT, "rework2b3-moves", "contrapunctus-3.html")
DIST_HTML = os.path.join(REPO_ROOT, "rework2b3-moves", "contrapunctus-3.html")

def fetch_and_embed_fonts(css_url):
    print(f"[Bundle] Fetching font stylesheet from {css_url}...")
    req = urllib.request.Request(
        css_url,
        headers={"User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36"}
    )
    css = urllib.request.urlopen(req).read().decode("utf-8")

    def repl_url(match):
        font_url = match.group(1)
        print(f"[Bundle] Downloading and base64-encoding font: {font_url}...")
        font_bytes = urllib.request.urlopen(font_url).read()
        b64 = base64.b64encode(font_bytes).decode("ascii")
        return f"url(data:font/woff2;base64,{b64})"

    latin_blocks = re.findall(r"/\* latin \*/\s*@font-face\s*\{[^}]+\}", css)
    if not latin_blocks:
        latin_blocks = re.findall(r"@font-face\s*\{[^}]+\}", css)

    embedded_blocks = []
    for block in latin_blocks:
        emb = re.sub(r"url\((https://[^\)]+)\)", repl_url, block)
        embedded_blocks.append(emb)

    return "\n".join(embedded_blocks)

def bundle():
    print(f"[Bundle] Processing {SRC_HTML}...")
    with open(SRC_HTML, "r", encoding="utf-8") as f:
        html = f.read()

    # Find external google font link tags
    font_link_regex = r'<link rel="preconnect" href="https://fonts\.googleapis\.com">\s*<link rel="preconnect" href="https://fonts\.gstatic\.com"[^>]*>\s*<link rel="stylesheet" href="(https://fonts\.googleapis\.com/css2\?[^"]+)">'
    match = re.search(font_link_regex, html)

    if match:
        css_url = match.group(1)
        embedded_fonts = fetch_and_embed_fonts(css_url)
        replacement = f"<style>\n/* Inlined Google Fonts (Zero External Dependencies) */\n{embedded_fonts}\n</style>"
        html = re.sub(font_link_regex, replacement, html)
        print("[Bundle] Inlined Google fonts as base64 woff2 data URIs.")
    else:
        print("[Bundle] No external Google font link tags found (already inlined or offline).")

    # Verify zero external dependencies remaining
    remaining_urls = re.findall(r'https?://[^\s"\'<>]+', html)
    print(f"[Bundle] Remaining external URLs: {len(remaining_urls)}")
    for u in set(remaining_urls):
        print(f"  - {u}")

    with open(DIST_HTML, "w", encoding="utf-8") as f:
        f.write(html)
    print(f"[Bundle] Complete standalone bundle written to {DIST_HTML} ({len(html)} bytes)")

if __name__ == "__main__":
    bundle()
