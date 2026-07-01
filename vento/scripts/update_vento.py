import json
import random
from pathlib import Path
from datetime import datetime

STATIONS = [
    "Desenzano",
    "Peschiera",
    "Salò",
    "Toscolano",
    "Gargnano",
    "Campione del Garda",
    "Malcesine"
]

DIRECTIONS = [
    "N", "NNE", "NE", "ENE",
    "E", "ESE", "SE", "SSE",
    "S", "SSW", "SW", "WSW",
    "W", "WNW", "NW", "NNW"
]


def fake_station(name):
    wind = round(random.uniform(1, 22), 1)
    gust = round(wind + random.uniform(2, 12), 1)

    return {
        "name": name,
        "wind": wind,
        "dir": random.choice(DIRECTIONS),
        "max": gust,
        "maxTime": datetime.now().strftime("%H:%M"),
        "last": datetime.now().strftime("%d-%m-%Y %H:%M")
    }


def main():

    stations = [fake_station(s) for s in STATIONS]

    output = {
        "updated": datetime.now().strftime("%d-%m-%Y %H:%M"),
        "stations": stations
    }

    repo_root = Path(__file__).resolve().parents[2]

    json_file = repo_root / "vento" / "vento.json"

    with open(json_file, "w", encoding="utf-8") as f:
        json.dump(output, f, indent=2, ensure_ascii=False)

    print(f"Aggiornato {json_file}")


if __name__ == "__main__":
    main()
