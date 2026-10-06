import json, urllib.request, urllib.parse, time, datetime
UA = {"User-Agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 Chrome/120 Safari/537.36"}
NOW = int(time.time())
def get(url):
    req = urllib.request.Request(url, headers=UA)
    with urllib.request.urlopen(req, timeout=25) as r:
        return json.loads(r.read().decode("utf-8", "replace"))
def ts(x):
    return datetime.datetime.utcfromtimestamp(x).strftime("%m-%d %H:%M")
# today's top stories, no query, last 30h
url = ("https://hn.algolia.com/api/v1/search_by_date?tags=story&hitsPerPage=300&numericFilters=" +
       urllib.parse.quote("created_at_i>%d" % (NOW - 30*3600)))
d = get(url)
rows = []
for h in d.get("hits", []):
    p = h.get("points") or 0
    if p >= 25:
        rows.append((p, h.get("num_comments") or 0, ts(h.get("created_at_i")), h.get("title") or "",
                     (h.get("url") or "")[:100], "https://news.ycombinator.com/item?id=" + str(h.get("objectID"))))
for r in sorted(rows, reverse=True):
    print("%4d %4dc %s | %s | %s | %s" % r)
print("TOTAL>=25:", len(rows))
