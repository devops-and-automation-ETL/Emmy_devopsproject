
from flask import Flask, jsonify
import requests

app = Flask(__name__)

@app.route("/")
def fetch_weather():
    api_url = "https://opendata-download-metfcst.smhi.se/api/category/pmp3g/version/2/geotype/point/lon/18.0686/lat/59.3293/data.json"
    headers = {
        "Accept": "application/json",
        "User-Agent": "weather-app",
    }
    response = requests.get(api_url, headers=headers)
    if response.status_code == 200:
        return jsonify(response.json())
    else:
        return jsonify({"error": "Failed to fetch data from SMHI API"}), response.status_code

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=80)
