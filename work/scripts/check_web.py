"""Сверка выжимок из сети (work/brief/W*.md): открываются ли ссылки, сколько разных источников и доля свежих (2023–2026)."""
import glob, os, re, ssl, sys, urllib.request
from concurrent.futures import ThreadPoolExecutor
WORK = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..")
URL = re.compile(r"https?://[^\s)\]>»\"']+")
DATE = re.compile(r"\b(0[1-9]|1[0-2])\.(20\d\d)\b|\b(20\d\d)\b")
ctx = ssl.create_default_context(cafile=os.environ.get("SSL_CERT_FILE") or "/root/.ccr/ca-bundle.crt") if os.path.exists("/root/.ccr/ca-bundle.crt") else None

def status(url):
    try:
        req = urllib.request.Request(url, headers={"User-Agent": "Mozilla/5.0"}, method="GET")
        with urllib.request.urlopen(req, timeout=12, context=ctx) as r:
            return r.status
    except urllib.error.HTTPError as e:
        return e.code
    except Exception:
        return 0

def main():
    allurls = {}
    for p in sorted(glob.glob(os.path.join(WORK, "brief", "W*.md"))):
        txt = open(p, encoding="utf-8").read()
        urls = sorted(set(u.rstrip(".,;:") for u in URL.findall(txt)))
        facts = [l for l in txt.splitlines() if l.strip().startswith("- ") and URL.search(l)]
        fresh = sum(1 for l in facts if any(int(y or y2) >= 2023 for _, y, y2 in DATE.findall(l) if (y or y2)))
        allurls[os.path.basename(p)] = urls
        print(f"{os.path.basename(p)}: ссылок {len(urls)}, фактов со ссылкой {len(facts)}, из них с датой 2023+ {fresh}")
    flat = sorted(set(u for v in allurls.values() for u in v))
    with ThreadPoolExecutor(16) as ex:
        res = dict(zip(flat, ex.map(status, flat)))
    ok = [u for u, s in res.items() if 200 <= s < 400]
    blocked = [u for u, s in res.items() if s in (401, 403, 406, 429, 0)]
    dead = [u for u, s in res.items() if s in (404, 410)]
    print(f"всего разных ссылок {len(flat)}: открываются {len(ok)}, блокируют проверку {len(blocked)}, не найдены {len(dead)}")
    for u in dead:
        print("  404:", u)
    return 0

if __name__ == "__main__":
    sys.exit(main())
