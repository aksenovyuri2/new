"""Сжатый вид записей отбора для чтения: одна строка на запись, с опорой и силой источника."""
import json
import os
import sys

WORK = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..")
VENDOR_HOSTS = ("pega.com", "braze.com", "mindbox", "airship.com", "clevertap", "moengage", "insider", "adobe.com")


def strength(e: dict) -> str:
    types = sorted({l["type"] for l in e["links"]})
    sites = e["sites"]
    first = [l for l in e["links"] if l["type"] in ("П", "Н")]
    first_sites = {s for s in sites if not any(v in s for v in VENDOR_HOSTS)}
    if not e["links"]:
        return "без ссылки"
    tag = "/".join(types)
    if first and len(first_sites) >= 2:
        return f"{tag}; сайтов {len(sites)}"
    return f"{tag}; сайтов {len(sites)}"


def main() -> int:
    entries = json.load(open(os.path.join(WORK, "variants.json"), encoding="utf-8"))
    src = {}
    p = os.path.join(WORK, "sources_check.json")
    if os.path.exists(p):
        src = {(r["packet"], r["n"]): r["verdict"] for r in json.load(open(p, encoding="utf-8"))}
    by = {}
    for e in entries:
        by.setdefault(e["packet"], []).append(e)
    out_dir = os.path.join(WORK, "compact")
    os.makedirs(out_dir, exist_ok=True)
    total = 0
    for packet, es in by.items():
        lines = [f"# {packet}: {len(es)} записей", ""]
        for e in es:
            flag = " ⚠ЧИСЛА_НЕ_ИЗ_ТЕКСТА" if e["numbers_not_in_text"] else ""
            v = src.get((packet, e["n"]))
            vs = f" · сверка: {v}" if v and v not in ("значимых чисел нет",) else ""
            nums = "" if e["numbers"].lower().startswith("нет") else f" ‖ {e['numbers']}"
            lines.append(f"{e['n']}. **{e['who']}** [{e['kind']}] {e['gist']}{nums} ({', '.join(e['ids'])}; {strength(e)}{vs}){flag}")
        text = "\n".join(lines)
        total += len(text)
        open(os.path.join(out_dir, packet + ".md"), "w", encoding="utf-8").write(text)
    print("знаков всего:", total)
    return 0


if __name__ == "__main__":
    sys.exit(main())
