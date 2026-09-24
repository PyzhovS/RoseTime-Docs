# 🛡 Политика конфиденциальности (Privacy Policy) / RoseTime

*(Select language / Выберите язык: [Русский](#русский) | [English](#english))*

---

<a name="русский"></a>
## 🇷🇺 Политика конфиденциальности приложения RoseTime

**Дата вступления в силу:** 23 сентября 2026 года (Версия 1.2.3)

Настоящая Политика конфиденциальности описывает, как мобильное приложение **RoseTime** (далее — «Приложение», «Мы», «Сервис») собирает, обрабатывает, хранит и защищает информацию пользователей (мастеров индустрии красоты, стилистов и владельцев студий), а также их клиентов при использовании персональной онлайн-записи. 

Мы придерживаемся принципа **«Приватность по умолчанию» (Privacy by Design)** и обеспечиваем высочайший стандарт защиты данных в строгом соответствии с руководствами Apple App Store Review Guidelines (включая раздел 5.1 Privacy & Data Collection и требование 5.1.1(v) об удалении аккаунта), регламентом GDPR и требованиями Apple Privacy Manifest (iOS 17+).

---

### 1. Какие данные обрабатывает Приложение

RoseTime создано как ваш персональный интеллектуальный ассистент и CRM-система. В процессе работы Приложение обрабатывает следующие категории данных:

* **Данные о визитах и расписании:** Дата и время записей, выбранные процедуры из вашего каталога, длительность процедур, стоимость, статус сеанса и история визитов.
* **Данные о клиентах:** Имена или псевдонимы клиентов, контактные номера телефонов, заметки мастера по процедуре (формулы окрашивания, особенности ногтевой пластины, предпочтения).
* **Финансовая аналитика и статистика:** Доходы от выполненных процедур, расчет чистой выручки, расходы на материалы и аренду, сводная динамика загрузки графика. Все финансовые расчеты производятся **строго локально на устройстве**.
* **Адресная книга устройства (iOS Contacts):** По вашему явному разовому разрешению через системный компонент iOS `CNContactPickerViewController` Приложение может импортировать выбранный контакт (имя и номер телефона) напрямую в карточку клиента. Мы не сканируем и не выгружаем вашу телефонную книгу целиком.
* **Пользовательские настройки:** Предпочитаемый язык интерфейса (Русский / Қазақша / English), рабочие часы, параметры шторки приватности Face ID и согласие на использование ИИ.

---

### 2. 100% Локальное хранение данных (SwiftData) и Apple iCloud Sync

* **Хранение на вашем устройстве:** Все рабочие данные (клиентская база, история процедур, финансовые отчеты и заметки) сохраняются **исключительно локально на вашем iPhone** в защищенной базе данных Apple SwiftData (SQLite).
* **Бесплатная синхронизация Apple iCloud:** Синхронизация базы данных SwiftData и настроек расписания через защищенное личное облако Apple iCloud мастера (`NSUbiquitousKeyValueStore` и Apple CloudKit) является **100% бесплатной и автоматической для всех тарифов** (включая базовый Free). Данные передаются со сквозным шифрованием Apple под вашей персональной учетной записью Apple ID. Ни разработчик, ни сторонние лица не имеют доступа к вашему персональному облаку.
* **Отсутствие сторонних трекеров и продажи данных:** Мы **не собираем, не передаем, не продаем и не передаем в аренду** вашу базу клиентов или финансовые показатели рекламным сетям, аналитическим трекерам (Google Analytics, AppsFlyer, Facebook SDK) или брокерам данных.
* **Apple Privacy Manifest:** В приложении официально задекларирован системный манифест `PrivacyInfo.xcprivacy`:
  * `NSPrivacyTracking`: `false` (отслеживание пользователей полностью отсутствует).
  * `NSPrivacyTrackingDomains`: `[]` (0 внешних трекинговых доменов).
  * `NSPrivacyAccessedAPITypes`: категория `UserDefaults` с официальным кодом `CA92.1` (*App Functionality*).
  * `NSPrivacyCollectedDataTypes`: категория `Contact Info` и `User Content` для функционирования приложения без кросс-апп трекинга (*App Functionality, Not Linked for Tracking*).

---

### 3. Защита Биометрических Данных (Face ID / Touch ID / Passcode)

* RoseTime предоставляет функцию **«Шторка приватности» (Privacy Mode)** для сокрытия финансовых показателей от посторонних глаз с использованием системного фреймворка Apple **LocalAuthentication**.
* **Абсолютная изоляция биометрии:** Приложение **никогда не имеет доступа, не сканирует и не сохраняет** ваши биометрические данные (отпечатки пальцев или карту лица Face ID). Аутентификация выполняется аппаратно внутри защищенного сопроцессора **Apple Secure Enclave**. Приложение получает от операционной системы только булев результат проверки (*успех / отказ*).
* В случае неудачи сканирования лица система автоматически предлагает резервный ввод системного код-пароля iPhone (Device Passcode) в соответствии со стандартами Apple HIG.

---

### 4. Обработка данных сторонними сервисами ИИ (Google Gemini API) и Zero-PII Shield

Для работы интеллектуальных функций (разбор сообщений клиентов из мессенджеров, контекстный перенос визитов, дайджесты расписания и советы мастера) Приложение использует модель **Google Gemini** через зашифрованный серверный edge-прокси Cloudflare:

* **Раскрытие передаваемых данных:** Передаются исключительно обезличенные параметры расписания — дата, время слотов, длительность сеанса и названия процедур из вашего каталога (например, «Маникюр», «Педикюр»).
* **Строгое исключение персональных данных (Zero-PII Armor):** Номера телефонов, фамилии клиентов и личные заметки мастера **НИКОГДА не передаются стороннему сервису**. Номера телефонов аппаратно маскируются токеном `[PHONE]`, а имена подменяются анонимными идентификаторами (`Client_1`, `Client_2`). Реальное сопоставление с базой выполняется строго на процессоре вашего iPhone после получения ответа.
* **Защита данных и отсутствие обучения моделей:** Google LLC не сохраняет запросы пользователей API и не использует их для обучения своих публичных моделей машинного обучения (GDPR, SOC 2, ISO 27001).
* **Приоритет согласия (Consent First):** Запросы к ИИ не отправляются без предварительного явного согласия пользователя в экране `AIConsentView`. Согласие можно отозвать в любой момент.

---

### 5. Голосовой ввод и микрофон (Speech Recognition)

* **Активация по требованию:** Микрофон активируется **исключительно по прямому нажатию пользователя на кнопку микрофона** 🎤 на экране ввода. Фоновая или скрытая запись звука исключена.
* **Локальная транзитная обработка:** Преобразование речи в текст осуществляется в реальном времени с использованием системного фреймворка Apple `Speech` (`SFSpeechRecognizer`).
* **Zero Audio Retention:** Аудиозаписи никогда не сохраняются в виде файлов на диске устройства и не передаются в интернет.

---

### 6. Уведомления и Live Activities

* Локальные напоминания о визитах формируются через системный `UNUserNotificationCenter` на самом устройстве.
* Интерактивные сеансы на Dynamic Island и экране блокировки работают через нативный Apple `ActivityKit` без отправки сетевых данных.
* Уведомления о входящих онлайн-заявках доставляются через Apple Push Notification service (APNs) с использованием криптографических ключей ES256.

---

### 7. Подписки и платежи App Store (StoreKit 2)

* Оплата подписок RoseTime PRO и RoseTime AI обрабатывается исключительно через официальную платформу In-App Purchases компании Apple (StoreKit 2).
* Приложение никогда не собирает, не обрабатывает и не сохраняет данные банковских карт. Управление подпиской доступно в настройках учетной записи Apple ID.

---

### 8. Персональная Онлайн-Запись и Apple App Clip (Cloudflare Edge D1)

Для мастеров, активирующих функцию онлайн-записи, предоставляется персональная ссылка `rosetime.app/имя`:

* **Привязка к Apple ID:** Регистрация адреса ссылки осуществляется через защищенную авторизацию **Sign in with Apple**, исключающую подделку личности и перехват адреса.
* **Мгновенная запись через Apple App Clip:** Для пользователей iPhone запись работает через нативную технологию Apple App Clip без необходимости скачивания приложения из App Store. Поддерживаются кратковременные системные уведомления (до 8 часов) для информирования клиента о статусе визита без доступа к геолокации и без рекламных трекеров.
* **Атомарная защита от накладок (Double-Booking Shield):** Сервер Cloudflare Edge D1 производит атомарную блокировку слота при бронировании — одновременная запись двух клиентов на одно и то же время математически исключена.
* **Какие данные передаются:** Открытые слоты мастера, перечень услуг и заявка клиента (имя и телефон).
* **Использование данных клиентов:** Данные клиента используются **исключительно для доставки заявки мастеру** и отображения статуса бронирования. Данные клиентов никогда не передаются сторонним рекламным сетям, не используются для маркетинговых рассылок и не продаются.
* **Антиспам-защита без трекинга:** Для защиты расписания мастера от спам-ботов используется сервис **Cloudflare Turnstile**, проверяющий браузер без использования отслеживающих cookies и без сбора персональных профилей, а также скрытые ловушки Honeypot и ограничение частоты запросов (IP Rate Limiting).

---

### 9. Полное удаление аккаунта и данных на сервере — Clean Slate Protocol (Apple Guideline 5.1.1(v))

В соответствии с требованием Apple App Store Review Guideline 5.1.1(v) пользователю предоставлена возможность полного, мгновенного и необратимого удаления своей учетной записи и всех сопутствующих данных:

* **Как выполнить:** Перейдите во вкладку «Профиль» $\to$ «Правовая информация и управление данными» $\to$ нажмите **«Стереть абсолютно всё»**.
* **Биометрическая защита:** Для предотвращения случайного сброса требуется обязательная авторизация через **Face ID / Touch ID** или системный код-пароль устройства.
* **Что удаляется:**
  * С серверов Cloudflare Edge D1 безвозвратно удаляются профиль мастера, персональная ссылка `rosetime.app/имя`, опубликованные слоты, каталог услуг и все поступившие заявки клиентов (атомарный запрос `POST /api/v1/master/delete-account`).
  * С устройства полностью стирается локальная база данных SwiftData (записи, клиенты, услуги, история уведомлений), сбрасываются настройки `UserDefaults` и облачные кэши Apple iCloud KVS.
  * Приложение возвращается в чистое исходное состояние первого запуска (экран выбора языка и онбординг).

---

### 10. Контакты разработчика

По любым вопросам, связанным с настоящей Политикой конфиденциальности или безопасностью данных в RoseTime, вы можете обратиться к разработчику:

* **Разработчик:** Сергей Пыжов
* **Контактный Email:** `pyzhovs@icloud.com`
* **Сайт сервиса:** [https://rosetime.app](https://rosetime.app)
* **Официальный репозиторий документации:** [https://github.com/PyzhovS/RoseTime-Docs](https://github.com/PyzhovS/RoseTime-Docs)

---
---

<a name="english"></a>
## 🇬🇧 RoseTime Privacy Policy

**Effective Date:** September 23, 2026 (Version 1.2.3)

This Privacy Policy explains how the **RoseTime** mobile application ("Application", "We", "Service") collects, processes, stores, and protects information from its users (beauty artists, hairstylists, nail technicians, and studio owners) as well as their clients using the online booking features.

We strictly adhere to the principle of **Privacy by Design** and ensure the highest standards of data protection in compliance with the Apple App Store Review Guidelines (including Section 5.1 Privacy & Data Collection and Guideline 5.1.1(v) regarding account deletion), GDPR regulations, and Apple Privacy Manifest requirements (iOS 17+).

---

### 1. Information Processed by the Application

RoseTime serves as your personal smart scheduling assistant and salon CRM. The Application processes the following categories of data:

* **Appointment & Schedule Records:** Date, start/end times, catalog procedures, treatment durations, pricing, visit statuses, and history logs.
* **Client Information:** Client names or aliases, contact phone numbers, and private stylist notes (color formulas, nail plate specifics, preferences).
* **Financial Analytics & Revenue Metrics:** Completed procedure earnings, net revenue metrics, supply expenses, studio rent, and schedule utilization. All financial calculations are performed **strictly locally on your device**.
* **iOS Contacts Access:** With your explicit one-time permission granted via the native iOS `CNContactPickerViewController`, the Application can import a chosen contact (name and phone number) directly into a client card. We do NOT scan, upload, or export your full address book.
* **User Preferences:** Preferred interface language (Russian / Kazakh / English), operating hours, Face ID Privacy Shield settings, and AI feature consent.

---

### 2. 100% On-Device Storage (SwiftData) & Free Apple iCloud Sync

* **Stored on Your iPhone:** All business operational data (client rosters, appointment logs, revenue analytics, and notes) is stored **strictly on your local device** inside an encrypted Apple SwiftData container by default.
* **Universal Free Apple iCloud Sync:** Database synchronization and schedule preferences via personal Apple iCloud (`NSUbiquitousKeyValueStore` and Apple CloudKit) are **100% free and automatic across all tiers** (including Free). Data is transmitted with end-to-end Apple encryption under your personal Apple ID account. Neither the developer nor third parties have access to your personal cloud.
* **Zero Third-Party Trackers & No Data Selling:** We do **NOT collect, sell, lease, or distribute** your client contacts or revenue figures to advertising networks, tracking SDKs, or data brokers.
* **Apple Privacy Manifest Compliance:** The app officially ships with `PrivacyInfo.xcprivacy`:
  * `NSPrivacyTracking`: `false` (User tracking is completely disabled).
  * `NSPrivacyTrackingDomains`: `[]` (0 tracking domains).
  * `NSPrivacyAccessedAPITypes`: `UserDefaults` category with official reason `CA92.1` (*App Functionality*).
  * `NSPrivacyCollectedDataTypes`: `Contact Info` and `User Content` categories for core application features without tracking (*App Functionality, Not Linked for Tracking*).

---

### 3. Biometric Data Protection (Face ID / Touch ID / Passcode)

* RoseTime provides the **Face ID Privacy Shield** to shroud financial figures from peering eyes using Apple's **LocalAuthentication** framework.
* **Absolute Biometric Isolation:** The Application **never accesses, scans, or retains** raw biometric face maps or fingerprints. Authentication is processed inside the **Apple Secure Enclave** coprocessor. The app receives only an authenticated boolean confirmation from iOS.
* If biometric matching is unsuccessful, iOS automatically provides fallback to the device passcode.

---

### 4. Third-Party AI Processing (Google Gemini API) & Zero-PII Shield

For smart scheduling analysis, message parsing, and client retention recommendations, the Application utilizes **Google Gemini** models via an encrypted Cloudflare Edge proxy:

* **Data Disclosed:** Strictly anonymized schedule parameters — dates, slot times, appointment durations, and service names from your catalog.
* **Zero-PII Hardware Filtering:** Phone numbers, client surnames, and personal formulas are **NEVER transmitted to third-party services**. Numbers are scrubbed on-device with `[PHONE]`, and names are pseudonymized (`Client_1`, `Client_2`).
* **No Model Training:** Google LLC does not retain user API queries or utilize them to train public AI models (GDPR, SOC 2, ISO 27001).
* **Consent First:** AI features remain inactive until explicit approval is granted via `AIConsentView`. Consent can be revoked at any time.

---

### 5. Speech Recognition & Microphone

* **On-Demand Activation:** The microphone is activated **strictly upon your explicit tap on the mic button 🎤**. Background or unauthorized recording is impossible.
* **On-Device Real-Time Processing:** Speech-to-text is handled via Apple’s native `Speech` framework (`SFSpeechRecognizer`).
* **Zero Audio Retention:** Audio streams are never archived to disk or transmitted to external servers.

---

### 6. Notifications & Live Activities

* Appointment alarms are managed locally via Apple's `UNUserNotificationCenter` on-device.
* Dynamic Island Live Activities operate through native Apple `ActivityKit` without external networking.
* Real-time online booking alerts are delivered securely via Apple Push Notification service (APNs) using ES256 Web Crypto.

---

### 7. App Store Purchases & Subscriptions (StoreKit 2)

* Transactions for RoseTime PRO and RoseTime AI subscriptions are processed exclusively via Apple In-App Purchases (StoreKit 2).
* The Application never collects, processes, or stores payment card credentials. Subscription management is available natively in Apple ID settings.

---

### 8. Personal Online Booking & Apple App Clip (Cloudflare Edge D1)

For masters utilizing online booking, a personalized web portal is provided at `rosetime.app/name`:

* **Apple ID Binding:** Slug registration is authenticated via **Sign in with Apple**, preventing identity spoofing and unauthorized slug takeovers.
* **Instant Native Booking via Apple App Clip:** For iPhone clients, booking runs natively through Apple App Clip without downloading the full app from the App Store. Ephemeral notifications (up to 8 hours) provide immediate appointment status updates without location tracking, advertising trackers, or persistent cookies.
* **Atomic Concurrency Protection (Double-Booking Shield):** Cloudflare Edge D1 enforces atomic slot locking upon submission — concurrent double-bookings for the exact same slot are mathematically impossible.
* **Data Processed on Edge Servers:** Open availability slots, catalog services, and incoming client reservations (name and phone number).
* **Client Data Usage:** Client information is processed **solely to notify the master and schedule the visit**. Client information is never sold, shared with advertising networks, or used for cross-promotions.
* **Non-Tracking Anti-Spam:** Form submission is secured by **Cloudflare Turnstile** (non-cookie bot challenge), honeypots, and edge IP rate limiting.

---

### 9. Account & Data Deletion — Clean Slate Protocol (Apple Guideline 5.1.1(v))

In compliance with Apple App Store Review Guideline 5.1.1(v), users can initiate complete, immediate, and irreversible account and data deletion at any time:

* **How to Execute:** Open Profile $\to$ Legal & Data Management $\to$ select **"Reset All Data"**.
* **Biometric Authentication:** Requires **Face ID / Touch ID** or device passcode authorization to prevent accidental resets.
* **What is Deleted:**
  * From Cloudflare Edge D1 servers: master profile, personal link `rosetime.app/name`, published slots, catalog services, and all incoming bookings are permanently purged via `POST /api/v1/master/delete-account`.
  * From the device: the SwiftData container (appointments, clients, services, notifications) is erased, `UserDefaults` are reset, and Apple iCloud KVS records are purged.
  * The application smoothly transitions back to the initial setup screen (language selection and onboarding).

---

### 10. Developer Contact Information

For inquiries, feedback, or privacy-related questions, please contact:

* **Developer:** Sergey Pyzhov
* **Support Email:** `pyzhovs@icloud.com`
* **Website:** [https://rosetime.app](https://rosetime.app)
* **Documentation Repository:** [https://github.com/PyzhovS/RoseTime-Docs](https://github.com/PyzhovS/RoseTime-Docs)

---
<p align="center">
  <i>RoseTime — Dedicated to beauty professionals' privacy, security, and peace of mind. 💅🛡️</i>
</p>
