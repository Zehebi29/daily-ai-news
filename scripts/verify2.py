#!/usr/bin/env python3
import urllib.request, json, re, html, time, urllib.parse

def get(url, timeout=35):
    req = urllib.request.Request(url, headers={"User-Agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 Chrome/124 Safari/537.36"})
    with urllib.request.urlopen(req, timeout=timeout) as r:
        return r.read().decode("utf-8", "replace")

print("--- HF createdAt ---")
for mid in ["Qwen/Qwen-Image-2.1","XingChen-AGI/Xing4.0-29B-A4B","MiniMaxAI/MiniMax-H3","internlm/Atria-Dawn-Preview",
            "Qwen/Qwen3.8-Flash-Next","zai-org/GLM-5.3-Flash","openbmb/MiniCPM5-2B","convaiinnovations/laya",
            "deepseek-ai/DeepSeek-V4.1-Flash","TaichuAI/ZDTaichu5.0-9B","TokenRhythm/NeoHorse-1-9B","m-a-p/YuE2-3B",
            "Lightricks/LTX-2.5","netease-youdao/Confucius4-R2T2","Altworld/Hemmingway-1","Qwen/Qwen3.8-27B"]:
    try:
        d = json.loads(get("https://huggingface.co/api/models/" + mid))
        print("%-38s created=%s likes=%-6s dl=%-9s" % (mid, d.get("createdAt","")[:16], d.get("likes"), d.get("downloads")))
    except Exception as e:
        print(mid, "FAIL", e)

print()
print("--- Qwen Image 2.1 model card (HF) ---")
try:
    h = get("https://huggingface.co/Qwen/Qwen-Image-2.1")
    h = re.sub(r"(?is)<(script|style|svg|nav|footer|head)[^>]*>.*?</\1>", " ", h)
    t = html.unescape(re.sub(r"<[^>]+>", " ", h))
    t = re.sub(r"[ \t\xa0]+", " ", t)
    t = re.sub(r"\n\s*\n+", "\n", t)
    print(t.strip()[:3000])
except Exception as e:
    print("FAIL", e)

print()
print("--- HN item for Qwen Image 2.1 ---")
try:
    r = json.loads(get("https://hn.algolia.com/api/v1/search?query=%22Qwen%20Image%202.1%22&tags=story&hitsPerPage=5"))
    for h in r["hits"]:
        print(h["objectID"], h["points"], h["num_comments"], h["created_at"], h["title"], h.get("url"))
        if h["num_comments"] > 0:
            it = json.loads(get("https://hn.algolia.com/api/v1/items/%s" % h["objectID"]))
            cmts = [c for c in (it.get("children") or []) if c.get("text")]
            cmts.sort(key=lambda c: -(c.get("points") or 0))
            for c in cmts[:6]:
                tx = html.unescape(re.sub(r"<[^>]+>", " ", c.get("text") or ""))
                print("   *", re.sub(r"\s+", " ", tx)[:400])
except Exception as e:
    print("FAIL", e)

print()
print("--- searches: vergetc/tc qwen image ---")
for u in ["https://techcrunch.com/wp-json/wp/v2/search?search=qwen%20image&per_page=5",
          "https://www.theverge.com/rss/search.xml?q=qwen"]:
    try:
        print(u, "->", get(u)[:300].replace("\n"," "))
    except Exception as e:
        print(u, "FAIL", e)

print()
print("--- Verge AI page titles today ---")
try:
    h = get("https://www.theverge.com/ai-artificial-intelligence")
    for m in re.finditer(r'<a[^>]+href="(/[^"]+)"[^>]*>\s*<[^>]*>\s*([^<]{15,140})</', h):
        print("  -", m.group(1), "|", html.unescape(m.group(2)).strip()[:110])
except Exception as e:
    print("FAIL", e)

print()
print("--- HF papers trending ---")
for u in ["https://huggingface.co/api/daily_papers?limit=15"]:
    try:
        d = json.loads(get(u))
        for p in d:
            pp = p.get("paper", {})
            print("  -", pp.get("publishedAt","")[:10], "|", pp.get("title","")[:110], "|", pp.get("upvotes"), "| https://arxiv.org/abs/"+str(pp.get("id")))
    except Exception as e:
        print("FAIL", e)

print()
print("--- Alibaba medical (SCMP) + Xing4.0 grep ---")
for u in ["https://www.scmp.com/tech/big-tech/article/3368055/alibaba-open-sources-medical-ai-model-can-detect-cancer-and",
          "https://xingchen-agi.com"]:
    try:
        h = get(u)
        h = re.sub(r"(?is)<(script|style|svg|nav|footer|head)[^>]*>.*?</\1>", " ", h)
        t = html.unescape(re.sub(r"<[^>]+>", " ", h))
        print("URL", u)
        print(re.sub(r"\s+", " ", t).strip()[:1400])
    except Exception as e:
        print(u, "FAIL", e)
