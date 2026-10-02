# Сигналы сегментации CRM-коммуникаций и количественные гардрейлы (усталость, opt-out, жёсткие внешние пороги)

Дата сбора: 2026-10-01. Бюджет: 32 вызова инструментов. Официальные документы читались «как есть на 2026-10-01».

Условные обозначения статуса источника:
- ОТКРЫТ = страницу или PDF я открыл целиком (WebFetch или Read), цифры взяты из текста.
- ВЫДАЧА = страницу видел только в результатах поиска (заголовок и URL совпадают, цифры из сниппета). Использовать с оговоркой.

Теги вопросов кейса. Нумерацию вопросов кейса (1.1, 1.4, 2.3) мне не передали, поэтому ставлю тематические теги: [СИГН] сигналы сегментации; [УСТ] усталость и частота; [БЕНЧ] бенчмарки opt-in / отписки / жалоб; [ПОРОГ] жёсткие внешние пороги; [ГАРД] наборы гардрейл-метрик. Сопоставить с номерами кейса — на стороне автора отчёта.

Покрытие и честная оговорка. Из известных списков (known_urls.txt) я ничего не пересобирал. По сигналам сегментации у крупных компаний новых публикаций 2023–2026 я нашёл мало (LinkedIn, YouTube, Airship, OneSignal); основная масса уже в known_urls (Pinterest, Grab, Uber, Swiggy, Netflix и др.). Эти ссылки я здесь только упоминаю как указатели, их содержимое мной не проверялось.

---

## 1. Какие сигналы используют для сегментации CRM-коммуникаций и кто их публикует

### Takeaway
Новые публичные доказательства 2025–2026 сводятся к трём семействам сигналов: состояние пользователя (давность визита, история отправок за последние часы), реакция на сами уведомления (игнор при получении, отключение) и поведенческие триггеры/согласие по каналу. Сегментация и автоматизация дают измеримый прирост: в данных Airship приложения с сегментацией и автоматизацией имеют Engagement Score в среднем на 31% выше среднего по категории, а события-триггеры дают CTR в 4–9 раз выше обычной рассылки (OneSignal).

### Cited Findings

Карточка 1. LinkedIn — «Generative Sequential Notification Optimization via Multi-Objective Decision Transformers» (arXiv 2509.02458, сентябрь 2025). Тип: инженерная статья. Масштаб: сотни кандидатов-уведомлений на пользователя, миллионы пользователей, 100–150 тыс. запросов в секунду. Теги: [СИГН] [УСТ] [ГАРД]. Статус: ОТКРЫТ. URL: https://arxiv.org/html/2509.02458v1
- Признаки состояния пользователя в модели: число и типы уведомлений, отправленных за последние X часов; время с последнего визита; история визитов; профиль; понимание содержания уведомления; контекст кандидата. — [LinkedIn arXiv 2509.02458](https://arxiv.org/html/2509.02458v1)
- Усталость моделируется штрафом: «adaptive volume penalty rewards» в функции награды, а не жёстким капом. — [LinkedIn arXiv 2509.02458](https://arxiv.org/html/2509.02458v1)
- Результат онлайн-эксперимента (Decision Transformer против CQL-базы): сессии +0,72%, объём уведомлений −1,68%, CTR без значимых изменений. Гардрейл-тройка: Sessions, Notification Volume, Notification CTR. — [LinkedIn arXiv 2509.02458](https://arxiv.org/html/2509.02458v1)

Карточка 2. YouTube — тест переменной частоты уведомлений для подписчиков «Все» (Social Media Today, 26.03.2025). Тип: новостной пересказ анонса YouTube. Теги: [СИГН] [УСТ]. Статус: ОТКРЫТ. URL: https://www.socialmediatoday.com/news/youtube-tests-update-channel-notification-frequency/743645/
- Ключевой сигнал: «недавняя вовлечённость несмотря на полученные уведомления». Зрителям, которые не взаимодействовали с каналом, хотя уведомления получали, пуш не отправляют, оставляя запись во входящих приложения. — [Social Media Today](https://www.socialmediatoday.com/news/youtube-tests-update-channel-notification-frequency/743645/)
- Мотивация: перегруженные пользователи не меняют подписку на канал, а отключают все уведомления YouTube целиком. Числовых результатов в статье нет. — [Social Media Today](https://www.socialmediatoday.com/news/youtube-tests-update-channel-notification-frequency/743645/)
- Вторичный пересказ (только по выдаче): эксперимент дал меньше отключений уведомлений по отдельным каналам и меньше полного отключения уведомлений приложения; цифр нет. — [PPC Land: YouTube ends push notifications for inactive subscribers](https://ppc.land/youtube-ends-push-notifications-for-inactive-subscribers-in-new-rollout/)

Карточка 3. OneSignal — «The 2026 State of Customer Engagement Report: Are AI Filters Already Deciding Who Sees Your Messages?» (автор Brian Wisniach, 25.03.2026). Тип: отчёт вендора по агрегированным данным платформы (размер выборки в открытой части не указан). Теги: [СИГН] [УСТ] [БЕНЧ]. Статус: ОТКРЫТ (страница-анонс; отраслевые таблицы opt-in в открытой части отсутствуют). URL: https://onesignal.com/blog/the-2026-state-of-customer-engagement-report-is-here/
- Поведенческие триггеры дают CTR выше обычной рассылки в 4–9 раз. — [OneSignal 2026](https://onesignal.com/blog/the-2026-state-of-customer-engagement-report-is-here/)
- По выдаче поиска (та же страница): CTR event-triggered push 4,38% против 0,91% при обычном таргетинге и 0,48% без таргетинга. — [OneSignal 2026](https://onesignal.com/blog/the-2026-state-of-customer-engagement-report-is-here/)
- 63% команд с автоматизированными Journeys сообщают о лучших результатах при меньшем числе сообщений; 78% — о росте выручки. — [OneSignal 2026](https://onesignal.com/blog/the-2026-state-of-customer-engagement-report-is-here/)
- 75,8% команд считают, что пуш сильнее всего влияет на удержание в первые 30 дней после установки (сигнал стадии жизненного цикла). — [OneSignal 2026](https://onesignal.com/blog/the-2026-state-of-customer-engagement-report-is-here/)

Карточка 4. Airship — «Mobile App Push Notification Benchmarks for 2025» (PDF, 30 стр., 19.03.2025, автор Abbie Baxter). Тип: бенчмарк-отчёт вендора. Масштаб: более 9 млрд пользователей приложений, тысячи приложений, 13 вертикалей, январь–декабрь 2024; в выборку входят приложения не менее чем с 1000 активных пользователей и 1000 пушей в месяц. Теги: [СИГН] [БЕНЧ] [УСТ] [ГАРД]. Статус: ОТКРЫТ (прочитан как PDF-изображения, стр. 1–15, 21–28). URL: https://growth.airship.com/rs/313-QPJ-195/images/Airship-2025-Push-Notification-Benchmarks-EN.pdf?version=0
- Сегментация и автоматизация: приложения, использующие пуш и in-app вместе с сегментацией и автоматизацией, имеют Engagement Score в среднем на 31% выше среднего по категории (ссылка на прежнее исследование Airship). — [Airship 2025 Benchmarks, стр. 3](https://growth.airship.com/rs/313-QPJ-195/images/Airship-2025-Push-Notification-Benchmarks-EN.pdf?version=0)
- Нулевая сторона данных: рекомендует опросы и центры предпочтений, чтобы знать, какой контент, где и когда клиент хочет получать. — [Airship 2025 Benchmarks, стр. 26](https://growth.airship.com/rs/313-QPJ-195/images/Airship-2025-Push-Notification-Benchmarks-EN.pdf?version=0)
- Онбординг-кампании повышают opt-in до 40% выше среднего по категории; in-app сообщения дают в среднем +14% к opt-in среди отписавшихся; пользователи с opt-in делают на 13% больше покупок, чем без opt-in (у лучших приложений до 39%). — [Airship 2025 Benchmarks, стр. 7, 12](https://growth.airship.com/rs/313-QPJ-195/images/Airship-2025-Push-Notification-Benchmarks-EN.pdf?version=0)

Карточка 5. Jeunen, Hanna, Wheeler — «Sustained Impact of Agentic Personalisation in Marketing: A Longitudinal Case Study» (arXiv 2604.08621, 09.04.2026). Тип: короткая научная статья (4 стр.), реальное потребительское приложение, 11 месяцев. Теги: [СИГН] [ГАРД]. Статус: ОТКРЫТ (только аннотация). URL: https://arxiv.org/abs/2604.08621
- Активная фаза (маркетологи вручную задают контент, аудитории, стратегии) даёт наибольший относительный прирост вовлечённости; в пассивной фазе автономные агенты из фиксированной библиотеки компонентов сохраняют положительный прирост. Числовых значений в аннотации нет. — [arXiv 2604.08621](https://arxiv.org/abs/2604.08621)

Карточка 6. Latinia — «How to Prevent Push Notification Fatigue in Banking». Тип: блог вендора, цитирует McKinsey Global Banking Annual Review 2024. Теги: [УСТ]. Статус: ВЫДАЧА (сниппет). URL: https://latinia.com/en/resources/how-to-prevent-push-notification-fatigue-in-banking
- По сниппету: банки с продвинутой персонализацией в реальном времени получают до +30% цифровой вовлечённости и −20% отказов от уведомлений (ссылка на McKinsey 2024; первоисточник не открыт, не использовать как твёрдую цифру).

### Inferences
- Из LinkedIn и YouTube видно, что состояние усталости на практике кодируют двумя классами признаков: «сколько отправили недавно» (счётчики за скользящее окно) и «реагировал ли на отправленное» (игнор при получении). Оба подходят как поля профиля для сегмента «в зоне риска усталости».
- YouTube и LinkedIn не поднимают порог для всех, а выключают или снижают частоту точечно для невовлечённых. Это прямо переносится в правило «подавление пуша для сегмента X, при этом сообщение остаётся в инбоксе/in-app».
- Все прирост-цифры (31% Engagement Score, 4–9x CTR) корреляционные, из данных вендоров; в кейсе их надо подавать как ориентир, а не как эффект сегментации.

### Gaps
- Не найдено новых (2023–2026) публикаций крупных B2C-компаний по сигналам LTV/RFM, чувствительности к цене, uplift-скорам и аффинити к категориям, кроме тех, что уже есть в known_urls. Здесь можно опираться на known_urls (например, Avito RFM, Uber, Swiggy, Grab frequency-capping); их содержимое мной не проверялось.
- Публикаций о числовых порогах «зоны риска усталости» (сколько игнорированных пушей подряд) у именованных компаний не найдено. Утверждения вендорских блогов об этом (например, «4 подряд проигнорированных пуша — кандидат на cooldown») я не включаю, так как не открывал источник.
- Данные о Zomato (сигналы: кухня, чек, время заказа, история просмотров) встретились только в низкокачественных блогах-пересказах; не использованы.

---

## 2. Усталость от коммуникаций: убывающая отдача, эксперименты со снижением объёма, моделирование

### Takeaway
Лучшая найденная количественная связка: у LinkedIn снижение объёма на 1,68% при росте сессий на 0,72% и неизменном CTR; в опросе Airship главные причины отказа от коммуникаций брендов — «слишком часто» и «нерелевантно»; в данных Airship типичное приложение шлёт около 6–8 пушей на пользователя в месяц (медиана), а верхние 10% — 150–160 (при этом у верхнего дециля выше сессии на активного пользователя, но это корреляция). Устаревшие, широко цитируемые «пороги» (46% отключений при 2–5 пушах в неделю и т. п.) вторичны и первоисточник не установлен.

### Cited Findings
- Эксперимент LinkedIn: меньше уведомлений, больше сессий, CTR без значимых изменений (+0,72% сессий, −1,68% объёма). — [LinkedIn arXiv 2509.02458](https://arxiv.org/html/2509.02458v1)
- OneSignal: 63% команд, перешедших на автоматизированные Journeys, видят лучшие результаты при меньшем числе сообщений. Это опрос, не эксперимент. — [OneSignal 2026](https://onesignal.com/blog/the-2026-state-of-customer-engagement-report-is-here/)
- Airship, опрос в семи странах: две главные причины отказа от коммуникаций брендов совпадали во всех странах — сообщения были либо слишком частыми, либо нерелевантными/не персонализированными. — [Airship 2025 Benchmarks, стр. 21](https://growth.airship.com/rs/313-QPJ-195/images/Airship-2025-Push-Notification-Benchmarks-EN.pdf?version=0)
- Airship, среднее число пушей на пользователя в месяц (годовые усреднённые месячные значения, 2023 → 2024). Android: P90 144 → 151,4; медиана 5,9 → 6,4; P10 0,4 → 0,6. iOS: P90 150 → 162,3; медиана 8,0 → 8,3; P10 0,8 → 0,8. — [Airship 2025 Benchmarks, стр. 24](https://growth.airship.com/rs/313-QPJ-195/images/Airship-2025-Push-Notification-Benchmarks-EN.pdf?version=0)
- Airship, P90 по вертикалям (iOS / Android, пушей на пользователя в месяц): Media 293,6 / 293,1; Sports 177,4 / 221; Entertainment 80,4 / 86,8; Social 53,7 / 46,9; Retail 34,1 / 27,3; Finance 7,5 / 5,1; Travel 15,9 / 15,9; Food & Drink 14,7 / 17,1. — [Airship 2025 Benchmarks, стр. 22–23](https://growth.airship.com/rs/313-QPJ-195/images/Airship-2025-Push-Notification-Benchmarks-EN.pdf?version=0)
- Airship: приложения из верхнего дециля по объёму отправок на пользователя дают в среднем на 72% больше сессий на активного пользователя против среднего по категории (Engagement Benchmarks, корреляция; сам отчёт предупреждает, что перегрузка подрывает доверие и ведёт к opt-out и удалению приложения). — [Airship 2025 Benchmarks, стр. 21](https://growth.airship.com/rs/313-QPJ-195/images/Airship-2025-Push-Notification-Benchmarks-EN.pdf?version=0)
- Только по выдаче поиска, первоисточник не установлен, данные старые: «1 пуш в неделю — 10% отключают и 6% удаляют приложение; 2–5 в неделю — 46% рискуют отключить; 6–10 в неделю — 32% удаляют». Страницы в выдаче: [Mobiloud: 50+ Push Notification Statistics for 2025](https://www.mobiloud.com/blog/push-notification-statistics) и [Business of Apps: Push Notifications Statistics (2026)](https://www.businessofapps.com/marketplace/push-notifications/research/push-notifications-statistics/); какая именно страница даёт какую цифру, я не проверял.
- Платформенный регулятор частоты: Android 16 (стабильный релиз 10.06.2025) включает по умолчанию «Notification Cooldown»: каждое следующее уведомление в серии от одного приложения тише и свёрнуто, на срок до 1–2 минут; приоритетные уведомления, звонки и будильники не затрагиваются. — [Android Authority](https://www.androidauthority.com/android-16-notification-cooldown-3501276/); дата стабильного релиза и «включено по умолчанию» — [PushEngage: Android 16 Notification Cooldown](https://www.pushengage.com/android-notification-cooldown/) (по выдаче).
- Модели усталости (состояние, затухание): у LinkedIn — состояние = счётчики отправленных за последние X часов + время с последнего визита; затухание не раскрыто, используется адаптивный штраф за объём. — [LinkedIn arXiv 2509.02458](https://arxiv.org/html/2509.02458v1)

### Inferences
- Для кейса честнее всего писать так: «у крупных игроков снижение объёма при сохранении результата достижимо и измерено (LinkedIn: −1,68% объёма при +0,72% сессий), но порог усталости зависит от вертикали: медиана 6–8 пушей в месяц на пользователя, у ритейла P90 около 27–34, у медиа P90 около 290».
- Цифры вроде «46% отключают при 2–5 пушах в неделю» нельзя класть в основу гардрейлов: они не привязаны к вертикали и первоисточнику; безопаснее ориентироваться на распределения Airship по вертикалям и на собственный holdout.
- Платформенные механизмы (Android cooldown) снижают ценность «пачек» из нескольких пушей подряд: пачка схлопывается на уровне ОС.

### Gaps
- Не найдено экспериментов 2023–2026 с «N-м сообщением в день/неделю» в виде кривой убывающей отдачи (вероятность отклика против числа предыдущих сообщений) у именованных компаний вне known_urls. LinkedIn даёт только агрегат объём/сессии.
- Нет опубликованных значений затухания (период полураспада усталости) — только то, что оно моделируется окном «последние X часов» и штрафом.
- Данные о доле удалений приложения именно из-за уведомлений из бенчмарк-отчётов Airship/OneSignal/Braze/MoEngage/CleverTap в открытых частях не найдены (в Airship за 2025 год метрики uninstall нет; отчёт лишь советует следить за ними).

---

## 3. Бенчмарки: opt-in пуша, отключения, отписки, жалобы, SMS

### Takeaway
Медианы opt-in по Airship (данные 2024): Android 59,5%, iOS 49,4%; Android падает после Android 13 (с 71,3% до 59,5% за год), iOS стабилен. Норма по email у Klaviyo (вторичные данные): отписки около 0,1–0,3% (среднее 0,2%), жалобы ниже 0,08–0,1%. Русскоязычные нормативы по отпискам/жалобам из открытых источников нашёл только в статье Mailfit в журнале Mindbox (Mail.ru: допустимая доля жалоб зависит от объёма).

### Cited Findings

Push opt-in (Airship, данные 2024, годовое усреднение месячных значений):
- Android: 2023 — P90 88,0%, медиана 71,3%, P10 42,1%; 2024 — P90 79,7%, медиана 59,5%, P10 37,1%. — [Airship 2025 Benchmarks, стр. 10](https://growth.airship.com/rs/313-QPJ-195/images/Airship-2025-Push-Notification-Benchmarks-EN.pdf?version=0)
- iOS: 2023 — 73,9% / 49,1% / 27,3%; 2024 — 74,1% / 49,4% / 27,1% (P90 / медиана / P10). — [Airship 2025 Benchmarks, стр. 10](https://growth.airship.com/rs/313-QPJ-195/images/Airship-2025-Push-Notification-Benchmarks-EN.pdf?version=0)
- Причина падения Android: приложения под Android 13+ обязаны получать согласие на уведомления (раньше включались по умолчанию). — [Airship 2025 Benchmarks, стр. 7](https://growth.airship.com/rs/313-QPJ-195/images/Airship-2025-Push-Notification-Benchmarks-EN.pdf?version=0)
- Примеры по вертикалям (в отчёте приведены для иллюстрации чтения данных, OS на графике не указана): Media — P90 60%, медиана 44,5%, P10 29,8%; Medical/Health/Fitness — 76,5% / 57,1% / 25,9%; Nonprofit — 76,1% / 67,5% / 36%. — [Airship 2025 Benchmarks, стр. 6](https://growth.airship.com/rs/313-QPJ-195/images/Airship-2025-Push-Notification-Benchmarks-EN.pdf?version=0)
- По графикам (чтение с изображения, точность около ±3 п.п.) медианы iOS: Education около 76%, Utility около 64%, Food & Drink около 62%, Media около 60%, Finance около 55%, Travel около 60%, Retail около 47%, Entertainment около 47%, Gaming/Gambling около 44%. Медианы Android: Utility около 71%, Gaming/Gambling около 70%, Finance около 67%, Travel около 67%, Education около 64%, Retail около 56%. — [Airship 2025 Benchmarks, стр. 8–9](https://growth.airship.com/rs/313-QPJ-195/images/Airship-2025-Push-Notification-Benchmarks-EN.pdf?version=0)
- Данные Airship за 2025 год (по выдаче поиска, вторичный пересказ): медиана Android 53,3%, iOS 48,85%. — [Trending Media Buzz: Push Notification Opt-In Rates](https://www.trendingmediabuzz.com/marketing/push-notification-opt-in-rate/)
- Противоречащие данные: у Pushwoosh (по сниппету поиска) в 2025 году глобальный opt-in 61%, Android 67%, iOS 56%, а в отдельном сравнении iOS 43,9% против Android 91,1% — несовместимые методики и выборки, использовать только как справку. — [Pushwoosh: Push notification benchmarks 2025](https://www.pushwoosh.com/blog/push-notification-benchmarks/)

Push direct open rate (Airship, Android, P90 по вертикалям; медианы по графику около 2–5%):
- Charities 20,1%, Utility 19%, Travel 17,6%, Medical/Health 15,7%, Government 15,3%, Education 12,3%, Food & Drink 9,8%, Social 9,9%, Entertainment 8,4%, Gaming 8,3%, Finance 8,1%, Retail 8,1%, Media 8%, Sports 6,4%. — [Airship 2025 Benchmarks, стр. 15](https://growth.airship.com/rs/313-QPJ-195/images/Airship-2025-Push-Notification-Benchmarks-EN.pdf?version=0)

Email (вторичные данные, агентские и агрегатор-страницы; официальной страницы Klaviyo с числами я не нашёл):
- Klaviyo: средняя отписка около 0,2% (диапазон 0,1–0,3%), жалоба на спам ниже 0,08–0,1%; по отраслям отписки: Fashion 0,20–0,35%, Health & Wellness 0,15–0,25%, Food & Beverage 0,12–0,20%, Pet 0,10–0,18%. — [Gosh Digital: Klaviyo Benchmarks by Industry](https://www.goshdigital.co/blog/klaviyo-benchmarks-by-industry) (по выдаче)
- Агрегатор: медианы B2B SaaS — отписка 0,15%, жалоба 0,02%; Ecommerce Fashion — 0,23% и 0,03%. — [Mailneo: Email benchmarks by industry (2026 database)](https://www.mailneo.co/benchmarks) (по выдаче, методика не проверена)
- Официальная справка Klaviyo числовых порогов отписки/жалоб/баунса не публикует; дельвербилити-скор считается за последние 30 дней по открытиям, кликам, баунсам, отпискам и жалобам, рассчитывается при не менее 1000 писем за 30 дней; шкала: Poor 0–49, Fair 50–74, Good 75–89, Excellent 90–100. — [Klaviyo Help: Understanding the email deliverability hub](https://help.klaviyo.com/hc/en-us/articles/18378819907995)

Россия (email):
- Mailfit в журнале Mindbox (14.10.2025, «Как сделать рассылку в Mail.ru, Yandex и Gmail: нюансы и советы»): Gmail допускает жалобы до 0,1%, критично 0,3%; Mail.ru — допустимая доля жалоб зависит от объёма: до 10 000 писем — 1,1%, при 10 млн и более — не выше 0,8%; для Яндекса порога не указано. Баунсы: до 2% норма, 2–5% — аудит, более 5% — серьёзные проблемы; доставляемость 95%+ оптимально. — [Mindbox Journal](https://mindbox.ru/journal/education/rassylka-yandex-mail-gmail/)
- Рекомендованные частоты по типам бизнеса (авторская рекомендация): e-commerce 2–4 раза в неделю, EdTech 1–2, медиа 3–7, B2B/SaaS 1–2 раза в месяц, маркетплейсы 3–5; контакты без активности 90+ дней предлагается отписывать вручную. — [Mindbox Journal](https://mindbox.ru/journal/education/rassylka-yandex-mail-gmail/)
- Утверждение автора «если более 70% пользователей не открывают 5–7 рассылок подряд, Gmail помечает письма как нерелевантные и отправляет в спам» не подтверждено официальной документацией Google; использовать как гипотезу. — [Mindbox Journal](https://mindbox.ru/journal/education/rassylka-yandex-mail-gmail/)

SMS (Россия):
- Требования к согласию и правам абонента: согласие должно быть явным и однозначным (не автоматически при регистрации на сайте), нужны отдельное согласие на рекламу и согласие на обработку персональных данных; с 01.08.2025 абонент может заранее отказаться от рекламных звонков и сообщений через оператора (после этого рассылка запрещена даже при наличии согласия); с 01.09.2025 согласие должно быть подтверждено оператором; штрафы по ст. 18 закона о рекламе: юрлица 300 тыс.–1 млн руб., должностные лица 20–100 тыс., физлица 10–20 тыс.; нарушения по закону о связи: малый бизнес 150–500 тыс., крупный/средний 300 тыс.–1 млн руб. — [Habr/click.ru: SMS-рассылки по новым правилам](https://habr.com/ru/companies/click/articles/955480/). Оговорка: нумерация законов в извлечении неточна (закон о связи — не № 41-ФЗ в моём прочтении), нужна сверка с первоисточником.
- Отдельные источники по выдаче утверждают, что рассылки допускаются 08:00–22:00 по времени получателя, а операторы вводят ограничения по частоте «не более 4 сообщений в сутки»; в статье Habr/click.ru про время суток и частоту ничего нет, поэтому эти цифры считаю непроверенными. — [Sostav: SMS-рассылки по новым правилам](https://www.sostav.ru/blogs/275971/69568) (по выдаче)

### Inferences
- Для планирования охвата пуш-канала на iOS ориентир медианы около 49%, на Android около 53–60% (с трендом вниз); верхний дециль iOS около 74% достижим только в вертикалях Education/Utility/Travel с хорошим онбордингом.
- Метрика «охват по пушу» должна считаться от базы с opt-in, иначе сегменты по каналу будут искажены тем, что Android теряет согласие системно, а не из-за качества коммуникаций.

### Gaps
- Нет открытых российских бенчмарков Mindbox/Unisender/Sendsay с числами по отпискам и жалобам, которые бы я открыл и проверил: поиск вернул рейтинги сервисов и общие статьи. Утверждение «норма отписок до 0,5%, жалоб ниже 0,1%» встретилось в сниппете без идентифицируемого источника; использовать нельзя.
- Не нашёл числовых бенчмарков SMS opt-out (процент ответов STOP) от Braze, Klaviyo, Attentive, а также российских.
- Данные Braze, MoEngage, CleverTap по доле отключений и удалений приложения из-за уведомлений в открытом доступе не получены (часть Braze уже в known_urls).
- Для Mail.ru официальные правила (help.mail.ru) дают только порог 5% невалидных адресов; порогов по жалобам в официальном документе нет, цифры 0,8–1,1% идут из статьи Mailfit и требуют сверки.

---

## 4. Жёсткие внешние пороги

### Takeaway
Для массовых отправителей Gmail (более 5000 писем в сутки на Gmail-адреса, с 01.02.2024) жёстко требует спам-рейт ниже 0,30% (цель ниже 0,10%) и one-click отписку по RFC 8058; Yahoo требует тот же 0,3% и исполнение отписки в течение двух дней. У Яндекса и Mail.ru публичных числовых порогов по жалобам не найдено. В пуше жёстких чисел нет, но Android 13+ ввёл обязательное согласие, а Android 16 — автоматическое «схлопывание» пачек уведомлений.

### Cited Findings
- Gmail (официальная справка «Email sender guidelines», доступ 2026-10-01): «массовый отправитель» — более 5000 сообщений в сутки на Gmail-аккаунты, требования действуют с 01.02.2024; обязательны SPF, DKIM, DMARC с выравниванием домена From; спам-рейт держать «ниже 0,30%» (жёсткое требование) и ниже 0,10% (рабочая цель, мониторинг через Postmaster Tools); маркетинговые и подписные письма должны поддерживать one-click отписку заголовками `List-Unsubscribe-Post: List-Unsubscribe=One-Click` и `List-Unsubscribe` (RFC 8058); Postmaster Tools только показывает метрики, ограничения применяет SMTP-ответами Gmail (обычно 4.7.28). — [Google: Email sender guidelines](https://support.google.com/a/answer/81126)
- Срок 48 часов на исполнение отписки в извлечённом тексте страницы Google не подтверждён; вторичные источники называют 48 часов, а также потерю права на смягчающие меры, пока спам-рейт не вернётся ниже 0,3% на 7 дней подряд. — [GMass: Gmail Bulk Sender Guidelines](https://www.gmass.co/blog/gmail-bulk-sender-guidelines/) (по выдаче)
- Yahoo Sender Hub, «Sender Best Practices» (по результатам поиска по сайту senders.yahooinc.com, доступ 2026-10-01): спам-рейт ниже 0,3%; функционирующий List-Unsubscribe с one-click для маркетинговых и подписных писем; заметная ссылка отписки в теле письма; исполнение отписки в течение 2 дней; one-click не требуется для транзакционных писем; для массовых отправителей SPF и DKIM и DMARC минимум p=none; программа Complaint Feedback Loop для DKIM-доменов. — [Yahoo Sender Hub: Sender Best Practices](https://senders.yahooinc.com/best-practices/) (по выдаче)
- Mail.ru (официальный раздел для разработчиков, «Общие положения», доступ 2026-10-01): более 5% невалидных адресов в базе ведёт к спаму или блокировке; отписка через List-Unsubscribe должна выполняться сразу после перехода по ссылке; готовой формулы прогрева домена и IP нет; числового порога жалоб нет. — [Mail.ru Help: Общие положения](https://help.mail.ru/developers/mailing_rules/general/)
- Яндекс: официальный раздел «Отправить много писем» и требования к честным рассылкам — отправлять только согласившимся, проставлять List-Unsubscribe, при жалобах доступ может быть заблокирован; числового порога жалоб в найденных страницах не было. — [Яндекс 360: Отправить много писем](https://yandex.ru/support/yandex-360/customers/mail/ru/web/letter/create/send-many-letters) (по выдаче); [Блог Почты: Яндекс.Почта для честных рассылок](https://yandex.ru/blog/mail/15382) (по выдаче)
- Apple/Google, пуш: Android 13+ требует runtime-разрешения на уведомления (подтверждено в отчёте Airship). — [Airship 2025 Benchmarks, стр. 7](https://growth.airship.com/rs/313-QPJ-195/images/Airship-2025-Push-Notification-Benchmarks-EN.pdf?version=0). Android 16 Notification Cooldown описан в разделе 2. Официальные Apple HIG и документацию Google по уведомлениям я не открывал (бюджет вызовов).
- Россия, SMS: см. раздел 3 (согласие, отказ через оператора с 01.08.2025, подтверждённое оператором согласие с 01.09.2025, штрафы). — [Habr/click.ru](https://habr.com/ru/companies/click/articles/955480/)

### Inferences
- Для email-канала разумная «трёхуровневая» шкала гардрейла: зелёная зона — жалобы ниже 0,10%, жёлтая — 0,10–0,30%, красная — 0,30% и выше (по Google и Yahoo). Она применима к домену отправителя в целом, а не к отдельной кампании: одна «шумная» кампания тянет вниз весь домен.
- Для России жалобы на Mail.ru, возможно, допускаются выше, чем на Gmail (по Mailfit: 0,8–1,1% зависимо от объёма), но это неофициальная цифра, поэтому корпоративный гардрейл логично брать по Gmail (0,10% / 0,30%).

### Gaps
- Не открыты первоисточники: Apple Human Interface Guidelines по уведомлениям, Android notification guidelines, правила Google Play и App Store по частоте и согласию на push.
- Не найден официальный числовой порог жалоб Яндекса; в сниппетах мелькает «0,8–1% блокировка домена» без подтверждающего первоисточника (всплыло в выдаче рядом с [Calltouch](https://www.calltouch.ru/blog/kak-sdelat-massovuyu-rassylku-pisem-v-yandeks-pochte-podrobnoe-rukovodstvo/); страницу не открывал).
- Нет первичного юридического текста по российским SMS (федеральные законы 2025 года, ограничения по времени суток и частоте); сверка нужна по КонсультантПлюс/Гарант.

---

## 5. Опубликованные наборы гардрейл-метрик у именованных компаний

### Takeaway
Из найденного: LinkedIn использует связку Sessions + Notification Volume + Notification CTR; Airship советует вместе с direct open rate смотреть конверсии, активных пользователей, opt-out, indirect opens и uninstalls; Klaviyo сводит дельвербилити в скор из открытий, кликов, баунсов, отписок и жалоб за 30 дней; YouTube следит за долей зрителей, отключающих уведомления канала и всего приложения.

### Cited Findings
- LinkedIn: Sessions (просмотры страниц с разрывом 30+ минут), Notification Volume (доставленные), Notification CTR как индикатор качества; цель — снизить объём без потери сессий и без падения CTR. — [LinkedIn arXiv 2509.02458](https://arxiv.org/html/2509.02458v1)
- Airship: direct open rate предлагается смотреть вместе с конверсиями, активными пользователями, opt-out, indirect opens и uninstalls. — [Airship 2025 Benchmarks, стр. 14](https://growth.airship.com/rs/313-QPJ-195/images/Airship-2025-Push-Notification-Benchmarks-EN.pdf?version=0)
- Klaviyo: компоненты скора доставляемости за 30 дней — открытия, клики, баунсы, отписки, жалобы; минимум 1000 писем. — [Klaviyo Help](https://help.klaviyo.com/hc/en-us/articles/18378819907995)
- Google и Yahoo: спам-рейт как внешний жёсткий гардрейл (0,10% цель, 0,30% предел) и время исполнения отписки (2 дня). — [Google](https://support.google.com/a/answer/81126); [Yahoo](https://senders.yahooinc.com/best-practices/)
- YouTube: доля зрителей, отключающих уведомления по каналу и по всему приложению, как негативный исход эксперимента (по вторичному пересказу). — [PPC Land](https://ppc.land/youtube-ends-push-notifications-for-inactive-subscribers-in-new-rollout/)

### Inferences
- Универсальный набор для кейса: (1) положительный результат (сессии/конверсия, лучше в holdout), (2) объём (сообщений на пользователя за окно), (3) качество (CTR/открытия), (4) негатив (отписки, жалобы, отключения пуша, удаления), (5) внешний предел (спам-рейт домена, баунсы). У LinkedIn нет прямого негативного показателя в найденной статье, он у Airship и YouTube.

### Gaps
- Пороговые значения самих гардрейлов (при каком росте отписок эксперимент останавливается) ни одна из найденных компаний не публикует.
- Наборы гардрейлов Uber, Swiggy, Grab, Pinterest, Netflix, Spotify уже в known_urls; здесь не перепроверялись.

---

## Сводные таблицы для отчёта

### Таблица 1. Таксономия сигналов

| Класс сигнала | Конкретные признаки | Кто использует (по моим источникам) | Источник |
|---|---|---|---|
| Стадия жизненного цикла | первые 30/90 дней после установки, онбординг | Airship (онбординг-кампании: opt-in до +40% к категории), OneSignal (75,8% команд: пуш сильнее всего влияет на удержание в первые 30 дней) | [Airship PDF](https://growth.airship.com/rs/313-QPJ-195/images/Airship-2025-Push-Notification-Benchmarks-EN.pdf?version=0); [OneSignal](https://onesignal.com/blog/the-2026-state-of-customer-engagement-report-is-here/) |
| Давность и активность | время с последнего визита, история визитов, «неактивен 90+ дней» | LinkedIn (state-признаки); Mailfit/Mindbox (чистка неактивных 90+ дней) | [LinkedIn](https://arxiv.org/html/2509.02458v1); [Mindbox](https://mindbox.ru/journal/education/rassylka-yandex-mail-gmail/) |
| Состояние усталости (нагрузка) | число и типы уведомлений за последние X часов | LinkedIn (признак + адаптивный штраф за объём) | [LinkedIn](https://arxiv.org/html/2509.02458v1) |
| Риск негативной реакции | нет вовлечённости при полученных уведомлениях; отключение уведомлений | YouTube (подавление пуша для подписчиков «Все» без недавней вовлечённости, остаётся инбокс) | [Social Media Today](https://www.socialmediatoday.com/news/youtube-tests-update-channel-notification-frequency/743645/) |
| Намерение и поведение в сессии | события-триггеры, поведенческие триггеры | OneSignal (CTR 4,38% против 0,91% и 0,48%; 4–9x) | [OneSignal](https://onesignal.com/blog/the-2026-state-of-customer-engagement-report-is-here/) |
| Содержание и контекст кандидата | понимание содержания уведомления, контекст | LinkedIn | [LinkedIn](https://arxiv.org/html/2509.02458v1) |
| Достижимость и согласие по каналу | opt-in пуша по ОС; Android 13+ runtime-разрешение; согласие на SMS (РФ, оператор); one-click отписка email | Airship (Android 59,5%, iOS 49,4% в 2024); Google/Yahoo; РФ-закон о рекламе | [Airship PDF](https://growth.airship.com/rs/313-QPJ-195/images/Airship-2025-Push-Notification-Benchmarks-EN.pdf?version=0); [Google](https://support.google.com/a/answer/81126); [Habr/click.ru](https://habr.com/ru/companies/click/articles/955480/) |
| Заявленные предпочтения (zero-party) | опросы, центры предпочтений: контент, время, канал | Airship (рекомендация) | [Airship PDF, стр. 26](https://growth.airship.com/rs/313-QPJ-195/images/Airship-2025-Push-Notification-Benchmarks-EN.pdf?version=0) |
| Модельные скоры (политика отправки) | многоцелевая оптимизация сессий, объёма и CTR (Decision Transformer); агентная персонализация | LinkedIn; Jeunen и др. (сохранение прироста в «пассивной» фазе) | [LinkedIn](https://arxiv.org/html/2509.02458v1); [arXiv 2604.08621](https://arxiv.org/abs/2604.08621) |
| Ценность (LTV, RFM), чувствительность к цене, аффинити к категории, uplift | не найдено в моих источниках 2023–2026 | см. known_urls (указатели, мной не проверялись) | н/д |

### Таблица 2. Пороги и нормы

| Показатель | Норма / порог | Тип порога | Источник и статус |
|---|---|---|---|
| Спам-рейт Gmail (массовые отправители, более 5000 писем/сутки на Gmail) | цель ниже 0,10%, жёстко ниже 0,30% | Жёсткий внешний, с 01.02.2024 | [Google](https://support.google.com/a/answer/81126), ОТКРЫТ |
| Спам-рейт Yahoo | ниже 0,3% | Жёсткий внешний | [Yahoo Sender Hub](https://senders.yahooinc.com/best-practices/), ВЫДАЧА |
| One-click отписка | заголовки List-Unsubscribe и List-Unsubscribe-Post (RFC 8058), для маркетинговых писем | Жёсткий внешний | [Google](https://support.google.com/a/answer/81126), ОТКРЫТ |
| Срок исполнения отписки | Yahoo: 2 дня; Google: 48 часов по вторичным источникам | Жёсткий (Yahoo), уточнить (Google) | [Yahoo](https://senders.yahooinc.com/best-practices/); [GMass](https://www.gmass.co/blog/gmail-bulk-sender-guidelines/), ВЫДАЧА |
| Невалидные адреса, Mail.ru | более 5% → спам или блокировка | Жёсткий внешний (официальный текст) | [Mail.ru Help](https://help.mail.ru/developers/mailing_rules/general/), ОТКРЫТ |
| Жалобы Mail.ru | до 10 тыс. писем — 1,1%; от 10 млн — не выше 0,8% | Неофициальная оценка эксперта | [Mindbox/Mailfit](https://mindbox.ru/journal/education/rassylka-yandex-mail-gmail/), ОТКРЫТ |
| Жалобы Яндекса | числового порога в открытых источниках не найдено | н/д | см. Gaps |
| Баунсы (email) | до 2% норма; 2–5% аудит; более 5% серьёзная проблема | Рекомендация эксперта | [Mindbox/Mailfit](https://mindbox.ru/journal/education/rassylka-yandex-mail-gmail/) |
| Отписки email, норма | около 0,1–0,3% (среднее 0,2%) | Бенчмарк (вторичный) | [Gosh Digital](https://www.goshdigital.co/blog/klaviyo-benchmarks-by-industry), ВЫДАЧА |
| Жалобы email, норма | ниже 0,08–0,1% (Klaviyo); медианы отраслей около 0,02–0,03% | Бенчмарк (вторичный) | [Gosh Digital](https://www.goshdigital.co/blog/klaviyo-benchmarks-by-industry); [Mailneo](https://www.mailneo.co/benchmarks), ВЫДАЧА |
| Push opt-in, Android (данные 2024) | P10 37,1%; медиана 59,5%; P90 79,7% (2023: 42,1 / 71,3 / 88,0) | Бенчмарк | [Airship PDF, стр. 10](https://growth.airship.com/rs/313-QPJ-195/images/Airship-2025-Push-Notification-Benchmarks-EN.pdf?version=0), ОТКРЫТ |
| Push opt-in, iOS (данные 2024) | P10 27,1%; медиана 49,4%; P90 74,1% (2023: 27,3 / 49,1 / 73,9) | Бенчмарк | то же, ОТКРЫТ |
| Push opt-in, 2025 (вторичный пересказ) | медианы: Android 53,3%, iOS 48,85% | Бенчмарк (вторичный) | [Trending Media Buzz](https://www.trendingmediabuzz.com/marketing/push-notification-opt-in-rate/), ВЫДАЧА |
| Пушей на пользователя в месяц (2024) | Android: P10 0,6, медиана 6,4, P90 151,4; iOS: 0,8 / 8,3 / 162,3; P90 Media около 293, Sports 177–221, Retail 27–34, Finance 5–8 | Бенчмарк | [Airship PDF, стр. 22–24](https://growth.airship.com/rs/313-QPJ-195/images/Airship-2025-Push-Notification-Benchmarks-EN.pdf?version=0), ОТКРЫТ |
| Direct open rate пуша (Android, P90) | от 6,4% (Sports) до 20,1% (Charities); Retail 8,1%; Finance 8,1%; медианы около 2–5% | Бенчмарк | [Airship PDF, стр. 15](https://growth.airship.com/rs/313-QPJ-195/images/Airship-2025-Push-Notification-Benchmarks-EN.pdf?version=0), ОТКРЫТ |
| Эффект opt-in на покупки | +13% покупок у подписанных; у лучших приложений до +39% | Бенчмарк (корреляция) | [Airship PDF, стр. 7](https://growth.airship.com/rs/313-QPJ-195/images/Airship-2025-Push-Notification-Benchmarks-EN.pdf?version=0), ОТКРЫТ |
| Эксперимент с объёмом | LinkedIn: объём −1,68%, сессии +0,72%, CTR без значимых изменений | Пример гардрейла и эффекта | [LinkedIn arXiv](https://arxiv.org/html/2509.02458v1), ОТКРЫТ |
| Android Notification Cooldown | серия уведомлений от одного приложения схлопывается и затихает до 1–2 минут; приоритетные, звонки, будильники исключены | Платформенный механизм (Android 16, июнь 2025) | [Android Authority](https://www.androidauthority.com/android-16-notification-cooldown-3501276/); [PushEngage](https://www.pushengage.com/android-notification-cooldown/), ВЫДАЧА |
| Android 13+ | обязательное runtime-разрешение на уведомления | Платформенный жёсткий | [Airship PDF, стр. 7](https://growth.airship.com/rs/313-QPJ-195/images/Airship-2025-Push-Notification-Benchmarks-EN.pdf?version=0), ОТКРЫТ |
| SMS в РФ | явное согласие; с 01.08.2025 отказ через оператора; с 01.09.2025 согласие подтверждается оператором; штрафы юрлиц по ст. 18 закона о рекламе 300 тыс.–1 млн руб. | Закон (с оговоркой по номерам законов) | [Habr/click.ru](https://habr.com/ru/companies/click/articles/955480/), ОТКРЫТ |
| SMS в РФ: время и частота | 08:00–22:00 и «не более 4 в сутки» | Не подтверждено, только сниппет | [Sostav](https://www.sostav.ru/blogs/275971/69568), ВЫДАЧА |
| Устаревшие частотные «пороги» (1/нед: 10% отключений, 6% удалений; 2–5/нед: 46%; 6–10/нед: 32% удаляют) | цифры без установленного первоисточника | Использовать только как справку | [Mobiloud](https://www.mobiloud.com/blog/push-notification-statistics); [Business of Apps](https://www.businessofapps.com/marketplace/push-notifications/research/push-notifications-statistics/), ВЫДАЧА |
| Дельвербилити-скор Klaviyo | окно 30 дней, мин. 1000 писем; Poor 0–49, Fair 50–74, Good 75–89, Excellent 90–100 | Набор метрик вендора | [Klaviyo Help](https://help.klaviyo.com/hc/en-us/articles/18378819907995), ОТКРЫТ |
