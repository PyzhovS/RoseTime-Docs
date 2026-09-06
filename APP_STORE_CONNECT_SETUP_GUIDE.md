# 🌹 Руководство по Настройке App Store Connect и Подписок StoreKit 2 (RoseTime)

Данный документ содержит пошаговую инструкцию по полной настройке юридических соглашений, Политики Конфиденциальности, Apple Standard EULA, 4 продуктов подписок StoreKit 2, тарифов, Free Trial (пробных периодов) и скриншотов для цензоров Apple в консоли [App Store Connect](https://appstoreconnect.apple.com).

---

## 📜 ЭТАП 1: Указание Политики Конфиденциальности и Apple Standard EULA

### 1.1. Ссылка на Политику Конфиденциальности (Privacy Policy URL)
Apple требует указать работающую веб-ссылку на Политику Конфиденциальности:
1. Откройте **[App Store Connect](https://appstoreconnect.apple.com)** $\rightarrow$ **«Мои приложения»** $\rightarrow$ выберите **RoseTime**.
2. В левом меню выберите страницу **«1.0 Готово к продаже»** (или «Подготовка к отправке»).
3. Прокрутите вниз до блока **«Общие сведения»**:
   * В поле **«URL-адрес политики конфиденциальности»** вставьте:  
     `https://github.com/PyzhovS/RoseTime-Docs/blob/main/PRIVACY_POLICY.md`
4. Нажмите кнопку **«Сохранить»** (в правом верхнем углу).
5. В левом меню перейдите в раздел **«Конфиденциальность приложения»** (App Privacy) $\rightarrow$ нажмите **«Начать»** (или «Редактировать») $\rightarrow$ укажите этот же URL.

### 1.2. Условия использования (EULA / Terms of Use)
По умолчанию Apple применяет официальное лицензионное соглашение **Apple Standard EULA**.
* В поле **«Описание приложения»** (Description) на странице версии в самом низу добавьте стандартный блок:
  ```text
  Политика конфиденциальности: https://github.com/PyzhovS/RoseTime-Docs/blob/main/PRIVACY_POLICY.md
  Условия использования (EULA): https://www.apple.com/legal/internet-services/itunes/dev/stdeula/
  ```

---

## 💎 ЭТАП 2: Настройка 4 Продуктов Подписок StoreKit 2

В коде приложения (`SubscriptionManager.swift`) зафиксированы точные идентификаторы:
* `com.pyzhov.rosetime.pro.monthly`
* `com.pyzhov.rosetime.pro.annual`
* `com.pyzhov.rosetime.ai.monthly`
* `com.pyzhov.rosetime.ai.annual`

### 2.1. Создание Группы Подписок (Subscription Group)
1. В левом меню перейдите в **«Монетизация»** $\rightarrow$ **«Подписки»** (Subscriptions).
2. Нажмите синий плюс **«+»** рядом с «Группы подписок».
3. Введите название группы: `RoseTime Subscriptions` и нажмите **«Создать»**.

---

### 2.2. Добавление и Настройка 4 Подписок

Внутри группы `RoseTime Subscriptions` нажмите кнопку **«Создать подписку»** («+») для каждого из 4 продуктов:

#### 1️⃣ Продукт: RoseTime PRO (Месяц)
* **Название для справки:** `RoseTime PRO Monthly`
* **Идентификатор продукта (Product ID):** `com.pyzhov.rosetime.pro.month` *(или `com.pyzhov.rosetime.pro.monthly`)*
* **Длительность подписки:** `1 месяц`
* **Цена подписки:** Выберите уровень цен **1 990 ₸** (или $3.99 USD).
* **Локализация подписки:**
  * Язык: *Русский (Russian)*
  * Отображаемое имя: `RoseTime PRO (1 месяц)`
  * Описание (лимит Apple 55 символов): `Вся статистика, iCloud бэкап и умные окна на 1 месяц`
  * Язык: *Английский (English - US)* (рекомендуется)
  * Отображаемое имя: `RoseTime PRO (1 Month)`
  * Описание: `All stats, iCloud backup and smart slots for 1 month`
* **Вступительное предложение (Free Trial 7 дней):**
  * В блоке «Вступительные предложения» нажмите **«+»**.
  * Выберите все страны/территории $\rightarrow$ Тип: **Бесплатно (Free Trial)** $\rightarrow$ Длительность: **7 дней**.

---

#### 2️⃣ Продукт: RoseTime PRO (Год)
* **Название для справки:** `RoseTime PRO Annual`
* **Идентификатор продукта (Product ID):** `com.pyzhov.rosetime.pro.annual`
* **Длительность подписки:** `1 год`
* **Цена подписки:** Выберите уровень цен **14 990 ₸** (или $29.99 USD).
* **Локализация подписки:**
  * Язык: *Русский (Russian)*
  * Отображаемое имя: `RoseTime PRO (1 год)`
  * Описание (лимит Apple 55 символов): `Вся статистика, iCloud бэкап и умные окна на 1 год`
  * Язык: *Английский (English - US)* (рекомендуется)
  * Отображаемое имя: `RoseTime PRO (1 Year)`
  * Описание: `All stats, iCloud backup and smart slots for 1 year`
* **Вступительное предложение (Free Trial 7 дней):**
  * Добавьте Free Trial на **7 дней**.

---

#### 3️⃣ Продукт: RoseTime AI ✨ (Месяц)
* **Название для справки:** `RoseTime AI Monthly`
* **Идентификатор продукта (Product ID):** `com.pyzhov.rosetime.ai.monthly`
* **Длительность подписки:** `1 месяц`
* **Цена подписки:** Выберите уровень цен **3 490 ₸** (или $6.99 USD).
* **Локализация подписки:**
  * Язык: *Русский (Russian)*
  * Отображаемое имя: `RoseTime AI (1 месяц)`
  * Описание (лимит Apple 55 символов): `Нейросеть Gemini, авто-тексты и PRO-функции на месяц`
  * Язык: *Английский (English - US)* (рекомендуется)
  * Отображаемое имя: `RoseTime AI (1 Month)`
  * Описание: `Gemini AI, smart texts and PRO features for 1 month`
* **Вступительное предложение (Free Trial 3 дня):**
  * В блоке «Вступительные предложения» нажмите **«+»**.
  * Выберите все страны/территории $\rightarrow$ Тип: **Бесплатно (Free Trial)** $\rightarrow$ Длительность: **3 дня**.

---

#### 4️⃣ Продукт: RoseTime AI ✨ (Год)
* **Название для справки:** `RoseTime AI Annual`
* **Идентификатор продукта (Product ID):** `com.pyzhov.rosetime.ai.annual`
* **Длительность подписки:** `1 год`
* **Цена подписки:** Выберите уровень цен **29 990 ₸** (или $59.99 USD).
* **Локализация подписки:**
  * Язык: *Русский (Russian)*
  * Отображаемое имя: `RoseTime AI (1 год)`
  * Описание (лимит Apple 55 символов): `Нейросеть Gemini, авто-тексты и PRO-функции на 1 год`
  * Язык: *Английский (English - US)* (рекомендуется)
  * Отображаемое имя: `RoseTime AI (1 Year)`
  * Описание: `Gemini AI, smart texts and PRO features for 1 year`
* **Вступительное предложение (Free Trial 3 дня):**
  * Добавьте Free Trial на **3 дня**.

---

### 2.3. Ранжирование Тарифов (Subscription Levels)
Внутри группы `RoseTime Subscriptions` расположите карточки по уровням приоритета (для правильной работы переходов Upgrade / Downgrade в iOS):
* **Уровень 1 (Высший приоритет — AI):**
  * `RoseTime AI Annual`
  * `RoseTime AI Monthly`
* **Уровень 2 (Базовый приоритет — PRO):**
  * `RoseTime PRO Annual`
  * `RoseTime PRO Monthly`

---

## 📸 ЭТАП 3: Скриншоты Paywall для Проверки (Review Screenshots)

> [!IMPORTANT]
> Apple отклонит подписки без прикрепленного скриншота экрана покупки. Цензор должен видеть реальный Paywall.

### 3.1. Как сделать скриншот:
1. Запустите симулятор iPhone в Xcode (`Cmd + R`).
2. Перейдите во вкладку **«Профиль»** $\rightarrow$ нажмите **«RoseTime PRO / AI»** (откроется Paywall).
3. Нажмите **`Cmd + S`** на клавиатуре Mac — снимок экрана сохранится на Рабочий стол.
4. Сделайте 2 снимка:
   * С выбранным тарифом **RoseTime PRO** (видны 7 дней триала);
   * С выбранным тарифом **RoseTime AI** (видны 3 дня триала).

### 3.2. Загрузка в App Store Connect:
1. Откройте каждый из 4 продуктов подписок.
2. Прокрутите вниз до блока **«Сведения для проверки»** (Review Information).
3. В поле **«Скриншот для проверки»** загрузите скриншот Paywall.
4. В поле **«Заметки для проверки»** (Review Notes) укажите:
   ```text
   Экран оформления подписки открывается из вкладки «Профиль» по кнопке «RoseTime PRO / AI». 
   Реализован на нативном StoreKit 2 с поддержкой Free Trial (7 дней для PRO, 3 дня для AI).
   ```
5. Нажмите **«Сохранить»**.

---

## 🚀 ЭТАП 4: Привязка Подписок к Релизу Версии 1.0

1. В левом меню перейдите на страницу **«1.0 Готово к продаже»** (или «Подготовка к отправке»).
2. Прокрутите страницу вниз до блока **«Встроенные покупки и подписки»** (In-App Purchases and Subscriptions).
3. Нажмите кнопку **«Выбрать подписки»** (или синий плюс **«+»**).
4. Отметьте все 4 подписки (`pro.monthly`, `pro.annual`, `ai.monthly`, `ai.annual`) и нажмите **«Готово»**.
5. Нажмите **«Сохранить»** в правом верхнем углу страницы.
Теперь при отправке версии 1.0 на ревью в Apple уходит полный синхронизированный комплект: билд, метаданные и 4 подписки StoreKit 2! 🌹✨

---

## 🎤 ЭТАП 5: Разрешения Микрофона и Распознавания Речи (Apple 5.1.1)

В RoseTime встроен режим голосовой диктовки сообщений для мастеров, работающих в перчатках. Чтобы цензоры Apple гарантированно и без единого вопроса одобрили приложение:

### 5.1. Заметки для Проверяющего (App Review Notes)
На странице версии в App Store Connect найдите блок **«Сведения для проверки приложения»** (App Review Information) $\rightarrow$ поле **«Заметки»** (Notes). Вставьте официальное пояснение на английском языке:

```text
The microphone and speech recognition features (SFSpeechRecognizer) allow beauty professionals to dictate client bookings hands-free while working in gloves or during beauty procedures. 

Key Privacy Safeguards:
1. Microphone activates strictly upon explicit user tap on the mic button inside AI Assistant.
2. Audio is transcribed transiently in real-time via Apple's native Speech framework.
3. No audio files are ever saved, stored on device, or uploaded to any external servers.
4. If permission is denied, the app gracefully degrades to standard manual text input without blocking user workflow.
```

### 5.2. Анкета «Конфиденциальность приложения» (App Privacy Nutrition Labels)
В левом меню перейдите в раздел **«Конфиденциальность приложения»** (App Privacy):
* Вопрос: *«Собираете ли вы или ваши сторонние партнеры данные из этого приложения?»*
* Аудиоданные: **«Нет»** (так как аудио обрабатывается исключительно транзитно на процессоре устройства через нативный фреймворк Apple и не сохраняется/не отправляется во внешнюю сеть).
* Если Apple запрашивает декларацию API: укажите **«Функционал приложения» (App Functionality)**, с признаками:
  * *Связаны ли данные с личностью пользователя?* $\rightarrow$ **Нет (No)**.
  * *Используются ли данные для отслеживания?* $\rightarrow$ **Нет (No)**.

---

## 🏁 ЭТАП 6: Финальная Отправка на Модерацию (Submit for Review)

1. Убедитесь, что статус всех 4 подписок в группе: **«Готово к отправке»** (Ready to Submit).
2. На странице версии нажмите синюю кнопку **«Добавить для проверки»** (Add for Review) в правом верхнем углу.
3. На следующем экране подтвердите отсутствие нерегламентированного шифрования (ITSAppUsesNonExemptEncryption = NO) и нажмите **«Отправить на проверку»** (Submit to App Review).
4. Среднее время проверки Apple составляет от 12 до 24 часов. Вы получите email-уведомление от App Store Connect об успешном одобрении (Approved)! 🚀🌹
