import json, urllib.request, urllib.parse, time, sys

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

def hn_flt(q, days, minp):
    cutoff = NOW - days * DAY
    url = ("https://hn.algolia.com/api/v1/search?query=" + urllib.parse.quote(q) +
           "&tags=story&hitsPerPage=60&numericFilters=" +
           urllib.parse.quote("created_at_i>%d,points>=%d" % (cutoff, minp)))
    d = get(url)
    out = []
    for h in d.get("hits", []):
        out.append((h.get("points") or 0, h.get("num_comments") or 0, h.get("title") or "",
                    h.get("url") or "", "https://news.ycombinator.com/item?id=" + str(h.get("objectID"))))
    return out

def merge(*lists):
    seen = {}
    for L in lists:
        for p, c, t, u, d in L:
            k = u or t
            if k not in seen or seen[k][0] < p:
                seen[k] = (p, c, t, u, d)
    return sorted(seen.values(), key=lambda x: -x[0])

if __name__ == "__main__":
    mode = sys.argv[1]
    res = []
    if mode == "broad":
        for d in (1, 2, 3):
            url = ("https://hn.algolia.com/api/v1/search_by_date?tags=story&hitsPerPage=200&numericFilters=" +
                   urllib.parse.quote("created_at_i>%d" % (NOW - d * DAY)) +
                   "&query=" + urllib.parse.quote("AI"))
            dd = get(url)
            for h in dd.get("hits", []):
                res.append((h.get("points") or 0, h.get("num_comments") or 0, h.get("title") or "",
                            h.get("url") or "", "https://news.ycombinator.com/item?id=" + str(h.get("objectID"))))
        res = merge(res)
    else:
        kw = json.loads(sys.argv[2])
        for q in kw:
            res = merge(res, hn_flt(q, 8, 12))
    for p, c, t, u, d in res:
        if p < 20 and mode == "broad":
            continue
        print("%4d %4d | %s | %s | %s" % (p, c, t, u[:110], d))
