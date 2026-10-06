import json, urllib.request, time, re, html, datetime
UA={"User-Agent":"Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 Chrome/120 Safari/537.36"}
def get(u):
    req=urllib.request.Request(u,headers=UA)
    with urllib.request.urlopen(req,timeout=25) as r:
        return json.loads(r.read().decode("utf-8","replace"))
def ts(x):
    return datetime.datetime.utcfromtimestamp(x).strftime("%m-%d %H:%M")
for oid in ["49919910","49910553","49911520","49914236","49913950"]:
    d=get("https://hn.algolia.com/api/v1/items/"+oid)
    print(oid, "|", ts(d.get("created_at_i") or 0), "|", d.get("points"), "pts", d.get("num_comments") if "num_comments" in d else "", "|", d.get("title"))
    print("   URL:", d.get("url"))
    t=d.get("text") or ""
    if t:
        print("   TEXT:", re.sub(r"\s+"," ",html.unescape(re.sub(r"<[^>]+>"," ",t)))[:400])
    time.sleep(1)
