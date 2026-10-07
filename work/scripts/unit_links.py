"""Печатает дату, тип и ссылки абзацев исследования: python3 unit_links.py R2-0042 R3-0068"""
import json, os, sys, re
WORK = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..")
units = {u["id"]: u for u in json.load(open(os.path.join(WORK, "units.json"), encoding="utf-8"))}
for uid in sys.argv[1:]:
    u = units.get(uid)
    if not u:
        print(uid, "НЕТ ТАКОГО АБЗАЦА"); continue
    links = []
    for l in u.get("links") or []:
        links.append(l if isinstance(l, str) else (l.get("url"), l.get("label")))
    md = re.findall(r"\[([^\]]+)\]\((https?://[^)]+)\)", u["text"])
    print(uid, "|", u["text"][:160].replace("\n", " "))
    for lab, url in md[:6]:
        print("   ", lab, "->", url)
    for x in links[:4]:
        print("   link:", x)
