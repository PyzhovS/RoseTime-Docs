# 🛡 Политика конфиденциальности (Privacy Policy) / RoseTime

*(Select language / Выберите язык: [Русский](#русский) | [English](#english))*

---

<a name="русский"></a>
## 🇷🇺 Политика конфиденциальности приложения RoseTime

**Дата вступления в силу:** 22 августа 2026 года (Версия 1.0.0)

Настоящая Политика конфиденциальности описывает, как мобильное приложение **RoseTime** (далее — «Приложение», «Мы», «Сервис») собирает, обрабатывает, хранит и защищает информацию пользователей (мастеров индустрии красоты, стилистов и владельцев салонов). 

Мы придерживаемся принципа **«Приватность по умолчанию» (Privacy by Design)** и обеспечиваем высочайший стандарт защиты персональных данных в строгом соответствии с руководствами Apple App Store Review Guidelines (включая раздел 5.1 Privacy & Data Collection), регламентом GDPR и требованиями Apple Privacy Manifest (iOS 17+).

---

### 1. Какие данные обрабатывает Приложение

RoseTime создано как ваш персональный интеллектуальный ассистент и CRM-система. В процессе работы Приложение обрабатывает следующие категории данных:

* **Данные о визитах и расписании:** Дата и время записей, выбранные процедуры из вашего прайс-листа, длительность процедур, стоимость, статус сеанса и история визитов.
* **Данные о клиентах:** Имена или псевдонимы клиентов, контактные номера телефонов, заметки мастера по процедуре (формулы окрашивания, особенности ногтевой пластины).
* **Финансовая аналитика и статистика:** Доходы от выполненных процедур, расчет чистой выручки и сводная динамика загрузки рабочего графика.
* **Адресная книга устройства (iOS Contacts):** По вашему явному разовому разрешению через системный компонент iOS `CNContactPickerViewController` Приложение может импортировать выбранный контакт (имя и номер телефона) напрямую в карточку клиента. Мы не сканируем и не выгружаем вашу телефонную книгу целиком.
* **Пользовательские настройки:** Предпочитаемый язык интерфейса (Русский / English), рабочие часы, параметры шторки приватности Face ID и согласие на использование ИИ.

---

### 2. 100% Локальное хранение данных и Apple SwiftData

* **Хранение только на вашем устройстве:** Все рабочие данные (клиентская база, история процедур, финансовые отчеты и заметки) сохраняются **исключительно локально на вашем iPhone** в защищенной базе данных Apple SwiftData.
* **Отсутствие сторонних трекеров и продажи данных:** Мы **не собираем, не передаем, не продаем и не передаем в аренду** вашу базу клиентов или финансовые показатели рекламным сетям, аналитическим трекерам (Google Analytics, AppsFlyer, Facebook SDK) или брокерам данных.
* **Apple Privacy Manifest:** В приложении официально задекларирован системный манифест `PrivacyInfo.xcprivacy`:
  * `NSPrivacyTracking`: `false` (отслеживание пользователей полностью отсутствует).
  * `NSPrivacyTrackingDomains`: `[]` (0 внешних трекинговых доменов).
  * `NSPrivacyAccessedAPITypes`: категория `UserDefaults` с официальным кодом `CA92.1` (*App Functionality*).

---

### 3. Защита Биометрических Данных (Face ID / Touch ID)

* RoseTime предоставляет функцию **«Шторка приватности» (Privacy Mode)** для сокрытия финансовых показателей от посторонних глаз с использованием системного фреймворка Apple **LocalAuthentication**.
* **Абсолютная изоляция биометрии:** Приложение **никогда не имеет доступа, не сканирует и не сохраняет** ваши биометрические данные (отпечатки пальцев или карту лица Face ID). Аутентификация выполняется аппаратно внутри защищенного сопроцессора **Apple Secure Enclave**. Приложение получает от операционной системы только булев результат проверки (*успех / отказ*).

---

### 4. Умный ИИ-Ассистент и Политика Zero PII Shield

Для работы интеллектуальных функций (разбор сообщений клиентов из мессенджеров, контекстный перенос визитов, дайджесты расписания и советы мастера) Приложение использует защищенную архитектуру:

* **Защищенный Серверный Прокси (Cloudflare Edge BFF):** Все сетевые запросы к модели искусственного интеллекта **Google Gemini 3.1 Flash Lite** передаются через серверный прокси (`https://rosetime-proxy.pyzhov-ai.workers.dev`), развернутый на изолированных edge-нодах Cloudflare. API-ключи изолированы в зашифрованном хранилище и недоступны клиентам.
* **Маскировка персональных данных (Zero PII Armor):**
  * Перед отправкой любого входящего текста в модель все телефонные номера автоматически вырезаются и заменяются маской `[PHONE]`.
  * Имена клиентов заменяются анонимными токенами (`Client_1`, `Client_2`), а реальное сопоставление с локальной базой данных выполняется **строго на вашем устройстве** после получения структурированного ответа.
* **Отсутствие обучения моделей:** Передаваемые данные являются временными (ephemeral), не сохраняются на дисках облачных провайдеров и **категорически не используются для обучения публичных нейросетей**.
* **Автономный On-Device Мозг:** При отсутствии интернет-соединения Приложение автоматически переключается на встроенные офлайн-парсеры дат (`RussianDateParser`, `EnglishDateParser`) и банк из 40 авторских офлайн-советов.
* **Явное согласие:** ИИ-функции активируются только при подтверждении согласия пользователя (`AIConsentView`) и могут быть отключены в Настройках в любой момент.

---

### 5. Уведомления и Live Activities (Виджеты)

* Приложение использует локальный системный центр уведомлений `UNUserNotificationCenter` для отправки напоминаний о визитах. Все уведомления генерируются локально на процессоре вашего устройства без использования удаленных Push-серверов.
* Виджет экрана блокировки и Dynamic Island работают через нативный Apple `ActivityKit`. Состояние сессии передается напрямую в расширение виджета без отправки во внешнюю сеть.

---

### 6. Право на Удаление и Управление Данными (Data Erasure)

* Вы обладаете полным суверенным контролем над всей информацией в Приложении. Вы можете в любой момент изменить или удалить любого клиента, визит или услугу.
* **Полный сброс данных («Сбросить все данные»):** В разделе настроек профиля доступна функция мгновенного безвозвратного удаления всей базы SwiftData и сброса настроек `UserDefaults`.
* При удалении Приложения с устройства все связанные локальные файлы стираются операционной системой iOS.

---

### 7. Контакты и Обратная Связь

По любым вопросам, связанным с настоящей Политикой конфиденциальности или безопасностью данных в RoseTime, вы можете обратиться к разработчику:

* **Разработчик:** Сергей Пыжов
* **Контактный Email:** `pyzhovs@icloud.com`
* **Официальный репозиторий:** [https://github.com/PyzhovS/RoseTime-Docs](https://github.com/PyzhovS/RoseTime-Docs)

---
---

<a name="english"></a>
## 🇬🇧 RoseTime Privacy Policy

**Effective Date:** August 22, 2026 (Version 1.0.0)

This Privacy Policy explains how the **RoseTime** mobile application ("Application", "We", "Service") collects, processes, stores, and safeguards information from its users (beauty artists, hairstylists, nail technicians, and salon owners).

We strictly adhere to the principle of **Privacy by Design** and ensure the highest standards of data protection in compliance with the Apple App Store Review Guidelines (including Section 5.1 Privacy & Data Collection), GDPR regulations, and Apple Privacy Manifest specifications (iOS 17+).

---

### 1. Information Processed by the Application

RoseTime serves as your personal smart scheduling assistant and salon CRM. The Application processes the following categories of local data:

* **Appointment & Schedule Records:** Date, start/end times, catalog procedures, treatment durations, pricing, visit statuses, and history logs.
* **Client Information:** Client names or aliases, contact phone numbers, and private stylist notes (color formulas, nail plate specifics).
* **Financial Analytics & Revenue Metrics:** Completed procedure earnings, net revenue metrics, and working schedule utilization dynamics.
* **iOS Contacts Access:** With your explicit one-time permission granted via the native iOS `CNContactPickerViewController`, the Application can import a chosen contact (name and phone number) directly into a client card. We do NOT scan, upload, or export your full address book.
* **User Preferences:** Preferred interface language (Russian / English), operating hours, Face ID Privacy Shield settings, and AI feature consent.

---

### 2. 100% On-Device Storage & Apple SwiftData

* **Stored Solely on Your iPhone:** All business operational data (client rosters, appointment logs, revenue analytics, and notes) is stored **strictly on your local device** inside an encrypted Apple SwiftData container.
* **Zero Third-Party Trackers & No Data Selling:** We do **NOT collect, sell, lease, or distribute** your client contacts or revenue figures to advertising networks, tracking SDKs (Google Analytics, AppsFlyer, Facebook SDK), or data brokers.
* **Apple Privacy Manifest Compliance:** The app officially ships with `PrivacyInfo.xcprivacy`:
  * `NSPrivacyTracking`: `false` (User tracking is completely disabled).
  * `NSPrivacyTrackingDomains`: `[]` (0 tracking domains).
  * `NSPrivacyAccessedAPITypes`: `UserDefaults` category with official reason `CA92.1` (*App Functionality*).

---

### 3. Biometric Security (Face ID / Touch ID)

* RoseTime features a **Privacy Shield** mode to instantly shroud financial figures and client details from unauthorized viewers using Apple’s **LocalAuthentication** framework.
* **Zero Biometric Access Guarantee:** The Application **never accesses, captures, or transmits** raw fingerprint data or Face ID facial maps. Authentication is handled exclusively by the hardware-isolated **Apple Secure Enclave**. RoseTime only receives a boolean verification result (*success / failure*).

---

### 4. Smart AI Assistant & Zero PII Shield

To empower intelligent natural-language scheduling (parsing messy messenger bookings, rescheduling appointments, calendar resolution, and daily salon digests), RoseTime leverages a hardened serverless architecture:

* **Secure Cloudflare Edge BFF Proxy:** All requests to the **Google Gemini 3.1 Flash Lite** model pass through an isolated proxy (`https://rosetime-proxy.pyzhov-ai.workers.dev`) on Cloudflare's Edge V8 network. API credentials remain securely vaulted on the server.
* **Zero PII Data Anonymization Armor:**
  * Before any text is dispatched to the AI model, all phone numbers are sanitized with a regex and replaced by `[PHONE]`.
  * Client names are substituted with anonymous pseudonyms (`Client_1`, `Client_2`), and genuine client identity binding occurs **strictly on your iPhone** after receiving the structured response.
* **Zero Model Training:** Transmitted payloads are purely ephemeral, never logged to disk, and **never used to train public machine learning models**.
* **Adaptive On-Device Offline Brain:** In offline mode or under network loss, the Application seamlessly falls back to on-device NLP parsers (`RussianDateParser`, `EnglishDateParser`) and an embedded vault of 40 expert master tips.
* **Transparent Consent:** AI capabilities require explicit opt-in (`AIConsentView`) and can be toggled off at any moment in Settings.

---

### 5. Notifications & Live Activities (WidgetKit)

* The Application utilizes Apple’s local `UNUserNotificationCenter` for upcoming appointment alarms. All notifications are scheduled on-device without remote push notification servers.
* Lock Screen widgets and Dynamic Island Live Activities operate through native Apple `ActivityKit`, streaming session states directly on the device with zero network transmission.

---

### 6. User Data Control & Complete Erasure

* You maintain sovereign administrative control over your data. You can edit, update, or permanently delete any appointment, client, or catalog service at any time.
* **Complete Data Reset ("Reset All Data"):** The Profile Settings menu provides a 1-tap option to permanently wipe all SwiftData databases and reset `UserDefaults`.
* Deleting the Application from your iOS device immediately and permanently purges all local app data.

---

### 7. Developer Contact Information

If you have questions, inquiries, or feedback regarding this Privacy Policy or data security in RoseTime, please contact:

* **Developer:** Sergey Pyzhov
* **Support Email:** `pyzhovs@icloud.com`
* **Official Repository:** [https://github.com/PyzhovS/RoseTime-Docs](https://github.com/PyzhovS/RoseTime-Docs)

---
<p align="center">
  <i>RoseTime — Dedicated to beauty professionals' privacy and peace of mind. 💅🛡️</i>
</p>
