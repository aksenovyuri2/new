# Стиль ЦИАН (cian.ru)

К = точно из кода CSS; В = вывод. cian.ru закрыт (403/captcha); CSS с CDN через Exa. Снимки: 2025-05 (S2,S3), 2026-03 (S1,S4,S5). CSS после ребрендинга (июнь 2026) не найден.
Базовый URL B = https://static.cdn-cian.ru/frontend/
S1 B+header-frontend/v2-get-header-microfrontend.919060e5dc508f42.css
S2 B+frontend-mainpage/main.895e4534ecca8545950c.css
S3 B+recommendations-micro-frontend/v1-get-recommendations-micro-frontend.6d4e3c9c5bfea56493c9.css
S4 B+desktop-filters-micro-frontend/v1-get-desktop-filters-microfrontend.583b78b34ddcb321.css
S5 B+mortgage-promo-frontend/chunk.0d98c092d6b54a27.css
S6 trace-logos.ru/logos/developers/cian/

## Цвета (светлая тема)
- Синий основной (кнопки, бренд): #0468FF (S2,S6) К; токен 2026 blue500 #006CFD (S1) К. Нажатие #075AD9; ссылка #0661EC.
- Текст: #152242 (S2) / #0D162E (S1) К. Вторичный: #707A95 (S2) / #697797 (S1) К.
- Фон: #FFFFFF; серый #F3F6FF (S2) / #F3F5FA (S1); светло-синий #E6F0FF К.
- Границы: #C9D1E5 (S2) / #D0D8E9 (S1); тонкая #E8E9EC К.
- Зелёный #34AC0A (фон #EBF9E6), оранж #DB6F0A (#FFF2E6), красный #DB1F36 (#FFE9EB) — S1,S2 К. Текст 2026: #227E01, #A14F00, #C2122D К.
- Декор (S1) К: жёлтый #FFF500, фиолет #8729FF, розовый #FFE1FF, персик #FFDCC8, песок #FFEBAF.
- Ребрендинг 2026-06: к синему добавлены жёлтый и оранжевый, hex не найдены (companies.rbc.ru, РБК).

## Шрифт
- Lato: `Lato, Arial, sans-serif`; lato-regular/bold/black.woff2 в B+fonts/h/ (S4) К.
- Заголовки и кнопки 700. Hero 36/40 (моб. 28/36, трекинг -0.5px), H2 22/28, H3 18/24, H4 16/22 (S5) К. Текст 14/20, 16/24, подпись 12/16 (S3) К.

## Компоненты
- Кнопка: XS h28 r4; M h44 r8; L h56 r8; Lato 700, 14–16px (S3) К. Primary #0468FF/белый; secondary #E6F0FF/#0661EC; outline 1px #C9D1E5.
- Поле: r8, рамка 1px #C9D1E5, 16/22 (S4) К; h44 В.
- Бейдж: h24, pad 4×8, r4, 12/16 (S3) К. Чип-тег фильтра: #E6F0FF, pad 4×12, r99 (пилюля); чип-кнопка r8, pad 10×16; выбран: рамка #3686FF, фон #F3F6FF (S2,S4) К.
- Карточка (рекомендации): белая, 1px #C9D1E5, r12, фото r12 сверху, 320:280 (S3) К. Промо-карточка r16, тень 0 4px 16px rgba(0,0,0,.1), моб. r8 (S5) К. Плашки r16 #E6F0FF / r8 #F3F6FF (S3) К.
- Тени: выпадашка 0 10px 20px rgba(0,0,0,.1), r4; поповер 0 8px 16px rgba(0,0,0,.08) (S2) К.
- Плотность: компактная, сетка 4px В, текст 14px, контейнер до 1100px (S5).
- Не найдено: полный CSS карточки объявления в выдаче.
