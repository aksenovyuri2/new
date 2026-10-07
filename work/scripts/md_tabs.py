"""Переносит документ «Позиция и 14 решений.md» на страницу со схемами.

Части 1–2 идут на вкладку «Позиция», решения части 3 — на вкладки блоков 1–4,
части 4–5 — на вкладку «Допущения». Поддерживается только та разметка, что есть в документе:
заголовки, абзацы, списки, таблицы, блоки кода, полужирный текст и пометки источников.
"""
import html
import os
import re
import sys

WORK = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..")
SRC = os.path.join(WORK, "..", "Позиция и 14 решений.md")
OUT = os.path.join(WORK, "page", "sections")
MARKS = {"задание": ("task", "Из задания"), "ЦИАН": ("cian", "ЦИАН"), "рынок": ("market", "Рынок"),
         "допущение": ("assume", "Допущение"), "предложение": ("prop", "Предложение")}


def inline(text: str) -> str:
    t = html.escape(text, quote=False)
    for key, (cls, label) in MARKS.items():
        t = t.replace(f"**[{key}]**", f'<span class="mark {cls}">{label}</span>')
    t = re.sub(r"\*\*(.+?)\*\*", r"<b>\1</b>", t)
    return t


def render(md: str) -> str:
    out, lines, i = [], md.strip("\n").split("\n"), 0
    while i < len(lines):
        line = lines[i]
        if not line.strip() or line.strip() == "---":
            i += 1
        elif line.startswith("```"):
            j = i + 1
            while j < len(lines) and not lines[j].startswith("```"):
                j += 1
            out.append("<pre>" + html.escape("\n".join(lines[i + 1:j])) + "</pre>")
            i = j + 1
        elif line.startswith("#"):
            level = min(len(line) - len(line.lstrip("#")) + 1, 4)
            out.append(f"<h{level}>{inline(line.lstrip('#').strip())}</h{level}>")
            i += 1
        elif line.lstrip().startswith("|"):
            rows = []
            while i < len(lines) and lines[i].lstrip().startswith("|"):
                rows.append([c.strip() for c in lines[i].strip().strip("|").split("|")])
                i += 1
            head, body = rows[0], [r for r in rows[2:]]
            out.append('<div class="tablewrap"><table><thead><tr>' + "".join(f"<th>{inline(c)}</th>" for c in head)
                       + "</tr></thead><tbody>" + "".join("<tr>" + "".join(f"<td>{inline(c)}</td>" for c in r) + "</tr>" for r in body)
                       + "</tbody></table></div>")
        elif re.match(r"^\s*(-|\d+\.)\s", line):
            tag = "ol" if re.match(r"^\s*\d+\.", line) else "ul"
            items = []
            while i < len(lines) and re.match(r"^\s*(-|\d+\.)\s", lines[i]):
                items.append(re.sub(r"^\s*(-|\d+\.)\s+", "", lines[i]))
                i += 1
            out.append(f"<{tag}>" + "".join(f"<li>{inline(x)}</li>" for x in items) + f"</{tag}>")
        else:
            par = [line]
            i += 1
            while i < len(lines) and lines[i].strip() and not re.match(r"^(#|\||```|\s*(-|\d+\.)\s)", lines[i]):
                par.append(lines[i])
                i += 1
            out.append("<p>" + inline(" ".join(par)) + "</p>")
    return "\n".join(out)


def card(title: str, body_md: str, eyebrow: str = "") -> str:
    eb = f'<p class="code"><span>{html.escape(eyebrow)}</span></p>' if eyebrow else ""
    return f'<article class="doc">{eb}<h2>{inline(title)}</h2>\n{render(body_md)}\n</article>'


def write(name: str, tab: str, content: str) -> None:
    open(os.path.join(OUT, name), "w", encoding="utf-8").write(f"<!-- tab: {tab} -->\n{content}\n")


def main() -> int:
    md = open(SRC, encoding="utf-8").read()
    parts = re.split(r"^## (Часть \d\.[^\n]*)\n", md, flags=re.M)
    by = {parts[i].split(".")[0]: (parts[i], parts[i + 1]) for i in range(1, len(parts), 2)}
    # позиция: часть 2 первой, затем часть 1
    pos_sections = re.split(r"^### ", by["Часть 2"][1], flags=re.M)
    pos = ['<p class="intro">С чем мы идём к директору по продукту. Сначала позиция, ниже — что удалось узнать о самом ЦИАН. '
           "Тезис, трактовку «привлечения» и спорные решения можно править: текст меняется быстро, схемы ниже по вкладкам от формулировок почти не зависят.</p>"]
    for sec in pos_sections[1:]:
        title, _, body = sec.partition("\n")
        pos.append(card(title.strip(), body, "Позиция"))
    pos.append(card("Что мы узнали про ЦИАН", by["Часть 1"][1], "Факты из открытых источников"))
    write("10_position.html", "position", "\n".join(pos))
    # решения по блокам
    decisions = re.split(r"^### (\d\.\d)\. ", by["Часть 3"][1], flags=re.M)
    blocks = {"1": [], "2": [], "3": [], "4": []}
    for i in range(1, len(decisions), 2):
        code, text = decisions[i], decisions[i + 1]
        title, _, body = text.partition("\n")
        blocks[code[0]].append(f'<details class="dec" id="d{code.replace(".", "-")}"><summary><span class="q">{code}</span> {inline(title.strip())}</summary>\n{render(body)}\n</details>')
    for b, items in blocks.items():
        write(f"{int(b) + 2}9_decisions.html", f"b{b}",
              '<h2 class="sect">Решения по вопросам блока: полный текст</h2>\n' + "\n".join(items))
    write("80_assume.html", "assume", card("Реестр допущений", by["Часть 5"][1], "Что мы приняли без данных")
          + "\n" + card("Что остаётся неизвестным", by["Часть 4"][1], "Пробелы"))
    print("вкладки собраны: позиция, решения по блокам 1–4, допущения")
    return 0


if __name__ == "__main__":
    sys.exit(main())
