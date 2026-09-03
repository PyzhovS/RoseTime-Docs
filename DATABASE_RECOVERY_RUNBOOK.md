# 🌹 RoseTime — Регламент Службы Поддержки: Восстановление Баз Данных (Database Recovery SOP & Runbook)

*(Select language / Выберите язык: [Русский](#русский) | [English](#english))*

---

<a name="русский"></a>
## 🇷🇺 Регламент Восстановления Данных Мастера (SOP / Runbook)

Данный документ является официальной рабочей инструкцией для инженеров службы технической поддержки RoseTime при обращении пользователя с файлом аварийного архива базы данных (`default.store.corrupt_<timestamp>`).

---

### 🏛 1. Общие Сведения и Архитектура Защиты (Store Safety Shield)
При сбое инициализации контейнера SwiftData (например, аппаратный сбой файловой системы iOS или повреждение lock-файла SQLite WAL) приложение RoseTime **не удаляет поврежденный файл**, а автоматически создает защитную копию:
```
<App_Sandbox>/Library/Application Support/default.store.corrupt_<timestamp>
<App_Sandbox>/Library/Application Support/default.store-wal.corrupt_<timestamp>
<App_Sandbox>/Library/Application Support/default.store-shm.corrupt_<timestamp>
```
Пользователь может отправить этот файл в службу поддержки через Telegram, WhatsApp или Email.

---

### 💻 2. Пошаговая Инструкция для Инженера Поддержки (macOS)

#### Шаг 1: Проверка целостности файла
Откройте **Терминал** на macOS и проверьте файл:
```bash
sqlite3 default.store.corrupt_1787679000 "PRAGMA integrity_check;"
```

#### Шаг 2: Восстановление структуры базы утилитой `.recover`
Встроенная системная утилита SQLite `.recover` считывает все сохранившиеся B-деревья даже из поврежденных секторов:
```bash
sqlite3 default.store.corrupt_1787679000 ".recover" | sqlite3 recovered.sqlite
```

#### Шаг 3: Экспорт данных в чистый JSON через Python
Используйте скрипт `recover_rosetime.py` для формирования читаемого файла восстановления:

```python
import sqlite3
import json
from datetime import datetime, timedelta

def recover_rosetime_data(sqlite_file: str, output_json: str = "rosetime_restored.json"):
    conn = sqlite3.connect(sqlite_file)
    cursor = conn.cursor()
    
    # 1. Извлечение Клиентов
    clients = []
    try:
        for row in cursor.execute("SELECT ZNAME, ZPHONE, ZNOTES FROM ZCLIENT"):
            clients.append({
                "name": row[0] or "",
                "phone": row[1] or "",
                "notes": row[2] or ""
            })
    except Exception as e:
        print(f"Предупреждение при чтении клиентов: {e}")
        
    # 2. Извлечение Услуг
    services = []
    try:
        for row in cursor.execute("SELECT ZNAME, ZPRICE, ZDURATIONMINUTES FROM ZSERVICEITEM"):
            services.append({
                "name": row[0] or "",
                "price": row[1] or 0.0,
                "durationMinutes": int(row[2] or 60)
            })
    except Exception as e:
        print(f"Предупреждение при чтении услуг: {e}")
        
    # 3. Извлечение Записей (Конвертация Apple Cocoa Epoch -> ISO 8601)
    appointments = []
    cocoa_epoch = datetime(2001, 1, 1)
    try:
        for row in cursor.execute("SELECT ZSERVICENAME, ZDATE, ZPRICE, ZDURATIONMINUTES, ZNOTES FROM ZAPPOINTMENT"):
            appt_date = cocoa_epoch + timedelta(seconds=row[1]) if row[1] else None
            appointments.append({
                "serviceName": row[0] or "",
                "date": appt_date.strftime("%Y-%m-%d %H:%M") if appt_date else "",
                "price": row[2] or 0.0,
                "durationMinutes": int(row[3] or 60),
                "notes": row[4] or ""
            })
    except Exception as e:
        print(f"Предупреждение при чтении записей: {e}")
        
    result = {
        "version": "2026.1",
        "recoveredAt": datetime.now().isoformat(),
        "clientsCount": len(clients),
        "appointmentsCount": len(appointments),
        "clients": clients,
        "services": services,
        "appointments": appointments
    }
    
    with open(output_json, "w", encoding="utf-8") as f:
        json.dump(result, f, ensure_ascii=False, indent=2)
        
    print(f"✅ Успешно спасено: {len(clients)} клиентов, {len(services)} услуг, {len(appointments)} записей!")

if __name__ == "__main__":
    import sys
    db = sys.argv[1] if len(sys.argv) > 1 else "recovered.sqlite"
    recover_rosetime_data(db)
```

---

### 📲 3. Передача Восстановленных Данных Мастеру

1. **Способ А (JSON-импорт):**
   * Отправьте файл `rosetime_restored.json` мастеру в мессенджер.
   * Мастер нажимает на файл $\to$ выбирает **«Поделиться»** $\to$ **RoseTime**.
   * Приложение автоматически импортирует записи и клиентов.

2. **Способ Б (Прямая замена через Finder / iTunes):**
   * Переименуйте `recovered.sqlite` в `default.store`.
   * Мастер подключает iPhone к Mac/ПК через кабель.
   * В Finder (или iTunes) $\to$ раздел «Файлы» $\to$ папка **RoseTime** $\to$ заменяет файл `default.store`.
   * При следующем запуске приложения все данные восстанавливаются на 100%.

---
---

<a name="english"></a>
## 🇬🇧 Database Recovery SOP & Runbook for Support Team

This document is the official standard operating procedure for RoseTime technical support engineers when handling corrupt database archive files (`default.store.corrupt_<timestamp>`).

---

### 🏛 1. Store Safety Shield Overview
When SwiftData fails to initialize a persistent container (e.g. filesystem lock or schema migration discrepancy), RoseTime does not destroy the corrupt store. Instead, it archives it under:
```
<App_Sandbox>/Library/Application Support/default.store.corrupt_<timestamp>
```
The user exports this diagnostic file to technical support.

---

### 💻 2. macOS Recovery Procedure

#### Step 1: Check File Integrity
```bash
sqlite3 default.store.corrupt_1787679000 "PRAGMA integrity_check;"
```

#### Step 2: Extract B-Trees via `.recover`
```bash
sqlite3 default.store.corrupt_1787679000 ".recover" | sqlite3 recovered.sqlite
```

#### Step 3: Run Python Export Tool
```bash
python3 recover_rosetime.py recovered.sqlite
```

---

### 📲 3. Delivering Restored Data to Master

1. **Method A (JSON Direct Ingestion):**
   * Transmit `rosetime_restored.json` to the client.
   * Client taps file $\to$ **Share** $\to$ **RoseTime**. Data is imported into SwiftData.

2. **Method B (File Replacement via Finder / iTunes):**
   * Rename `recovered.sqlite` to `default.store`.
   * Connect iPhone via USB $\to$ Finder / iTunes $\to$ **Files** $\to$ **RoseTime** $\to$ replace store file.

---
<p align="center">
  <i>RoseTime Support Team — Standard Operating Procedure 2026. 🌹✨</i>
</p>
