#!/usr/bin/env python3
import urllib.request, urllib.parse, json, re, html

def get(url, timeout=30):
    req = urllib.request.Request(url, headers={"User-Agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 Chrome/124 Safari/537.36"})
    with urllib.request.urlopen(req, timeout=timeout) as r:
        return r.read().decode("utf-8", "replace")

def ptext(url, limit=1500):
    try:
        h = get(url)
    except Exception as e:
        return "FAIL: %s" % e
    h = re.sub(r"(?is)<(script|style|svg|nav|footer|head)[^>]*>.*?</\1>", " ", h)
    h = re.sub(r"(?is)<br\s*/?>|</p>|</div>|</li>|</h[1-6]>", "\n", h)
    t = html.unescape(re.sub(r"<[^>]+>", " ", h))
    return re.sub(r"\s+", " ", t).strip()[:limit]

for u in ["https://huggingface.co/Altworld/Hemmingway-1",
          "https://huggingface.co/convaiinnovations/laya",
          "https://huggingface.co/XingChen-AGI/Xing4.0-29B-A4B",
          "https://cactuscompute.com/needle"]:
    print("=" * 80)
    print(u)
    print(ptext(u))

print("=" * 80)
print("HN threads: Cactus Needle / Pirate Face / mini-AGI comments")
for q in ["Cactus Needle", "Pirate Face", "mini-AGI"]:
    try:
        r = json.loads(get("https://hn.algolia.com/api/v1/search?query=%s&tags=story&hitsPerPage=3" % urllib.parse.quote(q)))
        for h in r["hits"]:
            print("%s | %s pts | %s comments | %s | https://news.ycombinator.com/item?id=%s" % (h["created_at"][:16], h["points"], h["num_comments"], h["title"][:90], h["objectID"]))
        h0 = r["hits"][0]
        if h0["num_comments"]:
            it = json.loads(get("https://hn.algolia.com/api/v1/items/%s" % h0["objectID"]))
            for c in [c for c in (it.get("children") or []) if c.get("text")][:4]:
                print("    *", re.sub(r"\s+", " ", html.unescape(re.sub(r"<[^>]+>", " ", c["text"])))[:330])
    except Exception as e:
        print(q, "FAIL", e)
    print()

print("=" * 80)
print("FT: AI chatbots wrong financial answers")
print(ptext("https://www.ft.com/content/c0cd359d-df84-4208-a789-ffa864b43666", 1200))
print()
print("Verge UN + Amazon/Meta Muse")
print(ptext("https://www.theverge.com/ai-artificial-intelligence/998090/un-ai-panel-hugging-face-hack-precautionary-principle", 1600))
print()
print(ptext("https://www.theverge.com/tech/998078/amazon-blocks-meta-muse-ai-agent-shopping", 1200))
