"""Вкладка «Варианты рынка»: все записи отбора по вопросам кейса, со ссылками и статусом сверки."""
import html
import json
import os
import sys

WORK = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..")
QUESTIONS = [
    ("1.1", "По каким признакам и сигналам сегментировать", ["q1.1"]),
    ("1.2", "Как выбирать человека, сообщение, канал и момент", ["q1.2"]),
    ("1.3", "Как разрешать конкуренцию вертикалей и маркетинга", ["q1.3"]),
    ("1.4", "Как учитывать эффект, уместность, усталость и риск", ["q1.4"]),
    ("Блок 1", "Примеры компаний из первого отчёта", ["r1_b1"]),
    ("2.1", "Ключевые метрики", ["q2.1"]),
    ("2.2", "Как измерять добавленный эффект", ["q2.2"]),
    ("2.3", "Защитные метрики", ["q2.3"]),
    ("2.4", "Контрольные группы", ["q2.4"]),
    ("Блок 2", "Примеры компаний из первого отчёта", ["r1_b2"]),
    ("3.1", "Что централизовать", ["q3.1"]),
    ("3.2", "Кто за что отвечает", ["q3.2"]),
    ("3.3", "Приоритизация и конфликты", ["q3.3"]),
    ("Блок 3", "Примеры компаний из первого отчёта", ["r1_b3"]),
    ("4.1", "Что входит в MVP", ["q4.1"]),
    ("4.2", "Результаты через 3 и 6 месяцев", ["q4.2"]),
    ("4.3", "Зависимости и риски", ["q4.3"]),
    ("Блок 4", "Примеры компаний из первого отчёта", ["r1_b4"]),
]
TYPE = {"П": "сама компания", "В": "вендор", "Т": "пересказ", "Н": "наука", "Ф": "фреймворк", "?": "тип не указан"}
VERDICT = {
    "все числа найдены на страницах": "числа найдены в источнике",
    "часть чисел найдена": "часть чисел найдена",
    "числа на страницах не найдены": "числа скриптом не найдены",
    "страницы не открылись скрипту": "источник скрипту не открылся",
    "нет ссылки в абзацах": "ссылка в соседнем абзаце",
    "значимых чисел нет": "",
}


def main() -> int:
    entries = json.load(open(os.path.join(WORK, "variants.json"), encoding="utf-8"))
    checks = {(r["packet"], r["n"]): r["verdict"] for r in json.load(open(os.path.join(WORK, "sources_check.json"), encoding="utf-8"))}
    e = html.escape
    out = ["<!-- tab: market -->",
           '<p class="intro">Все варианты из исследования, разобранные по вопросам кейса: что делает каждая компания, вендор, закон или научная работа. '
           f'Всего {len(entries)} записей. Отбор делала простая модель, скрипт проверил, что ни один абзац трёх отчётов не потерян и что числа в записях есть в тексте отчёта. '
           'Затем скрипт открыл источники и поискал числа на страницах: результат в последнем столбце. «Синтез отчёта» — выводы авторов исследования, а не практика компании.</p>']
    for code, title, packets in QUESTIONS:
        es = [x for x in entries if x["packet"] in packets]
        rows = []
        for x in es:
            seen, links = set(), []
            for l in x["links"]:
                if l["url"] in seen:
                    continue
                seen.add(l["url"])
                links.append(f'<a href="{e(l["url"])}" rel="noopener" title="{e(TYPE.get(l["type"], l["type"]))}">{e(l["label"][:40])}</a>')
            nums = "" if x["numbers"].lower().startswith("нет") else e(x["numbers"])
            warn = " · числа записи не совпали с текстом отчёта" if x["numbers_not_in_text"] else ""
            rows.append(f"<tr><td><b>{e(x['who'])}</b><br><span class=\"kind\">{e(x['kind'])}</span></td><td>{e(x['gist'])}</td>"
                        f"<td>{nums}</td><td>{' · '.join(links[:6])}</td><td>{e(VERDICT.get(checks.get((x['packet'], x['n']), ''), ''))}{warn}</td></tr>")
        out.append(f'<details class="mk"><summary><span class="q">{e(code)}</span> {e(title)} <span class="n">{len(es)}</span></summary>'
                   '<div class="tablewrap"><table><thead><tr><th>Кто</th><th>Что делает</th><th>Числа</th><th>Источники</th><th>Сверка</th></tr></thead><tbody>'
                   + "\n".join(rows) + "</tbody></table></div></details>")
    open(os.path.join(WORK, "page", "sections", "90_market.html"), "w", encoding="utf-8").write("\n".join(out))
    print("записей:", len(entries))
    return 0


if __name__ == "__main__":
    sys.exit(main())
