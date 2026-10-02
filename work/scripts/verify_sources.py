"""Шаг 2.4. Первая сверка с первоисточником.

Для каждой записи отбора открывает страницы-источники и ищет на них значимые
числа из записи. Значимое число: с дробной частью, из трёх и более цифр или со
знаком процента. Короткие целые не проверяются: они совпадают случайно.
Выход: sources_check.json и сводка в консоль. Страницы кладутся в кэш.
"""
import hashlib
import html
import json
import os
import re
import ssl
import sys
import urllib.request
from concurrent.futures import ThreadPoolExecutor

HERE = os.path.dirname(os.path.abspath(__file__))
WORK = os.path.join(HERE, "..")
CACHE = os.path.join(WORK, "cache")
UA = "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0 Safari/537.36"
SIG_RE = re.compile(r"\d+[.,]\d+|\d{3,}|\d+(?=\s?%)")


def fetch(url: str) -> tuple[str, str]:
    """Вернуть (статус, текст страницы)."""
    key = os.path.join(CACHE, hashlib.sha1(url.encode()).hexdigest() + ".txt")
    if os.path.exists(key):
        data = open(key, encoding="utf-8").read()
        return data.split("\n", 1)[0], data.split("\n", 1)[1] if "\n" in data else ""
    status, text = "не открылась", ""
    try:
        req = urllib.request.Request(url, headers={"User-Agent": UA, "Accept-Language": "ru,en;q=0.8"})
        with urllib.request.urlopen(req, timeout=20, context=ssl.create_default_context()) as r:
            ctype = r.headers.get("Content-Type", "")
            raw = r.read(3_000_000)
            if "pdf" in ctype or url.lower().endswith(".pdf"):
                status = "pdf"
            else:
                enc = r.headers.get_content_charset() or "utf-8"
                page = raw.decode(enc, errors="replace")
                page = re.sub(r"(?is)<(script|style|noscript)[^>]*>.*?</\1>", " ", page)
                text = html.unescape(re.sub(r"(?s)<[^>]+>", " ", page))
                text = re.sub(r"\s+", " ", text)
                status = "открылась" if len(text) > 1500 else "пустая или заглушка"
    except Exception as exc:  # сеть, блокировка, сертификат
        status = "не открылась: " + type(exc).__name__
    open(key, "w", encoding="utf-8").write(status + "\n" + text)
    return status, text


def norm_num(x: str) -> str:
    return x.replace(",", ".")


def page_numbers(text: str) -> set[str]:
    t = text.replace(" ", " ").replace(" ", " ")
    t = re.sub(r"(?<=\d)[ ,](?=\d{3}\b)", "", t)  # 12 000 и 12,000 -> 12000
    return {norm_num(x) for x in re.findall(r"\d+(?:[.,]\d+)?", t)}


def main() -> int:
    os.makedirs(CACHE, exist_ok=True)
    entries = json.load(open(os.path.join(WORK, "variants.json"), encoding="utf-8"))
    urls = sorted({l["url"] for e in entries for l in e["links"]})
    with ThreadPoolExecutor(max_workers=12) as pool:
        pages = dict(zip(urls, pool.map(fetch, urls)))
    nums_cache = {u: page_numbers(t) for u, (s, t) in pages.items() if s == "открылась"}
    out, tally = [], {}
    for e in entries:
        claim = "" if e["numbers"].lower().startswith("нет") else e["numbers"]
        claim = re.sub(r"(?<=\d)[  ](?=\d{3}\b)", "", claim)
        sig = sorted({norm_num(x) for x in SIG_RE.findall(claim)})
        res = {"packet": e["packet"], "n": e["n"], "who": e["who"], "sig_numbers": sig, "pages": []}
        best = None
        for l in e["links"]:
            status, _ = pages[l["url"]]
            item = {"url": l["url"], "page": status}
            if status == "открылась" and sig:
                found = [x for x in sig if x in nums_cache[l["url"]]]
                item["found"], item["missing"] = found, [x for x in sig if x not in found]
            res["pages"].append(item)
        if not sig:
            verdict = "значимых чисел нет"
        elif not e["links"]:
            verdict = "нет ссылки в абзацах"
        else:
            opened = [p for p in res["pages"] if p["page"] == "открылась"]
            if not opened:
                verdict = "страницы не открылись скрипту"
            else:
                found_any = set().union(*[set(p["found"]) for p in opened])
                if len(found_any) == len(sig):
                    verdict = "все числа найдены на страницах"
                elif found_any:
                    verdict = "часть чисел найдена"
                else:
                    verdict = "числа на страницах не найдены"
                res["not_found"] = [x for x in sig if x not in found_any]
        res["verdict"] = verdict
        tally[verdict] = tally.get(verdict, 0) + 1
        out.append(res)
    json.dump(out, open(os.path.join(WORK, "sources_check.json"), "w", encoding="utf-8"), ensure_ascii=False, indent=1)
    st = {}
    for s, _ in pages.values():
        st[s.split(":")[0]] = st.get(s.split(":")[0], 0) + 1
    print("страниц:", len(urls), st)
    for k, v in sorted(tally.items(), key=lambda kv: -kv[1]):
        print(f"{v:4d}  {k}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
