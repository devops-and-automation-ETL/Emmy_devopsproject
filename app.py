from flask import Flask, jsonify
import requests
from datetime import datetime

app = Flask(__name__)

def fetch_weather():
    api_url = "https://opendata-download-metfcst.smhi.se/api/category/pmp3g/version/2/geotype/point/lon/18.0686/lat/59.3293/data.json"
    headers = {
        "Accept": "application/json",
        "User-Agent": "weather-app"
    }
    response = requests.get(api_url, headers=headers)
    if response.status_code == 200:
        return response.json()
    else:
        return {"error": "Failed to fetch data from SMHI API"}

@app.route('/')
def index():
    return "Welcome to the Weather App! Visit /weather to see the weather data."

@app.route('/weather')
def get_weather():
    weather_data = fetch_weather()
    return jsonify(weather_data)

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=80)
