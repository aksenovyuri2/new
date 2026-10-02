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
CORE = {"1.1": "s-b1", "1.2": "s-b2", "1.3": "s-b4", "1.4": "s-b5", "2.1": "s-v1", "2.2": "s-v2", "2.3": "s-v3",
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
        if sid != "s-e1" and ('class="answer"' not in body or 'class="basis"' not in body):
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
    nums = {r["code"]: r["value"] for r in json.load(open(os.path.join(WORK, "numbers.json"), encoding="utf-8"))}
    for name, weight in (("mortgage", "w_mortgage"), ("newbuild", "w_dev_call"), ("promo", "w_promo")):
        u = nums["u_active_promo"] if name == "promo" else nums["u_active_hint"]
        raw = 1000 * nums[f"ex_{name}_p"] * u * nums[weight] * nums[f"ex_{name}_fit"]
        score = raw - (nums["ex_contacts_7d"] - nums["fatigue_free"]) * nums["fatigue_step"] - 1000 * nums["push_optout"] * nums["channel_cost"]
        if abs(raw - nums[f"ex_{name}_raw"]) > 1e-9 or abs(score - nums[f"ex_{name}_push"]) > 1e-9:
            problems.append(f"пример Б5, {name}: пересчёт не сошёлся")
    order = ["s-e1", "s-a1", "s-a2", "s-a3", "s-a4", "s-b1", "s-b2", "s-b3", "s-b4", "s-b5", "s-v1", "s-v2", "s-v3", "s-g1", "s-g2", "s-d1", "s-d2", "s-d3"]
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
