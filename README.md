# Smart Building Climate Monitor API

Eine RESTful API zur Erfassung und Verwaltung von Raumklima-Daten (Temperatur, Luftfeuchtigkeit) in Smart-Building-Umgebungen. 

## Features
- **Raumklima-Monitoring:** Endpunkte zum Abrufen und Speichern von Sensordaten.
- **Datenbank-Anbindung:** Leichtgewichtige Persistenz mit SQLite.
- **Automatische Dokumentation:** Interaktive API-Spezifikation via Swagger UI.

## Tech Stack
- **Sprache:** Python 3.12+
- **Framework:** FastAPI
- **Datenbank:** SQLite
- **Webserver:** Uvicorn

## Schnelleinrichtung (Local Setup)

1.  Repository klonen:

    ```bash
    git clone [https://github.com/t-skjellet/smart-building-monitor.git](https://github.com/t-skjellet/smart-building-monitor.git)
    cd smart-building-monitor

2.  Virtuelle Umgebung erstellen und aktivieren:

    python -m venv venv
    source venv/bin/activate  # Unter Windows: venv\Scripts\activate

3.  Abhängigkeiten installieren:

    ```bash
    pip install fastapi uvicorn

4.  Server starten:

    ```bash
    uvicorn main:app --reload

5.  Die interaktive Dokumentation aufrufen:

    Öffne http://127.0.0.1:8000/docs im Browser.
