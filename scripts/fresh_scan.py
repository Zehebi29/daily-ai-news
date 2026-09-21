#!/usr/bin/env python3
# Today's fresh HN (>=8 pts) + GitHub trending + HF trending
import urllib.request, urllib.parse, json, re, sys, time

def get(url, timeout=35):
    req = urllib.request.Request(url, headers={"User-Agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 Chrome/124 Safari/537.36"})
    with urllib.request.urlopen(req, timeout=timeout) as r:
        return r.read().decode("utf-8", "replace")

AIRE = re.compile(r"\b(ai|llm|model|gpt|claude|gemini|qwen|deepseek|llama|agent|neural|inference|open.?source|weights|transformer|diffusion|robot|nvidia|anthropic|openai|mistral|kimi|glm|jev|benchmark|dataset|training)\b", re.I)

now = int(time.time())
DAY = 86400
# fresh today (last 16h) + yesterday, lower threshold
seen = {}
for days, mp in ((0.7, 5), (1.5, 8)):
    for page in (0, 1):
        try:
            cu = int(now - days * DAY)
            u = ("https://hn.algolia.com/api/v1/search_by_date?tags=story&hitsPerPage=100&page=%d&numericFilters=created_at_i>%d,points>%d" % (page, cu, mp))
            r = json.loads(get(u))
            for h in r.get("hits", []):
                t = h.get("title") or ""
                if not AIRE.search(t):
                    continue
                seen[h["objectID"]] = (h.get("points") or 0, h.get("created_at", "")[:16], t, h.get("url") or "", h.get("num_comments"))
        except Exception as e:
            print("ERR", days, page, e, file=sys.stderr)
        time.sleep(0.2)

items = sorted(seen.values(), key=lambda x: (x[1], -x[0]), reverse=True)
print("=== FRESH HN (%d) ===" % len(items))
for p, a, t, u, c in items:
    print("%4d | %s | %s | %s" % (p, a, t[:110], u[:120]))

print()
print("=== GITHUB TRENDING (python) ===")
try:
    html = get("https://github.com/trending/python?since=daily")
    for m in re.finditer(r'<h2 class="h3 lh-condensed">\s*<a href="([^"]+)"[^>]*>\s*(.*?)\s*</a>\s*</h2>\s*(?:<p class="col-9[^"]*">\s*(.*?)\s*</p>)?', html, re.S):
        repo = m.group(1).strip()
        desc = re.sub(r"<[^>]+>", "", m.group(3) or "").strip()[:130]
        print("  - %s | %s" % (repo, desc))
except Exception as e:
    print("GH python FAILED", e)
try:
    html = get("https://github.com/trending?since=daily")
    for m in re.finditer(r'<h2 class="h3 lh-condensed">\s*<a href="([^"]+)"[^>]*>\s*(.*?)\s*</a>\s*</h2>\s*(?:<p class="col-9[^"]*">\s*(.*?)\s*</p>)?', html, re.S):
        repo = m.group(1).strip()
        desc = re.sub(r"<[^>]+>", "", m.group(3) or "").strip()[:130]
        print("  - %s | %s" % (repo, desc))
except Exception as e:
    print("GH all FAILED", e)

print()
print("=== HF TRENDING ===")
try:
    html = get("https://huggingface.co/models?sort=trending")
    found = 0
    for m in re.finditer(r'href="/([\w\.\-]+/[\w\.\-]+)"[^>]*>', html):
        s = m.group(1)
        if s.count("/") == 1 and not s.startswith("docs"):
            print("  -", s)
            found += 1
            if found > 40:
                break
except Exception as e:
    print("HF FAILED", e)

print()
print("=== HF PAPERS / trending models API ===")
try:
    d = json.loads(get("https://huggingface.co/api/models?sort=trendingScore&direction=-1&limit=25"))
    for m in d:
        print("  - %s | dl=%s | likes=%s" % (m.get("modelId"), m.get("downloads"), m.get("likes")))
except Exception as e:
    print("HF api FAILED", e)
