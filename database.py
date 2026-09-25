import sqlite3

def init_db():
    # Verbindet mit der Datenbank-Datei (wird automatisch erstellt, falls nicht vorhanden)
    conn = sqlite3.connect("climate_data.db")
    cursor = conn.cursor()
    
    # Tabelle für die Telemetriedaten anlegen
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS sensor_readings (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            location TEXT NOT NULL,
            temperature REAL NOT NULL,
            humidity REAL NOT NULL,
            status TEXT NOT NULL,
            timestamp DATETIME DEFAULT CURRENT_TIMESTAMP
        )
    """)
    
    conn.commit()
    conn.close()
    print("Datenbank für Gebäudetechnik erfolgreich initialisiert!")

if __name__ == "__main__":
    init_db()