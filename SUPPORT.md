# 💬 Центр Поддержки и Часто Задаваемые Вопросы / RoseTime Support & FAQ

*(Select language / Выберите язык: [Русский](#русский) | [English](#english))*

---

<a name="русский"></a>
## 🇷🇺 Служба поддержки пользователей RoseTime

Если у вас возникли вопросы по работе приложения, предложения по улучшению функционала или технические сложности, наша служба поддержки готова оперативно вам помочь.

### 📬 Контакты для связи
* **Официальный Email:** [pyzhovs@icloud.com](mailto:pyzhovs@icloud.com)
* **Разработчик:** Сергей Пыжов
* **Сайт онлайн-записи:** [rosetime.app](https://rosetime.app)
* **Время ответа:** Обычно в течение 24 часов в рабочие дни.

---

### ❓ Часто задаваемые вопросы (FAQ)

#### 1. Где хранятся данные моих клиентов и выручка?
Все данные (список клиентов, история визитов, заметки и финансовая статистика) сохраняются **исключительно локально на вашем iPhone** с использованием защищенной базы данных Apple SwiftData и бесплатно реплицируются в ваш персональный Apple iCloud. Ваши данные никогда не выгружаются на сторонние серверы и не продаются третьим лицам.

#### 2. Как работает онлайн-запись 2.0 и персональная ссылка мастера?
В тарифе PRO вы можете за 1 минуту активировать персональную витрину `rosetime.app/ваше_имя`. Ссылка привязывается к вашему Apple ID. Вы выбираете, какие услуги показывать онлайн, а свободные слоты берутся строго из вашего расписания. Клиенты бронируют окна без скачивания приложений и регистрации, а заявка мгновенно приходит пуш-уведомлением на ваш iPhone.

#### 3. Как настраивается время удержания слота (Hold Time)?
В разделе «Настройки онлайн-записи» $\to$ «Время удержания слота» вы можете раздельно настроить:
* **День-в-день (сегодня):** от 15 минут до 2 часов, чтобы не упустить горящие окна при отсутствии подтверждения.
* **На будущие дни (завтра и позже):** от 1 до 24 часов, чтобы дать клиенту комфортное время на согласование визита.
Если вы не подтвердите заявку до истечения таймера, слот автоматически вернется в статус свободного.

#### 4. Защищены ли мои слоты от ботов и спамеров?
Да, на уровне Cloudflare Edge внедрен 4-уровневый защитный комплекс:
1. **Cloudflare Turnstile:** интеллектуальная верификация человека без раздражающих капч.
2. **Honeypot:** невидимые ловушки в коде страницы, мгновенно блокирующие скрипты спама.
3. **Лимит на номер телефона:** один номер не может удерживать более одной активной заявки одновременно.
4. **IP Rate Limiting:** ограничение количества запросов с одного IP-адреса.

#### 5. Как защитить доходы от клиентов на рабочем месте?
Включите функцию **«Шторка приватности» (Face ID)** в настройках Профиля. При показе экрана клиенту или сворачивании приложения финансовые цифры маскируются звездочками (`*** ₸`), и для их просмотра потребуется авторизация через Face ID, Touch ID или код-пароль iPhone.

#### 6. Как перенести приложение на новый iPhone?
При стандартном переносе данных iOS (через «Быстрое начало» или резервную копию iCloud) вся локальная база SwiftData и настройки расписания автоматически переносятся на новый iPhone. Ваша персональная ссылка онлайн-записи восстанавливается через привязанный Apple ID в один клик.

#### 7. Как полностью удалить свои данные и освободить персональную ссылку?
В приложении реализован протокол **Clean Slate**: перейдите в «Профиль» $\to$ «Правовая информация и управление данными» $\to$ нажмите **«Стереть абсолютно всё»** и подтвердите операцию через Face ID / код-пароль iPhone. Система атомарно удалит все опубликованные слоты, услуги и брони с серверов Cloudflare D1, освободит ваш адрес `rosetime.app/имя` и полностью очистит базу данных на устройстве.

#### 8. Как работает ИИ-Ассистент и безопасен ли он?
ИИ-Ассистент использует защищенный серверный шлюз и модель Google Gemini. Перед отправкой запроса номера телефонов клиентов аппаратно маскируются (`[PHONE]`), а имена клиентов обезличиваются. Никакие персональные данные клиентов не сохраняются в облаке и не используются для обучения нейросетей.

#### 9. Что делать при аварийном сбое базы данных?
Приложение оснащено системой **Store Safety Shield** — при любом сбое базы данных создается защитная копия `.corrupt_<timestamp>`. Обратитесь в службу поддержки (`pyzhovs@icloud.com`), и инженер поможет восстановить записи согласно [Регламенту восстановления (Runbook)](DATABASE_RECOVERY_RUNBOOK.md).

#### 10. Как работает голосовая диктовка и безопасен ли микрофон?
Функция голосовой диктовки в AI-Ассистенте создана специально для работы в перчатках. Микрофон активируется **строго по вашему нажатию на кнопку 🎤**. Речь расшифровывается локально через нативный Apple `Speech Framework`. Аудиозаписи никогда не сохраняются в виде файлов и не передаются в интернет.

#### 11. Что такое Apple App Clip и как клиенты видят мою ссылку?
Для клиентов на iPhone при переходе по вашей персональной ссылке или при сканировании QR-кода снизу экрана плавно выплывает нативная карточка Apple App Clip. Клиент бронирует визит за 15 секунд с автоподстановкой контактов Apple QuickType и приятным виброоткликом Taptic Engine без скачивания приложений из App Store. Для клиентов на Android и компьютерах открывается элегантный веб-виджет в фирменной эстетике Rose Gold.

#### 12. Что происходит, если два клиента бронируют один и тот же слот одновременно?
Система оснащена интеллектуальным атомарным замком базы данных Cloudflare Edge (Double-Booking Shield). Кто первый нажал «Забронировать» — тот занимает слот. Второму клиенту мгновенно показывается предупреждение «Слот уже занят или забронирован другим клиентом» с бережным сохранением уже введенного имени и телефона, предлагая выбрать соседний свободный слот в один тап. Двойная запись исключена.

---
---

<a name="english"></a>
## 🇬🇧 RoseTime User Support & Help Center

If you have questions, feedback, feature requests, or technical issues with RoseTime, we are here to assist you.

### 📬 Contact Us
* **Official Support Email:** [pyzhovs@icloud.com](mailto:pyzhovs@icloud.com)
* **Lead Developer:** Sergey Pyzhov
* **Online Booking Portal:** [rosetime.app](https://rosetime.app)
* **Response Time:** Typically within 24 hours on business days.

---

### ❓ Frequently Asked Questions (FAQ)

#### 1. Where are my client database and revenue metrics stored?
All records (client roster, appointment logs, formulas, and revenue stats) are stored **strictly on your iPhone** in an encrypted Apple SwiftData container and replicated to your personal Apple iCloud free of charge. Your business data is never uploaded to external commercial servers or sold to third parties.

#### 2. How does Online Booking 2.0 and my personal link work?
With RoseTime PRO, you can activate your branded booking portal at `rosetime.app/your_name` in under a minute. The link is bound to your Apple ID. You choose which services to offer online, while open slots are calculated directly from your real schedule. Clients book appointments without downloading apps, and you receive instant push alerts on your iPhone.

#### 3. How do I configure Slot Hold Times?
Navigate to Online Booking Settings $\to$ Slot Hold Time to customize:
* **Same-Day Bookings (Today):** from 15 minutes to 2 hours, preventing last-minute slots from being blocked indefinitely.
* **Advance Bookings (Tomorrow & beyond):** from 1 to 24 hours, giving clients ample time to finalize details.
If a request is not confirmed before expiration, the slot automatically re-opens for other clients.

#### 4. Are my open slots protected against bots and fake bookings?
Yes. Our Cloudflare Edge infrastructure enforces a 4-tier anti-spam perimeter:
1. **Cloudflare Turnstile:** Frictionless human verification without annoying image captchas.
2. **Honeypot Traps:** Invisible form inputs that instantly trap and reject automated spam scripts.
3. **Phone Number Concurrency Limit:** A single phone number cannot hold more than one active pending booking at a time.
4. **IP Rate Limiting:** Edge-level rate throttling prevents request flooding.

#### 5. How do I protect earnings from clients glancing at my screen?
Enable the **Face ID Privacy Shield** in Profile Settings. When presenting your screen or switching apps, financial figures are masked with asterisks (`*** ₸`), requiring Face ID, Touch ID, or device passcode authentication to reveal.

#### 6. How do I migrate my database to a new iPhone?
During standard Apple iOS migration (via Quick Start or iCloud backup), your entire SwiftData database and schedules transfer automatically. Your personal online booking link restores seamlessly via your Apple ID in one tap.

#### 7. How do I erase all data and release my personal link?
RoseTime features the **Clean Slate Protocol**: go to Profile $\to$ Legal & Data Management $\to$ select **"Reset All Data"** and authenticate with Face ID / passcode. The system atomically purges all published slots, services, and bookings from Cloudflare D1, frees your `rosetime.app/name` slug, and wipes the local database clean.

#### 8. How does the AI Assistant work and is it safe?
The smart assistant routes queries via a secure Cloudflare Edge gateway to Google Gemini models. Before transmission, phone numbers are scrubbed with `[PHONE]` and names are pseudonymized. Zero client PII is stored in the cloud or used to train models.

#### 9. What if my database experiences an emergency crash?
RoseTime features **Store Safety Shield** — any crash archives your data into `.corrupt_<timestamp>`. Reach out to support (`pyzhovs@icloud.com`), and an engineer will assist with recovery per the [Database Recovery Runbook](DATABASE_RECOVERY_RUNBOOK.md).

#### 10. How does voice dictation work and is my microphone safe?
Hands-free voice dictation was engineered specifically for beauty masters working in gloves. The microphone is activated **strictly upon your explicit tap on the mic button 🎤**. Speech is transcribed on-device via Apple's native `Speech Framework`. No audio recordings are ever stored or uploaded.

#### 11. What is Apple App Clip and how do clients experience my link?
For iPhone clients, tapping your personal booking link or scanning your QR code smoothly summons a native Apple App Clip card from the bottom of the screen. Clients complete their booking in 15 seconds with Apple QuickType autofill and Taptic Engine feedback without downloading the full app from the App Store. Android and desktop users seamlessly open an elegant web widget in signature Rose Gold aesthetics.

#### 12. What happens if two clients attempt to book the exact same slot concurrently?
The platform enforces atomic concurrency locking on Cloudflare Edge (Double-Booking Shield). Whichever client submits first atomically secures the slot. The second client immediately receives a friendly notification ("Slot already booked") while preserving their entered contact info, enabling them to pick an alternative open slot in one tap. Overlapping bookings are strictly impossible.

---
<p align="center">
  <i>RoseTime Support Team — Dedicated to empowering beauty professionals worldwide. 💅✨</i>
</p>
