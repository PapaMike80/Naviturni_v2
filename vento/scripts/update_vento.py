import json
import requests
from datetime import datetime

# -----------------------------
# CONFIG STAZIONI
# -----------------------------
STATIONS = [
    {
        "name": "Desenzano",
        "url": "https://www.meteopassione.com/stazioni/desenzano",
        "type": "manual_demo"
    },
    {
        "name": "Peschiera",
        "url": "https://www.meteonetwork.eu/it/weather-station/vnt259-stazione-meteorologica-di-peschiera-del-garda",
        "type": "manual_demo"
    },
    {
        "name": "Salò",
        "url": "https://www.meteopassione.com/stazioni/salo-lago-di-garda",
        "type": "manual_demo"
    },
    {
        "name": "Toscolano",
        "url": "https://www.meteopassione.com/stazioni/museo-della-carta-toscolano-maderno",
        "type": "manual_demo"
    },
    {
        "name": "Gargnano",
        "url": "https://www.circolovelagargnano.it/",
        "type": "manual_demo"
    },
    {
        "name": "Campione del Garda",
        "url": "https://www.meteopassione.com/stazioni/campione",
        "type": "manual_demo"
    },
    {
        "name": "Malcesine",
        "url": "https://stazioni.meteoproject.it/dati/malcesine/",
        "type": "manual_demo"
    }
]

# -----------------------------
# DEMO PARSER
# (qui in step 3 diventa reale scraping)
# -----------------------------
def get_fake_data(name):
    import random

    wind = round(random.uniform(1, 22), 1)
    max_wind = round(wind + random.uniform(2, 15), 1)

    dirs = ["N","NE","E","SE","S","SW","W","NW","NNE","ENE","ESE","SSE"]
    direction = random.choice(dirs)

    return {
        "name": name,
        "wind": wind,
        "dir": direction,
        "max": max_wind,
        "maxTime": datetime.now().strftime("%H:%M"),
        "last": datetime.now().strftime("%d-%m-%Y %H:%M")
    }

# -----------------------------
# BUILD JSON
# -----------------------------
def build():
    stations_data = []

    for s in STATIONS:
        try:
            # STEP 2: simulazione dati
            data = get_fake_data(s["name"])
            stations_data.append(data)

        except Exception as e:
            print("Errore:", s["name"], e)

    output = {
        "updated": datetime.now().strftime("%d-%m-%Y %H:%M"),
        "stations": stations_data
    }

    with open("vento.json", "w", encoding="utf-8") as f:
        json.dump(output, f, indent=2, ensure_ascii=False)

    print("vento.json aggiornato")

if __name__ == "__main__":
    build()
