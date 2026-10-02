"""Шаги 2.2–2.3. Проверка записей отбора и расчёт силы источников.

Проверяет: формат, покрытие всех абзацев пакета, наличие чисел из записи
в указанных абзацах, наличие всех компаний из меток ссылок.
Считает силу: типы источников, независимые сайты, статусы проверки ссылок.
Выход: variants.json (все записи с опорой) и отчёт в консоль.
"""
import glob
import json
import os
import re
import sys
from urllib.parse import urlparse

HERE = os.path.dirname(os.path.abspath(__file__))
WORK = os.path.join(HERE, "..")
NOTES = ("/Users/urij/Library/Application Support/Claude/scratch-workspaces/"
         "04a091d9-9c6b-4cc2-a36e-0d43efe33d60/dcf82310-8165-479f-960f-ddcfa85873bf/"
         "scratch-2026-10-01-ab7d6b/research_notes/")
ID_RE = re.compile(r"R[123]-\d{4}")
NUM_RE = re.compile(r"\d+(?:[.,]\d+)?")


def norm(text: str) -> str:
    return text.replace(" ", " ").replace(" ", " ").replace("−", "-").replace(",", ".")


def load_status() -> dict:
    """Собрать статусы ссылок из файлов проверки всех трёх кругов."""
    st = {}
    for path in glob.glob(NOTES + "*/*.tsv"):
        name = os.path.basename(path)
        for line in open(path, encoding="utf-8", errors="replace"):
            parts = line.rstrip("\n").split("\t")
            url = next((p for p in parts if p.startswith("http")), None)
            if not url:
                continue
            rest = " ".join(p for p in parts if p != url).lower()
            if name in ("browser_status.tsv", "old_links_browser.tsv"):
                s = "браузер: открылась" if "exists" in rest else ("браузер: не открылась" if "blocked" in rest or "missing" in rest else None)
            else:
                code = re.search(r"\b(\d{3})\b", rest)
                if rest.startswith("ok") or (code and code.group(1) == "200"):
                    s = "открывается"
                elif code and code.group(1) in ("401", "403", "429", "999"):
                    s = "сайт блокирует проверку"
                else:
                    s = "не открывается"
            if s:
                prev = st.get(url)
                if prev is None or s.startswith("браузер: открылась") or (prev == "не открывается"):
                    st[url] = s
    return st


def parse_variants(path: str) -> tuple[list, set]:
    text = open(path, encoding="utf-8").read()
    body, _, skipped = text.partition("## Пропущено")
    entries = []
    for chunk in re.split(r"^###\s+", body, flags=re.M)[1:]:
        lines = chunk.strip().split("\n")
        e = {"who": lines[0].strip(), "gist": "", "numbers": "", "ids": [], "kind": ""}
        for l in lines[1:]:
            l = l.strip().lstrip("-").strip()
            for key, field in (("суть:", "gist"), ("числа:", "numbers"), ("вид:", "kind")):
                if l.lower().startswith(key):
                    e[field] = l[len(key):].strip()
            if l.lower().startswith("абзацы:"):
                e["ids"] = ID_RE.findall(l)
        entries.append(e)
    return entries, set(ID_RE.findall(skipped))


def main() -> int:
    units = {u["id"]: u for u in json.load(open(os.path.join(WORK, "units.json"), encoding="utf-8"))}
    index = json.load(open(os.path.join(WORK, "packets", "index.json"), encoding="utf-8"))
    status = load_status()
    all_entries, problems, report = [], 0, {}
    for path in sorted(glob.glob(os.path.join(WORK, "variants", "*.md"))):
        packet = os.path.basename(path)[:-3]
        if packet.startswith("_") or packet not in index:
            continue
        packet_ids = {u["id"] for u in units.values() if u["bucket"] == packet}
        entries, skipped = parse_variants(path)
        used = set()
        bad_fmt = bad_num = bad_ids = 0
        for n, e in enumerate(entries, 1):
            e["packet"], e["n"] = packet, n
            ids = [i for i in e["ids"] if i in units]
            if not e["gist"] or not ids:
                bad_fmt += 1
            if len(ids) != len(e["ids"]) or any(i not in packet_ids for i in ids):
                bad_ids += 1
            used |= set(ids)
            src = norm(" ".join(units[i]["text"] for i in ids))
            src_nums = set(NUM_RE.findall(src))
            claimed = NUM_RE.findall(norm(e["gist"] + " ; " + ("" if e["numbers"].lower().startswith("нет") else e["numbers"])))
            missing = [x for x in claimed if x not in src_nums and not re.fullmatch(r"\d", x)]
            e["numbers_not_in_text"] = missing
            if missing:
                bad_num += 1
            links = [l for i in ids for l in units[i]["links"]]
            e["links"] = [{"url": l["url"], "label": l["label"], "type": l.get("type", "?"),
                           "status": status.get(l["url"], "нет в проверке")} for l in links]
            sites = {urlparse(l["url"]).netloc.replace("www.", "") for l in links}
            e["sites"] = sorted(sites)
            e["first_party"] = sum(1 for l in links if l.get("type") in ("П", "Н"))
            all_entries.append(e)
        uncovered = sorted(packet_ids - used - skipped)
        skipped_with_links = sorted(i for i in (skipped & packet_ids) - used if units[i]["links"])
        # компания считается потерянной, если ни один её абзац не вошёл ни в одну запись
        miss_comp = sorted(c for c, ids in index[packet]["companies"].items() if not (set(ids) & used))
        problems += bad_fmt + bad_num + bad_ids + len(uncovered) + len(skipped_with_links)
        report[packet] = {"uncovered": uncovered, "skipped_with_links": skipped_with_links,
                          "missing_companies": miss_comp,
                          "bad_numbers": [(e["who"], e["numbers_not_in_text"]) for e in entries if e["numbers_not_in_text"]],
                          "bad_ids": [(e["who"], [i for i in e["ids"] if i not in packet_ids]) for e in entries
                                      if any(i not in packet_ids for i in e["ids"])]}
        print(f"{packet:6s} записей={len(entries):3d} формат_плохой={bad_fmt} чужие_номера={bad_ids} "
              f"числа_не_из_текста={bad_num} непокрыто={len(uncovered)} "
              f"пропущено_со_ссылками={len(skipped_with_links)} компаний_потеряно={len(miss_comp)}")
    json.dump(all_entries, open(os.path.join(WORK, "variants.json"), "w", encoding="utf-8"),
              ensure_ascii=False, indent=1)
    json.dump(report, open(os.path.join(WORK, "variants_check.json"), "w", encoding="utf-8"),
              ensure_ascii=False, indent=1)
    print(f"всего записей: {len(all_entries)}; замечаний: {problems}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
