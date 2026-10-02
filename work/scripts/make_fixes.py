"""Собрать для каждого пакета список правок по итогам проверки отбора."""
import json
import os
import sys

WORK = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..")


def main() -> int:
    rep = json.load(open(os.path.join(WORK, "variants_check.json"), encoding="utf-8"))
    index = json.load(open(os.path.join(WORK, "packets", "index.json"), encoding="utf-8"))
    only = set(sys.argv[1:])
    for packet, r in rep.items():
        if only and packet not in only:
            continue
        lines = [f"# Правки к файлу variants/{packet}.md", "",
                 "Проверка скриптом нашла пропуски. Исправь файл результата на месте: допиши недостающие записи "
                 "перед разделом «## Пропущено», исправь ошибочные. Готовые верные записи не трогай.", ""]
        n = 0
        if r["uncovered"]:
            n += len(r["uncovered"])
            lines += ["## Абзацы, которых нет ни в записях, ни в «Пропущено»",
                      "Перечитай каждый в пакете. Если в нём есть содержание, сделай запись. Если нет — добавь в «Пропущено» с причиной.",
                      ", ".join(r["uncovered"]), ""]
        if r["skipped_with_links"]:
            n += len(r["skipped_with_links"])
            lines += ["## Абзацы со ссылками, отправленные в «Пропущено»",
                      "В них названы источники. Перечитай: если там есть факт о компании или источнике, сделай запись и убери номер из «Пропущено».",
                      ", ".join(r["skipped_with_links"]), ""]
        if r["missing_companies"]:
            n += len(r["missing_companies"])
            lines += ["## Компании и источники, ни один абзац которых не вошёл в записи",
                      "Для каждой сделай запись по указанным абзацам."]
            lines += [f"- {c}: {', '.join(index[packet]['companies'][c])}" for c in r["missing_companies"]]
            lines.append("")
        if r["bad_numbers"]:
            n += len(r["bad_numbers"])
            lines += ["## Числа, которых нет в указанных абзацах",
                      "Проверь по тексту: исправь число, поправь номера абзацев или убери число."]
            lines += [f"- запись «{w}»: {', '.join(x)}" for w, x in r["bad_numbers"]]
            lines.append("")
        if r["bad_ids"]:
            n += len(r["bad_ids"])
            lines += ["## Номера абзацев не из этого пакета", "В поле «абзацы» должны быть только номера из пакета " + packet + "."]
            lines += [f"- запись «{w}»: {', '.join(x)}" for w, x in r["bad_ids"]]
            lines.append("")
        path = os.path.join(WORK, "variants", f"_правки_{packet}.md")
        if n:
            open(path, "w", encoding="utf-8").write("\n".join(lines))
        elif os.path.exists(path):
            os.remove(path)
        print(packet, "правок:", n)
    return 0


if __name__ == "__main__":
    sys.exit(main())
