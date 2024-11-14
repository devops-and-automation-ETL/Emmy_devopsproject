import requests
import os

def fetch_weather():
    api_url = "https://opendata-download-metfcst.smhi.se/api/category/pmp3g/version/2/geotype/point/lon/18.0686/lat/59.3293/data.json"
    headers = {
        "Accept": "application/json",
        "User-Agent": "weather-app",
        "Authorization": f"Bearer {os.getenv('SMHI_API_KEY')}"
    }
    response = requests.get(api_url, headers=headers)
    if response.status_code == 200:
        return response.json()
    else:
        raise Exception("Failed to fetch data from SMHI API")

if __name__ == "__main__":
    weather_data = fetch_weather()
    print("Weather data:", weather_data)
