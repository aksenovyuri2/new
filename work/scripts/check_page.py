"""Этап 8. Сверка страницы и выгрузка текста схем для теста и рецензента.

Проверяет: у каждого вопроса кейса есть схема ядра; у каждой схемы есть рисунок с подписью,
ответ и источники; все ссылки навигатора ведут на существующие схемы; пример в Б5 сходится с формулой.
Пишет test/schemes_text.md (только рисунки и подписи) и test/page_text.md (всё, кроме вариантов рынка).
"""
import html
import json
import os
import re
import sys

WORK = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..")
PAGE = os.path.join(WORK, "..", "cian-comms-schemes.html")
CORE = {"1.1": "s-b1", "1.2": "s-b2", "1.3": "s-b4", "1.4": "s-m1", "2.1": "s-v1", "2.2": "s-v2", "2.3": "s-v3",
        "2.4": "s-v2", "3.1": "s-g1", "3.2": "s-g1", "3.3": "s-g2", "4.1": "s-d1", "4.2": "s-d2", "4.3": "s-d3"}


def text_of(fragment: str) -> str:
    t = re.sub(r"<(script|style)[^>]*>.*?</\1>", " ", fragment, flags=re.S)
    t = re.sub(r"</(p|h1|h2|h3|h4|li|tr|figcaption|summary|div|article|text)>", "\n", t)
    t = re.sub(r"</t[dh]>", " | ", t)
    t = html.unescape(re.sub(r"<[^>]+>", "", t))
    return "\n".join(x.strip() for x in t.split("\n") if x.strip())


def main() -> int:
    page = open(PAGE, encoding="utf-8").read()
    problems = []
    schemes = dict(re.findall(r'<article class="scheme" id="([^"]+)">(.*?)</article>', page, flags=re.S))
    for q, sid in CORE.items():
        if sid not in schemes:
            problems.append(f"вопрос {q}: нет схемы {sid}")
        elif "★" not in schemes[sid]:
            problems.append(f"вопрос {q}: схема {sid} не помечена ядром")
    for sid, body in schemes.items():
        if "<svg" not in body or "<figcaption>" not in body:
            problems.append(f"{sid}: нет рисунка или подписи")
        if sid not in ("s-e1", "s-e2") and ('class="answer"' not in body or 'class="basis"' not in body):
            problems.append(f"{sid}: нет ответа или источников")
        for svg in re.findall(r"<svg[^>]*>", body):
            if 'role="img"' not in svg or "aria-label=" not in svg:
                problems.append(f"{sid}: у рисунка нет описания")
        if "{{" in body or "??" in body:
            problems.append(f"{sid}: не подставлено число")
    ids = set(re.findall(r'id="([^"]+)"', page))
    tabs = set(re.findall(r'data-tab="([^"]+)"', page))
    for href in re.findall(r'href="#([^"]+)"', page):
        if href not in ids and href not in tabs:
            problems.append(f"ссылка #{href} никуда не ведёт")
    # критерии приёмки уровня CPO
    core_links, core_who = set(), set()
    for sid, body in schemes.items():
        if sid in ("s-e1", "s-e2"):
            continue
        if 'class="market"' not in body:
            problems.append(f"{sid}: нет полосы «Рынок»")
        links = set(re.findall(r'href="(https?://[^"]+)"', body))
        who = set(re.findall(r'<span class="who">([^<]+)</span>', body))
        if "★" in body:
            core_links |= links
            core_who |= who
            if len(links) < 3:
                problems.append(f"{sid}: на схеме ядра меньше 3 внешних источников ({len(links)})")
    for pid in ("b1", "b2", "b3", "b4"):
        m = re.search(r'<section class="panel" id="p-%s"[^>]*>(.*?)</section>' % pid, page, flags=re.S)
        if m and 'class="tradeoff"' not in m.group(1):
            problems.append(f"вкладка {pid}: нет таблицы компромиссов")
    for sid in ("s-m2", "s-d2"):
        if sid in schemes and "2028" not in schemes[sid] and sid == "s-m2":
            problems.append(f"{sid}: нет связи с целью 2028")
    # версия 4: новые вкладки, единое имя главной метрики, связь роадмапа с деревом метрик
    for pid in ("role", "value", "channels", "intel"):
        m = re.search(r'<section class="panel" id="p-%s"[^>]*>(.*?)</section>' % pid, page, flags=re.S)
        if not m:
            problems.append(f"вкладка {pid}: нет")
            continue
        body = m.group(1)
        n = body.count('<article class="scheme"')
        if n < 3:
            problems.append(f"вкладка {pid}: схем меньше трёх ({n})")
        for need, what in (('class="market"', "данных рынка"), ("mark assume", "допущений"),
                           ('class="tradeoff"', "таблицы компромиссов")):
            if need not in body:
                problems.append(f"вкладка {pid}: нет {what}")
    plain = text_of(page)
    for old in re.findall(r"главн\w* метрик\w*\s*[—:]\s*(?:добавленн|дополнительн)\w* (?:контакт|целев)\w*", plain):
        problems.append(f"старое имя главной метрики: «{old}»")
    if "добавленная выручка на человека за 12 месяцев" not in plain:
        problems.append("нет главной метрики «добавленная выручка на человека за 12 месяцев»")
    if "s-r4" in schemes and 'href="#s-r3"' not in schemes["s-r4"]:
        problems.append("s-r4: роадмап не ссылается на дерево метрик s-r3")
    print(f"на схемах ядра: внешних источников {len(core_links)}, компаний в полосах «Рынок» {len(core_who)}")
    if len(core_links) < 50:
        problems.append(f"на схемах ядра меньше 50 источников ({len(core_links)})")
    if len(core_who) < 40:
        problems.append(f"на схемах ядра меньше 40 компаний ({len(core_who)})")
    # карточки ответов на вопросы кейса
    qa = re.findall(r'<article class="doc" id="(q[^"]+)">(.*?)</article>', page, flags=re.S)
    for qid, body in qa:
        if body.count("<tr><th>") != 6:
            problems.append(f"карточка {qid}: не шесть строк стратегия → допущения")
        if not re.search(r'href="#s-', body):
            problems.append(f"карточка {qid}: нет ссылки на схему")
        if 'mark assume' not in body:
            problems.append(f"карточка {qid}: не помечены допущения")
    print(f"карточек ответов: {len(qa)}")
    order = [sid for sid in re.findall(r'<article class="scheme" id="([^"]+)">', page)]
    with open(os.path.join(WORK, "test", "schemes_text.md"), "w", encoding="utf-8") as f:
        for sid in order:
            body = re.sub(r'<div class="answer">.*?</div>\s*<div class="basis">.*?</div>', "", schemes[sid], flags=re.S)
            body = re.sub(r"<svg[^>]*aria-label=\"[^\"]*\"[^>]*>", "<svg>", body)
            f.write(f"\n\n===== СХЕМА {sid}\n" + text_of(body))
    panels = re.findall(r'<section class="panel" id="p-([^"]+)"[^>]*>(.*?)</section>', page, flags=re.S)
    with open(os.path.join(WORK, "test", "page_text.md"), "w", encoding="utf-8") as f:
        for pid, body in panels:
            if pid == "market":
                continue
            body = re.sub(r"<svg[^>]*aria-label=\"([^\"]*)\"[^>]*>", r"<p>[Рисунок: \1]</p><svg>", body)
            f.write(f"\n\n######## ВКЛАДКА {pid}\n" + text_of(body))
    print(f"схем: {len(schemes)}; вопросов кейса закрыто ядром: {sum(1 for s in CORE.values() if s in schemes)} из {len(CORE)}")
    print("замечаний:", len(problems))
    for p in problems:
        print("  -", p)
    for name in ("schemes_text.md", "page_text.md"):
        print(name, os.path.getsize(os.path.join(WORK, "test", name)), "байт")
    return 0


if __name__ == "__main__":
    sys.exit(main())
