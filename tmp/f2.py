import urllib.request, re, html
UA={"User-Agent":"Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 Chrome/120 Safari/537.36"}
def fetch(u):
    try:
        req=urllib.request.Request(u,headers=UA)
        with urllib.request.urlopen(req,timeout=30) as r: return r.read().decode("utf-8","replace")
    except Exception as e: return "ERR "+str(e)
def text(h):
    h=re.sub(r"(?is)<(script|style|svg|noscript).*?</\1>"," ",h)
    t=re.sub(r"(?s)<[^>]+>"," ",h); t=html.unescape(t)
    return re.sub(r"\s+"," ",t).strip()
t=text(fetch("https://insufferable.dev/posts/the-ai-race-just-got-awkward/"))
print("INS:", t[:1600])
print()
sh=text(fetch("https://thenewstack.io/coding-agents-leaked-screenshots/"))
for m in re.finditer(r"[^.]*screenshot[^.]*\.", sh):
    s=m.group(0).strip()
    if len(s)>50: print(" *", s[:400])
