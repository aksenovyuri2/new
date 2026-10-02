"""Сверка выжимок доказательств (work/brief/E*.md) с исследованием.

Для каждой строки со ссылкой на абзац (R1-0001 и т.п.) проверяет:
- абзац существует в units.json;
- значимые числа строки (с дробью, из трёх и более цифр или с %) есть в тексте этого абзаца.
Печатает сводку по файлам и строки с расхождениями.
"""
import glob, json, os, re, sys
WORK = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..")
units = {u["id"]: u["text"] for u in json.load(open(os.path.join(WORK, "units.json"), encoding="utf-8"))}
ID = re.compile(r"R[123]-\d{4}")
NUM = re.compile(r"(?<![\w.,])(\d+[.,]\d+|\d{3,}|\d+\s?%)")

def norm(s):
    return s.replace(" ", " ").replace(" ", "").replace(",", ".")

def main():
    bad_total = 0
    for path in sorted(glob.glob(os.path.join(WORK, "brief", "E*.md"))):
        lines = open(path, encoding="utf-8").read().splitlines()
        ids_all, missing, mism, comp = set(), [], [], set()
        for ln in lines:
            ids = ID.findall(ln)
            if not ids:
                continue
            ids_all.update(ids)
            for i in ids:
                if i not in units:
                    missing.append(i)
            texts = norm(" ".join(units.get(i, "") for i in ids))
            for n in NUM.findall(ID.sub(" ", ln)):
                if norm(n).rstrip("%") not in texts:
                    mism.append((n, ln[:140]))
            m = re.search(r"·\s*([^·]{2,40}?)\s*·\s*(дата\s*)?\d{2}\.\d{4}", ln)
            if m:
                comp.add(m.group(1).strip())
        bad_total += len(missing)
        print(f"{os.path.basename(path)}: абзацев {len(ids_all)}, нет в базе {len(missing)}, чисел без опоры {len(mism)}, компаний ~{len(comp)}")
        for i in missing[:10]:
            print("   нет абзаца", i)
        for n, ln in mism[:25]:
            print(f"   число {n}: {ln}")
    return 1 if bad_total else 0

if __name__ == "__main__":
    sys.exit(main())
