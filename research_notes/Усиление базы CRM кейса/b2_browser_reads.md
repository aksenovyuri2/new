# B2: чтение закрытых для curl страниц через браузер (очередь R6–R10, вкладка tab-2)

Дата проверки: 2026-10-01. Инструмент: встроенный браузер mcp__Claude_Browser__ (одна своя вкладка tab-2; navigate + javascript_tool; для страниц одного домена после загрузки читал соседние через fetch внутри вкладки: ст. 44.1 ФЗ «О связи», патенты на patents.google.com, посты t.me). Только чтение: без входа, форм и обходов защиты. Порядок: R8, R6, R7, R9, R10. PDF-ссылки (Braze, Магнит, SSRN, USPTO) не открывал, чтобы не запускать скачивание; для патентов и arXiv читал HTML-аналоги. В очереди URL TAdviser (строка 2) обрезан без закрывающей скобки; в таблице и статусе дан рабочий вариант со скобкой.

## Сводка

Итого по 50 ссылкам: существует 37, отсутствует 0, заблокировано 13. Извлечено: да 21, частично 15, нет 14 (успешных, то есть да или частично: 36).

Заблокировано: домены fas.gov.ru (5 страниц), rkn.gov.ru и 23.rkn.gov.ru (2), rshb.ru (1) браузер отклонил («navigation denied or failed»); openreview.net (проверка браузера) и papers.ssrn.com (Cloudflare) отдали проверку, не обходил; rbc.ru отдал пустую страницу; два PDF (Braze, Магнит) не открывал по своему решению. Статус «exists» у трёх патентных PDF USPTO означает: патент существует и прочитан на patents.google.com, сам PDF не открывался.

Главные подтверждённые факты:
- Pega CDH: приоритет = P × C × V × L (склонность × вес контекста × ценность действия × бизнес-рычаги); стартовая склонность 0.5, предсказания обновляются раз в час, Thompson sampling добавляет шум при малом числе ответов.
- Патент Microsoft/LinkedIn US12536414B2 (выдан 2026-01-27): отправлять уведомление, если ΔPr = Pr(визит | уведомление) − Pr(визит | без уведомления) выше порога; окно w = 1 или 7 дней.
- Патент Adobe US12229804B2 (выдан 2025-02-18): групповая выпуклая оптимизация частоты при заданном допуске отписок; допуск вроде «ниже 20%» или «10–20%».
- ShareChat, post-stratification (arXiv 2606.04110, 02.06.2026): снижение дисперсии 99.3% против 47.62% у CUPED подтверждено; но Type-I error 6.1% на 40+ боевых тестах; MDE при 10% трафика с ~136% до ~10%.
- Лента + CM Ocean Optimum: 3 месяца до промышленной эксплуатации, ЛИП (CBC), 8 млн клиентов, цикл не более 10 минут. Магнит Доставка: 4 → 13 месяцев подтверждено по датам (сентябрь 2021 — октябрь 2022), CRM 12% → 20%, доставляемость пушей 60% → 98%.
- Право: ст. 44.1-1 ФЗ «О связи» (массовые вызовы, введена 41-ФЗ от 01.04.2025); п. 1.1 ст. 44.1 (отказ от рассылки через оператора, тот же 41-ФЗ); с 01.03.2027 новая редакция по ФЗ от 26.06.2026 N 210-ФЗ; разъяснения ФАС (Приказ N 410/24): согласие должно однозначно идентифицировать абонента, бремя доказательства на рекламораспространителе, мессенджеры включены. Постановление N 974 не про email/push (правила для операторов рекламных данных).
- Не подтвердились: «4–6 недель и 3 месяца миграции с Emarsys» (Insider: 3 месяца = окно возврата денег); «90 дней: 2 пилота, 9 потоков, +12%» (у Branch8 такого текста нет, клиент безымянный).

## Сводная таблица

| URL | исследователь | существует | извлечено (да/частично/нет) |
|---|---|---|---|
| https://fas.gov.ru/publications/19244 | r8 | blocked | нет |
| https://fas.gov.ru/news/8016 | r8 | blocked | нет |
| https://fas.gov.ru/publications/21602 | r8 | blocked | нет |
| https://fas.gov.ru/news/33193 | r8 | blocked | нет |
| https://fas.gov.ru/publications/20057 | r8 | blocked | нет |
| https://23.rkn.gov.ru/news/news159224.htm | r8 | blocked | нет |
| https://rkn.gov.ru/press/news/news74777.htm | r8 | blocked | нет |
| https://www.rbc.ru/technology_and_media/10/02/2026/698afe729a79470c08a17b91 | r8 | blocked | нет |
| https://www.svoboda.org/a/roskomnadzor-pochti-polnostjyu-zamedlil-rabotu-telegram/33716478.html | r8 | exists | да |
| http://publication.pravo.gov.ru/document/0001202504010010 | r8 | exists | частично |
| https://www.consultant.ru/document/cons_doc_LAW_43224/b5a11e1f308ded9f4b94bf885bcf76ed577f9576/ | r8 | exists | да |
| https://www.consultant.ru/document/cons_doc_LAW_418000/ | r8 | exists | да |
| https://www.consultant.ru/document/cons_doc_LAW_482014/d54cdfade7a7dd1f49306a747e3204aa24f7ab41/ | r8 | exists | да |
| https://www.consultant.ru/law/podborki/reklama_bez_soglasiya/ | r8 | exists | частично |
| https://openreview.net/forum?id=8GH752ZJ5j | r6 | blocked | нет |
| https://help.salesforce.com/s/articleView?language=en_US&id=mktg.mc_ees_einstein_feature_overview.htm&type=5 | r6 | exists | частично |
| https://support.iterable.com/hc/en-us/articles/13102589168916-Channel-Optimization | r6 | exists | да |
| https://support.iterable.com/hc/en-us/articles/7412316462996-Optimizing-Campaign-Delivery | r6 | exists | частично |
| https://communities.sas.com/t5/SAS-Communities-Library/SAS-Customer-Intelligence-360-Decision-management-machine/ta-p/518913 | r6 | exists | частично |
| https://academy.pega.com/topic/configuring-adaptive-model/v1 | r6 | exists | да |
| https://academy.pega.com/topic/customer-decision-hub-predictions/v2 | r6 | exists | да |
| https://medium.com/@tushargoelml/near-real-time-optimization-of-notifications-at-linkedin-part-i-893dcb8eef41 | r6 | exists | частично |
| https://dl.acm.org/doi/10.1145/3219819.3219906 | r6 | exists | частично |
| https://papers.ssrn.com/sol3/Delivery.cfm/6165626.pdf?abstractid=6165626 | r6 | blocked | нет |
| https://image-ppubs.uspto.gov/dirsearch-public/print/downloadPdf/12536414 | r6 | exists | да |
| https://image-ppubs.uspto.gov/dirsearch-public/print/downloadPdf/12229804 | r6 | exists | да |
| https://image-ppubs.uspto.gov/dirsearch-public/print/downloadPdf/10516644 | r6 | exists | да |
| https://link.springer.com/chapter/10.1007/978-3-031-94544-1_15 | r7 | exists | да |
| https://arxiv.org/html/2606.04110 | r7 | exists | да |
| https://tech.instacart.com/instacarts-economics-team-using-surrogate-indices-to-estimate-long-run-heterogeneous-treatment-0bf7bc96c6e6 | r7 | exists | частично |
| https://ar5iv.labs.arxiv.org/html/2210.08338 | r7 | exists | да |
| https://habr.com/ru/companies/garage8/articles/941598/ | r7 | exists | да |
| https://arxiv.org/pdf/2510.03468 | r7 | exists | да |
| https://tech.instacart.com/bandits-for-marketing-optimization-f5a63b9bfaa7 | r7 | exists | частично |
| https://www.sostav.ru/blogs/286455/75101 | r9 | exists | да |
| https://lms.matemarketing.ru/content/conference/3 | r9 | exists | частично |
| https://mailingday.ru | r9 | exists | частично |
| https://conference.mindbox.ru/ | r9 | exists | частично |
| https://auditorium-cg.ru/crm25 | r9 | exists | частично |
| https://www.pega.com/insights/resources/pegaworld-2025-shifting-high-gear-citibanks-path-scalable-high-powered-marketing | r9 | exists | нет |
| https://www.rshb.ru/news/06082026_000001 | r10 | blocked | нет |
| https://www.tadviser.ru/index.php/%D0%9F%D1%80%D0%BE%D0%B5%D0%BA%D1%82:%D0%9B%D0%B5%D0%BD%D1%82%D0%B0_%D0%A1%D0%B5%D1%82%D1%8C_%D1%80%D0%BE%D0%B7%D0%BD%D0%B8%D1%87%D0%BD%D0%BE%D0%B9_%D1%82%D0%BE%D1%80%D0%B3%D0%BE%D0%B2%D0%BB%D0%B8_(Data_Sapience:_CM_Ocean) | r10 | exists | да |
| https://companies.rbc.ru/news/NSlD1nloc9/bank-hlyinov-i-glowbyte-vnedrili-reshenie-cm-ocean-ot-data-sapience/ | r10 | exists | частично |
| https://s203.q4cdn.com/277576744/files/doc_financials/2027/q1/BRZE-USQ_Transcript_2026-05-27.pdf | r10 | blocked | нет |
| https://www.magnit.com/upload/iblock/fd7/vcyltyz1s5yttt1dl1hn08nza0663ujq/MAGNIT_AR_2025.pdf | r10 | blocked | нет |
| https://branch8.com/posts/salesforce-marketing-cloud-to-braze-migration-guide-apac | r10 | exists | да |
| https://insiderone.com/customer-engagement-platforms/migration/ | r10 | exists | да |
| https://mindbox.ru/journal/cases/magnit-dostavka/ | r10 | exists | да |
| https://datasapience.ru/implementation-of-targeted-marketing-automation-platform | r10 | exists | да |
| https://mindbox.ru/journal/cases/inventive-retail-group/ | r10 | exists | частично |

## Подробно по ссылкам

## R8: право РФ, каналы, SMS (подвопросы 2.3, 4.3)

Примечание: домены fas.gov.ru (5 страниц) и rkn.gov.ru / 23.rkn.gov.ru (2 страницы) браузер отклонил («navigation denied or failed»); по правилу не повторял. Часть их содержания закрыта через КонсультантПлюс (см. ниже).

### 1. https://www.consultant.ru/document/cons_doc_LAW_43224/b5a11e1f308ded9f4b94bf885bcf76ed577f9576/ — ст. 44.1-1 «Массовые вызовы» ФЗ «О связи»
- Название: Статья 44.1-1. Массовые вызовы (Федеральный закон от 07.07.2003 N 126-ФЗ «О связи», ред. от 20.02.2026 по шапке КонсультантПлюс).
- Тип: закон (КонсультантПлюс). Подвопрос 4.3.
- Факты:
  - Статья введена ФЗ от 01.04.2025 N 41-ФЗ. п. 1: массовые и (или) автоматические телефонные вызовы допускаются «при условии получения предварительного согласия абонента, выраженного посредством совершения им действий, однозначно идентифицирующих этого абонента и позволяющих достоверно установить его волеизъявление»; без согласия, если заказчик (или оператор по своей инициативе) «не докажет, что такое согласие было получено» (бремя доказывания на заказчике).
  - п. 2: абонент в порядке, установленном Правительством РФ, вправе направить оператору отказ от массовых вызовов; оператор обязан прекратить вызовы. п. 3: массовые вызовы по инициативе заказчика осуществляются на основании договора с оператором абонента.
  - п. 4: вызовы с нарушением закона незаконны, кроме инициированных госорганами, подведомственными организациями, органами МСУ и иными организациями по перечню Правительства.
  - Аннотация КонсультантПлюс: «С 01.03.2027 п. 4 ст. 44.1-1 излагается в новой редакции (ФЗ от 26.06.2026 N 210-ФЗ)». Это новая дата и новый закон; прежние заметки их могли не содержать.

### 2. (бонус, прочитано через fetch из той же вкладки) https://www.consultant.ru/document/cons_doc_LAW_43224/7caf446de1e18caa61180692ea35572c94080475/ — ст. 44.1 «Рассылка по сети подвижной радиотелефонной связи»
- Тип: закон. Подвопрос 4.3 (по queue: «статьи про рассылки, даты вступления п. 1.1 ст. 44.1»).
- Факты:
  - Ст. 44.1 введена ФЗ от 21.07.2014 N 272-ФЗ. п. 1: рассылка допускается при предварительном согласии абонента, выраженном «действиями, однозначно идентифицирующими этого абонента»; рассылка признаётся без согласия, если заказчик (или оператор по своей инициативе) «не докажет, что такое согласие было получено».
  - п. 1.1 (введён ФЗ от 01.04.2025 N 41-ФЗ): абонент вправе в порядке, установленном Правительством РФ, направить оператору подвижной радиотелефонной связи отказ от получения рассылки; оператор обязан прекратить рассылку этому абоненту.
  - п. 2: рассылка по инициативе заказчика идёт на основании договора с оператором абонента. п. 3: рассылка с нарушением закона незаконна, кроме сообщений при переносе номера, обязательных для оператора, и сообщений по инициативе ФОИВ, «Роскосмоса», фондов, органов власти субъектов, МСУ, страховых медицинских организаций (ОМС); редакции 216-ФЗ от 13.07.2015 и 552-ФЗ от 28.12.2024.
  - Аннотации КонсультантПлюс: «С 01.03.2027 п. 10 дополняется ст. 44» и «п. 11 дополняется ст. 44 (ФЗ от 26.06.2026 N 210-ФЗ)» (то есть к ст. 44 добавляются новые пункты с 01.03.2027).
  - Дат вступления в силу самого п. 1.1 на этой странице нет.

### 3. http://publication.pravo.gov.ru/document/0001202504010010 — ФЗ от 01.04.2025 № 41-ФЗ (официальная публикация)
- Название: «О создании государственной информационной системы противодействия правонарушениям, совершаемым с использованием информационных и коммуникационных технологий, и о внесении изменений в отдельные законодательные акты Российской Федерации». Номер опубликования 0001202504010010, дата опубликования 01.04.2025.
- Тип: закон (официальный портал). Подвопрос 4.3.
- Извлечено частично: текст закона отдан постранично картинками (44 страницы), текстового слоя нет; заголовок, дату и номер подтвердил. Даты вступления в силу п. 1.1 ст. 44.1 в тексте страницы нет (смотреть вручную).

### 4. https://www.consultant.ru/document/cons_doc_LAW_418000/ — Постановление Правительства РФ от 28.05.2022 N 974 (ред. от 18.09.2025)
- Название: «Об утверждении Правил взаимодействия Роскомнадзора с операторами рекламных данных, включая порядок, формат и сроки предоставления ... информации о распространенных в сети "Интернет" рекламе и (или) социальной рекламе». Срок действия ограничен 1 сентября 2028 года. Редакции: Постановления от 20.12.2022 N 2355, от 28.05.2025 N 743, от 18.09.2025 N 1427.
- Тип: подзаконный акт. Подвопрос 4.3.
- Вывод: это правила передачи данных ОРД (ЕРИР, маркировка интернет-рекламы), в тексте Правил (около 16 тыс. знаков) нет слов «электронная почта», «push», «мессенджер», «SMS», «рассылка», «сети электросвязи» (0 совпадений). Норм об исключениях для email/push в нём нет; гипотезу «974 содержит исключения для email/push» отклоняю. Исключения для интернет-рекламы смотреть в ст. 18.1 38-ФЗ.

### 5. https://www.consultant.ru/document/cons_doc_LAW_482014/d54cdfade7a7dd1f49306a747e3204aa24f7ab41/ — раздел VII Руководства ФАС по обязательным требованиям в рекламе
- Название: «VII. О распространении рекламы по сетям электросвязи», из Приказа ФАС России от 20.06.2024 N 410/24 «Об утверждении руководств по соблюдению обязательных требований в сфере рекламы».
- Тип: регулятор (позиция ФАС в форме руководства). Подвопрос 4.3.
- Факты:
  - Требование ч. 1, 2 ст. 18 38-ФЗ распространяется «на всю без исключения рекламу, распространяемую по сетям электросвязи», в том числе на WhatsApp и Viber и иные приложения, передающие информацию по сетям электросвязи; разработчики мессенджеров рекламораспространителями только из-за этого не признаются.
  - Согласие абонента должно позволять «однозначно идентифицировать» абонента; «простое заполнение бланка (формы), не позволяющее однозначно установить и подтвердить, кто именно заполнил такую форму, не является соблюдением данного требования». Рассылка без согласия, если заказчик «не докажет, что такое согласие было получено» (ч. 1 ст. 44.1 ФЗ «О связи»).
  - Место правонарушения определяется по субъекту, которому выделен диапазон номера (реестр opendata.digital.gov.ru/registry/numeric). При рассылках с «коротких» и «буквенных» номеров оператор абонента может быть признан рекламораспространителем (ч. 7 ст. 38 38-ФЗ). Непредставление сведений ФАС — ч. 6 ст. 19.8 КоАП.
  - Telegram: в режиме мессенджера (обмен сообщениями с конкретными пользователями) реклама не подпадает под ст. 18.1 38-ФЗ (маркировка), но подпадает ч. 1 ст. 18; Telegram-каналы (широкий круг) рассматриваются как реклама в сети «Интернет» и подпадают под ст. 18.1 (ч. 16: пометка «реклама» и указание рекламодателя).
  - Суммы штрафов на этой странице нет.

### 6. https://www.consultant.ru/law/podborki/reklama_bez_soglasiya/ — подборка «Реклама без согласия» (2026-2025-2024)
- Название: Реклама без согласия \ 2026-2025-2024 год \ КонсультантПлюс. Тип: подборка (закон, практика, статьи). Подвопрос 4.3.
- Факты:
  - 38-ФЗ «О рекламе» указан в ред. от 26.07.2026. ч. 1 ст. 18: реклама по сетям электросвязи допускается «только при условии предварительного согласия абонента или адресата»; признаётся распространённой без согласия, если рекламораспространитель «не докажет, что такое согласие было получено»; рекламораспространитель обязан немедленно прекратить рассылку по требованию.
  - Судебная практика 2025 по ст. 14.3 КоАП: согласие «должно четко содержать волеизъявление конкретного абонента на получение рекламы от конкретного рекламораспространителя и должно быть зафиксировано»; без доказательств реклама признаётся распространённой без согласия.
  - Статья «Практическая бухгалтерия» 2023, N 10: ФАС узнаёт о нарушении по обращениям абонентов, возбуждение дела по иным основаниям маловероятно. Суммы штрафов на странице не названы. Подборка без полного текста судебных актов (нужна регистрация).

### 7. https://www.svoboda.org/a/roskomnadzor-pochti-polnostjyu-zamedlil-rabotu-telegram/33716478.html — «Роскомнадзор почти полностью замедлил работу Telegram»
- Дата: 2026-03-25 20:14 МСК. Тип: СМИ (Радио Свобода, ссылка на проект OONI и «Агентство»). Подвопрос 4.3.
- Факты: по тестам OONI на утро 25 марта уровень аномалий (признаков блокировки) Telegram достигает 74%; максимум 1317 аномалий зафиксирован в воскресенье 22 марта (78%); сопоставимо с замедлением Signal и WhatsApp (около 87% аномалий по выходным). Без VPN мессенджеры у россиян не открываются. РБК, The Bell и Baza сообщали о планах «тотальной блокировки» Telegram к апрелю. Минцифры сообщили, что Telegram не будут блокировать для военных «в зоне СВО».

### 8. https://www.rbc.ru/technology_and_media/10/02/2026/698afe729a79470c08a17b91 — РБК, заявление РКН о Telegram (10.02.2026 по URL)
- Статус: blocked (страница загрузилась пустой: title и текст пусты). Не извлечено.

## R6: формулы и механика решений (подвопросы 1.1, 1.2, 1.4)

### 1. https://openreview.net/forum?id=8GH752ZJ5j — BUOPLR (Kuaishou, ICML 2026)
- Статус: blocked. Страница «Verifying your browser | OpenReview» (проверка браузера, предлагает войти). Обход не пытался. Не извлечено. Идёт в «Посмотреть вручную».

### 2. Salesforce Help: Einstein for Marketing Cloud Engagement Feature Overview and Requirements
- URL: https://help.salesforce.com/s/articleView?id=mktg.mc_ees_einstein_feature_overview.htm&type=5 (copyright 2026, дата редакции не показана). Тип: документация вендора. Подвопросы 1.1, 1.2, 1.4.
- Факты:
  - Пороги по истории вовлечения для функций Einstein: минимум 7 дней, рекомендуется 28, оптимально 90 («Threshold / Days of Historical Data: Minimum 7, Recommended 28, Optimal 90»).
  - Einstein Engagement Scoring «predicts consumer engagement with email and mobile push messaging», выдаёт баллы вероятности вовлечения контакта (Smart Segmentation).
  - Einstein Send Time Optimization (STO) определяет лучшее время отправки email или push; Einstein Engagement Frequency «evaluates your contacts and identifies the optimal number of email messages or push notifications to send», цель: избежать как недостатка, так и «burnout from too many messages» (Smart Orchestration).
  - Доступность: Messaging and Journeys (Professional как add-on, Corporate, Enterprise, Enterprise+), Account Engagement (Advanced, Premium), CDP зависит от редакции M&J.
  - Не найдено на этой странице: классы насыщенности, минимальные объёмы для Engagement Frequency, окно STO, связка с Journey Builder (это отдельные статьи; в оглавлении страницы их нет, ссылки на подстраницы EF и STO не найдены). Идёт в «Посмотреть вручную».

### 3. Iterable: Channel Optimization
- URL: https://support.iterable.com/hc/en-us/articles/13102589168916-Channel-Optimization. Тип: документация вендора (дата не показана). Подвопрос 1.2.
- Факты:
  - Механика: при входе пользователя в плитку Channel Optimization Iterable «analyzes their historical data and sends the message to the channel it determines they're most likely to engage with»; данные анализируются еженедельно («on a weekly basis»).
  - Минимум данных: проект должен иметь не менее трёх месяцев кампаний и не менее двух активных каналов; поддерживаются email, SMS, push.
  - Пока данных мало, отправка идёт «using a randomized algorithm, not the fallback settings»; fallback-порядок каналов применяется, когда данные пользователя неубедительны (сопоставимая частота взаимодействия по каналам) или неполны (например, нет адреса email); новый пользователь в зрелом проекте получает рассылку по fallback, пока истории не хватит.
  - Не поддерживается для transactional, blast и триггерных кампаний вне journey, а также с Send Time Optimization. Поддерживает Rate limiting и Quiet Hours. Отписки учитываются платформой автоматически. Определение «вовлечения» в тексте не дано.

### 4. Iterable: Optimizing Campaign Delivery
- URL: https://support.iterable.com/hc/en-us/articles/7412316462996-Optimizing-Campaign-Delivery. Тип: документация вендора. Подвопрос 1.2.
- Факты:
  - STO (email, push): включается, если проекту хватает исторических данных; пользователю задаётся окно завершения отправки 6–24 часа («enter a number of hours (between 6 and 24) by which the send must complete»); после старта отключить STO нельзя.
  - Quiet Hours: для SMS включены по умолчанию, окно 20:00–09:00 каждый день в локальном времени получателя; для остальных каналов выключены.
  - Frequency capping (email, push, SMS): действует по настройкам Frequency Management проекта; для transactional не применяется; кампания может быть выведена из-под лимита.
  - Вес свежих данных и запасной вариант STO в этой статье не описаны (отдельная статья Send Time Optimization).

### 5. SAS Customer Intelligence 360: Decision management, machine learning...
- URL: https://communities.sas.com/t5/SAS-Communities-Library/SAS-Customer-Intelligence-360-Decision-management-machine/ta-p/518913. Тип: блог вендора (SAS Communities Library, дата не извлечена). Подвопрос 1.2.
- Факты: слой decisioning включает «real-time event processing with contextual data», «contact policies and offer eligibility», ускоренное развёртывание моделей и управление моделями. Решение выбирает только одно лучшее предложение из возможных «depending on the individual's propensity to buy». Бизнес-правила имеют приоритет над скором (пример: клиент младше порога возраста не получает рекламу независимо от propensity). Формулы приоритета, арбитража между кампаниями и параметров контактных политик в статье нет.

### 6. Pega Academy: Configuring an adaptive model (v1)
- URL: https://academy.pega.com/topic/configuring-adaptive-model/v1. Тип: документация вендора (©2026; версия v1 с пометкой «Verify the version tags»). Подвопросы 1.2, 1.4.
- Факты:
  - Формула арбитража: «propensity (P), context weighting (C), action value (V), and business levers (L) ... plugged into a simple formula, P * C * V * L»; результат — prioritization value для выбора топ-действий.
  - Склонность считает адаптивная модель (самообучающаяся); стартовая склонность любого действия 0.5 («the same as the flip of a coin»); после показа без клика она падает: Standard Card с 0.5 до 0.25. Для сглаживания используется Thompson sampling: при малом числе ответов добавляется много шума, с ростом числа ответов шум уменьшается.
  - Исходы: Clicked = позитив, NoResponse (нет клика за срок ожидания) = негатив. Параметр «model update frequency» = число накопленных ответов до обновления модели; значения по умолчанию рекомендуется менять только опытному аналитику. Конкретного минимального числа ответов для старта на странице нет.

### 7. Pega Academy: Customer Decision Hub predictions (v2)
- URL: https://academy.pega.com/topic/customer-decision-hub-predictions/v2. Тип: документация вендора. Подвопросы 1.2, 1.4.
- Факты: предсказания CDH используют адаптивные модели, которые «learn from customer responses and receive automatic updates every hour». Предустановленные предсказания: Predict Web Propensity (клик по баннеру), Outbound Email Propensity (клик по ссылке в письме), Predict Inbound CallCenter Propensity. Ярлыки ответа «Clicked» и «NoResponse», NoResponse фиксируется после таймаута, который можно запускать при решении или при просмотре предложения (чтобы не ловить ложные негативы). Решение: «business rules, interaction context, and propensity». Терминов «насыщенность» или «усталость» (fatigue/saturation) на странице нет.

### 8. Medium (Tushar Goel): Near Real-Time Optimization of Notifications at LinkedIn, Part I
- URL: https://medium.com/@tushargoelml/near-real-time-optimization-of-notifications-at-linkedin-part-i-893dcb8eef41. Дата: 8 апреля 2022. Тип: статья-пересказ (источник — KDD 2018 «Near real-time optimization of activity-based notifications»). Подвопрос 1.4 (фон).
- Факты: отключение уведомлений («disablement») названо дорогим: плохой опыт и потеря канала; из-за сложности моделирования его вводят как ограничение. Решение в три шага: кандидаты-получатели, модели отклика (логистическая регрессия с L2: pClickPush и pClickInApp), оптимизация выбора. Метрики моделей: AUC и O/E ratio (положительные примеры / сумма предсказанных вероятностей). Порог на члена и связь с объёмом в Части I не раскрыты (отсылка на Часть II).

### 9. ACM DL: Notification Volume Control and Optimization System at Pinterest
- URL: https://dl.acm.org/doi/10.1145/3219819.3219906. Авторы: Bo Zhao, Koichiro Narita, Burkay Orten, John Egan; KDD '18, стр. 1012–1020; опубликовано 19 июля 2018. Тип: научная статья (открытый доступ). Подвопрос 1.4 (фон).
- Факты (из аннотации): «decide notification volume for each user such that long term user engagement is optimized»; система запущена в проде Pinterest в середине 2017 и «significantly reduced notification volume and improved CTR of notifications and site engagement metrics» по сравнению с прежним ML-подходом. Полный текст (формулы приращённой ценности за неделю) не читал: PDF не открывал.

### 10. SSRN 6165626 (Baek, Chen, Ma, Mitrofanov)
- URL: https://papers.ssrn.com/sol3/Delivery.cfm/6165626.pdf?abstractid=6165626. Статус: blocked: страница abstract_id=6165626 отдала проверку Cloudflare («Just a moment...»); PDF-ссылку не открывал (скачивание). Дата, версия, статус публикации не получены.

### 11. US12536414B2 «Notification management and channel selection» (через patents.google.com; PDF USPTO не открывал)
- URL запроса: https://image-ppubs.uspto.gov/dirsearch-public/print/downloadPdf/12536414; факты с https://patents.google.com/patent/US12536414B2/en (fetch в той же вкладке). Тип: патент.
- Правообладатель Microsoft Technology Licensing LLC (LinkedIn); изобретатели Guangyu Yang, Wensheng Sun, Jiaxi Xu, Xianen Qiu, Yiping Yuan. Подана 2022-06-23 (заявка US 17/847,886), выдана 2026-01-27. Подвопрос 1.2.
- Формула: решение об отправке по двум вероятностям. Pr(T_i ≤ w | z_i, m) — вероятность визита участника i в течение окна w при отправке уведомления сейчас; Pr(T_i ≤ w | z_i, not m) — вероятность визита без уведомления. «The greater the difference between the first probability and the second probability, the greater the motivation to issue a notification»; при нескольких типах j: ΔPr(T_i ≤ w | z_i, m_j) = Pr(T_i ≤ w | z_i, m_j) − Pr(T_i ≤ w | z_i, not m_j). Окно w: «7 if it is desired to boost weekly active members or 1 ... daily active members».
- Порог: «calculating a difference between the first probability and the second probability, and sending the notification when the difference is greater than a predetermined threshold value»; при отказе уведомление возвращается в очередь («requeuing»). Вероятности считаются по нескольким каналам: in-app, mobile push, email.
- Модель: три нейросети (эмбеддинг участника; два параметра распределения Вейбулла), обучение с цензурированием справа (бит censor) для устранения смещения в «time-to-visit»; предыдущая версия — Weibull AFT Survival Regression (pVisit).

### 12. US12229804B2 «Multi-objective electronic communication frequency optimization» (через patents.google.com)
- Факты с https://patents.google.com/patent/US12229804B2/en. Тип: патент. Подвопросы 1.2, 1.4.
- Правообладатель Adobe Inc; изобретатели Lei Zhang, Lijun Yu, Jun He, Zhenyu Yan, Wuyang Dai. Приоритет 2021-07-02 (заявка US 17/366,910), выдан 2025-02-18.
- Суть: оптимизатор частоты балансирует цели кампании (открытия, клики, конверсии, взвешенная сумма, open rate, click rate; 6 целей) и допустимый уровень отписок. Claim 1: цель «maximize an amount of electronic communications opened»; вход «opt-out rate tolerance»; групповая оптимизация частоты «determined convexly» с ограничением по откликам на письма (релевантность тем писем и тел писем); индивидуальная частота = групповая оптимизация, применённая к прежней частоте человека; пересчёт при изменении цели.
- Числа из описания: допуск отписок задаётся как порог, например «below 20%, or between 10-20%», либо «5% or 10%»; ожидаемый уровень отписок = текущий уровень отписок × коэффициент допуска (opt-out tolerance ratio). Получатели кластеризуются по прошлым действиям, чтобы не оптимизировать миллионы получателей напрямую. Постановка: выпуклая оптимизация min f0(x) при f_i(x) ≤ b_i (уравнение 11 в патенте).

### 13. US10516644 «Near real time relevance ranker for notifications» (через patents.google.com)
- Факты с https://patents.google.com/patent/US10516644/en. Тип: патент. Подвопрос 1.2 (фон).
- Правообладатель Microsoft Technology Licensing LLC (LinkedIn); изобретатели Changji Shi, Zhongen Tao, Jinyun Yan, Yan Gao, Shaunak Chatterjee, Sandor Nyako. Подана 2018-04-30 (заявка US 15/966,567), выдан 2019-12-24.
- Claim 1: по потоку уведомлений от разных продюсеров (у каждого свой «first pass ranker» с предварительными оценками) онлайн извлекаются признаки реального времени, ML-модель считает оценку релевантности; затем берётся «personalized threshold calculated for the subject member profile based on previously obtained signals with respect to engagement ... with previously delivered notifications»; уведомление доставляется, если оценка релевантности сравнивается с персональным порогом положительно. Формулы самого порога в claim нет.

## R7: измерение (подвопросы 2.1, 2.2, 2.4)

### 1. Springer: «Metrics for Experimentation Programs: Categories, Benefits and Challenges»
- URL: https://link.springer.com/chapter/10.1007/978-3-031-94544-1_15. Авторы: Nils Stotz, Paul Drews (Leuphana University Lüneburg). Конференция XP 2025 (Agile Processes in Software Engineering and Extreme Programming, LNBIP vol. 545), стр. 210–225, First Online 29 мая 2025, open access, DOI 10.1007/978-3-031-94544-1_15. Тип: научная статья. Подвопрос 2.1.
- Факты:
  - 18 программных метрик в шести доменах: Volume, Outcome-Based, Quality, Engagement, Process Efficiency, Strategic Alignment (в тексте шестой домен также назван Meta-Metrics). Основа: интервью с 48 практиками экспериментирования.
  - Volume (3): число экспериментов на команду или организацию; breadth and depth (число команд и число экспериментов на команду); experiment creation velocity. Outcome-Based (5): revenue generated; CLV; avoided losses; uplift по KPI; доля успешных или заключительных (conclusive) экспериментов. Quality (3): качество гипотез; proper sample sizes; adherence to power calculations.
  - Process Efficiency: «Time to insights measures the duration from experiment setup to actionable results»; ease of use. Meta-Metrics: «percentage of business decisions influenced by experimentation»; «ratio of validated changes to total changes».
  - Ограничения: выборка 48 практиков; метрики вроде доли решений под влиянием экспериментов сложно измерить в менее «data-driven» организациях; предостережение: метрики throughput полезны для масштаба, но нельзя переоценивать количество в ущерб качеству. Строгого определения «coverage» в тексте главы не нашёл (в аннотации названа «experimentation coverage»).

### 2. arXiv 2606.04110: «Variance Reduction for Heavy-Tailed Monetization Metrics in Ranking Experiments via Post-Stratification»
- URL: https://arxiv.org/html/2606.04110. Версия v1, 02 июня 2026, cs.LG. Авторы: Neeti Pokharna (ShareChat), Olivier Jeunen (Aampe), Yatharth Saraf (ShareChat), Aleksei Ustimenko (Simulacra Research). Тип: научная статья. Подвопрос 2.2.
- Факты (подтверждены по таблицам):
  - Таблица 1 (GMV; Var. Reduction | Med. rel. Z | Type-I Error): Raw GMV: -, -, 1.0%; CUPED-adjusted: 47.62%, 1.10, 2.6%; Post-strat (winsorized): 99.3%, 1.35, 6.1%; Post-strat (raw tails): 99.7%, 1.36, 6.1%. Число 99,3% и 47,62% подтверждены; «45% меньше трафика» стоит в аннотации; в тексте также «reliable decisions using 40–50% less traffic» и средний time-to-decision снижен примерно на 50%.
  - Таблица 2, чувствительность к порогу хвоста (Threshold | Var. Reduction | Median n_tail): 99.9%ile: 95.2%, 500; 99.95%ile: 97.8%, 250; 99.99%ile: 99.3%, 100; 99.995%ile: 99.7%, 50. Выбросы <0.01% пользователей доминируют в дисперсии.
  - MDE при 10% трафика: с ~136% от среднего (raw GMV) до ~10% (после пост-стратификации).
  - Оговорка: 6.1% Type-I Error по 40+ боевым A/B-тестам выше номинала (в симуляции A/A 0%); метод не рекомендуется для экспериментов, нацеленных на «хвост» (например, VIP-функции); пороги страт фиксируют до анализа, есть мониторинг «stratum drift» и минимальный размер страты.

### 3. Instacart: «Using Surrogate Indices to Estimate Long-Run Heterogeneous Treatment Effects of Membership Incentives»
- URL: https://tech.instacart.com/instacarts-economics-team-using-surrogate-indices-to-estimate-long-run-heterogeneous-treatment-0bf7bc96c6e6. Автор Levi Boxell, 27 августа 2024. Тип: компания (инженерный блог). Подвопрос 2.2.
- Факты (раздел Backtesting): основной тест = сравнение средних эффектов (ATE) на реальных долгосрочных исходах из библиотеки старых экспериментов с ATE по суррогатному индексу; равенство эффектов «equivalent to jointly testing the surrogate index assumptions». Оговорка: бэктест возможен только на среднесрочных исходах («Medium-run vs. long-run»), риск, что индекс хорош для среднего срока и плох для долгого; поэтому применена полупараметрическая модель (ретеншн × прибыль на удержанного клиента, экстраполяция по малому числу параметров). Для CATE бэктест повторяют по сегментам до воздействия. Итог: «significant improvements in overall ATE accuracy, even larger improvements in CATE accuracy for individual segments» относительно простых одномерных методов; числовых значений точности в тексте нет (они на рисунках).

### 4. ar5iv 2210.08338: «Fair Effect Attribution in Parallel Online Experiments»
- URL: https://ar5iv.labs.arxiv.org/html/2210.08338. Авторы: Alexander Buchholz, Vito Bellini, Giuseppe Di Benedetto, Yannik Stein, Matteo Ruffini, Fabian Moerchen (Amazon Music ML); ACM 2022. Тип: научная статья. Подвопрос 2.2.
- Факты:
  - Стоимость коалиции v(S) = μ_S − μ_0 (эффект над базовой группой). Взвешенная доля Шепли (ур. 4): Δ̃_l = Σ_{T∈P(L)} P(T)·φ_l^T(v), где φ_l^T(v) — значение Шепли, ограниченное коалициями до T, P(T) — доля трафика в комбинации T; бюджетно сбалансирована, наследует свойство нулевого игрока.
  - Альтернатива, средняя доля (ур. 5): Δ_l = Σ_T [μ_T − μ_0] · P(T) · 1{l∈T} / |T|; бюджет сбалансирован, но нулевые игроки не обязательно игнорируются.
  - Таблица 2 (Amazon Music, lift %, в скобках 95% ДИ): Average cost: Exp.0 −0.59 (−1.35, 0.21), Exp.1 −0.24 (−0.97, 0.64), Exp.2 −0.44 (−1.26, 0.32). Marginal impact: −1.33 (−3.56, 1.20), −0.87 (−3.12, 1.85), −1.28 (−3.56, 1.31). Shapley cost: Exp.0 −10.19 (−12.31, −7.90), Exp.1 +7.93 (4.45, 10.97), Exp.2 +0.99 (−1.41, 2.78). Значимы только оценки Шепли для Exp.0 и Exp.1.
  - Условный вариант через CATE для подгрупп; будущая работа: приближённый Шепли и пропуски, если не все комбинации экспериментов случились.

### 5. Habr (Garage 8): «Нормально делай — нормально будет: как создавать CRM-коммуникации на миллионы пользователей без ошибок»
- URL: https://habr.com/ru/companies/garage8/articles/941598/. Дата публикации 2025-08-28 (по метаданным). Тип: компания (корпоративный блог). Подвопрос 2.1.
- Факты:
  - Бенчмарки подготовки (полный цикл от обсуждения до отправки): срочная коммуникация (письмо, пуш, баннер) — 3 часа; новый триггер (1 письмо + 1 пуш) — 2 дня; переработка существующего сценария (3 письма + баннеры + пересборка логики) — 4 дня; промо нового предложения (5 писем, 10 пушей, 5 баннеров, креативы в приложении) — 5 дней; крупная мультиканальная кампания (15 писем, 20 пушей, 10 баннеров, креативы в приложении) — 2 недели.
  - Шаблон установочной встречи PBR (участники: CRM-маркетолог, копирайтер, дизайнер, заказчик). Вопросы: зачем пишем и какой результат хотим; кому интересно; «Какой метрикой будем мерить успех?»; требования к тексту и дизайну; дедлайны. Результат: офферы, посылы, CTA; каналы; механика (триггеры, отложенные и повторные касания); сегменты; участники и зоны ответственности; сроки; дата запуска. Отдельного поля «метрика успеха» в шаблоне нет, это один из вопросов встречи.
  - Контекст: промо ушло в 8 стран на 13 языках; рекомендация не тратить час на правку, которая даёт эффект порядка 0.1%.

### 6. arXiv 2510.03468: «Improving Sensitivity in A/B Tests: Integrating CUPED with Trimmed Mean Techniques»
- URL запроса: https://arxiv.org/pdf/2510.03468; прочитана HTML-версия https://arxiv.org/html/2510.03468 (PDF не открывал). v1, 03 октября 2025, stat.ME. Авторы: Kevin Charette, Tristan Boudreault (Shopify). Тип: научная статья. Подвопрос 2.2.
- Факты (Таблица 2, мощность %, ρ_s = 0.25: без CUPED / с CUPED; ρ_s = 0.95: без / с): Normal: Welch 8.50 / 8.70 / 8.48 / 43.11; Yuen 8.43 / 8.70 / 8.46 / 42.67. Lognormal: Welch 4.46 / 4.41 / 4.35 / 6.47; Yuen 64.66 / 64.94 / 64.92 / 99.34. Zero-inflated lognormal: Welch 3.89 / 3.80 / 3.82 / 5.24; Yuen 28.58 / 28.62 / 28.66 / 66.39.; порядок в каждой строке: ρ_s=0.25 без CUPED / с CUPED, затем ρ_s=0.95 без CUPED / с CUPED.
- Таблица 1 (эффект: нетримм. / 1% тримм.): Normal .250/.250; Lognormal .250/.066; Zero inflated lognormal .250/.024. Вывод авторов: выигрыш CUPED заметен только при высокой корреляции (ρ_s = 0.95), при 0.25 почти нулевой; тримминг почти не снижает мощность при нормальных данных.

### 7. Instacart: «Bandits for Marketing Optimization»
- URL: https://tech.instacart.com/bandits-for-marketing-optimization-f5a63b9bfaa7. Автор Tilman Drerup, 26 июня 2024. Тип: компания (блог). Подвопрос 2.1.
- Факты: цель бюджета Objective := Return − Cost; «performance curve» связывает действие (например, целевую CPA) с объективом; наблюдательные данные смещены (праздники, ставки конкурентов), поэтому нужны адаптивные эксперименты со случайными возмущениями. Цикл из двух шагов: (1) моделирование кривых байесовской параметрической моделью с ограничением «кривая стартует с нуля при нулевых расходах»; оценка IPW-регрессией (inverse-propensity-weighted) с учётом пропенситетов действий; (2) explore-exploit алгоритм выбирает следующее действие по кампании. Конкретных числовых метрик результатов в доступной части нет.

## R9: оргмодель и арбитраж (подвопросы 1.3, 3.1–3.3)

### 1. https://www.sostav.ru/blogs/286455/75101 — «Топ телеграм-каналов о лояльности, CRM и клиентском опыте для маркетологов»
- Блог «Лояльно говоря» на Sostav, дата «21 Янв» (год на странице не указан), чтение 7 мин. Тип: статья-подборка. Подвопросы 1.3, 3.1–3.3.
- Факты:
  - На странице 15 ссылок t.me (порядок как в тексте подборки): cx_quality, b2b_marketing_ru, yesemailme (чат CRM Marketing & Retention), cx_lab, MediaNation, loytalk («Лояльно говоря», проект Set Loyalty), crmlove (студия CRMLOVE), cmo4cmo (CMO Talks), b2b_agora, retention_marketing («Retention Expert», WIM.Agency), helpfulmarketing (Mindbox Журнал), crm_forever (Юрий Николаев, директор по продажам Bitrix24), vforvalue (Виктор Крылов, директор по продукту CDP Билайна, ex-директор по маркетингу Самоката: клиентоцентричность, CDP, CVM), psy_loyalty (Екатерина Пронина), GalinaKurtygina (Галина Куртыгина, операционный директор Profitbase и директор по клиентскому сервису ГК Artsofte). Соответствие имени канала описанию проверено по порядку; название подтверждено только у vforvalue.
  - Скан через t.me/s/<канал>?q=<слово> (работает из браузера): по «RACI», «контактная политика», «вертикал», «арбитраж» совпадений в vforvalue, loytalk, crmlove, crm_forever, psy_loyalty нет; в retention_marketing два нерелевантных поста.
  - Найдено по теме оргмодели: https://t.me/vforvalue/11 (2024-09-07, В. Крылов, «CVM ≠ CRM»): для полноценного CVM «требуется перекроить оргструктуру», нужно объединить «Продукт, создающий ценность, и маркетинг»; автор ставит вопрос, где структурно должен находиться CRM-маркетинг (текст в извлечении оборван). Также https://t.me/vforvalue/18 (2024-09-26, лонгрид «Правильная стратегия CVM/CRM» на telegra.ph, не открывал); https://t.me/loytalk/69 (2025-09-01): исследование Direct Service, 12 интервью с экспертами топ-ритейла: «CVM не то же самое, что CRM», подходит не всем, есть барьеры и драйверы (полный отчёт по ссылке, не открывал); https://t.me/crmlove/378 (2026-04-08): CVM против CRM; https://t.me/retention_marketing/216 (2021-10-14): «карта коммуникаций» (анонс эфира).

### 2. https://lms.matemarketing.ru/content/conference/3 — Матемаркетинг (страница-программа)
- Название: «Матемаркетинг - 2023» (88 докладов). Важно: ссылка из очереди ведёт на 2023, а не на MM'24/25/26. Тип: конференция. Подвопросы 1.3, 3.1–3.3.
- Факты:
  - Список всех конференций (lms.matemarketing.ru/content/conferences): AHA'26 (50 докладов), Матемаркетинг-2025 (120), ML и рекомендательные системы (31), Эффективность рекламных кампаний (32), A/B-тесты (67), Трек Яндекса (34), Трек Авито (44), Aha!2025 (77), Матемаркетинг-2024 (125), Aha!2024 (53), «Еком и Райдтех Яндекса на ММ'24» (6). Идентификаторы: conference/20 = Матемаркетинг-2025; conference/3 = 2023; conference/5 = 2021 (64 доклада; главные темы включают «Customer Value Maximization (CVM)»); conference/6 = 2020 (50 докладов); id для 2024 и 2026 не определён (карточки открываются кликом, href нет).
  - 2023: онлайн-день 26 октября, основная часть 9–10 ноября, Москва, Grand Ball Room; в программе доклад «Работа над удержанием в начале воронки vs в конце воронки. Плюсы и минусы на примере Самоката» (Крылов Виктор, директор по продукту, Билайн; теги CRM, Лояльность, LTV).
  - MM-2025 (conference/20): доступ «по подписке», 9990 RUB, «Подписка "Годовая"»; названия докладов видны; найдены «Использование LLM/ML для генерации и персонализации коммуникаций в CRM» (Бронский Василий, руководитель службы аналитики коммуникаций, Яндекс) и «От плейлиста до паттерна: как сегментация пользователей превращает любителя музыки в лояльного пользователя» (Арсентьева Алена, VK Музыка). Просмотрена только начальная часть списка (около 410 строк); докладов про оргмодель CRM, контактную политику, приоритеты среди просмотренных заголовков нет. Видео и слайды за подпиской. Даты MM'25 (20–21.11.2025) не подтверждал.

### 3. https://mailingday.ru — Mailing Day 2026 (редирект на mailingday.ru/2026)
- Название: «Mailing Day 2026», тема «Перезапуск CRM-маркетинга и лояльности», 5 июня, Москва, ул. Мясницкая 13с20 (м. Чистые пруды); секции «Аналитика», «Каналы и механика», «Процессы», «Технологии». Тип: конференция. Подвопросы 3.1, 3.2.
- Факты:
  - «Политика внутри корпораций: как согласовывать и защищать свои предложения» (Анатолий Гиль, CMO Бандеролька, секция «Процессы»).
  - «От перформанса к CRM: инструкция по сборке кросс-командного конвейера для лидогенерации» (Ирина Иванова, Контур; Екатерина Уракова, Контур.Банк): команда из маркетинга, CRM, продукта и бизнеса за три месяца создала 8 контентных цепочек, более 2 млн руб. выручки, стоимость привлечения клиента снижена в 2 раза.
  - «Просчёт окупаемости CRM-маркетинга, ГКГ, ЛКГ, атрибуция» (Ксения Максимова, CRM Lead Yandex GO): ГК всех механик, ГК каналов, окно атрибуции. «Мобильные пуши: процессы, ИИ, аналитика, замеры давления на аудиторию» (Александра Косорукова, Head CRM Lamoda). «Рост доли CRM-канала до 18,4% за счёт механик триггерного прогрева и гиперперсонализации» (спикеры: Виктория Ок…, …унева из Out of Cloud/Kokoc Performance, Полина Загребина из NAOS; сопоставление докладчика и темы не уточнено). AI-аналитика email-кампаний (Александр Некипелов, глава команды CRM Маркетинга, МТС Линк).
  - Программа Mailing Day 2025 (06.06.2025, Санкт-Петербург) не открывалась.

### 4. https://conference.mindbox.ru/ — Mindbox Конференция 2026
- Название: «Mindbox Конференция 2026, 23–24 октября, онлайн и в Москве». Тип: конференция вендора. Подвопросы 3.1, 3.2, 3.3.
- Факты: 23 октября треки «CRM-маркетинг» и «Реклама» (эфир и запись), офлайн-воркшопы без записи; 24 октября онлайн «Лаборатория вайбкодинга» (1000 мест); заявлено 27 докладов и воркшопов, 40+ спикеров. Доклады: «7 татуировок CRM-лида: как построить прибыльный CRM, в который поверит весь бизнес» (16:45); «Строим персональный CRM-маркетинг: 5 шагов Учи.ру, которые дали 34,7% к выручке канала в несезон» (12:15); «Как Сравни нашли денежный сегмент и увеличили выручку от рассылок этим клиентам на 20%» (12:45); «Начинаем с базы: как «Аудиомания» увеличила выручку email-канала, сократив отправки» (15:15); «×2 к ROMI реактивации. Кейс «Купера»» (16:15); «+2% инкрементальной выручки приложения: Burger King» (11:15); воркшоп «Аудит программы лояльности: как срезать затраты и не потерять клиентов». Имена спикеров в тексте страницы не выведены. Программ прошлых лет не открывал; докладов именно про оргмодель в вертикалях и приоритеты нет.

### 5. https://auditorium-cg.ru/crm25 — CRM FORCE 2025
- Название: «I Всероссийский практический Форум по развитию CRM-систем CRM FORCE 2025», 1 октября 2025, отель «Москва Красносельская», Москва; статус «Завершен»; более 60 руководителей CRM-департаментов, 18 спикеров. Тип: конференция. Подвопросы 3.1, 3.2.
- Факты:
  - Дмитрий Кривошеев (руководитель управления кросс-продаж, Т-Банк): эволюция CRM в крупнейших экосистемах, от массового охвата и базовой автоматизации к глубокой персонализации и управлению лояльности; успех строится на нативных цифровых интерфейсах, сервисах «в один клик» и разумном ИИ.
  - Светлана Мызникова (начальник управления развития отношений с клиентами, Банк «Санкт-Петербург»): участвовала в дискуссии об инновациях CRM (с Е. Озеровой, ЕВРАЗ; М. Шагдаровым, Head of CRM Купер; Н. Храмцовой, Комус); в пресс-релизе указано, что она «затронула вопрос о том, как соблюдать баланс между операционной работой и задачами по развитию» в CRM-подразделении (фраза обрывается в моём извлечении).
  - Вадим Порватов (Сбербанк): uplift-модели как оценка дополнительного эффекта самого контакта.
  - Слайдов и записей на странице нет (слова «презентации», «видео», «запись», «материалы» не найдены).

### 6. https://www.pega.com/insights/resources/pegaworld-2025-shifting-high-gear-citibanks-path-scalable-high-powered-marketing — Citibank на PegaWorld 2025
- Название: «PegaWorld 2025: Shifting into High Gear: Citibank's Path to Scalable, High-powered Marketing Operations»; видео 45:00, субтитры доступны. Тип: вендор (доклад клиента). Подвопрос 3.3.
- Факты: описание: Omni-Channel Decision Engine на Pega Customer Decision Hub помог оптимизировать тестирование креативов, управление комплаенсом и ускорить поставку между программами и стейкхолдерами; обсуждаются сложности согласования людей, процессов и технологий. Вкладка «Transcript» есть, но текст не появился (клик не раскрыл содержимое). Значение «bi monthly» не проверено, нужно смотреть видео.

## R10: запуски и результаты (подвопросы 4.1, 4.2)

### 1. https://www.rshb.ru/news/06082026_000001 — первоисточник РСХБ
- Статус: blocked (браузер отклонил навигацию на rshb.ru). Дата старта, длительность, состав первой версии, что отложено: не извлечено.

### 2. TAdviser: «Лента Сеть розничной торговли (Data Sapience: CM Ocean)»
- URL: https://www.tadviser.ru/index.php/Проект:Лента_Сеть_розничной_торговли_(Data_Sapience:_CM_Ocean). Страница есть (404 в предыдущем чтении был ложным). Дата проекта в карточке: 2025/05 — 2025/08; подрядчик GlowByte; новость GlowByte от 11 сентября 2025. Тип: компания/справочник проектов. Подвопросы 4.1, 4.2.
- Факты:
  - «от начала проекта до промышленной эксплуатации прошло 3 месяца»; полный цикл (разбиение данных, решение оптимизационных задач, склейка и запись) занимает не более 10 минут; в базе 8 млн клиентов и 15 млн коммуникаций; решение осиливает до 600 млн строк входных данных за 2,5 часа.
  - Что оптимизируется: выбор оффера из матрицы релевантных и канала (SMS, push, email) с учётом пропускной способности канала и бюджета; ограничения: эффективность предложений (модуль прогнозирования), доступность каналов, бюджет, лимиты на число коммуникаций, «контактная и продуктовая политика». Задача сводится к линейному целочисленному программированию (CBC-солвер) с прогнозами ML-моделей; сценарий оптимизации = «свод бизнес-ограничений, метрик и алгебраических выражений», запуск за минуты без технической специализации.
  - До проекта: маркетологи сами формировали входной список предложений, каждому присваивался скоринг; механизм «закрытый и сложный для интерпретации», учесть несколько ограничений было нельзя, «приоритетные предложения забивали лимиты доступных каналов, вытесняя альтернативные», прогнозные модели не использовались, UI не было.
  - Эффект: «оптимизационные сценарии показали улучшение ключевой бизнес-метрики» без числа; метрики сравнения старого и нового подхода: качество охвата и влияние на целевые метрики. Стоимость проекта не названа. Цитата GlowByte (А. Ефимов): внедрение оптимизатора — «один из финальных этапов развития CVM в части аналитики», к этому моменту должны быть оцифрованы справочная информация, контактная политика, скоры откликов.

### 3. РБК Компании: «Банк «Хлынов» и GlowByte внедрили решение CM Ocean от Data Sapience»
- URL: https://companies.rbc.ru/news/NSlD1nloc9/bank-hlyinov-i-glowbyte-vnedrili-reshenie-cm-ocean-ot-data-sapience/. Дата 25 декабря 2025 (рубрика «Разработка программного обеспечения», автор GlowByte). Тип: пресс-релиз компании (публикация на РБК). Подвопрос 4.2.
- Факты: платформа CM Ocean Batch Flow; банк «может запускать до 10 кампаний одновременно через любые каналы»; A/B-тесты «в 2 клика, а не через неделю»; цитата Екатерины Эфрос (зам. начальника управления по маркетингу): «автоматизация делает за них 80% работы. Скорость запуска кампаний выросла в 3 раза, конверсия — на 25%». Этапов и сроков проекта в тексте нет (в планах интеграция со всеми внутренними системами и B2B-коммуникации).

### 4. Braze Q1 FY2027, транскрипт (PDF)
- URL: https://s203.q4cdn.com/277576744/files/doc_financials/2027/q1/BRZE-USQ_Transcript_2026-05-27.pdf. Статус: blocked по моему решению: PDF не открывал (риск скачивания); ранее 403. Не извлечено.

### 5. Годовой отчёт «Магнит» 2025 (PDF >10 МБ)
- URL: https://www.magnit.com/upload/iblock/fd7/vcyltyz1s5yttt1dl1hn08nza0663ujq/MAGNIT_AR_2025.pdf. Статус: blocked по моему решению: PDF не открывал (скачивание, объём). Не извлечено.

### 6. Branch8: «Salesforce Marketing Cloud to Braze Migration Guide for APAC Retail»
- URL: https://branch8.com/posts/salesforce-marketing-cloud-to-braze-migration-guide-apac. Автор Matt Li, 12 июля 2026. Тип: вендор/агентство (блог, продающий услуги). Подвопрос 4.2.
- Факты:
  - «14 недель» подтверждено: «the total project ran 14 weeks from kickoff to SFMC decommissioning»; клиент не назван («the multi-brand retailer mentioned at the start»); команда: два инженера Branch8, один аналитик, три маркетолога клиента неполный день; недели 1–2 аудит и модель данных, 3–4 идентификация и дедупликация (340K дублирующих профилей в пяти бизнес-юнитах SFMC), 5–7 редизайн journey и перенос шаблонов Liquid, 8–9 интеграции, далее.
  - Рекомендация: бюджет 10–16 недель для среднего APAC-ритейла; SFMC держать в режиме чтения 90 дней (это период архива, а не «90 дней с пилотами»).
  - Формулировка «90 дней: 2 пилота, 9 потоков выведено, активация +12%» на странице не найдена (поиск по «12%», «nine», «9 » и «90-day» подтвердил только архивный срок). Именованного клиента нет, вывод: безымянный маркетинговый кейс агентства, не независимый источник.

### 7. Insider One: «Customer Engagement Platform Migration Guide»
- URL: https://insiderone.com/customer-engagement-platforms/migration/. Дата не указана. Тип: вендор. Подвопрос 4.2.
- Факты: «3 месяца» на странице это окно возврата денег («If you're not satisfied within the first three months, you can opt out and receive a full refund», программа «$0 Migration»), а не срок миграции. Фраз «4–6 недель» и слова «Emarsys» на странице нет. Единственный клиентский кейс: PERCENTIL (рост среднего чека на 10%, конверсии на 25%, конверсия у анонимных пользователей 20%), без дат. Тезис исследователя «4–6 недель до запуска и 3 месяца миграции с Emarsys» не подтверждён.

### 8. Mindbox: «Магнит Доставка получает 20% выручки из CRM-канала...»
- URL: https://mindbox.ru/journal/cases/magnit-dostavka/. Дата 8 июня 2023. Тип: вендор (кейс). Подвопрос 4.2.
- Факты:
  - Результат: доля CRM в выручке e-com 12% → 20%; доставляемость мобильных пушей 60% → 98%; click rate пушей 0,7% → 1,25%; «Срок. 1 год».
  - Интеграция началась в сентябре 2021, по плану «максимум четыре месяца», «в реальности она длилась больше года: первые механики с пушами были запущены в октябре 2022 года» (4 → 13 месяцев подтверждается по датам).
  - Причины задержки (слова экс-продакта Максима Эль-Кама): 1) разработчики без опыта интеграции (команда из 5: 2 бэкендера, QA, 2 мобильных); 2) архитектурные ошибки в ТЗ (данные брали не из Bitrix, он «чуть не лёг»); 3) не декомпозировали цель (34-страничный Google-док как одна задача); 4) устаревшие инструкции (60% информации в ТЗ устарело, пропустили новую версию API); 5) не хватало экспертизы и внимания менеджера Mindbox, нерегулярные синки, два раза менялся менеджер. Код реально писали «от силы полтора месяца».
  - Сервис уведомлений Магнита модерирует пуши, чтобы транзакционные и маркетинговые не перебивали друг друга.

### 9. Data Sapience: «Внедрение платформы автоматизации целевого маркетинга» (Финуслуги)
- URL: https://datasapience.ru/implementation-of-targeted-marketing-automation-platform. Дата публикации не указана. Тип: вендор (кейс). Подвопросы 4.1, 4.2.
- Факты: «Срок реализации: Август — декабрь 2022»; «Срок разработки до завершения этапа MVP и отправки первых коммуникаций занял всего 4 месяца. Целевое решение было внедрено за 8 месяцев»; платформа CM Ocean; до 2 млн персональных предложений создаётся и приоритизируется ежедневно, до 120 пакетных кампаний в день, покрытие клиентской базы «практически 100%». Проект начинался на решении западного вендора, смена из-за ухода западных компаний в начале 2022.
- Расхождение: период на странице (август–декабрь 2022) не совпадает ни с «12.2023–08.2024», ни с датой новости 09.2024 из заметок R10, и внутри страницы «Август — декабрь» (5 месяцев) расходится с «целевое решение за 8 месяцев». Гипотеза: 12.2023–08.2024 — другой этап или другой проект (смена платформы или Real-Time), нужно искать отдельную страницу.

### 10. Mindbox: «Inventive Retail Group сократила затраты на CRM-маркетинг в 1,5 раза...»
- URL: https://mindbox.ru/journal/cases/inventive-retail-group/. Дата публикации 29 ноября 2023. Тип: вендор (кейс). Подвопрос 4.2.
- Факты: затраты на CRM-инструменты снизились в 1,5 раза (по финансовой отчётности IRG); интеграция начата с розницы (80% клиентского потока офлайн): «Интеграция с 1С вместе с тестированием заняла три месяца», два разработчика на полный день; первым подключили restore: в начале октября 2022, к концу октября подключили Samsung, затем «по одному бренду в месяц». Для сайтов нужно было новое ТЗ на каждый. Точного числа брендов, вошедших в первые 3 месяца, в тексте нет (по описанию 2 бренда за первый месяц и далее по одному в месяц, итого порядка 4 к концу третьего месяца; это оценка, а не цитата).


## Посмотреть вручную

| Приоритет | Ссылка | Почему не прочитано | Гипотеза: зачем смотреть | Что там может быть | Подвопросы |
|---|---|---|---|---|---|
| 1 | https://fas.gov.ru/publications/19244 ; https://fas.gov.ru/publications/21602 ; https://fas.gov.ru/publications/20057 ; https://fas.gov.ru/news/8016 ; https://fas.gov.ru/news/33193 | Браузер отклонил навигацию на fas.gov.ru (5 страниц, повторы не делал) | Первоисточник позиции ФАС по согласию на SMS и мессенджеры и фактические штрафы по решениям | Дата и название решений, разъяснения по ч. 1 ст. 18 38-ФЗ, размеры штрафов по ч. 1 ст. 14.3 КоАП в конкретных делах | 4.3 |
| 1 | https://rkn.gov.ru/press/news/news74777.htm ; https://23.rkn.gov.ru/news/news159224.htm | Браузер отклонил навигацию на rkn.gov.ru и 23.rkn.gov.ru | Порядок отказа от рассылки по постановлению Правительства (№ 1137) и памятка по идентификатору рекламы | Пошаговый порядок отказа абонента через оператора, охват каналов (SMS, мессенджеры, email) | 4.3 |
| 1 | http://publication.pravo.gov.ru/document/0001202504010010 | Текст 41-ФЗ отдан постранично картинками (44 страницы), текстового слоя нет | Даты вступления в силу п. 1.1 ст. 44.1 и ст. 44.1-1 | Статья с датами вступления частей закона (на КонсультантПлюс есть только вводные примечания) | 4.3 |
| 1 | https://www.rbc.ru/technology_and_media/10/02/2026/698afe729a79470c08a17b91 | Страница загрузилась пустой (title и текст пусты, ранее 401) | Текст заявления РКН об ограничении Telegram (10.02.2026 по URL) | Формулировка, дата и перечень ограничений Telegram как канала для рассылок | 4.3 |
| 1 | https://openreview.net/forum?id=8GH752ZJ5j | Проверка браузера OpenReview («Verifying your browser»), не обходил | Полный текст BUOPLR (Kuaishou, ICML 2026) | Формулы uplift по бандлам, «скор конкурентоспособности», таблица A/B (DAU, CTR, удержание, доля отключений), абляции | 1.2, 1.4 |
| 1 | https://help.salesforce.com/s/articleView?id=mktg.mc_ees_einstein_feature_overview.htm&type=5 (оглавление «Einstein and Analytics in Marketing Cloud Engagement»: искать статьи «Einstein Engagement Frequency» и «Einstein Send Time Optimization») | Обзорная страница отдала только пороги данных (7/28/90 дней); подстраниц в оглавлении не нашёл | Классы насыщенности и минимальные объёмы данных для Engagement Frequency, окно STO, использование в Journey Builder | Пороги классов, минимальное число отправок, правила решения в Journey Builder | 1.1, 1.2, 1.4 |
| 2 | https://papers.ssrn.com/sol3/papers.cfm?abstract_id=6165626 | Cloudflare «Just a moment»; PDF-ссылку не открывал (скачивание) | Дата выпуска, версия и статус Baek, Chen, Ma, Mitrofanov | Дата, журнал или статус препринта, ограничения подхода | 1.4 |
| 2 | https://www.rshb.ru/news/06082026_000001 | Браузер отклонил навигацию на rshb.ru (в прошлом чтении ошибка сертификата) | Первоисточник РСХБ для кейса запуска | Дата старта и длительность проекта, состав первой версии, что отложено | 4.1, 4.2 |
| 2 | https://s203.q4cdn.com/277576744/files/doc_financials/2027/q1/BRZE-USQ_Transcript_2026-05-27.pdf | PDF, 403 ранее; не открывал из-за риска скачивания | Клиентские примеры Braze с датами и числами миграции | Примеры консолидации платформ с сроками и эффектом | 4.2 |
| 2 | https://www.magnit.com/upload/iblock/fd7/vcyltyz1s5yttt1dl1hn08nza0663ujq/MAGNIT_AR_2025.pdf | PDF более 10 МБ; не открывал из-за скачивания | Годовой отчёт «Магнит»: CVM, персонализация, «Магнит Плюс» | Сроки запуска, доли персональных предложений, эффект от платформы коммуникаций | 4.2 |
| 2 | https://www.pega.com/insights/resources/pegaworld-2025-shifting-high-gear-citibanks-path-scalable-high-powered-marketing | Вкладка «Transcript» есть, текст не раскрылся; видео 45:00 | Что означает «bi monthly» у Citi (дважды в месяц или раз в два месяца) и как устроены комплаенс и согласование | Фраза про частоту обзора приоритетов, роли стейкхолдеров | 3.3 |
| 2 | https://lms.matemarketing.ru/content/conferences (карточки «Матемаркетинг - 2024», «Матемаркетинг - 2025» = /content/conference/20, «AHA'26») | Видео и слайды по подписке (годовая 9990 RUB); ссылка из очереди вела на 2023; просмотрено только начало списка | Доклады про оргмодель CRM/CVM, контактную политику и приоритеты | Заголовки и аннотации докладов; записи за пейволлом | 1.3, 3.1–3.3 |
| 3 | https://mailingday.ru/2025 (адрес не проверен) | Открывалась только программа 2026; 2025 (06.06.2025, СПб) не открывал | Темы про команду CRM, согласования и нагрузку на клиента | Программа и спикеры Mailing Day 2025 | 3.1, 3.2 |
| 3 | https://t.me/vforvalue/11 и telegra.ph «Правильная стратегия CVM/CRM» (09-26) | Пост оборван в извлечении; лонгрид не открывал | Где структурно должен находиться CRM-маркетинг (в продукте или маркетинге) по Крылову | Ответ автора на вопрос о подчинении CRM, схема оргструктуры | 1.3, 3.1 |
| 3 | Отчёт Direct Service «CRM или CVM» (12 интервью с топ-ритейлом) по ссылке из https://t.me/loytalk/69 | Ссылка из поста не открывалась | Барьеры и драйверы внедрения CVM, оргмодель в ритейле | Выводы 12 интервью | 1.3, 3.1 |
| 3 | https://conference.mindbox.ru/ (раздел «История», программы прошлых лет) | Открывалась только программа 2026 | Доклады о оргмодели CRM и работе с продуктовыми командами | Прошлые программы, записи | 3.1–3.3 |
| 3 | https://dl.acm.org/doi/pdf/10.1145/3219819.3219906 | Полный текст Pinterest KDD'18 не читал (PDF) | Как оценивается приращённая ценность каждого следующего уведомления за неделю | Формулы объёма уведомлений на пользователя | 1.4 |
| 3 | https://datasapience.ru (поиск новости Финуслуг 09.2024) | На странице кейса период «август–декабрь 2022»; 12.2023–08.2024 не нашёл | Разобрать, это второй этап или другой проект | Период, состав первой версии, что отложено | 4.1, 4.2 |
| 3 | Рисунки с результатами бэктеста в https://tech.instacart.com/instacarts-economics-team-using-surrogate-indices-to-estimate-long-run-heterogeneous-treatment-0bf7bc96c6e6 | Числа точности на изображениях, текст их не содержит | Количественная точность суррогатного индекса (ATE и CATE) | Графики разницы фактических и импутированных эффектов | 2.2 |
