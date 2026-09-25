from fastapi import FastAPI
from pydantic import BaseModel
import sqlite3
from database import init_db

# 1. Datenbank beim Start direkt vorbereiten
init_db()

app = FastAPI(title="Smart-Building Climate Monitor")

# 2. Datenstruktur für eingehende Sensordaten (Pydantic-Modell)
class SensorData(BaseModel):
    location: str        # z. B. "Serverraum 1" oder "Labor B"
    temperature: float   # z. B. 22.5
    humidity: float      # z. B. 45.0

# 3. Hilfsfunktion für den Statuscheck 
def evaluate_status(temp: float) -> str:
    if temp > 28.0:
        return "CRITICAL_HOT"
    elif temp < 15.0:
        return "CRITICAL_COLD"
    return "OK"

# 4. API-Endpunkt: Sensordaten empfangen und in SQLite speichern
@app.post("/api/v1/telemetry")
def receive_telemetry(data: SensorData):
    status = evaluate_status(data.temperature)
    
    conn = sqlite3.connect("climate_data.db")
    cursor = conn.cursor()
    cursor.execute(
        "INSERT INTO sensor_readings (location, temperature, humidity, status) VALUES (?, ?, ?, ?)",
        (data.location, data.temperature, data.humidity, status)
    )
    conn.commit()
    conn.close()
    
    return {
        "message": "Daten erfolgreich gespeichert",
        "status": status,
        "data": data
    }

# 5. API-Endpunkt: Alle Messwerte auslesen
@app.get("/api/v1/telemetry")
def get_all_telemetry():
    conn = sqlite3.connect("climate_data.db")
    cursor = conn.cursor()
    cursor.execute("SELECT id, location, temperature, humidity, status, timestamp FROM sensor_readings ORDER BY id DESC")
    rows = cursor.fetchall()
    conn.close()
    
    return {"readings": rows}