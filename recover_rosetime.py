#!/usr/bin/env python3
"""
RoseTime Database Recovery Tool (Support Team)
Extracts Clients, Services, and Appointments from a recovered SQLite database into JSON.
"""

import sys
import os
import sqlite3
import json
from datetime import datetime, timedelta

def recover_rosetime_data(sqlite_file: str, output_json: str = "rosetime_restored.json"):
    if not os.path.exists(sqlite_file):
        print(f"❌ Ошибка: Файл '{sqlite_file}' не найден.")
        sys.exit(1)
        
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
        print(f"⚠️ Предупреждение при чтении ZCLIENT: {e}")
        
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
        print(f"⚠️ Предупреждение при чтении ZSERVICEITEM: {e}")
        
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
        print(f"⚠️ Предупреждение при чтении ZAPPOINTMENT: {e}")
        
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
    print(f"📁 Файл сохранен: {output_json}")

if __name__ == "__main__":
    db = sys.argv[1] if len(sys.argv) > 1 else "recovered.sqlite"
    out = sys.argv[2] if len(sys.argv) > 2 else "rosetime_restored.json"
    recover_rosetime_data(db, out)
