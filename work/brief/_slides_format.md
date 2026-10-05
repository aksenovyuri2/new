# Формат слайда (тип Slides) — выжимка

Один файл = одна `<section id="ID" …>` без `<html>`, `<head>`, `<style>`. Холст 1920×1080, все стили встроенные. Заметки — одна `<aside>`, последним ребёнком, простой текст до 4000 знаков.

## Элементы
- Текст: `h1 h2 h3 p ul ol li br`; инлайн `b i u a span(style="color:…")`. У span нельзя задавать размер и шрифт.
- Контейнеры: `div` — flex row, flex column или grid; вложенность до 15. Div невидим, пока у него нет background, border или box-shadow.
- `img src alt style="width;height;object-fit:cover|contain"`. src — только `/_blob/<id>` загруженного файла.
- `table` из `tr`, `th` (первая строка), `td`. Без colspan и rowspan. Фон — только на `tr`. Ширины колонок — `width:N%` на каждой ячейке первой строки. Строка ≈ 2,1 × размер шрифта на строку текста.
- `hr`.
- `x-shape kind="rect|rounded|ellipse|diamond|arrow-right|arrow-left|arrow-up|arrow-down|line"` — фигура без содержимого. Стрелку держи около 2:1.
- `x-connector x1 y1 x2 y2 head="end|both|none" route="straight|hv|vh|elbow"` — по координатам холста или относительно `position:relative` div.
- `x-icon name` — одно из: Activity Book Chart Chat Check CheckCircle Clock Cloud Code Database Globe GraduationCap Home Key Lightbulb Lightning Link Lock PaperPlane Play Search Settings Star ThumbsUp Tool Trust Users Verified Warning Wrench.
- `svg aria-label` — только графика. Текст в svg не грузит шрифты: подписи делай через p поверх или рядом.
- Не больше 200 элементов на слайд.

## Разрешённый CSS (остальное запрещено)
- **Положение:** `position:absolute|relative`; `left top right bottom` в px или % — только у absolute.
- **Размеры:** `width height` — px, auto или %. % — только у absolute, td/th и детей flex. `min-width` — px, min-content или max-content; `min-height max-width max-height` — px.
- **Flex и grid:**
  - `display:flex|grid|none` — только у section и div;
  - `flex-direction`, `flex-wrap`, `gap` (одно значение, px), `align-items`;
  - `justify-content`: start, center, end, space-between, space-around, space-evenly;
  - `flex: N` или `flex:1`, `flex-grow`, `flex-shrink`, `flex-basis`, `align-self`;
  - `grid-template-columns` и `grid-template-rows`: px, fr, auto, repeat; без minmax и auto-fill;
  - `grid-column: span N`.
- **Отступы:** `padding` — px, 1–4 значения. **margin нельзя.**
- **Шрифт:**
  - `font-family` (Carlito, Arial, sans-serif), `font-size` в px, не меньше 24;
  - `font-weight` 100–900;
  - `line-height` (число), `letter-spacing`, `text-align`, `text-transform`;
  - `white-space:nowrap|normal`, `font-variant-numeric:tabular-nums`.
- **Цвет и фон:**
  - `color`;
  - `background` — цвет или linear-gradient;
  - `border` — «Npx solid|dashed|dotted #hex», обязательно со словом стиля; `border-top/-right/-bottom/-left`; `border-radius`; `box-shadow`;
  - `opacity`;
  - `overflow:hidden|visible` — только у div.
- **transform:** translate, rotate, scale.

## Ширина текста
Текст переносится только по пробелам. Слово шире блока ломается посреди слова. Для Carlito закладывай около 0,5 × размер шрифта на знак, для жирного — около 0,55. Пример: колонка 592 px с отступами 48 при 24px вмещает около 45 знаков в строке.

## Высота
Заголовок ≈ размер × строки × 1,12. Абзац 24px при line-height 1.4 ≈ 34 px на строку. Карточка = отступы + сумма строк + gap; фиксированную высоту меньше содержимого не ставь.
