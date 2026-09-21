#!/usr/bin/env python3
import urllib.request, urllib.parse, json, re, html

def get(url, timeout=30):
    req = urllib.request.Request(url, headers={"User-Agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 Chrome/124 Safari/537.36"})
    with urllib.request.urlopen(req, timeout=timeout) as r:
        return r.read().decode("utf-8", "replace")

def ptext(url, limit=5000):
    try:
        h = get(url)
    except Exception as e:
        return "FAIL: %s" % e
    h = re.sub(r"(?is)<(script|style|svg|nav|footer|head)[^>]*>.*?</\1>", " ", h)
    h = re.sub(r"(?is)<br\s*/?>|</p>|</div>|</li>|</h[1-6]>", "\n", h)
    t = html.unescape(re.sub(r"<[^>]+>", " ", h))
    return re.sub(r"[ \t]+", " ", re.sub(r"\n\s*\n+", "\n", t)).strip()[:limit]

print("=== Verge UN full ===")
print(ptext("https://www.theverge.com/ai-artificial-intelligence/998090/un-ai-panel-hugging-face-hack-precautionary-principle", 5000))
print()
print("=== Laya card raw ===")
print(get("https://huggingface.co/convaiinnovations/laya/raw/main/README.md")[:3000])
print()
print("=== Xing4.0 card raw ===")
try:
    print(get("https://huggingface.co/XingChen-AGI/Xing4.0-29B-A4B/raw/main/README.md")[:2500])
except Exception as e:
    print("FAIL", e)
print()
print("=== Qwen blog via HN top comment/other coverage ===")
print(ptext("https://www.comfy.org/blog/qwen-image-2-1", 1200)[:1200])
