# 🌹 RoseTime — Описание релиза 1.2.3 (Build 35)

---

## 🇷🇺 Русская версия (Russian)

### 📱 Для App Store Connect («Что нового в этой версии»):
```text
Пока вы создаете красоту — RoseTime заботится о том, чтобы каждый рабочий день проходил легко, быстро и с эстетическим удовольствием. Встречайте RoseTime 1.2.3: революция в онлайн-записи через Apple App Clip, безупречная защита вашего расписания и новый уровень заботы о клиентах!

• Мгновенная онлайн-запись нового поколения: вашим клиентам больше не нужно ничего скачивать или переходить на сторонние сайты! При переходе по вашей персональной ссылке прямо на экране iPhone клиента плавно появляется нативная карточка Apple — запись на любимую процедуру занимает всего 15 секунд.
• Защита от накладок и двойных записей: теперь ваш график под надежным интеллектуальным замком. Два клиента никогда не запишутся на один и тот же слот — система мгновенно бронирует время для первого и бережно предлагает альтернативу второму.
• Идеальный ввод номеров телефонов: номер клиента форматируется плавно, красиво и без единой ошибки, независимо от того, как вы или клиент начинаете ввод («+7», «7» или «8»).
• Чистое и гармоничное расписание: напоминания, дайджесты и календарь теперь отображают только актуальные подтвержденные визиты — никакого визуального шума и спокойствие на протяжении всего дня.
• Премиальный тактильный комфорт: фирменный мягкий виброотклик iPhone сопровождает каждое действие, подчеркивая высокий статус вашего сервиса.

Спасибо, что развиваете свой бьюти-бизнес вместе с RoseTime!
```

---

### 📋 Общее резюме релиза (Release Summary):

#### 1. ✨ Мгновенная онлайн-запись через Apple App Clip (120 FPS)
* Нативная интеграция Apple App Clip без необходимости скачивания приложения из App Store.
* Плавное открытие карточки бронирования снизу экрана с системной автоподстановкой QuickType.
* Элегантный fallback на веб-виджет для пользователей Android и десктопа.

#### 2. 🛡️ Атомарная защита от двойных записей (Double-Booking Shield)
* Атомарная блокировка слотов на уровне Cloudflare Edge SQLite D1.
* Интеллектуальное разрешение коллизий и сохранение введенных данных клиента при статусе занятости слота.
* Честное 15-минутное окно удержания бронирования.

#### 3. 📱 Безупречный ввод номера телефона 2.0
* Прецизионная поддержка ввода через «+7», «7» и «8» без потери крайних цифр.
* Канонический формат номеров с неразрывными пробелами.

#### 4. ⚡️ Фокусное расписание и дайджесты
* Дайджесты и виджеты отображают строго подтвержденные визиты.
* Автоматическая архивация просроченных и отклоненных заявок.

---
---

## 🇬🇧 Английская версия (English)

### 📱 For App Store Connect ("What's New in This Version"):
```text
While you craft beauty, RoseTime ensures your workday flows effortlessly, swiftly, and with refined elegance. Welcome RoseTime 1.2.3: next-generation online booking powered by Apple App Clip, unshakeable schedule protection, and elevated client care!

• Next-Gen Instant Online Booking: Your clients no longer need to download an app or browse clunky websites! Tapping your booking link smoothly summons a native Apple App Clip card right on their iPhone — booking their favorite beauty service takes just 15 seconds.
• Zero-Collision Schedule Protection: Your appointment book is now under intelligent real-time protection. Overlapping double-bookings are completely eliminated, keeping your calendar pristine and stress-free.
• Flawless Phone Number Formatting: Client phone numbers format effortlessly and beautifully from the very first tap, ensuring seamless contact and instant WhatsApp connectivity.
• Pure & Focused Daily Agenda: Daily focus digests, reminders, and calendar views now spotlight only confirmed appointments, keeping your day clear and organized.
• Signature Tactile Elegance: Refined native haptic feedback accompanies every step of the journey, reflecting the premium standards of your beauty studio.

Thank you for choosing RoseTime to empower your beauty business!
```

---

### 📋 General Release Summary (English):

#### 1. ✨ Instant Online Booking via Apple App Clip (120 FPS)
* Native Apple App Clip integration requiring zero app installations from the App Store.
* Smooth bottom-sheet card presentation with QuickType autofill support.
* Graceful fallback to responsive Rose Gold web widget for Android & desktop users.

#### 2. 🛡️ Concurrency & Double-Booking Shield
* Atomic database-level slot locking powered by Cloudflare Edge SQLite D1.
* Frictionless conflict resolution preserving client inputs upon slot competition.
* 15-minute countdown reservation hold lifecycle.

#### 3. 📱 Flawless Phone Number Input 2.0
* Canonical "+7", "7", and "8" input normalization without trailing digit loss.
* Standardized non-breaking spacing and instant WhatsApp communication.

#### 4. ⚡️ Focused Agenda & Digests
* Schedule filters, widgets, and daily reminders exclusively highlight confirmed appointments.
* Automatic archiving of expired holds and clean schedule maintenance.
