import json, urllib.request, urllib.parse, time, sys, datetime

UA = {"User-Agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 Chrome/120 Safari/537.36"}
NOW = int(time.time())
DAY = 86400

def get(url, tries=3):
    for i in range(tries):
        try:
            req = urllib.request.Request(url, headers=UA)
            with urllib.request.urlopen(req, timeout=25) as r:
                return json.loads(r.read().decode("utf-8", "replace"))
        except Exception as e:
            if i == tries - 1:
                return {"_err": str(e)}
            time.sleep(2)

def ts(x):
    try:
        return datetime.datetime.utcfromtimestamp(x).strftime("%m-%d %H:%M")
    except Exception:
        return "?"

queries = sys.argv[1:]
seen = {}
for q in queries:
    for days in (3, 8):
        url = ("https://hn.algolia.com/api/v1/search_by_date?query=" + urllib.parse.quote(q) +
               "&tags=story&hitsPerPage=40&numericFilters=" + urllib.parse.quote("created_at_i>%d,points>=8" % (NOW - days*DAY)))
        d = get(url)
        for h in d.get("hits", []):
            oid = str(h.get("objectID"))
            p = h.get("points") or 0
            if oid not in seen or seen[oid][0] < p:
                seen[oid] = (p, h.get("num_comments") or 0, ts(h.get("created_at_i") or 0),
                             h.get("title") or "", h.get("url") or "", "https://news.ycombinator.com/item?id=" + oid)
for v in sorted(seen.values(), key=lambda x: x[2], reverse=True):
    print("%s | %4d pts %4dc | %s | %s | %s" % (v[2], v[0], v[1], v[3][:95], (v[4] or "")[:100], v[5]))
