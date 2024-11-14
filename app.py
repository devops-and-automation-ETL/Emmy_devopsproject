from flask import Flask, jsonify
import requests
from datetime import datetime

app = Flask(__name__)

@app.route("/")
def fetch_weather():
    api_url = "https://opendata-download-metobs.smhi.se/api/version/latest/parameter/1/station/159880/period/latest-hour/data.json"
    response = requests.get(api_url)
    if response.status_code == 200:
        data = response.json()
        
        weather_info = {
            "temperature": f"{next(item['value'] for item in data['value'] if item['name'] == 't')}°C",
            "wind_speed": f"{next(item['value'] for item in data['value'] if item['name'] == 'ws')} m/s",
            "wind_direction": f"{next(item['value'] for item in data['value'] if item['name'] == 'wd')}°",
            "air_pressure": f"{next(item['value'] for item in data['value'] if item['name'] == 'msl')} hPa",
            "humidity": f"{next(item['value'] for item in data['value'] if item['name'] == 'r')}%",
            "precipitation": f"{next(item['value'] for item in data['value'] if item['name'] == 'pmax')} mm",
            "cloud_cover": f"{next(item['value'] for item in data['value'] if item['name'] == 'tcc_mean')}%",
            "visibility": f"{next(item['value'] for item in data['value'] if item['name'] == 'vis')} km",
            "thunder_probability": f"{next(item['value'] for item in data['value'] if item['name'] == 'tstm')}%",
            "solar_radiation": f"{next(item['value'] for item in data['value'] if item['name'] == 'global_rad')} W/m²",
            "location": "Stockholm",
            "date": datetime.now().strftime("%Y-%m-%d")
        }
        return jsonify(weather_info)
    else:
        return jsonify({"error": "Failed to fetch data from SMHI API"}), response.status_code

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=80)
