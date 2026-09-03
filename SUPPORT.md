# 💬 Центр Поддержки и Часто Задаваемые Вопросы / RoseTime Support & FAQ

*(Select language / Выберите язык: [Русский](#русский) | [English](#english))*

---

<a name="русский"></a>
## 🇷🇺 Служба поддержки пользователей RoseTime

Если у вас возникли вопросы по работе приложения, предложения по улучшению функционала или технические сложности, наша служба поддержки готова оперативно вам помочь.

### 📬 Контакты для связи
* **Официальный Email:** [pyzhovs@icloud.com](mailto:pyzhovs@icloud.com)
* **Разработчик:** Сергей Пыжов
* **Время ответа:** Обычно в течение 24 часов в рабочие дни.

---

### ❓ Часто задаваемые вопросы (FAQ)

#### 1. Где хранятся данные моих клиентов и выручка?
Все данные (список клиентов, история визитов, заметки и финансовая статистика) сохраняются **исключительно локально на вашем iPhone** с использованием защищенной базы данных Apple SwiftData. Ваши данные никогда не выгружаются на сторонние серверы и не передаются третьим лицам.

#### 2. Как работает ИИ-Ассистент и безопасен ли он?
ИИ-Ассистент использует защищенный серверный прокси и модель Google Gemini 3.1 Flash Lite. Перед отправкой запроса номера телефонов клиентов маскируются (`[PHONE]`), а имена клиентов заменяются анонимными токенами. Никакие персональные данные клиентов не сохраняются в облаке и не используются для обучения нейросетей. При отсутствии интернета приложение автоматически переключается на встроенный офлайн-мозг.

#### 3. Как защитить доходы от клиентов на рабочем месте?
Включите функцию **«Шторка приватности» (Face ID)** в настройках Профиля. При скрытии приложения или активации шторки финансовые цифры маскируются, и для их просмотра потребуется авторизация через Face ID или Touch ID.

#### 4. Как перенести приложение на новый iPhone?
При стандартном переносе данных iOS с одного iPhone на другой (через «Быстрое начало» или резервную копию iCloud/Mac) вся локальная база данных SwiftData автоматически и бесшовно переносится на ваше новое устройство.

#### 5. Как удалить все данные из приложения?
Откройте вкладку «Профиль» $\to$ «Правовая информация и управление данными» $\to$ нажмите **«Сбросить все данные»**. Вся база данных будет безвозвратно удалена с устройства.

#### 6. Что делать при аварийном сбое базы данных?
Приложение оснащено системой **Store Safety Shield** — при любом сбое базы данных создается защитная копия `.corrupt_<timestamp>`. Обратитесь в службу поддержки (`pyzhovs@icloud.com`), и инженер восстановит все ваши записи согласно [Регламенту восстановления (Runbook)](DATABASE_RECOVERY_RUNBOOK.md).

---
---

<a name="english"></a>
## 🇬🇧 RoseTime User Support & Help Center

If you have questions, feedback, feature requests, or technical issues with RoseTime, we are here to assist you.

### 📬 Contact Us
* **Official Support Email:** [pyzhovs@icloud.com](mailto:pyzhovs@icloud.com)
* **Lead Developer:** Sergey Pyzhov
* **Response Time:** Typically within 24 hours on business days.

---

### ❓ Frequently Asked Questions (FAQ)

#### 1. Where are my client database and revenue metrics stored?
All records (client roster, appointment logs, color formulas, and revenue stats) are stored **strictly on your iPhone** in an encrypted Apple SwiftData container. Your business data is never uploaded to external commercial clouds or sold to third parties.

#### 2. How does the AI Assistant work and is it safe?
The smart assistant routes queries via a secure Cloudflare Edge proxy to Google Gemini 3.1 Flash Lite. Before transmission, all phone numbers are scrubbed with `[PHONE]` and names are converted into anonymous pseudonyms. Zero client PI is retained in the cloud or used to train models. Offline NLP parsers take over when internet is unavailable.

#### 3. How do I protect earnings from clients glancing at my screen?
Enable the **Face ID Privacy Shield** in Profile Settings. Financial figures will be immediately shrouded and require Face ID or Touch ID authentication to unmask.

#### 4. How do I migrate my database to a new iPhone?
During standard Apple iOS device-to-device migration (via Quick Start, encrypted iCloud backup, or Mac backup), your SwiftData container will automatically transfer to your new iPhone without any data loss.

#### 5. How can I completely erase my application data?
Navigate to Profile $\to$ Data Management $\to$ select **"Reset All Data"**. This permanently and irreversibly purges the SwiftData database and resets app preferences.

#### 6. What if my database experiences an emergency crash?
RoseTime features **Store Safety Shield** — any crash archives your data into `.corrupt_<timestamp>`. Reach out to support (`pyzhovs@icloud.com`), and an engineer will restore your client and appointment logs per the [Database Recovery Runbook](DATABASE_RECOVERY_RUNBOOK.md).

---
<p align="center">
  <i>RoseTime Support Team — We are here to help your beauty business thrive. 💅✨</i>
</p>
