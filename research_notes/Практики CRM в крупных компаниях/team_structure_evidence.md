# Структура CRM / lifecycle / коммуникационных команд в крупных B2C-компаниях: горизонтальная платформа vs вертикальные команды (topic [3])

Условные обозначения достоверности:
- **[О]** — страница открыта и прочитана целиком (через WebFetch).
- **[С]** — виден только заголовок и сниппет в поисковой выдаче (страница не открылась: 403/404/500). Использовать осторожно, как индикатор, а не как доказательство деталей.
- **[В]** — источник вне окна октябрь 2023 – октябрь 2026; приведён только как контекст.
- Для вакансий без даты указано «актуальная вакансия на дату проверки 2026-10-01» либо «снята/архивная, дата публикации не указана».

Охват: открыто 8 источников (7 в окне дат, 1 вне окна), ещё ~9 источников видны только по сниппетам. Устойчивые (с прочитанным текстом) примеры в окне дат: Avito, Zalando, Duolingo, Uber, Яндекс Путешествия — пять компаний; Delivery Hero и Airbnb — только сниппеты; LinkedIn — вне окна. Порог «8+ конкретных компаний» достигнут только если считать сниппеты и контекст вне окна. Лимит в 30 вызовов инструментов исчерпан.

---

## 1. Какие компании разделяют «платформу коммуникаций / каналы / CRM-инструменты» (горизонталь) и «журнейсы/кампании по продуктам и бизнес-линиям» (вертикаль) и что владеет каждая сторона?

### Takeaway
Самое чёткое разделение на платформу и вертикали-клиентов задокументировано у Avito (платформа коммуникаций в продуктовой команде + вертикали Товары/Авто/Недвижимость/Услуги/Работа как внутренние клиенты). У Zalando CRM — централизованная команда до 50 FTE, которая исполняет кампании для стран и «propositions»; у Duolingo горизонтальная команда Notifications задаёт стандарты, а уведомления своих фич отправляют сами продуктовые команды. У Яндекса и Uber видны CRM-группы, привязанные к конкретным сервисам и аудиториям (вертикали), но про их центральную платформу вакансии прямо не говорят.

### Cited Findings

**Avito** (маркетплейс; вертикали Товары, Авто, Недвижимость, Услуги, Работа; масштаб аудитории на страницах не указан)
- Страница «Вакансии в команду коммуникационных продуктов Авито» — актуальная страница на дату проверки 2026-10-01, дата не указана; тип: карьерная страница [О]. Команда коммуникационных продуктов владеет мессенджером, звонками (маскировка номеров, колл-трекинг, защита от спама), чат-ботами и CRM-платформой (push, email, центр уведомлений, мессенджер; сегментация и триггерные кампании). Обслуживает частных пользователей и бизнес-продавцов по категориям Goods, Auto, Jobs, Services, Real Estate. Открытые роли: Senior PM (мессенджер, звонки, боты) и Lead PM CRM-платформы коммуникаций — [career.avito.com/teams/communication-products](https://career.avito.com/teams/communication-products/)
- «Ведущий продакт-менеджер платформы коммуникаций Авито с пользователями (CRM)» — размещена 8 июля 2026, обновлена 2 августа 2026; тип: вакансия Avito, зеркало на агрегаторе freehire.me (оригинал на сайте Avito не открывался) [О]. Мандат платформы: «развитие системы, через которую проходят и балансируются все коммуникации сервиса с пользователями»; платформа определяет, «что и кому сообщает сервис», балансирует частоту, канал, объём и время доставки, использует двухстадийный подбор сообщений. Внутренние клиенты — вертикали (Авито Товары, Авто, Недвижимость, Услуги, Работа). Партнёры: маркетинг вертикалей, ML/инженерия/инфраструктура, аналитики и Data Science, команды ранжирования и рекомендаций. От PM ждут опыта A/B-тестов, инкрементальности и holdout-замеров — [freehire.me, вакансия Avito](https://freehire.me/jobs/vedushchii-prodakt-menedzher-platformy-kommunikatsii-avito-s-pol-zovateliami-crm-avito-rw6vfnrl)
- Habr «Как мы в Авито проводим A/B-тесты CRM-рассылок» — 23 января 2025, автор Armen Yesan, data analyst по CRM в Avito; тип: инженерный/аналитический пост компании [О]. CRM-маркетологи создают кампании по предоставленным шаблонам, CRM-аналитики валидируют результаты и оценивают баланс между вовлечением и оттоком; по тексту, в 2023 году CRM-отдел провёл 39% всех A/B-тестов в Avito — [Habr, Avito](https://habr.com/ru/companies/avito/articles/875012/)

**Zalando** (по тексту вакансии: 52M+ клиентов, 26 рынков)
- «Director of CRM - Zalando» (BuiltIn) — вакансия снята 22 апреля 2025, исходная дата публикации не указана; тип: вакансия [О]. Мандат: «operational and strategic implementation of Zalando's communication platform» — своевременная и релевантная CRM-коммуникация по всем каналам. Команда до 50 FTE с пятью внутренними функциями: Audience Management (стратегия, сегментация, планирование каналов), Direct Marketing (исполнение кампаний), Product & Tech Consulting (развитие платформы, настройка каналов), Engineering (инфраструктура, масштабируемость), Analytics (отчётность, таргетинг, измерение). Бизнес-партнёры: Country General Managers, Proposition Leaders, Loyalty team, Product & Engineering leadership, Applied Science teams — [BuiltIn: Director of CRM - Zalando](https://builtin.com/job/director-crm/4687095)
- «CRM Manager - Loyalty (all genders) at Zalando» [С] — виден только заголовок; говорит о том, что у программы лояльности есть выделенный CRM-менеджер (деталей нет) — [scalestack.ai](https://scalestack.ai/jobboard/jobs/crm-manager-loyalty-all-genders-at-zalando-61bn03)

**Duolingo**
- «Lead Product Manager, Notifications - Duolingo» (BuiltIn) — снята 25 июля 2025, дата публикации не указана; тип: вакансия [О]. Роль должна устанавливать лучшие практики управления уведомлениями «на уровне отдельной фичи и компании в целом» и «работать с командами по всему Duolingo над улучшением уведомлений, которые они отправляют для своих фич» (in-app, email, тексты, фреймворки экспериментов). Партнёры: дизайнеры, product writers, инженеры, кросс-функциональные продуктовые команды, руководство — [BuiltIn](https://builtin.com/job/lead-product-manager-notifications/3578682)
- «Senior Product Manager, Notifications - Duolingo» [С, страница вернула 403; сведения из сниппета поиска] — команда Notifications находится в «Out-of-App Area» внутри Growth-направления; ведёт новые типы уведомлений, opt-in и охват, email и альтернативные каналы; сотрудничает с product, engineering, data science, ML/AI, design и product writing — [BuiltIn NYC](https://www.builtinnyc.com/job/senior-product-manager-social-growth/8492791)

**Uber**
- «Global CRM Marketing Associate» — 1 марта 2025, вакансия закрыта; тип: вакансия (зеркало huzzle) [О]. Команда Global CRM Marketing (фокус — ранний lifecycle клиентов Eats): E2E-стратегия CRM, lifecycle-маркетинг, маркетинговая автоматизация (транзакционные, промо, информационные кампании), управление промо, KPI и сегментация. Партнёры: региональный маркетинг, data science, product, market research & insights, marketing analytics, команды deployment и контента/креатива, operations, communications, business development — [Huzzle](https://www.huzzle.com/jobs/global-crm-marketing-associate-806606)
- «Marketing Technology Associate, CRM Deployment - New York» [С, страница вернула 500] — по сниппету, североамериканская CRM-команда, где сотрудник работает с маркетологами, PM, инженерами и операциями «чтобы сообщения доходили до нужной аудитории» — [Uber Careers](https://www.uber.com/global/en/careers/list/145655/)
- «product operations manager personalized marketing solutions» [С, страница вернула 404] — по сниппету, команда «CRM Strategic Operations» на стыке marketing, product и engineering — [The Muse](https://www.themuse.com/jobs/uber/product-operations-manager-personalized-marketing-solutions)
- «CRM Marketing Manager, Merchant at Uber» [С] — выделенная Merchant CRM team; сквозная lifecycle-стратегия для сезонных пиков — [The Muse](https://www.themuse.com/jobs/uber/crm-marketing-manager-merchant)
- «Uber hiring Regional CRM Operations Manager in San Francisco» [С, дата не определена, ID вакансии указывает, вероятно, на старую публикацию — возможно вне окна] — US/CA Deployment Lead отвечает за команду, которая «строит и рассылает» коммуникации миллионам пользователей (Drivers, Riders, Couriers, Eaters, Restaurants) через собственные цифровые каналы — [LinkedIn](https://www.linkedin.com/jobs/view/regional-crm-operations-manager-at-uber-2220527242)

**Яндекс** (CRM-группы по сервисам)
- «Вакансия «Руководитель группы CRM маркетинга в Путешествия» в Яндексе» — архивная вакансия, дата не указана [О]. Группа отвечает за CRM-стратегию Яндекс Путешествий: каналы email, push, SMS, мессенджер, ремаркетинговые баннеры; база более 1 млн пользователей; частота и ToV; взаимодействие с продуктовой командой для развития CRM-инструментов и системы коммуникаций — [Яндекс Вакансии](https://yandex.ru/jobs/vacancies/rukovoditel-gruppi-crm-marketinga-v-puteshestviya-13522)
- Отдельные вакансии CRM-групп под разные сервисы [С, только заголовки из выдачи; даты не определены]: «Руководитель группы CRM маркетинга в Москве … Яндекс Доставка» — [hh.ru](https://hh.ru/vacancy/122390144); «Руководитель CRM в Яндекс.Директ» — [Яндекс Вакансии](https://yandex.ru/jobs/vacancies/%D1%80%D1%83%D0%BA%D0%BE%D0%B2%D0%BE%D0%B4%D0%B8%D1%82%D0%B5%D0%BB%D1%8C-crm-%D0%B2-%D1%8F%D0%BD%D0%B4%D0%B5%D0%BA%D1%81-%D0%B4%D0%B8%D1%80%D0%B5%D0%BA%D1%82-4771); «Руководитель CRM-маркетинга (международное направление) в Яндекс.Еду» — [Facancy](https://facancy.ru/vacancies/rukovoditel-crm-marketinga-mezhdunarodnoe-napravlenie-v-iandeks-edu); «Вакансия CRM-маркетолог в Яндекс Браузер в Казани» — [Careerist](https://kazan.careerist.ru/vakansii/crm-marketolog-v-yandeks-brauzer-83213002.html)

**Delivery Hero (foodpanda)**
- «Head, Crm at Delivery Hero (foodpanda)» [С, страница вернула 403; агрегатор; дата не определена] — по сниппету, роль отвечает за lifecycle-видение и стратегию по трём брендам и 16 рынкам, руководит lifecycle-менеджерами, CRM Ops и MarTech-специалистами — [Workopia](https://workopia.io/jobs/f759cde2ffedd3090fec233a857174fa)

**Airbnb**
- «Staff Software Engineer, Marketing Technology Orchestration - Airbnb» [С, страница вернула 403; дата не определена] — по сниппету, Orchestration Platform Team даёт marketing- и product-командам возможность связываться с гостями и хостами персонализированными сообщениями по пользовательским путям — [BuiltIn NYC](https://www.builtinnyc.com/job/staff-software-engineer-marketing-technology-orchestration/6259078)

**LinkedIn [В — вне периода, 20 декабря 2017]**
- «Scaling notifications through a platform approach» (Adam Hobson, Notification Platform Team, InfoWorld) [О]. Платформа даёт дизайн-систему уведомлений, render models, общую схему и сервис Air Traffic Controller («управление частотой и выбором канала внешних коммуникаций с участниками»); команды-партнёры владеют «producers» уведомлений и добавляют одну строку кода для привязки типа уведомления к способу агрегации; в статье «dozens of partner teams». Использовать только как архитектурный ориентир — [InfoWorld](https://www.infoworld.com/article/2260937/scaling-notifications-through-a-platform-approach.html)

### Inferences
- Прослеживаются три модели (гипотезы по прочитанным источникам, не утверждения компаний):
  1. **Платформа как продукт + вертикали-клиенты** (Avito; ориентир LinkedIn): платформа владеет правилами доставки (частота, канал, объём, время, балансировка), инструментами, A/B-инфраструктурой; вертикали (их маркетинг) формируют кампании и бизнес-цели. В Avito среди партнёров платформы прямо названы маркетинг вертикалей.
  2. **Центральная CRM-фабрика** (Zalando): одна команда до 50 FTE с собственными аудиторным менеджментом, direct marketing, продуктово-техническим консалтингом и инжинирингом; страны и propositions выступают заказчиками, а не самостоятельными исполнителями.
  3. **Enabler + feature teams** (Duolingo): горизонтальная Notifications-команда задаёт стандарты и инструменты, продуктовые команды сами отправляют уведомления своих фич.
- Яндекс и Uber по вакансиям выглядят как CRM по сервисам/аудиториям (Путешествия, Доставка, Директ, Еда, Браузер; Eats-lifecycle, Merchant), с отдельной «deployment»/«strategic operations» функцией у Uber. Это вертикальная модель с неподтверждённой центральной платформой.
- Владение по предметам (только то, что прямо видно): каналы и правила доставки — платформа (Avito); сегментация и кампании — вертикальный маркетинг (Avito) или центральный Audience Management (Zalando); эксперименты — A/B-фреймворк у платформы/CRM-отдела (Avito, Duolingo); шаблоны — упоминаются у Avito как предоставляемые CRM-маркетологам.

### Gaps
- Нет прямых данных, кто владеет бюджетом на коммуникации (платформа или вертикали), кто владеет контентом/шаблонами в Duolingo, Zalando, Uber.
- Ни одна вакансия не показала организационную схему «Яндекс: центральная CRM-платформа ↔ CRM-группы сервисов»; это остаётся выводом из заголовков.
- Revolut, Monzo, Nubank, Booking, Spotify (потребительская сторона), Grab, Swiggy, Zalando-платформа, Т-Банк, Сбер, Ozon, Купер, Самокат, МТС, Альфа-Банк, X5, Магнит: найти в рамках бюджета не удалось. Т-Банк: в выдаче были только общие страницы карьеры («Бизнес-платформы», вакансии Т-Бизнес с junior CRM-менеджером) без описания структуры; не включено.
- Ложное срабатывание для отчёта: вакансия Ozon «Руководитель группы разработки (Платформа коммуникаций)» на getmatch по сниппету относится к внутренним корпоративным инструментам (Mattermost, Jitsi), а не к клиентским коммуникациям — [getmatch](https://getmatch.ru/vacancies/15358-rukovoditel-gruppy-razrabotki-platforma-kommunikatsii). Не использовать как пример CRM-платформы.
- Spotify «Associate Director, CRM & Martech» (Glassdoor) относится к рекламодателям (B2B), а не к потребителям; для данной темы нерелевантно.

---

## 2. Как разрешаются конфликты между бизнес-линиями за одного пользователя (общий бюджет уведомлений, приоритеты, советы, центральный арбитражный сервис, SLA/согласования)?

### Takeaway
Единственный хорошо документированный в окне дат механизм — центральный сервис-арбитр в Avito: балансировщик, который из 400+ ежедневных кампаний оставляет пользователю только наиболее релевантные и ограничивает суточный объём коммуникаций. Про советы, согласования, SLA и «общую валюту уведомлений» в найденных источниках нет прямых данных.

### Cited Findings
- Avito: платформа применяет политики, ограничивающие суточный объём уведомлений на пользователя; балансировщик распределяет 400+ ежедневных кампаний и при пересечении аудиторий «сравнивает кампании и отправляет пользователю только наиболее релевантные в течение дня», что предотвращает каннибализацию каналов. Глобальная контрольная группа используется, чтобы измерять совокупный инкрементальный эффект всех CRM-коммуникаций — Habr, 23 января 2025 [О] — [Habr, Avito](https://habr.com/ru/companies/avito/articles/875012/)
- Avito (мандат платформы в вакансии, июль–август 2026): платформа «балансирует частоту, канал, объём и время доставки», использует «двухстадийную схему подбора» и управляет «конкурирующими вертикалями в едином опыте» [О, зеркало вакансии] — [freehire.me](https://freehire.me/jobs/vedushchii-prodakt-menedzher-platformy-kommunikatsii-avito-s-pol-zovateliami-crm-avito-rw6vfnrl)
- Avito (дополнительные статьи, не открывались, выданы поиском по теме балансировщика): «Как мы автоматизировали A/B-тестирование CRM-рассылок и избавили аналитиков от рутины» — [Habr](https://habr.com/ru/companies/avito/articles/918634/); «Как с помощью доработки RFM сделать CRM-рассылки эффективнее» — [Habr](https://habr.com/ru/companies/avito/articles/838722/)
- Duolingo: роль Lead PM Notifications включает «установление лучших практик управления уведомлениями на уровне фичи и компании в целом», то есть конфликт между фичами решается стандартами и экспертизой центральной команды (формулировка вакансии; механизма принуждения не описано) — [BuiltIn](https://builtin.com/job/lead-product-manager-notifications/3578682)
- [В] LinkedIn: Air Traffic Controller управляет частотой и выбором канала внешних коммуникаций «на уровне участника» для всех партнёрских команд, 2017 — [InfoWorld](https://www.infoworld.com/article/2260937/scaling-notifications-through-a-platform-approach.html)

### Inferences
- Рабочий паттерн в найденных кейсах — «технический арбитр» на стороне платформы (лимит частоты на пользователя + выбор лучшего сообщения по релевантности), а не регулярный совет по приоритетам.
- Глобальная контрольная группа у Avito показывает, что платформа измеряет вклад CRM целиком, а не только отдельных вертикалей; это даёт общую базу для споров о распределении «внимания» пользователя (интерпретация).
- В Zalando, судя по составу бизнес-партнёров (Country GMs, Proposition Leaders), конфликты, вероятно, решаются через стейкхолдер-менеджмент директора CRM; в вакансии механизма нет.

### Gaps
- Не найдено ни одного источника про формальные советы, SLA, процедуры согласования или «внутреннюю валюту» (кредиты на коммуникации) между бизнес-линиями.
- Неизвестно, как в балансировщике Avito задаются приоритеты: только релевантность или есть бизнес-веса вертикалей. В прочитанной статье Habr и вакансии это не раскрыто.
- По Uber, Zalando, Яндексу нет данных о едином лимите частоты между сервисами.

---

## 3. Где CRM находится в организации (маркетинг, продукт, данные, отдельный CVM/CRM) и как взаимодействует с data science, legal/compliance, поддержкой и брендом?

### Takeaway
В прочитанных источниках позиции различаются: у Zalando CRM подчинён Performance Marketing & Growth, у Duolingo — продуктовая команда в Growth, у Avito — платформа в продуктовой организации (команда коммуникационных продуктов) с CRM-аналитиками и маркетологами, у Uber CRM — внутри маркетинга с отдельной операционной/стратегической функцией на стыке с product и engineering. Data science присутствует как партнёр везде; legal/compliance и поддержка в вакансиях практически не упоминаются.

### Cited Findings
- Zalando: Director of CRM подчиняется руководству Performance Marketing & Growth и описан как «key member of Zalando's leadership team»; партнёры — Country GMs, Proposition Leaders, Loyalty team, Product & Engineering leadership, Applied Science teams. Вакансия снята 22 апреля 2025 [О] — [BuiltIn](https://builtin.com/job/director-crm/4687095)
- Zalando: отдельная роль «Head of Revenue Operations & CRM - Platform Experience & Revenue Operations» [С, 404 при открытии; по сниппету — «newly established», строит revenue operating system платформы Zalando и «coherent CRM ecosystem»; дата не определена] — это другая ветка организации (Platform), а не Performance Marketing; соотношение двух CRM-ролей не раскрыто — [Zalando Jobs](https://jobs.zalando.com/en/jobs/2723917-Head-of-Revenue-Operations-&-CRM---Platform-Experi)
- Duolingo: Notifications — продуктовая команда (PM-led) в Growth («Out-of-App Area») [С]; партнёры — product, engineering, data science, ML/AI, design, product writing — [BuiltIn NYC](https://www.builtinnyc.com/job/senior-product-manager-social-growth/8492791). Lead PM Notifications работает с designers, product writers, engineers [О] — [BuiltIn](https://builtin.com/job/lead-product-manager-notifications/3578682)
- Uber: Global CRM Marketing — маркетинговая функция; партнёры: product, data science, market research & insights, marketing analytics, регион, deployment, контент/креатив, operations, communications — 1 марта 2025 [О] — [Huzzle](https://www.huzzle.com/jobs/global-crm-marketing-associate-806606). Отдельная «CRM Strategic Operations» на стыке marketing/product/engineering [С] — [The Muse](https://www.themuse.com/jobs/uber/product-operations-manager-personalized-marketing-solutions)
- Avito: платформа коммуникаций — часть продуктовой команды «коммуникационных продуктов» вместе с мессенджером, звонками и ботами; партнёры — ML/инженерия, аналитики/DS, ранжирование/рекомендации, маркетинг вертикалей [О] — [career.avito.com](https://career.avito.com/teams/communication-products/), [freehire.me](https://freehire.me/jobs/vedushchii-prodakt-menedzher-platformy-kommunikatsii-avito-s-pol-zovateliami-crm-avito-rw6vfnrl). CRM-аналитики и CRM-маркетологи описаны как роли в CRM-контуре [О] — [Habr](https://habr.com/ru/companies/avito/articles/875012/)
- Яндекс Путешествия: CRM-группа взаимодействует с продуктовой командой для развития CRM-инструментов; ToV и частота — зона ответственности группы [О] — [Яндекс Вакансии](https://yandex.ru/jobs/vacancies/rukovoditel-gruppi-crm-marketinga-v-puteshestviya-13522)
- Delivery Hero: Head of CRM руководит lifecycle-менеджерами, CRM Ops и MarTech [С] — [Workopia](https://workopia.io/jobs/f759cde2ffedd3090fec233a857174fa)

### Inferences
- Организационная «домашняя база» CRM — не единая: marketing (Zalando, Uber), product/growth (Duolingo, Avito). Чем больше CRM воспринимается как инфраструктура (платформа, алгоритмы доставки), тем чаще она в продукте; чем больше как исполнение и стратегия кампаний — тем чаще в маркетинге (обобщение по 4–5 кейсам, не статистика).
- Data science/analytics встроены как постоянные партнёры (Avito: DS, ранжирование/рекомендации; Zalando: Applied Science; Uber: data science; Duolingo: data science, ML/AI).
- Бренд/контент проявляется через product writers (Duolingo), content/creative (Uber), ToV (Яндекс).

### Gaps
- Нет ни одного упоминания legal/compliance и customer support как формальных партнёров CRM-команды в прочитанных вакансиях (кроме общих «operations»/«communications» у Uber). Отсутствие упоминания не доказывает отсутствие взаимодействия.
- Нет данных по отдельным CVM-подразделениям (банки, телеком): Т-Банк, Сбер, Альфа-Банк, МТС по бюджету не раскрыты.
- Не открыты: Lenny's Newsletter «How Duolingo builds product» (в выдаче: https://www.lennysnewsletter.com/p/how-duolingo-builds-product), которая могла бы подтвердить положение Notifications и Retention внутри Growth.

---

## 4. Размеры команд и роли (CRM manager, lifecycle PM, CRM analyst, CRM developer, marketing ops), где указаны

### Takeaway
Размер команды указан только у Zalando (до 50 FTE, пять функций). По остальным компаниям видны названия ролей, но не численность.

### Cited Findings
- Zalando: до 50 FTE; функции Audience Management, Direct Marketing, Product & Tech Consulting, Engineering, Analytics; вакансия снята 22 апреля 2025 [О] — [BuiltIn](https://builtin.com/job/director-crm/4687095)
- Avito: роли CRM-маркетолог (кампании по шаблонам), CRM-аналитик (валидация результатов, баланс вовлечения и оттока), Lead PM CRM-платформы коммуникаций, Senior PM мессенджера/звонков/ботов; численность не указана [О] — [Habr](https://habr.com/ru/companies/avito/articles/875012/), [career.avito.com](https://career.avito.com/teams/communication-products/)
- Uber: роли CRM Marketing Associate/Manager, Marketing Technology Associate (CRM Deployment), Regional CRM Operations Manager (US/CA Deployment Lead), Product Operations Manager (Personalized Marketing Solutions); зарплата Global CRM Marketing Associate — базовая $104,000–$115,500, Нью-Йорк, 1 марта 2025 [О для Global CRM Marketing Associate, остальные — С] — [Huzzle](https://www.huzzle.com/jobs/global-crm-marketing-associate-806606), [Uber Careers](https://www.uber.com/global/en/careers/list/145655/), [The Muse](https://www.themuse.com/jobs/uber/product-operations-manager-personalized-marketing-solutions), [LinkedIn](https://www.linkedin.com/jobs/view/regional-crm-operations-manager-at-uber-2220527242)
- Delivery Hero (foodpanda): lifecycle-менеджеры, CRM Ops, MarTech, 3 бренда и 16 рынков под одним Head of CRM [С] — [Workopia](https://workopia.io/jobs/f759cde2ffedd3090fec233a857174fa)
- Duolingo: PM, дизайн, product writing, инжиниринг, data science, ML/AI; численность не указана; зарплатная вилка Lead PM $148,800–$274,600, New York (гибрид), вакансия снята 25 июля 2025 [О] — [BuiltIn](https://builtin.com/job/lead-product-manager-notifications/3578682)
- Яндекс Путешествия: руководитель группы CRM-маркетинга; численность группы не раскрыта [О] — [Яндекс Вакансии](https://yandex.ru/jobs/vacancies/rukovoditel-gruppi-crm-marketinga-v-puteshestviya-13522)

### Inferences
- Роли типично разделены на (а) стратегию/кампании (CRM manager/marketer), (б) операции/развёртывание (CRM Ops, Deployment), (в) продукт/технологии платформы (PM, MarTech, engineering), (г) аналитику/эксперименты. Явное выделение «deployment/ops» отдельно от стратегии видно у Uber и Delivery Hero (по сниппетам); у Zalando аналогичное разделение внутри одной команды.
- Единичный размер (Zalando, до 50 FTE на 52M+ клиентов) нельзя обобщать на другие компании.

### Gaps
- Нет данных о соотношении числа CRM-менеджеров к числу вертикалей, о численности команд Avito, Uber, Яндекса, Duolingo.
- Роль «CRM developer» отдельно не описана ни в одном прочитанном источнике; инжиниринг упоминается как функция внутри Zalando CRM и как партнёр у Avito/Uber.
- Вакансии не дают данных о подчинении и обороте людей; зарплатные вилки приведены только как справка.
