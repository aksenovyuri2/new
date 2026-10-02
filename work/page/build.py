"""Сборка страницы со схемами.

Берёт template.html и разделы из sections/*.html. Подставляет числа из числового
каркаса (numbers.json) на место {{код|формат}}. Неизвестный код — ошибка сборки.
Печатает числа, записанные в разделах цифрами в обход каркаса: их нужно проверить глазами.
"""
import glob
import json
import os
import re
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
WORK = os.path.join(HERE, "..")
OUT = os.path.join(WORK, "..", "cian-comms-schemes.html")
TABS = [
    ("position", "Позиция"),
    ("asis", "Как есть"),
    ("b1", "1. Решения"),
    ("b2", "2. Метрики"),
    ("b3", "3. Взаимодействие"),
    ("b4", "4. MVP и запуск"),
    ("nav", "Навигатор"),
    ("assume", "Допущения"),
    ("market", "Варианты рынка"),
]
PH_RE = re.compile(r"\{\{\s*([a-z0-9_%]+)\s*(?:\|\s*([^}\s]+)\s*)?\}\}")


def trim(x: float, digits: int) -> str:
    s = f"{x:.{digits}f}"
    if "." in s:
        s = s.rstrip("0").rstrip(".")
    return s.replace(".", ",").replace("-", "−")


def fmt(value: float, spec: str | None) -> str:
    spec = spec or "num"
    if spec.startswith("%"):
        return trim(value * 100, int(spec[1:] or 2)) + "%"
    if spec.startswith("млн"):
        return trim(value / 1e6, int(spec[3:] or 2))
    if spec.startswith("тыс"):
        return trim(value / 1e3, int(spec[3:] or 0))
    if spec.startswith("num"):
        return trim(value, int(spec[3:] or 2))
    raise ValueError("неизвестный формат " + spec)


def main() -> int:
    numbers = {r["code"]: r["value"] for r in json.load(open(os.path.join(WORK, "numbers.json"), encoding="utf-8"))}
    used, errors, literal = set(), [], []
    panels = {tid: [] for tid, _ in TABS}
    for path in sorted(glob.glob(os.path.join(HERE, "sections", "*.html"))):
        src = open(path, encoding="utf-8").read()
        m = re.match(r"\s*<!--\s*tab:\s*(\w+)\s*-->", src)
        if not m or m.group(1) not in panels:
            errors.append(f"{os.path.basename(path)}: нет строки <!-- tab: ... --> или вкладка неизвестна")
            continue
        body = src[m.end():]
        plain = re.sub(r"<[^>]+>", " ", PH_RE.sub(" ", re.sub(r"<!--.*?-->", "", body, flags=re.S)))
        nums = sorted(set(re.findall(r"(?<![\w.,])\d+(?:[.,]\d+)?\s?(?:%|млн|тыс)?", plain)))
        literal.append((os.path.basename(path), [n.strip() for n in nums]))

        def sub(mm: re.Match) -> str:
            code, spec = mm.group(1), mm.group(2)
            if code not in numbers:
                errors.append(f"{os.path.basename(path)}: нет кода {code} в числовом каркасе")
                return "??"
            used.add(code)
            return fmt(numbers[code], spec)

        panels[m.group(1)].append(PH_RE.sub(sub, body))
    tabs_html, panels_html = [], []
    for tid, title in TABS:
        if not panels[tid]:
            continue
        n = sum(x.count('class="scheme"') for x in panels[tid])
        badge = f'<span class="n">{n}</span>' if n else ""
        tabs_html.append(f'<button type="button" role="tab" data-tab="{tid}" aria-selected="false">{title}{badge}</button>')
        panels_html.append(f'<section class="panel" id="p-{tid}" role="tabpanel" aria-label="{title}">\n' + "\n".join(panels[tid]) + "\n</section>")
    page = open(os.path.join(HERE, "template.html"), encoding="utf-8").read()
    page = page.replace("<!--TABS-->", "\n".join(tabs_html)).replace("<!--PANELS-->", "\n".join(panels_html))
    open(OUT, "w", encoding="utf-8").write(page)
    # обёртка для локального просмотра: при публикации такую же добавляет сама площадка
    os.makedirs(os.path.join(HERE, "out"), exist_ok=True)
    open(os.path.join(HERE, "out", "index.html"), "w", encoding="utf-8").write(
        '<!doctype html><html lang="ru"><head><meta charset="utf-8">'
        '<meta name="viewport" content="width=device-width, initial-scale=1, viewport-fit=cover">'
        "<style>body{margin:0}img{max-width:100%}[hidden]{display:none!important}</style></head><body>" + page + "</body></html>")
    print(f"собрано: {os.path.getsize(OUT)} байт, вкладок {len(tabs_html)}, чисел из каркаса {len(used)}")
    for name, nums in literal:
        print(f"  числа цифрами в {name}: {', '.join(nums) if nums else 'нет'}")
    for e in errors:
        print("ОШИБКА:", e)
    return 1 if errors else 0


if __name__ == "__main__":
    sys.exit(main())
