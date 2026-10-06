import urllib.request, re, html, sys
UA={"User-Agent":"Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 Chrome/120 Safari/537.36"}
def fetch(u):
    try:
        req=urllib.request.Request(u,headers=UA)
        with urllib.request.urlopen(req,timeout=30) as r:
            return r.read().decode("utf-8","replace")
    except Exception as e:
        return "ERR "+str(e)
def text(h):
    h=re.sub(r"(?is)<(script|style|svg|noscript).*?</\1>"," ",h)
    t=re.sub(r"(?s)<[^>]+>"," ",h)
    t=html.unescape(t)
    return re.sub(r"\s+"," ",t).strip()
URLS = [
 "https://blog.google/innovation-and-ai/models-and-research/gemini-models/gemini-4-argon/",
 "https://artificialanalysis.ai/models/gemini-4-argon",
 "https://news.synopsys.com/2026-09-30-OpenAI-and-Synopsys-Announce-GPT-Synopsys-Frontier-Intelligence",
 "https://techcrunch.com/2026/09/30/reddit-is-killing-rss-feeds-ending-public-api-access-because-of-ai-bots/",
 "https://www.reuters.com/business/ftc-opens-probe-into-ai-giants-including-anthropic-openai-new-york-post-report-2026-09-30/",
 "https://insufferable.dev/posts/the-ai-race-just-got-awkward/",
]
KW = re.compile(r"(benchmark|price|pricing|token|availab|launch|release|SWE|Terminal|GPQA|score|context|window|param|FTC|probe|inquiry|antitrust|RSS|API|Reddit|chip|EDA|design|Synopsys|Sol|percent|%|Argon|dropped|skeptic|cost)", re.I)
for u in URLS:
    c = fetch(u)
    print("="*100)
    print(u, "LEN", len(c))
    if c.startswith("ERR"):
        print(c); continue
    t = text(c)
    # split into sentences and keep those matching keywords
    sents = re.split(r"(?<=[.!?])\s+", t)
    out, seen = [], set()
    for s in sents:
        if 40 < len(s) < 500 and KW.search(s):
            k = s[:60]
            if k in seen: continue
            seen.add(k); out.append(s)
    for s in out[:45]:
        print(" *", s)
