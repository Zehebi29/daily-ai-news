#!/usr/bin/env python3
import urllib.request, json, re, sys, html

def get(url, timeout=35):
    req = urllib.request.Request(url, headers={"User-Agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 Chrome/124 Safari/537.36",
                                               "Accept-Language": "en-US,en;q=0.9"})
    with urllib.request.urlopen(req, timeout=timeout) as r:
        return r.read().decode("utf-8", "replace")

def text(url, limit=2600):
    try:
        h = get(url)
    except Exception as e:
        return "FAIL %s: %s" % (url, e)
    h = re.sub(r"(?is)<(script|style|svg|nav|footer|head)[^>]*>.*?</\1>", " ", h)
    h = re.sub(r"(?is)<br\s*/?>|</p>|</div>|</li>|</h[1-6]>", "\n", h)
    t = re.sub(r"<[^>]+>", " ", h)
    t = html.unescape(t)
    t = re.sub(r"[ \t\xa0]+", " ", t)
    t = re.sub(r"\n\s*\n+", "\n", t)
    return t.strip()[:limit]

URLS = [
 "https://qwen.ai/blog?id=qwen-image-2.1",
 "https://pirateface.co/",
 "https://github.com/volotat/mini-AGI/",
 "https://github.com/BytedTsinghua-SIA/DAPO",
]
for u in URLS:
    print("=" * 90)
    print("URL:", u)
    print(text(u))

print("=" * 90)
print("HF createdAt check")
for mid in ["Qwen/Qwen-Image-2.1","Altworld/Hemmingway-1","MiniMaxAI/MiniMax-H3","internlm/Atria-Dawn-Preview",
            "Qwen/Qwen3.8-Flash-Next","zai-org/GLM-5.3-Flash","XingChen-AGI/Xing4.0-29B-A4B",
            "openbmb/MiniCPM5-2B","convaiinnovations/laya","deepseek-ai/DeepSeek-V4.1-Flash",
            "TaichuAI/ZDTaichu5.0-9B","TokenRhythm/NeoHorse-1-9B","m-a-p/YuE2-3B","Lightricks/LTX-2.5",
            "netease-youdao/Confucius4-R2T2","Qwen/Qwen3.8-27B"]:
    try:
        d = json.loads(get("https://huggingface.co/api/models/" + mid))
        print("%-38s created=%s likes=%s dl=%s tags=%s" % (mid, d.get("createdAt","")[:16], d.get("likes"), d.get("downloads"), ",".join((d.get("tags") or [])[:6])))
    except Exception as e:
        print(mid, "FAIL", e)
