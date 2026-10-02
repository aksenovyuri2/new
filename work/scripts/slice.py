"""Шаг 2.1. Нарезка трёх отчётов исследования на пакеты по вопросам кейса.

Каждый абзац и каждая строка таблицы получают номер. Из меток ссылок
вида [Компания, 06.2026 · П ⚠](url) извлекаются компания, дата, тип источника.
Выход: units.json (все единицы текста), packets/*.md (пакеты для отбора),
packets/index.json (состав пакетов и список компаний в каждом).
"""
import json
import os
import re
import sys

SRC = ("/Users/urij/Library/Application Support/Claude/scratch-workspaces/"
       "04a091d9-9c6b-4cc2-a36e-0d43efe33d60/dcf82310-8165-479f-960f-ddcfa85873bf/"
       "scratch-2026-10-01-ab7d6b/reports/")
OUT = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..")
REPORTS = {
    "R1": "Практики CRM в крупных компаниях.md",
    "R2": "Доказательная база для CRM кейса.md",
    "R3": "Усиление базы CRM кейса.md",
}
R1_THEMES = [
    ("Один шлюз решает", "b1"),
    ("Прирост к holdout", "b2"),
    ("Платформа владеет правилами", "b3"),
    ("Запуск начинается", "b4"),
    ("Что делать первым", "b4"),
]
Q_RE = re.compile(r"^#{2,3}\s+([1-4]\.[1-4])\s")
LINK_RE = re.compile(r"\[([^\]\[]+?)\]\((https?://[^)\s]+)\)")
BOLD_LEAD_RE = re.compile(r"^\*\*([^*]{2,60}?)\.?\*\*")


def bucket_for(report, heading_stack, line):
    """Определить пакет по текущим заголовкам."""
    for h in reversed(heading_stack):
        m = Q_RE.match(h)
        if m and report in ("R2", "R3"):
            return "q" + m.group(1)
    if report == "R1":
        for h in reversed(heading_stack):
            if h.startswith("## "):
                for key, b in R1_THEMES:
                    if key in h:
                        return "r1_" + b
                break
    return "meta"


def parse_links(text):
    links = []
    for label, url in LINK_RE.findall(text):
        label = label.strip()
        item = {"label": label, "url": url}
        if "·" in label:
            parts = [x.strip() for x in label.split("·")]
            left = parts[0]
            t = next((x[0] for x in parts[1:] if x[:1] in "ПВТНФ"), None)
            d = re.search(r"(?:\d{2}\.)?\d{4}", left)
            who = left.split(",")[0].strip()
            if t and who:
                item.update(who=who, date=d.group(0) if d else "без даты", type=t,
                            warn="⚠" in label, background="фон" in label)
        links.append(item)
    return links


def parse_report(code, path):
    units, stack = [], []
    lines = open(path, encoding="utf-8").read().split("\n")
    n = 0
    buf, table_header = [], None

    def flush_par():
        nonlocal buf, n
        text = "\n".join(buf).strip()
        buf = []
        if not text:
            return
        n += 1
        units.append({"id": f"{code}-{n:04d}", "report": code, "kind": "par",
                      "bucket": bucket_for(code, stack, text),
                      "heading": stack[-1] if stack else "", "text": text,
                      "links": parse_links(text)})

    for line in lines:
        if line.startswith("#"):
            flush_par()
            table_header = None
            level = len(line) - len(line.lstrip("#"))
            stack = [h for h in stack if (len(h) - len(h.lstrip("#"))) < level]
            stack.append(line.strip())
            continue
        if line.lstrip().startswith("|"):
            flush_par()
            if table_header is None:
                table_header = line.strip()
                continue
            if re.match(r"^\s*\|[\s:\-|]+\|\s*$", line):
                continue
            n += 1
            units.append({"id": f"{code}-{n:04d}", "report": code, "kind": "row",
                          "bucket": bucket_for(code, stack, line),
                          "heading": stack[-1] if stack else "",
                          "table_header": table_header, "text": line.strip(),
                          "links": parse_links(line)})
            continue
        table_header = None
        if not line.strip():
            flush_par()
        else:
            buf.append(line)
    flush_par()
    return units


def companies_of(unit):
    names = set()
    for l in unit["links"]:
        if "who" in l:
            names.add(l["who"])
    m = BOLD_LEAD_RE.match(unit["text"])
    if m and unit["report"] == "R1":
        names.add(m.group(1).strip())
    return names


def main():
    all_units = []
    for code, fname in REPORTS.items():
        all_units += parse_report(code, SRC + fname)
    # библиотеки ссылок и служебные разделы в пакеты не идут
    for u in all_units:
        h = u["heading"]
        if "Библиотека ссылок" in h or re.match(r"^#+\s+Библиотека", h):
            u["bucket"] = "library"
    os.makedirs(os.path.join(OUT, "packets"), exist_ok=True)
    json.dump(all_units, open(os.path.join(OUT, "units.json"), "w", encoding="utf-8"),
              ensure_ascii=False, indent=0)
    buckets = {}
    for u in all_units:
        buckets.setdefault(u["bucket"], []).append(u)
    index = {}
    for b, us in sorted(buckets.items()):
        if b in ("library",):
            continue
        out, last_heading, last_table = [], None, None
        comps = {}
        for u in us:
            if u["heading"] != last_heading:
                out.append("\n" + u["heading"] + "\n")
                last_heading, last_table = u["heading"], None
            if u["kind"] == "row":
                if u["table_header"] != last_table:
                    out.append("Таблица, столбцы: " + u["table_header"])
                    last_table = u["table_header"]
            else:
                last_table = None
            out.append(f"[{u['id']}] {u['text']}\n")
            for c in companies_of(u):
                comps.setdefault(c, []).append(u["id"])
        body = "\n".join(out)
        open(os.path.join(OUT, "packets", b + ".md"), "w", encoding="utf-8").write(body)
        index[b] = {"units": len(us), "bytes": len(body.encode("utf-8")),
                    "chars": len(body), "with_links": sum(1 for u in us if u["links"]),
                    "companies": {k: v for k, v in sorted(comps.items())}}
    json.dump(index, open(os.path.join(OUT, "packets", "index.json"), "w", encoding="utf-8"),
              ensure_ascii=False, indent=1)
    # сверка: ничего не потеряно
    total_src = sum(len(open(SRC + f, encoding="utf-8").read()) for f in REPORTS.values())
    total_units = sum(len(u["text"]) for u in all_units)
    print(f"единиц текста: {len(all_units)}; знаков в отчётах: {total_src}; знаков в единицах: {total_units}")
    for b, info in index.items():
        print(f"{b:8s} единиц={info['units']:4d} со ссылками={info['with_links']:4d} "
              f"знаков={info['chars']:7d} компаний={len(info['companies'])}")
    lib = len(buckets.get("library", []))
    print("строк библиотек (не в пакетах):", lib)
    unparsed = [l["label"] for u in all_units if u["bucket"] != "library" for l in u["links"] if "who" not in l]
    print("ссылок без распознанной метки:", len(unparsed), "| примеры:", unparsed[:8])


if __name__ == "__main__":
    sys.exit(main())
