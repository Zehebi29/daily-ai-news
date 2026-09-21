#!/usr/bin/env python3
import urllib.request, urllib.parse, json, time, re, sys

def get(url, timeout=30):
    req = urllib.request.Request(url, headers={"User-Agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 Chrome/124 Safari/537.36"})
    with urllib.request.urlopen(req, timeout=timeout) as r:
        return r.read().decode("utf-8", "replace")

def hn(url):
    return json.loads(get(url))

now = int(time.time())
DAY = 86400

def hn_q(q, days=3, sort="search_by_date", tags="story", n=40, mp=0):
    cu = now - days * DAY
    u = ("https://hn.algolia.com/api/v1/%s?query=%s&tags=%s&hitsPerPage=%d&numericFilters=created_at_i>%d"
         % (sort, urllib.parse.quote(q), tags, n, cu))
    if mp:
        u += ",points>%d" % mp
    return hn(u)

seen = {}
def add(h, tag):
    oid = h.get("objectID")
    t = h.get("title") or ""
    if not t:
        return
    if oid not in seen or (h.get("points") or 0) > (seen[oid].get("p") or 0):
        seen[oid] = {"t": t, "u": h.get("url") or ("https://news.ycombinator.com/item?id=" + str(oid)),
                     "hn": "https://news.ycombinator.com/item?id=%s" % oid,
                     "p": h.get("points") or 0, "c": h.get("num_comments") or 0,
                     "a": h.get("created_at"), "q": tag}

QUERIES = ["open source model", "open weights", "releases model", "LLM benchmark", "Qwen", "DeepSeek",
           "Llama", "GPT-5", "Claude", "Gemini", "Mistral", "Kimi", "GLM", "Zhipu", "MiniMax",
           "Show HN AI", "inference engine", "fine-tuned model", "MoE", "reasoning model",
           "model release", "Hugging Face", "vLLM", "quantization", "world model", "agent model"]

for q in QUERIES:
    try:
        r = hn_q(q, days=3, n=30)
        for h in r.get("hits", []):
            add(h, "q:" + q)
    except Exception as e:
        print("ERR", q, e, file=sys.stderr)
    time.sleep(0.2)

# search by points (7d)
for q in ["open source model", "new model", "LLM release"]:
    try:
        r = hn_q(q, days=7, sort="search", n=30, mp=50)
        for h in r.get("hits", []):
            add(h, "pts:" + q)
    except Exception as e:
        print("ERR2", q, e, file=sys.stderr)
    time.sleep(0.2)

# broad scan
for d in (1, 2, 3):
    try:
        cu = now - d * DAY
        u = ("https://hn.algolia.com/api/v1/search_by_date?tags=story&hitsPerPage=200&numericFilters=created_at_i>%d" % cu)
        r = hn(u)
        for h in r.get("hits", []):
            add(h, "broad%d" % d)
    except Exception as e:
        print("BR ERR", e, file=sys.stderr)

items = [v for v in seen.values() if v["p"] >= 15]
items.sort(key=lambda x: -x["p"])
print("TOTAL", len(seen), "cand>=15", len(items))
for it in items[:80]:
    print("%4d | %s | %s | %s" % (it["p"], it["a"][:16], it["t"][:110], (it["u"] or "")[:110]))
