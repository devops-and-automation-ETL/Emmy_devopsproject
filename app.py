from flask import Flask, jsonify
import requests
import os

app = Flask(__name__)

@app.route("/")
def fetch_weather():
    # API URL för att hämta senaste temperaturen
    api_url = "https://opendata-download-metobs.smhi.se/api/version/latest/parameter/1/station/159880/period/latest-hour/data.json"
    headers = {
        "Accept": "application/json",
        "User-Agent": "weather-app",
    }
    response = requests.get(api_url, headers=headers)
    if response.status_code == 200:
        data = response.json()
        # Extrahera temperaturvärdet
        temperature = data["value"][0]["value"]
        return jsonify({"temperature": f"{temperature}°C"})
    else:
        return jsonify({"error": "Failed to fetch data from SMHI API"}), response.status_code

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=80)
