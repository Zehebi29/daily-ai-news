#!/usr/bin/env python3
# RSS + GitHub trending + HF trending scanner
import urllib.request, json, re, sys, datetime

def get(url, timeout=35):
    req = urllib.request.Request(url, headers={"User-Agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 Chrome/124 Safari/537.36"})
    with urllib.request.urlopen(req, timeout=timeout) as r:
        return r.read().decode("utf-8", "replace")

FEEDS = {
  "Verge": "https://www.theverge.com/rss/index.xml",
  "Ars": "https://feeds.arstechnica.com/arstechnica/index",
  "TechCrunch": "https://techcrunch.com/category/artificial-intelligence/feed/",
  "TNS": "https://thenewstack.io/feed/",
  "HNfront": "https://hnrss.org/frontpage?points=100",
  "VentureBeat": "https://venturebeat.com/category/ai/feed/",
  "Register": "https://www.theregister.com/software/ai_ml/headlines.atom",
}

def clean(s):
    s = re.sub(r"<!\[CDATA\[(.*?)\]\]>", r"\1", s, flags=re.S)
    s = re.sub(r"<[^>]+>", "", s)
    s = (s.replace("&amp;", "&").replace("&lt;", "<").replace("&gt;", ">")
          .replace("&quot;", '"').replace("&#39;", "'").replace("&apos;", "'").replace("&nbsp;", " "))
    return re.sub(r"\s+", " ", s).strip()

for name, url in FEEDS.items():
    try:
        xml = get(url)
        blocks = re.findall(r"<(?:item|entry)[ >].*?</(?:item|entry)>", xml, flags=re.S)
        print("=== %s (%d items) ===" % (name, len(blocks)))
        for b in blocks[:22]:
            m = re.search(r"<title[^>]*>(.*?)</title>", b, flags=re.S)
            l = re.search(r"<link[^>]*href=\"([^\"]+)\"", b) or re.search(r"<link[^>]*>(.*?)</link>", b, flags=re.S)
            d = re.search(r"<(?:pubDate|published|updated)[^>]*>(.*?)</", b, flags=re.S)
            t = clean(m.group(1)) if m else "?"
            lk = clean(l.group(1)) if l else "?"
            dd = clean(d.group(1)) if d else "?"
            print("  - [%s] %s | %s" % (dd[:25], t[:120], lk[:140]))
    except Exception as e:
        print("=== %s FAILED: %s ===" % (name, e))
