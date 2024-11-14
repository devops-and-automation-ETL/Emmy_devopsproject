from flask import Flask, jsonify
import requests
from datetime import datetime

app = Flask(__name__)

@app.route("/")
def fetch_weather():
    try:
        api_url = "https://opendata-download-metobs.smhi.se/api/version/latest/parameter/1/station/159880/period/latest-hour/data.json"
        response = requests.get(api_url)
        response.raise_for_status()  # Kontrollera om förfrågan lyckades

        data = response.json()
        temperature = data["value"][0]["value"]
        wind_speed = next((item["value"] for item in data["value"] if item["name"] == "ws"), "N/A")
        wind_direction = next((item["value"] for item in data["value"] if item["name"] == "wd"), "N/A")
        precipitation = next((item["value"] for item in data["value"] if item["name"] == "pmax"), "N/A")

        weather_info = {
            "temperature": f"{temperature}°C",
            "precipitation": f"{precipitation} mm",
            "wind_speed": f"{wind_speed} m/s",
            "wind_direction": f"{wind_direction}°",
            "location": "Stockholm",
            "date": datetime.now().strftime("%Y-%m-%d")
        }

        return jsonify(weather_info)

    except requests.exceptions.RequestException as e:
        # Om ett API-fel uppstår, returnera ett felmeddelande
        return jsonify({"error": f"Failed to fetch data from SMHI API: {e}"})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=80)
