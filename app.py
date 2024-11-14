from flask import Flask, jsonify
import requests

app = Flask(__name__)

@app.route("/")
def fetch_weather():
    longitude = 18.0686
    latitude = 59.3293
    api_url = f"https://opendata-download-metfcst.smhi.se/api/category/pmp3g/version/2/geotype/point/lon/{longitude}/lat/{latitude}/data.json"
    headers = {
        "Accept": "application/json",
        "User-Agent": "weather-app",
    }
    response = requests.get(api_url, headers=headers)
    if response.status_code == 200:
        data = response.json()
        forecast_list = []
        parameter_mapping = {
            "t": "Temperature (°C)",
            "ws": "Wind speed (m/s)",
            "wd": "Wind direction (°)",
            "r": "Relative humidity (%)",
            "msl": "Air pressure (hPa)",
            "vis": "Visibility (km)",
            "pcat": "Precipitation category",
            "pmean": "Mean precipitation (mm/h)",
            "tstm": "Thunder probability (%)",
            "Wsymb2": "Weather symbol"
        }
        for time_series in data.get("timeSeries", []):
            valid_time = time_series["validTime"]
            parameters = time_series["parameters"]
            data_dict = {"validTime": valid_time}
            for param in parameters:
                if param["name"] in parameter_mapping:
                    name = parameter_mapping[param["name"]]
                    value = param["values"][0]
                    data_dict[name] = value
            forecast_list.append(data_dict)
        return jsonify(forecast_list)
    else:
        return "Failed to fetch data from SMHI API", response.status_code

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=80)
